# Generated by Django 3.1.6 on 2021-03-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210313_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='orerplaced',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
    ]