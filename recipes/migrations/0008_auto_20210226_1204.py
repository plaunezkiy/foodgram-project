# Generated by Django 3.1.6 on 2021-02-26 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20210226_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'Ингридиент к рецептам', 'verbose_name_plural': 'Ингридиенты к рецептам'},
        ),
    ]