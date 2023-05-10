# Generated by Django 4.1.7 on 2023-05-10 12:57

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, height_field='_height', upload_to=blog.models.update_filename, width_field='_width'),
        ),
    ]
