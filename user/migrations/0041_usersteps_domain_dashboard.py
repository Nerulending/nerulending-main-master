# Generated by Django 3.0.5 on 2020-06-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0040_auto_20200626_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersteps',
            name='domain_dashboard',
            field=models.CharField(blank=True, default='', max_length=500, null=True,
                                   verbose_name='Domain name dashboard'),
        ),
    ]
