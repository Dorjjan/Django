from django.db import models


class MensClothes(models.Model):
    def __str__(self):
        return self.nazwa
    class TypeMensClothes(models.TextChoices):
        SPODENKI = 'SX', ('Spodenki')
        JOGGERY = 'JX', ('Joggery')
        BLUZY = 'BX', ('Bluzy')
    type_mens_clothes =models.CharField(
        max_length=100,
        choices=TypeMensClothes.choices,
        default=TypeMensClothes.SPODENKI
     )        
    
    
    nazwa = models.CharField(max_length=120)
    rozmiar = models.CharField(max_length=4)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kolor = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Odziez Meska"
        verbose_name_plural="Odziez Meska"

class WomansClothes(models.Model):
    def __str__(self):
        return self.nazwa
    
    class TypeWomensClothes(models.TextChoices):
        SPODENKI = 'SY', ('Spodenki')
        SUKIENKI = 'CY', ('Joggery')
        BUTY = 'BY', ('Bluzy')
    type_womens_clothes =models.CharField(
        max_length=100,
        choices=TypeWomensClothes.choices,
        default=TypeWomensClothes.SPODENKI
     )   
   
    nazwa = models.CharField(max_length=120)
    rozmiar = models.CharField(max_length=4)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kolor = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Odziez Damska"
        verbose_name_plural="Odziez Damska"
