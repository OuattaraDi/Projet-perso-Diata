import json
from decimal import Decimal # Assurez-vous d'importer Decimal

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse # Importez l'encodeur de Django

from .models import (
    Accueil_salon, AccueilRdv, Apropos_HC, AproposBackgroundVideo, AproposStat, Banniere, Coiffeuse, Coiffeuse_semaine,
    Coiffeuse_semaine1, ContactInfo, ContactMessage, Footer, GalerieImageComplet, ImageGalerie, MapSection, MenuItem, MiseEnRelationAccueil, Partner,
    Produit, RendezVous, SiteSettings, Page, Slide, TeamSection, Temoignage, Apropos_accueil
)

# --- Définition de l'encodeur JSON personnalisé ---
class DecimalEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj) # Convertit Decimal en chaîne de caractères
        return super().default(obj) # Laisse Django gérer les autres types

# --- Vues ---

def home(request):
    menu_items = MenuItem.objects.prefetch_related('submenus').order_by('order')
    print(f"DEBUG: Nombre d'éléments de menu récupérés : {menu_items.count()}")

    site_settings = SiteSettings.objects.first()
    slides = Slide.objects.all().order_by('order')

    return render(request, 'menu.html', {
        'menu_items': menu_items,
        'site_settings': site_settings,
        'slides': slides
    })
    
    

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.shortcuts import render
from .models import Page  # ou le nom de ton modèle principal
from django.shortcuts import render
from .models import Page  # Assure-toi d'importer ton modèle



import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import (
    Page, Slide, Apropos_accueil, AccueilRdv, Accueil_salon, Banniere,
    Coiffeuse_semaine, Produit, Coiffeuse_semaine1, ImageGalerie, Temoignage,
    Footer, MiseEnRelationAccueil, Partner, GalerieImageComplet, MenuItem,
    SiteSettings, Coiffeuse, Apropos_HC, AproposStat, AproposBackgroundVideo,
    ContactInfo, TeamSection, MapSection, ContactMessage, RendezVous,
    CoiffeuseFreelance  # Import du modèle pour le formulaire
)
from .forms import CoiffeuseFreelanceForm  # Import du formulaire
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    sections = page.sections.order_by('order')
    slides = Slide.objects.all().order_by('order')
    aproposaccueil = Apropos_accueil.objects.first()
    accueil_rdv_content = AccueilRdv.objects.first()
    salons_recommandes = Accueil_salon.objects.filter(est_recommande=True)

    config_page = Accueil_salon.objects.first()
    titre_principal = config_page.titre_principal if config_page else "Les salons les plus recommandés"
    texte_bouton = config_page.texte_bouton_enregistrement if config_page else "Inscrire un salon de coiffure"
    url_bouton = config_page.url_bouton_enregistrement if config_page else "/salons/inscrire/"
    etoiles_ranges = {salon.id: range(salon.etoiles) for salon in salons_recommandes}

    banniere = Banniere.objects.first()
    coiffeuse_semaine_section = Coiffeuse_semaine.objects.first()
    produits = Produit.objects.all()
    coiffeuse_semaine1_content = Coiffeuse_semaine1.objects.first()

    images_galerie = ImageGalerie.objects.all()
    temoignages = Temoignage.objects.all()
    footer_settings = Footer.objects.first() or Footer(location_name="72e avenue, New York, NY 99220")

    blocs_mise_en_relation = MiseEnRelationAccueil.objects.all()
    partners = Partner.objects.all()
    images_completes = GalerieImageComplet.objects.all()
    menu_items = MenuItem.objects.prefetch_related('submenus').order_by('order')

    site_settings = SiteSettings.objects.first()

    # --- Coiffeuses JSON
    all_coiffeuses = Coiffeuse.objects.all()
    coiffeuses_list = []
    for coiffeuse_obj in all_coiffeuses:
        coiffeuse_dict = {
            'id_coiffeuse': str(coiffeuse_obj.id_coiffeuse),
            'nom': coiffeuse_obj.nom,
            'age': coiffeuse_obj.age,
            'localisation': coiffeuse_obj.localisation,
            'description': coiffeuse_obj.description,
            'specialites': coiffeuse_obj.specialites,
            'disponibilites': coiffeuse_obj.disponibilites,
            'note_moyenne': coiffeuse_obj.note_moyenne,
            'est_coiffeuse_de_la_semaine': coiffeuse_obj.est_coiffeuse_de_la_semaine,
            'image_url': coiffeuse_obj.image.url if coiffeuse_obj.image else '',
        }
        if isinstance(coiffeuse_dict['specialites'], str):
            try:
                coiffeuse_dict['specialites'] = json.loads(coiffeuse_dict['specialites'])
            except json.JSONDecodeError:
                coiffeuse_dict['specialites'] = []
        coiffeuses_list.append(coiffeuse_dict)

    # --- Apropos HC
    apropos_hc_content = Apropos_HC.objects.first()
    apropos_stats = AproposStat.objects.all() 
    video_fond = AproposBackgroundVideo.objects.first()
    contact_infos = ContactInfo.objects.all()
    team_section = TeamSection.objects.first()
    map_section = MapSection.objects.first()

    # --- Formulaire Contact
    if request.method == 'POST' and 'contact_form_submit' in request.POST:
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet', '')
        message = request.POST.get('message')

        if nom and email and message:
            ContactMessage.objects.create(
                nom=nom,
                email=email,
                sujet=sujet,
                message=message
            )
            return redirect('contact_message')
        else:
            return render(request, 'contact.html')

    # --- Prise de rendez-vous classique (form avec bouton name="prendre_rdv_submit")
    if request.method == 'POST' and 'prendre_rdv_submit' in request.POST:
        nom = request.POST.get('client_lastname')
        prenom = request.POST.get('client_firstname')
        email = request.POST.get('client_email')
        telephone = request.POST.get('client_phone')
        prestation = request.POST.get('service_type')
        date_rdv = request.POST.get('date_rd')
        heure_rdv = request.POST.get('time_rd')
        commentaire = request.POST.get('comments')

        if nom and prenom and email and prestation and date_rdv and heure_rdv:
            RendezVous.objects.create(
                nom=nom,
                prenom=prenom,
                email=email,
                telephone=telephone,
                prestation=prestation,
                date_rdv=date_rdv,
                heure_rdv=heure_rdv,
                commentaire=commentaire
            )
            return redirect('merci')

    # --- Réservation AJAX
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            data = json.loads(request.body)
            champs_obligatoires = ['coiffeuseId', 'clientName', 'clientEmail', 'rdvAddress', 'rdvDate', 'rdvTime', 'serviceType']
            if not all(data.get(field) for field in champs_obligatoires):
                return JsonResponse({'success': False, 'message': 'Veuillez remplir tous les champs obligatoires.'}, status=400)

            coiffeuse = get_object_or_404(Coiffeuse, id_coiffeuse=data['coiffeuseId'])

            rendez_vous = RendezVous.objects.create(
                coiffeuse=coiffeuse,
                nom_client=data['clientName'],
                email_client=data['clientEmail'],
                telephone_client=data.get('clientPhone', ''),
                adresse_rdv=data['rdvAddress'],
                date_rdv=data['rdvDate'],
                heure_rdv=data['rdvTime'],
                service_souhaite=data['serviceType'],
                message_client=data.get('message', '')
            )
            return JsonResponse({'success': True, 'message': 'Votre demande de rendez-vous a été envoyée !', 'rendezvous_id': rendez_vous.id})

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Requête JSON invalide.")
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Erreur serveur : {str(e)}'}, status=500)

    # --- Réservation simple (coiffeuse sélectionnée dans form)
    if request.method == 'POST' and 'formulaire_rdv_submit' in request.POST:
        try:
            coiffeuse_id = request.POST.get('coiffeuse_id')
            coiffeuse = get_object_or_404(Coiffeuse, id_coiffeuse=coiffeuse_id)

            rendez_vous = RendezVous.objects.create(
                coiffeuse=coiffeuse,
                nom_client=request.POST.get('nom_client'),
                email_client=request.POST.get('email_client'),
                telephone_client=request.POST.get('telephone_client', ''),
                adresse_rdv=request.POST.get('adresse_rdv'),
                date_rdv=request.POST.get('date_rdv'),
                heure_rdv=request.POST.get('heure_rdv'),
                service_souhaite=request.POST.get('service_souhaite'),
                message_client=request.POST.get('message_client', '')
            )
            return redirect('merci')

        except Exception as e:
            print("Erreur:", e)
            return redirect('merci.html')

    # --- NOUVEAU : Gestion du formulaire CoiffeuseFreelanceForm
    if request.method == 'POST' and 'coiffeuse_freelance_submit' in request.POST:
        form = CoiffeuseFreelanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscription-coiffeuse-reussie')  # À créer : page de succès ou une url valide
    else:
        form = CoiffeuseFreelanceForm()

    # --- Rendu final avec formulaire dans le contexte
    return render(request, 'page_detail.html', {
        'page': page,
        'sections': sections,
        'slides': slides,
        'aproposaccueil': aproposaccueil,
        'accueil_rdv_content': accueil_rdv_content,
        'salons': salons_recommandes,
        'etoiles_ranges': etoiles_ranges,
        'titre_principal': titre_principal,
        'texte_bouton': texte_bouton,
        'url_bouton': url_bouton,
        'url_bouton_global': 'https://exemple.com/formulaire',
        'texte_bouton_global': 'S’inscrire maintenant',
        'banniere': banniere,
        'coiffeuse_semaine_section': coiffeuse_semaine_section,
        'produits': produits,
        'coiffeuse_semaine1_content': coiffeuse_semaine1_content,
        'images_galerie': images_galerie,
        'temoignages': temoignages,
        'footer_settings': footer_settings,
        'blocs_mise_en_relation': blocs_mise_en_relation,
        'coiffeuses_json': json.dumps(coiffeuses_list, cls=DecimalEncoder),
        'partners': partners,
        'apropos_hc_content': apropos_hc_content,
        'apropos_stats': apropos_stats,
        'video_fond': video_fond,
        'contact_infos': contact_infos,
        'team_section': team_section,
        'map_section': map_section,
        'images_completes': images_completes,
        'menu_items': menu_items,
        'site_settings': site_settings,
        'coiffeuse_freelance_form': form,  # <-- formulaire à passer au template
    })

def accueil(request):
    page = Page.objects.filter(slug="accueil").first()
    slides = Slide.objects.all().order_by('order')
    aproposaccueil = Apropos_accueil.objects.first()
    salons_recommandes = Accueil_salon.objects.filter(est_recommande=True)
    config_page = Accueil_salon.objects.first()
    titre_principal = config_page.titre_principal if config_page else "Les salons les plus recommandés"
    texte_bouton = config_page.texte_bouton_enregistrement if config_page else "Inscrire un salon de coiffure"
    url_bouton = config_page.url_bouton_enregistrement if config_page else "/salons/inscrire/"
    etoiles_ranges = {salon.id: range(salon.etoiles) for salon in salons_recommandes}

    banniere = Banniere.objects.first()
    coiffeuse_semaine_section = Coiffeuse_semaine.objects.first()
    produits = Produit.objects.all()
    coiffeuse_semaine1_content = Coiffeuse_semaine1.objects.first()

    images_galerie = ImageGalerie.objects.all()
    temoignages = Temoignage.objects.all()
    footer_settings = Footer.objects.first() or Footer(location_name="72e avenue, New York, NY 99220")

    blocs_mise_en_relation = MiseEnRelationAccueil.objects.all()
    partners = Partner.objects.all()
    images_completes = GalerieImageComplet.objects.all()
    
    
    menu_items = MenuItem.objects.prefetch_related('submenus').order_by('order')
    print(f"DEBUG: Nombre d'éléments de menu récupérés : {menu_items.count()}")

    site_settings = SiteSettings.objects.first()
    slides = Slide.objects.all().order_by('order')

    if not page:
        return render(request, 'erreur.html', {"message": "La page 'accueil' n'existe pas encore dans la base de données."})

    sections = page.sections.order_by('order')
    return render(request, 'page_detail.html', {
        'page': page,
        'sections': sections,
        'slides': slides,
        'aproposaccueil': aproposaccueil,
        'salons': salons_recommandes,

        'salons': salons_recommandes,
        'etoiles_ranges': etoiles_ranges,
        'titre_principal': titre_principal,
        'texte_bouton': texte_bouton,
        'url_bouton': url_bouton,
        'url_bouton_global': 'https://exemple.com/formulaire',
        'texte_bouton_global': 'S’inscrire maintenant',
        'banniere': banniere,
        'coiffeuse_semaine_section': coiffeuse_semaine_section,
        'produits': produits,
        'coiffeuse_semaine1_content': coiffeuse_semaine1_content,
        'images_galerie': images_galerie,
        'temoignages': temoignages,
        'footer_settings': footer_settings,
        'blocs_mise_en_relation': blocs_mise_en_relation,

        'partners': partners,

        'images_completes': images_completes,
        'menu_items': menu_items,
        'site_settings': site_settings,
        'slides': slides
        
    })

def prendre_rdv(request):
    if request.method == 'POST':
        nom = request.POST.get('client_lastname')
        prenom = request.POST.get('client_firstname')
        email = request.POST.get('client_email')
        telephone = request.POST.get('client_phone')
        prestation = request.POST.get('service_type')
        date_rdv = request.POST.get('date_rd')
        heure_rdv = request.POST.get('time_rd')
        commentaire = request.POST.get('comments')

        # Tu peux ici enregistrer les données dans la base ou envoyer un email
        RendezVous.objects.create(
    nom=nom,
    prenom=prenom,
    email=email,
    telephone=telephone,
    prestation=prestation,
    date_rdv=date_rdv,
    heure_rdv=heure_rdv,
    commentaire=commentaire
)

        # Rediriger ou afficher un message
        return redirect('merci')  # suppose que tu as une page merci

    return render(request, 'mercu.html')  # le nom de ton template

def merci(request):
    return render(request, 'merci.html', {
        'titre_page': "Merci pour votre prise de rendez-vous",
        'message_confirmation': "Votre demande a bien été envoyée. Nous vous contacterons dans les plus brefs délais.",
    })


from django.shortcuts import render, redirect
from .models import RendezVous

def prendre_rendezvous(request):
    if request.method == 'POST':
        RendezVous.objects.create(
            nom=request.POST.get('client_lastname'),
            prenom=request.POST.get('client_firstname'),
            email=request.POST.get('client_email'),
            telephone=request.POST.get('client_phone'),
            prestation=request.POST.get('service_type'),
            date_rdv=request.POST.get('date_rd'),
            heure_rdv=request.POST.get('time_rd'),
            commentaire=request.POST.get('comments', '')
        )
        return redirect('merci')  # Crée cette page ou remplace par un message
    return render(request, 'merci.html')  # ← ton template HTML


def contact_message(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        # Enregistrer dans la base
        ContactMessage.objects.create(
            nom=nom,
            email=email,
            sujet=sujet,
            message=message
        )

        # Rediriger vers une page "contact_message"
        return redirect(reverse('contact_message'))

    return render(request, 'contact.html')