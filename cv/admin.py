from django.contrib import admin

# Register your models here.
from cv.models import SocialMedia, Profile

admin.site.register(SocialMedia)
admin.site.register(Profile)