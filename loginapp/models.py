from django.db import models

class User_Details(models.Model):
    firstName = models.CharField(max_length=30,null=False)
    lastName = models.CharField(max_length=30,null=False)
    emailAddress = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=30,null=False)
    contactNumber = models.IntegerField(null=False)

class Login_Details(models.Model):
    emailAddress = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=30,null=False)

class Document(models.Model):
    documentName = models.FileField()    
    uploadDate = models.DateTimeField(auto_now_add =True)

class Candidate_Details(models.Model):
    candidateName = models.CharField(max_length=50,null=False)
    phoneNumber = models.IntegerField(null=False)
    documentName = models.CharField(max_length=20,null=False)