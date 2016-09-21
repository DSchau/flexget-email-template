#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader, Template
from json import loads as load_json

import flexget_templates as custom_templates

env = Environment(loader=FileSystemLoader('dist'))

for template in dir(custom_templates):
  if template.startswith('filter_'):
    env.filters[template.split('filter_')[-1]] = getattr(custom_templates, template)

template = env.get_template('html-dschau.template')

rendered = template.render(load_json(open('mock/template.json').read())).strip()

output = open('dist/index.html', 'w')
output.write(rendered)
output.close()

print 'dist/index.html templated'
