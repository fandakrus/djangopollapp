from django.shortcuts import render

import socket
import json


def index(request):
    return render(request, 'Basic/index.html', context={'data': []})


def controls(request):
    return render(request, 'Basic/controls.html', context={})


def trigger(request):
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))
    x = {
        "Pawel": 1, 
        "humidity": 8
    }
    data = json.dumps(x)
    print(data)
    s.sendall(data.encode('utf-8'))
    return render(request, 'Basic/controls.html', context={})