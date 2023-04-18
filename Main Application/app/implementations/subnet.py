import logging
logger = logging.getLogger(f'ip-master.{__name__}')

import psycopg2.errors as err
from app.models.subnet import subnetModel
from inspect import currentframe
from app.implementations import whoami

def _getSubnetById(session,id=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        subnet = session.query(subnetModel).filter_by(id=id).first()
        if subnet == None:
            raise err.NoDataFound(f'Could not find Subnet with id: {id}')
        else:
            logger.debug(f'{subnet}')
            logger.debug(f'{repr(subnet)}')
            logger.info(f'Found Subnet:{subnet.name} with id={id}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return subnet
    
    return None


def _getSubnetByName(session,name=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if name == None or name == '':
        raise err.InvalidParameterValue('Value missing for name')
    else:
        subnets = session.query(subnetModel).filter_by(name=name).all()
        logger.debug(f'{len(subnets)}')
        if len(subnets) < 1:
            raise err.NoDataFound(f'Could not find Subnet with name: {name}')
        else:
            logger.info(f'Found {len(subnets)} Subnet(s) with name={name}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return subnets
    
    return None


def _addSubnet(session,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if 'name' not in columns:
        raise err.InvalidParameterValue('Value missing for Subnet/Mask')

    for k,v in columns.items():
        logger.debug(f'key {k} = {v}')

    newSubnet = subnetModel(**columns)
    session.add(newSubnet)
    session.commit()

    subnet = _getSubnetById(session,newSubnet.id)

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return subnet


def _deleteSubnetById(session,id):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    subnet = session.query(subnetModel).filter_by(id=id).first()
    session.delete(subnet)
    session.commit()

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return True


def _updateSubnetById(session,id,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    logger.debug(f'{columns.keys()}')

    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        logger.debug(f'id = {id}')
        columns['id'] = id
        logger.debug(f'columns = {columns}')
        subnet = session.query(subnetModel).filter_by(id=id).first()

        updateSubnet = session.merge(subnetModel(**columns))
        session.commit()

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return updateSubnet



    
