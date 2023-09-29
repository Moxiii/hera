from django.urls import path
from account.views import * 
urlpatterns = [
    path('/profile',Dashboard.as_view() , name='profile')
]
