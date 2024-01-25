# Generated by Django 1.10.6 on 2017-03-24 09:12
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0037_set_page_owner_editable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="first_published_at",
            field=models.DateTimeField(
                blank=True, db_index=True, null=True, verbose_name="first published at"
            ),
        ),
    ]