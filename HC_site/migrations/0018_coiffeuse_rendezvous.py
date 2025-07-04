# Generated by Django 5.1.6 on 2025-06-12 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0017_miseenrelationaccueil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coiffeuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_coiffeuse', models.CharField(help_text='Identifiant unique pour la coiffeuse (ex: aicha, nina).', max_length=50, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('localisation', models.CharField(help_text='Localisation principale de la coiffeuse (ville, quartier).', max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('specialites', models.JSONField(default=list, help_text="Liste des compétences de la coiffeuse (ex: ['Tresses africaines', 'Coupe homme']).")),
                ('disponibilites', models.CharField(help_text="Ex: 'Lundi - Samedi (9h - 18h)'", max_length=255)),
                ('note_moyenne', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('est_coiffeuse_de_la_semaine', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Coiffeuse',
                'verbose_name_plural': 'Coiffeuses',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254)),
                ('telephone_client', models.CharField(blank=True, max_length=20, null=True)),
                ('adresse_rdv', models.CharField(help_text='Adresse complète du lieu du rendez-vous (domicile, bureau, etc.).', max_length=255)),
                ('date_rdv', models.DateField()),
                ('heure_rdv', models.TimeField()),
                ('service_souhaite', models.CharField(max_length=100)),
                ('message_client', models.TextField(blank=True, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('confirme', models.BooleanField(default=False)),
                ('coiffeuse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', to='HC_site.coiffeuse')),
            ],
            options={
                'verbose_name': 'Rendez-vous',
                'verbose_name_plural': 'Rendez-vous',
                'ordering': ['date_rdv', 'heure_rdv'],
                'unique_together': {('coiffeuse', 'date_rdv', 'heure_rdv')},
            },
        ),
    ]
