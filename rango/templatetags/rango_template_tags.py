from django import template
from rango.models import Category

register = template.Library()


@register.inclusion_tag('rango/cats.html')
# returns a list of categories but mashed up with template rango/cats.html
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat':cat}
