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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class OamCCStatus_Enum(Enum):
    """
    OamCCStatus_Enum

    OAM Continuity check (CC) status.
    ready(1)               \-\- CC is not activated on VC.
    waitActiveResponse(2)  \-\- Waiting for active\-response.
    waitActiveConfirm(3)   \-\- Waiting for active\-confirm.
    active(4)              \-\- CC is activated on VC.
    waitDeactiveConfirm(5) \-\- Waiting for deactivate 
                              confirm.

    """

    READY = 1

    WAITACTIVERESPONSE = 2

    WAITACTIVECONFIRM = 3

    ACTIVE = 4

    WAITDEACTIVECONFIRM = 5


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _CISCO_ATM_EXT_MIB as meta
        return meta._meta_table['OamCCStatus_Enum']


class OamCCVcState_Enum(Enum):
    """
    OamCCVcState_Enum

    OAM Continuity check (CC) VC state.
    verified(1)            \-\- CC is successful. VC is up.
    aisrdi(2)              \-\- CC failed. VC is down.
    notManaged(3)          \-\- VC is not managed by CC.

    """

    VERIFIED = 1

    AISRDI = 2

    NOTMANAGED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _CISCO_ATM_EXT_MIB as meta
        return meta._meta_table['OamCCVcState_Enum']



