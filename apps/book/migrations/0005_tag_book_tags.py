# Generated by Django 5.0.6 on 2024-07-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0004_alter_book_authors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="tags",
            field=models.ManyToManyField(related_name="book", to="book.tag"),
        ),
    ]
