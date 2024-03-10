# Generated by Django 4.2.11 on 2024-03-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Admin', 'Admin'), ('Super-Admin', 'Super-Admin')], default='ST', max_length=30),
        ),
    ]
