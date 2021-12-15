from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

from .models import Tags, Comments, Thread
from .forms import ThreadForm
from django.contrib.auth.forms import UserCreationForm

from .decorators import unauthenticated_user, authenticated_user

@unauthenticated_user
def home(request):
    post = Thread.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'home.html', context)

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name,
                username = username, password = password1, email = email)
                user.save()
                messages.info(request, 'User created!')
            return redirect('/login')
        else:
            messages.info(request, 'Password does not match!')
            return redirect('/register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('/login')

    return render(request, 'login.html')

def signup(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')

    else:
        f = UserCreationForm()

    return render(request, 'signup.html', {'form': f})

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

def logout(request):
    auth.logout(request)
    return redirect('/home')

