from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from render.SearchForm import SearchForm
from api.models import Sneaker
from django.core.cache import cache 
@login_required
def home_page_view(request):
    return render(request,'index.html')

def search(request,user_token):
    results = cache.get(user_token)

    if results is not None:
        return render(request, 'recherche.html', {'results': results})
    else:
        return HttpResponse('Aucun résultat trouvé pour cet identifiant utilisateur.')