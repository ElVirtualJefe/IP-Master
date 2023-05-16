# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import logging
from app.implementations import whoami
from inspect import currentframe

app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

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
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

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

        app_logger.debug(f'template = {template}')
        if template in ['test.html','subnets.html']:
            app_logger.debug(f'Getting CSV File')
            object_list = get_csv()
            app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
            return render_template(prefix + template, segment=segment, object_list=object_list)

        # Serve the file (if exists) from app/templates/home/FILE.html
        app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
        return render_template(prefix + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@blueprint.route('/grpc-test')
def grpc_test():
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    from app.implementations import clients
    app_logger.debug(f'clients = {clients}')
    app_logger.debug(f'{clients["ipAddress"]}')
    res = clients['ipAddress'].get_ip_address(id='ae03ddbc-f9bd-4d85-9981-a9aa9b342a70')
    app_logger.debug(f'Response = {res}')

    app_logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return render_template('home/test-grpc.html',res=res.ipAddress)


@blueprint.route('/i')
def test_index():
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    app_logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return render_template('home/index2.html')

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

def get_csv():
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    
    try:
        import csv
        from pathlib import Path

        app_logger.debug(f'CWD = {Path.cwd()}')
        csv_path = 'app/static/la-riots-deaths.csv'
        csv_file = open(csv_path, 'rt')
        csv_obj = csv.DictReader(csv_file)
        csv_list = list(csv_obj)
    except:
        app_logger.error(f'Something broke:', exc_info=True)

    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
    return csv_list

