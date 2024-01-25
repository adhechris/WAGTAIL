# Generated by Django 4.0.7 on 2022-10-10 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0015_add_more_verbose_names"),
        ("wagtailsearch", "0003_remove_editors_pick"),
    ]

    operations = [
        migrations.CreateModel(
            name="SearchPromotion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.page",
                        verbose_name="page",
                    ),
                ),
                (
                    "query",
                    # Changed in Wagtail 6.0. This was previously a foreign key to
                    # wagtailsearch.query, but that table doesn't exist any more (and we can't
                    # force this migration to run before its deletion, because the searchpromotions
                    # app can be installed at any time). Instead, we arbitrarily point it to
                    # wagtailcore.page - this is fine, because any project that's running this
                    # migration under Wagtail>=6.0 will subsequently run searchpromotions migration
                    # 0005, which will change it to point to wagtailsearchpromotions.query.
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="editors_picks",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "verbose_name": "Search promotion",
                "ordering": ("sort_order",),
            },
        ),
    ]