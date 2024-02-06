# Generated by Django 5.0.1 on 2024-01-19 09:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0008_rename_email_subscribeduser_u_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('cover_img', models.ImageField(upload_to='images/')),
                ('blog_description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]