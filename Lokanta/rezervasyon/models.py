from django.db import models

# Create your models here.
class Rezervasyon(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tarih = models.DateField()
    numara = models.IntegerField()
    ksayi = models.IntegerField()
    saat = models.DateField(blank = True, null = True)


class baglanti (models.Model) :
    first_name = models.CharField(max_length=30)
    emailadress = models.CharField(max_length=30)
    yazi = models.TextField()


class menu (models.Model) :
    yemekısmı = models.CharField(max_length=30)
    yemekfıyatı = models.IntegerField
    yemektanıtım = models.CharField(max_length=150)
    yemekresmı = models.ImageField
