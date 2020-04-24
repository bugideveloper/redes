from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from inicio.views import *

app_name="inicio"

urlpatterns = [
	path('',principal,name='principal'),
	path('tabla/',tabla,name='tabla'),
]