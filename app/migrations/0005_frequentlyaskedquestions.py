# Generated by Django 5.0 on 2025-05-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_testimonial_rating_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
