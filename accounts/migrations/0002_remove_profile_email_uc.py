# Generated by Django 2.2.2 on 2019-07-27 17:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="email_uc",
        ),
    ]
