import time
"""Views for the base app"""

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.contrib import messages

from base.models import sensors, controller_setpoints
from base.forms import DateForm, ControlForm
from base.models import water_amount

from graphos.sources.model import ModelDataSource
from django.http import HttpResponse, HttpResponseRedirect
from graphos.renderers import flot
from graphos.views import FlotAsJson, RendererAsJson
from datetime import datetime
from datetime import timedelta

import json
import calendar
from django.http import Http404, HttpResponse


def home(request):
    """ Default view for the root """
    query = sensors.objects.latest('time')
    query.time = time.ctime(int(query.time))
    query.temp = round(query.temp, 2)
    query.hum = round(query.hum, 2)
    #for i in query:
    #    i.time = time.ctime(int(i.time))
    return render(request, 'base/home.html', {'query':query})


def monitor(request):
    if request.method == 'GET':
        form = DateForm()
    else:
        form = DateForm(request.POST)
    
    end = sensors.objects.latest('time')
    end_time = datetime.fromtimestamp(
        int(end.time)).strftime('%Y-%m-%d %H:%M')
    start = sensors.objects.earliest('time')
    start_time = datetime.fromtimestamp(
        int(start.time)).strftime('%Y-%m-%d %H:%M')
    query = sensors.objects.latest('time')
    query.time = time.ctime(int(query.time))

    yesterday = datetime.now() - timedelta(days = 1)
    yesterday_time = yesterday.strftime("%Y-%m-%d %H:%M")

    dates = request.POST
    start_date = dates.get('start_date',yesterday_time)
    end_date = dates.get('end_date',end_time)
    
    start_stamp = time.mktime(time.strptime(start_date, "%Y-%m-%d %H:%M"))
    end_stamp = time.mktime(time.strptime(end_date, "%Y-%m-%d %H:%M"))


    queryset = sensors.objects.filter(time__gte = start_stamp,
                                      time__lt = end_stamp).order_by('time')

    queryset1 = water_amount.objects.filter(time__gte = start_stamp,
                                      time__lt = end_stamp).order_by('time')
        
    data_source1 = ModelDataSource(queryset, fields=['java_time','temp'])
    data_source2 = ModelDataSource(queryset, fields=['java_time','hum'])
    data_source3 = ModelDataSource(queryset, fields=['java_time','light'])
    data_source4 = ModelDataSource(queryset, fields=['java_time','lux'])

    data_source5 = ModelDataSource(queryset1, fields=['java_time','liters_total_r1','liters_total_r2','liters_total_r3'])


    line_chart1 = flot.LineChart(data_source1,options = {'series': {'lines': {'fill':'true'}, 'color':'blue'}, 'xaxis':{'mode': 'time', 'timeformat': '%m/%e %I:%M %P', "timezone":"browser"}})
    line_chart2 = flot.LineChart(data_source2,options = {'series': {'lines': {'fill':'true'}, 'color':'red'}, 'xaxis':{'mode': 'time', 'timeformat': '%m/%e %I:%M %P','timezone':'browser'}})
    line_chart3 = flot.LineChart(data_source3,options = {'series': {'lines': {'fill':'true'}, 'color':'green'}, 'xaxis':{'mode': 'time', 'timeformat': '%m/%e %I:%M %P','timezone':'browser'}})
    line_chart4 = flot.LineChart(data_source4,options = {'series': {'lines': {'fill':'true'}, 'color':'purple'}, 'xaxis':{'mode': 'time', 'timeformat': '%m/%e %I:%M %P','timezone':'browser'}})
    
    line_chart5 = flot.BarChart(data_source5, options = {'series': {'lines': {'steps':'boolean'}}, 'xaxis':{'mode': 'time', 'timeformat': '%m/%e %I:%M %P', "timezone":"browser"}})

    context = {
            "line_chart1": line_chart1,
            "line_chart2": line_chart2,
            "line_chart3": line_chart3,
            "line_chart4": line_chart4,
            "line_chart5": line_chart5,
            "form": form,
            "dates":dates,
            "start_stamp":start_stamp,
    }
    
    return render(request, 'base/monitor.html', context)

def about(request):
    return render(request, 'base/about.html',{})

def control(request):
    if request.method == 'GET':
        cur = controller_setpoints.objects.latest('id')
        data = {'humidity':cur.humidity,'r1_water':cur.r1_water,'r2_water':cur.r2_water,'r3_water':cur.r3_water,'water_frequency':cur.water_frequency,'lights_on':cur.lights_on,'lights_off':cur.lights_off}
        form = ControlForm(initial=data)
    else:
        form = ControlForm(request.POST)
        if form.is_valid():
            form.time = time.time()
            form.save()
            return HttpResponseRedirect('/grow/control')
    context = {
            "form":form
    }
        
    return render(request, 'base/control.html',context)

