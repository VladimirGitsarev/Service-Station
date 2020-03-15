from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderForm, OrderAdminForm, CarForm
from account.models import Car
from .models import Order
from django.http import HttpResponseRedirect
from account.models import Profile
from django.core.mail import send_mail
import datetime
# Create your views here.
@login_required 
def orders(request):
    if request.user.is_superuser:
        orders = Order.objects.order_by('-created_at')
    else:
        orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'orders.html', {'section':'orders', 'orders':orders})

@login_required
def appointment(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        car_form = CarForm(request.POST)
        if order_form.is_valid():
            new_order = order_form.save(commit=False)
            new_order.user = request.user
            new_order.profile = Profile.objects.get(id=request.user.id)
            new_order.status = 'Waiting'
            if not request.user.car.count():
                new_car = car_form.save(commit=False)
                new_car.user = request.user
                new_car.save()
                new_order.car = new_car
            else:
                new_order.car = Car.objects.get(id=request.POST.get('car-select'))
            new_order.save()
        return HttpResponseRedirect('/orders/')
    else:
        car_form = CarForm()
        order_form = OrderForm()
        cars = request.user.car.all() 
        return render(request, 'appointment.html', {'section':'appointment', 'order_form':order_form, 'car_form':car_form, 'cars':cars})

@login_required
@staff_member_required
def order_edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        prev_status = order.status
        order_form = OrderAdminForm(instance=order, data=request.POST) 
        if order_form.is_valid():
            if prev_status == 'Waiting' and request.POST['status'] == 'In progress':
                car_info = order.car.make + ' ' + order.car.model + ' ' + str(order.car.year) + ' ' + order.car.vin
                subject = 'Your request accepted'
                message = "Your request for {} accepted\
                          \nWe will report you when the order is ready\
                          \nType: {}\
                          \nYour message: {}\
                          \nEstimated order cost: {}$\
                          \nAll information about your orders is avaliable in your profile: \
                          \n{}" \
                          .format(car_info, order.type, order.message, order.price, request.build_absolute_uri().replace('edit/'+str(order.id), ''))
                send_mail(subject, message, 'vladimir.gitsarev@gmail.com', [order.user.email])
            elif prev_status == 'In progress' and request.POST['status'] == 'Completed':
                order.closed_at = datetime.datetime.now()
                car_info = order.car.make + ' ' + order.car.model + ' ' + str(order.car.year) + ' ' + order.car.vin
                subject = 'Your order completed'
                message = "Your order for {} completed\
                          \nType: {}\
                          \nYour message: {}\
                          \nOrder cost: {}$\
                          \nAll information about your orders is avaliable in your profile: \
                          \n{}" \
                          .format(car_info, order.type, order.message, order.price, request.build_absolute_uri().replace('edit/'+str(order.id), ''))
                send_mail(subject, message, 'vladimir.gitsarev@gmail.com', [order.user.email])
            elif prev_status == 'Waiting' and request.POST['status'] == 'Cancelled':
                car_info = order.car.make + ' ' + order.car.model + ' ' + str(order.car.year) + ' ' + order.car.vin
                subject = 'Your order cancelled'
                message = "Your request for {} cancelled\
                          \nType: {}\
                          \nYour message: {}\
                          \nAll information about your orders is avaliable in your profile: \
                          \n{}" \
                          .format(car_info, order.type, order.message, request.build_absolute_uri().replace('edit/'+str(order.id), ''))
                send_mail(subject, message, 'vladimir.gitsarev@gmail.com', [order.user.email])
            order_form.save()
        return HttpResponseRedirect('/orders/')
    else:   
        order_form = OrderAdminForm(instance=order)
        return render(request, 'order_edit.html', {'section':'order', 'order':order, 'order_form':order_form})

