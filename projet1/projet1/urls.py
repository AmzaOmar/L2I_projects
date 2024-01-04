from django.contrib import admin
from django.urls import path,include
from Connexion.views import inscription , connexion , deconnexion , menu
from Acceuil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Acceuil.urls')),
    path('connexion ou insciption', menu , name="menu"),
    path('inscription/', inscription , name="inscription"),
    path('connexion/', connexion , name="connexion"),
    path("Deconnexion/", deconnexion, name="deconnexion"),
]

