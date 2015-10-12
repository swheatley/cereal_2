from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True) 

    def __unicode__(self):
        return self.name


class Cereal(models.Model):
    cereal_name = models.CharField(max_length=200, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sodium = models.IntegerField(null=True, blank=True)
    dietary_fiber = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    sugars = models.IntegerField(null=True, blank=True)
    potassium = models.IntegerField(null=True, blank=True)
    vitamins_and_minerals = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.cereal_name


