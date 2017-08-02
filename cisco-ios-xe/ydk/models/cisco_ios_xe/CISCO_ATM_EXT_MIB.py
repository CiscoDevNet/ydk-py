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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Oamccstatus(Enum):
    """
    Oamccstatus

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

    ready = Enum.YLeaf(1, "ready")

    waitActiveResponse = Enum.YLeaf(2, "waitActiveResponse")

    waitActiveConfirm = Enum.YLeaf(3, "waitActiveConfirm")

    active = Enum.YLeaf(4, "active")

    waitDeactiveConfirm = Enum.YLeaf(5, "waitDeactiveConfirm")


class Oamccvcstate(Enum):
    """
    Oamccvcstate

    OAM Continuity check (CC) VC state.

    verified(1)            \-\- CC is successful. VC is up.

    aisrdi(2)              \-\- CC failed. VC is down.

    notManaged(3)          \-\- VC is not managed by CC.

    .. data:: verified = 1

    .. data:: aisrdi = 2

    .. data:: notManaged = 3

    """

    verified = Enum.YLeaf(1, "verified")

    aisrdi = Enum.YLeaf(2, "aisrdi")

    notManaged = Enum.YLeaf(3, "notManaged")



