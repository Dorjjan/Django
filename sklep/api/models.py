from django.db import models

class TypUbraniaM(models.Model):
    typ = models.CharField(max_length=120)
    class Meta:
        verbose_name= "Typ Meski"
        verbose_name_plural="Typy Meskie"
class TypUbraniaK(models.Model):
    typ = models.CharField(max_length=120)
    class Meta:
        verbose_name= "Typ Damski"
        verbose_name_plural="Typy Damskie"

class OdziezMeska(models.Model):
    def __str__(self):
        return self.nazwa
    
    typM = models.ForeignKey(TypUbraniaM, on_delete=models.CASCADE, null=True)
    
    nazwa = models.CharField(max_length=120)
    rozmiar = models.CharField(max_length=4)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kolor = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Odziez Meska"
        verbose_name_plural="Odziez Meska"

class OdziezDamska(models.Model):
    def __str__(self):
        return self.nazwa
    
    typ = models.ForeignKey(TypUbraniaK, on_delete=models.CASCADE, null=True)
   
    nazwa = models.CharField(max_length=120)
    rozmiar = models.CharField(max_length=4)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    kolor = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Odziez Damska"
        verbose_name_plural="Odziez Damska"
