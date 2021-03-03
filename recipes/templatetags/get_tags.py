from django import template
from django.conf import settings

register = template.Library()


@register.filter(is_safe=True)
def get_tags(tag_list, css_class):
    tags = ''
    for tag in tag_list:
        tags += f'<li class="{css_class}">' \
                f'<span class="badge badge_style_{settings.TAGS_CLASSES[tag][0]}">' \
                f'{settings.TAGS_CLASSES[tag][1]}</span></li>'

    return tags
