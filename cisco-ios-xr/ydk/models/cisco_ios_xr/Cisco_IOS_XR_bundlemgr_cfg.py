""" Cisco_IOS_XR_bundlemgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR bundlemgr package configuration.

This module contains definitions
for the following management objects\:
  lacp\: Link Aggregation Control Protocol commands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-rgmgr\-cfg,
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: no_cfg = 0

    	BFD mode not configured on per-bundle basis

    .. data:: cisco = 1

    	BFD mode Cisco

    .. data:: ietf = 2

    	BFD mode IETF

    """

    no_cfg = 0

    cisco = 1

    ietf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BfdModeEnum']


class BundleCiscoExtTypesEnum(Enum):
    """
    BundleCiscoExtTypesEnum

    Bundle cisco ext types

    .. data:: lon_signaling_off = 0

    	LON signaling disabled

    .. data:: lon_signaling_on = 1

    	LON signaling enabled

    """

    lon_signaling_off = 0

    lon_signaling_on = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleCiscoExtTypesEnum']


class BundleLoadBalanceEnum(Enum):
    """
    BundleLoadBalanceEnum

    Bundle load balance

    .. data:: default = 0

    	Default hash function used

    .. data:: efp_auto = 1

    	Send all traffic for this EFP over an

    	automatically selected member

    .. data:: efp_value = 2

    	Send all traffic for this EFP over the member

    	corresponding to the specified hash function

    .. data:: source_ip = 3

    	Load balance according to source IP address

    .. data:: destination_ip = 4

    	Load balance according to detination IP address

    """

    default = 0

    efp_auto = 1

    efp_value = 2

    source_ip = 3

    destination_ip = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleLoadBalanceEnum']


class BundleMaximumActiveLinksModeEnum(Enum):
    """
    BundleMaximumActiveLinksModeEnum

    Bundle maximum active links mode

    .. data:: default = 0

    	Default

    .. data:: hot_standby = 1

    	Hot standby

    """

    default = 0

    hot_standby = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleMaximumActiveLinksModeEnum']


class BundleMinimumBandwidthRangeEnum(Enum):
    """
    BundleMinimumBandwidthRangeEnum

    Bundle minimum bandwidth range

    .. data:: none = 0

    	None

    .. data:: kbps = 1

    	kbps

    .. data:: mbps = 2

    	mbps

    .. data:: gbps = 3

    	gbps

    """

    none = 0

    kbps = 1

    mbps = 2

    gbps = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleMinimumBandwidthRangeEnum']


class BundleModeEnum(Enum):
    """
    BundleModeEnum

    Bundle mode

    .. data:: on = 0

    	On

    .. data:: active = 1

    	Active

    .. data:: passive = 2

    	Passive

    """

    on = 0

    active = 1

    passive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundleModeEnum']


class BundlePeriodEnum(Enum):
    """
    BundlePeriodEnum

    Bundle period

    .. data:: true = 1

    	Use the standard LACP short period (1s)

    """

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundlePeriodEnum']


class BundlePortActivityEnum(Enum):
    """
    BundlePortActivityEnum

    Bundle port activity

    .. data:: on = 1

    	On

    .. data:: active = 2

    	Active

    .. data:: passive = 3

    	Passive

    .. data:: inherit = 4

    	Inherit

    """

    on = 1

    active = 2

    passive = 3

    inherit = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['BundlePortActivityEnum']


class ChurnLoggingEnum(Enum):
    """
    ChurnLoggingEnum

    Churn logging

    .. data:: actor = 1

    	Logging for actor churn only

    .. data:: partner = 2

    	Logging for partner churn only

    .. data:: both = 3

    	Logging for actor and partner churn

    """

    actor = 1

    partner = 2

    both = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['ChurnLoggingEnum']


class MlacpMaximizeParameterEnum(Enum):
    """
    MlacpMaximizeParameterEnum

    Mlacp maximize parameter

    .. data:: links = 1

    	Maximize the number of operational links

    .. data:: bandwidth = 2

    	Maximize the operational bandwidth

    """

    links = 1

    bandwidth = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpMaximizeParameterEnum']


class MlacpSwitchoverEnum(Enum):
    """
    MlacpSwitchoverEnum

    Mlacp switchover

    .. data:: brute_force = 1

    	Brute force shutdown

    .. data:: revertive = 2

    	Revertive behavior

    """

    brute_force = 1

    revertive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['MlacpSwitchoverEnum']


class PeriodShortEnumEnum(Enum):
    """
    PeriodShortEnumEnum

    Period short enum

    .. data:: true = 1

    	Use the standard LACP short period (1s)

    """

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['PeriodShortEnumEnum']



class Lacp(object):
    """
    Link Aggregation Control Protocol commands
    
    .. attribute:: system_mac
    
    	Unique identifier for this system
    	**type**\:  str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    .. attribute:: system_priority
    
    	Priority for this system. Lower value is higher priority
    	**type**\:  int
    
    	**range:** 1..65535
    
    	**default value**\: 32768
    
    

    """

    _prefix = 'bundlemgr-cfg'
    _revision = '2016-12-16'

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
        if self.system_mac is not None:
            return True

        if self.system_priority is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_bundlemgr_cfg as meta
        return meta._meta_table['Lacp']['meta_info']


