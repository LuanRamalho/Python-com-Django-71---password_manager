# Generated by Django 5.1.2 on 2025-03-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordentry',
            name='extra_fields',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
