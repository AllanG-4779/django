from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import UserForms


# Create your views here.
def Register(request):
    if request.method == "POST":
        form = UserForms.UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save(commit=True)

            return redirect("login")
    else:
        form = UserForms.UserRegistration()

    return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
    # the instance parameter is used for populating the current logged in user
    if request.method == 'POST':
        user_update = UserForms.UserUpdate(request.POST, instance=request.user)
        profile_update = UserForms.UpdatePhoto(request.POST,request.FILES,instance=request.user.profile)

        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            messages.success(request, "Profile Updated successfully")
            print('success')
            return redirect("user-profile")

    else:
        user_update = UserForms.UserUpdate(instance=request.user)
        profile_update = UserForms.UpdatePhoto(instance=request.user.profile)
    context = {
        "user_update":user_update,'profile':profile_update
    }


    return render(request, "users/profile.html", context)
