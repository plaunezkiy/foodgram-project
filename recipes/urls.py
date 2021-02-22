from django.urls import path

from . import views


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('new/', views.CreateRecipeView.as_view(), name='new_recipe'),
    path('recipe/<slug:slug>/edit/', views.EditRecipeView.as_view(), name='edit_recipe'),

    path('ingredients/', views.list_ingredients, name='list_ingredients'),
]
