from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, View
from django.urls import reverse_lazy

from .forms import SignUpForm
from .models import User
from recipes.models import Recipe
from recipes.mixins import MainMixin


class ProfileView(MainMixin, View):
    template = 'profile.html'
    tab = 'recipes'
    profile = True

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        self.title = user.get_full_name()
        self.queryset = Recipe.objects.filter(author=user)
        return super(ProfileView, self).get(request)


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
