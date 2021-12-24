from django.contrib import admin

# Register your models here.
from .models import Thread, Community, UserProfile, Comment, Reply

admin.site.register(Thread)
admin.site.register(Community)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Reply)