from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from adr_app import predict

# Create your views here.
@csrf_exempt
def home(request):

   if request.method == "GET":
      return render(request,'index.html')
   
   if request.method == "POST":
      result = predict.process(request.POST)
      return render(request,'response.html',{"result":result})

   
