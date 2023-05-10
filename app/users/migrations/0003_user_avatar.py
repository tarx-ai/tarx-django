# Generated by Django 4.1.7 on 2023-05-10 15:08

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_application_uuid_user_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/assets/image/default_avatar.png', upload_to=users.models.update_filename),
        ),
    ]
