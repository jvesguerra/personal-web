# Generated by Django 5.1.4 on 2024-12-05 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_person_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="person",
            table="people",
        ),
    ]