from django.contrib import admin
from django.urls import path,include
from Connexion.views import inscription , connexion
from Acceuil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', inscription , name="inscription"),
    path('connexion/', connexion , name="connexion"),
]

