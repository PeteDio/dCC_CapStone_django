# Generated by Django 4.0 on 2021-12-21 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_alter_meal_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='datetime',
            new_name='date',
        ),
    ]