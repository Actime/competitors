from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Competitor, Team
from events.models import Event, Competition, Category
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
    # The user is logged in
    if request.user.is_authenticated() :
        # Render the view
        context = {
            'menu_actives' : menu_actives,
            'menu_actives' : menu_actives,
            'json_data' : json_data,
        }
        return render( request, 'Competitors/Dashboard.html')
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
    # The user is logged in
    if request.user.is_authenticated() :
        # Render the view
        context = {
            'event' : Event.objects.get( pk = pk ),
            'title' : '',
            'competitions' : Competition.objects.filter( competition_event = pk ),
            'menu_actives' : menu_actives,
            'json_data' : json_data,
            'teams' : Team.objects.all(),
            'categories' : Category.objects.all()
        }
        return render( request, 'Competitors/Registration.html', context )
    else :
        return HttpResponseRedirect( reverse("accounts.login") )
# End of competitor_registration function