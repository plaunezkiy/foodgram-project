from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'),
    path('purchases/download/', views.download_purchases,
         name='download_purchases'),
    path('purchases/<int:recipe_id>/', views.PurchaseView.as_view(),
         name='remove_purchase'),

    path('new/', views.CreateRecipeView.as_view(), name='new_recipe'),
    path('user/<str:username>/<slug:slug>/', views.single_recipe,
         name='recipe'),
    path('user/<str:username>/<slug:slug>/edit/',
         views.EditRecipeView.as_view(),
         name='edit_recipe'),
    path('user/<str:username>/<slug:slug>/delete/', views.delete_recipe,
         name='delete_recipe'),

    path('ingredients/', views.list_ingredients, name='list_ingredients'),
    path('tag/<str:tag>/<str:previous>/', views.edit_tag,
         name='edit_tag'),

    path('subscriptions/', views.SubscribeView.as_view(),
         name='subscriptions'),
    path('subscriptions/<int:user_id>/', views.SubscribeView.as_view(),
         name='remove_subscription'),

    path('favorites/', views.FavoriteView.as_view(), name='favorites'),
    path('favorites/<int:recipe_id>/', views.FavoriteView.as_view(),
         name='remove_favorite'),

    path('about/', views.about, name='about'),
    path('spec/', views.spec, name='spec'),
]
