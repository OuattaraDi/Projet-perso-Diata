# Generated by Django 5.1.6 on 2025-06-15 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0033_prestation_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('field_type', models.CharField(choices=[('text', 'Texte'), ('email', 'Email'), ('tel', 'Téléphone'), ('date', 'Date'), ('time', 'Heure'), ('textarea', 'Zone de texte'), ('select', 'Liste déroulante')], max_length=20)),
                ('required', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_soumission', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(max_length=100)),
                ('champ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='HC_site.formfield')),
            ],
        ),
        migrations.CreateModel(
            name='FieldResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.TextField()),
                ('champ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HC_site.formfield')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champs', to='HC_site.formresponse')),
            ],
        ),
    ]
