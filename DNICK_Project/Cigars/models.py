import uuid

from django.contrib.auth.models import User
from django.db import models

class Kupuvac(models.Model):
    Ime = models.CharField(max_length=255,blank=True,default=True)
    Prezime = models.CharField(max_length=255,blank=True,default=True)
    Username=models.CharField(max_length=255,blank=True,default=True)
    godina_na_ragjane = models.IntegerField(blank=True,default=True)
    #korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Ime} {self.Prezime}"

class Proizvoditel(models.Model):
    ime_na_proizvoditel=models.CharField(max_length=255)


class Proizvod(models.Model):

    ime_na_proizvoditel=models.CharField(max_length=255,blank=True,default=True)
    deskripcija=models.TextField(max_length=2000,blank=True,default=True)
    zemja_na_poteklo=models.CharField(max_length=255,blank=True,default=True)
    cena=models.IntegerField(blank=True,default=True)
    zaliha=models.IntegerField(blank=True,default=True)
    fotografija=models.ImageField(upload_to="static/",blank=True,default=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,default=True)
class Prodavac(models.Model):
    Ime = models.CharField(max_length=255,blank=True,default=True)
    Prezime = models.CharField(max_length=255,blank=True,default=True)
    Username = models.CharField(max_length=255,blank=True,default=True)
    godina_na_ragjane = models.IntegerField(blank=True,default=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Ime} {self.Prezime}"

class ProdavacProizvod(models.Model):
    Proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE,default=True,blank=True)
    Prodavac = models.ForeignKey(Prodavac, on_delete=models.CASCADE)

class Najava(models.Model):
    Korisnicko_ime= models.CharField(max_length=255)
    Lozinka=models.CharField(max_length=255)
class KupuvacProizvod(models.Model):
    kupuvac = models.ForeignKey(Kupuvac, on_delete=models.CASCADE,default=True,blank=True)
    Proizvod=models.ForeignKey(Proizvod, on_delete=models.CASCADE)

# Create your models here.
