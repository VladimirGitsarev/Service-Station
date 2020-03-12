# Generated by Django 3.0.3 on 2020-03-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='Unknown', max_length=20),
            preserve_default=False,
        ),
    ]