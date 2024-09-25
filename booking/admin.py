from django.contrib import admin
from .models import Bus, Seat, Booking

class BusAdmin(admin.ModelAdmin):
    list_display = ('destination', 'date', 'departure_time', 'number_plate', 'price')
    search_fields = ('destination', 'number_plate')
    list_filter = ('date', 'departure_time')
    ordering = ('date', 'departure_time')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number',)
    search_fields = ('seat_number',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('receipt', 'date', 'departure_time', 'destination', 'seat_number', 'passenger', 'price', 'amount', 'paid', 'number_plate')
    search_fields = ('receipt', 'passenger', 'number_plate')
    list_filter = ('date', 'paid')
    readonly_fields = ('receipt', 'amount', 'price')

# Register the models with the admin site
admin.site.register(Bus, BusAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)
