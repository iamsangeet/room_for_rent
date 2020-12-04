from django import forms
from .models import Room,Category

class RoomForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    no_of_rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    image = forms.ImageField(),
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'})),
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Room
        fields = '__all__'
