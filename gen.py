import pandas
import json
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader('main', 'templates'), autoescape=select_autoescape(['html','xml']))
				  
with open('projects.json', 'r') as reader:
    projects = json.load(reader)

template = env.get_template('base.html')
template.stream(projects=projects).dump('index.html')