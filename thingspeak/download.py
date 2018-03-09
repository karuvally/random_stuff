#!/usr/bin/env python3
# fetch data from ThingSpeak
# Copyright 2018, Aswin Babu Karuvally

# get the serious stuff
import requests


# fetch data from ThingSpeak
def fetch_data():
    response = requests.get('https://api.thingspeak.com/channels/443375/feeds.json?api_key=9H7M1245D2MTWUJV&results=2')
    retrieved_data = response.json()
    print(retrieved_data)


# run the function
fetch_data()
