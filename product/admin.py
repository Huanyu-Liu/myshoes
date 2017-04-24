from django.contrib import admin
from .models import Username,Product,Cart

# Register your models here.
class UsernameAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    fieldsets = [
        (None, {'fields': ['username']}),
        (None, {'fields': ['password'],}),
    ]

admin.site.register(Username,UsernameAdmin)
admin.site.register(Product)
admin.site.register(Cart)