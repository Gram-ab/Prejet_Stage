from calendar import day_abbr
from contextlib import nullcontext
from dis import code_info
from email.policy import default
from sqlite3 import Time
from typing import Type
import datetime
import django


from django.db import models
from django.forms import CharField, IntegerField


class Vis_type(models.Model):
    Id_type = models.IntegerField(primary_key = True)
    Lib_type = models.CharField(max_length=255)
class Visiteur(models.Model):
    code_visiteur = models.CharField(max_length=255 , primary_key = True)
    nom_visiteur = models.CharField(max_length=255)
    prenom_visiteur =models.CharField(max_length=255)
    CIN= models.CharField(max_length=25)
    Tel = models.CharField(max_length=30)
    Adresse = models.CharField(max_length=255)
    Entreprise = models.CharField(max_length=255)
    Type = models.ForeignKey(Vis_type , on_delete=models.CASCADE)
    sexe =models.CharField(max_length=15 , default="F")
class Prestation(models.Model):
    Code_prest = models.IntegerField(primary_key = True)
    Lib_prest = models.CharField(max_length=255)    
class Service (models.Model):
    code_service = models.IntegerField(primary_key = True)
    Lib_service = models.CharField(max_length=255)
class Departement(models.Model):
    code_dep = models.IntegerField(primary_key = True)
    A_dep = models.CharField(max_length=25,default='DEP')
    Lib_dep = models.CharField(max_length=55)
class Fonctionnaire(models.Model):
    code_F =models.IntegerField(primary_key = True)
    cin_F = models.CharField(max_length=255)
    nom_F = models.CharField(max_length=255)
    prenom_F = models.CharField(max_length=255)
    Departement = models.ForeignKey(Departement , on_delete=models.CASCADE)
    Service = models.ForeignKey(Service , on_delete=models.CASCADE)
class date(models.Model):
   Code_date=models.IntegerField(primary_key = True) 
   visit_date = models.CharField(max_length=255,null=True)  
   visit_time = models.CharField(max_length=255 , null = True)  
class Histo_Prestation(models.Model):
    Status_CHOICES = [
        ('en_coure', 'En coure'),
        ('traité', 'traité'),
        ('attente', 'en attente')
    ]
    code_vist = models.ForeignKey(Visiteur ,on_delete=models.CASCADE)
    code_F =  models.ForeignKey(Fonctionnaire  , on_delete=models.CASCADE)
    code_Pres = models.ForeignKey(Prestation  , on_delete=models.CASCADE)
    code_date = models.ForeignKey(date  ,on_delete=models.CASCADE)
    status = models.CharField(max_length=55 , choices=Status_CHOICES , default='en_coure')
