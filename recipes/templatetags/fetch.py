from django import template
from ..models import Recipe

register = template.Library()


@register.filter
def latest(author, n):
    recipes = Recipe.objects.filter(author=author)[:n]
    return recipes


@register.filter
def get_followed(user):
    return user.follower.all().values_list('author', flat=True)
