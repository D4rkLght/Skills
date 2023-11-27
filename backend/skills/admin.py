from django.contrib import admin

from skills.models import ResourceLibrary, SkillGroup, Specialization, PostLevel, Skill

# Register your models here.
admin.site.register(ResourceLibrary)
admin.site.register(SkillGroup)

admin.site.register(Specialization)
admin.site.register(Skill)

admin.site.register(PostLevel)
