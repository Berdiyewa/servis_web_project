from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TelecomData
from .forms import TelecomDataForm


def index(request):
    return render(request, 'telecom/index.html')


def detail(request):
  if request.method == 'POST':
    form = TelecomDataForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = TelecomDataForm()
  # Fix: Use parentheses to create a dictionary
  context = {'form': form}
  return render(request, 'telecom/details.html', context)



