# Generated by Django 4.2.5 on 2023-09-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='job_position',
        ),
    ]