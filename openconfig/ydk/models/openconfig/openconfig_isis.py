""" openconfig_isis 

This module describes a YANG model for ISIS protocol configuration.
It is a limited subset of all of the configuration parameters
available in the variety of vendor implementations, hence it is
expected that it would be augmented with vendor \- specific configuration
data as needed. Additional modules or submodules to handle other
aspects of ISIS configuration, including policy, routing, types,
LSDB and additional address families are also expected. This model
supports the following ISIS configuration level hierarchy\:

ISIS
+\-> { global ISIS configuration}
   +\-> levels +\-> { level config}
       +\-> { system\-level\-counters }
       +\-> { level link\-state\-database}
   +\-> interface +\-> { interface config }
       +\-> { circuit\-counters }
       +\-> { levels config }
       +\-> { level adjacencies }

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IsisMetricFlags(Enum):
    """
    IsisMetricFlags (Enum Class)

    Type definition for flags used in IS\-IS metrics

    .. data:: INTERNAL = 0

    	When this flag is not set, internal metrics are in use.

    .. data:: UNSUPPORTED = 1

    	When this flag (referred to as the S-bit) is set, then

    	the metric is unsupported.

    """

    INTERNAL = Enum.YLeaf(0, "INTERNAL")

    UNSUPPORTED = Enum.YLeaf(1, "UNSUPPORTED")



