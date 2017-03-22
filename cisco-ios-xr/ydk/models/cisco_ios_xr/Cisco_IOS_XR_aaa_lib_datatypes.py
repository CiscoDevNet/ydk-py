""" Cisco_IOS_XR_aaa_lib_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AaaAccountingBroadcastEnum(Enum):
    """
    AaaAccountingBroadcastEnum

    Aaa accounting broadcast

    .. data:: disable = 0

    	Disable Broadcast

    .. data:: enable = 1

    	Enable Broadcast

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_datatypes as meta
        return meta._meta_table['AaaAccountingBroadcastEnum']


class AaaAccountingEnum(Enum):
    """
    AaaAccountingEnum

    Aaa accounting

    .. data:: not_set = 0

    	Not Set

    .. data:: start_stop = 1

    	Start Stop

    .. data:: stop_only = 2

    	Stop Only

    """

    not_set = 0

    start_stop = 1

    stop_only = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_datatypes as meta
        return meta._meta_table['AaaAccountingEnum']


class AaaAccountingRpFailoverEnum(Enum):
    """
    AaaAccountingRpFailoverEnum

    Aaa accounting rp failover

    .. data:: disable = 0

    	Disable rpfailover

    .. data:: enable = 1

    	Enable rpfailover

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_datatypes as meta
        return meta._meta_table['AaaAccountingRpFailoverEnum']


class AaaAccountingUpdateEnum(Enum):
    """
    AaaAccountingUpdateEnum

    Aaa accounting update

    .. data:: none = 0

    	Not Set

    .. data:: newinfo = 3

    	Update records for new accountable information

    	only

    .. data:: periodic = 4

    	Update records at periodic intervals

    """

    none = 0

    newinfo = 3

    periodic = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_datatypes as meta
        return meta._meta_table['AaaAccountingUpdateEnum']


class AaaMethodEnum(Enum):
    """
    AaaMethodEnum

    Aaa method

    .. data:: not_set = 0

    	Not Set

    .. data:: none = 1

    	None

    .. data:: local = 2

    	Local

    .. data:: radius = 3

    	Radius

    .. data:: tacacs_plus = 4

    	TACACS+

    .. data:: dsmd = 5

    	DSMD

    .. data:: sgbp = 6

    	SGBP

    .. data:: acct_d = 7

    	AcctD

    .. data:: error = 8

    	Error

    .. data:: if_authenticated = 9

    	If Authenticated

    .. data:: server_group = 10

    	Server Group

    .. data:: server_group_not_defined = 11

    	Server Group Not Defined

    .. data:: line = 12

    	Line

    .. data:: enable = 13

    	Enable

    .. data:: kerberos = 14

    	Kerberos

    .. data:: diameter = 15

    	Diameter

    .. data:: last = 16

    	Last

    """

    not_set = 0

    none = 1

    local = 2

    radius = 3

    tacacs_plus = 4

    dsmd = 5

    sgbp = 6

    acct_d = 7

    error = 8

    if_authenticated = 9

    server_group = 10

    server_group_not_defined = 11

    line = 12

    enable = 13

    kerberos = 14

    diameter = 15

    last = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_datatypes as meta
        return meta._meta_table['AaaMethodEnum']



