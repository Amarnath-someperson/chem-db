# Generated by Django 5.0.3 on 2024-03-24 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0002_category_slug_reactions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reactions',
            new_name='Reaction',
        ),
    ]