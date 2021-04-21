
from django.shortcuts import render, redirect
from django.core.serializers.json import Serializer as jSerializer
import requests as r

import socket

def ss(s, *args, **kwargs):
    print('*'*100)
    print(s, args, kwargs)
    print('*'*100)

def getIndexOrNone(index):
    if index:
        data = index
    else: data = None
    return data
        


def home(request):

    ipStackApiKey = '6730878c51e9adc7a252681fb560f5b7'

    hostName = socket.gethostname()
    ipAdress = socket.gethostbyname(hostName)

    
    remote_address = request.META.get('REMOTE_ADDR')

    if (ipAdress.startswith(('127', '192', '0')) ) or (remote_address == '127.0.0.1') :
        url = f'http://api.ipstack.com/check?access_key={ipStackApiKey}'

    else:
        url = f'http://api.ipstack.com/{remote_address}?access_key={ipStackApiKey}'

    params = {} 
    data = r.get(url=url, params=params).json()

    flagUrl = getIndexOrNone(data['location']['country_flag'])
    langDetails = getIndexOrNone(data['location']['languages'][0])
    
    context = {
        'data' : data,
        'flag' : flagUrl,
        'lang' : langDetails

    }
    return render (request, 'index.html', context)