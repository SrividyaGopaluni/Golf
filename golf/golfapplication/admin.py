from django.contrib import admin
from .models import User, SlotBooking


# Register your models here.

class CustomerList(admin.ModelAdmin):

    listdisplay = ('first_name', 'email', 'phone_number')
    listfilter = ('last_name', 'email')
    searchfields = ('first_name',)
    order = ['last_name']


admin.site.register(User)
admin.site.register(SlotBooking)
