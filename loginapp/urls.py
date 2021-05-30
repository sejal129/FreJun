from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signUp',views.signUp,name='signUp'),
    path('enterData',views.enterData,name='enterData'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('uploadData',views.uploadData,name='uploadData'),
    path('showData',views.showData,name='showData'),
]
