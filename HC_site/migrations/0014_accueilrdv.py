# Generated by Django 5.1.6 on 2025-06-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0013_imagegalerie'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccueilRdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_ligne_1', models.CharField(max_length=255, verbose_name='Titre - ligne 1')),
                ('titre_ligne_2', models.CharField(max_length=255, verbose_name='Titre - ligne 2')),
                ('titre_ligne_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre - ligne 3')),
                ('titre_ligne_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titre - ligne 4')),
                ('texte_bouton', models.CharField(max_length=100, verbose_name='Texte du bouton')),
                ('lien_bouton', models.URLField(blank=True, null=True, verbose_name='Lien du bouton')),
                ('image', models.ImageField(upload_to='image_Apropos_accueil/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Accueil - Rendez-vous',
                'verbose_name_plural': 'Accueil - Rendez-vous',
            },
        ),
    ]
