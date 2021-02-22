import os
from django.db import models
from users.models import get_user_model
from multiselectfield import MultiSelectField

User = get_user_model()
TAGS = (
    ('breakfast', 'Завтрак'),
    ('lunch', 'Обед'),
    ('dinner', 'Ужин')
)


class Ingredient(models.Model):
    title = models.CharField(max_length=75)
    dimension = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.title} / {self.dimension}"

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ['title']


class Recipe(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/recipes/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_image_name(self):
        return os.path.basename(self.image.url)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-pub_date']


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
