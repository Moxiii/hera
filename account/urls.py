from django.urls import path
from account.views import * 
urlpatterns = [
    path('/dashboard',Dashboard.as_view() , name='dashboard')
]
