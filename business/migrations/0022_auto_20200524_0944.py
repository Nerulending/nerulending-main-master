# Generated by Django 3.0.5 on 2020-05-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0021_businesscreditsteps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesscreditsteps',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='businesscreditsteps',
            name='updated_at',
        ),
    ]