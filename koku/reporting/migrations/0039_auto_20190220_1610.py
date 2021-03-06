# Generated by Django 2.1.5 on 2019-02-20 16:10

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0038_auto_20190220_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCPAWSStorageLineItemDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.CharField(max_length=50, null=True)),
                ('cluster_alias', models.CharField(max_length=256, null=True)),
                ('namespace', models.CharField(max_length=253)),
                ('pod', models.CharField(max_length=253)),
                ('node', models.CharField(max_length=253)),
                ('resource_id', models.CharField(max_length=253, null=True)),
                ('persistentvolumeclaim', models.CharField(max_length=253)),
                ('persistentvolume', models.CharField(max_length=253)),
                ('storageclass', models.CharField(max_length=50, null=True)),
                ('usage_start', models.DateTimeField()),
                ('usage_end', models.DateTimeField()),
                ('persistentvolumeclaim_capacity_bytes', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('persistentvolumeclaim_capacity_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('volume_request_storage_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('persistentvolumeclaim_usage_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('persistentvolume_labels', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('persistentvolumeclaim_labels', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('line_item_type', models.CharField(max_length=50)),
                ('usage_account_id', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=50)),
                ('usage_type', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('availability_zone', models.CharField(max_length=50, null=True)),
                ('usage_amount', models.FloatField(null=True)),
                ('normalization_factor', models.FloatField(null=True)),
                ('normalized_usage_amount', models.FloatField(null=True)),
                ('currency_code', models.CharField(max_length=10)),
                ('unblended_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('unblended_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('blended_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('blended_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('public_on_demand_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('public_on_demand_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('tax_type', models.TextField(null=True)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'db_table': 'reporting_ocpawsstoragelineitem_daily',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OCPAWSUsageLineItemDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.CharField(max_length=50, null=True)),
                ('cluster_alias', models.CharField(max_length=256, null=True)),
                ('namespace', models.CharField(max_length=253)),
                ('pod', models.CharField(max_length=253)),
                ('node', models.CharField(max_length=253)),
                ('resource_id', models.CharField(max_length=253, null=True)),
                ('usage_start', models.DateTimeField()),
                ('usage_end', models.DateTimeField()),
                ('pod_usage_cpu_core_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_request_cpu_core_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_limit_cpu_core_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_usage_memory_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_request_memory_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_limit_memory_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('node_capacity_cpu_cores', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('node_capacity_cpu_core_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('node_capacity_memory_bytes', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('node_capacity_memory_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('cluster_capacity_cpu_core_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('cluster_capacity_memory_byte_seconds', models.DecimalField(decimal_places=6, max_digits=24, null=True)),
                ('pod_labels', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('line_item_type', models.CharField(max_length=50)),
                ('usage_account_id', models.CharField(max_length=50)),
                ('product_code', models.CharField(max_length=50)),
                ('usage_type', models.CharField(max_length=50, null=True)),
                ('operation', models.CharField(max_length=50, null=True)),
                ('availability_zone', models.CharField(max_length=50, null=True)),
                ('usage_amount', models.FloatField(null=True)),
                ('normalization_factor', models.FloatField(null=True)),
                ('normalized_usage_amount', models.FloatField(null=True)),
                ('currency_code', models.CharField(max_length=10)),
                ('unblended_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('unblended_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('blended_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('blended_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('public_on_demand_cost', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('public_on_demand_rate', models.DecimalField(decimal_places=9, max_digits=17, null=True)),
                ('tax_type', models.TextField(null=True)),
                ('tags', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
            options={
                'db_table': 'reporting_ocpawsusagelineitem_daily',
                'managed': False,
            },
        ),
        migrations.RemoveIndex(
            model_name='ocpawscostlineitemdailysummary',
            name='cost_pod_labels_idx',
        ),
        migrations.RenameField(
            model_name='ocpawscostlineitemdailysummary',
            old_name='pod_labels',
            new_name='openshift_labels',
        ),
        migrations.AddField(
            model_name='ocpawscostlineitemdailysummary',
            name='shared_projects',
            field=models.IntegerField(default=1),
        ),
        migrations.AddIndex(
            model_name='ocpawscostlineitemdailysummary',
            index=models.Index(fields=['resource_id'], name='cost_summary_resource_idx'),
        ),
        migrations.AddIndex(
            model_name='ocpawscostlineitemdailysummary',
            index=django.contrib.postgres.indexes.GinIndex(fields=['openshift_labels'], name='cost_labels_idx'),
        ),
    ]
