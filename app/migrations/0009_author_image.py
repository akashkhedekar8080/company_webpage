# Generated by Django 5.0 on 2025-05-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
