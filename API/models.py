from django.db import models

class City(models.Model):
    City_Name = models.CharField(default="",max_length=30,verbose_name="City_Name")

    def __str__(self):
        return self.City_Name

class Temperature(models.Model):
    ID = models.ForeignKey(City,on_delete = models.CASCADE)
    Year = models.IntegerField(default=0,verbose_name="Year")
    temperature = models.IntegerField(default=0,verbose_name="temperature")
