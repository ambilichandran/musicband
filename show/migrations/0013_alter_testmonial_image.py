# Generated by Django 5.1.2 on 2024-11-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0012_testmonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmonial',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
