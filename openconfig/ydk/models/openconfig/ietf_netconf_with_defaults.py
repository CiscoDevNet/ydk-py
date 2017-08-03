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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class WithDefaultsMode(Enum):
    """
    WithDefaultsMode

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

    report_all = Enum.YLeaf(0, "report-all")

    report_all_tagged = Enum.YLeaf(1, "report-all-tagged")

    trim = Enum.YLeaf(2, "trim")

    explicit = Enum.YLeaf(3, "explicit")



