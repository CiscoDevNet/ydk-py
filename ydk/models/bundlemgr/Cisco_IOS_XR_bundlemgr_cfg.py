""" Cisco_IOS_XR_bundlemgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR bundlemgr package configuration.

This module contains definitions
for the following management objects\:
  lacp\: Link Aggregation Control Protocol commands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BfdModeEnum(Enum):
    """
    BfdModeEnum

    Bfd mode

    .. data:: NO_CFG = 0

    	BFD mode not configured on per-bundle basis

    .. data:: CISCO = 1

    	BFD mode Cisco

    .. data:: IETF = 2

    	BFD mode IETF

    """

    NO_CFG = 0

    CISCO = 1

    IETF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BfdModeEnum']


class BundleCiscoExtTypesEnum(Enum):
    """
    BundleCiscoExtTypesEnum

    Bundle cisco ext types

    .. data:: LON_SIGNALING_OFF = 0

    	LON signaling disabled

    .. data:: LON_SIGNALING_ON = 1

    	LON signaling enabled

    """

    LON_SIGNALING_OFF = 0

    LON_SIGNALING_ON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleCiscoExtTypesEnum']


class BundleLoadBalanceEnum(Enum):
    """
    BundleLoadBalanceEnum

    Bundle load balance

    .. data:: DEFAULT = 0

    	Default hash function used

    .. data:: EFP_AUTO = 1

    	Send all traffic for this EFP over an

    	automatically selected member

    .. data:: EFP_VALUE = 2

    	Send all traffic for this EFP over the member

    	corresponding to the specified hash function

    .. data:: SOURCE_IP = 3

    	Load balance according to source IP address

    .. data:: DESTINATION_IP = 4

    	Load balance according to detination IP address

    """

    DEFAULT = 0

    EFP_AUTO = 1

    EFP_VALUE = 2

    SOURCE_IP = 3

    DESTINATION_IP = 4


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleLoadBalanceEnum']


class BundleMaximumActiveLinksModeEnum(Enum):
    """
    BundleMaximumActiveLinksModeEnum

    Bundle maximum active links mode

    .. data:: DEFAULT = 0

    	Default

    .. data:: HOT_STANDBY = 1

    	Hot standby

    """

    DEFAULT = 0

    HOT_STANDBY = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleMaximumActiveLinksModeEnum']


class BundlePortActivityEnum(Enum):
    """
    BundlePortActivityEnum

    Bundle port activity

    .. data:: ON = 1

    	On

    .. data:: ACTIVE = 2

    	Active

    .. data:: PASSIVE = 3

    	Passive

    """

    ON = 1

    ACTIVE = 2

    PASSIVE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundlePortActivityEnum']


class ChurnLoggingEnum(Enum):
    """
    ChurnLoggingEnum

    Churn logging

    .. data:: ACTOR = 1

    	Logging for actor churn only

    .. data:: PARTNER = 2

    	Logging for partner churn only

    .. data:: BOTH = 3

    	Logging for actor and partner churn

    """

    ACTOR = 1

    PARTNER = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['ChurnLoggingEnum']


class MlacpMaximizeParameterEnum(Enum):
    """
    MlacpMaximizeParameterEnum

    Mlacp maximize parameter

    .. data:: LINKS = 1

    	Maximize the number of operational links

    .. data:: BANDWIDTH = 2

    	Maximize the operational bandwidth

    """

    LINKS = 1

    BANDWIDTH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpMaximizeParameterEnum']


class MlacpSwitchoverEnum(Enum):
    """
    MlacpSwitchoverEnum

    Mlacp switchover

    .. data:: BRUTE_FORCE = 1

    	Brute force shutdown

    .. data:: REVERTIVE = 2

    	Revertive behavior

    """

    BRUTE_FORCE = 1

    REVERTIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpSwitchoverEnum']


class PeriodShortEnumEnum(Enum):
    """
    PeriodShortEnumEnum

    Period short enum

    .. data:: TRUE = 1

    	Use the standard LACP short period (1s)

    """

    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['PeriodShortEnumEnum']



class Lacp(object):
    """
    Link Aggregation Control Protocol commands
    
    .. attribute:: system_mac
    
    	Unique identifier for this system
    	**type**\: str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    .. attribute:: system_priority
    
    	Priority for this system. Lower value is higher priority
    	**type**\: int
    
    	**range:** 1..65535
    
    

    """

    _prefix = 'bundlemgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.system_mac = None
        self.system_priority = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-bundlemgr-cfg:lacp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.system_mac is not None:
            return True

        if self.system_priority is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['Lacp']['meta_info']


