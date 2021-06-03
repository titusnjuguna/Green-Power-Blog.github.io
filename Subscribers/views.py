from django.shortcuts import render
from Young_Proj.settings import EMAIL_HOST_USER
from . import forms
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject= "Confirm your Account"
        message= "Welcome to green power Inc. where carbon meets its competitor "
        recepient=str(sub['Email'].value())
        send_mail(subject, message,EMAIL_HOST_USER,recepient, fail_silently=False)
        return render(request,'Subscribers/success.html', {'recepient':recepient})
    return render(request,'Subscribers/index.html' , {'form':sub}) 





  
    











