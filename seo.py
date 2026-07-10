from flask import request


SITE_NAME = "Genelis"
SITE_URL = "https://genelis.in"
DEFAULT_OG_IMAGE = "/static/og/genelis-og-image.png"
ORGANIZATION_LOGO = "/static/icons/icon-512.png"


def absolute_url(path):
    """
    Converts a relative path into a complete Genelis URL.
    Leaves already absolute URLs unchanged.
    """
    if not path:
        return SITE_URL

    if path.startswith(("http://", "https://")):
        return path

    if not path.startswith("/"):
        path = f"/{path}"

    return f"{SITE_URL}{path}"


def build_seo(seo_data):
    """
    Builds complete SEO metadata for a page.
    """

    path = seo_data.get("path", request.path)

    if not path.startswith("/"):
        path = f"/{path}"

    canonical_url = absolute_url(path)

    title = seo_data.get("title", SITE_NAME)

    description = seo_data.get(
        "description",
        "Genelis is an AI-powered learning platform for CBSE and NCERT students."
    )

    og_image = absolute_url(
        seo_data.get("og_image", DEFAULT_OG_IMAGE)
    )

    return {
        "title": title,
        "description": description,
        "keywords": ", ".join(seo_data.get("keywords", [])),
        "canonical": canonical_url,
        "og_title": seo_data.get("og_title", title),
        "og_description": seo_data.get(
            "og_description",
            description
        ),
        "og_url": canonical_url,
        "og_image": og_image,
        "og_type": seo_data.get("og_type", "website"),
        "twitter_card": seo_data.get(
            "twitter_card",
            "summary_large_image"
        ),
        "robots": seo_data.get("robots", "index, follow")
    }


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE_URL}/#organization",
        "name": SITE_NAME,
        "url": SITE_URL,
        "logo": {
            "@type": "ImageObject",
            "url": absolute_url(ORGANIZATION_LOGO)
        },
        "description": (
            "Genelis is an AI-powered learning platform "
            "for CBSE and NCERT students."
        )
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "name": SITE_NAME,
        "url": SITE_URL,
        "description": (
            "AI-powered learning platform for CBSE "
            "and NCERT students."
        ),
        "publisher": {
            "@id": f"{SITE_URL}/#organization"
        }
    }


def webpage_schema(seo, page_type="WebPage"):
    return {
        "@context": "https://schema.org",
        "@type": page_type,
        "@id": f"{seo['canonical']}#webpage",
        "name": seo["title"],
        "description": seo["description"],
        "url": seo["canonical"],
        "isPartOf": {
            "@id": f"{SITE_URL}/#website"
        },
        "about": {
            "@id": f"{SITE_URL}/#organization"
        }
    }


def breadcrumb_schema(items):
    """
    items example:
    [
        {"name": "Home", "url": "/"},
        {"name": "Blog", "url": "/blog"},
        {"name": "Article Title", "url": "/blog/article-slug"}
    ]
    """
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": item["name"],
                "item": absolute_url(item["url"])
            }
            for index, item in enumerate(items, start=1)
        ]
    }


def blog_schema(seo):
    return {
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": f"{seo['canonical']}#blog",
        "name": seo["title"],
        "description": seo["description"],
        "url": seo["canonical"],
        "publisher": {
            "@id": f"{SITE_URL}/#organization"
        },
        "isPartOf": {
            "@id": f"{SITE_URL}/#website"
        }
    }


def blog_posting_schema(post, seo):
    image = absolute_url(
        post.get("image", DEFAULT_OG_IMAGE)
    )

    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "@id": f"{seo['canonical']}#article",
        "mainEntityOfPage": {
            "@id": f"{seo['canonical']}#webpage"
        },
        "headline": post["title"],
        "description": seo["description"],
        "url": seo["canonical"],
        "image": [image],
        "author": {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": SITE_URL
        },
        "publisher": {
            "@id": f"{SITE_URL}/#organization"
        }
    }

    if post.get("published_date"):
        schema["datePublished"] = post["published_date"]

    if post.get("updated_date"):
        schema["dateModified"] = post["updated_date"]
    elif post.get("published_date"):
        schema["dateModified"] = post["published_date"]

    return schema