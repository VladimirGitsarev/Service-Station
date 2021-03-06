# Generated by Django 3.0.3 on 2020-03-12 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('live support', 'Live support'), ('repair service', 'Repair service'), ('complete care', 'Complete care'), ('spare parts', 'Spare parts'), ('sales service', 'Sales service'), ('tyre service', 'Tyre service'), ('other', 'Other')], max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('closed_at', models.DateField()),
                ('status', models.CharField(choices=[('Cancelled', 'canceled'), ('Completed', 'completed'), ('In progress', 'in progress')], max_length=50)),
                ('price', models.FloatField()),
                ('message', models.TextField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
