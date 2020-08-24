from django.shortcuts import render
from django.core.mail import send_mail


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
            ['emperornabhith@gmail.com'],
            fail_silently=False
        )
    return render(request, 'contact.html')


def happyCustomers(request):
    return render(request, 'happyCustomers.html')
