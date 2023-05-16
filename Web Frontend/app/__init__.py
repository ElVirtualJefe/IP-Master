import logging
app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

from app.implementations import whoami
from inspect import currentframe

from flask import Flask

from flask_login import LoginManager
login_manager = LoginManager()


def register_extensions(app):
    #db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    from importlib import import_module

    for module_name in ('authentication', 'home'):
        app_logger.debug(f'Importing Module app.{module_name}.routes')
        module = import_module(f'app.{module_name}.routes')
        app_logger.debug(f'Registering Blueprint {module.blueprint}')
        app.register_blueprint(module.blueprint)

    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')


def create_app(name,config):
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    app = Flask(name)
    #app.config.from_object(config)

    app_logger.debug(f'Setting App configuration items')
    app.config['SECRET_KEY'] = config.get('general','SECRET_KEY')
    app.config['TESTING'] = config.get('general','TESTING')

    #app_logger.debug(f'Importing views')
    #from app import views

    register_extensions(app)
    #app.register_blueprint(github_blueprint, url_prefix="/login")    
    register_blueprints(app)

    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')
    return app


def server(config):
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    flask_app = create_app(__name__,config)

    flask_app.config.ASSETS_ROOT = '/static/assets'

    address = config.get('server','ADDRESS')
    port = config.get('server','PORT')
    debug = config.get('logging','LOG_LEVEL')

    app_logger.info(f'Starting test Web Server on {address}:{port}')
    flask_app.run(host=address,debug=bool(debug),port=int(port))


    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')


