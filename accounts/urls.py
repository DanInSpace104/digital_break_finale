from django.urls import include, path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
]
