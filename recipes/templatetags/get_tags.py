from django import template

register = template.Library()


@register.filter(is_safe=True)
def get_tags(tag_list, css_class):
    tag_keys = {
        'breakfast': ['orange', 'Завтрак'],
        'lunch': ['green', 'Обед'],
        'dinner': ['purple', 'Ужин']
    }
    tags = ''
    for tag in tag_list:
        tags += f'<li class="{css_class}">' \
                f'<span class="badge badge_style_{tag_keys[tag][0]}">' \
                f'{tag_keys[tag][1]}</span></li>'

    return tags
