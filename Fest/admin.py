from django.contrib import admin

from Event.models import Event
from .models import Fest


# @admin.register(Fest)
# class FestAdmin(admin.ModelAdmin):
#     list_display = ('organizer', 'name', 'website', 'start_date', 'end_date',)
#     list_filter = ('events',)
#     search_fields = ('fest_name',)
#

admin.register(Fest)
