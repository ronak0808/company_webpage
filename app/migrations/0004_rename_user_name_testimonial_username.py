# Generated by Django 5.1.4 on 2025-01-15 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='user_name',
            new_name='username',
        ),
    ]
