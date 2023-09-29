from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from authentification.models import User
from django.views import View



class Dashboard(View):   
    @staticmethod 
    def get_total_users():
        return User.objects.count()
    
    def get(self, request):
        if request.user.is_staff:
            total_users = self.get_total_users()
            return render(request, 'adminDashboard.html', {'total_users': total_users})
        else:
            return render(request,'dashboard.html')