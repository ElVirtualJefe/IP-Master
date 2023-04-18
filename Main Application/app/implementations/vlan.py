import logging
logger = logging.getLogger(f'ip-master.{__name__}')

import psycopg2.errors as err
from app.models.vlan import vLanModel
from inspect import currentframe
from app.implementations import whoami

def _getVlanById(session,id=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        vlan = session.query(vLanModel).filter_by(id=id).first()
        if vlan == None:
            raise err.NoDataFound(f'Could not find vLAN with id: {id}')
        else:
            logger.debug(f'{vlan}')
            logger.debug(f'{repr(vlan)}')
            logger.info(f'Found vLAN:{vlan.vlanNumber} with id={id}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return vlan
    
    return None


def _getVlanByNumber(session,vlanNumber=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if vlanNumber == None or vlanNumber == '':
        raise err.InvalidParameterValue('Value missing for vlanNumber')
    else:
        vlans = session.query(vLanModel).filter_by(vlanNumber=vlanNumber).all()
        logger.debug(f'{len(vlans)}')
        if len(vlans) < 1:
            raise err.NoDataFound(f'Could not find vLAN with number: {vlanNumber}')
        else:
            logger.info(f'Found {len(vlans)} vLAN(s) with vlanNumber={vlanNumber}')

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return vlans
    
    return None


def _getVlanBySubnet(session,id=None):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')
    from app.models.subnet import subnetModel

    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        s = session.query(subnetModel).filter_by(subnet_id=id).first()
        if s == None:
            raise err.NoDataFound(f'Could not find Subnet with id: {id}')
        else:
            logger.info(f'Found Subnet {s.name} with subnet_id={id}')
            vlan = _getVlanById(session,id=s.vlan_id)

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return vlan
    
    return None


def _addVlan(session,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    if 'vlanNumber' not in columns:
        raise err.InvalidParameterValue('Value missing for vlanNumber')
    
    for k,v in columns.items():
        logger.debug(f'key {k} = {v}')

    newVlan = vLanModel(**columns)
    session.add(newVlan)
    session.commit()

    vlan = _getVlanById(session,newVlan.id)

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return vlan


def _deleteVlanById(session,id):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    vlan = session.query(vLanModel).filter_by(id=id).first()
    session.delete(vlan)
    session.commit()

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return True


def _updateVlanById(session,id,**columns):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    logger.debug(f'{columns.keys()}')

    if id == None or id == '':
        raise err.InvalidParameterValue('Value missing for id')
    else:
        logger.debug(f'id = {id}')
        columns['id'] = id
        logger.debug(f'columns = {columns}')
        vlan = session.query(vLanModel).filter_by(id=id).first()

        updateVlan = session.merge(vLanModel(**columns))
        session.commit()

        logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
        return updateVlan



    
