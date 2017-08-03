""" cisco_bridge_common 

This module contains a collection of Cisco specific YANG type
definitions for Layer 2 Bridging.

Terms and Acronyms
  BD \: Bridge Domain

  DAI \: Dynamic ARP Inspection

  DHCP \: Dynamic Host Configuration Protocol

  IGMP \:  Internet Group Management Protocol

  IPSG \: IP Source Guard

  MLD \: Multicast Listener Discovery


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EthTrafficClass(Enum):
    """
    EthTrafficClass

    Traffic class for layer 2 ethernet transport

    .. data:: broadcast = 0

    	Ethernet frames with destination mac-address 

    	eqaul to FFFF.FFFF.FFFF

    .. data:: multicast = 1

    	Ethernet frame with destination MAC address not equal

    	to the broadcast address, but with the multicast bit set

    	to 1.

    .. data:: unknown_unicast = 2

    	Ethernet frames with with a packet destination MAC

    	address not yet learned.

    """

    broadcast = Enum.YLeaf(0, "broadcast")

    multicast = Enum.YLeaf(1, "multicast")

    unknown_unicast = Enum.YLeaf(2, "unknown-unicast")


class MacAgingType(Enum):
    """
    MacAgingType

    MAC aging mechanism.

    .. data:: inactivity = 0

    	Dynamically learnt MAC entries are aged out after

    	configured aging time only if no data traffic is 

    	detected during aging period.

    .. data:: absolute = 1

    	Dynamically learnt MAC entries are aged out after 

    	configured aging time.

    """

    inactivity = Enum.YLeaf(0, "inactivity")

    absolute = Enum.YLeaf(1, "absolute")


class MacLimitAction(Enum):
    """
    MacLimitAction

    Actions to be taken once mac limit threshold is exceeded.

    .. data:: none = 0

    	No action

    .. data:: flood = 1

    	Stop mac learning and flood unknown unicast traffic.

    .. data:: drop = 2

    	Stop mac learning and drop unknown unicast traffic.

    .. data:: shutdown = 3

    	Bring down operational status of the interface.

    """

    none = Enum.YLeaf(0, "none")

    flood = Enum.YLeaf(1, "flood")

    drop = Enum.YLeaf(2, "drop")

    shutdown = Enum.YLeaf(3, "shutdown")


class MacSecureAction(Enum):
    """
    MacSecureAction

    Actions to be taken upon mac secure violation.

    .. data:: none = 0

    	Forward the violating packet and allow the MAC to be

    	relearned.

    .. data:: restrict = 1

    	Drop violating packet.

    .. data:: shutdown = 2

    	Force shutdown the violating bridge port.

    """

    none = Enum.YLeaf(0, "none")

    restrict = Enum.YLeaf(1, "restrict")

    shutdown = Enum.YLeaf(2, "shutdown")



class MacLimitNotificationType(Identity):
    """
    Notification mechanism to use when mac limit threshold is
    exceeded.
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        super(MacLimitNotificationType, self).__init__("urn:cisco:params:xml:ns:yang:cisco-bridge-common", "cisco-bridge-common", "cisco-bridge-common:mac-limit-notification-type")


class NotifSyslog(Identity):
    """
    Generate syslog
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        super(NotifSyslog, self).__init__("urn:cisco:params:xml:ns:yang:cisco-bridge-common", "cisco-bridge-common", "cisco-bridge-common:notif-syslog")


class NotifNone(Identity):
    """
    Disable notification
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        super(NotifNone, self).__init__("urn:cisco:params:xml:ns:yang:cisco-bridge-common", "cisco-bridge-common", "cisco-bridge-common:notif-none")


class NotifSnmpTrap(Identity):
    """
    Generate SNMP trap
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        super(NotifSnmpTrap, self).__init__("urn:cisco:params:xml:ns:yang:cisco-bridge-common", "cisco-bridge-common", "cisco-bridge-common:notif-snmp-trap")


class NotifSyslogAndSnmpTrap(Identity):
    """
    Generate both syslog and SNMP trap
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        super(NotifSyslogAndSnmpTrap, self).__init__("urn:cisco:params:xml:ns:yang:cisco-bridge-common", "cisco-bridge-common", "cisco-bridge-common:notif-syslog-and-snmp-trap")


