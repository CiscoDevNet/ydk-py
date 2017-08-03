""" cisco_xe_openconfig_if_ethernet_ext 

Module to enable mapping for oc\-interfaces.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Auto(Identity):
    """
    Enable auto port\-speed negotiation for switches
    
    

    """

    _prefix = 'cisco-if-eth'
    _revision = '2017-03-09'

    def __init__(self):
        super(Auto, self).__init__("http://cisco.com/ns/yang/cisco-xe-openconfig-if-ethernet-ext", "cisco-xe-openconfig-if-ethernet-ext", "cisco-xe-openconfig-if-ethernet-ext:AUTO")


