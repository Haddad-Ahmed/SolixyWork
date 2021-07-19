from django import forms
from App1.models import Collection
from django.forms.widgets import Textarea
from bootstrap_modal_forms.forms import BSModalModelForm
import django_filters



class ADDCollectionForm(forms.ModelForm):
    class Meta:  # pr dire que je ne peux pas dupliquer la classe
         model = Collection
         fields = ('type','nom','public')
         widgets = {'besoins' : Textarea(attrs={'cols':20 , 'rows':20})}

class CollectionModelForm(BSModalModelForm):
    class Meta:  # pr dire que je ne peux pas dupliquer la classe
         model = Collection
         fields = ('type','nom','public')
         widgets = {'besoins' : Textarea(attrs={'cols':20 , 'rows':20})}

class CollectionFilter(django_filters.FilterSet):
    class Meta:
        model = Collection
        fields = ('type','nom','public')

