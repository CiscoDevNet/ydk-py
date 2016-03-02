""" tailf_xsd_types 

This module contains useful XML Schema Datatypes that are not
covered by YANG types directly.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




