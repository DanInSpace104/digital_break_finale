from django.shortcuts import render
from django.views.generic import DetailView
from .models import Profile


class ProfileView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'

