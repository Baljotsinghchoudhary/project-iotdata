import json,base64,requests
import wiotp.sdk.application
from wiotp.sdk.messages import Message, MessageCodec, JsonCodec, RawCodec, Utf8Codec
from wiotp.sdk.device import DeviceClient
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import iot
from django.conf import settings
from django.core.cache import cache
from datetime import datetime


def send(msg):
    subject = 'ALERT MOISTURE-CONTENT'
    message = render_to_string('email.html',{'content':msg})
    email=EmailMessage(subject,message,from_email='cloud_iot@gmail.com',to=['baljotsinghchoudhary@gmail.com','rohit04445@gmail.com'])
    email.content_subtype = "html"
    email.send()

#For reading last event on Sensor
def readSensor():
  
    appClient =wiotp.sdk.application.ApplicationClient(settings.MY_CONFIG_IOT)
    eventId = "iotsensor"
    # Get the last event using a python dictionary to define the device
    device = {"typeId": "sensors", "deviceId": "sensor1"}
    lastEvents = appClient.lec.get(device,eventId)
    event=(base64.b64decode(lastEvents.payload).decode('utf-8'))
    # eval() convert string to dictionary
    parsed_data= json.loads(event)
    useful_data=dict()
    useful_data['temperature']=round(parsed_data['d']['temperature'])
    useful_data['humidity']=round(parsed_data['d']['humidity'])
    useful_data['moisture']=round(parsed_data['d']['moisture'])
    iot_instance= iot()
    iot_instance.information=useful_data
    iot_instance.save()

    if(useful_data['moisture']<10):
        send("less than the threshold i.e. less than 10%")
    elif(useful_data['moisture']>85):
        send("more than the threshold i.e. greater than 85%")

    return useful_data


#For Reading LAst Event at Motor

def readMotor():

    appClient =wiotp.sdk.application.ApplicationClient(settings.MY_CONFIG_MOTOR)
    eventId = "status"
    # Get the last event using a python dictionary to define the device
    device = {"typeId": "motor", "deviceId": "motor1"}
    lastEvents = appClient.lec.get(device,eventId)
    event=(base64.b64decode(lastEvents.payload).decode('utf-8'))
    # eval() convert string to dictionary
    parsed_data=json.loads(event)

    return parsed_data['d']['status']
  

#For Sending Event to Motor 

def sendCommand(cmd):

   client =DeviceClient(config=settings.MY_CONFIG_SEND)
   # Connect
   client.connect()
   # Send Data
   myData={'d' : {'status':cmd }}
   client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=2, onPublish=None)
   # Disconnect
   client.disconnect()
   return ;

def getSensordata():
    result=None
    try:
        result=cache.get('IotStatus')
        if result is None:
            result=iot.objects.latest('timestamp').information
            cache.set('IotStatus',result,timeout=5*60)
    except Exception as e:
        result={'temperature':0,'humidity':0,'moisture':0}
    return result


def getmotorStatus():
    result=cache.get('MotorStatus')
    if result is None:
        result=readMotor();
        cache.set('MotorStatus',result,timeout=None)
    return result
    
def getweatherStatus():
    result=cache.get('WeatherStatus')
    if result is None:
        response= requests.get(settings.API_URL)
        data=response.json();
        result=[]
        for i in range(15):
            result.append({'timestamp':datetime.fromtimestamp(data['list'][i]['dt']).strftime("%d/%m %H:%M"),'temp':round((data['list'][i]['main']['temp']-273.15),2),'humidity':round(data['list'][i]['main']['humidity'],2),'wind_speed':round(data['list'][i]['wind']['speed'],2),
              'type_of_weather':data['list'][i]['weather'][0]['description'],'icon':data['list'][i]['weather'][0]['icon']})   
        
        cache.set('WeatherStatus',result,timeout=10*60)
    return result

def hardupdate():
    readSensor()
    cache.delete('IotStatus')
    cache.delete('WeatherStatus')
    cache.delete('MotorStatus')
    getSensordata()
    getmotorStatus()
    getweatherStatus()
