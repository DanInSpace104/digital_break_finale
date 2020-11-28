from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from .models import Claim, Category, Term, Cost
from zulip_api.zulip_api import zulip_create_stream
from django.http import HttpResponse
from django.conf import settings
from django.apps import apps


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        data['users'] = apps.get_model(settings.AUTH_USER_MODEL).objects.all()
        data['default_status'] = Claim._meta.get_field('status').get_default()
        return data

    def form_valid(self, form):
        print(form.data)
        response = super().form_valid(form)
        data = form.cleaned_data
        zulip_create_stream(
            data['expert'].email,
            data['users'],
            self.object.id,
            data['name'],
            data['category'],
        )
        name_costs = form.data['nameCosts[]']
        print(name_costs, type(name_costs))
        val_costs = form.data['valueCosts[]']
        print(val_costs, type(val_costs))
        name_terms = form.data['nameTerms[]']
        val_terms = form.data['valueTerms[]']

        for name, value in zip(name_costs, val_costs):
            cost = Cost(name=name, summ=int(value))
            cost.save()
            self.object.costs.add(cost)
        for name, value in zip(name_terms, val_terms):
            term = Term(name=name, days=int(value))
            term.save()
            self.object.terms.add(term)
        self.object.save()

        return response
