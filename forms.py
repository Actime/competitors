# -*- coding: utf-8 -*-
from registration.forms import RegistrationFormUniqueEmail
from django import forms
from .models import Register, Team

"""
Authentication Registration Form
"""
class AuthenticationRegistrationForm(RegistrationFormUniqueEmail) :
    
    SEX_CHOICES = (
        (0, 'M'),
        (1, 'F'),    
    )# End of sex choices
    
    name = forms.CharField( widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Nombre' } ), label="" )
    second_name = forms.CharField( widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Apellidos' } ), label="" )
    birth_date = forms.DateField( widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'datepicker form-control input-lg','placeholder':'Selecciona fecha'}),label="")
    city = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Ciudad' } ), label="")
    state = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Estado' } ), label="")
    country = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'País' } ), label="")
    zip_code = forms.CharField( widget=forms.TextInput(attrs={ 'class' : "form-control input-lg", 'type':'number', 'placeholder':'Código postal'}), label="")
    address = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Dirección 1' } ), label="" )
    address2 = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Dirección 2' } ), label="" )
    phone_number = forms.CharField(widget=forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Teléfono' } ), label="" )
    sex = forms.ChoiceField(choices = SEX_CHOICES, label="", initial='', widget=forms.Select( attrs= { 'class' : "form-control input-lg" } ), required=True)

# End of AuthenticationRegistrationForm class

class RegisterForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta : 
        model = Register
        fields = [ 
            'competition', 
            'category',
        ]
    #End of meta class

# End of RegisterForm class

class TeamForm( forms.ModelForm ) :
    # custom description field
    name = forms.CharField( widget = forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Nombre' } ), label="" )
    description = forms.CharField( widget = forms.Textarea( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Descripción' } ), label="" )
    city = forms.CharField( widget = forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Ciudad' } ), label="" )
    state = forms.CharField( widget = forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'Estado' } ), label="" )
    country = forms.CharField( widget = forms.TextInput( attrs = { 'class' : "form-control input-lg", 'placeholder' : 'País' } ), label="" )
    """
    Meta class
    """
    class Meta :
        model = Team
        fields = [
            'name',
            'description',
            'city', 
            'state',
            'country',
        ]
    # End of meta class
    
# End of TeamForm class