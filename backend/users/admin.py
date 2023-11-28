from django.contrib import admin

from users.models import UserProfile, UserSkill, User

admin.site.register(User)

admin.site.register(UserProfile)
admin.site.register(UserSkill)
