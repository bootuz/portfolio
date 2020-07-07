from django.db import models


class SocialMedia(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='icons')
    url = models.URLField()

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    name = models.CharField(max_length=180)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='photo', blank=True)
    social_media = models.ManyToManyField(SocialMedia, blank=True)
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return f'{self.name}'
