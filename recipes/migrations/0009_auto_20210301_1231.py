# Generated by Django 3.1.6 on 2021-03-01 03:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20210226_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['title'], 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'Ингредиент к рецептам', 'verbose_name_plural': 'Ингредиенты к рецептам'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together={('recipe', 'ingredient')},
        ),
    ]
