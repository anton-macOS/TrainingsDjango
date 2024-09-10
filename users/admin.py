from django.contrib import admin
from users.models import User, UserStats

admin.site.register(User)
admin.site.register(UserStats)
