from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def context_hehe(request):
    return {'userCreationForm': UserCreationForm(request.POST),
            }