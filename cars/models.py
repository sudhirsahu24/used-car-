from django.db import models


class CarPrice(models.Model):

    Car_Brand_Kia = models.CharField(max_length=50)
    Color_Red = models.CharField(max_length=50)
    No_of_years = models.IntegerField()
    Present_Price = models.FloatField()
    Kms_Driven = models.IntegerField()
    Owner = models.IntegerField()
    Fuel_Type_Petrol = models.CharField(max_length=50)
    Seller_Type_Individual = models.CharField(max_length=50)
    Transmission_Manual = models.CharField(max_length=50)




# Create your models here.
