from django.contrib import admin

# Register your models here.
from cv.models import CV, Language, Technology, Education, Experience, SourceCode, PersonalProject, SocialMedia


class CVAdmin(admin.ModelAdmin):
    filter_horizontal = ['experience', 'education', 'languages', 'technologies', 'social_media']


class ExperienceAdmin(admin.ModelAdmin):
    filter_horizontal = ['personal_projects', 'technologies']


admin.site.register(CV, CVAdmin)
admin.site.register(Language)
admin.site.register(Technology)
admin.site.register(Education)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(SourceCode)
admin.site.register(PersonalProject)
admin.site.register(SocialMedia)
