from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Tags, Comments, Thread
from .forms import ThreadForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth  import authenticate, logout, login
from django.contrib.auth.decorators import login_required




def signup(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
        
    else:
        f = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'signup.html', context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponseRedirect('/')
            else: 
                messages.error(request,"Invalid credentials!")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "You are  logged out.")
    return redirect('/')

@login_required
def addThread(request):
    submitted = False

    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-post?submitted=True')
    
    form = ThreadForm
    context = {
        'form' : form
    }
    return render(request, 'add_post.html', context)


def home(request):
    post = Thread.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'home.html', context)
