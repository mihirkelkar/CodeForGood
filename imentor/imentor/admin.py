from django.contrib import admin

from imentor.models import Message
from imentor.models import Tag
from imentor.models import UserProfile

admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(Tag)