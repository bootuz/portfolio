# Generated by Django 3.0.3 on 2020-02-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postimage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_images',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
