from django.contrib import admin
from .models import Profile,Challenge,Blog,Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Challenge)
admin.site.register(Blog)
admin.site.register(Comment)
