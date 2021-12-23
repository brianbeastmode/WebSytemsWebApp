from django.shortcuts import get_object_or_404, render
from .models import Thread, Community, UserProfile
from .utils import update_views
# Create your views here.

def home(request):
    thread = Thread.objects.all()
    comms = Community.objects.all()

    context = {
        'threads': thread,
        'comms' : comms,
    }
    return render(request, "home.html", context)

def view_thread(request, slug):
    threads = get_object_or_404(Thread, slug=slug)

    update_views(request, threads)
    context = {
        'threads' : threads,
    }
    return render(request, "view_post.html", context)

def community_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    threads = Thread.objects.filter(community = community)

    context = {
        'threads' : threads,
    }
    return render(request, "community_view.html", context)