from django.shortcuts import render
from django.http import HttpResponse


def greeting_page(request):
    return render(request, 'home/greeting_page.html')


def sign_in_page(request):
    return render(request, 'home/sign_in_page.html')


def profile_page(request):
    return render(request, 'home/profile_page.html')


def send_email(request):
        return render(request, 'home/send_email.html')
