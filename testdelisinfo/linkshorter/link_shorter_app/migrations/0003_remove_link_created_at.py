# Generated by Django 3.2.3 on 2021-05-18 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_shorter_app', '0002_alter_link_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='created_at',
        ),
    ]
