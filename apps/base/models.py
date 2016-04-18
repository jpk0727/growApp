from django.db import models

# Create your models here.


class sensors(models.Model):
    time = models.FloatField()
    temp = models.FloatField()
    hum = models.FloatField()
    light = models.FloatField()
    lux = models.FloatField()

    def _java_time(self):
        " returns the time in java format "
        return self.time * 1000

    java_time = property(_java_time)
    

class plant_area(models.Model):
    date = models.DateTimeField()
    row = models.CharField(max_length=2)
    column = models.IntegerField()
    area = models.FloatField()
    height = models.FloatField()


class water_amount(models.Model):
    time = models.FloatField()
    liters_added_r1 = models.FloatField()
    liters_total_r1 = models.FloatField()
    liters_added_r2 = models.FloatField()
    liters_total_r2 = models.FloatField()
    liters_added_r3 = models.FloatField()
    liters_total_r3 = models.FloatField()

    def _java_time(self):
        " returns the time in java format "
        return self.time * 1000

    java_time = property(_java_time)

class controller_setpoints(models.Model):
    time = models.FloatField(default=0)
    humidity = models.IntegerField()
    r1_water = models.IntegerField()
    r2_water = models.IntegerField()
    r3_water = models.IntegerField()
    water_frequency = models.IntegerField(null=True)
    lights_on = models.TimeField(null=True)
    lights_off = models.TimeField(null=True)
