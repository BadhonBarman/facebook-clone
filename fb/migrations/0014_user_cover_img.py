# Generated by Django 4.0.5 on 2022-07-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0013_rename_user_mobile_user_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover_img',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]
