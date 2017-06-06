""" common_mpls_types 

This module contains a collection of generally useful YANG types
that are specific to MPLS that can be usefully shared
between multiple models.

Terms and Acronyms

MPLS\: Multi Protocol Label Switching

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IetfMplsLabelEnum(Enum):
    """
    IetfMplsLabelEnum

    Temporary type until IETF definition

    .. data:: v4_explicit_null = 0

    	IETF MPLS IPv4 explicit null Label (0)

    .. data:: v6_explicit_null = 2

    	IETF MPLS IPv6 explicit null label (2)

    .. data:: implicit_null = 3

    	IETF MPLS implicit null label (3)

    """

    v4_explicit_null = 0

    v6_explicit_null = 2

    implicit_null = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _common_mpls_types as meta
        return meta._meta_table['IetfMplsLabelEnum']



