# Generated by Django 4.1.3 on 2022-11-28 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_course", "0001_initial"),
        ("app_lecturer", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="coursemodel",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app_lecturer.lecturermodel",
            ),
        ),
        migrations.AddField(
            model_name="coursemodel",
            name="students",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
