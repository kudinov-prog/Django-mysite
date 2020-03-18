from django.shortcuts import render
from django.http import HttpResponse

from .models import Adb

def adboard_list(request):
    s = 'Список заметок\r\n\r\n'
    for ad in Adb.objects.order_by('-published'):
        s += ad.title + '\r\n' + ad.content + '\r\n' + str(ad.published) + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

def index(request):
    http = '<h1>Главная</h1>'
    return HttpResponse(http)
