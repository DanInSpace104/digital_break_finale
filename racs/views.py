from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from .models import Claim
from zulip_api.zulip_api import zulip_create_stream
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


class CreateClaimView(CreateView):
    model = Claim
    template_name = 'claims/create_claim.html'
    success_url = '/'
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

    def form_valid(self, form):
        response = super().form_valid(form)
        data = form.cleaned_data
        zulip_create_stream(
            data['expert'].email,
            data['users'],
            self.object.id,
            data['name'],
            data['category'],
        )

        return response
