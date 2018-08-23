# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse('how are you')
	return render(request,'homepage/index.html')


# Create your views here.
