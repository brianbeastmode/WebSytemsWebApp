from django.contrib import admin
from .models import Thread, Comments, Tags, UserProfile
# Register your models here.


class ThreadAdmin(admin.ModelAdmin):
    readonly_fields = ['user']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        Thread.user = request.user
        return super().get_form(request, obj, **kwargs)


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comments)
admin.site.register(Tags)
admin.site.register(UserProfile)