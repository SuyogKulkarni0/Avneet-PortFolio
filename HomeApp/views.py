from django.shortcuts import render, HttpResponse
from HomeApp.models import Contact;
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("This is Home page Content from HttpResponse Method!!")

def about(request):
    a = 12;
    res = a*a;
    context={
        "Value": res
    }
    #context is a dictionary used to pass values from
    # models to templates that can be displayed on webpage's frontend
    # you've to use the same key name used here in the .html file to access it's value.
    return render(request,"about.html",context)
    # return HttpResponse("This is our About Page !!")

def dailysoaps(request):
    return render(request,"dailysoaps.html")

def advertisements(request):
    return render(request,"advertisements.html")

def movies(request):
    return render(request,"movies.html")

def albums(request):
    return render(request,"albums.html")

def contri(request):
    return render(request,"contri.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name');
        email = request.POST.get('email');
        print(name);
        print(email);
        contact = Contact(name=name,email=email);
        contact.save();
        messages.success(request,"Your Contact has been sent !!")
    return render(request,"contact.html")