# Generated by Django 5.1 on 2024-08-29 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birhday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='birhday',
            new_name='birthday',
        ),
    ]
