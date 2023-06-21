# Generated by Django 4.2 on 2023-04-03 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('date_published', models.DateTimeField(blank=True, null=True, verbose_name='published since')),
                ('date_published_end', models.DateTimeField(blank=True, null=True, verbose_name='published until')),
                ('date_featured', models.DateTimeField(blank=True, null=True, verbose_name='featured date')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='djangocms_blog_post_author', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
    ]
