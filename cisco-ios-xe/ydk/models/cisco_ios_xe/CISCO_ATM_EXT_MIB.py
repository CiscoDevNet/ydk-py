""" CISCO_ATM_EXT_MIB 

An extension to the Cisco ATM MIB module for managing
ATM implementations.

Acronyms and terms used in the MIB module\:

AAL5        \-\- ATM adaptation layer 5.
AIS         \-\- Alarm Indication Signal.
CC          \-\- Continuity Check.
End\-to\-end  \-\- End\-to\-end continuity checking.
               Monitoring occurs on the entire VC
               between two ATM end stations.
F5 OAM      \-\- OAM information flow between 
               network elements (NEs) used within 
               virtual connections to report degraded 
               virtual channel performance.
OAM         \-\- Operations, Administration 
               and Maintenance.
RDI         \-\- Remote Detection Indication.
Segment     \-\- Segment continuity checking. 
               Monitoring occurs on a VC segment
               between a router and a first\-hop 
               ATM switch.
VC          \-\- Virtual Channel.
VCC         \-\- Virtual Channel Connection.
VCL         \-\- Virtual Channel Link.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class OamccstatusEnum(Enum):
    """
    OamccstatusEnum

    OAM Continuity check (CC) status.

    ready(1)               \-\- CC is not activated on VC.

    waitActiveResponse(2)  \-\- Waiting for active\-response.

    waitActiveConfirm(3)   \-\- Waiting for active\-confirm.

    active(4)              \-\- CC is activated on VC.

    waitDeactiveConfirm(5) \-\- Waiting for deactivate 

                              confirm.

    .. data:: ready = 1

    .. data:: waitActiveResponse = 2

    .. data:: waitActiveConfirm = 3

    .. data:: active = 4

    .. data:: waitDeactiveConfirm = 5

    """

    ready = 1

    waitActiveResponse = 2

    waitActiveConfirm = 3

    active = 4

    waitDeactiveConfirm = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_EXT_MIB as meta
        return meta._meta_table['OamccstatusEnum']


class OamccvcstateEnum(Enum):
    """
    OamccvcstateEnum

    OAM Continuity check (CC) VC state.

    verified(1)            \-\- CC is successful. VC is up.

    aisrdi(2)              \-\- CC failed. VC is down.

    notManaged(3)          \-\- VC is not managed by CC.

    .. data:: verified = 1

    .. data:: aisrdi = 2

    .. data:: notManaged = 3

    """

    verified = 1

    aisrdi = 2

    notManaged = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ATM_EXT_MIB as meta
        return meta._meta_table['OamccvcstateEnum']



