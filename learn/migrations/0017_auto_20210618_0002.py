# Generated by Django 3.1.7 on 2021-06-17 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0016_auto_20210618_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='user_details',
            new_name='userDetails',
        ),
    ]
