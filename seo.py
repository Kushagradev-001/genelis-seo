from flask import request


SITE_NAME = "Genelis"
SITE_URL = "https://genelis.in"
DEFAULT_OG_IMAGE = "/static/og/genelis-og-image.png"


def build_seo(seo_data):
    """
    Builds complete SEO metadata for a page.
    """

    path = seo_data.get("path", request.path)

    canonical_url = f"{SITE_URL}{path}"

    return {
        "title": seo_data.get("title", SITE_NAME),
        "description": seo_data.get(
            "description",
            "Genelis is an AI learning platform for CBSE and NCERT students."
        ),
        "keywords": ", ".join(seo_data.get("keywords", [])),
        "canonical": canonical_url,
        "og_title": seo_data.get("title", SITE_NAME),
        "og_description": seo_data.get(
            "description",
            "Genelis helps students learn with AI notes, mock tests, question banks, analytics, and personalized guidance."
        ),
        "og_url": canonical_url,
        "og_image": f"{SITE_URL}{DEFAULT_OG_IMAGE}",
        "twitter_card": "summary_large_image",
        "robots": "index, follow"
    }


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Genelis",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/static/icons/icon-512.png",
        "description": "Genelis is an AI learning platform for CBSE and NCERT students.",
        "sameAs": []
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Genelis",
        "url": SITE_URL,
        "description": "AI-powered learning platform for CBSE and NCERT students.",
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{SITE_URL}/search?q={{search_term_string}}",
            "query-input": "required name=search_term_string"
        }
    }


def webpage_schema(seo):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": seo["title"],
        "description": seo["description"],
        "url": seo["canonical"],
        "isPartOf": {
            "@type": "WebSite",
            "name": "Genelis",
            "url": SITE_URL
        }
    }