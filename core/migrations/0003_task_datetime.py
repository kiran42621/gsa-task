# Generated by Django 4.1 on 2024-05-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datetime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]