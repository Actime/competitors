# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""
# Imports
from rest_framework import serializers
from .models import Competitor, Authentication, Register, TimeReg, Team

"""
Competitor Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class CompetitorSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta : 
        model = Competitor
        fields = ( 
            'id', 
            'name', 
            'second_name',
            'birth_date',
            'city',
            'state',
            'country',
            'zip_code',
            'address',
            'address2',
            'email',
            'user', 
            'sex', 
            'phone_number',
            'timestamp',
            'updated',
        )
    # End of Meta class
    
# End of Competitor Serializer class

"""
Authentication Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class AuthenticationSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta : 
        model = Authentication
        fields = ( 
            'id',
            'competitor',
            'user',
        )
    # End of Meta class
    
# End of Authentication Serializer class

"""
Register Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class RegisterSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta : 
        model = Register
        fields = ( 
            'id',
            'competitor',
            'competition',
            'category',
            'competitor_num',
            'user',
            'register_state',
            'kit_state',
        )
    # End of Meta class
    
# End of Register Serializer class


"""
TimeReg Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Competitors
"""
class TimeRegSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta : 
        model = TimeReg
        fields = ( 
            'id',
            'register',
            'time',
        )
    # End of Meta class
    
# End of TimeReg Serializer class

class TeamSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serialziers information
    """
    class Meta :
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'city', 
            'state',
            'country',
            'user',
        )
    # End of meta class
    
# End of TeamSerializer class