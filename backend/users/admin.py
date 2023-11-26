from django.contrib import admin

from users.models import UserProfile, UserSkills, User

admin.site.register(User)

admin.site.register(UserProfile)
admin.site.register(UserSkills)
