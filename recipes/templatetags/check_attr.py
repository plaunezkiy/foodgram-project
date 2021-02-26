from django import template
from users.models import Favorite

register = template.Library()


@register.filter
def check_fav(recipe, user):
    obj = Favorite.objects.filter(recipe=recipe, user=user)
    return obj.exists()
