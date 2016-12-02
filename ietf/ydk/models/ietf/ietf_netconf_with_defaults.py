""" ietf_netconf_with_defaults 

This module defines an extension to the NETCONF protocol
that allows the NETCONF client to control how default
values are handled by the server in particular NETCONF
operations.

Copyright (c) 2011 IETF Trust and the persons identified as
the document authors.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6243; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class WithDefaultsModeEnum(Enum):
    """
    WithDefaultsModeEnum

    Possible modes to report default data.

    .. data:: report_all = 0

    	All default data is reported.

    .. data:: report_all_tagged = 1

    	All default data is reported.

    	Any nodes considered to be default data

    	will contain a 'default' XML attribute,

    	set to 'true' or '1'.

    .. data:: trim = 2

    	Values are not reported if they contain the default.

    .. data:: explicit = 3

    	Report values that contain the definition of

    	explicitly set data.

    """

    report_all = 0

    report_all_tagged = 1

    trim = 2

    explicit = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_with_defaults as meta
        return meta._meta_table['WithDefaultsModeEnum']



