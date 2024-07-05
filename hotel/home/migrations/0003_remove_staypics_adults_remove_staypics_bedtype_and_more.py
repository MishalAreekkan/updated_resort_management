# Generated by Django 5.0.6 on 2024-07-05 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staypics',
            name='adults',
        ),
        migrations.RemoveField(
            model_name='staypics',
            name='bedtype',
        ),
        migrations.RemoveField(
            model_name='staypics',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='staypics',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='staypics',
            name='children',
        ),
        migrations.AddField(
            model_name='staypics',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.myuser'),
            preserve_default=False,
        ),
    ]
