# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 5, 2016
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Import classes 
from competitors.models import TimeReg, Register, Authentication, Competitor, Team
from events.models import Event, Competition
from helpers.imgur import *
# Import Serializers
from competitors.serializers import TimeRegSerializer, RegisterSerializer, AuthenticationSerializer, CompetitorSerializer, TeamSerializer
from events.serializers import EventSerializer, CompetitionSerializer
# Image decode shit
from PIL import Image
from base64 import *
import datetime

"""
RegisterList Api View
Object list and creation
"""
class RegisterList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Register.objects.all()
    # Serializer class
    serializer_class = RegisterSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Register List class

"""
Register by competition list
"""
class RegisterByCompetitionList( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Register.objects.all()
    # Serializer class
    serializer_class = RegisterSerializer
    # Get query set function
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the competition id from the request
        competition_id = self.request.GET['competition_id']
        # filter the objects and then return them
        return Register.objects.filter(competition=competition_id)
    # End of get_query
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    #End of list function
    
# End of Register By Compeitiion list api view

"""
Register Detail Api View
"""
class RegisterDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Register.objects.all()
    # Serializer class
    serializer_class = RegisterSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Register Detail class

"""
TimeRegList Api View
Object list and creation
"""
class TimeRegList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = TimeReg.objects.all()
    # Serializer class
    serializer_class = TimeRegSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    def create(self, request, *args, **kwargs):
        """
        Create function
        This will just work for our custom post function
        hehe pretty lazy if you ask me :)
        """
        response_data = list()
        for d_t in request.data :
            # Serialize the object we ha
            event = Event.objects.get( pk = int( d_t["event_id"] ) )
            # get competitions event
            competitions = Competition.objects.filter( competition_event = event.pk )
            register = None
            # loop for getting the right competition
            for c in competitions :
                try :
                    # find the register matching competition and competitors number
                    register = Register.objects.filter( competition = c.pk ).get( competitor_num = int(d_t["competitor_num"]) )
                except( Register.DoesNotExist ) :
                    pass # pass if shit
            # if the register exists
            if register :
                # New time register
                time_reg = TimeReg()
                # Set the register on the time register variable
                time_reg.register = register
                # format time
                d = datetime.datetime.strptime(d_t["time"], '%H:%M:%S')
                # set the time on the time register
                time_reg.time = d.time()
                # if it is saved
                try :
                    # Save the register; 
                    # working so far, serializer not working, not losin' time on that .l.
                    time_reg.save()
                    # on data field
                    data= {
                        "id" : time_reg.id,
                        "register" : time_reg.register.pk,
                        "time" : time_reg.time,
                        "timestamp" : time_reg.timestamp,
                        "updated" : time_reg.updated
                    }
                    # return the response data
                    response_data.append(data)
                except Exception as e: # otherwise
                    # On data variable the exception message
                    data = {
                        "data" : e.message()
                    }
                    # return the serialized data
                    response_data.append(data)
                # End of saved validation
            # End of register validation
            else :
                data = {
                    "data" : None
                }
                response_data.append(data)
            # End of register validation
        # End of for of all the shit
        return Response({ 'data' : response_data })
    # End of create function
# End of Time Reg List class

class TimeRegByRegisterList( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = TimeReg.objects.all()
    # Serializer class
    serializer_class = TimeRegSerializer
    # Retrieve function definition
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        register_id = self.request.GET['register_id']
        # filter the objects and then return them
        return TimeReg.objects.filter(register=register_id)
    # End of get_query
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    #End of list function
    
# End of time register by register list api view
"""
Time Reg Detail Api View
"""
class TimeRegDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = TimeReg.objects.all()
    # Serializer class
    serializer_class = TimeRegSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Time Reg Detail class

"""
AuthenticationList Api View
Object list and creation
"""
class AuthenticationList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Authentication.objects.all()
    # Serializer class
    serializer_class = AuthenticationSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Authentication List class

"""
Authentication Detail Api View
"""
class AuthenticationDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Authentication.objects.all()
    # Serializer class
    serializer_class = AuthenticationSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Authentication Detail class

"""
CompetitorList Api View
Object list and creation
"""
class CompetitorList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Competitor.objects.all()
    # Serializer class
    serializer_class = CompetitorSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function
# End of Competitor List class

"""
Competitor Detail Api View
"""
class CompetitorDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Competitor.objects.all()
    # Serializer class
    serializer_class = CompetitorSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competitor Detail class

"""
Team list 
GET; POST;
"""
class TeamList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Team.objects.all()
    # Serializer class
    serializer_class = TeamSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of team list api view

"""
Team detail 
GET; DELETE; UPDATE
"""
class TeamDetail(  generics.UpdateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Team.objects.all()
    # Serializer class
    serializer_class = TeamSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
#End of team detail api view class