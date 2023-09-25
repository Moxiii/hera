from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from render.SearchForm import SearchForm
from api.models import Sneaker
@login_required
def home_page_view(request):
    return render(request,'index.html')

def search(request):
    form = SearchForm(request.GET)
    results = []

    # if form.is_valid():
    #     query = form.cleaned_data['query']
    #     results = Sneaker.objects.filter(name__icontains=query)

    return render(request, 'recherche.html', {'form': form})