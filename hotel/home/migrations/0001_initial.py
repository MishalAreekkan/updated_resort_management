# Generated by Django 5.0.6 on 2024-07-05 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BookDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinePics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_time', models.CharField(choices=[('Lunch', 'Lunch'), ('Evening', 'Evening'), ('Dinner', 'Dinner')], max_length=10)),
                ('meal_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StayPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('adults', models.PositiveIntegerField(default=2)),
                ('children', models.PositiveIntegerField(default=0)),
                ('bedtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookDetails.bookingfield')),
            ],
        ),
    ]