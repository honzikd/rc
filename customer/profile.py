# -*- coding: utf-8 -*-

from django import forms
from models import Customer
from registration.forms import RegistrationForm

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="Jméno") 
    last_name = forms.CharField(label="Příjmení")
    address = forms.CharField(label="Adresa")
    city = forms.CharField(label="Město")
    zip = forms.IntegerField(label="PSČ", min_value=10000, max_value=79999)
    date_of_birth = forms.DateField(label="Datum narození")

    def save(self, user):
        try:	
            data = user.get_profile()
        except:
            data = Customer(user=user)
            
        print 'Inside save method of UserRegForm'
        
        data.first_name = self.cleaned_data["first_name"]
        data.last_name = self.cleaned_data["last_name"]
        data.address = self.cleaned_data["address"]
        data.city = self.cleaned_data["city"]
        data.zip = self.cleaned_data["zip"]
        data.date_of_birth = self.cleaned_data["date_of_birth"]
        data.save()
        

class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(label="Jméno") 
    last_name = forms.CharField(label="Příjmení")
    address = forms.CharField(label="Adresa")
    city = forms.CharField(label="Město")
    zip = forms.IntegerField(label="PSČ", min_value=10000, max_value=79999)
    date_of_birth = forms.DateField(label="Datum narození")