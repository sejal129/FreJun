from django.contrib import admin
from .models import User_Details, Login_Details, Candidate_Details, Document

admin.site.register(User_Details)
admin.site.register(Login_Details)
admin.site.register(Candidate_Details)
admin.site.register(Document)