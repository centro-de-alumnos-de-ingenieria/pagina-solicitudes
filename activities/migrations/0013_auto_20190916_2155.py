# Generated by Django 2.2.2 on 2019-09-17 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("activities", "0012_auto_20190916_2155"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activity",
            name="space",
        ),
        migrations.AddField(
            model_name="activity",
            name="space_1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="space_1",
                to="activities.Space",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="space_2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="space_2",
                to="activities.Space",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="space_3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="space_3",
                to="activities.Space",
            ),
        ),
    ]
