# Generated by Django 3.2.25 on 2024-06-13 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
