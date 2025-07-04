# Generated by Django 5.1.6 on 2025-06-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HC_site', '0020_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apropos_HC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_apropos_hc/')),
                ('mis_a_jour_le', models.DateTimeField(auto_now=True)),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contenu Apropos HC',
                'verbose_name_plural': 'Contenus Apropos HC',
            },
        ),
    ]
