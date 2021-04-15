import threading

import requests
import json
import webbrowser
googlekey="AIzaSyDt0xXUuQ_T82f8RL_dR0go7IMzCKJUnBM"

def getGooglePlaces(_latlng):
    reqUrl='https://maps.googleapis.com/maps/api/geocode/json?latlng='+_latlng+'&sensor=false&key='+googlekey
    ret = requests.get(reqUrl)
    dictinfo = json.loads(ret.text)
    if len(dictinfo["results"])==0:
        return ""
    return dictinfo["results"][0]["formatted_address"]

def openMap(_place):
    reqUrl = 'https://maps.googleapis.com/maps/api/staticmap?center=' + _place + '&zoom=10&size=800x800&key=' + googlekey
    webbrowser.open(reqUrl)
