# Generated by Django 4.2.5 on 2023-09-11 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='title',
            new_name='job_title',
        ),
    ]
