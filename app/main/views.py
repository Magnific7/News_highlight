from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources
    business_sources = get_sources('business')
    general_sources = get_sources('general')
    # sport_sources = get_sources('sport')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, business_sources = business_sources, general_sources = general_sources, entertainment_sources = entertainment_sources, technology_sources = technology_sources )