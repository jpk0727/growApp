import time
import json
import moment
from datetime import datetime
from django import forms
from base.models import sensors

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
