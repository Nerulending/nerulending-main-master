# Generated by Django 3.1.1 on 2020-11-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0034_auto_20201109_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='basic_partnership_program_price',
            field=models.DecimalField(decimal_places=2, default=2000.0, max_digits=50, verbose_name='Basic Partnership Program Price Annual'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='premium_partnership_program_price',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=50, verbose_name='Basic Partnership Program Price Monthly'),
        ),
    ]
