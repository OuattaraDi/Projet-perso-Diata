from django.contrib import admin
from .models import AccueilRdv, Apropos_HC, AproposBackgroundVideo, AproposStat, Coiffeuse, Coiffeuse_semaine1, CoiffeuseFreelance, ContactInfo, ContactMessage, Footer, GalerieImageComplet, ImageGalerie, MapSection, MenuItem, MiseEnRelationAccueil, Partner, RendezVous, Slide, SubMenuItem, SiteSettings, Page, Section, Apropos_accueil, TeamSection, Temoignage

class SubMenuItemInline(admin.TabularInline):
    model = SubMenuItem
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ['order']
    inlines = [SubMenuItemInline]

admin.site.register(MenuItem, MenuItemAdmin)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('logo_preview', 'prendre_rdv_url', 'se_connecter_url')

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" style="height: 40px;" />'
        return "Aucun logo"
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo'
    

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    


class SectionInline(admin.TabularInline):  # ou admin.StackedInline si tu préfères
    model = Section
    extra = 1
    fields = ('title', 'template_name', 'order')
    ordering = ('order',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'template_name', 'order')
    list_filter = ('page',)
    ordering = ('page', 'order')



@admin.register(Apropos_accueil)
class AproposAccueilAdmin(admin.ModelAdmin):
    list_display = ("titre_ligne_1", "titre_ligne_2", "titre_ligne_3", "texte_bouton", "lien_bouton")
    search_fields = ("titre_ligne_1", "titre_ligne_2", "titre_ligne_3")


# votre_app/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import Accueil_salon

@admin.register(Accueil_salon)
class Accueil_salonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation', 'etoiles', 'est_recommande', 'apercu_logo', 'titre_principal', 'texte_bouton_enregistrement')
    list_filter = ('est_recommande', 'localisation')
    search_fields = ('nom', 'localisation', 'titre_principal')

    fieldsets = (
        ("Informations sur le Salon", {
            'fields': ('nom', 'localisation', 'etoiles', 'logo', 'est_recommande')
        }),
        ("Configuration Accueil_salon", {
            'fields': ('titre_principal', 'texte_bouton_enregistrement', 'url_bouton_enregistrement')
        }),
    )

    def apercu_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height:50px; border-radius: 50%; object-fit: cover;" />', obj.logo.url)
        return "Pas de logo"
    apercu_logo.short_description = 'Logo'


# mon_app/admin.py

from django.contrib import admin
from .models import Banniere, Coiffeuse_semaine, Produit # Assurez-vous d'importer tous vos modèles

# Enregistrez vos modèles pour les rendre visibles dans l'interface d'administration
admin.site.register(Banniere)
admin.site.register(Coiffeuse_semaine)
admin.site.register(Produit)
admin.site.register(AccueilRdv)
admin.site.register(RendezVous)
admin.site.register(CoiffeuseFreelance)



@admin.register(Coiffeuse_semaine1)
class Coiffeuse_semaine1Admin(admin.ModelAdmin):
    list_display = ('title_part1', 'title_part2', 'button_text', 'image_display')
    search_fields = ('title_part1', 'title_part2', 'description')
    readonly_fields = ('image_display',)

    def image_display(self, obj):
        if obj.image:
            return '<img src="%s" width="100" height="auto" />' % obj.image.url
        return "Pas d'image"
    
    image_display.allow_tags = True
    image_display.short_description = "Image"
    
    
@admin.register(ImageGalerie)
class ImageGalerieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'ordre', 'description')
    list_editable = ('ordre',)
    ordering = ('ordre',)
    
@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'text')
    
    
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = (
        'location_name',
        'principal_logo',
        'social_media_logo',
    )
    fieldsets = (
        (None, {
            'fields': ('principal_logo', 'social_media_logo', 'location_name',)
        }),
    )

    def has_add_permission(self, request):
        return not Footer.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return Footer.objects.exists()

@admin.register(MiseEnRelationAccueil)
class MiseEnRelationAccueilAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description',  'url')
    




@admin.register(Coiffeuse)
class CoiffeuseAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'id_coiffeuse',
        'localisation',
        'note_moyenne',
        'est_coiffeuse_de_la_semaine',
        'display_image' # <-- Ajout de la méthode pour afficher la miniature
    )
    search_fields = ('nom', 'localisation', 'specialites')
    list_filter = ('est_coiffeuse_de_la_semaine', 'note_moyenne')
    fieldsets = (
        (None, {
            'fields': ('id_coiffeuse', 'nom', 'age', 'localisation', 'description', 'image') # <-- CORRECTION ICI : 'image_url' devient 'image'
        }),
        ('Détails professionnels', {
            'fields': ('specialites', 'disponibilites', 'note_moyenne')
        }),
        ('Statut', {
            'fields': ('est_coiffeuse_de_la_semaine',)
        }),
    )

    # Méthode pour afficher la miniature de l'image dans list_display
    def display_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "(Pas d'image)"
    display_image.short_description = "Image" # Nom de la colonne dans l'admin




@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'has_logo')
    search_fields = ('name', 'description')
    list_filter = ('name',)

    def has_logo(self, obj):
        return bool(obj.logo)
    has_logo.boolean = True
    has_logo.short_description = 'Logo Existant'


@admin.register(Apropos_HC)
class Apropos_HC_Admin(admin.ModelAdmin):
    list_display = ('titre', 'mis_a_jour_le')
    search_fields = ('titre', 'description')
    fields = ('titre', 'description', 'image')



@admin.register(AproposStat)
class AproposStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'valeur', 'suffixe', 'ordre', 'mis_a_jour_le')
    list_editable = ('ordre',)
    ordering = ('ordre',)
    search_fields = ('label',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('label', 'valeur', 'suffixe', 'icone', 'ordre')
        }),
        ('Dates', {
            'fields': ('cree_le', 'mis_a_jour_le'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('cree_le', 'mis_a_jour_le')

@admin.register(AproposBackgroundVideo)
class AproposBackgroundVideoAdmin(admin.ModelAdmin):
    pass



@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'icone', 'contenu')
    list_filter = ('icone',)
    search_fields = ('titre', 'contenu')


@admin.register(TeamSection)
class TeamSectionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sous_titre', 'texte_bouton')
    search_fields = ('titre', 'sous_titre')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoye')
    search_fields = ('nom', 'email', 'sujet')
    readonly_fields = ('date_envoye',)


@admin.register(MapSection)
class MapSectionAdmin(admin.ModelAdmin):
    list_display = ('map_link',)



@admin.register(GalerieImageComplet)
class GalerieImageCompletAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    