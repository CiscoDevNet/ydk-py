""" Cisco_IOS_XR_aaa_lib_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AaaAccounting(Enum):
    """
    AaaAccounting (Enum Class)

    Aaa accounting

    .. data:: not_set = 0

    	Not Set

    .. data:: start_stop = 1

    	Start Stop

    .. data:: stop_only = 2

    	Stop Only

    """

    not_set = Enum.YLeaf(0, "not-set")

    start_stop = Enum.YLeaf(1, "start-stop")

    stop_only = Enum.YLeaf(2, "stop-only")


class AaaAccountingBroadcast(Enum):
    """
    AaaAccountingBroadcast (Enum Class)

    Aaa accounting broadcast

    .. data:: disable = 0

    	Disable Broadcast

    .. data:: enable = 1

    	Enable Broadcast

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class AaaAccountingRpFailover(Enum):
    """
    AaaAccountingRpFailover (Enum Class)

    Aaa accounting rp failover

    .. data:: disable = 0

    	Disable rpfailover

    .. data:: enable = 1

    	Enable rpfailover

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class AaaAccountingUpdate(Enum):
    """
    AaaAccountingUpdate (Enum Class)

    Aaa accounting update

    .. data:: none = 0

    	Not Set

    .. data:: newinfo = 3

    	Update records for new accountable information

    	only

    .. data:: periodic = 4

    	Update records at periodic intervals

    """

    none = Enum.YLeaf(0, "none")

    newinfo = Enum.YLeaf(3, "newinfo")

    periodic = Enum.YLeaf(4, "periodic")


class AaaMethod(Enum):
    """
    AaaMethod (Enum Class)

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

    not_set = Enum.YLeaf(0, "not-set")

    none = Enum.YLeaf(1, "none")

    local = Enum.YLeaf(2, "local")

    radius = Enum.YLeaf(3, "radius")

    tacacs_plus = Enum.YLeaf(4, "tacacs-plus")

    dsmd = Enum.YLeaf(5, "dsmd")

    sgbp = Enum.YLeaf(6, "sgbp")

    acct_d = Enum.YLeaf(7, "acct-d")

    error = Enum.YLeaf(8, "error")

    if_authenticated = Enum.YLeaf(9, "if-authenticated")

    server_group = Enum.YLeaf(10, "server-group")

    server_group_not_defined = Enum.YLeaf(11, "server-group-not-defined")

    line = Enum.YLeaf(12, "line")

    enable = Enum.YLeaf(13, "enable")

    kerberos = Enum.YLeaf(14, "kerberos")

    diameter = Enum.YLeaf(15, "diameter")

    last = Enum.YLeaf(16, "last")


class AaaMethodAccounting(Enum):
    """
    AaaMethodAccounting (Enum Class)

    Aaa method accounting

    .. data:: not_set = 0

    	Not Set

    .. data:: none = 1

    	None

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

    .. data:: local = 17

    	Local

    """

    not_set = Enum.YLeaf(0, "not-set")

    none = Enum.YLeaf(1, "none")

    radius = Enum.YLeaf(3, "radius")

    tacacs_plus = Enum.YLeaf(4, "tacacs-plus")

    dsmd = Enum.YLeaf(5, "dsmd")

    sgbp = Enum.YLeaf(6, "sgbp")

    acct_d = Enum.YLeaf(7, "acct-d")

    error = Enum.YLeaf(8, "error")

    if_authenticated = Enum.YLeaf(9, "if-authenticated")

    server_group = Enum.YLeaf(10, "server-group")

    server_group_not_defined = Enum.YLeaf(11, "server-group-not-defined")

    line = Enum.YLeaf(12, "line")

    enable = Enum.YLeaf(13, "enable")

    kerberos = Enum.YLeaf(14, "kerberos")

    diameter = Enum.YLeaf(15, "diameter")

    last = Enum.YLeaf(16, "last")

    local = Enum.YLeaf(17, "local")



