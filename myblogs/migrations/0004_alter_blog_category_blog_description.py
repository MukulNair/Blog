# Generated by Django 5.0.1 on 2024-01-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0003_blog_category_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_category',
            name='blog_description',
            field=models.CharField(max_length=1000),
        ),
    ]
