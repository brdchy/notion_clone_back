# Generated by Django 5.0.6 on 2024-05-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notion_app', '0002_alter_project_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='name',
            field=models.CharField(default='sasha', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='sasha', max_length=255),
        ),
    ]
