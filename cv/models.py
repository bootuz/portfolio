from django.db import models

# Create your models here.


class PersonalProject(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Technology(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return f'{self.name}'


class SourceCode(models.Model):
    service = models.CharField(max_length=180)
    url = models.URLField()

    def __str__(self):
        return f'{self.service}'


class Experience(models.Model):
    company_name = models.CharField(max_length=180)
    city = models.CharField(max_length=20, blank=True)
    url = models.URLField()
    source_code = models.ForeignKey(SourceCode, on_delete=models.CASCADE, blank=True)
    position = models.CharField(max_length=250)
    personal_projects = models.ManyToManyField(PersonalProject, blank=True)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    date_started = models.DateField()
    date_finished = models.DateField()

    def __str__(self):
        return f'{self.company_name}'


class Education(models.Model):
    university_name = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)
    date_started = models.DateField()
    date_finished = models.DateField()

    def __str__(self):
        return f'{self.university_name}'


class Language(models.Model):
    CHOICES = (
        ('Elementary', 'Elementary'),
        ('Intermediate', 'Intermediate'),
        ('Upper-intermediate', 'Upper-intermediate'),
        ('Advanced', 'Advanced'),
        ('Native', 'Native')
    )

    language = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f'{self.language}'


class SocialMedia(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='icons')
    url = models.URLField()

    def __str__(self):
        return f'{self.name}'


class CV(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='photo', blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    social_media = models.ManyToManyField(SocialMedia, blank=True)
    bio = models.TextField(blank=True)
    experience = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    languages = models.ManyToManyField(Language)
    technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'Resumes'


