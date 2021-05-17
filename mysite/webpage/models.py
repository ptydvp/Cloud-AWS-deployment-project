from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class restaurant_type(models.Model):
    type_name = models.CharField(max_length=50)

class restaurant(models.Model):
    restaurant_type_id = models.ForeignKey(restaurant_type, on_delete=models.CASCADE, default='')
    location_address = models.CharField(max_length=200)
    restaurant_name = models.CharField(max_length=50)
    seller_phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    own_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    OPEN = 'OP'
    CLOSE = 'CL'
    Restaurant_TODAY = (
        (OPEN,'open'),
        (CLOSE,'close'),
        )
    restaurant_status = models.CharField(
        max_length=2,
        choices=Restaurant_TODAY,
        default=OPEN,
    )


class restaurant_menu(models.Model):
    menu_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='menu_image', blank=True)
    menu_price = models.FloatField()
    restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

# class order_list(models.Model):
#     desc = models.CharField(max_length=200)
#     unit = models.CharField(max_length=10)
#     unit_price = models.FloatField()
#     order_order_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class customer(models.Model):
#     rs = (
#         (1, "reserve"),
#         (2, "no"),
#     )
#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     cus_phone = models.CharField(max_length=10)
#     resecus_status = models.IntegerField(choices=rs)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class admin(models.Model):
#     contact = models.CharField(max_length=50)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class comment(models.Model):
#     comment_detail = models.TextField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant_id = models.ForeignKey(restaurant, on_delete=models.CASCADE)

# class admin_customer(models.Model):
#     customer_user_id = models.ForeignKey(customer, on_delete=models.CASCADE)
#     admin_user_id = models.ForeignKey(admin, on_delete=models.CASCADE)

# class menu_order_list(models.Model):
#     menu_menu_id = models.ForeignKey(restaurant_menu, on_delete=models.CASCADE)
#     order_list_list_id = models.ForeignKey(order_list, on_delete=models.CASCADE)