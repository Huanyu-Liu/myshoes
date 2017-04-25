from django.contrib import admin
from .models import Username,Product,Cart
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
# class UsernameAdmin(admin.ModelAdmin):
#     list_display = ('username','password')
#     fieldsets = [
#         (None, {'fields': ['username']}),
#         (None, {'fields': ['password'],}),
#     ]

class StaffAdmin(UserAdmin):

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.filter(Q(is_staff=True) | Q(is_superuser=True))
        return qs

class CustomerAdmin(StaffAdmin):

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.exclude(Q(is_staff=True) | Q(is_superuser=True))
        return qs

admin.site.unregister(User)
admin.site.register(User, StaffAdmin)
admin.site.register(Username, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Cart)