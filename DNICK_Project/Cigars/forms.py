from django import forms
from .models import *

class ProizvodForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(ProizvodForm,self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"]="form-control"
    class Meta:
        model= Proizvod
        exclude=("user","sifra",)

class ProdavacForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(ProdavacForm,self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"]="form-control"
    class Meta:
        model= Prodavac
        exclude = ("Ime", "Prezime",)
class KupuvacForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(KupuvacForm,self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"]="form-control"
    class Meta:
        model= Kupuvac
        exclude = ("Ime", "Prezime",)

class NarackaForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(NarackaForm,self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"]="form-control"
    class Meta:
        model= Proizvod
        exclude = ("Ime", "Prezime",)

class NajavaForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(NarackaForm,self).__init__(*args, **kwargs)
        for filed in self.visible_fields():
            filed.field.widget.atrs["class"]="form-control"
    class Meta:
        model= Najava
        exclude = ("Korisnicko_ime", "Lozinka",)