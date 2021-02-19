from django.contrib import admin

# Register your models here.
from .models import Image, currentevent, newsfeed, User

admin.site.register(Image)
admin.site.register(currentevent)
admin.site.register(newsfeed)
# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')


