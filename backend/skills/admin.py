from django.contrib import admin

from skills.models import ResourceLibrary, SkillGroup, Specialization, Skill


admin.site.register(ResourceLibrary)
admin.site.register(SkillGroup)
admin.site.register(Specialization)
admin.site.register(Skill)

