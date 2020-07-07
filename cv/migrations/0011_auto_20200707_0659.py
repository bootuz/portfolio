# Generated by Django 3.0.3 on 2020-07-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20200707_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='personal_projects',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='source_code',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='technologies',
        ),
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(default='null', upload_to='cv'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CV',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='PersonalProject',
        ),
        migrations.DeleteModel(
            name='SourceCode',
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
    ]
