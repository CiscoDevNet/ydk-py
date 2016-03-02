""" HCNUM_TC 

A MIB module containing textual conventions
for high capacity data types. This module
addresses an immediate need for data types not directly
supported in the SMIv2. This short\-term solution
is meant to be deprecated as a long\-term solution
is deployed.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




