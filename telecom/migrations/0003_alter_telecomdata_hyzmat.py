# Generated by Django 5.0.6 on 2024-05-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecom', '0002_telecomdata_delete_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telecomdata',
            name='hyzmat',
            field=models.CharField(choices=[('wifi', 'WiFi'), ('ip', 'IP')], max_length=20, verbose_name='Hyzmaty saýlaň'),
        ),
    ]
