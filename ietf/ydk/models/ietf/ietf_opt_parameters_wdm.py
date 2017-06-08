""" ietf_opt_parameters_wdm 

This module contains a collection of YANG definitions for
collecting and configuring Optical Parameters
in Optical Networks and calculate the circuit feasibility.

Copyright (c) 2016 IETF Trust and the persons identified
as authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and
subject to the license terms contained in, the Simplified
BSD License set forth in Section 4.c of the IETF Trust's
Legal Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




