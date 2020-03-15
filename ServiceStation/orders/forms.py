from django import forms
from django.contrib.auth.models import User
from django.forms import Select
from .models import Order
from account.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'vin')
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('type', 'message')
        labels = {
            'type': ('Select type of service')
        }
        help_texts = {
            'message':'Leave us information about your problem'
        } 

class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('type', 'status', 'price')
