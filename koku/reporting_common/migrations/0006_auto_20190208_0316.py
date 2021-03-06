# Generated by Django 2.1.5 on 2019-02-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_common', '0005_auto_20181127_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportcolumnmap',
            name='report_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reportcolumnmap',
            name='provider_column_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='reportcolumnmap',
            unique_together={('report_type', 'provider_column_name')},
        ),
    ]
