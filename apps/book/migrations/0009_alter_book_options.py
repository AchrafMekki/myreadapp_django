# Generated by Django 5.0.6 on 2024-07-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0008_alter_bookauthor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "default_related_name": "%(app_label)s_%(model_name)s",
                "ordering": ("title",),
            },
        ),
    ]
