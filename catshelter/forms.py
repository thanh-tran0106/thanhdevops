from django import forms
from .models import Feline

class CatIDSearchForm(forms.Form):
   # feline_id = forms.IntegerField(label='Cat ID')
    name = forms.CharField(label='Cat Name', max_length=100)

class FelineForm(forms.ModelForm):
    class Meta:
        model = Feline
        fields = ['name', 'breed', 'coloration', 'age', 'sex', 'fav_toy', 'photo']
  # Include the photo field
