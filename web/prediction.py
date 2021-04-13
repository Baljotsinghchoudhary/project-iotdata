import _pickle as c
import os
from django.conf import settings

def load(file_name):
    # Used for reading the data from the file having the data
    with open(file_name, 'rb') as f:
        clf = c.load(f)
    return clf

def predicting(SoilMoisture,Temperature,Humidity,Time):
    print(settings.BASE_DIR)
    clf_entropy = load(os.path.join(settings.PROJECT_DIR, 'model.mdl'))#add the address here
    kk = [[SoilMoisture, Temperature, Humidity, Time]]
    answer = clf_entropy.predict(kk)
    if answer[0] == 0:
        return "OFF"
    else:
        return "ON"

