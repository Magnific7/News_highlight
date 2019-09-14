from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

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
    title = 'Home - Welcome to The best News Website '
    return render_template('index.html', title = title, business_sources = business_sources, general_sources = general_sources, entertainment_sources = entertainment_sources, technology_sources = technology_sources )

@main.route('/source/<id>')
def article(id):
	'''
	View Function that returns the source page and its data
	'''
	articles = get_articles(id)
    # sources = get_sources(id)
	title = f'Top Articles'

	return render_template('source.html',title=title,articles = articles)    

