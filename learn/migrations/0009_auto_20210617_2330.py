# Generated by Django 3.1.7 on 2021-06-17 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0008_auto_20210617_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
