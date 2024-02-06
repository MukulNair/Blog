# Generated by Django 5.0.1 on 2024-01-16 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0006_subscribedusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date created')),
            ],
        ),
        migrations.DeleteModel(
            name='SubscribedUsers',
        ),
    ]
