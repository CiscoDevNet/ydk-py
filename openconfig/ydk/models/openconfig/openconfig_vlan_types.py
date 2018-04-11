""" openconfig_vlan_types 

This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VlanModeType(Enum):
    """
    VlanModeType (Enum Class)

    VLAN interface mode (trunk or access)

    .. data:: ACCESS = 0

    	Access mode VLAN interface (No 802.1q header)

    .. data:: TRUNK = 1

    	Trunk mode VLAN interface

    """

    ACCESS = Enum.YLeaf(0, "ACCESS")

    TRUNK = Enum.YLeaf(1, "TRUNK")



class TPIDTYPES(Identity):
    """
    Base identity for TPID values that can override the VLAN
    ethertype value
    
    

    """

    _prefix = 'oc-vlan-types'
    _revision = '2016-05-26'

    def __init__(self):
        super(TPIDTYPES, self).__init__("http://openconfig.net/yang/vlan-types", "openconfig-vlan-types", "openconfig-vlan-types:TPID_TYPES")


class TPID0x8100(Identity):
    """
    Default TPID value for 802.1q single\-tagged VLANs.
    
    

    """

    _prefix = 'oc-vlan-types'
    _revision = '2016-05-26'

    def __init__(self):
        super(TPID0x8100, self).__init__("http://openconfig.net/yang/vlan-types", "openconfig-vlan-types", "openconfig-vlan-types:TPID_0x8100")


class TPID0x8A88(Identity):
    """
    TPID value for 802.1ad provider bridging, Q\-in\-Q,
    or stacked VLANs
    
    

    """

    _prefix = 'oc-vlan-types'
    _revision = '2016-05-26'

    def __init__(self):
        super(TPID0x8A88, self).__init__("http://openconfig.net/yang/vlan-types", "openconfig-vlan-types", "openconfig-vlan-types:TPID_0x8A88")


class TPID0x9100(Identity):
    """
    Alternate TPID value
    
    

    """

    _prefix = 'oc-vlan-types'
    _revision = '2016-05-26'

    def __init__(self):
        super(TPID0x9100, self).__init__("http://openconfig.net/yang/vlan-types", "openconfig-vlan-types", "openconfig-vlan-types:TPID_0x9100")


class TPID0X9200(Identity):
    """
    Alternate TPID value
    
    

    """

    _prefix = 'oc-vlan-types'
    _revision = '2016-05-26'

    def __init__(self):
        super(TPID0X9200, self).__init__("http://openconfig.net/yang/vlan-types", "openconfig-vlan-types", "openconfig-vlan-types:TPID_0X9200")


