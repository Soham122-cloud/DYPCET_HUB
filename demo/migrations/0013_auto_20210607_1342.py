# Generated by Django 3.2 on 2021-06-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20210603_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='hosted',
            field=models.URLField(blank=True, null=True),
        ),
    ]
