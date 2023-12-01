from django.contrib import admin

from users.models import UserProfile, UserSkill, User, UserResources

admin.site.register(User)
admin.site.register(UserSkill)


class EnrollmentInline(admin.StackedInline):
    """Вспомогальельный класс для отображения ресурсов пользователя."""
    model = UserResources
    extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Админка профайла пользователя."""
    inlines = [
        EnrollmentInline
    ]
