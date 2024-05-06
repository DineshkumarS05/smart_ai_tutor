# Generated by Django 4.1.7 on 2024-03-29 07:22

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_lesson_number_lesson_lesson_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_no',
            field=models.TextField(default=1, unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_video',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='lesson-video'),
        ),
    ]
