from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
