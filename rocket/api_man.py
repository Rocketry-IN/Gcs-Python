import requests
import time
import json

#3 api calls per second 


def api_call():
    r = requests.get("https://backend-gcs.onrender.com/mock/sensor-data").text
    return r

def send_command():
    requests.post("https://backend-gcs.onrender.com/mock/sensor-data", "1")