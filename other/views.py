from django.shortcuts import render
from django.core.mail import send_mail
from .models import Customer
from django.template.defaulttags import register


@register.filter
def get_range(value):
    return range(value)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        msg = request.POST["msg"]
        send_mail(
            'Message from website',
            f'Somebody sent you a message through your Pebblwave website. \n \n Name: {name} \n Email: {email} \n \n Message: {msg}',
            'rayanshgupta1406@gmail.com',
            ['rashi@stexports.com'],
            fail_silently=False
        )
    return render(request, 'contact.html')


def happyCustomers(request):
    customers = Customer.objects.all()
    return render(request, 'happyCustomers.html', {'customers': customers, 'length': len(customers)})
