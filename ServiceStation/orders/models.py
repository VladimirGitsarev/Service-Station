from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Car, Profile

# Create your models here.

class Order(models.Model):
    WORK_TYPE_CHOICES = [
        ('Live support','Live support'),
        ('Repair service', 'Repair service'),
        ('Complete care', 'Complete care'),
        ('Spare parts', 'Spare parts'),
        ('Sales service', 'Sales service'),
        ('Tyre service', 'Tyre service'),
        ('Other', 'Other')
    ]
    STATUS_CHOICES = (
        ('Waiting', 'Waiting'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_orders')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')
    type = models.CharField(choices=WORK_TYPE_CHOICES, max_length=50, default='Other') 
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Waiting')
    price = models.FloatField(null=True)
    message = models.TextField(max_length=250)
