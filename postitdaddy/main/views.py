from django.shortcuts import get_object_or_404, render, redirect
from .models import Thread, Community, User, UserProfile, Comment, Reply
from .forms import ThreadForm, CommunityForm
from .utils import update_views
from django.contrib.auth.decorators import login_required


def home(request):
    thread = Thread.objects.all()
    comms = Community.objects.all()
    commForm = CommunityForm

    context = {
        'threads': thread,
        'comms' : comms,
        'commForm' : commForm,
    }
    return render(request, "index.html", context)
    
@login_required
def view_thread(request, slug):
    threads = get_object_or_404(Thread, slug=slug)
    userProfile = UserProfile.objects.get(user=request.user)
 
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=userProfile, content=comment)
        threads.comment.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=userProfile, content=reply)
        comment_obj.reply.add(new_reply.id)

    context = {
        'thread' : threads,
    }
    return render(request, "view_thread.html", context)

def community_view(request, slug):
    community = get_object_or_404(Community, slug=slug)
    threads = Thread.objects.filter(community = community)

    context = {
        'threads' : threads,
    }
    return render(request, "community_view.html", context)

@login_required
def addThread(request):

    if "text-post" in request.POST:
        form = ThreadForm(request.POST or None)
        if form.is_valid():
            print('valid ra sya')
            user = UserProfile.objects.get(user=request.user)
            newform = form.save(commit=False)
            newform.user = user
            newform.save()
            form.save_m2m()
            return redirect("home")
    
    if "image-post" in request.POST:
        form = ThreadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data.get("image"))
            user = UserProfile.objects.get(user=request.user)
            newform = form.save(commit=False)
            newform.user = user
            newform.save()
            form.save_m2m()
            return redirect("home")

    form = ThreadForm
    context = {
        'form' : form
    }
    return render(request, 'add_thread.html', context)
    
@login_required
def addCommunity(request):

    if request.method == 'POST':
        form = CommunityForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = CommunityForm  