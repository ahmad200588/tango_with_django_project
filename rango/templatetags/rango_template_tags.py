from django import template

from rango.models import Category


register = template.Library()


@register.simple_tag
def get_category_list():
    """Return all categories ordered by likes for the sidebar."""
    return Category.objects.order_by("-likes")
