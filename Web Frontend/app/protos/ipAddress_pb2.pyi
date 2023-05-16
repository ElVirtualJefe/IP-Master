from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IpAddressIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class IpAddressNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class IpAddressResponse(_message.Message):
    __slots__ = ["ipAddress"]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    ipAddress: ipAddress
    def __init__(self, ipAddress: _Optional[_Union[ipAddress, _Mapping]] = ...) -> None: ...

class IpAddressSubnetRequest(_message.Message):
    __slots__ = ["subnet_id"]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    subnet_id: str
    def __init__(self, subnet_id: _Optional[str] = ...) -> None: ...

class ipAddress(_message.Message):
    __slots__ = ["dataLastSeen", "dateCreated", "dateLastEdited", "description", "hostname", "id", "ipAddress", "is_available", "is_gateway", "macAddress", "owner", "state_id", "subnet_id"]
    DATALASTSEEN_FIELD_NUMBER: _ClassVar[int]
    DATECREATED_FIELD_NUMBER: _ClassVar[int]
    DATELASTEDITED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    MACADDRESS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    dataLastSeen: str
    dateCreated: str
    dateLastEdited: str
    description: str
    hostname: str
    id: str
    ipAddress: str
    is_available: bool
    is_gateway: bool
    macAddress: str
    owner: str
    state_id: str
    subnet_id: str
    def __init__(self, id: _Optional[str] = ..., subnet_id: _Optional[str] = ..., ipAddress: _Optional[str] = ..., is_gateway: bool = ..., description: _Optional[str] = ..., hostname: _Optional[str] = ..., macAddress: _Optional[str] = ..., owner: _Optional[str] = ..., state_id: _Optional[str] = ..., dataLastSeen: _Optional[str] = ..., dateLastEdited: _Optional[str] = ..., dateCreated: _Optional[str] = ..., is_available: bool = ...) -> None: ...
