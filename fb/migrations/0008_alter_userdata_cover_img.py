# Generated by Django 4.0.5 on 2022-07-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0007_alter_userdata_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='cover_img',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
