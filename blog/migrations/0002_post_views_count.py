# Generated by Django 3.0.8 on 2020-07-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
