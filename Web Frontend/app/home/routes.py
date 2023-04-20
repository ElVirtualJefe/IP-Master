# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
#@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@blueprint.route('/<module>/<template>')
#@login_required
def route_template(template,module=None):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        if module != None:
            prefix = f'home/{module}/'
            segment = f'{module}-{segment}'
        else:
            prefix = 'home/'

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template(prefix + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
