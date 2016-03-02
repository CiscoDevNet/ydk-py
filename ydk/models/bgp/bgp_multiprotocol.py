""" bgp_multiprotocol 

This module is part of a YANG model for BGP protocol
configuration, focusing on configuration of multiprotocol
BGP, in particular various relevant address families (AFI) and
sub\-address families (SAFI).

Identities (rather than enumerated types) are used to identify
each AFI / SAFI type to make it easier for users to extend to
pre\-standard or custom AFI/SAFI types.  This module is only
intended to capture the most

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




