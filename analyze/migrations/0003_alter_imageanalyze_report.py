# Generated by Django 4.0.4 on 2022-05-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0002_report_imageanalyze'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageanalyze',
            name='report',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='analyze.report'),
        ),
    ]
