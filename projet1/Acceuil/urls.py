from django.urls import path
from Acceuil import views

urlpatterns = [
    path('', views.acceuil, name="acceuil"),
    path('', views.base, name="base"),
]
