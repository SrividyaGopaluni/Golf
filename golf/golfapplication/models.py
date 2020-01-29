# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    login_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.last_name)


class SlotBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    booked_date = models.DateTimeField(default=timezone.now)
    booked_timeslot = models.TimeField(default=timezone.now)


