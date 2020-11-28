import json

from django.apps import apps
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import CreateView
from zulip_api.zulip_api import zulip_create_stream

from .models import Category, Claim, Cost, Term
from .mail import send_email


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
        for user in self.object.users.all():
            send_email(user.email, self.object.name, 'новая заявка создана')
        send_email(
            self.object.expert.email,
            self.object.name,
            'новая заявка создана',
        )

        return response


class ChartClaimView(View):
    def get(self, request):
        claims = Claim.objects.all()
        res = {key: 0 for key, value in Claim.STATUS_CHOICES}
        print(res)
        for claim in claims:
            res[claim.status] += 1

        return render(request, 'claims/chart.html', {'res': list(res.values())})


class ClaimListView(ListView):
    model = Claim
    template_name = 'claims/claim_list.html'


class ClaimDetailView(DetailView):
    model = Claim
    template_name = 'claims/detail.html'


class ExpertPageView(View):
    def get(self, request, *args, **kwargs):
        ctx = {}
        expert_claims = Claim.objects.filter(expert=kwargs['pk'])
        new_claims = expert_claims.filter(status='EX')
        ctx['expert_claims'] = expert_claims
        ctx['new_claims'] = new_claims
        return render(request, 'cabinet/expert.html', ctx)
