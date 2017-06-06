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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EthTrafficClassEnum(Enum):
    """
    EthTrafficClassEnum

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

    broadcast = 0

    multicast = 1

    unknown_unicast = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['EthTrafficClassEnum']


class MacAgingTypeEnum(Enum):
    """
    MacAgingTypeEnum

    MAC aging mechanism.

    .. data:: inactivity = 0

    	Dynamically learnt MAC entries are aged out after

    	configured aging time only if no data traffic is 

    	detected during aging period.

    .. data:: absolute = 1

    	Dynamically learnt MAC entries are aged out after 

    	configured aging time.

    """

    inactivity = 0

    absolute = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['MacAgingTypeEnum']


class MacLimitActionEnum(Enum):
    """
    MacLimitActionEnum

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

    none = 0

    flood = 1

    drop = 2

    shutdown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['MacLimitActionEnum']


class MacSecureActionEnum(Enum):
    """
    MacSecureActionEnum

    Actions to be taken upon mac secure violation.

    .. data:: none = 0

    	Forward the violating packet and allow the MAC to be

    	relearned.

    .. data:: restrict = 1

    	Drop violating packet.

    .. data:: shutdown = 2

    	Force shutdown the violating bridge port.

    """

    none = 0

    restrict = 1

    shutdown = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['MacSecureActionEnum']



class MacLimitNotificationTypeIdentity(object):
    """
    Notification mechanism to use when mac limit threshold is
    exceeded.
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['MacLimitNotificationTypeIdentity']['meta_info']


class NotifSyslogIdentity(MacLimitNotificationTypeIdentity):
    """
    Generate syslog
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        MacLimitNotificationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['NotifSyslogIdentity']['meta_info']


class NotifSyslogAndSnmpTrapIdentity(MacLimitNotificationTypeIdentity):
    """
    Generate both syslog and SNMP trap
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        MacLimitNotificationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['NotifSyslogAndSnmpTrapIdentity']['meta_info']


class NotifNoneIdentity(MacLimitNotificationTypeIdentity):
    """
    Disable notification
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        MacLimitNotificationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['NotifNoneIdentity']['meta_info']


class NotifSnmpTrapIdentity(MacLimitNotificationTypeIdentity):
    """
    Generate SNMP trap
    
    

    """

    _prefix = 'cbridge'
    _revision = '2016-12-14'

    def __init__(self):
        MacLimitNotificationTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_common as meta
        return meta._meta_table['NotifSnmpTrapIdentity']['meta_info']


