from django.shortcuts import render


def index(request):
    return render(request, 'Expensify/index.html')


def add_expense(request):
    return render(request, 'Expensify/index.html')
