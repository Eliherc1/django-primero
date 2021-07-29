from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.

#def index(request):
#    return HttpResponse("this is the equivalent of @app.route('/')!")

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number} ")

def destroy(request, number):
    return redirect("/blogs")

def bonus(request):
    info=[
        {'Titulo': 'Blogs' , 'Blog_num:': '1'} ,
        {'Titulo': 'Paginas' , 'Pag_num:': '2'}
    ]
    return JsonResponse({'inf': info})