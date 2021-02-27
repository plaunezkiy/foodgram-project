from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "name")
    search_fields = ("description",)
    list_filter = ("tags", "author", "name")
    inlines = [
        RecipeIngredientInline,
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "dimension")
    search_fields = ("title",)
    list_filter = ("title",)
