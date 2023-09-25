from django.urls import path , include
from authentification.views import *
urlpatterns = [
    path('/login',login_page,name='login'),
    path('/logout',logout_user , name='logout'),
    path('/signup', signup_page , name='signup'),
]
