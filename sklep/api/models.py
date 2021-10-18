from django.db import models

class Ubranie(models.Model):
    nazwa = models.CharField(max_length=120)
    rozmiar = models.CharField(max_length=4)
    cena = models.CharField(max_length=10)
    plec = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)



