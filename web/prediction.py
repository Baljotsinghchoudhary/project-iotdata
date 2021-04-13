import _pickle as c
import os
from django.conf import settings


def load(file_name):
    # Used for reading the data from the file having the data
    with open(file_name, 'rb') as f:
        clf = c.load(f)
    return clf

def predicting(SoilMoisture,Temperature,Humidity,Time):
    modelName="model64bit.mdl"  #default 64 bit model
  
    if  settings.PYTHON_BITNESS=='32bit':
        modelName="model32bit.mdl"
        
    clf_entropy = load(os.path.join(settings.BASE_DIR,modelName))#add the address here
    kk = [[SoilMoisture, Temperature, Humidity, Time]]
    answer = clf_entropy.predict(kk)
    if answer[0] == 0:
        return "OFF"
    else:
        return "ON"

