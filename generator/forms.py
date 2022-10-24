from django.forms import models
from django import forms


class MyPasswordForm(forms.Form):
    kinds = ((5, 5), (6, 6), (7, 7),
             (8, 8), (9, 9), (10, 10),
             (11, 11), (12, 12), (13, 13),
             (14, 14), (15, 15), (16, 16),
             (17, 17), (18, 18), (19, 19),
             (20, 20))
    length = forms.ChoiceField(label='Choose length', initial=(10, 10), choices=kinds)
    uppercase = forms.BooleanField(label='Uppercase', initial=False, required=False)
    numbers = forms.BooleanField(label='Numbers', initial=False, required=False)
    special = forms.BooleanField(label='Special', initial=False, required=False)
