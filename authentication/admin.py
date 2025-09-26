from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)