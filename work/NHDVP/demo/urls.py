from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^testdata/$', views.testDataView.as_view()),
    url(r'^testhtml/$', views.testHtmlView.as_view()),
]
