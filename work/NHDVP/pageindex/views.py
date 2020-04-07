from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from utils import models
from rest_framework import serializers
import json
from collections import OrderedDict


# Create your views here.
