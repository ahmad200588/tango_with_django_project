from rango.models import Category


def sidebar_categories(request):
    """Provide a small list of categories and expose it to any template."""

    categories = Category.objects.order_by("-likes")[:5]
    return {
        "sidebar_categories": categories,
        # Keep the legacy name available for templates that still want it.
        "categories": categories,
    }
