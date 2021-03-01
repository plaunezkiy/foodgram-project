from django.db import models
from django.contrib.auth import get_user_model

from recipes.models import Recipe


class Follow(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name="follower")
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name="following")

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'author')

    def __str__(self):
        return f'{self.user.username} - {self.author.username}'


class Favorite(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorite')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='favorite_recipe')

    class Meta:
        verbose_name = 'Любимый рецепт'
        verbose_name_plural = 'Любимые рецепты'
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f'{self.user.username} - {self.recipe.name}'
