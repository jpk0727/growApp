import time
import json
import moment
from datetime import datetime 
from django import forms
from base.models import sensors, controller_setpoints
from django.utils.translation import ugettext_lazy as _


from bootstrap3_datetime.widgets import DateTimePicker

# class DateForm(forms.Form):
#     start_date = forms.DateField(
#             widget=DateTimePicker())
#     end_date = forms.DateField(

class DateForm(forms.Form):

    end = sensors.objects.latest('time')
    end_time = datetime.fromtimestamp(
        int(end.time)).strftime('%Y-%m-%d %H:%M')
    start = sensors.objects.earliest('time')
    start_time = datetime.fromtimestamp(
        int(start.time)).strftime('%Y-%m-%d %H:%M')


    start_date = forms.DateTimeField(
            widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                "locale": "en",
                "minDate":  start_time,
                "maxDate":end_time,
                "defaultDate": start_time,
                "sideBySide": True}))
    end_date = forms.DateTimeField(
            widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                "locale": "en",
                "minDate":  start_time,
                "maxDate":end_time,
                "defaultDate":end_time,
                "sideBySide": True}))


class ControlForm(forms.ModelForm):
    lights_on = forms.TimeField(
            widget=DateTimePicker(options={"format": "HH:mm",
                "locale":"en",
                "pickDate":0}))

    lights_off = forms.TimeField(
            widget=DateTimePicker(options={"format": "HH:mm",
                "locale":"en",
                "pickDate":0}))
    class Meta:
        model = controller_setpoints
        fields = ['humidity','r1_water','r2_water','r3_water','water_frequency','lights_on','lights_off']
    
        labels = {
            "humidity":_("Relative Percent Humidity"),
            "r1_water":_("Number of Seconds to Water Row 1"),
            "r2_water":_("Number of Seconds to Water Row 2"),
            "r3_water":_("Number of Seconds to Water Row 3"),
            "water_frequency":_("How often to water in minutes"),
            "lights_on":_("What time of day to start the lights"),
            "lights_off":_("What time of day to turn off the lights")
        }
