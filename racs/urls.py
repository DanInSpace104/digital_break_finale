from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('claims/create/', views.CreateClaimView.as_view(), name='claim_create'),
    path('claims/chart/', views.ChartClaimView.as_view(), name='chart_claim'),
    path('claims/', views.ClaimListView.as_view(), name='claim_list'),
    path('claims/detail/<int:pk>', views.ClaimDetailView.as_view(), name='claim_detail'),
    path('cabinet/expert/<int:pk>', views.ExpertPageView.as_view(), name='expert_cabinet'),
    path('cabinet/user/<int:pk>', views.UserPageView.as_view(), name='user_cabinet'),
    path('cabinet/director/<int:pk>', views.DirectorPageView.as_view(), name='director_cabinet'),
]
