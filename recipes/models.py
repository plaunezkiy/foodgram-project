import os

from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

TAGS = (
    ('breakfast', 'Завтрак'),
    ('lunch', 'Обед'),
    ('dinner', 'Ужин')
)


class Ingredient(models.Model):
    title = models.CharField(max_length=75)
    dimension = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.title} / {self.dimension}'

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['title']


class Recipe(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='recipes')
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='media/recipes/',
                              blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.author}'

    @property
    def get_image_name(self):
        return os.path.basename(self.image.url) or None

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Ингредиент к рецептам'
        verbose_name_plural = 'Ингредиенты к рецептам'
        unique_together = ("recipe", "ingredient")

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.title} - ' \
               f'{self.ingredient.dimension}'
