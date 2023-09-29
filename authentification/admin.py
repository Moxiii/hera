from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'token', 'is_staff')

    def get_queryset(self, request):
        # Surchargez la méthode pour filtrer les utilisateurs par statut d'administrateur
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True)

admin.site.register(User, CustomUserAdmin)
