from django.contrib import admin
from models import *

class RickrollStoryAdmin(admin.ModelAdmin):
    list_display = ('fake_title', 'views')

admin.site.register(RickrollStory, RickrollStoryAdmin)