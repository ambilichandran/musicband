# Generated by Django 5.1.1 on 2024-10-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_alter_book_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.TextField(null=True),
        ),
    ]
