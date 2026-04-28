from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html',{})

def details_page(request):
    return render(request, 'details.html',{})

def projects_page(request):
    data = Projects.objects.all()
    return render(request, 'projects.html',{'data':data})

def contact_page(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if not name or not email or not message:
            messages.error(request, "please fill the form")
        else:
            Contact.objects.create(name=name,email=email,message=message)
            messages.success(request, "Form submitted successfully")
            return redirect('contact')
    return render(request, 'contact.html') 