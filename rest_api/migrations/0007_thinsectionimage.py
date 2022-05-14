# Generated by Django 4.0.4 on 2022-05-14 18:20

from django.db import migrations, models
import django.db.models.deletion
import thin.storage.image_storage


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_rename_thin_section_thinsection_thin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThinSectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('image', models.FileField(blank=True, default=None, storage=thin.storage.image_storage.ClientDocsStorage(), upload_to='')),
                ('thin_sections_plots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rest_api.thinsection')),
            ],
        ),
    ]