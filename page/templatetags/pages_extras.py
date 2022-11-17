from ..models import Page
from django import template

# Registrar este script como un template
register = template.Library()

# Agregar un decorador


@register.simple_tag
# Consultar todas las páginas secundarias
def get_pages_list():
    pages = Page.objects.all()
    return pages
