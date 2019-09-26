# Generated by Django 2.2.5 on 2019-09-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0017_space_color'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.AddField(
            model_name='activity',
            name='participants_amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Número de participantes'),
        ),
    ]