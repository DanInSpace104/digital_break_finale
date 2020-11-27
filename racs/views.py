from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Claim


class IndexView(TemplateView):
    template_name = 'index.html'


class CreateClaimView(CreateView):
    model = Claim
    template_name = 'claims/create_claim.html'
    fields = (
        'name',
        'users',
        'status',
        'curr_desc',
        'new_desc',
        'pos_effect',
        'costs',
        'terms',
        'expert',
        'category',
    )
