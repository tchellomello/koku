# Generated by Django 2.1.5 on 2019-01-25 01:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0023_awscostentrylineitemdailysummary_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCPUsagePodLabelSummary',
            fields=[
                ('key', models.CharField(max_length=253, primary_key=True, serialize=False)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=253), size=None)),
            ],
            options={
                'db_table': 'reporting_ocpusagepodlabel_summary',
            },
        ),
    ]
