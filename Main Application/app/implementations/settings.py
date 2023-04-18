import logging
logger = logging.getLogger(f'ip-master.{__name__}')

import psycopg2.errors as err
from app.models.ipAddress import ipAddressModel
from inspect import currentframe
from app.implementations import whoami

def _getIpAddressById(session,id=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        ip = session.query(ipAddressModel).filter_by(id=id).first()
        if ip == None:
            raise err.NoDataFound(f'Could not find IP Address with id: {id}')
        else:
            logger.debug(f'{ip}')
            logger.debug(f'{repr(ip)}')
            logger.info(f'Found IP:{ip.ipAddress} with id={id}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ip
    
    return None


def _getIpAddressByName(session,name=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if name == None or name == '':
        raise err.InvalidParameterValue('Value missing for name')
    else:
        ips = session.query(ipAddressModel).filter_by(ipAddress=name).all()
        logger.debug(f'{len(ips)}')
        if len(ips) < 1:
            raise err.NoDataFound(f'Could not find IP Address with name: {name}')
        else:
            logger.info(f'Found {len(ips)} IP(s) with name={name}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ips
    
    return None


def _getIpAddressBySubnet(session,id=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        ips = session.query(ipAddressModel).filter_by(subnet_id=id).all()
        logger.debug(f'{len(ips)}')
        if len(ips) < 1:
            raise err.NoDataFound(f'Could not find IP Address in subnet_id: {id}')
        else:
            logger.info(f'Found {len(ips)} IP(s) with subnet_id={id}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return ips
    
    return None


def _addIpAddress(session,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if 'ipAddress' not in columns:
        raise err.InvalidParameterValue('Value missing for ipAddress')
    if 'is_gateway' not in columns:
        columns['is_gateway'] = False
    if 'is_available' not in columns:
        columns['is_available'] = False
    if 'subnet_id' not in columns:
        raise err.InvalidParameterValue('Value missing for subnet_id')
    
    for k,v in columns.items():
        logger.debug(f'key {k} = {v}')

    newIp = ipAddressModel(**columns)
    session.add(newIp)
    session.commit()

    ip = _getIpAddressById(session,newIp.id)

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return ip


def _deleteIpAddressById(session,id):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    ip = session.query(ipAddressModel).filter_by(id=id).first()
    session.delete(ip)
    session.commit()

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')


def _updateIpAddressById(session,id,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    logger.debug(f'{columns.keys()}')

    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        logger.debug(f'id = {id}')
        columns['id'] = id
        logger.debug(f'columns = {columns}')
        ip = session.query(ipAddressModel).filter_by(id=id).first()

        updateIp = session.merge(ipAddressModel(**columns))
        session.commit()

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return updateIp



    
