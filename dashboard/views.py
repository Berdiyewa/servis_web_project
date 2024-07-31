from django.http import HttpResponse
from telecom.models import TelecomData  # Use absolute import if both modules are in the same directory level
from django.shortcuts import render, redirect


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def tables(request):
    telecom_data = TelecomData.objects.all()
    return render(request, 'dashboard/tables.html', {'telecom_data': telecom_data})


def billing(request):
    return render(request, 'dashboard/billing.html')


def notifications(request):
    return render(request, 'dashboard/notifications.html')


def profile(request):
    return render(request, 'dashboard/profile.html')


def base_sign(request):
    return render(request, 'dashboard/base_sign.html')


def signin(request):
    return render(request, 'dashboard/sign-in.html')


def signup(request):
    return render(request, 'dashboard/sign-up.html')



# def TelecomData_list(request):
#     telecom_data = TelecomData.objects.all()
#     return render(request, 'dashboard/tables.html', {'telecom_data': telecom_data})

