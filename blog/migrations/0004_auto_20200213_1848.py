# Generated by Django 3.0.3 on 2020-02-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200213_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_images',
            field=models.ManyToManyField(to='blog.PostImages'),
        ),
    ]