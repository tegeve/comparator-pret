from django.db import models


class Produse(models.Model):
    objects = None
    cod_produs = models.CharField(max_length=100)
    descriere = models.CharField(max_length=100)
    active = models.BooleanField(default=1)
    pret_altex = models.CharField(max_length=100)
    pret_emag = models.CharField(max_length=100)
    imagine = models.ImageField(null=True, blank=True)


    def __str__(self):
        return f"{self.cod_produs}"

