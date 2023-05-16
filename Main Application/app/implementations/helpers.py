from inspect import currentframe
from app.implementations import whoami
import logging
logger = logging.getLogger(f'ip-master.{__name__}')


from app.protos import ipAddress_pb2 as ip_pb2
from app.models import Base


def convertRowToMessage(row):
    logger.debug(f'Inside function {__name__}.{whoami(currentframe())}')

    from sqlalchemy import DateTime
    from sqlalchemy.dialects.postgresql import UUID

    logger.debug(f'{row}')
    logger.debug(f'Table Name = {row.__tablename__}')

    logger.debug(f'Result Found - Creating gRPC Message Object')

    table = Base.metadata.tables[row.__tablename__]
    mes = ip_pb2.ipAddress()

    for c in table.columns:
        logger.debug(f'Column - {c.name}')
        attr = getattr(row,c.name,None)

        if attr == None:
            continue
            
        logger.debug(f'Column Type {type(c.type)}')
        if type(c.type) == UUID or type(c.type) == DateTime:
            attr = attr.__str__()

        logger.debug(f'Attribute found for Column {c.name} - {attr}')
        setattr(mes,c.name,attr)

    '''
    logger.debug(f'Adding the ID - {row.id}')
    mes.id = row.id.__str__()
    logger.debug(f'Adding the IP Address - {row.ipAddress}')
    mes.ipAddress = row.ipAddress
    logger.debug(f'Adding Gateway Status - {row.is_gateway}')
    mes.is_gateway = row.is_gateway
    logger.debug(f'Adding Description - {row.description}')
    if row.description == None:
        mes.description = ""
    else:
        mes.description = row.description
    logger.debug(f'Base attributes added')
    '''

    logger.debug(f'Leaving function {__name__}.{whoami(currentframe())}')
    return mes

