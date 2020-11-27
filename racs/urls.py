from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('claims/create', views.CreateClaimView.as_view(), name='claim_create'),
]
