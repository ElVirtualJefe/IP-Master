import logging
logger = logging.getLogger(f'ip-master.{__name__}')

logger.debug(f'Inside module {__name__}')
    

def testIpAddressTable(session):
    from app.implementations import ipAddress

    logger.debug(f'{ipAddress._getIpAddressById(session,"ae03ddbc-f9bd-4d85-9981-a9aa9b342a70").ipAddress}')

    for ip in ipAddress._getIpAddressByName(session,"172.16.103.153"):
        logger.debug(f'{ip.ipAddress} - {ip.id}')

    for ip in ipAddress._getIpAddressBySubnet(session,"7690d124-f66f-4495-a585-788595a419f1"):
        logger.debug(f'{ip.ipAddress} - {ip.id}')

    newIp = ipAddress._addIpAddress(session,ipAddress="172.16.103.154",subnet_id="7690d124-f66f-4495-a585-788595a419f1")
    logger.debug(f'{newIp.ipAddress} - {newIp.id}')

    from time import sleep
    sleep(10)

    try:
        updateIp = ipAddress._updateIpAddressById(session,newIp.id,is_available=True,description="This is a test, and will be deleted!!")
        logger.debug(f'{updateIp.ipAddress} - {updateIp.description}')

        sleep(30)
    except:
        logger.debug(f'Could not update IP -> Deleting the entry now',exc_info=True)

    logger.debug(f'{ipAddress._deleteIpAddressById(session,newIp.id)}')


def testSubnetTable(session):
    from app.implementations import subnet

    logger.debug(f'{subnet._getSubnetById(session,"7690d124-f66f-4495-a585-788595a419f1").name}')

    for s in subnet._getSubnetByName(session,"172.16.103.0/24"):
        logger.debug(f'{s.name} - {s.id}')

    newSubnet = subnet._addSubnet(session,name="172.16.105.0/24",description="Initial Entry")
    logger.debug(f'{newSubnet.name} - {newSubnet.id}')

    from time import sleep
    sleep(10)

    try:
        updateSubnet = subnet._updateSubnetById(session,newSubnet.id,description="This is a test, and will be deleted!!")
        logger.debug(f'{updateSubnet.name} - {updateSubnet.description}')

        sleep(30)
    except:
        logger.debug(f'Could not update Subnet -> Deleting the entry now',exc_info=True)

    logger.debug(f'{subnet._deleteSubnetById(session,newSubnet.id)}')


def testVlanTable(session):
    from app.implementations import vlan

    logger.debug(f'{vlan._getVlanById(session,"375ba262-5462-4df2-bbc5-985462b346c8").vlanNumber}')

    for v in vlan._getVlanByNumber(session,103):
        logger.debug(f'{v.vlanNumber} - {v.id}')

    newVlan = vlan._addVlan(session,name="Server 105",vlanNumber=105,description="Initial Entry")
    logger.debug(f'{newVlan.vlanNumber} - {newVlan.id}')

    from time import sleep
    sleep(10)

    try:
        updateVlan = vlan._updateVlanById(session,newVlan.id,description="This is a test, and will be deleted!!")
        logger.debug(f'{updateVlan.name} - {updateVlan.description}')

        sleep(30)
    except:
        logger.debug(f'Could not update vLAN -> Deleting the entry now',exc_info=True)

    logger.debug(f'{vlan._deleteVlanById(session,newVlan.id)}')


def doTesting(session):
    logger.debug(f'Inside function {__name__}.doTesting')

    testVlanTable(session)
    testSubnetTable(session)
    testIpAddressTable(session)

    logger.debug(f'Leaving function {__name__}.doTesting')
    

logger.debug(f'Leaving module {__name__}')