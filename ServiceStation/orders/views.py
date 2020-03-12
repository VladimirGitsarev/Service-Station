from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def orders(request):
    return render(request, 'orders.html', {'section':'orders'})