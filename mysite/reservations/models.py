from django.db import models
from webpage.models import restaurant
from django.contrib.auth.models import User
# Create your models here.
class myreservation(models.Model):
    person = models.IntegerField()
    reser_day = models.DateField()
    reser_time = models.TimeField()
    reser_as = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now=True)

class reservation_accepted(models.Model):
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    PENDING = 'Pending'
    CANCEL = 'Cancel'
    Accepted_status = (
        (ACCEPTED,'accepted'),
        (REJECTED,'rejected'),
        (PENDING,'pending'),
        (CANCEL,'cancel'),
    )
    reser_status = models.CharField(
        max_length=8,
        choices=Accepted_status,
    )
    reservation = models.OneToOneField(myreservation, on_delete=models.CASCADE)