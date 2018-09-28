# Generated by Django 2.1 on 2018-09-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20180926_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ocpusagelineitem',
            old_name='pod_usage_memory_seconds',
            new_name='pod_limit_cpu_cores',
        ),
        migrations.RenameField(
            model_name='ocpusagelineitemdaily',
            old_name='pod_usage_memory_seconds',
            new_name='pod_limit_cpu_cores',
        ),
        migrations.RenameField(
            model_name='ocpusagelineitemdailysummary',
            old_name='pod_usage_memory_seconds',
            new_name='pod_limit_cpu_cores',
        ),
        migrations.AddField(
            model_name='ocpusagelineitem',
            name='pod_limit_memory_bytes',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitem',
            name='pod_request_cpu_core_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitem',
            name='pod_request_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitem',
            name='pod_usage_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdaily',
            name='pod_limit_memory_bytes',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdaily',
            name='pod_request_cpu_core_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdaily',
            name='pod_request_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdaily',
            name='pod_usage_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='pod_limit_memory_bytes',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='pod_request_cpu_core_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='pod_request_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='ocpusagelineitemdailysummary',
            name='pod_usage_memory_byte_seconds',
            field=models.DecimalField(decimal_places=5, max_digits=17, null=True),
        ),
    ]
