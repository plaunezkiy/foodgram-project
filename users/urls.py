from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('user/<str:username>/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
