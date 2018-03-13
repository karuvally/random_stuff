#!/usr/bin/env python3
# push data to ThingSpeak
# Copyright 2018, Aswin Babu Karuvally

# get the serious stuff
import requests
import random


# the function to upload data
def upload_data():
    # generate a upload data
    upload_value = str(random.randint(1, 100))
    print('uploading the value ' + upload_value)
    requests_object = requests.get('https://api.thingspeak.com/update?api_key=AF3WSB8SADM89PS1&field1=' + upload_value)

upload_data()
