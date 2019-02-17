from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number_of_tees', 'number_of_stickers',
                    'subscribed', 'created', 'modified')
    list_filter = ('subscribed', 'created')
    search_fields = ('name', 'email')
    date_hierarchy = 'created'
