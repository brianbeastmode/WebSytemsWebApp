from django.contrib import admin
from .models import Thread, Comments, Tags
# Register your models here.

admin.site.register(Thread)
admin.site.register(Comments)
admin.site.register(Tags)