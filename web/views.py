from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from  .models import iot
from django.conf import settings
import json
from django.core.cache import cache
from .api import getSensordata,getmotorStatus,getweatherStatus,sendCommand,hardupdate


# Create your views here.

def home(request):
    sensor_data=getSensordata()
    motor_data=getmotorStatus()
    weather_data=getweatherStatus()
    return render(request,'home.html',{'sensor_data':sensor_data,'motor_data':motor_data,'weather_data':weather_data})

def seton(request):
    sendCommand("ON")
    cache.delete('MotorStatus')
    result=getmotorStatus()
    return JsonResponse({'status':result})

def setoff(request):
    sendCommand("OFF")
    cache.delete('MotorStatus')
    result=getmotorStatus()
    return HttpResponse({'status':result})

def getdata(request):
    sensor_data=getSensordata()
    motor_data=getmotorStatus()
    weather_data=getweatherStatus()
    return JsonResponse({'sensor_data':sensor_data,'motor_data':motor_data,'weather_data':weather_data})

def update(request):
    hardupdate()
    return getdata(request)

def past_trend(request):
    query=iot.objects.order_by('-timestamp')[:6]
    query=reversed(query)
    temp=[]
    moist=[]
    humid=[]
    timestamp=[]
    for obj in query:
        timestamp.append(obj.timestamp.strftime("%d/%m %H:%M"))
        temp.append(obj.information['temperature'])
        moist.append(obj.information['moisture'])
        humid.append(obj.information['humidity'])
    return render(request,'pasttrend.html',{'temp_data':temp,'moist_data':moist,'humid_data':humid,'timestamp':timestamp})