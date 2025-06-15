from django import forms
from django.db import models

# Create your models here.
from django.db import models
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class SubMenuItem(models.Model):
    menu = models.ForeignKey(MenuItem, related_name="submenus", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.menu.name} → {self.name}"


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')
    prendre_rdv_url = models.URLField(blank=True, null=True)
    se_connecter_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Paramètres du site"


class Slide(models.Model):
    title = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    button_link = models.URLField(blank=True, null=True)
    background_image = models.ImageField(upload_to='slides/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    template_name = models.CharField(max_length=255, default='default.html')  # sans 'sections/'
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.page.title})"



class Apropos_accueil(models.Model):
    titre_ligne_1 = models.CharField("Titre - ligne 1", max_length=255)
    titre_ligne_2 = models.CharField("Titre - ligne 2", max_length=255)
    titre_ligne_3 = models.CharField("Titre - ligne 3", max_length=255, blank=True, null=True)
    description = models.TextField("Description de l'offre")
    texte_bouton = models.CharField("Texte du bouton", max_length=100)
    lien_bouton = models.URLField("Lien du bouton")
    image = models.ImageField("Image", upload_to="image_Apropos_accueil/")

    def __str__(self):
        return f"{self.titre_ligne_1} - {self.titre_ligne_2}"



class Apropos_salon(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100)
    etoiles = models.IntegerField(default=5)
    logo = models.ImageField(upload_to='salons_logos/', help_text="Logo du salon de coiffure")
    est_recommande = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

# votre_app/models.py


class Accueil_salon(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100)
    etoiles = models.IntegerField(default=5)
    logo = models.ImageField(upload_to='salons_logos/', help_text="Logo du salon de coiffure")
    est_recommande = models.BooleanField(default=True)

    titre_principal = models.CharField(max_length=200, default="Les salons les plus recommandés")
    texte_bouton_enregistrement = models.CharField(max_length=100, default="Inscrire un salon de coiffure")
    url_bouton_enregistrement = models.URLField(
        max_length=200,
        blank=True,
        default="/salons/inscrire/",
        help_text="URL vers laquelle le bouton d'inscription redirigera (ex: /mon-app/inscription/)"
    )

    class Meta:
        verbose_name = "Salon et Configuration de Page"
        verbose_name_plural = "Accueil_salon"
      

    def __str__(self):
        return self.nom
    
    

class Banniere(models.Model):
    texte = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Bannière Supérieure"
        verbose_name_plural = "Bannières Supérieures"

    def __str__(self):
        return self.texte

class Coiffeuse_semaine(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='promo_images/') # 'promo_images/' est le sous-dossier dans MEDIA_ROOT
    bouton_texte = models.CharField(max_length=50, default="Savoir Plus") # Texte affiché sur le bouton
    bouton_url = models.URLField(max_length=200, default="#") # Nouveau champ pour l'URL du bouton

    class Meta:
        verbose_name = "Section Coiffeuse de la semaine"
        verbose_name_plural = "Sections Coiffeuses de la semaine"

    def __str__(self):
        return self.titre

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/') # 'product_images/' est le sous-dossier dans MEDIA_ROOT

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom



class Coiffeuse_semaine1(models.Model):
    title_part1 = models.CharField(max_length=100, default="À PROPOS")
    title_part2 = models.CharField(max_length=100, default="DE NOTRE STUDIO")
    description = models.TextField(default="La danse est un art du spectacle composé de séquences de mouvements humains soigneusement sélectionnées. Ces mouvements ont une valeur esthétique et symbolique, et sont reconnus comme tels par les interprètes et les observateurs d'une culture donnée.")
    button_text = models.CharField(max_length=50, default="NOTRE HISTOIRE")
    image = models.ImageField(upload_to='uploads/', help_text="Téléchargez l'image du danseur.")

    class Meta:
        verbose_name = "Coiffeuse de la semaine Accueil"
        verbose_name_plural = "Coiffeuses de la semaine Accueil"

    def __str__(self):
        return f"{self.title_part1} {self.title_part2}"
    



class ImageGalerie(models.Model):
    titre = models.CharField(max_length=100, blank=True)  # optionnel, pour nommer l’image
    description = models.CharField(max_length=255, blank=True)  # pour alt text
    image = models.ImageField(upload_to='galerie/')  # upload local (ajoute Pillow)
    ordre = models.PositiveIntegerField(default=0)  # pour définir position dans la grille
    class Meta:
        ordering = ['ordre']  # trier par ordre

    def __str__(self):
        return self.titre or f"Image {self.pk}"
    
    
    


class AccueilRdv(models.Model):
    titre_ligne_1 = models.CharField("Titre - ligne 1", max_length=255)
    titre_ligne_2 = models.CharField("Titre - ligne 2", max_length=255)
    titre_ligne_3 = models.CharField("Titre - ligne 3", max_length=255, blank=True, null=True)
    titre_ligne_4 = models.CharField("Titre - ligne 4", max_length=255, blank=True, null=True)
    texte_bouton = models.CharField("Texte du bouton", max_length=100)
    lien_bouton = models.URLField("Lien du bouton", blank=True, null=True)
    image = models.ImageField("Image", upload_to="image_Apropos_accueil/")

    class Meta:
        verbose_name = "Accueil - Rendez-vous"
        verbose_name_plural = "Accueil - Rendez-vous"

    def __str__(self):
        parts = [self.titre_ligne_1, self.titre_ligne_2, self.titre_ligne_3, self.titre_ligne_4]
        display_parts = [part for part in parts if part]
        return " - ".join(display_parts) if display_parts else "Nouvel élément Accueil RDV"
    
    


class Temoignage(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name




class Footer(models.Model):
    principal_logo = models.ImageField(
        upload_to='footer_logos/',
        blank=True,
        null=True,
        help_text="Le logo principal du site."
    )
    social_media_logo = models.ImageField(
        upload_to='social_media_logos/',
        blank=True,
        null=True,
        help_text="Le logo utilisé pour les icônes de réseaux sociaux."
    )
    location_name = models.CharField(
        max_length=255,
        default="New York",
        help_text="Le nom de la localisation (ex: New York)."
    )

    def __str__(self):
        return f"Footer - {self.location_name}"
    

class MiseEnRelationAccueil(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='accueil/')
    url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.titre
    


class Coiffeuse(models.Model):
    id_coiffeuse = models.CharField(max_length=50, unique=True, help_text="Identifiant unique pour la coiffeuse (ex: aicha, nina).")
    nom = models.CharField(max_length=100)
    age = models.CharField(max_length=20, blank=True, null=True)
    localisation = models.CharField(max_length=200, help_text="Localisation principale de la coiffeuse (ville, quartier).")
    description = models.TextField(blank=True, null=True)
    specialites = models.JSONField(default=list, help_text="Liste des compétences de la coiffeuse (ex: ['Tresses africaines', 'Coupe homme']).")
    disponibilites = models.CharField(max_length=255, help_text="Ex: 'Lundi - Samedi (9h - 18h)'")
    note_moyenne = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    image = models.ImageField(upload_to='coiffeuses/', blank=True, null=True, help_text="Image de profil de la coiffeuse.")
    est_coiffeuse_de_la_semaine = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Coiffeuse"
        verbose_name_plural = "Coiffeuses"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class RendezVous(models.Model):
    coiffeuse = models.ForeignKey(Coiffeuse, on_delete=models.CASCADE, related_name='rendezvous')
    nom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    telephone_client = models.CharField(max_length=20, blank=True, null=True)
    adresse_rdv = models.CharField(max_length=255, help_text="Adresse complète du lieu du rendez-vous (domicile, bureau, etc.).")
    date_rdv = models.DateField()
    heure_rdv = models.TimeField()
    service_souhaite = models.CharField(max_length=100)
    message_client = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    confirme = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
        ordering = ['date_rdv', 'heure_rdv']
        unique_together = ('coiffeuse', 'date_rdv', 'heure_rdv')

    def __str__(self):
        return f"RDV avec {self.coiffeuse.nom} pour {self.nom_client} le {self.date_rdv} à {self.heure_rdv} à {self.adresse_rdv}"


class Partner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500)
    logo = models.ImageField(upload_to='partners_logos/', blank=True, null=True)

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    


class Apropos_HC(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images_apropos_hc/', blank=True, null=True)
    
    mis_a_jour_le = models.DateTimeField(auto_now=True)
    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contenu Apropos HC"
        verbose_name_plural = "Contenus Apropos HC"

    def __str__(self):
        return self.titre
    
    

class AproposStat(models.Model):
    icone = models.CharField(max_length=100, blank=True, help_text="Facultatif : Nom d'icône CSS ou emoji.")
    valeur = models.PositiveIntegerField(help_text="Valeur numérique à afficher.")
    suffixe = models.CharField(max_length=10, blank=True, help_text="Ex: k, +, %, etc.")
    label = models.CharField(max_length=255, help_text="Texte descriptif sous le chiffre (ex: Clients satisfaits).")
    ordre = models.PositiveIntegerField(default=0, help_text="Ordre d'affichage dans la section.")

    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour_le = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Statistique À propos"
        verbose_name_plural = "Statistiques À propos"
        ordering = ['ordre']

    def __str__(self):
        return f"{self.label} : {self.valeur}{self.suffixe}"


class AproposBackgroundVideo(models.Model):
    video_fond = models.FileField(
        upload_to='videos/', 
        help_text="Vidéo de fond pour la section statistiques",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Vidéo de fond - {self.video_fond.name if self.video_fond else 'Aucune vidéo'}"






class ContactInfo(models.Model):
    ICON_CHOICES = [
        ('fa-envelope', 'Email'),
        ('fa-phone', 'Téléphone'),
        ('fa-map-marker-alt', 'Adresse'),
    ]

    titre = models.CharField(max_length=100)
    contenu = models.CharField(max_length=255)
    icone = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.titre

class TeamSection(models.Model):
    titre = models.CharField(max_length=255)
    sous_titre = models.CharField(max_length=255)
    texte_bouton = models.CharField(max_length=100, default="Formulaire de contact")
    lien_bouton = models.URLField(default="#contact")
    image_background = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.titre

class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'sujet', 'message']

class MapSection(models.Model):
    map_link = models.URLField(
        max_length=500,  # pour éviter l'erreur de dépassement de caractères
        help_text="Collez ici le lien Google Maps",
        default="https://www.google.com/maps"
    )

    def __str__(self):
        return "Section Carte"


class GalerieImageComplet(models.Model):
    image = models.ImageField(upload_to='galerie/')

    def __str__(self):
        return f"Image {self.id}"
    

class RendezVous(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    prestation = models.CharField(max_length=50)
    date_rdv = models.DateField()
    heure_rdv = models.TimeField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.date_rdv}"
    

class CoiffeuseFreelance(models.Model):
    nom = models.CharField("Nom", max_length=100)
    prenom = models.CharField("Prénom", max_length=100)
    situation_matrimoniale = models.CharField("Situation matrimoniale", max_length=50)
    a_des_enfants = models.CharField("Avez-vous des enfants ?", max_length=10)
    nombre_enfants = models.PositiveIntegerField("Nombre d'enfants", null=True, blank=True)
    lieu_habitation = models.CharField("Lieu d'habitation", max_length=255)
    telephone = models.CharField("Contact principal", max_length=20)
    contact_urgence = models.CharField("Contact en cas d'urgence", max_length=20)
    competences = models.TextField("Compétences")
    disponibilites = models.CharField("Jours de disponibilité", max_length=255)
    date_inscription = models.DateTimeField("Date d'inscription", auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"