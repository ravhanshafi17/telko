from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Mid_level_User)
admin.site.register(Low_level_User)
admin.site.register(High_level_User)