# Generated by Django 4.2.8 on 2023-12-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='numero_carte',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='numero_telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='region',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='ufr',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='universite',
            field=models.CharField(max_length=10),
        ),
    ]
