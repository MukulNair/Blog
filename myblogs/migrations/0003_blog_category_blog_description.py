# Generated by Django 5.0.1 on 2024-01-15 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0002_blog_category_blog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_category',
            name='blog_description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]