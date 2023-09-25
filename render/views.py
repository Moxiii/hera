from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home_page_view(request):
    return HttpResponse("La vue api est ici : http://127.0.0.1:8000/api/Sneaker/")