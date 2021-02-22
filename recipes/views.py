import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from pytils.translit import slugify
from django.views.generic import View

from .forms import RecipeForm
from .models import Ingredient, Recipe


def base(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


class CreateRecipeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        form = RecipeForm()
        return render(request, 'recipe_form.html', context={'form': form})

    def post(self, request):
        form = RecipeForm(request.POST, files=request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.name)
            recipe.save()
        else:
            return render(request, 'recipe_form.html', context={'form': form})

        return redirect('index')


class EditRecipeView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.author != request.user:
            return redirect('index')

        form = RecipeForm(instance=recipe)
        return render(
            request,
            'recipe_form.html',
            context={
                'form': form, 'edit': True, 'image_name': recipe.get_image_name()
            }
        )

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.author != request.user:
            return redirect('index')

        form = RecipeForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.edit(request.user)
        else:
            return render(request, 'recipe_form.html',
                          context={
                              'form': form, 'edit': True, 'image_name': recipe.get_image_name()
                          }
                          )
        return redirect('index')



# operating requests


def list_ingredients(request):
    query = request.GET.get('query').lower()
    ingredients = Ingredient.objects.filter(title__icontains=query).values('title', 'dimension')
    return JsonResponse(list(ingredients), safe=False)
