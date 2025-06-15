from django import forms
from .models import CoiffeuseFreelance, ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'message']


        
class CoiffeuseFreelanceForm(forms.ModelForm):
    class Meta:
        model = CoiffeuseFreelance
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'prenom': forms.TextInput(attrs={'placeholder': 'Votre prénom'}),
            'situation_matrimoniale': forms.Select(choices=[
                ('célibataire', 'Célibataire'),
                ('mariée', 'Mariée'),
                ('fiancée', 'Fiancée'),
                ('autre', 'Autre')
            ]),
            'a_des_enfants': forms.Select(choices=[
                ('non', 'Non'),
                ('oui', 'Oui')
            ]),
            'nombre_enfants': forms.NumberInput(attrs={'min': 0, 'placeholder': "Nombre d'enfants"}),
            'lieu_habitation': forms.TextInput(attrs={'placeholder': 'Votre ville / quartier'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}),
            'contact_urgence': forms.TextInput(attrs={'placeholder': 'Téléphone urgence'}),
            'competences': forms.Textarea(attrs={'placeholder': 'Décrivez vos compétences en coiffure...'}),
            'disponibilites': forms.TextInput(attrs={'placeholder': 'Ex : Lundi à samedi, sauf mercredi'}),
        }