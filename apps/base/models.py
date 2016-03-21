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
    
