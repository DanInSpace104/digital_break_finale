from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('claims/create/', views.CreateClaimView.as_view(), name='claim_create'),
    path('claims/chart/', views.ChartClaimView.as_view(), name='chart_claim'),
    path('claims/', views.ClaimListView.as_view(), name='claim_list'),
    path('claims/detail', views.ClaimDetailView.as_view(), name='claim_detail'),
]
