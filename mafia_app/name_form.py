from django import forms

class Players(forms.Form):
    name_one = forms.CharField(label='Player 1 ', max_length=20)
    name_two = forms.CharField(label='Player 2 ', max_length=20)
    name_three = forms.CharField(label='Player 3 ', max_length=20)
    name_four = forms.CharField(label='Player 4 ', max_length=20)

    name_one.widget.attrs.update({'autofocus': 'autofocus'})