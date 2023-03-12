from django import forms


class PurchaseForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    phone_number = forms.CharField(label="Telephone Number")
    location = forms.CharField(label="Location")
    city = forms.CharField(label="City")
    quantity = forms.IntegerField(min_value=1, label="Quantity")
    
