from flask import Flask, render_template, abort
from seo_data import SEO_DATA, get_class_seo
from seo import build_seo, organization_schema, website_schema, webpage_schema
from config import CTA_LINKS, tracked_app_link
from faq_data import FAQ_DATA, build_faq_schema
from blog_data import get_all_posts, get_post_by_slug, get_related_posts, get_prev_next_posts, get_featured_post
from flask import Response

app = Flask(__name__)

@app.context_processor
def inject_cta_links():
    return {
        "CTA_LINKS": CTA_LINKS,
        "tracked_app_link": tracked_app_link
    }

CLASS_DATA = {
    "9": {
        "badge": "CBSE CLASS 9",
        "heading": "Build strong foundations with AI-powered learning.",
        "subheading": "Class 9 is where students begin strengthening core concepts for higher classes.",
        "focus": "Strong fundamentals",
        "description": "Genelis helps Class 9 students build clarity across key subjects with structured learning guidance, practice support, and revision direction.",
        "subjects": ["Mathematics", "Science", "Social Science", "English"],
        "faqs": [
            "Is Genelis useful for Class 9 students?",
            "Which subjects are supported for Class 9?",
            "Can Genelis help with concept clarity?"
        ]
    },
    "10": {
        "badge": "CBSE CLASS 10",
        "heading": "Prepare for board exams with more clarity.",
        "subheading": "Class 10 is a major academic milestone where structured revision and focused practice become essential.",
        "focus": "Board-focused preparation",
        "description": "Genelis helps Class 10 students organize notes, practice questions, mock tests, and revision guidance into one connected learning experience.",
        "subjects": ["Mathematics", "Science", "Social Science", "English"],
        "faqs": [
            "Is Genelis aligned for Class 10 board preparation?",
            "Can students use Genelis for revision?",
            "Does Genelis support mock test practice?"
        ]
    },
    "11": {
        "badge": "CBSE CLASS 11",
        "heading": "Go deeper into concepts with structured AI guidance.",
        "subheading": "Class 11 introduces deeper subject learning and requires stronger conceptual understanding.",
        "focus": "Deeper conceptual learning",
        "description": "Genelis supports Class 11 students as they transition into advanced subjects with guided study flows and smarter revision support.",
        "subjects": ["Physics", "Chemistry", "Biology", "Mathematics", "Economics", "Business Studies", "Accountancy", "English"],
        "faqs": [
            "Which streams does Genelis support for Class 11?",
            "Can Genelis help with difficult concepts?",
            "Is Genelis useful for science and commerce students?"
        ]
    },
    "12": {
        "badge": "CBSE CLASS 12",
        "heading": "Prepare confidently for important academic outcomes.",
        "subheading": "Class 12 requires consistency, revision discipline, and focused practice across the year.",
        "focus": "Exam-ready preparation",
        "description": "Genelis helps Class 12 students prepare with structured study support, practice direction, and performance-focused revision guidance.",
        "subjects": ["Physics", "Chemistry", "Biology", "Mathematics", "Economics", "Business Studies", "Accountancy", "English"],
        "faqs": [
            "Can Genelis help with Class 12 board preparation?",
            "Does Genelis support revision planning?",
            "Can students track weak areas?"
        ]
    }
}


def get_classes_data():
    return [
        {
            "id": "9",
            "name": "Class 9",
            "headline": "Build strong foundations.",
            "description": "Support for Mathematics, Science, Social Science, and English."
        },
        {
            "id": "10",
            "name": "Class 10",
            "headline": "Prepare with more clarity.",
            "description": "Structured support for board-focused learning and revision."
        },
        {
            "id": "11",
            "name": "Class 11",
            "headline": "Go deeper into concepts.",
            "description": "Explore subject-wise learning across science, commerce, and humanities."
        },
        {
            "id": "12",
            "name": "Class 12",
            "headline": "Prepare for important outcomes.",
            "description": "Focused learning support for school exams and future academic goals."
        }
    ]


def render_seo_template(template_name, seo_key, faq_key=None, **kwargs):
    seo = build_seo(SEO_DATA[seo_key])


    schemas = [
        organization_schema(),
        website_schema(),
        webpage_schema(seo)
    ]

    faq = None

    if faq_key:
        faq = FAQ_DATA[faq_key]
        schemas.append(build_faq_schema(faq))

    return render_template(
        template_name,
        seo=seo,
        schemas=schemas,
        faq=faq,
        **kwargs
    )


@app.route("/")
def home():
    return render_seo_template("index.html", "home", faq_key="home")


@app.route("/about")
def about():
    return render_seo_template("about.html", "about", faq_key="about")


@app.route("/learning-system")
def learning_system():
    return render_seo_template(
        "learning-system.html",
        "learning_system",
        faq_key="learning_system"
    )


@app.route("/classes")
def classes():
    return render_seo_template(
        "classes.html",
        "classes",
        faq_key="classes",
        classes_data=get_classes_data()
    )


@app.route("/classes/<class_id>")
def class_detail(class_id):
    class_info = CLASS_DATA.get(class_id)

    if not class_info:
        return "Class not found", 404

    class_seo = build_seo(get_class_seo(class_id, class_info))

    faq_key = f"class_{class_id.split('-')[-1]}"
    faq = None

    schemas = [
        organization_schema(),
        website_schema(),
        webpage_schema(class_seo)
    ]

    if faq_key:
        faq = FAQ_DATA[faq_key]
        schemas.append(build_faq_schema(faq))

    return render_template(
        "class.html",
        seo=class_seo,
        schemas=schemas,
        class_info=class_info,
        faq=faq
    )


@app.route("/pricing")
def pricing():
    return render_seo_template("pricing.html", "pricing", faq_key="pricing")


@app.route("/blog")
def blog():

    posts = get_all_posts()

    featured_post = get_featured_post()

    return render_template(
        "blog.html",
        posts=posts,
        featured_post=featured_post
    )


@app.route("/contact")
def contact():
    return render_seo_template("contact.html", "contact", faq_key="contact")


@app.route("/robots.txt")
def robots_txt():
    return render_template("robots.txt"), 200, {"Content-Type": "text/plain"}


@app.route("/sitemap.xml")
def sitemap():

    BASE_URL = "https://genelis.in"

    sitemap_pages = [

        {
            "url": f"{BASE_URL}/",
            "changefreq": "weekly",
            "priority": "1.0"
        },

        {
            "url": f"{BASE_URL}/about",
            "changefreq": "monthly",
            "priority": "0.8"
        },

        {
            "url": f"{BASE_URL}/learning-system",
            "changefreq": "monthly",
            "priority": "0.9"
        },

        {
            "url": f"{BASE_URL}/pricing",
            "changefreq": "monthly",
            "priority": "0.8"
        },

        {
            "url": f"{BASE_URL}/classes",
            "changefreq": "weekly",
            "priority": "0.9"
        },

        {
            "url": f"{BASE_URL}/blog",
            "changefreq": "weekly",
            "priority": "0.8"
        },

        {
            "url": f"{BASE_URL}/contact",
            "changefreq": "yearly",
            "priority": "0.6"
        }

    ]

    # Automatically include all class pages

    for class_id in CLASS_DATA.keys():

        sitemap_pages.append({

            "url": f"{BASE_URL}/classes/{class_id}",

            "changefreq": "weekly",

            "priority": "0.8"

        })

    return (
        render_template(
            "sitemap.xml",
            sitemap_pages=sitemap_pages
        ),
        200,
        {
            "Content-Type": "application/xml"
        },
    )


@app.route("/terms")
def terms():
    return render_seo_template("legal/terms.html", "terms")


@app.route("/privacy")
def privacy():
    return render_seo_template("legal/privacy.html", "privacy")


@app.route("/cookies")
def cookies():
    return render_seo_template("legal/cookies.html", "cookies")


@app.route("/refund")
def refund():
    return render_seo_template("legal/refund.html", "refund")


@app.route("/grievance")
def grievance():
    return render_seo_template("legal/grievance.html", "grievance")


@app.route("/copyright")
def copyright():
    return render_seo_template("legal/copyright.html", "copyright")


@app.route("/childsafety")
def childsafety():
    return render_seo_template("legal/childsafety.html", "childsafety")


@app.route("/responsibleAI")
def responsibleAI():
    return render_seo_template("legal/responsibleAI.html", "responsibleAI")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.route("/blog/<slug>")
def blog_post(slug):
    post = get_post_by_slug(slug)

    if post is None:
        abort(404)

    related_posts = get_related_posts(slug)

    previous_post, next_post = get_prev_next_posts(slug)

    return render_template(
        "blog_post.html",
        post=post,
        related_posts=related_posts,
        previous_post=previous_post,
        next_post=next_post
    )
@app.route("/blog-sitemap.xml")
def blog_sitemap():

    posts = get_all_posts()

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

    for post in posts:

        xml += f"""
    <url>
        <loc>https://genelis.in/blog/{post['slug']}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.90</priority>
    </url>
"""

    xml += "</urlset>"

    return Response(xml, mimetype="application/xml")

@app.route("/sitemap.xml")
def main_sitemap():

    static_pages = [
        "",
        "about",
        "classes",
        "learning-system",
        "pricing",
        "blog",
        "contact"
    ]

    posts = get_all_posts()

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

    for page in static_pages:
        xml += f"""
    <url>
        <loc>https://genelis.in/{page}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.80</priority>
    </url>
"""

    for post in posts:
        xml += f"""
    <url>
        <loc>https://genelis.in/blog/{post['slug']}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.90</priority>
    </url>
"""

    xml += "</urlset>"

    return Response(xml, mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)