from django.db import models


class Cautare(models.Model):
    objects = None
    cod_produs = models.CharField(max_length=100)
    descriere_si_pret = models.CharField(max_length=100)
    magazin = models.CharField(max_length=100)
    active = models.BooleanField(default=1)
    cautare = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cautare}"



