# Generated by Django 3.2.3 on 2022-12-04 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_remove_club_club_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
    ]