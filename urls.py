# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Sunday, January 31, 2016
"""
# Imports
from django.conf.urls import patterns, url
from .views import *

# General Url patterns
urlpatterns = patterns(
    'competitors.views',
    # Competitors 
    url( r'^(?P<pk>[0-9]+)$', competitor_detail, name='views.competitor.detail' ),
    # The fucken dashboard
    url( r'^u/$', competitor_dashboard, name='views.competitor.dashboard' ),
    # The event regsitration ea ea
    url( r'^register/(?P<pk>[0-9]+)$', competitor_registration, name='views.competitor.registration' ),
    
)# End of general sytem url patterns