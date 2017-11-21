# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))