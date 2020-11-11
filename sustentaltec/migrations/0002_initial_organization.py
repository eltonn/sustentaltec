# Generated by Django 3.0.6 on 2020-08-18 02:22

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Organization = apps.get_model("sustentaltec", "Organization")
    db_alias = schema_editor.connection.alias
    Organization.objects.using(db_alias).bulk_create(
        [Organization(name="Main Company", location="localhost")]
    )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Country = apps.get_model("sustentaltec", "Organization")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).filter(
        name="Main Company", location="localhost"
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sustentaltec', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
