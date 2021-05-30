from django.shortcuts import render, get_object_or_404
from .models import User_Details,Login_Details, Document
from .forms import DocumentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.validators import FileExtensionValidator
from django.template import RequestContext
from .serializers import loginSerializer
from rest_framework.views

def welcome(request):
    return render(request,'welcome.html')

def login(request):
    return render(request,'login.html')

def signUp(request):
    return render(request,'signUp.html')

def enterData(request):
    if request.method=="POST":
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        emailAddress=request.POST['email']
        password=request.POST['Password']
        contactNumber=request.POST['contactNumber']
        userData=User_Details()
        userData.firstName=firstName
        userData.lastName=lastName
        userData.emailAddress=emailAddress
        userData.password=password
        userData.contactNumber=contactNumber
        userData.save()
        return render(request,'login.html')
    else:
        return render(request,'signUp.html')


def userLogin(request):
    if request.method=="POST":
        emailAddress=request.POST['emailAddress']
        password=request.POST['password']
        loginData=Login_Details()
        loginData.emailAddress=emailAddress
        loginData.password=password
        loginData.save()
        return render(request,'home.html')
    else:
        return render(request,'login.html')


def uploadData(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['formFile'])
            newdoc.save()
            messages.info(request, 'File Uploaded Successfully')
            return render(request, 'home.html')

        else:
            form = DocumentForm() 
    messages.info(request, 'No file uploded.')
    return render(request, 'home.html')


def showData(request):
    pass