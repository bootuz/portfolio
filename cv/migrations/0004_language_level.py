# Generated by Django 3.0.3 on 2020-02-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20200210_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='level',
            field=models.CharField(default='', max_length=20),
        ),
    ]