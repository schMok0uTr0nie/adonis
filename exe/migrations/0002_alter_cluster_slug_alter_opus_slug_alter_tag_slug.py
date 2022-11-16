# Generated by Django 4.1.3 on 2022-11-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='opus',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
    ]