# Generated by Django 5.1.2 on 2025-03-17 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_link', models.URLField()),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passwords.folder')),
            ],
        ),
    ]
