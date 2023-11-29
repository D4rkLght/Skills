from django.contrib import admin

from skills.models import ResourceLibrary, Skill, SkillGroup, Specialization

admin.site.register(ResourceLibrary)
admin.site.register(SkillGroup)
admin.site.register(Specialization)
admin.site.register(Skill)
