from inspect import currentframe
from app.implementations import whoami
import logging
logger = logging.getLogger(f'ip-master.{__name__}')

import psycopg2.errors as err
from app.models.ipAddress import ipAddressModel
from app.protos import ipAddress_pb2 as ip_pb2
from sqlalchemy import exc as sa_exc
from grpc import StatusCode
from app.implementations.helpers import convertRowToMessage

from app import _create_database_connection


def getIpAddress(request,context,session=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    #from app import SESSION as session
    from app.config import config
    if session == None:
        session = _create_database_connection(config['postgres'])
 
    logger.debug(f'session = {session}')
    logger.debug(f'Request Type = {type(request)}')

    try:
        if type(request) == ip_pb2.IpAddressIdRequest:
            if request.id == None or request.id == '':
                raise err.InvalidParameterValue('Value missing for id')
            else:

                ip = session.query(ipAddressModel).filter_by(id=request.id).first()
                if ip == None:
                    raise err.NoDataFound(f'Could not find IP Address with id: {request.id}')
                else:
                    logger.debug(f'{ip}')
                    logger.debug(f'{repr(ip)}')
                    logger.info(f'Found IP:{ip.ipAddress} with id={ip.id}')

        elif type(request) == ip_pb2.IpAddressNameRequest:
            if request.name == None or request.name == '':
                raise err.InvalidParameterValue('Value missing for name')
            else:

                ip = session.query(ipAddressModel).filter_by(name=request.name).all()
                if ip == None:
                    raise err.NoDataFound(f'Could not find IP Address with name: {request.name}')
                else:
                    logger.debug(f'{ip}')
                    logger.debug(f'{repr(ip)}')
                    logger.info(f'Found IP:{ip.ipAddress} with id={ip.id}')

        elif type(request) == ip_pb2.IpAddressSubnetRequest:
            if request.id == None or request.id == '':
                raise err.InvalidParameterValue('Value missing for subnet_id')
            else:

                ip = session.query(ipAddressModel).filter_by(subnet_id=request.id).all()
                if ip == None:
                    raise err.NoDataFound(f'Could not find IP Address with name: {request.name}')
                else:
                    logger.debug(f'{ip}')
                    logger.debug(f'{repr(ip)}')
                    logger.info(f'Found IP:{ip.ipAddress} with id={ip.id}')

    except sa_exc.DataError as e:
        logger.exception(f'Invalid input: {request}')
        #print(e.args)
        #print_exc()
        context.set_code(StatusCode.INVALID_ARGUMENT)
        context.set_details(f'[ERROR] Invalid input: {request}')
        session.rollback()
        #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
    except err.NoDataFound as e:
        logger.exception(f'Could not find entry with {request}')
        #print(e)
        context.set_code(StatusCode.NOT_FOUND)
        context.set_details(f'[ERROR] Could not find entry with {request}')
        session.rollback()
        #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
    except Exception as e:
        print("[ERROR] - ")
        print(e.__class__)
        print(e.__class__.__name__)
        print(e)
        session.rollback()
        #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
    else:
        resIpAddress = convertRowToMessage(ip)

        logger.debug(f'IP Found and Object created')
        session.close()
        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return resIpAddress
    
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

    ip = getIpAddress()

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

