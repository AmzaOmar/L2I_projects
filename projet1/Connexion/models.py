import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=30)
    universite = models.CharField(max_length=10)
    ufr = models.CharField(max_length=30)
    numero_carte = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    date_naissance = models.DateField(default=datetime.date.today)
    numero_telephone = models.CharField(max_length=10)
    

    def __str__(self):
        return self.prenom

