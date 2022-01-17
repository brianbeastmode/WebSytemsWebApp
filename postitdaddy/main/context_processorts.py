from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Community



def context_hehe(request):
    comms = Community.objects.all()
    return {'userCreationForm': UserCreationForm(request.POST), 'comms' : comms,
            }