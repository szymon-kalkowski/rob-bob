from pyexpat import model
from django.db import models

class Opinie(models.Model):
    imie = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=70, blank=True)
    ocena = models.PositiveIntegerField(default=1)
    opinia = models.TextField(max_length=1000, blank=True)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Opinia"
        verbose_name_plural = "Opinie"

class Uslugi(models.Model):
    nazwa = models.CharField(max_length=200)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"

class Realizacje(models.Model):
    zdjecie = models.FileField(blank=False)

    class Meta:
        verbose_name = "Realizacja"
        verbose_name_plural = "Realizacje"

class Edycje(models.Model):
    slide_1 = models.FileField(blank=False)
    slide_2 = models.FileField(blank=False)
    slide_3 = models.FileField(blank=False)

    o_nas_tytul = models.CharField(max_length=300)
    o_nas_opis = models.TextField(max_length=2000)

    tel_1 = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20)

    regulamin = models.FileField(blank=False)

    class Meta:
        verbose_name = "Edycja"
        verbose_name_plural = "Edycje"