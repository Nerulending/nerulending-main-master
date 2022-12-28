# Generated by Django 3.0.5 on 2021-01-03 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0049_auto_20201208_1800'),
        ('orders', '0022_auto_20201217_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradelineorder',
            name='whitelabel_portal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic.Subdomain'),
        ),
        migrations.AlterField(
            model_name='usersteps',
            name='whitelabel_portal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic.Subdomain'),
        ),
    ]