# Generated by Django 3.1.7 on 2021-07-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0057_auto_20210718_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuserbio',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/avatarLogo.jpg', null=True, upload_to='static/img/'),
        ),
    ]