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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BfdMode_Enum(Enum):
    """
    BfdMode_Enum

    Bfd mode

    """

    """

    BFD mode not configured on per\-bundle basis

    """
    NO_CFG = 0

    """

    BFD mode Cisco

    """
    CISCO = 1

    """

    BFD mode IETF

    """
    IETF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BfdMode_Enum']


class BundleCiscoExtTypes_Enum(Enum):
    """
    BundleCiscoExtTypes_Enum

    Bundle cisco ext types

    """

    """

    LON signaling disabled

    """
    LON_SIGNALING_OFF = 0

    """

    LON signaling enabled

    """
    LON_SIGNALING_ON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleCiscoExtTypes_Enum']


class BundleLoadBalance_Enum(Enum):
    """
    BundleLoadBalance_Enum

    Bundle load balance

    """

    """

    Default hash function used

    """
    DEFAULT = 0

    """

    Send all traffic for this EFP over an
    automatically selected member

    """
    EFP_AUTO = 1

    """

    Send all traffic for this EFP over the member
    corresponding to the specified hash function

    """
    EFP_VALUE = 2

    """

    Load balance according to source IP address

    """
    SOURCE_IP = 3

    """

    Load balance according to detination IP address

    """
    DESTINATION_IP = 4


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleLoadBalance_Enum']


class BundleMaximumActiveLinksMode_Enum(Enum):
    """
    BundleMaximumActiveLinksMode_Enum

    Bundle maximum active links mode

    """

    """

    Default

    """
    DEFAULT = 0

    """

    Hot standby

    """
    HOT_STANDBY = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleMaximumActiveLinksMode_Enum']


class BundlePortActivity_Enum(Enum):
    """
    BundlePortActivity_Enum

    Bundle port activity

    """

    """

    On

    """
    ON = 1

    """

    Active

    """
    ACTIVE = 2

    """

    Passive

    """
    PASSIVE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundlePortActivity_Enum']


class ChurnLogging_Enum(Enum):
    """
    ChurnLogging_Enum

    Churn logging

    """

    """

    Logging for actor churn only

    """
    ACTOR = 1

    """

    Logging for partner churn only

    """
    PARTNER = 2

    """

    Logging for actor and partner churn

    """
    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['ChurnLogging_Enum']


class MlacpMaximizeParameter_Enum(Enum):
    """
    MlacpMaximizeParameter_Enum

    Mlacp maximize parameter

    """

    """

    Maximize the number of operational links

    """
    LINKS = 1

    """

    Maximize the operational bandwidth

    """
    BANDWIDTH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpMaximizeParameter_Enum']


class MlacpSwitchover_Enum(Enum):
    """
    MlacpSwitchover_Enum

    Mlacp switchover

    """

    """

    Brute force shutdown

    """
    BRUTE_FORCE = 1

    """

    Revertive behavior

    """
    REVERTIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpSwitchover_Enum']


class PeriodShortEnum_Enum(Enum):
    """
    PeriodShortEnum_Enum

    Period short enum

    """

    """

    Use the standard LACP short period (1s)

    """
    TRUE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['PeriodShortEnum_Enum']



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
        if self.is_presence():
            return True
        if self.system_mac is not None:
            return True

        if self.system_priority is not None:
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.bundlemgr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['Lacp']['meta_info']


