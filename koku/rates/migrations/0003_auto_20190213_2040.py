# Generated by Django 2.1.5 on 2019-02-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20181205_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='metric',
            field=models.CharField(choices=[('cpu_core_usage_per_hour', 'cpu_core_usage_per_hour'), ('cpu_core_request_per_hour', 'cpu_core_request_per_hour'), ('memory_gb_usage_per_hour', 'memory_gb_usage_per_hour'), ('memory_gb_request_per_hour', 'memory_gb_request_per_hour'), ('storage_gb_usage_per_month', 'storage_gb_usage_per_month'), ('storage_gb_request_per_month', 'storage_gb_request_per_month')], default='cpu_core_usage_per_hour', max_length=256),
        ),
    ]
