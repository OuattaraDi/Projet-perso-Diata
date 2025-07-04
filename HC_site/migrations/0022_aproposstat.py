# Generated by Django 5.1.6 on 2025-06-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0021_apropos_hc'),
    ]

    operations = [
        migrations.CreateModel(
            name='AproposStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icone', models.CharField(blank=True, help_text="Facultatif : Nom d'icône CSS ou emoji.", max_length=100)),
                ('valeur', models.PositiveIntegerField(help_text='Valeur numérique à afficher.')),
                ('suffixe', models.CharField(blank=True, help_text='Ex: k, +, %, etc.', max_length=10)),
                ('label', models.CharField(help_text='Texte descriptif sous le chiffre (ex: Clients satisfaits).', max_length=255)),
                ('ordre', models.PositiveIntegerField(default=0, help_text="Ordre d'affichage dans la section.")),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('mis_a_jour_le', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Statistique À propos',
                'verbose_name_plural': 'Statistiques À propos',
                'ordering': ['ordre'],
            },
        ),
    ]
