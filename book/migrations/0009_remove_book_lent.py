# Generated by Django 5.0.3 on 2024-03-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_book_lent_alter_book_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='lent',
        ),
    ]
