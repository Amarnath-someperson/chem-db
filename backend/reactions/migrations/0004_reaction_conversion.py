# Generated by Django 5.0.3 on 2024-03-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0003_rename_reactions_reaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='conversion',
            field=models.CharField(default='null', max_length=250),
            preserve_default=False,
        ),
    ]