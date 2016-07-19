# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Monday, January 4, 2016
"""

# Imports
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from states.models import KitState, RegisterState
from events.models import Competition, Category

"""
Competitor
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class Competitor( models.Model ) :
    # See UML definition for fields
    name = models.CharField( max_length = 200, default = '' )
    second_name = models.CharField( max_length = 200, default = '' )
    birth_date = models.DateField( blank = True, default = '1992-05-05' )
    city = models.CharField( max_length = 500, default = '' )
    state = models.CharField( max_length = 500, default = '' )
    country = models.CharField( max_length = 500, default = '' )
    zip_code = models.IntegerField( default = 0 )
    address = models.CharField( max_length = 500, default = '' )
    address2 = models.CharField( max_length = 500, default = '', blank=True )
    email = models.EmailField( max_length = 500, blank=True, unique = True, default='' )
    user = models.ForeignKey( User, default = 1 )
    # Phone regex validation
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$', message="Número de teléfono incorrecto." )
    phone_number = models.CharField( max_length = 200, validators=[phone_regex], blank=True, default='' )
    # The sex choices
    SEX_CHOICES = (
        (0, 'M'),
        (1, 'F'),    
    )# End of sex choices
    sex = models.IntegerField(choices=SEX_CHOICES, default=0)
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Stringable function """
        return ( "{0} {1}" ).format( self.name, self.second_name )
    #End of unicode function
    
# End of Competitor model

"""
Authentication
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class Authentication( models.Model ) :
    # See UML definition for fields
    competitor = models.ForeignKey( Competitor, default = 1 )
    user = models.ForeignKey( User, default = 1, unique=True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Stringable function """
        return ( "[{0}]-[{1}]-[{2}]" ).format( self.pk, self.competitor, self.user )
    #End of unicode function
    
# End of Authentication model

"""
Team - a team for registration
Model class 
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class Team( models.Model ) :
    
    name = models.CharField( max_length = 200, default = '', unique=True )
    description = models.TextField( max_length = None, default = '' )
    
    city = models.CharField( max_length = 500, default = '' )
    state = models.CharField( max_length = 500, default = '' )
    country = models.CharField( max_length = 500, default = '' )
    
    user = models.ForeignKey( User, default = 1 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Stringable function """
        return self.name
    #End of unicode function
    
# End of Team model class

"""
Register
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class Register( models.Model ) :
    # See UML definition for fields
    competitor = models.ForeignKey( Competitor, default = 1 )
    competition = models.ForeignKey( Competition, default = 1 )
    category = models.ForeignKey( Category, default = 1 )
    competitor_num = models.IntegerField( default = 0 )
    user = models.ForeignKey( User, default = 1 )
    register_state = models.ForeignKey( RegisterState, default = 1 )
    kit_state = models.ForeignKey( KitState, default = 1 )
    team = models.ForeignKey( Team, default=1 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Stringable function """
        return ( "{0} {1} {2}" ).format( self.competitor, self.competition, self.competitor_num )
    #End of unicode function
    
# End of Register model

"""
TimeReg - time register
Model class 
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class TimeReg( models.Model ) :
    # See UML definition for fields
    register = models.ForeignKey( Register, default = 1 )
    time = models.TimeField( blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Stringable function """
        return ( "{0} {1}" ).format( self.register, self.time )
    #End of unicode function
    
# End of TimeReg model