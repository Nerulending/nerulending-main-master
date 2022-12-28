# Generated by Django 3.0.5 on 2020-05-06 18:56

from django.db import migrations


def create_portals(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Portal = apps.get_model("user", "Portal")
    db_alias = schema_editor.connection.alias
    Portal.objects.all().delete()
    Portal.objects.using(db_alias).bulk_create([
        Portal(name="Build business credit with no personal guarantee", code="business_credit_with_nopg"),
        Portal(name="Get a long term business loan", code="long_term_loan"),
        Portal(name="Access immediate credit for your business", code="imediate_business_credit"),
        Portal(name="Fix/Build my personal credit", code="fix_personal_credit"),
        Portal(name="Learn how to market my business", code="business_marketing"),
        Portal(name="Repair my business credit", code="repair_business_credit"),
        Portal(name="Get services you offer", code="services_you_offer"),
        Portal(name="Get business insurance", code="business_insurance"),
        Portal(name="Need a merchant account", code="need_merchant_account"),
        Portal(name="Offering financing to customers", code="offer_financing2_customers"),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0018_portal_code'),
    ]

    operations = [
        migrations.RunPython(create_portals),
    ]
