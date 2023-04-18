import logging
from configparser import ConfigParser

app_logger = logging.getLogger(f'ip-master.{__name__}')
app_logger.debug(f'Entering module {__name__}')

from inspect import currentframe
from app.implementations import whoami


def _create_database_connection_uri(config):
    from urllib.parse import quote_plus as urlquote

    username = config.get('DB_USERNAME')
    password = urlquote(config.get('DB_PASSWORD'))
    dbname = config.get('DB_NAME')
    dbserver = config.get('DB_SERVER')
    dbport = config.getint('DB_PORT')

    return f"postgresql+psycopg2://{username}:{password}@{dbserver}:{dbport}/{dbname}"

def _create_database_connection(config):
    app_logger.debug('Inside function app._create_database_connection')

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker,scoped_session
    from app.models import db

    try:

        SQLALCHEMY_DATABASE_URI = _create_database_connection_uri(config)
        SQLALCHEMY_TRACK_MODIFICATIONS = False

        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        db.create_all(engine)

        Session = scoped_session(sessionmaker(bind=engine))
        app_logger.debug(f'{engine.url}')

        app_logger.debug('Leaving function app._create_database_connection')
        return Session()

    except:
        app_logger.critical('Database configuration failed - Terminating Application',exc_info=True)
        raise 'Database configuration failed'



def test(config = ConfigParser()):
    app_logger.debug('Inside function app.test')

    SESSION = _create_database_connection(config['postgres'])
    
    app_logger.debug('Starting app Testing')
    from app import app_testing
    app_testing.doTesting(SESSION)

    SESSION.close()
    
    app_logger.debug('Leaving function app.test')


def server(config = ConfigParser()):
    app_logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    SESSION = _create_database_connection(config['postgres'])

    app_logger.info(f'Building GRPC Server...')
    import grpc
    from concurrent import futures
    from app.protos.stubs import ipAddress_pb2_grpc as ip_grpc
    from app.implementations import ipAddressServer

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=int(config.get('server','MAX_WORKER_THREADS'))))
    address = f'{config.get("server","ADDRESS")}:{config.get("server","PORT")}'
    server.add_insecure_port(address)
    server = ipAddressServer.serve(server)

    app_logger.info(f'Starting GRPC Server')
    server.start()
    app_logger.info(f'GRPC Server running at {address}')

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        app_logger.debug(f'Server stopping due to Keyboard Interruption')
        server.stop(0)
    except:
        server.stop(401)

    app_logger.info(f'GRPC Server stopped')

    SESSION.close()

    app_logger.debug(f'Leaving {__name__}.{whoami(currentframe())}')

