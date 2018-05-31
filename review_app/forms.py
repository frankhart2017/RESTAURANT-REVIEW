from django import forms

class Review(forms.Form):
    review = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'How was the food?', 'class': 'input'}))
