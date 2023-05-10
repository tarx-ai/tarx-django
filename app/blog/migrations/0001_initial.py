# Generated by Django 4.1.7 on 2023-05-10 09:59

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=128)),
                ('introduction', models.CharField(max_length=128)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('mins_read', models.IntegerField(default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['uuid'], name='blog_post_uuid_a20c8f_idx'),
        ),
    ]
