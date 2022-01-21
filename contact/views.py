from django.shortcuts import render,redirect
from . import forms
from .forms import FormName
from django.http import HttpResponse, HttpResponseRedirect
from phonenumber_field.formfields import PhoneNumberField
from django.contrib import messages

# Create your views here.
def form_name_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent')
            return redirect('contactus')

    else:
        form = FormName()



    return render(request,'contact/contactus.html',{'form':form})
