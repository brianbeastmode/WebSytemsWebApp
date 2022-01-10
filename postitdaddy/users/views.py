from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth  import authenticate, logout as lt, login
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm



# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("update_profile")
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'users/signup.html', context)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else: 
                messages.error(request,"Invalid credentials!")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'users/signin.html', context)    

@login_required
def update_profile(request):
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = request.user
            update_profile.save()
            return redirect("home")
    context = {
        'form' : form
    }    
    return render(request, "users/update_profile.html", context)

@login_required
def logout(request):
    lt(request)
    messages.info(request, "You are  logged out.")
    return redirect("home")