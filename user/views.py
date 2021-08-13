from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages

# Create your views here.
def Register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save( commit=True)
            messages.success(request, f'Account created successfully for {username}')
            return  redirect ("see-jobs")
        else:
            messages.error(request,f'Correct the errors below first')


    else:
        form = UserCreationForm()

    return render(request,"users/register.html" ,{"form":form})

