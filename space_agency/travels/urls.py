from django.urls import path

from travels import views

urlpatterns = [
    path('', views.home, name='home'),
]