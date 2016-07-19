# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date
from .models import Competitor, Team, Authentication, Register
from events.models import Event, Competition, Category
from states.models import KitState, RegisterState
from .forms import TeamForm
import os, json

# Create your views here.
def competitor_detail( request, pk ) :
    """
    Competitor detail that shows all the info of the competitor
    """
    # get the competitor by id
    competitor = Competitor.objects.get( pk = pk )
    # Init context to send to the template
    context = {
        'competitor' : competitor,
    }# End of context variable 
    # Render the view 
    return render( request, 'Competitors/Detail.html', context )
# End of competitor_detail function

@login_required
def competitor_dashboard( request ) :
    """
    Competitor dashboard when logged in
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    menu_actives = [ "", "active", "", "", "" ]
    # Get the teams
    teams = Team.objects.filter( user = request.user.pk )
    # The user is logged in
    if request.user.is_authenticated() :
        # Get the competitor by user
        auth = Authentication.objects.get( user = request.user.id )
        # Get the next events by ret date
        next_events = Event.objects.filter(date_start__gte = date.today()).order_by('date_start')
        # Get all the events
        past_events = Event.objects.filter(date_start__lte = date.today()).order_by('-date_start')[:8]
        # Get completed events
        registrations = Register.objects.filter( competitor = auth.competitor.pk )
        # Render the view
        context = {
            'menu_actives' : menu_actives,
            'json_data' : json_data,
            'competitor' : auth.competitor,
            'next_events' : next_events,
            'registrations' : registrations,
            'past_events' : past_events,
            'recent_events' : "",
            'teams' : teams
        }
        return render( request, 'Competitors/Dashboard.html', context )
    else :
        return HttpResponseRedirect( reverse("accounts.login") )
# End of competitor_dshboard function

@login_required
def competitor_registration( request, pk ) :
    """
    Competitor registration to an event
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    menu_actives = [ "", "active", "", "", "" ]
    errors = []
    #verify if it is a post
    if request.method == 'POST' :
        # Get the category id from the template
        category = int(request.POST['category'])
        # Get the team id from the template
        team = int(request.POST['team'])
        # Get the competition id from the template
        competition = int(request.POST['competition'])
        # Validate if the variables are valid
        if not competition :
            errors.append( "Seleccione una competencia." )
        elif not category :
            errors.append( "Seleccione una categoría." )
        elif 'terms' not in request.POST  :
            errors.append( "Acepte nuestros términos y condiciones para continuar con su pago." )
        else :
            # new register
            register = Register()
            # Get the competitor by user
            auth = Authentication.objects.get( user = request.user.id )
            if not Register.objects.filter( competition = competition ).get( competitor = auth.competitor.pk ) :
                # register 
                register.competitor_num = get_competitor_number( competition )
                register.category = Category.objects.get( pk = category )
                register.competitor = auth.competitor
                register.competition = Competition.objects.get( pk = competition )
                register.user = request.user
                register.team = Team.objects.get( pk = team )
                register.register_state = RegisterState.objects.get( description = "Pagado" )
                register.kit_state = KitState.objects.get( description = "Pendiente" )
                register.save()
                # Render the view
                context = {
                    'event' : Event.objects.get( pk = pk ),
                    'title' : '',
                    'menu_actives' : menu_actives,
                    'json_data' : json_data,
                    'register' : register
                }
                return render( request, 'Competitors/Registration_complete.html', context )
            else :
                errors.append( "Usted ya se ha registrado a este evento. Revise su historial." )
    # Get all the teams from the user
    teams = Team.objects.all( )
    # The user is logged in
    if request.user.is_authenticated() :
        # Render the view
        context = {
            'event' : Event.objects.get( pk = pk ),
            'title' : '',
            'competitions' : Competition.objects.filter( competition_event = pk ),
            'menu_actives' : menu_actives,
            'json_data' : json_data,
            'teams' : teams,
            'categories' : Category.objects.all(),
            'errors' : errors
        }
        return render( request, 'Competitors/Registration.html', context )
    else :
        return HttpResponseRedirect( reverse("accounts.login") )
# End of competitor_registration function

@login_required
def team_create( request ) :
    """
    Team create view
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    #Menu actives
    menu_actives = [ "", "", "", "", "" ]
    #validate the post view
    if request.method == 'POST' :
        # Get the data from the template
        form = TeamForm( request.POST, prefix = 'form' )
        
        if form.is_valid() :
            # set the instance form the saved form
            instance = form.save( commit = False )
            # Set the teams user
            instance.user = request.user
            # Save the instance
            instance.save()
            # the context variable for info
            return HttpResponseRedirect( reverse( "views.competitor.dashboard" ) )
            
    form = TeamForm( prefix = 'form' )
    #the context variable for info
    context = {
        'form' : form,
        'menu_actives' : menu_actives,
        'json_data' : json_data,
    }
    # render template
    return render( request, 'Competitors/team_add.html', context )
    # End of validations
# End of team_create function view


def get_competitor_number( id ) :
    """
    Get function just for getting the fucking register number
    """
    # First get the competition by primary key
    competition = Competition.objects.get( pk = id )
    # Get the event by competition 
    event = Event.objects.get( pk = competition.competition_event.pk )
    # Get all the competitions by event
    competitions = Competition.objects.filter( competition_event = event.pk )
    # Init an empty list of registers
    registers = list()
    # Get all registers by each competition
    for comp in competitions :
        temporal_registers = Register.objects.filter( competition = comp.pk )
        # Verify if the temporal registers are actually not null
        if temporal_registers is not None :
            # Merge the temporal registers to the registers list
            registers = registers + [entry for entry in temporal_registers]
    # End of for
    # validate if the registers list is empty
    if len(registers) :
        # Merge all by order of timestamp
        registers.sort(key=lambda x:x.timestamp, reverse=False)
        # Get the last competitors number
        last_competitor_num = registers[-1].competitor_num
        # Return the last number plus one
        return last_competitor_num + 1
    # If there is no register return 1
    else :
        return 1
    # End of else
# End of get_copmetitor_number function