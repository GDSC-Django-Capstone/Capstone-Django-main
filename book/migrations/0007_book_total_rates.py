# Generated by Django 5.0.3 on 2024-03-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rates',
            field=models.IntegerField(default=0),
        ),
    ]
