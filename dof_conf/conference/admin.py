from django.contrib import admin

from .models import Speaker, ScheduleItem


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_active', 'created', 'modified')
    list_filter = ('is_active',)
    search_fields = ('name',)
    date_hierarchy = 'created'


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker', 'datetime', 'is_active', 'created',
                    'modified')
    list_filter = ('is_active', 'datetime')
    search_fields = ('title', 'speaker__name')
    date_hierarchy = 'datetime'
