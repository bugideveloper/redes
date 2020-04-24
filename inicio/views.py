from django.shortcuts import render,redirect
# Create your views here.
from inicio.views import *
import json
from django.http import StreamingHttpResponse
from inicio.models import *

def principal(request):
	archivos = Archivo.objects.all()
	context = {
		"archivos":archivos
	}
	return render(request,"index.html",context)

def tabla(request):
	if request.method == 'POST':
			received_json_data=json.loads(request.POST['data'])
			return StreamingHttpResponse('it was post request: '+str(received_json_data))
	return render(request,"index.html")