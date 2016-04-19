""" Cisco_IOS_XR_asr9k_qos_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-qos package configuration.

This module contains definitions
for the following management objects\:
  qos\: Global QOS configuration.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class QosFieldNotSupportedEnum(Enum):
    """
    QosFieldNotSupportedEnum

    Qos field not supported

    .. data:: NOT_SUPPORTED = 0

    	Dummy data type leave unspecified

    """

    NOT_SUPPORTED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['QosFieldNotSupportedEnum']


class QosPolicyAccountEnum(Enum):
    """
    QosPolicyAccountEnum

    Qos policy account

    .. data:: NO_PREFERENCE = 0

    	No account turn off preference

    .. data:: LAYER2 = 1

    	Turn on layer 2 accounting

    .. data:: NO_LAYER2 = 2

    	Turn off layer 2 accounting

    .. data:: USER_DEFINED = 4

    	User defined accounting

    .. data:: LAYER1 = 8

    	Turn on layer 1 accounting

    """

    NO_PREFERENCE = 0

    LAYER2 = 1

    NO_LAYER2 = 2

    USER_DEFINED = 4

    LAYER1 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['QosPolicyAccountEnum']


class Qosl2DataLinkEnum(Enum):
    """
    Qosl2DataLinkEnum

    Qosl2 data link

    .. data:: AAL5 = 0

    	ATM adaption layer AAL5

    """

    AAL5 = 0


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qosl2DataLinkEnum']


class Qosl2EncapEnum(Enum):
    """
    Qosl2EncapEnum

    Qosl2 encap

    .. data:: SNAP_PPPOA = 1

    	snap-pppoa encap used between the DSLAM and CPE

    .. data:: MUX_PPPOA = 2

    	mux-pppoa encap used between the DSLAM and CPE

    .. data:: SNAP1483_ROUTED = 3

    	snap-1483routed encap used between the DSLAM

    	and CPE

    .. data:: MUX1483_ROUTED = 4

    	mux-1483routed encap used between the DSLAM and

    	CPE

    .. data:: SNAP_RBE = 5

    	snap-rbe encap used between the DSLAM and CPE

    .. data:: SNAP_DOT1QRBE = 6

    	snap-dot1q-rbe encap used between the DSLAM and

    	CPE

    .. data:: MUX_RBE = 7

    	mux-rbe encap used between the DSLAM and CPE

    .. data:: MUX_DOT1QRBE = 8

    	mux-dot1q-rbe encap used between the DSLAM and

    	CPE

    """

    SNAP_PPPOA = 1

    MUX_PPPOA = 2

    SNAP1483_ROUTED = 3

    MUX1483_ROUTED = 4

    SNAP_RBE = 5

    SNAP_DOT1QRBE = 6

    MUX_RBE = 7

    MUX_DOT1QRBE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qosl2EncapEnum']



class Qos(object):
    """
    Global QOS configuration.
    
    .. attribute:: fabric_service_policy
    
    	Name of the fabric service policy
    	**type**\: str
    
    	**range:** 0..63
    
    

    """

    _prefix = 'asr9k-qos-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.fabric_service_policy = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-qos-cfg:qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.fabric_service_policy is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.asr9k._meta import _Cisco_IOS_XR_asr9k_qos_cfg as meta
        return meta._meta_table['Qos']['meta_info']


