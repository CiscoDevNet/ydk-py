""" cisco_ospf 

This YANG module defines the Cisco OSPF common 
yang model
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AccessListInOutTypeEnum(Enum):
    """
    AccessListInOutTypeEnum

    Access list in and out

    .. data:: in_ = 0

    	Filter incoming routing updates

    .. data:: out = 1

    	Filter outgoing routing updates

    """

    in_ = 0

    out = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ospf as meta
        return meta._meta_table['AccessListInOutTypeEnum']


class OspfExternalTypeEnum(Enum):
    """
    OspfExternalTypeEnum

    external route types

    .. data:: Y_1 = 0

    	type 1

    .. data:: Y_2 = 1

    	type 2

    """

    Y_1 = 0

    Y_2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ospf as meta
        return meta._meta_table['OspfExternalTypeEnum']


class OspfLogAdjEnum(Enum):
    """
    OspfLogAdjEnum

    Ospf log adjacency changes

    .. data:: enable = 0

    	Enable log adjacency brief

    .. data:: detail = 1

    	Enable log adjcency detail

    .. data:: disable = 2

    	disable log adjacency

    """

    enable = 0

    detail = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ospf as meta
        return meta._meta_table['OspfLogAdjEnum']


class PrefixApplicabilityEnum(Enum):
    """
    PrefixApplicabilityEnum

    Ospf uloop avoidance

    .. data:: protected = 1

    	Protected prefixes only

    .. data:: all = 2

    	All prefixes

    """

    protected = 1

    all = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_ospf as meta
        return meta._meta_table['PrefixApplicabilityEnum']



