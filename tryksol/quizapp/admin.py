from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User , Category , Quiz , Option , Result

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Option)
admin.site.register(Result)