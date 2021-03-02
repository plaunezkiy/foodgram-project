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


@register.filter
def get_recipes(ids):
    recipes = Recipe.objects.filter(id__in=ids)
    return recipes


@register.filter
def declination(counter):
    counter -= 3
    div, remainder = divmod(counter, 10)
    if div == remainder == 1:
        return f'{counter} рецептов'
    if remainder == 1:
        return f'{counter} рецепт'
    if 2 <= remainder <= 4:
        return f'{counter} рецепта'
    return f'{counter} рецептов'
