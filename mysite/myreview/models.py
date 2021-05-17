from django.db import models
from django.contrib.auth.models import User
from webpage.models import restaurant
# Create your models here.
class Review(models.Model):
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "(%s) (%s) %s" %(self.user.username, self.restaurant.restaurant_name, self.comment)
