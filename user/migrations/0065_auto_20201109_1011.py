# Generated by Django 3.1.1 on 2020-11-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0064_externalresourcecredentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalresourcecredentials',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
