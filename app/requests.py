# from app import app
import urllib.request,json
from .models import Sources

# Getting api key
api_key = None
# Getting the source base url
sources_base_url= None

def configure_request(app):
    global api_key,sources_base_url
    api_key = app.config['NEWS_API_KEY']
    sources_base_url = app.config['SOURCES_BASE_URL']

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = sources_base_url.format(category, api_key)

	with urllib.request.urlopen(get_sources_url,data=None) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results

def process_sources(sources_results):
	'''
	Function  that processes the sources result and transform them to a list of Objects
	Args:
	sources_results: A list of dictionaries that contain sources details
	Returns :
	sources_list: A list of sources objects
	'''
	sources_list = []
	for source_item in sources_results:
		id = source_item.get('id')
		name = source_item.get('name')
		description = source_item.get('description')
		url = source_item.get('url')
		category = source_item.get('category')

		source_object = Sources(id,name,description,url,category)
		sources_list.append(source_object)

	return sources_list    