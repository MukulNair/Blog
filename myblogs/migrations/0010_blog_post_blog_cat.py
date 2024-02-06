# Generated by Django 5.0.1 on 2024-01-29 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0009_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_cat',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_category'),
            preserve_default=False,
        ),
    ]
