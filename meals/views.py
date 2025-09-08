from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import login as login
from .forms import SignUpForm


# Create your views here.
# views.py



def register(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request,'register.html' , {'form' : form })


def home(request):    
    return render(request, 'home.html')


def meal_recommendations(request):
    input = request.GET['disease']
    disease = Disease.objects.get(name__iexact = input)  
    if input is not None:
        meals = disease.meals.all() 
    return render(request, 'meals.html', {
        'meal': meals,   'disease' :disease,
    })

    

