# Generated by Django 5.1.6 on 2025-06-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0031_alter_imagegalerie_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='miseenrelationaccueil',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
