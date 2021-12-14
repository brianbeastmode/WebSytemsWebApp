from django.shortcuts import render, redirect, get_object_or_404
from .models import Tags, Comments, Thread
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.http import HttpResponse


from .decorators import unauthenticated_user, authenticated_user

@unauthenticated_user
def home(request):
    post = Thread.objects.all()
    context = {
        'posts' : post
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

def logout(request):
    auth.logout(request)
    return redirect('/home')

def vote(request):
   thread_id = int(request.POST.get('id'))
   vote_type = request.POST.get('type')
   vote_action = request.POST.get('action')

   thread = get_object_or_404(Thread, pk=thread_id)

   thisUserUpVote = thread.userUpVotes.filter(id = request.user.id).count()
   thisUserDownVote = thread.userDownVotes.filter(id = request.user.id).count()

   if (vote_action == 'vote'):
      if (thisUserUpVote == 0) and (thisUserDownVote == 0):
         if (vote_type == 'up'):
            thread.userUpVotes.add(request.user)
         elif (vote_type == 'down'):
            thread.userDownVotes.add(request.user)
         else:
            return HttpResponse('error-unknown vote type')
      else:
         return HttpResponse('error - already voted', thisUserUpVote, thisUserDownVote)
   elif (vote_action == 'recall-vote'):
      if (vote_type == 'up') and (thisUserUpVote == 1):
         thread.userUpVotes.remove(request.user)
      elif (vote_type == 'down') and (thisUserDownVote ==1):
         thread.userDownVotes.remove(request.user)
      else:
         return HttpResponse('error - unknown vote type or no vote to recall')
   else:
      return HttpResponse('error - bad action')


   num_votes = thread.userUpVotes.count() - thread.userDownVotes.count()

   return HttpResponse(num_votes)