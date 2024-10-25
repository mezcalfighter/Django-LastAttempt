from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello world from views.py")

def index(request):
    return render(request,"index.html",{
        'message':'Listado de Productos',
        'title':'Productos',
        'products':[
            {'title':'Playera','price':5,'stock':True,}, #producto
            {'title':'Camisa','price':7,'stock':True,}, 
            {'title':'Mochila','price':20,'stock':False,}, 
            {'title':'Laptop','price':500,'stock':True,}, 
        ],
    })