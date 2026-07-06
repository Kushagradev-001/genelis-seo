WEBSITE_URL = "https://genelis.in"
APP_URL = "https://app.genelis.in"


def tracked_app_link(source, campaign="website_cta"):
    return (
        f"{APP_URL}/"
        f"?utm_source=genelis_website"
        f"&utm_medium=cta"
        f"&utm_campaign={campaign}"
        f"&utm_content={source}"
    )


CTA_LINKS = {
    "start_learning": tracked_app_link("start_learning"),

    "navbar_start": tracked_app_link("navbar_start_learning"),
    "footer_start": tracked_app_link("footer_start_learning"),
    "global_cta": tracked_app_link("global_cta"),
    "final_cta": tracked_app_link("final_cta"),

    "homepage_hero": tracked_app_link("homepage_hero"),
    "homepage_workspace": tracked_app_link("homepage_workspace"),
    "homepage_learning_loop": tracked_app_link("homepage_learning_loop"),

    "learning_system_primary": tracked_app_link("learning_system_primary"),
    "learning_system_final": tracked_app_link("learning_system_final"),

    "about_primary": tracked_app_link("about_primary"),
    "about_learning_loop": tracked_app_link("about_learning_loop"),

    "product_preview": tracked_app_link("product_preview"),

    "classes_primary": tracked_app_link("classes_primary"),
    "class_detail_primary": tracked_app_link("class_detail_primary"),

    "pricing_free": tracked_app_link("pricing_free"),
    "pricing_monthly": tracked_app_link("pricing_monthly"),
    "pricing_annual": tracked_app_link("pricing_annual"),

    "blog_primary": tracked_app_link("blog_primary"),
    "contact_primary": tracked_app_link("contact_primary"),
    "contact_support": "mailto:support@genelis.in",

    "login": f"{APP_URL}/login",
    "signup": f"{APP_URL}/signup",
    "app_home": APP_URL,
}