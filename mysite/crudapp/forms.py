from django import forms
from .models import Berita

class BeritaForm(forms.ModelForm):
    class Meta:
        model = Berita
        fields = ['judul', 'isi', 'kategori']