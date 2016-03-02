""" Cisco_IOS_XR_pfi_im_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pfi\-im\-cmd package operational data.

This module contains definitions
for the following management objects\:
  interfaces\: Interface operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BmMbrStateReason_Enum(Enum):
    """
    BmMbrStateReason_Enum

    Bm mbr state reason

    """

    """

    Reason unavailable (diagnostics error)

    """
    BM_MBR_STATE_REASON_UNKNOWN = 0

    """

    Link cannot be used (unknown reason)

    """
    BM_MBR_STATE_REASON_UNSELECTABLE_UNKNOWN = 1

    """

    Link is down

    """
    BM_MBR_STATE_REASON_LINK_DOWN = 2

    """

    Link is being removed from the bundle

    """
    BM_MBR_STATE_REASON_LINK_DELETING = 3

    """

    Link is in the process of being created

    """
    BM_MBR_STATE_REASON_CREATING = 4

    """

    Bundle is in the process of being created

    """
    BM_MBR_STATE_REASON_BUNDLE_CREATING = 5

    """

    Bundle is in the process of being deleted

    """
    BM_MBR_STATE_REASON_BUNDLE_DELETING = 6

    """

    Bundle has been shut down

    """
    BM_MBR_STATE_REASON_BUNDLE_ADMIN_DOWN = 7

    """

    Bundle is in the process of being replicated to
    this location

    """
    BM_MBR_STATE_REASON_REPLICATING = 8

    """

    Incompatible with other links in the bundle
    (bandwidth out of range)

    """
    BM_MBR_STATE_REASON_BANDWIDTH = 9

    """

    Loopback\: Actor and Partner have the same
    System ID and Key

    """
    BM_MBR_STATE_REASON_LOOP_BACK = 10

    """

    Incompatible with other links in the bundle
    (LACP vs non\-LACP)

    """
    BM_MBR_STATE_REASON_ACTIVITY_TYPE = 11

    """

    Bundle shutdown is configured for the bundle

    """
    BM_MBR_STATE_REASON_BUNDLE_SHUTDOWN = 12

    """

    Not enough links available to meet
    minimum\-active threshold

    """
    BM_MBR_STATE_REASON_MIN_SELECTED = 13

    """

    Link is Standby due to maximum\-active links
    configuration

    """
    BM_MBR_STATE_REASON_MAX_SELECTED = 14

    """

    Bundle has too many member links configured

    """
    BM_MBR_STATE_REASON_LINK_LIMIT = 15

    """

    Bundle has reached maximum supported number of
    active links

    """
    BM_MBR_STATE_REASON_ACTIVE_LIMIT = 16

    """

    Link is Standby (unknown reason)

    """
    BM_MBR_STATE_REASON_STANDBY_UNKNOWN = 17

    """

    Link is Expired; LACPDUs are not being received
    from the partner

    """
    BM_MBR_STATE_REASON_EXPIRED = 18

    """

    Link is Defaulted; LACPDUs are not being
    received from the partner

    """
    BM_MBR_STATE_REASON_DEFAULTED = 19

    """

    Link is Not Aggregatable (unknown reason)

    """
    BM_MBR_STATE_REASON_ACT_OR_NOT_AGG = 20

    """

    Partner has marked the link as Not Aggregatable

    """
    BM_MBR_STATE_REASON_PARTNER_NOT_AGG = 21

    """

    Partner System ID/Key do not match that of the
    Selected links

    """
    BM_MBR_STATE_REASON_LAGID = 22

    """

    Bundle interface is not present in
    configuration

    """
    BM_MBR_STATE_REASON_BUNDLE_NOT_CFGD = 23

    """

    Wait\-while timer is running

    """
    BM_MBR_STATE_REASON_BUNDLE_NOT_READY = 24

    """

    Partner has not echoed the correct parameters
    for this link

    """
    BM_MBR_STATE_REASON_PARTNER_OOD = 25

    """

    Partner is not Synchronized (Waiting, Standby,
    or LAG ID mismatch)

    """
    BM_MBR_STATE_REASON_PARTNER_NOT_IN_SYNC = 26

    """

    Partner is not Synchronized (Waiting, not
    Selected, or out\-of\-date)

    """
    BM_MBR_STATE_REASON_FOREIGN_PARTNER_OOS = 27

    """

    Link is Attached and has not gone Collecting
    (unknown reason)

    """
    BM_MBR_STATE_REASON_ATTACH_UNKNOWN = 28

    """

    Partner has not advertized that it is
    Collecting

    """
    BM_MBR_STATE_REASON_PARTNER_NOT_COLLECTING = 29

    """

    Link is Collecting and has not gone
    Distributing (unknown reason)

    """
    BM_MBR_STATE_REASON_COLLECT_UNKNOWN = 30

    """

    Link is marked as Standby by mLACP peer

    """
    BM_MBR_STATE_REASON_STANDBY_FOREIGN = 31

    """

    Link is waiting for BFD session to start

    """
    BM_MBR_STATE_REASON_BFD_STARTING = 32

    """

    BFD state of this link is Down

    """
    BM_MBR_STATE_REASON_BFD_DOWN = 33

    """

    BFD session is unconfigured on the remote end

    """
    BM_MBR_STATE_REASON_BFD_NBR_UNCONFIG = 34

    """

    Link is not operational as a result of mLACP
    negotiations

    """
    BM_MBR_STATE_REASON_MLACP = 35

    """

    ICCP group is isolated from the core network

    """
    BM_MBR_STATE_REASON_PE_ISOLATED = 36

    """

    Forced switchover to the mLACP peer

    """
    BM_MBR_STATE_REASON_FORCED_SWITCHOVER = 37

    """

    Link is error disabled (unknown reason)

    """
    BM_MBR_STATE_REASON_ERRDIS_UNKNOWN = 38

    """

    Waiting for member state information from mLACP
    peer

    """
    BM_MBR_STATE_REASON_MLACP_NO_MBR_STATE_INFO = 39

    """

    Link is Active

    """
    BM_MBR_STATE_REASON_ACTIVE = 40

    """

    Waiting for bundle state information from mLACP
    peer

    """
    BM_MBR_STATE_REASON_MLACP_NO_BDL_STATE_INFO = 41

    """

    Waiting for bundle configuration information
    from mLACP peer

    """
    BM_MBR_STATE_REASON_MLACP_NO_BDL_CONFIG_INFO = 42

    """

    Waiting for bundle to complete initial
    synchronization with mLACP peer

    """
    BM_MBR_STATE_REASON_MLACP_NO_BDL_SYNC = 43

    """

    mLACP bundle does not have a peer device

    """
    BM_MBR_STATE_REASON_MLACP_BDL_HAS_NO_PEER = 44

    """

    Link is being ignored due to an inconsistency
    with mLACP peer

    """
    BM_MBR_STATE_REASON_MLACP_NAK = 45

    """

    ICCP transport is unavailable

    """
    BM_MBR_STATE_REASON_MLACP_TRANSPORT_UNAVAILABLE = 46

    """

    ICCP Group is not fully configured

    """
    BM_MBR_STATE_REASON_MLACP_NOT_CONFIGURED = 47

    """

    mLACP recovery delay timer is running

    """
    BM_MBR_STATE_REASON_RECOVERY_TIMER = 48

    """

    mLACP peer is active

    """
    BM_MBR_STATE_REASON_MLACP_STANDBY = 49

    """

    mLACP peer has more links/bandwidth available

    """
    BM_MBR_STATE_REASON_MAXIMIZED_OUT = 50

    """

    mLACP peer has one or more links Selected

    """
    BM_MBR_STATE_REASON_MLACP_PEER_SELECTED = 51

    """

    mLACP bundle does not have a peer device
    (connect timer running)

    """
    BM_MBR_STATE_REASON_MLACP_CONNECT_TIMER_RUNNING = 52

    """

    Bundle is not configured to run mLACP

    """
    BM_MBR_STATE_REASON_BUNDLE_NOT_MLACP = 53

    """

    Bundle has too many working links configured
    (more than the maximum\-active limit)

    """
    BM_MBR_STATE_REASON_NO_LON = 54

    """

    Additional bandwidth from link would exceed
    load balancing capabilities

    """
    BM_MBR_STATE_REASON_CUMUL_REL_BW_LIMIT = 55

    """

    No MAC address available for the bundle

    """
    BM_MBR_STATE_REASON_NO_MAC = 56

    """

    No system ID available for use by this bundle

    """
    BM_MBR_STATE_REASON_NO_SYSTEM_ID = 57

    """

    Link is shutdown

    """
    BM_MBR_STATE_REASON_LINK_SHUTDOWN = 58

    """

    Non\-LACP link in mLACP bundle

    """
    BM_MBR_STATE_REASON_ACTIVITY_MLACP = 59

    """

    LACP link in inter\-chassis bundle

    """
    BM_MBR_STATE_REASON_ACTIVITY_ICCP = 60

    """

    Parent bundle is both inter\-chassis and
    configured for mLACP

    """
    BM_MBR_STATE_REASON_BUNDLE_ICPE_MLACP = 61

    """

    Too many bundle members in system; no link
    number available

    """
    BM_MBR_STATE_REASON_NO_LINK_NUM = 62

    """

    mLACP peer has a higher priority link

    """
    BM_MBR_STATE_REASON_STANDBY_PEER_HIGHER_PRIO = 63

    """

    Link is in standby redundancy state

    """
    BM_MBR_STATE_REASON_RED_STATE_STANDBY = 64

    """

    One or more links in the bundle are in standby
    redundancy state

    """
    BM_MBR_STATE_REASON_OTHER_RED_STATE_STANDBY = 65

    """

    Holding down temporary to avoid churn after
    restart

    """
    BM_MBR_STATE_REASON_HOLD_ING = 66

    """

    Bundle has been error\-disabled

    """
    BM_MBR_STATE_REASON_BUNDLE_ERROR_DISABLED = 67

    """

    Bundle has been disabled by EFD

    """
    BM_MBR_STATE_REASON_BUNDLE_EFD_DISABLED = 68

    """

    Singleton ICCP group is isolated from the core
    network

    """
    BM_MBR_STATE_REASON_SINGLETON_PE_ISOLATED = 69

    """

    Enumeration maximum value

    """
    BM_MBR_STATE_REASON_COUNT = 70


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMbrStateReason_Enum']


class BmMuxreason_Enum(Enum):
    """
    BmMuxreason_Enum

    Bm muxreason

    """

    """

    Selection logic has not yet been run for the
    bundle this link is a member of

    """
    BM_MUX_REASON_NO_REASON = 0

    """

    Link is down

    """
    BM_MUX_REASON_LINK_DOWN = 1

    """

    Link is being removed from the bundle

    """
    BM_MUX_REASON_LINK_DELETED = 2

    """

    Link has wrong duplexity

    """
    BM_MUX_REASON_DUPLEX = 3

    """

    Link has wrong bandwidth

    """
    BM_MUX_REASON_BANDWIDTH = 4

    """

    Link is a loopback interface

    """
    BM_MUX_REASON_LOOP_BACK = 5

    """

    Link has wrong activity type

    """
    BM_MUX_REASON_ACTIVITY_TYPE = 6

    """

    Link's bundle already has maximum number of
    members allowed

    """
    BM_MUX_REASON_LINK_LIMIT = 7

    """

    Link is attached to a shared medium

    """
    BM_MUX_REASON_SHARED = 8

    """

    Link has wrong LAG ID

    """
    BM_MUX_REASON_LAGID = 9

    """

    Link's bundle does not exist

    """
    BM_MUX_REASON_NO_BUNDLE = 10

    """

    Link's bundle has no primary link

    """
    BM_MUX_REASON_NO_PRIMARY = 11

    """

    Link's bundle is shut down

    """
    BM_MUX_REASON_BUNDLE_DOWN = 12

    """

    Link is marked individual by partner

    """
    BM_MUX_REASON_INDIVIDUAL = 13

    """

    Link is Defaulted, suggesting it is not
    receiving LACPDUs from the peer

    """
    BM_MUX_REASON_DEFAULTED = 14

    """

    Link is in InSync state

    """
    BM_MUX_REASON_IN_SYNC = 15

    """

    Link is in Collecting state

    """
    BM_MUX_REASON_COLLECTING = 16

    """

    Link exceeds maximum active limit

    """
    BM_MUX_REASON_ACTIVE_LINK_LIMIT = 17

    """

    Link is in Distributing state

    """
    BM_MUX_REASON_DISTRIBUTING = 18

    """

    Enumeration maximum value

    """
    BM_MUX_REASON_COUNT = 19


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMuxreason_Enum']


class BmMuxstate_Enum(Enum):
    """
    BmMuxstate_Enum

    Bm muxstate

    """

    """

    Port is not attached to a bundle

    """
    DETACHED = 1

    """

    Port has chosen bundle and is waiting to join

    """
    WAITING = 2

    """

    Port is attached to the bundle but not active

    """
    ATTACHED = 3

    """

    Port is ready to receive data

    """
    COLLECTING = 4

    """

    Port is distributing data

    """
    DISTRIBUTING = 5

    """

    Port is active and can send and receive data

    """
    COLLECTING_DISTRIBUTING = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmMuxstate_Enum']


class BmSeverity_Enum(Enum):
    """
    BmSeverity_Enum

    Severity of the member state reason

    """

    """

    OK

    """
    OK = 0

    """

    Information

    """
    INFORMATION = 1

    """

    Misconfiguration

    """
    MISCONFIGURATION = 2

    """

    Warning

    """
    WARNING = 3

    """

    Error

    """
    ERROR = 5


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmSeverity_Enum']


class BmStateReasonTarget_Enum(Enum):
    """
    BmStateReasonTarget_Enum

    Scope of the state reason

    """

    """

    Member applicable reason

    """
    MEMBER_REASON = 0

    """

    Bundle applicable reason

    """
    BUNDLE_REASON = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmStateReasonTarget_Enum']


class BmdMemberState_Enum(Enum):
    """
    BmdMemberState_Enum

    Bmd member state

    """

    """

    Member is configured

    """
    BMD_MBR_STATE_CONFIGURED = 1

    """

    Member is standby

    """
    BMD_MBR_STATE_STANDBY = 2

    """

    Member is hot standby

    """
    BMD_MBR_STATE_HOT_STANDBY = 3

    """

    Member is negotiating

    """
    BMD_MBR_STATE_NEGOTIATING = 4

    """

    Member has a BFD session running

    """
    BMD_MBR_STATE_BFD_RUNNING = 5

    """

    Member is active

    """
    BMD_MBR_STATE_ACTIVE = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmdMemberState_Enum']


class BmdMemberTypeEnum_Enum(Enum):
    """
    BmdMemberTypeEnum_Enum

    Bmd member type enum

    """

    """

    Member has been configured on the local device

    """
    BMD_MBR_LOCAL = 0

    """

    Member has been configured on an mLACP peer
    device

    """
    BMD_MBR_FOREIGN = 1

    """

    Member's type is unknown

    """
    BMD_MBR_UNKNOWN = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['BmdMemberTypeEnum_Enum']


class EfpPayloadEtype_Enum(Enum):
    """
    EfpPayloadEtype_Enum

    Payload ethertype match

    """

    """

    Any

    """
    PAYLOAD_ETHERTYPE_ANY = 0

    """

    IP

    """
    PAYLOAD_ETHERTYPE_IP = 1

    """

    PPPoE

    """
    PAYLOAD_ETHERTYPE_PPPOE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpPayloadEtype_Enum']


class EfpTagEtype_Enum(Enum):
    """
    EfpTagEtype_Enum

    Tag ethertype

    """

    """

    Untagged

    """
    UNTAGGED = 0

    """

    Dot1Q

    """
    DOT1Q = 33024

    """

    Dot1ad

    """
    DOT1AD = 34984


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpTagEtype_Enum']


class EfpTagPriority_Enum(Enum):
    """
    EfpTagPriority_Enum

    Priority

    """

    """

    Priority 0

    """
    PRIORITY0 = 0

    """

    Priority 1

    """
    PRIORITY1 = 1

    """

    Priority 2

    """
    PRIORITY2 = 2

    """

    Priority 3

    """
    PRIORITY3 = 3

    """

    Priority 4

    """
    PRIORITY4 = 4

    """

    Priority 5

    """
    PRIORITY5 = 5

    """

    Priority 6

    """
    PRIORITY6 = 6

    """

    Priority 7

    """
    PRIORITY7 = 7

    """

    Any priority

    """
    PRIORITY_ANY = 8


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['EfpTagPriority_Enum']


class GccDerState_Enum(Enum):
    """
    GccDerState_Enum

    Gcc der state

    """

    """

    In Service

    """
    IN_SERVICE = 0

    """

    Out Of Service

    """
    OUT_OF_SERVICE = 1

    """

    Maintainance

    """
    MAINTAINANCE = 2

    """

    Automatic In Service

    """
    AIS = 3


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['GccDerState_Enum']


class GccSecState_Enum(Enum):
    """
    GccSecState_Enum

    Gcc sec state

    """

    """

    Normal

    """
    NORMAL = 0

    """

    Maintainance

    """
    MAINTAINANCE = 1

    """

    Automatic In Service

    """
    AIS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['GccSecState_Enum']


class ImAttrDuplex_Enum(Enum):
    """
    ImAttrDuplex_Enum

    Im attr duplex

    """

    """

    im attr duplex unknown

    """
    IM_ATTR_DUPLEX_UNKNOWN = 0

    """

    im attr duplex half

    """
    IM_ATTR_DUPLEX_HALF = 1

    """

    im attr duplex full

    """
    IM_ATTR_DUPLEX_FULL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrDuplex_Enum']


class ImAttrFlowControl_Enum(Enum):
    """
    ImAttrFlowControl_Enum

    Im attr flow control

    """

    """

    im attr flow control off

    """
    IM_ATTR_FLOW_CONTROL_OFF = 0

    """

    im attr flow control on

    """
    IM_ATTR_FLOW_CONTROL_ON = 1

    """

    im attr flow control not sup

    """
    IM_ATTR_FLOW_CONTROL_NOT_SUP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrFlowControl_Enum']


class ImAttrLink_Enum(Enum):
    """
    ImAttrLink_Enum

    Im attr link

    """

    """

    im attr link type auto

    """
    IM_ATTR_LINK_TYPE_AUTO = 0

    """

    im attr link type force

    """
    IM_ATTR_LINK_TYPE_FORCE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrLink_Enum']


class ImAttrMedia_Enum(Enum):
    """
    ImAttrMedia_Enum

    Im attr media

    """

    """

    im attr media other

    """
    IM_ATTR_MEDIA_OTHER = 0

    """

    im attr media unknown

    """
    IM_ATTR_MEDIA_UNKNOWN = 1

    """

    im attr media aui

    """
    IM_ATTR_MEDIA_AUI = 2

    """

    im attr media 10base5

    """
    IM_ATTR_MEDIA_10BASE5 = 3

    """

    im attr media foirl

    """
    IM_ATTR_MEDIA_FOIRL = 4

    """

    im attr media 10base2

    """
    IM_ATTR_MEDIA_10BASE2 = 5

    """

    im attr media 10broad36

    """
    IM_ATTR_MEDIA_10BROAD36 = 6

    """

    im attr media 10base

    """
    IM_ATTR_MEDIA_10BASE = 7

    """

    im attr media 10base thd

    """
    IM_ATTR_MEDIA_10BASE_THD = 8

    """

    im attr media 10base tfd

    """
    IM_ATTR_MEDIA_10BASE_TFD = 9

    """

    im attr media 10base fp

    """
    IM_ATTR_MEDIA_10BASE_FP = 10

    """

    im attr media 10base fb

    """
    IM_ATTR_MEDIA_10BASE_FB = 11

    """

    im attr media 10base fl

    """
    IM_ATTR_MEDIA_10BASE_FL = 12

    """

    im attr media 10base flhd

    """
    IM_ATTR_MEDIA_10BASE_FLHD = 13

    """

    im attr media 10base flfd

    """
    IM_ATTR_MEDIA_10BASE_FLFD = 14

    """

    im attr media 100base t4

    """
    IM_ATTR_MEDIA_100BASE_T4 = 15

    """

    im attr media 100base tx

    """
    IM_ATTR_MEDIA_100BASE_TX = 16

    """

    im attr media 100base txhd

    """
    IM_ATTR_MEDIA_100BASE_TXHD = 17

    """

    im attr media 100base txfd

    """
    IM_ATTR_MEDIA_100BASE_TXFD = 18

    """

    im attr media 100base fx

    """
    IM_ATTR_MEDIA_100BASE_FX = 19

    """

    im attr media 100base fxhd

    """
    IM_ATTR_MEDIA_100BASE_FXHD = 20

    """

    im attr media 100base fxfd

    """
    IM_ATTR_MEDIA_100BASE_FXFD = 21

    """

    im attr media 100base ex

    """
    IM_ATTR_MEDIA_100BASE_EX = 22

    """

    im attr media 100base exhd

    """
    IM_ATTR_MEDIA_100BASE_EXHD = 23

    """

    im attr media 100base exfd

    """
    IM_ATTR_MEDIA_100BASE_EXFD = 24

    """

    im attr media 100base t2

    """
    IM_ATTR_MEDIA_100BASE_T2 = 25

    """

    im attr media 100base t2hd

    """
    IM_ATTR_MEDIA_100BASE_T2HD = 26

    """

    im attr media 100base t2fd

    """
    IM_ATTR_MEDIA_100BASE_T2FD = 27

    """

    im attr media 1000base x

    """
    IM_ATTR_MEDIA_1000BASE_X = 28

    """

    im attr media 1000base xhdx

    """
    IM_ATTR_MEDIA_1000BASE_XHDX = 29

    """

    im attr media 1000base xfd

    """
    IM_ATTR_MEDIA_1000BASE_XFD = 30

    """

    im attr media 1000base lx

    """
    IM_ATTR_MEDIA_1000BASE_LX = 31

    """

    im attr media 1000base lxhd

    """
    IM_ATTR_MEDIA_1000BASE_LXHD = 32

    """

    im attr media 1000base lxfdx

    """
    IM_ATTR_MEDIA_1000BASE_LXFDX = 33

    """

    im attr media 1000base sx

    """
    IM_ATTR_MEDIA_1000BASE_SX = 34

    """

    im attr media 1000base sxhd

    """
    IM_ATTR_MEDIA_1000BASE_SXHD = 35

    """

    im attr media 1000base sxfd

    """
    IM_ATTR_MEDIA_1000BASE_SXFD = 36

    """

    im attr media 1000base cx

    """
    IM_ATTR_MEDIA_1000BASE_CX = 37

    """

    im attr media 1000base cxhdx

    """
    IM_ATTR_MEDIA_1000BASE_CXHDX = 38

    """

    im attr media 1000base cxfd

    """
    IM_ATTR_MEDIA_1000BASE_CXFD = 39

    """

    im attr media 1000base

    """
    IM_ATTR_MEDIA_1000BASE = 40

    """

    im attr media 1000base thd

    """
    IM_ATTR_MEDIA_1000BASE_THD = 41

    """

    im attr media 1000base tfd

    """
    IM_ATTR_MEDIA_1000BASE_TFD = 42

    """

    im attr media 10gbase x

    """
    IM_ATTR_MEDIA_10GBASE_X = 43

    """

    im attr media 10gbase lx4

    """
    IM_ATTR_MEDIA_10GBASE_LX4 = 44

    """

    im attr media 10gbase r

    """
    IM_ATTR_MEDIA_10GBASE_R = 45

    """

    im attr media 10gbase er

    """
    IM_ATTR_MEDIA_10GBASE_ER = 46

    """

    im attr media 10gbase lr

    """
    IM_ATTR_MEDIA_10GBASE_LR = 47

    """

    im attr media 10gbase sr

    """
    IM_ATTR_MEDIA_10GBASE_SR = 48

    """

    im attr media 10gbase w

    """
    IM_ATTR_MEDIA_10GBASE_W = 49

    """

    im attr media 10gbase ew

    """
    IM_ATTR_MEDIA_10GBASE_EW = 50

    """

    im attr media 10gbase lw

    """
    IM_ATTR_MEDIA_10GBASE_LW = 51

    """

    im attr media 10gbase sw

    """
    IM_ATTR_MEDIA_10GBASE_SW = 52

    """

    im attr media 10gbase zr

    """
    IM_ATTR_MEDIA_10GBASE_ZR = 53

    """

    im attr media 802 9a

    """
    IM_ATTR_MEDIA_802_9A = 54

    """

    im attr media rj45

    """
    IM_ATTR_MEDIA_RJ45 = 55

    """

    im attr media 1000base zx

    """
    IM_ATTR_MEDIA_1000BASE_ZX = 56

    """

    im attr media 1000base cwdm

    """
    IM_ATTR_MEDIA_1000BASE_CWDM = 57

    """

    im attr media 1000base cwdm 1470

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1470 = 58

    """

    im attr media 1000base cwdm 1490

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1490 = 59

    """

    im attr media 1000base cwdm 1510

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1510 = 60

    """

    im attr media 1000base cwdm 1530

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1530 = 61

    """

    im attr media 1000base cwdm 1550

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1550 = 62

    """

    im attr media 1000base cwdm 1570

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1570 = 63

    """

    im attr media 1000base cwdm 1590

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1590 = 64

    """

    im attr media 1000base cwdm 1610

    """
    IM_ATTR_MEDIA_1000BASE_CWDM_1610 = 65

    """

    im attr media 10gbase dwdm

    """
    IM_ATTR_MEDIA_10GBASE_DWDM = 66

    """

    im attr media 100gbase lr4

    """
    IM_ATTR_MEDIA_100GBASE_LR4 = 67

    """

    im attr media 1000base dwdm

    """
    IM_ATTR_MEDIA_1000BASE_DWDM = 68

    """

    im attr media 1000base dwdm 1533

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1533 = 69

    """

    im attr media 1000base dwdm 1537

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1537 = 70

    """

    im attr media 1000base dwdm 1541

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1541 = 71

    """

    im attr media 1000base dwdm 1545

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1545 = 72

    """

    im attr media 1000base dwdm 1549

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1549 = 73

    """

    im attr media 1000base dwdm 1553

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1553 = 74

    """

    im attr media 1000base dwdm 1557

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1557 = 75

    """

    im attr media 1000base dwdm 1561

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1561 = 76

    """

    im attr media 40gbase lr4

    """
    IM_ATTR_MEDIA_40GBASE_LR4 = 77

    """

    im attr media 40gbase er4

    """
    IM_ATTR_MEDIA_40GBASE_ER4 = 78

    """

    im attr media 100gbase er4

    """
    IM_ATTR_MEDIA_100GBASE_ER4 = 79

    """

    im attr media 1000base ex

    """
    IM_ATTR_MEDIA_1000BASE_EX = 80

    """

    im attr media 1000base bx10 d

    """
    IM_ATTR_MEDIA_1000BASE_BX10_D = 81

    """

    im attr media 1000base bx10 u

    """
    IM_ATTR_MEDIA_1000BASE_BX10_U = 82

    """

    im attr media 1000base dwdm 1561 42

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1561_42 = 83

    """

    im attr media 1000base dwdm 1560 61

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1560_61 = 84

    """

    im attr media 1000base dwdm 1559 79

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1559_79 = 85

    """

    im attr media 1000base dwdm 1558 98

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1558_98 = 86

    """

    im attr media 1000base dwdm 1558 17

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1558_17 = 87

    """

    im attr media 1000base dwdm 1557 36

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1557_36 = 88

    """

    im attr media 1000base dwdm 1556 55

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1556_55 = 89

    """

    im attr media 1000base dwdm 1555 75

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1555_75 = 90

    """

    im attr media 1000base dwdm 1554 94

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1554_94 = 91

    """

    im attr media 1000base dwdm 1554 13

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1554_13 = 92

    """

    im attr media 1000base dwdm 1553 33

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1553_33 = 93

    """

    im attr media 1000base dwdm 1552 52

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1552_52 = 94

    """

    im attr media 1000base dwdm 1551 72

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1551_72 = 95

    """

    im attr media 1000base dwdm 1550 92

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1550_92 = 96

    """

    im attr media 1000base dwdm 1550 12

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1550_12 = 97

    """

    im attr media 1000base dwdm 1549 32

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1549_32 = 98

    """

    im attr media 1000base dwdm 1548 51

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1548_51 = 99

    """

    im attr media 1000base dwdm 1547 72

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1547_72 = 100

    """

    im attr media 1000base dwdm 1546 92

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1546_92 = 101

    """

    im attr media 1000base dwdm 1546 12

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1546_12 = 102

    """

    im attr media 1000base dwdm 1545 32

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1545_32 = 103

    """

    im attr media 1000base dwdm 1544 53

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1544_53 = 104

    """

    im attr media 1000base dwdm 1543 73

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1543_73 = 105

    """

    im attr media 1000base dwdm 1542 94

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1542_94 = 106

    """

    im attr media 1000base dwdm 1542 14

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1542_14 = 107

    """

    im attr media 1000base dwdm 1541 35

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1541_35 = 108

    """

    im attr media 1000base dwdm 1540 56

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1540_56 = 109

    """

    im attr media 1000base dwdm 1539 77

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1539_77 = 110

    """

    im attr media 1000base dwdm 1538 98

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1538_98 = 111

    """

    im attr media 1000base dwdm 1538 19

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1538_19 = 112

    """

    im attr media 1000base dwdm 1537 40

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1537_40 = 113

    """

    im attr media 1000base dwdm 1536 61

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1536_61 = 114

    """

    im attr media 1000base dwdm 1535 82

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1535_82 = 115

    """

    im attr media 1000base dwdm 1535 04

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1535_04 = 116

    """

    im attr media 1000base dwdm 1534 25

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1534_25 = 117

    """

    im attr media 1000base dwdm 1533 47

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1533_47 = 118

    """

    im attr media 1000base dwdm 1532 68

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1532_68 = 119

    """

    im attr media 1000base dwdm 1531 90

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1531_90 = 120

    """

    im attr media 1000base dwdm 1531 12

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1531_12 = 121

    """

    im attr media 1000base dwdm 1530 33

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_1530_33 = 122

    """

    im attr media 1000base dwdm tunable

    """
    IM_ATTR_MEDIA_1000BASE_DWDM_TUNABLE = 123

    """

    im attr media 10gbase dwdm 1561 42

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1561_42 = 124

    """

    im attr media 10gbase dwdm 1560 61

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1560_61 = 125

    """

    im attr media 10gbase dwdm 1559 79

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1559_79 = 126

    """

    im attr media 10gbase dwdm 1558 98

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1558_98 = 127

    """

    im attr media 10gbase dwdm 1558 17

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1558_17 = 128

    """

    im attr media 10gbase dwdm 1557 36

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1557_36 = 129

    """

    im attr media 10gbase dwdm 1556 55

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1556_55 = 130

    """

    im attr media 10gbase dwdm 1555 75

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1555_75 = 131

    """

    im attr media 10gbase dwdm 1554 94

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1554_94 = 132

    """

    im attr media 10gbase dwdm 1554 13

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1554_13 = 133

    """

    im attr media 10gbase dwdm 1553 33

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1553_33 = 134

    """

    im attr media 10gbase dwdm 1552 52

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1552_52 = 135

    """

    im attr media 10gbase dwdm 1551 72

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1551_72 = 136

    """

    im attr media 10gbase dwdm 1550 92

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1550_92 = 137

    """

    im attr media 10gbase dwdm 1550 12

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1550_12 = 138

    """

    im attr media 10gbase dwdm 1549 32

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1549_32 = 139

    """

    im attr media 10gbase dwdm 1548 51

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1548_51 = 140

    """

    im attr media 10gbase dwdm 1547 72

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1547_72 = 141

    """

    im attr media 10gbase dwdm 1546 92

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1546_92 = 142

    """

    im attr media 10gbase dwdm 1546 12

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1546_12 = 143

    """

    im attr media 10gbase dwdm 1545 32

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1545_32 = 144

    """

    im attr media 10gbase dwdm 1544 53

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1544_53 = 145

    """

    im attr media 10gbase dwdm 1543 73

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1543_73 = 146

    """

    im attr media 10gbase dwdm 1542 94

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1542_94 = 147

    """

    im attr media 10gbase dwdm 1542 14

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1542_14 = 148

    """

    im attr media 10gbase dwdm 1541 35

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1541_35 = 149

    """

    im attr media 10gbase dwdm 1540 56

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1540_56 = 150

    """

    im attr media 10gbase dwdm 1539 77

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1539_77 = 151

    """

    im attr media 10gbase dwdm 1538 98

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1538_98 = 152

    """

    im attr media 10gbase dwdm 1538 19

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1538_19 = 153

    """

    im attr media 10gbase dwdm 1537 40

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1537_40 = 154

    """

    im attr media 10gbase dwdm 1536 61

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1536_61 = 155

    """

    im attr media 10gbase dwdm 1535 82

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1535_82 = 156

    """

    im attr media 10gbase dwdm 1535 04

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1535_04 = 157

    """

    im attr media 10gbase dwdm 1534 25

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1534_25 = 158

    """

    im attr media 10gbase dwdm 1533 47

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1533_47 = 159

    """

    im attr media 10gbase dwdm 1532 68

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1532_68 = 160

    """

    im attr media 10gbase dwdm 1531 90

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1531_90 = 161

    """

    im attr media 10gbase dwdm 1531 12

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1531_12 = 162

    """

    im attr media 10gbase dwdm 1530 33

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_1530_33 = 163

    """

    im attr media 10gbase dwdm tunable

    """
    IM_ATTR_MEDIA_10GBASE_DWDM_TUNABLE = 164

    """

    im attr media 40gbase dwdm 1561 42

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1561_42 = 165

    """

    im attr media 40gbase dwdm 1560 61

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1560_61 = 166

    """

    im attr media 40gbase dwdm 1559 79

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1559_79 = 167

    """

    im attr media 40gbase dwdm 1558 98

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1558_98 = 168

    """

    im attr media 40gbase dwdm 1558 17

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1558_17 = 169

    """

    im attr media 40gbase dwdm 1557 36

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1557_36 = 170

    """

    im attr media 40gbase dwdm 1556 55

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1556_55 = 171

    """

    im attr media 40gbase dwdm 1555 75

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1555_75 = 172

    """

    im attr media 40gbase dwdm 1554 94

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1554_94 = 173

    """

    im attr media 40gbase dwdm 1554 13

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1554_13 = 174

    """

    im attr media 40gbase dwdm 1553 33

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1553_33 = 175

    """

    im attr media 40gbase dwdm 1552 52

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1552_52 = 176

    """

    im attr media 40gbase dwdm 1551 72

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1551_72 = 177

    """

    im attr media 40gbase dwdm 1550 92

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1550_92 = 178

    """

    im attr media 40gbase dwdm 1550 12

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1550_12 = 179

    """

    im attr media 40gbase dwdm 1549 32

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1549_32 = 180

    """

    im attr media 40gbase dwdm 1548 51

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1548_51 = 181

    """

    im attr media 40gbase dwdm 1547 72

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1547_72 = 182

    """

    im attr media 40gbase dwdm 1546 92

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1546_92 = 183

    """

    im attr media 40gbase dwdm 1546 12

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1546_12 = 184

    """

    im attr media 40gbase dwdm 1545 32

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1545_32 = 185

    """

    im attr media 40gbase dwdm 1544 53

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1544_53 = 186

    """

    im attr media 40gbase dwdm 1543 73

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1543_73 = 187

    """

    im attr media 40gbase dwdm 1542 94

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1542_94 = 188

    """

    im attr media 40gbase dwdm 1542 14

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1542_14 = 189

    """

    im attr media 40gbase dwdm 1541 35

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1541_35 = 190

    """

    im attr media 40gbase dwdm 1540 56

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1540_56 = 191

    """

    im attr media 40gbase dwdm 1539 77

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1539_77 = 192

    """

    im attr media 40gbase dwdm 1538 98

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1538_98 = 193

    """

    im attr media 40gbase dwdm 1538 19

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1538_19 = 194

    """

    im attr media 40gbase dwdm 1537 40

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1537_40 = 195

    """

    im attr media 40gbase dwdm 1536 61

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1536_61 = 196

    """

    im attr media 40gbase dwdm 1535 82

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1535_82 = 197

    """

    im attr media 40gbase dwdm 1535 04

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1535_04 = 198

    """

    im attr media 40gbase dwdm 1534 25

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1534_25 = 199

    """

    im attr media 40gbase dwdm 1533 47

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1533_47 = 200

    """

    im attr media 40gbase dwdm 1532 68

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1532_68 = 201

    """

    im attr media 40gbase dwdm 1531 90

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1531_90 = 202

    """

    im attr media 40gbase dwdm 1531 12

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1531_12 = 203

    """

    im attr media 40gbase dwdm 1530 33

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_1530_33 = 204

    """

    im attr media 40gbase dwdm tunable

    """
    IM_ATTR_MEDIA_40GBASE_DWDM_TUNABLE = 205

    """

    im attr media 100gbase dwdm 1561 42

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1561_42 = 206

    """

    im attr media 100gbase dwdm 1560 61

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1560_61 = 207

    """

    im attr media 100gbase dwdm 1559 79

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1559_79 = 208

    """

    im attr media 100gbase dwdm 1558 98

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1558_98 = 209

    """

    im attr media 100gbase dwdm 1558 17

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1558_17 = 210

    """

    im attr media 100gbase dwdm 1557 36

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1557_36 = 211

    """

    im attr media 100gbase dwdm 1556 55

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1556_55 = 212

    """

    im attr media 100gbase dwdm 1555 75

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1555_75 = 213

    """

    im attr media 100gbase dwdm 1554 94

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1554_94 = 214

    """

    im attr media 100gbase dwdm 1554 13

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1554_13 = 215

    """

    im attr media 100gbase dwdm 1553 33

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1553_33 = 216

    """

    im attr media 100gbase dwdm 1552 52

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1552_52 = 217

    """

    im attr media 100gbase dwdm 1551 72

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1551_72 = 218

    """

    im attr media 100gbase dwdm 1550 92

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1550_92 = 219

    """

    im attr media 100gbase dwdm 1550 12

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1550_12 = 220

    """

    im attr media 100gbase dwdm 1549 32

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1549_32 = 221

    """

    im attr media 100gbase dwdm 1548 51

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1548_51 = 222

    """

    im attr media 100gbase dwdm 1547 72

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1547_72 = 223

    """

    im attr media 100gbase dwdm 1546 92

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1546_92 = 224

    """

    im attr media 100gbase dwdm 1546 12

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1546_12 = 225

    """

    im attr media 100gbase dwdm 1545 32

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1545_32 = 226

    """

    im attr media 100gbase dwdm 1544 53

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1544_53 = 227

    """

    im attr media 100gbase dwdm 1543 73

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1543_73 = 228

    """

    im attr media 100gbase dwdm 1542 94

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1542_94 = 229

    """

    im attr media 100gbase dwdm 1542 14

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1542_14 = 230

    """

    im attr media 100gbase dwdm 1541 35

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1541_35 = 231

    """

    im attr media 100gbase dwdm 1540 56

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1540_56 = 232

    """

    im attr media 100gbase dwdm 1539 77

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1539_77 = 233

    """

    im attr media 100gbase dwdm 1538 98

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1538_98 = 234

    """

    im attr media 100gbase dwdm 1538 19

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1538_19 = 235

    """

    im attr media 100gbase dwdm 1537 40

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1537_40 = 236

    """

    im attr media 100gbase dwdm 1536 61

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1536_61 = 237

    """

    im attr media 100gbase dwdm 1535 82

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1535_82 = 238

    """

    im attr media 100gbase dwdm 1535 04

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1535_04 = 239

    """

    im attr media 100gbase dwdm 1534 25

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1534_25 = 240

    """

    im attr media 100gbase dwdm 1533 47

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1533_47 = 241

    """

    im attr media 100gbase dwdm 1532 68

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1532_68 = 242

    """

    im attr media 100gbase dwdm 1531 90

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1531_90 = 243

    """

    im attr media 100gbase dwdm 1531 12

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1531_12 = 244

    """

    im attr media 100gbase dwdm 1530 33

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_1530_33 = 245

    """

    im attr media 100gbase dwdm tunable

    """
    IM_ATTR_MEDIA_100GBASE_DWDM_TUNABLE = 246

    """

    im attr media 40gbase kr4

    """
    IM_ATTR_MEDIA_40GBASE_KR4 = 247

    """

    im attr media 40gbase cr4

    """
    IM_ATTR_MEDIA_40GBASE_CR4 = 248

    """

    im attr media 40gbase sr4

    """
    IM_ATTR_MEDIA_40GBASE_SR4 = 249

    """

    im attr media 40gbase fr

    """
    IM_ATTR_MEDIA_40GBASE_FR = 250

    """

    im attr media 100gbase cr10

    """
    IM_ATTR_MEDIA_100GBASE_CR10 = 251

    """

    im attr media 100gbase sr10

    """
    IM_ATTR_MEDIA_100GBASE_SR10 = 252

    """

    im attr media 40gbase csr4

    """
    IM_ATTR_MEDIA_40GBASE_CSR4 = 253

    """

    im attr media 10gbase cwdm

    """
    IM_ATTR_MEDIA_10GBASE_CWDM = 254

    """

    im attr media 10gbase cwdm tunable

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_TUNABLE = 255

    """

    im attr media 10gbase cwdm 1470

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1470 = 256

    """

    im attr media 10gbase cwdm 1490

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1490 = 257

    """

    im attr media 10gbase cwdm 1510

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1510 = 258

    """

    im attr media 10gbase cwdm 1530

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1530 = 259

    """

    im attr media 10gbase cwdm 1550

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1550 = 260

    """

    im attr media 10gbase cwdm 1570

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1570 = 261

    """

    im attr media 10gbase cwdm 1590

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1590 = 262

    """

    im attr media 10gbase cwdm 1610

    """
    IM_ATTR_MEDIA_10GBASE_CWDM_1610 = 263

    """

    im attr media 40gbase cwdm

    """
    IM_ATTR_MEDIA_40GBASE_CWDM = 264

    """

    im attr media 40gbase cwdm tunable

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_TUNABLE = 265

    """

    im attr media 40gbase cwdm 1470

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1470 = 266

    """

    im attr media 40gbase cwdm 1490

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1490 = 267

    """

    im attr media 40gbase cwdm 1510

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1510 = 268

    """

    im attr media 40gbase cwdm 1530

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1530 = 269

    """

    im attr media 40gbase cwdm 1550

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1550 = 270

    """

    im attr media 40gbase cwdm 1570

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1570 = 271

    """

    im attr media 40gbase cwdm 1590

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1590 = 272

    """

    im attr media 40gbase cwdm 1610

    """
    IM_ATTR_MEDIA_40GBASE_CWDM_1610 = 273

    """

    im attr media 100gbase cwdm

    """
    IM_ATTR_MEDIA_100GBASE_CWDM = 274

    """

    im attr media 100gbase cwdm tunable

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_TUNABLE = 275

    """

    im attr media 100gbase cwdm 1470

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1470 = 276

    """

    im attr media 100gbase cwdm 1490

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1490 = 277

    """

    im attr media 100gbase cwdm 1510

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1510 = 278

    """

    im attr media 100gbase cwdm 1530

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1530 = 279

    """

    im attr media 100gbase cwdm 1550

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1550 = 280

    """

    im attr media 100gbase cwdm 1570

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1570 = 281

    """

    im attr media 100gbase cwdm 1590

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1590 = 282

    """

    im attr media 100gbase cwdm 1610

    """
    IM_ATTR_MEDIA_100GBASE_CWDM_1610 = 283

    """

    im attr media 40gbase elpb

    """
    IM_ATTR_MEDIA_40GBASE_ELPB = 284

    """

    im attr media 100gbase elpb

    """
    IM_ATTR_MEDIA_100GBASE_ELPB = 285

    """

    im attr media 100gbase lr10

    """
    IM_ATTR_MEDIA_100GBASE_LR10 = 286

    """

    im attr media 40gbase

    """
    IM_ATTR_MEDIA_40GBASE = 287

    """

    im attr media 100gbase kp4

    """
    IM_ATTR_MEDIA_100GBASE_KP4 = 288

    """

    im attr media 100gbase kr4

    """
    IM_ATTR_MEDIA_100GBASE_KR4 = 289

    """

    im attr media 10gbase lrm

    """
    IM_ATTR_MEDIA_10GBASE_LRM = 290

    """

    im attr media 10gbase cx4

    """
    IM_ATTR_MEDIA_10GBASE_CX4 = 291

    """

    im attr media 10gbase

    """
    IM_ATTR_MEDIA_10GBASE = 292

    """

    im attr media 10gbase kx4

    """
    IM_ATTR_MEDIA_10GBASE_KX4 = 293

    """

    im attr media 10gbase kr

    """
    IM_ATTR_MEDIA_10GBASE_KR = 294

    """

    im attr media 10gbase pr

    """
    IM_ATTR_MEDIA_10GBASE_PR = 295

    """

    im attr media 100base lx

    """
    IM_ATTR_MEDIA_100BASE_LX = 296

    """

    im attr media 100base zx

    """
    IM_ATTR_MEDIA_100BASE_ZX = 297

    """

    im attr media 1000base bx d

    """
    IM_ATTR_MEDIA_1000BASE_BX_D = 298

    """

    im attr media 1000base bx u

    """
    IM_ATTR_MEDIA_1000BASE_BX_U = 299

    """

    im attr media 1000base bx20 d

    """
    IM_ATTR_MEDIA_1000BASE_BX20_D = 300

    """

    im attr media 1000base bx20 u

    """
    IM_ATTR_MEDIA_1000BASE_BX20_U = 301

    """

    im attr media 1000base bx40 d

    """
    IM_ATTR_MEDIA_1000BASE_BX40_D = 302

    """

    im attr media 1000base bx40 da

    """
    IM_ATTR_MEDIA_1000BASE_BX40_DA = 303

    """

    im attr media 1000base bx40 u

    """
    IM_ATTR_MEDIA_1000BASE_BX40_U = 304

    """

    im attr media 1000base bx80 d

    """
    IM_ATTR_MEDIA_1000BASE_BX80_D = 305

    """

    im attr media 1000base bx80 u

    """
    IM_ATTR_MEDIA_1000BASE_BX80_U = 306

    """

    im attr media 1000base bx120 d

    """
    IM_ATTR_MEDIA_1000BASE_BX120_D = 307

    """

    im attr media 1000base bx120 u

    """
    IM_ATTR_MEDIA_1000BASE_BX120_U = 308

    """

    im attr media 10gbase bx d

    """
    IM_ATTR_MEDIA_10GBASE_BX_D = 309

    """

    im attr media 10gbase bx u

    """
    IM_ATTR_MEDIA_10GBASE_BX_U = 310

    """

    im attr media 10gbase bx10 d

    """
    IM_ATTR_MEDIA_10GBASE_BX10_D = 311

    """

    im attr media 10gbase bx10 u

    """
    IM_ATTR_MEDIA_10GBASE_BX10_U = 312

    """

    im attr media 10gbase bx20 d

    """
    IM_ATTR_MEDIA_10GBASE_BX20_D = 313

    """

    im attr media 10gbase bx20 u

    """
    IM_ATTR_MEDIA_10GBASE_BX20_U = 314

    """

    im attr media 10gbase bx40 d

    """
    IM_ATTR_MEDIA_10GBASE_BX40_D = 315

    """

    im attr media 10gbase bx40 u

    """
    IM_ATTR_MEDIA_10GBASE_BX40_U = 316

    """

    im attr media 10gbase bx80 d

    """
    IM_ATTR_MEDIA_10GBASE_BX80_D = 317

    """

    im attr media 10gbase bx80 u

    """
    IM_ATTR_MEDIA_10GBASE_BX80_U = 318

    """

    im attr media 10gbase bx120 d

    """
    IM_ATTR_MEDIA_10GBASE_BX120_D = 319

    """

    im attr media 10gbase bx120 u

    """
    IM_ATTR_MEDIA_10GBASE_BX120_U = 320

    """

    im attr media 1000base dr lx

    """
    IM_ATTR_MEDIA_1000BASE_DR_LX = 321

    """

    im attr media 100gbase er4l

    """
    IM_ATTR_MEDIA_100GBASE_ER4L = 322

    """

    im attr media 100gbase sr4

    """
    IM_ATTR_MEDIA_100GBASE_SR4 = 323

    """

    im attr media 40gbase sr bd

    """
    IM_ATTR_MEDIA_40GBASE_SR_BD = 324


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrMedia_Enum']


class ImAttrTransportMode_Enum(Enum):
    """
    ImAttrTransportMode_Enum

    Im attr transport mode

    """

    """

    im attr transport mode unknown

    """
    IM_ATTR_TRANSPORT_MODE_UNKNOWN = 0

    """

    im attr transport mode lan

    """
    IM_ATTR_TRANSPORT_MODE_LAN = 1

    """

    im attr transport mode wan

    """
    IM_ATTR_TRANSPORT_MODE_WAN = 2

    """

    im attr transport mode otn bt opu1e

    """
    IM_ATTR_TRANSPORT_MODE_OTN_BT_OPU1E = 3

    """

    im attr transport mode otn bt opu2e

    """
    IM_ATTR_TRANSPORT_MODE_OTN_BT_OPU2E = 4

    """

    im attr transport mode otn opu3

    """
    IM_ATTR_TRANSPORT_MODE_OTN_OPU3 = 5

    """

    im attr transport mode otn opu4

    """
    IM_ATTR_TRANSPORT_MODE_OTN_OPU4 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImAttrTransportMode_Enum']


class ImCmdEncapsEnum_Enum(Enum):
    """
    ImCmdEncapsEnum_Enum

    Im cmd encaps enum

    """

    """

    frame relay

    """
    FRAME_RELAY = 0

    """

    vlan

    """
    VLAN = 1

    """

    ppp

    """
    PPP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdEncapsEnum_Enum']


class ImCmdFrTypeEnum_Enum(Enum):
    """
    ImCmdFrTypeEnum_Enum

    Im cmd fr type enum

    """

    """

    frame relay cisco

    """
    FRAME_RELAY_CISCO = 0

    """

    frame relay ietf

    """
    FRAME_RELAY_IETF = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdFrTypeEnum_Enum']


class ImCmdIntfTypeEnum_Enum(Enum):
    """
    ImCmdIntfTypeEnum_Enum

    Im cmd intf type enum

    """

    """

    srp

    """
    SRP = 0

    """

    tunnel

    """
    TUNNEL = 1

    """

    bundle

    """
    BUNDLE = 2

    """

    serial

    """
    SERIAL = 3

    """

    sonet pos

    """
    SONET_POS = 4

    """

    tunnel gre

    """
    TUNNEL_GRE = 5

    """

    pseudowire head end

    """
    PSEUDOWIRE_HEAD_END = 6

    """

    cem

    """
    CEM = 7

    """

    gcc

    """
    GCC = 8


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdIntfTypeEnum_Enum']


class ImCmdLmiTypeEnum_Enum(Enum):
    """
    ImCmdLmiTypeEnum_Enum

    Im cmd lmi type enum

    """

    """

    lmi type auto

    """
    LMI_TYPE_AUTO = 0

    """

    lmi type ansi

    """
    LMI_TYPE_ANSI = 1

    """

    lmi type ccitt

    """
    LMI_TYPE_CCITT = 2

    """

    lmi type cisco

    """
    LMI_TYPE_CISCO = 3


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdLmiTypeEnum_Enum']


class ImCmdLoopbackEnum_Enum(Enum):
    """
    ImCmdLoopbackEnum_Enum

    Im cmd loopback enum

    """

    """

    no loopback

    """
    NO_LOOPBACK = 0

    """

    internal loopback

    """
    INTERNAL_LOOPBACK = 1

    """

    external loopback

    """
    EXTERNAL_LOOPBACK = 2

    """

    line loopback

    """
    LINE_LOOPBACK = 3


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdLoopbackEnum_Enum']


class ImCmdStatsEnum_Enum(Enum):
    """
    ImCmdStatsEnum_Enum

    List of different interface stats structures

    """

    """

    full

    """
    FULL = 1

    """

    basic

    """
    BASIC = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImCmdStatsEnum_Enum']


class ImStateEnum_Enum(Enum):
    """
    ImStateEnum_Enum

    Im state enum

    """

    """

    im state not ready

    """
    IM_STATE_NOT_READY = 0

    """

    im state admin down

    """
    IM_STATE_ADMIN_DOWN = 1

    """

    im state down

    """
    IM_STATE_DOWN = 2

    """

    im state up

    """
    IM_STATE_UP = 3

    """

    im state shutdown

    """
    IM_STATE_SHUTDOWN = 4

    """

    im state err disable

    """
    IM_STATE_ERR_DISABLE = 5

    """

    im state down immediate

    """
    IM_STATE_DOWN_IMMEDIATE = 6

    """

    im state down immediate admin

    """
    IM_STATE_DOWN_IMMEDIATE_ADMIN = 7

    """

    im state down graceful

    """
    IM_STATE_DOWN_GRACEFUL = 8

    """

    im state begin shutdown

    """
    IM_STATE_BEGIN_SHUTDOWN = 9

    """

    im state end shutdown

    """
    IM_STATE_END_SHUTDOWN = 10

    """

    im state begin error disable

    """
    IM_STATE_BEGIN_ERROR_DISABLE = 11

    """

    im state end error disable

    """
    IM_STATE_END_ERROR_DISABLE = 12

    """

    im state begin down graceful

    """
    IM_STATE_BEGIN_DOWN_GRACEFUL = 13

    """

    im state reset

    """
    IM_STATE_RESET = 14

    """

    im state operational

    """
    IM_STATE_OPERATIONAL = 15

    """

    im state not operational

    """
    IM_STATE_NOT_OPERATIONAL = 16

    """

    im state unknown

    """
    IM_STATE_UNKNOWN = 17

    """

    im state last

    """
    IM_STATE_LAST = 18


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['ImStateEnum_Enum']


class InterfaceTypeSet_Enum(Enum):
    """
    InterfaceTypeSet_Enum

    Interface type set

    """

    """

    Restrict the output to hardware interfaces only

    """
    HARDWARE_INTERFACES = 0


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['InterfaceTypeSet_Enum']


class NcpIdent_Enum(Enum):
    """
    NcpIdent_Enum

    Ncp ident

    """

    """

    CDP control protocol

    """
    CDPCP = 1

    """

    IPv4 control protocol

    """
    IPCP = 2

    """

    IPv4 Interworking control protocol

    """
    IPCPIW = 3

    """

    IPv6 control protocol

    """
    IPV6CP = 4

    """

    MPLS control protocol

    """
    MPLSCP = 5

    """

    OSI (CLNS) control protocol

    """
    OSICP = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['NcpIdent_Enum']


class PppFsmState_Enum(Enum):
    """
    PppFsmState_Enum

    Ppp fsm state

    """

    """

    Connection Idle

    """
    PPP_FSM_STATE_INITIAL_0 = 0

    """

    This layer required, but lower layer down

    """
    PPP_FSM_STATE_STARTING_1 = 1

    """

    Lower layer up, but this layer not required

    """
    PPP_FSM_STATE_CLOSED_2 = 2

    """

    Listening for a Config Request

    """
    PPP_FSM_STATE_STOPPED_3 = 3

    """

    Shutting down due to local change

    """
    PPP_FSM_STATE_CLOSING_4 = 4

    """

    Shutting down due to peer's actions

    """
    PPP_FSM_STATE_STOPPING_5 = 5

    """

    Config Request Sent

    """
    PPP_FSM_STATE_REQ_SENT_6 = 6

    """

    Config Ack Received

    """
    PPP_FSM_STATE_ACK_RCVD_7 = 7

    """

    Config Ack Sent

    """
    PPP_FSM_STATE_ACK_SENT_8 = 8

    """

    Connection Open

    """
    PPP_FSM_STATE_OPENED_9 = 9


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['PppFsmState_Enum']


class SonetApsEt_Enum(Enum):
    """
    SonetApsEt_Enum

    APS states

    """

    """

    APS not configured on port

    """
    NOT_CONFIGURED = 0

    """

    Working port is up 

    """
    WORKING_ACTIVE = 1

    """

    Protect port is up  

    """
    PROTECT_ACTIVE = 2

    """

    Working port is down 

    """
    WORKING_INACTIVE = 3

    """

    Protect port is down  

    """
    PROTECT_INACTIVE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SonetApsEt_Enum']


class SrpMgmtFailureEt_Enum(Enum):
    """
    SrpMgmtFailureEt_Enum

    SRP failure type

    """

    """

    Hardware missing

    """
    HARDWARE_MISSING_FAILURE = 0

    """

    L1 admin state

    """
    LAYER1_ADMIN_STATE_FAILURE = 1

    """

    Layer 1 error

    """
    LAYER1_ERROR_FAILURE = 2

    """

    Keepalive missed

    """
    KEEPALIVE_MISSED_FAILURE = 3

    """

    Link quality degraded

    """
    LINK_QUALITY_DEGRADED_FAILURE = 4

    """

    Mate problem

    """
    MATE_PROBLEM_FAILURE = 5

    """

    Side mismatch

    """
    SIDE_MISMATCH_FAILURE = 6

    """

    Unknown

    """
    UNKNOWN_FAILURE = 7


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtFailureEt_Enum']


class SrpMgmtFailureStateEt_Enum(Enum):
    """
    SrpMgmtFailureStateEt_Enum

    SRP failure state type

    """

    """

    Idle

    """
    IDLE_FAILURE_STATE = 0

    """

    Wait To Restore

    """
    WAIT_TO_RESTORE_FAILURE_STATE = 1

    """

    Manual Switch

    """
    MANUAL_SWITCH_FAILURE_STATE = 2

    """

    Signal Degrade

    """
    SIGNAL_DEGRADE_FAILURE_STATE = 3

    """

    Signal Fail

    """
    SIGNAL_FAIL_FAILURE_STATE = 4

    """

    Forced Switch

    """
    FORCED_SWITCH_FAILURE_STATE = 5

    """

    Shutdown

    """
    SHUTDOWN_FAILURE_STATE = 6

    """

    Invalid

    """
    INVALID_FAILURE_STATE = 7

    """

    Unknown

    """
    UNKNOWN_FAILURE_STATE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtFailureStateEt_Enum']


class SrpMgmtIpsPathInd_Enum(Enum):
    """
    SrpMgmtIpsPathInd_Enum

    SRP IPS path indication

    """

    """

    SHORT

    """
    SHORT_PATH = 0

    """

    LONG

    """
    LONG_PATH = 1

    """

    UNKNOWN

    """
    UNKNOWN_PATH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsPathInd_Enum']


class SrpMgmtIpsReq_Enum(Enum):
    """
    SrpMgmtIpsReq_Enum

    SRP IPS request type

    """

    """

    Idle

    """
    IDLE_IPS_REQUEST = 0

    """

    Wait To Restore

    """
    WAIT_TO_RESTORE_IPS_REQUEST = 1

    """

    Manual Switch

    """
    MANUAL_SWITCH_IPS_REQUEST = 2

    """

    Signal Degrade

    """
    SIGNAL_DEGRADE_IPS_REQUEST = 3

    """

    Signal Fail

    """
    SIGNAL_FAIL_IPS_REQUEST = 4

    """

    Forced Switch

    """
    FORCED_SWITCH_IPS_REQUEST = 5

    """

    UNKNOWN

    """
    UNKNOWN_IPS_REQUEST = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsReq_Enum']


class SrpMgmtIpsWrapState_Enum(Enum):
    """
    SrpMgmtIpsWrapState_Enum

    SRP IPS side wrap state

    """

    """

    Idle

    """
    IDLE_WRAP_STATE = 0

    """

    Wrapped

    """
    WRAPPED_STATE = 1

    """

    Locked out

    """
    LOCKED_OUT_WRAP_STATE = 2

    """

    UNKNOWN

    """
    UNKNOWN_WRAP_STATE = 3


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtIpsWrapState_Enum']


class SrpMgmtSrrFailure_Enum(Enum):
    """
    SrpMgmtSrrFailure_Enum

    SRP SRR failure type

    """

    """

    Idle

    """
    IDLE_SRR_FAILURE = 0

    """

    Wait To Restore

    """
    WAIT_TO_RESTORE_SRR_FAILURE = 1

    """

    Signal Fail

    """
    SIGNAL_FAIL_SRR_FAILURE = 2

    """

    Forced Switch

    """
    FORCED_SWITCH_SRR_FAILURE = 3

    """

    UNKNOWN

    """
    UNKNOWN_SRR_FAILURE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtSrrFailure_Enum']


class SrpMgmtSrrNodeState_Enum(Enum):
    """
    SrpMgmtSrrNodeState_Enum

    SRP SRR node state

    """

    """

    Idle

    """
    IDLE_SRR_STATE = 0

    """

    Discovery

    """
    DISCOVERY_SRR_STATE = 1

    """

    UNKNOWN

    """
    UNKNOWN_SRR_STATE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['SrpMgmtSrrNodeState_Enum']


class StatsCounter_Enum(Enum):
    """
    StatsCounter_Enum

    Stats counter

    """

    """

    stats counter rate

    """
    STATS_COUNTER_RATE = 0

    """

    stats counter uint32

    """
    STATS_COUNTER_UINT32 = 1

    """

    stats counter uint64

    """
    STATS_COUNTER_UINT64 = 2

    """

    stats counter generic

    """
    STATS_COUNTER_GENERIC = 3

    """

    stats counter proto

    """
    STATS_COUNTER_PROTO = 4

    """

    stats counter srp

    """
    STATS_COUNTER_SRP = 5

    """

    stats counter ipv4 prec

    """
    STATS_COUNTER_IPV4_PREC = 6

    """

    stats counter ipv4 dscp

    """
    STATS_COUNTER_IPV4_DSCP = 7

    """

    stats counter mpls exp

    """
    STATS_COUNTER_MPLS_EXP = 8

    """

    stats counter ipv4 bgppa

    """
    STATS_COUNTER_IPV4_BGPPA = 9

    """

    stats counter src bgppa

    """
    STATS_COUNTER_SRC_BGPPA = 10

    """

    stats counter basic

    """
    STATS_COUNTER_BASIC = 11

    """

    stats counter comp generic

    """
    STATS_COUNTER_COMP_GENERIC = 12

    """

    stats counter comp proto

    """
    STATS_COUNTER_COMP_PROTO = 13

    """

    stats counter comp basic

    """
    STATS_COUNTER_COMP_BASIC = 14

    """

    stats counter accounting

    """
    STATS_COUNTER_ACCOUNTING = 15

    """

    stats counter comp accounting

    """
    STATS_COUNTER_COMP_ACCOUNTING = 16

    """

    stats counter flow

    """
    STATS_COUNTER_FLOW = 17

    """

    stats counter comp flow

    """
    STATS_COUNTER_COMP_FLOW = 18


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsCounter_Enum']


class StatsId_Enum(Enum):
    """
    StatsId_Enum

    Stats id

    """

    """

    stats id type unknown

    """
    STATS_ID_TYPE_UNKNOWN = 0

    """

    stats id type min

    """
    STATS_ID_TYPE_MIN = 1

    """

    stats id type spare

    """
    STATS_ID_TYPE_SPARE = 2

    """

    stats id type node

    """
    STATS_ID_TYPE_NODE = 3

    """

    stats id type other

    """
    STATS_ID_TYPE_OTHER = 4

    """

    stats id type feature

    """
    STATS_ID_TYPE_FEATURE = 5

    """

    stats id type max

    """
    STATS_ID_TYPE_MAX = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsId_Enum']


class StatsTypeContents_Enum(Enum):
    """
    StatsTypeContents_Enum

    Stats type contents

    """

    """

    stats type single

    """
    STATS_TYPE_SINGLE = 100

    """

    stats type variable

    """
    STATS_TYPE_VARIABLE = 101


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['StatsTypeContents_Enum']


class TunlPfiAfId_Enum(Enum):
    """
    TunlPfiAfId_Enum

    Tunl pfi af id

    """

    """

    Unspecified AFI

    """
    TUNL_PFI_AF_ID_NONE = 0

    """

    IPv4 AFI

    """
    TUNL_PFI_AF_ID_IPV4 = 2

    """

    IPv6 AFI

    """
    TUNL_PFI_AF_ID_IPV6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunlPfiAfId_Enum']


class TunnelGreMode_Enum(Enum):
    """
    TunnelGreMode_Enum

    Tunnel gre mode

    """

    """

    Tunnel GRE mode is Unknown

    """
    UNKNOWN = 0

    """

    Tunnel GRE Mode is IPv4

    """
    GR_EO_IPV4 = 1

    """

    Tunnel GRE Mode is IPv6

    """
    GR_EO_IPV6 = 2

    """

    Tunnel MGRE Mode is IPv4

    """
    MGR_EO_IPV4 = 3

    """

    Tunnel MGRE Mode is IPv6

    """
    MGR_EO_IPV6 = 4

    """

    Tunnel Mode is IPv4

    """
    IPV4 = 5

    """

    Tunnel Mode is IPv6

    """
    IPV6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelGreMode_Enum']


class TunnelKaDfState_Enum(Enum):
    """
    TunnelKaDfState_Enum

    Tunnel ka df state

    """

    """

    Tunnel GRE KA State is Disabled

    """
    DISABLE = 0

    """

    Tunnel GRE KA State is Enabled

    """
    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelKaDfState_Enum']


class TunnelKeyState_Enum(Enum):
    """
    TunnelKeyState_Enum

    Tunnel key state

    """

    """

    Tunnel GRE Key is not present

    """
    ABSENT = 0

    """

    Tunnel GRE Key is present

    """
    PRESENT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['TunnelKeyState_Enum']


class VlanEncaps_Enum(Enum):
    """
    VlanEncaps_Enum

    VLAN encapsulation

    """

    """

    No encapsulation

    """
    NO_ENCAPSULATION = 0

    """

    IEEE 802.1Q encapsulation

    """
    DOT1Q = 1

    """

    Double 802.1Q encapsulation

    """
    QINQ = 2

    """

    Double 802.1Q wildcarded encapsulation

    """
    QIN_ANY = 3

    """

    IEEE 802.1Q native VLAN encapsulation

    """
    DOT1Q_NATIVE = 4

    """

    IEEE 802.1ad encapsulation

    """
    DOT1AD = 5

    """

    IEEE 802.1ad native VLAN encapsulation

    """
    DOT1AD_NATIVE = 6

    """

    Ethernet Service Instance

    """
    SERVICE_INSTANCE = 7

    """

    IEEE 802.1ad 802.1Q encapsulation

    """
    DOT1AD_DOT1Q = 8

    """

    IEEE 802.1ad wildcard 802.1Q encapsulation

    """
    DOT1AD_ANY = 9


    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['VlanEncaps_Enum']



class Interfaces(object):
    """
    Interface operational data
    
    .. attribute:: interface_briefs
    
    	Brief operational data for interfaces
    	**type**\: :py:class:`InterfaceBriefs <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs>`
    
    .. attribute:: interface_summary
    
    	Interface summary information
    	**type**\: :py:class:`InterfaceSummary <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary>`
    
    .. attribute:: interface_xr
    
    	Detailed operational data for interfaces and configured features
    	**type**\: :py:class:`InterfaceXr <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr>`
    
    .. attribute:: interfaces
    
    	Descriptions for interfaces
    	**type**\: :py:class:`Interfaces <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces>`
    
    .. attribute:: inventory_summary
    
    	Inventory summary information
    	**type**\: :py:class:`InventorySummary <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary>`
    
    .. attribute:: node_type_sets
    
    	Node and/or interface type specific view of interface summary data
    	**type**\: :py:class:`NodeTypeSets <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets>`
    
    

    """

    _prefix = 'pfi-im-cmd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.interface_briefs = Interfaces.InterfaceBriefs()
        self.interface_briefs.parent = self
        self.interface_summary = Interfaces.InterfaceSummary()
        self.interface_summary.parent = self
        self.interface_xr = Interfaces.InterfaceXr()
        self.interface_xr.parent = self
        self.interfaces = Interfaces.Interfaces()
        self.interfaces.parent = self
        self.inventory_summary = Interfaces.InventorySummary()
        self.inventory_summary.parent = self
        self.node_type_sets = Interfaces.NodeTypeSets()
        self.node_type_sets.parent = self


    class InterfaceBriefs(object):
        """
        Brief operational data for interfaces
        
        .. attribute:: interface_brief
        
        	Brief operational attributes for a particular interface
        	**type**\: list of :py:class:`InterfaceBrief <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceBriefs.InterfaceBrief>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface_brief = YList()
            self.interface_brief.parent = self
            self.interface_brief.name = 'interface_brief'


        class InterfaceBrief(object):
            """
            Brief operational attributes for a particular
            interface
            
            .. attribute:: interface_name
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: actual_line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: actual_state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\: str
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: interface
            
            	Interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: l2_transport
            
            	L2 transport
            	**type**\: bool
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: parent_interface
            
            	Parent Interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: state
            
            	Operational state
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: sub_interface_mtu_overhead
            
            	Subif MTU overhead
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Interface type
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.actual_line_state = None
                self.actual_state = None
                self.bandwidth = None
                self.encapsulation = None
                self.encapsulation_type_string = None
                self.interface = None
                self.l2_transport = None
                self.line_state = None
                self.mtu = None
                self.parent_interface = None
                self.state = None
                self.sub_interface_mtu_overhead = None
                self.type = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-briefs/Cisco-IOS-XR-pfi-im-cmd-oper:interface-brief[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_name is not None:
                    return True

                if self.actual_line_state is not None:
                    return True

                if self.actual_state is not None:
                    return True

                if self.bandwidth is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.encapsulation_type_string is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.l2_transport is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.parent_interface is not None:
                    return True

                if self.state is not None:
                    return True

                if self.sub_interface_mtu_overhead is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceBriefs.InterfaceBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-briefs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface_brief is not None:
                for child_ref in self.interface_brief:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceBriefs']['meta_info']


    class InterfaceSummary(object):
        """
        Interface summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of :py:class:`InterfaceType <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface_counts = Interfaces.InterfaceSummary.InterfaceCounts()
            self.interface_counts.parent = self
            self.interface_type = YList()
            self.interface_type.parent = self
            self.interface_type.name = 'interface_type'


        class InterfaceCounts(object):
            """
            Counts for all interfaces
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.admin_down_interface_count = None
                self.down_interface_count = None
                self.interface_count = None
                self.up_interface_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.admin_down_interface_count is not None:
                    return True

                if self.down_interface_count is not None:
                    return True

                if self.interface_count is not None:
                    return True

                if self.up_interface_count is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceSummary.InterfaceCounts']['meta_info']


        class InterfaceType(object):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\: str
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_counts = Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self.interface_type_description = None
                self.interface_type_name = None


            class InterfaceCounts(object):
                """
                Counts for interfaces of this type
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_down_interface_count = None
                    self.down_interface_count = None
                    self.interface_count = None
                    self.up_interface_count = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.admin_down_interface_count is not None:
                        return True

                    if self.down_interface_count is not None:
                        return True

                    if self.interface_count is not None:
                        return True

                    if self.up_interface_count is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceSummary.InterfaceType.InterfaceCounts']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_counts is not None and self.interface_counts._has_data():
                    return True

                if self.interface_counts is not None and self.interface_counts.is_presence():
                    return True

                if self.interface_type_description is not None:
                    return True

                if self.interface_type_name is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceSummary.InterfaceType']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface_counts is not None and self.interface_counts._has_data():
                return True

            if self.interface_counts is not None and self.interface_counts.is_presence():
                return True

            if self.interface_type is not None:
                for child_ref in self.interface_type:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceSummary']['meta_info']


    class InterfaceXr(object):
        """
        Detailed operational data for interfaces and
        configured features
        
        .. attribute:: interface
        
        	Detailed operational data for a particular interface
        	**type**\: list of :py:class:`Interface <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Detailed operational data for a particular
            interface
            
            .. attribute:: interface_name
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: arp_information
            
            	Interface ARP type and timeout
            	**type**\: :py:class:`ArpInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.ArpInformation>`
            
            .. attribute:: bandwidth
            
            	Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: burned_in_address
            
            	Interface burned in address
            	**type**\: :py:class:`BurnedInAddress <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.BurnedInAddress>`
            
            .. attribute:: carrier_delay
            
            	Carrier Delay
            	**type**\: :py:class:`CarrierDelay <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.CarrierDelay>`
            
            .. attribute:: crc_length
            
            	Cyclic Redundancy Check length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dampening_information
            
            	State dampening information
            	**type**\: :py:class:`DampeningInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DampeningInformation>`
            
            .. attribute:: data_rates
            
            	Packet and byte rates
            	**type**\: :py:class:`DataRates <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.DataRates>`
            
            .. attribute:: description
            
            	Interface description string
            	**type**\: str
            
            .. attribute:: duplexity
            
            	Interface duplexity
            	**type**\: :py:class:`ImAttrDuplex_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrDuplex_Enum>`
            
            .. attribute:: encapsulation
            
            	Interface encapsulation
            	**type**\: str
            
            .. attribute:: encapsulation_information
            
            	Information specific to the encapsulation
            	**type**\: :py:class:`EncapsulationInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation>`
            
            .. attribute:: encapsulation_type_string
            
            	Interface encapsulation description string
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: hardware_type_string
            
            	Hardware type description string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: in_flow_control
            
            	Input flow control configuration
            	**type**\: :py:class:`ImAttrFlowControl_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControl_Enum>`
            
            .. attribute:: interface_handle
            
            	Interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_statistics
            
            	Packet, byte and error counters
            	**type**\: :py:class:`InterfaceStatistics <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics>`
            
            .. attribute:: interface_type
            
            	Interface type
            	**type**\: str
            
            .. attribute:: interface_type_information
            
            	Information specific to the interface type
            	**type**\: :py:class:`InterfaceTypeInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation>`
            
            .. attribute:: ip_information
            
            	Interface IP address info
            	**type**\: :py:class:`IpInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.IpInformation>`
            
            .. attribute:: is_dampening_enabled
            
            	Dampening enabled flag
            	**type**\: bool
            
            .. attribute:: is_data_inverted
            
            	Data invert flag
            	**type**\: bool
            
            .. attribute:: is_l2_looped
            
            	Loopback detected by layer 2
            	**type**\: bool
            
            .. attribute:: is_l2_transport_enabled
            
            	L2 transport flag
            	**type**\: bool
            
            .. attribute:: is_maintenance_enabled
            
            	Maintenance embargo flag
            	**type**\: bool
            
            .. attribute:: is_scramble_enabled
            
            	Interface scramble config
            	**type**\: bool
            
            .. attribute:: keepalive
            
            	Interface keepalive time (s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l2_interface_statistics
            
            	L2 Protocol Statistics
            	**type**\: :py:class:`L2InterfaceStatistics <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics>`
            
            .. attribute:: last_state_transition_time
            
            	The time elasped after the last state transition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: line_state
            
            	Line protocol state
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: link_type
            
            	Interface link type
            	**type**\: :py:class:`ImAttrLink_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrLink_Enum>`
            
            .. attribute:: loopback_configuration
            
            	Interface loopback configuration
            	**type**\: :py:class:`ImCmdLoopbackEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLoopbackEnum_Enum>`
            
            .. attribute:: mac_address
            
            	Interface MAC address
            	**type**\: :py:class:`MacAddress <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.MacAddress>`
            
            .. attribute:: max_bandwidth
            
            	Maximum Interface bandwidth (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: media_type
            
            	Interface media type
            	**type**\: :py:class:`ImAttrMedia_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrMedia_Enum>`
            
            .. attribute:: mtu
            
            	MTU in bytes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nv_optical
            
            	nV Optical Controller Information
            	**type**\: :py:class:`NvOptical <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.NvOptical>`
            
            .. attribute:: out_flow_control
            
            	Output flow control configuration
            	**type**\: :py:class:`ImAttrFlowControl_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrFlowControl_Enum>`
            
            .. attribute:: parent_interface_name
            
            	Parent interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: speed
            
            	Interface speed (Kb/s)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: state
            
            	Interface state
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: state_transition_count
            
            	The number of times the state has changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: transport_mode
            
            	Interface transport mode
            	**type**\: :py:class:`ImAttrTransportMode_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImAttrTransportMode_Enum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.arp_information = Interfaces.InterfaceXr.Interface.ArpInformation()
                self.arp_information.parent = self
                self.bandwidth = None
                self.burned_in_address = Interfaces.InterfaceXr.Interface.BurnedInAddress()
                self.burned_in_address.parent = self
                self.carrier_delay = Interfaces.InterfaceXr.Interface.CarrierDelay()
                self.carrier_delay.parent = self
                self.crc_length = None
                self.dampening_information = Interfaces.InterfaceXr.Interface.DampeningInformation()
                self.dampening_information.parent = self
                self.data_rates = Interfaces.InterfaceXr.Interface.DataRates()
                self.data_rates.parent = self
                self.description = None
                self.duplexity = None
                self.encapsulation = None
                self.encapsulation_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation()
                self.encapsulation_information.parent = self
                self.encapsulation_type_string = None
                self.hardware_type_string = None
                self.in_flow_control = None
                self.interface_handle = None
                self.interface_statistics = Interfaces.InterfaceXr.Interface.InterfaceStatistics()
                self.interface_statistics.parent = self
                self.interface_type = None
                self.interface_type_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation()
                self.interface_type_information.parent = self
                self.ip_information = Interfaces.InterfaceXr.Interface.IpInformation()
                self.ip_information.parent = self
                self.is_dampening_enabled = None
                self.is_data_inverted = None
                self.is_l2_looped = None
                self.is_l2_transport_enabled = None
                self.is_maintenance_enabled = None
                self.is_scramble_enabled = None
                self.keepalive = None
                self.l2_interface_statistics = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics()
                self.l2_interface_statistics.parent = self
                self.last_state_transition_time = None
                self.line_state = None
                self.link_type = None
                self.loopback_configuration = None
                self.mac_address = Interfaces.InterfaceXr.Interface.MacAddress()
                self.mac_address.parent = self
                self.max_bandwidth = None
                self.media_type = None
                self.mtu = None
                self.nv_optical = Interfaces.InterfaceXr.Interface.NvOptical()
                self.nv_optical.parent = self
                self.out_flow_control = None
                self.parent_interface_name = None
                self.speed = None
                self.state = None
                self.state_transition_count = None
                self.transport_mode = None


            class ArpInformation(object):
                """
                Interface ARP type and timeout
                
                .. attribute:: arp_is_learning_disabled
                
                	Whether the interface has dynamic learning disabled
                	**type**\: bool
                
                .. attribute:: arp_timeout
                
                	ARP timeout in seconds. Only valid if 'ARPIsLearningDisabled' is 'false'
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: arp_type_name
                
                	ARP type name
                	**type**\: str
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.arp_is_learning_disabled = None
                    self.arp_timeout = None
                    self.arp_type_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:arp-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.arp_is_learning_disabled is not None:
                        return True

                    if self.arp_timeout is not None:
                        return True

                    if self.arp_type_name is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.ArpInformation']['meta_info']


            class BurnedInAddress(object):
                """
                Interface burned in address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:burned-in-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.address is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.BurnedInAddress']['meta_info']


            class CarrierDelay(object):
                """
                Carrier Delay
                
                .. attribute:: carrier_delay_down
                
                	Carrier delay on state down (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: carrier_delay_up
                
                	Carrier delay on state up (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.carrier_delay_down = None
                    self.carrier_delay_up = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:carrier-delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.carrier_delay_down is not None:
                        return True

                    if self.carrier_delay_up is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.CarrierDelay']['meta_info']


            class DampeningInformation(object):
                """
                State dampening information
                
                .. attribute:: half_life
                
                	Configured decay half life in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_suppressed_enabled
                
                	Flag showing if state is suppressed
                	**type**\: bool
                
                .. attribute:: maximum_suppress_time
                
                	Maximum suppress time in mins
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: penalty
                
                	Dampening penalty of the interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: restart_penalty
                
                	Configured restart penalty
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: reuse_threshold
                
                	Configured reuse threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_remaining
                
                	Remaining period of suppression in secs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: suppress_threshold
                
                	Value of suppress threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.half_life = None
                    self.is_suppressed_enabled = None
                    self.maximum_suppress_time = None
                    self.penalty = None
                    self.restart_penalty = None
                    self.reuse_threshold = None
                    self.seconds_remaining = None
                    self.suppress_threshold = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dampening-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.half_life is not None:
                        return True

                    if self.is_suppressed_enabled is not None:
                        return True

                    if self.maximum_suppress_time is not None:
                        return True

                    if self.penalty is not None:
                        return True

                    if self.restart_penalty is not None:
                        return True

                    if self.reuse_threshold is not None:
                        return True

                    if self.seconds_remaining is not None:
                        return True

                    if self.suppress_threshold is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.DampeningInformation']['meta_info']


            class DataRates(object):
                """
                Packet and byte rates
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bandwidth = None
                    self.input_data_rate = None
                    self.input_load = None
                    self.input_packet_rate = None
                    self.load_interval = None
                    self.output_data_rate = None
                    self.output_load = None
                    self.output_packet_rate = None
                    self.peak_input_data_rate = None
                    self.peak_input_packet_rate = None
                    self.peak_output_data_rate = None
                    self.peak_output_packet_rate = None
                    self.reliability = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:data-rates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.bandwidth is not None:
                        return True

                    if self.input_data_rate is not None:
                        return True

                    if self.input_load is not None:
                        return True

                    if self.input_packet_rate is not None:
                        return True

                    if self.load_interval is not None:
                        return True

                    if self.output_data_rate is not None:
                        return True

                    if self.output_load is not None:
                        return True

                    if self.output_packet_rate is not None:
                        return True

                    if self.peak_input_data_rate is not None:
                        return True

                    if self.peak_input_packet_rate is not None:
                        return True

                    if self.peak_output_data_rate is not None:
                        return True

                    if self.peak_output_packet_rate is not None:
                        return True

                    if self.reliability is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.DataRates']['meta_info']


            class EncapsulationInformation(object):
                """
                Information specific to the encapsulation
                
                .. attribute:: dot1q_information
                
                	VLAN 802.1q information
                	**type**\: :py:class:`Dot1qInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation>`
                
                .. attribute:: encapsulation_type
                
                	EncapsulationType
                	**type**\: :py:class:`ImCmdEncapsEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdEncapsEnum_Enum>`
                
                .. attribute:: frame_relay_information
                
                	Frame Relay information
                	**type**\: :py:class:`FrameRelayInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation>`
                
                .. attribute:: ppp_information
                
                	PPP information
                	**type**\: :py:class:`PppInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dot1q_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation()
                    self.dot1q_information.parent = self
                    self.encapsulation_type = None
                    self.frame_relay_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation()
                    self.frame_relay_information.parent = self
                    self.ppp_information = Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation()
                    self.ppp_information.parent = self


                class Dot1qInformation(object):
                    """
                    VLAN 802.1q information
                    
                    .. attribute:: encapsulation_details
                    
                    	Encapsulation type and tag stack
                    	**type**\: :py:class:`EncapsulationDetails <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.encapsulation_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails()
                        self.encapsulation_details.parent = self


                    class EncapsulationDetails(object):
                        """
                        Encapsulation type and tag stack
                        
                        .. attribute:: dot1ad_dot1q_stack
                        
                        	802.1ad 802.1Q stack value
                        	**type**\: :py:class:`Dot1adDot1qStack <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack>`
                        
                        .. attribute:: dot1ad_native_tag
                        
                        	802.1ad native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_outer_tag
                        
                        	802.1ad Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dot1ad_tag
                        
                        	802.1ad tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: native_tag
                        
                        	Native tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: outer_tag
                        
                        	Outer tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: service_instance_details
                        
                        	Service Instance encapsulation
                        	**type**\: :py:class:`ServiceInstanceDetails <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails>`
                        
                        .. attribute:: stack
                        
                        	Stack value
                        	**type**\: :py:class:`Stack <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack>`
                        
                        .. attribute:: tag
                        
                        	Tag value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vlan_encapsulation
                        
                        	VLANEncapsulation
                        	**type**\: :py:class:`VlanEncaps_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.VlanEncaps_Enum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dot1ad_dot1q_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack()
                            self.dot1ad_dot1q_stack.parent = self
                            self.dot1ad_native_tag = None
                            self.dot1ad_outer_tag = None
                            self.dot1ad_tag = None
                            self.native_tag = None
                            self.outer_tag = None
                            self.service_instance_details = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails()
                            self.service_instance_details.parent = self
                            self.stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack()
                            self.stack.parent = self
                            self.tag = None
                            self.vlan_encapsulation = None


                        class Dot1adDot1qStack(object):
                            """
                            802.1ad 802.1Q stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dot1ad-dot1q-stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Dot1adDot1qStack']['meta_info']


                        class ServiceInstanceDetails(object):
                            """
                            Service Instance encapsulation
                            
                            .. attribute:: destination_mac_match
                            
                            	The destination MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: is_exact_match
                            
                            	Whether the packet must match the encapsulation exactly, with no further inner tags
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_preserving
                            
                            	Whether the native VLAN is customer\-tag preserving
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_native_vlan
                            
                            	Whether this represents the native VLAN on the port
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_traffic_stack
                            
                            	VLAN tags for locally\-sourced traffic
                            	**type**\: :py:class:`LocalTrafficStack <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack>`
                            
                            .. attribute:: payload_ethertype
                            
                            	Payload Ethertype to match
                            	**type**\: :py:class:`EfpPayloadEtype_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.EfpPayloadEtype_Enum>`
                            
                            .. attribute:: pushe
                            
                            	VLAN tags pushed on egress
                            	**type**\: list of :py:class:`Pushe <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe>`
                            
                            .. attribute:: source_mac_match
                            
                            	The source MAC address to match on ingress
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: tags_popped
                            
                            	Number of tags popped on ingress
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: tags_to_match
                            
                            	Tags to match on ingress packets
                            	**type**\: list of :py:class:`TagsToMatch <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.destination_mac_match = None
                                self.is_exact_match = None
                                self.is_native_preserving = None
                                self.is_native_vlan = None
                                self.local_traffic_stack = Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack()
                                self.local_traffic_stack.parent = self
                                self.payload_ethertype = None
                                self.pushe = YList()
                                self.pushe.parent = self
                                self.pushe.name = 'pushe'
                                self.source_mac_match = None
                                self.tags_popped = None
                                self.tags_to_match = YList()
                                self.tags_to_match.parent = self
                                self.tags_to_match.name = 'tags_to_match'


                            class LocalTrafficStack(object):
                                """
                                VLAN tags for locally\-sourced traffic
                                
                                .. attribute:: local_traffic_tag
                                
                                	VLAN tags for locally\-sourced traffic
                                	**type**\: list of :py:class:`LocalTrafficTag <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.local_traffic_tag = YList()
                                    self.local_traffic_tag.parent = self
                                    self.local_traffic_tag.name = 'local_traffic_tag'


                                class LocalTrafficTag(object):
                                    """
                                    VLAN tags for locally\-sourced traffic
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ethertype of tag
                                    	**type**\: :py:class:`EfpTagEtype_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype_Enum>`
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN Id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.ethertype = None
                                        self.vlan_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-traffic-tag'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.ethertype is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-traffic-stack'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.local_traffic_tag is not None:
                                        for child_ref in self.local_traffic_tag:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']


                            class Pushe(object):
                                """
                                VLAN tags pushed on egress
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag
                                	**type**\: :py:class:`EfpTagEtype_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype_Enum>`
                                
                                .. attribute:: vlan_id
                                
                                	VLAN Id
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.vlan_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:pushe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.ethertype is not None:
                                        return True

                                    if self.vlan_id is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info']


                            class TagsToMatch(object):
                                """
                                Tags to match on ingress packets
                                
                                .. attribute:: ethertype
                                
                                	Ethertype of tag to match
                                	**type**\: :py:class:`EfpTagEtype_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagEtype_Enum>`
                                
                                .. attribute:: priority
                                
                                	Priority to match
                                	**type**\: :py:class:`EfpTagPriority_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.EfpTagPriority_Enum>`
                                
                                .. attribute:: vlan_range
                                
                                	VLAN Ids to match
                                	**type**\: list of :py:class:`VlanRange <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.ethertype = None
                                    self.priority = None
                                    self.vlan_range = YList()
                                    self.vlan_range.parent = self
                                    self.vlan_range.name = 'vlan_range'


                                class VlanRange(object):
                                    """
                                    VLAN Ids to match
                                    
                                    .. attribute:: vlan_id_high
                                    
                                    	VLAN ID High
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: vlan_id_low
                                    
                                    	VLAN ID Low
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.vlan_id_high = None
                                        self.vlan_id_low = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:vlan-range'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.vlan_id_high is not None:
                                            return True

                                        if self.vlan_id_low is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tags-to-match'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.ethertype is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.vlan_range is not None:
                                        for child_ref in self.vlan_range:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:service-instance-details'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.destination_mac_match is not None:
                                    return True

                                if self.is_exact_match is not None:
                                    return True

                                if self.is_native_preserving is not None:
                                    return True

                                if self.is_native_vlan is not None:
                                    return True

                                if self.local_traffic_stack is not None and self.local_traffic_stack._has_data():
                                    return True

                                if self.local_traffic_stack is not None and self.local_traffic_stack.is_presence():
                                    return True

                                if self.payload_ethertype is not None:
                                    return True

                                if self.pushe is not None:
                                    for child_ref in self.pushe:
                                        if child_ref._has_data():
                                            return True

                                if self.source_mac_match is not None:
                                    return True

                                if self.tags_popped is not None:
                                    return True

                                if self.tags_to_match is not None:
                                    for child_ref in self.tags_to_match:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']


                        class Stack(object):
                            """
                            Stack value
                            
                            .. attribute:: outer_tag
                            
                            	Outer tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: second_tag
                            
                            	Second tag value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outer_tag = None
                                self.second_tag = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:stack'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.outer_tag is not None:
                                    return True

                                if self.second_tag is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails.Stack']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:encapsulation-details'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack._has_data():
                                return True

                            if self.dot1ad_dot1q_stack is not None and self.dot1ad_dot1q_stack.is_presence():
                                return True

                            if self.dot1ad_native_tag is not None:
                                return True

                            if self.dot1ad_outer_tag is not None:
                                return True

                            if self.dot1ad_tag is not None:
                                return True

                            if self.native_tag is not None:
                                return True

                            if self.outer_tag is not None:
                                return True

                            if self.service_instance_details is not None and self.service_instance_details._has_data():
                                return True

                            if self.service_instance_details is not None and self.service_instance_details.is_presence():
                                return True

                            if self.stack is not None and self.stack._has_data():
                                return True

                            if self.stack is not None and self.stack.is_presence():
                                return True

                            if self.tag is not None:
                                return True

                            if self.vlan_encapsulation is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation.EncapsulationDetails']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:dot1q-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.encapsulation_details is not None and self.encapsulation_details._has_data():
                            return True

                        if self.encapsulation_details is not None and self.encapsulation_details.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.Dot1qInformation']['meta_info']


                class FrameRelayInformation(object):
                    """
                    Frame Relay information
                    
                    .. attribute:: enquiries_received
                    
                    	Number of enquiry messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: enquiries_sent
                    
                    	Number of enquiry messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fr_encapsulation_type
                    
                    	Frame Relay encapsulation type
                    	**type**\: :py:class:`ImCmdFrTypeEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdFrTypeEnum_Enum>`
                    
                    .. attribute:: is_dte
                    
                    	The DTE/DCE LMI interface type
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_enabled
                    
                    	The status of FR LMI for an interface
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_nni_dce_up
                    
                    	Flag indicating whether the LMI  NNI\-DCE state is UP
                    	**type**\: bool
                    
                    .. attribute:: is_lmi_up
                    
                    	Flag indicating whether the LMI  DTE/DCE/NNI\-DTE state is UP
                    	**type**\: bool
                    
                    .. attribute:: is_nni
                    
                    	The NNI LMI interface type
                    	**type**\: bool
                    
                    .. attribute:: lmi_type
                    
                    	The LMI type\: Autosense, ANSI, CCITT or CISCO
                    	**type**\: :py:class:`ImCmdLmiTypeEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdLmiTypeEnum_Enum>`
                    
                    .. attribute:: lmidlci
                    
                    	LMI DLCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_received
                    
                    	Number of status messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_sent
                    
                    	Number of status messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_received
                    
                    	Number of update status messages received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: update_status_sent
                    
                    	Number of update status messages sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.enquiries_received = None
                        self.enquiries_sent = None
                        self.fr_encapsulation_type = None
                        self.is_dte = None
                        self.is_lmi_enabled = None
                        self.is_lmi_nni_dce_up = None
                        self.is_lmi_up = None
                        self.is_nni = None
                        self.lmi_type = None
                        self.lmidlci = None
                        self.status_received = None
                        self.status_sent = None
                        self.update_status_received = None
                        self.update_status_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:frame-relay-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.enquiries_received is not None:
                            return True

                        if self.enquiries_sent is not None:
                            return True

                        if self.fr_encapsulation_type is not None:
                            return True

                        if self.is_dte is not None:
                            return True

                        if self.is_lmi_enabled is not None:
                            return True

                        if self.is_lmi_nni_dce_up is not None:
                            return True

                        if self.is_lmi_up is not None:
                            return True

                        if self.is_nni is not None:
                            return True

                        if self.lmi_type is not None:
                            return True

                        if self.lmidlci is not None:
                            return True

                        if self.status_received is not None:
                            return True

                        if self.status_sent is not None:
                            return True

                        if self.update_status_received is not None:
                            return True

                        if self.update_status_sent is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.FrameRelayInformation']['meta_info']


                class PppInformation(object):
                    """
                    PPP information
                    
                    .. attribute:: is_loopback_detected
                    
                    	Loopback detected
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_mp_bundle_member
                    
                    	MP Bundle Member
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_multilink_open
                    
                    	Is Multilink Open
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lcp_state
                    
                    	LCP State
                    	**type**\: :py:class:`PppFsmState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmState_Enum>`
                    
                    .. attribute:: ncp_info_array
                    
                    	Array of per\-NCP data
                    	**type**\: list of :py:class:`NcpInfoArray <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.is_loopback_detected = None
                        self.is_mp_bundle_member = None
                        self.is_multilink_open = None
                        self.keepalive_period = None
                        self.lcp_state = None
                        self.ncp_info_array = YList()
                        self.ncp_info_array.parent = self
                        self.ncp_info_array.name = 'ncp_info_array'


                    class NcpInfoArray(object):
                        """
                        Array of per\-NCP data
                        
                        .. attribute:: ncp_identifier
                        
                        	NCP state identifier
                        	**type**\: :py:class:`NcpIdent_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.NcpIdent_Enum>`
                        
                        .. attribute:: ncp_state
                        
                        	NCP state value
                        	**type**\: :py:class:`PppFsmState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.PppFsmState_Enum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ncp_identifier = None
                            self.ncp_state = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ncp-info-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.ncp_identifier is not None:
                                return True

                            if self.ncp_state is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation.NcpInfoArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ppp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.is_loopback_detected is not None:
                            return True

                        if self.is_mp_bundle_member is not None:
                            return True

                        if self.is_multilink_open is not None:
                            return True

                        if self.keepalive_period is not None:
                            return True

                        if self.lcp_state is not None:
                            return True

                        if self.ncp_info_array is not None:
                            for child_ref in self.ncp_info_array:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation.PppInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:encapsulation-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.dot1q_information is not None and self.dot1q_information._has_data():
                        return True

                    if self.dot1q_information is not None and self.dot1q_information.is_presence():
                        return True

                    if self.encapsulation_type is not None:
                        return True

                    if self.frame_relay_information is not None and self.frame_relay_information._has_data():
                        return True

                    if self.frame_relay_information is not None and self.frame_relay_information.is_presence():
                        return True

                    if self.ppp_information is not None and self.ppp_information._has_data():
                        return True

                    if self.ppp_information is not None and self.ppp_information.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.EncapsulationInformation']['meta_info']


            class InterfaceStatistics(object):
                """
                Packet, byte and error counters
                
                .. attribute:: basic_interface_stats
                
                	Packet, byte and selected error counters
                	**type**\: :py:class:`BasicInterfaceStats <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats>`
                
                .. attribute:: full_interface_stats
                
                	Packet, byte and all error counters
                	**type**\: :py:class:`FullInterfaceStats <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats>`
                
                .. attribute:: stats_type
                
                	StatsType
                	**type**\: :py:class:`ImCmdStatsEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdStatsEnum_Enum>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.basic_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats()
                    self.basic_interface_stats.parent = self
                    self.full_interface_stats = Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats()
                    self.full_interface_stats.parent = self
                    self.stats_type = None


                class BasicInterfaceStats(object):
                    """
                    Packet, byte and selected error counters
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:basic-interface-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics.BasicInterfaceStats']['meta_info']


                class FullInterfaceStats(object):
                    """
                    Packet, byte and all error counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:full-interface-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics.FullInterfaceStats']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.basic_interface_stats is not None and self.basic_interface_stats._has_data():
                        return True

                    if self.basic_interface_stats is not None and self.basic_interface_stats.is_presence():
                        return True

                    if self.full_interface_stats is not None and self.full_interface_stats._has_data():
                        return True

                    if self.full_interface_stats is not None and self.full_interface_stats.is_presence():
                        return True

                    if self.stats_type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceStatistics']['meta_info']


            class InterfaceTypeInformation(object):
                """
                Information specific to the interface type
                
                .. attribute:: bundle_information
                
                	Bundle interface information
                	**type**\: :py:class:`BundleInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation>`
                
                .. attribute:: cem_information
                
                	Cem interface information
                	**type**\: :py:class:`CemInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation>`
                
                .. attribute:: gcc_information
                
                	GCC interface information
                	**type**\: :py:class:`GccInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation>`
                
                .. attribute:: interface_type_info
                
                	InterfaceTypeInfo
                	**type**\: :py:class:`ImCmdIntfTypeEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImCmdIntfTypeEnum_Enum>`
                
                .. attribute:: pseudowire_head_end_information
                
                	PseudowireHeadEnd interface information
                	**type**\: :py:class:`PseudowireHeadEndInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation>`
                
                .. attribute:: serial_information
                
                	Serial interface information
                	**type**\: :py:class:`SerialInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation>`
                
                .. attribute:: sonet_pos_information
                
                	SONET POS interface information
                	**type**\: :py:class:`SonetPosInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation>`
                
                .. attribute:: srp_information
                
                	SRP interface information
                	**type**\: :py:class:`SrpInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation>`
                
                .. attribute:: tunnel_gre_information
                
                	Tunnel GRE interface information
                	**type**\: :py:class:`TunnelGreInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation>`
                
                .. attribute:: tunnel_information
                
                	Tunnel interface information
                	**type**\: :py:class:`TunnelInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bundle_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation()
                    self.bundle_information.parent = self
                    self.cem_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation()
                    self.cem_information.parent = self
                    self.gcc_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation()
                    self.gcc_information.parent = self
                    self.interface_type_info = None
                    self.pseudowire_head_end_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation()
                    self.pseudowire_head_end_information.parent = self
                    self.serial_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation()
                    self.serial_information.parent = self
                    self.sonet_pos_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation()
                    self.sonet_pos_information.parent = self
                    self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation()
                    self.srp_information.parent = self
                    self.tunnel_gre_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation()
                    self.tunnel_gre_information.parent = self
                    self.tunnel_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation()
                    self.tunnel_information.parent = self


                class BundleInformation(object):
                    """
                    Bundle interface information
                    
                    .. attribute:: member
                    
                    	List of bundle members and their properties
                    	**type**\: list of :py:class:`Member <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        List of bundle members and their properties
                        
                        .. attribute:: bandwidth
                        
                        	Bandwidth of this member (kbps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: iccp_node
                        
                        	Location of member
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name
                        
                        	Member's interface name
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: link_order_number
                        
                        	Member's link order number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_address
                        
                        	MAC address of this member (deprecated)
                        	**type**\: :py:class:`MacAddress <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress>`
                        
                        .. attribute:: member_mux_data
                        
                        	Mux state machine data
                        	**type**\: :py:class:`MemberMuxData <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData>`
                        
                        .. attribute:: member_name
                        
                        	Member's (short form) name
                        	**type**\: str
                        
                        .. attribute:: member_type
                        
                        	Member's type (local/foreign)
                        	**type**\: :py:class:`BmdMemberTypeEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberTypeEnum_Enum>`
                        
                        .. attribute:: port_number
                        
                        	Member's link number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: port_priority
                        
                        	The priority of this member
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: underlying_link_id
                        
                        	Member's underlying link ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth = None
                            self.iccp_node = None
                            self.interface_name = None
                            self.link_order_number = None
                            self.mac_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress()
                            self.mac_address.parent = self
                            self.member_mux_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData()
                            self.member_mux_data.parent = self
                            self.member_name = None
                            self.member_type = None
                            self.port_number = None
                            self.port_priority = None
                            self.underlying_link_id = None


                        class MacAddress(object):
                            """
                            MAC address of this member (deprecated)
                            
                            .. attribute:: address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:mac-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.address is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MacAddress']['meta_info']


                        class MemberMuxData(object):
                            """
                            Mux state machine data
                            
                            .. attribute:: error
                            
                            	Internal value indicating if an error occurred trying to put a link into the desired state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: member_mux_state_reason
                            
                            	Reason for last Mux state change
                            	**type**\: :py:class:`BmMbrStateReason_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmMbrStateReason_Enum>`
                            
                            .. attribute:: member_mux_state_reason_data
                            
                            	Data regarding the reason for last Mux state change
                            	**type**\: :py:class:`MemberMuxStateReasonData <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData>`
                            
                            .. attribute:: member_state
                            
                            	Current internal state of this bundle member
                            	**type**\: :py:class:`BmdMemberState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmdMemberState_Enum>`
                            
                            .. attribute:: mux_state
                            
                            	Current state of this bundle member
                            	**type**\: :py:class:`BmMuxstate_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxstate_Enum>`
                            
                            .. attribute:: mux_state_reason
                            
                            	Reason for last Mux state change (Deprecated)
                            	**type**\: :py:class:`BmMuxreason_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmMuxreason_Enum>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.error = None
                                self.member_mux_state_reason = None
                                self.member_mux_state_reason_data = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData()
                                self.member_mux_state_reason_data.parent = self
                                self.member_state = None
                                self.mux_state = None
                                self.mux_state_reason = None


                            class MemberMuxStateReasonData(object):
                                """
                                Data regarding the reason for last Mux state
                                change
                                
                                .. attribute:: reason_type
                                
                                	The item the reason applies to
                                	**type**\: :py:class:`BmStateReasonTarget_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmStateReasonTarget_Enum>`
                                
                                .. attribute:: severity
                                
                                	The severity of the reason
                                	**type**\: :py:class:`BmSeverity_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.BmSeverity_Enum>`
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.reason_type = None
                                    self.severity = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member-mux-state-reason-data'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.reason_type is not None:
                                        return True

                                    if self.severity is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData.MemberMuxStateReasonData']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member-mux-data'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.error is not None:
                                    return True

                                if self.member_mux_state_reason is not None:
                                    return True

                                if self.member_mux_state_reason_data is not None and self.member_mux_state_reason_data._has_data():
                                    return True

                                if self.member_mux_state_reason_data is not None and self.member_mux_state_reason_data.is_presence():
                                    return True

                                if self.member_state is not None:
                                    return True

                                if self.mux_state is not None:
                                    return True

                                if self.mux_state_reason is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member.MemberMuxData']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:member'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.bandwidth is not None:
                                return True

                            if self.iccp_node is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.link_order_number is not None:
                                return True

                            if self.mac_address is not None and self.mac_address._has_data():
                                return True

                            if self.mac_address is not None and self.mac_address.is_presence():
                                return True

                            if self.member_mux_data is not None and self.member_mux_data._has_data():
                                return True

                            if self.member_mux_data is not None and self.member_mux_data.is_presence():
                                return True

                            if self.member_name is not None:
                                return True

                            if self.member_type is not None:
                                return True

                            if self.port_number is not None:
                                return True

                            if self.port_priority is not None:
                                return True

                            if self.underlying_link_id is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:bundle-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.BundleInformation']['meta_info']


                class CemInformation(object):
                    """
                    Cem interface information
                    
                    .. attribute:: dejitter_buffer
                    
                    	Dejitter buffer length configuredin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: framing
                    
                    	 If framing is TRUE then the CEM  interface is structure aware ; otherwise it is structure agnostic
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: payload
                    
                    	Payload size in bytes configured on CEM interface
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 32. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dejitter_buffer = None
                        self.framing = None
                        self.payload = None
                        self.timeslots = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:cem-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.dejitter_buffer is not None:
                            return True

                        if self.framing is not None:
                            return True

                        if self.payload is not None:
                            return True

                        if self.timeslots is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.CemInformation']['meta_info']


                class GccInformation(object):
                    """
                    GCC interface information
                    
                    .. attribute:: derived_mode
                    
                    	Derived State
                    	**type**\: :py:class:`GccDerState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.GccDerState_Enum>`
                    
                    .. attribute:: sec_state
                    
                    	Sec State 
                    	**type**\: :py:class:`GccSecState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.GccSecState_Enum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.derived_mode = None
                        self.sec_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:gcc-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.derived_mode is not None:
                            return True

                        if self.sec_state is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.GccInformation']['meta_info']


                class PseudowireHeadEndInformation(object):
                    """
                    PseudowireHeadEnd interface information
                    
                    .. attribute:: interface_list_name
                    
                    	Interface list Name
                    	**type**\: str
                    
                    .. attribute:: internal_label
                    
                    	Internal Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2_overhead
                    
                    	L2 Overhead
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_list_name = None
                        self.internal_label = None
                        self.l2_overhead = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:pseudowire-head-end-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interface_list_name is not None:
                            return True

                        if self.internal_label is not None:
                            return True

                        if self.l2_overhead is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.PseudowireHeadEndInformation']['meta_info']


                class SerialInformation(object):
                    """
                    Serial interface information
                    
                    .. attribute:: timeslots
                    
                    	Timeslots separated by \: or \- from 1 to 31. \: indicates individual timeslot and \- represents a range. E.g. 1\-3\:5 represents timeslots 1, 2, 3, and 5
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.timeslots = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:serial-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.timeslots is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SerialInformation']['meta_info']


                class SonetPosInformation(object):
                    """
                    SONET POS interface information
                    
                    .. attribute:: aps_state
                    
                    	APS state
                    	**type**\: :py:class:`SonetApsEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SonetApsEt_Enum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.aps_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:sonet-pos-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.aps_state is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SonetPosInformation']['meta_info']


                class SrpInformation(object):
                    """
                    SRP interface information
                    
                    .. attribute:: srp_information
                    
                    	SRP\-specific data
                    	**type**\: :py:class:`SrpInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation>`
                    
                    .. attribute:: srp_statistics
                    
                    	SRP\-specific packet and byte counters
                    	**type**\: :py:class:`SrpStatistics <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srp_information = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation()
                        self.srp_information.parent = self
                        self.srp_statistics = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics()
                        self.srp_statistics.parent = self


                    class SrpInformation(object):
                        """
                        SRP\-specific data
                        
                        .. attribute:: ips_info
                        
                        	SRP IPS information
                        	**type**\: :py:class:`IpsInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo>`
                        
                        .. attribute:: rate_limit_info
                        
                        	SRP rate limit information
                        	**type**\: :py:class:`RateLimitInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.RateLimitInfo>`
                        
                        .. attribute:: srr_info
                        
                        	SRP SRR information
                        	**type**\: :py:class:`SrrInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo>`
                        
                        .. attribute:: topology_info
                        
                        	SRP topology information
                        	**type**\: :py:class:`TopologyInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ips_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo()
                            self.ips_info.parent = self
                            self.rate_limit_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.RateLimitInfo()
                            self.rate_limit_info.parent = self
                            self.srr_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo()
                            self.srr_info.parent = self
                            self.topology_info = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo()
                            self.topology_info.parent = self


                        class IpsInfo(object):
                            """
                            SRP IPS information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	IPS information
                            	**type**\: list of :py:class:`LocalInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.local_information = YList()
                                self.local_information.parent = self
                                self.local_information.name = 'local_information'


                            class LocalInformation(object):
                                """
                                IPS information
                                
                                .. attribute:: is_inter_card_bus_enabled
                                
                                	Inter card bus enabled
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: mac_address
                                
                                	MAC address for node
                                	**type**\: str
                                
                                .. attribute:: side_a
                                
                                	Side A IPS details
                                	**type**\: :py:class:`SideA <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideA>`
                                
                                .. attribute:: side_b
                                
                                	Side B IPS details
                                	**type**\: :py:class:`SideB <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideB>`
                                
                                .. attribute:: wtr_timer_period
                                
                                	IPS Wait To Restore period in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.is_inter_card_bus_enabled = None
                                    self.mac_address = None
                                    self.side_a = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideA()
                                    self.side_a.parent = self
                                    self.side_b = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideB()
                                    self.side_b.parent = self
                                    self.wtr_timer_period = None


                                class SideA(object):
                                    """
                                    Side A IPS details
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of :py:class:`AssertedFailure <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideA.AssertedFailure>`
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\: str
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\: :py:class:`SrpMgmtIpsPathInd_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd_Enum>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\: str
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\: :py:class:`SrpMgmtIpsPathInd_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd_Enum>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\: :py:class:`SrpMgmtIpsWrapState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapState_Enum>`
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.asserted_failure = YList()
                                        self.asserted_failure.parent = self
                                        self.asserted_failure.name = 'asserted_failure'
                                        self.delay_keep_alive_trigger = None
                                        self.mac_address = None
                                        self.packet_sent_timer = None
                                        self.remote_request = None
                                        self.rx_message_type = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_packet_test = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.self_detected_request = None
                                        self.send_timer_time_remaining = None
                                        self.tx_message_type = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_packet_test = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.wrap_state = None
                                        self.wtr_timer_remaining = None


                                    class AssertedFailure(object):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\: :py:class:`SrpMgmtFailureEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEt_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.current_state = None
                                            self.debounced_delay = None
                                            self.debounced_state = None
                                            self.reported_state = None
                                            self.stable_time = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:asserted-failure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.current_state is not None:
                                                return True

                                            if self.debounced_delay is not None:
                                                return True

                                            if self.debounced_state is not None:
                                                return True

                                            if self.reported_state is not None:
                                                return True

                                            if self.stable_time is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideA.AssertedFailure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.asserted_failure is not None:
                                            for child_ref in self.asserted_failure:
                                                if child_ref._has_data():
                                                    return True

                                        if self.delay_keep_alive_trigger is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.packet_sent_timer is not None:
                                            return True

                                        if self.remote_request is not None:
                                            return True

                                        if self.rx_message_type is not None:
                                            return True

                                        if self.rx_neighbor_mac_address is not None:
                                            return True

                                        if self.rx_packet_test is not None:
                                            return True

                                        if self.rx_path_type is not None:
                                            return True

                                        if self.rx_ttl is not None:
                                            return True

                                        if self.self_detected_request is not None:
                                            return True

                                        if self.send_timer_time_remaining is not None:
                                            return True

                                        if self.tx_message_type is not None:
                                            return True

                                        if self.tx_neighbor_mac_address is not None:
                                            return True

                                        if self.tx_packet_test is not None:
                                            return True

                                        if self.tx_path_type is not None:
                                            return True

                                        if self.tx_ttl is not None:
                                            return True

                                        if self.wrap_state is not None:
                                            return True

                                        if self.wtr_timer_remaining is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideA']['meta_info']


                                class SideB(object):
                                    """
                                    Side B IPS details
                                    
                                    .. attribute:: asserted_failure
                                    
                                    	Failures presently asserted
                                    	**type**\: list of :py:class:`AssertedFailure <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideB.AssertedFailure>`
                                    
                                    .. attribute:: delay_keep_alive_trigger
                                    
                                    	Number of milliseconds to wait after an L1 failure is detected before triggering an L2 wrap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: packet_sent_timer
                                    
                                    	SRP IPS packet send interval in seconds
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remote_request
                                    
                                    	Remote Requests
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: rx_message_type
                                    
                                    	Type of message received
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: rx_neighbor_mac_address
                                    
                                    	Neighbour mac address for received message
                                    	**type**\: str
                                    
                                    .. attribute:: rx_packet_test
                                    
                                    	Test for existence of an RX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: rx_path_type
                                    
                                    	Short/long path for received message
                                    	**type**\: :py:class:`SrpMgmtIpsPathInd_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd_Enum>`
                                    
                                    .. attribute:: rx_ttl
                                    
                                    	Time to live for received message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: self_detected_request
                                    
                                    	Self Detected Requests
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: send_timer_time_remaining
                                    
                                    	Time in seconds remaining until next send of an IPS request
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tx_message_type
                                    
                                    	Type of message transmitted
                                    	**type**\: :py:class:`SrpMgmtIpsReq_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsReq_Enum>`
                                    
                                    .. attribute:: tx_neighbor_mac_address
                                    
                                    	Mac address of node receiving TXed messages
                                    	**type**\: str
                                    
                                    .. attribute:: tx_packet_test
                                    
                                    	Test for existence of a TX packet
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: tx_path_type
                                    
                                    	Short/long path of transmitted message
                                    	**type**\: :py:class:`SrpMgmtIpsPathInd_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsPathInd_Enum>`
                                    
                                    .. attribute:: tx_ttl
                                    
                                    	Time to live for transmitted message
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: wrap_state
                                    
                                    	Wrap state
                                    	**type**\: :py:class:`SrpMgmtIpsWrapState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtIpsWrapState_Enum>`
                                    
                                    .. attribute:: wtr_timer_remaining
                                    
                                    	Time in seconds until wrap removal
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.asserted_failure = YList()
                                        self.asserted_failure.parent = self
                                        self.asserted_failure.name = 'asserted_failure'
                                        self.delay_keep_alive_trigger = None
                                        self.mac_address = None
                                        self.packet_sent_timer = None
                                        self.remote_request = None
                                        self.rx_message_type = None
                                        self.rx_neighbor_mac_address = None
                                        self.rx_packet_test = None
                                        self.rx_path_type = None
                                        self.rx_ttl = None
                                        self.self_detected_request = None
                                        self.send_timer_time_remaining = None
                                        self.tx_message_type = None
                                        self.tx_neighbor_mac_address = None
                                        self.tx_packet_test = None
                                        self.tx_path_type = None
                                        self.tx_ttl = None
                                        self.wrap_state = None
                                        self.wtr_timer_remaining = None


                                    class AssertedFailure(object):
                                        """
                                        Failures presently asserted
                                        
                                        .. attribute:: current_state
                                        
                                        	Current state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: debounced_delay
                                        
                                        	Debounce delay
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: debounced_state
                                        
                                        	Debounced state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: reported_state
                                        
                                        	Reported state
                                        	**type**\: :py:class:`SrpMgmtFailureStateEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureStateEt_Enum>`
                                        
                                        .. attribute:: stable_time
                                        
                                        	Stable time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: type
                                        
                                        	Failure type
                                        	**type**\: :py:class:`SrpMgmtFailureEt_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtFailureEt_Enum>`
                                        
                                        

                                        """

                                        _prefix = 'pfi-im-cmd-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.current_state = None
                                            self.debounced_delay = None
                                            self.debounced_state = None
                                            self.reported_state = None
                                            self.stable_time = None
                                            self.type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:asserted-failure'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_presence():
                                                return True
                                            if self.current_state is not None:
                                                return True

                                            if self.debounced_delay is not None:
                                                return True

                                            if self.debounced_state is not None:
                                                return True

                                            if self.reported_state is not None:
                                                return True

                                            if self.stable_time is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        def is_presence(self):
                                            ''' Returns True if this instance represents presence container else returns False '''
                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideB.AssertedFailure']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.asserted_failure is not None:
                                            for child_ref in self.asserted_failure:
                                                if child_ref._has_data():
                                                    return True

                                        if self.delay_keep_alive_trigger is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.packet_sent_timer is not None:
                                            return True

                                        if self.remote_request is not None:
                                            return True

                                        if self.rx_message_type is not None:
                                            return True

                                        if self.rx_neighbor_mac_address is not None:
                                            return True

                                        if self.rx_packet_test is not None:
                                            return True

                                        if self.rx_path_type is not None:
                                            return True

                                        if self.rx_ttl is not None:
                                            return True

                                        if self.self_detected_request is not None:
                                            return True

                                        if self.send_timer_time_remaining is not None:
                                            return True

                                        if self.tx_message_type is not None:
                                            return True

                                        if self.tx_neighbor_mac_address is not None:
                                            return True

                                        if self.tx_packet_test is not None:
                                            return True

                                        if self.tx_path_type is not None:
                                            return True

                                        if self.tx_ttl is not None:
                                            return True

                                        if self.wrap_state is not None:
                                            return True

                                        if self.wtr_timer_remaining is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation.SideB']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.is_inter_card_bus_enabled is not None:
                                        return True

                                    if self.mac_address is not None:
                                        return True

                                    if self.side_a is not None and self.side_a._has_data():
                                        return True

                                    if self.side_a is not None and self.side_a.is_presence():
                                        return True

                                    if self.side_b is not None and self.side_b._has_data():
                                        return True

                                    if self.side_b is not None and self.side_b.is_presence():
                                        return True

                                    if self.wtr_timer_period is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo.LocalInformation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ips-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.is_admin_down is not None:
                                    return True

                                if self.local_information is not None:
                                    for child_ref in self.local_information:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.IpsInfo']['meta_info']


                        class RateLimitInfo(object):
                            """
                            SRP rate limit information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: rate_limit_detailed_info
                            
                            	SRP rate limit information
                            	**type**\: list of :py:class:`RateLimitDetailedInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.RateLimitInfo.RateLimitDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.rate_limit_detailed_info = YList()
                                self.rate_limit_detailed_info.parent = self
                                self.rate_limit_detailed_info.name = 'rate_limit_detailed_info'


                            class RateLimitDetailedInfo(object):
                                """
                                SRP rate limit information
                                
                                .. attribute:: min_priority_value
                                
                                	Minimum SRP priority for high\-priority transmit queue
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.min_priority_value = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:rate-limit-detailed-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.min_priority_value is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.RateLimitInfo.RateLimitDetailedInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:rate-limit-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.is_admin_down is not None:
                                    return True

                                if self.rate_limit_detailed_info is not None:
                                    for child_ref in self.rate_limit_detailed_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.RateLimitInfo']['meta_info']


                        class SrrInfo(object):
                            """
                            SRP SRR information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_srr_enabled
                            
                            	SRR enabled
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: srr_detailed_info
                            
                            	SRP information
                            	**type**\: list of :py:class:`SrrDetailedInfo <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.is_srr_enabled = None
                                self.srr_detailed_info = YList()
                                self.srr_detailed_info.parent = self
                                self.srr_detailed_info.name = 'srr_detailed_info'


                            class SrrDetailedInfo(object):
                                """
                                SRP information
                                
                                .. attribute:: inner_fail_type
                                
                                	Inner fail type
                                	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                
                                .. attribute:: is_announce
                                
                                	Is announcing enabled
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_inner_ring_in_use
                                
                                	 Is the inner ring in use
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_outer_ring_in_use
                                
                                	Is the outer ring in use
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: is_wrong_version_received
                                
                                	Wrong version recieved
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: last_wrong_version_receive_time
                                
                                	Time that last wrong version message recieved
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mac_address
                                
                                	SRR node mac address
                                	**type**\: str
                                
                                .. attribute:: next_srr_packet_send_time
                                
                                	Time remaining in seconds to next SRR packet send
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: node_state
                                
                                	SRR node state
                                	**type**\: :py:class:`SrpMgmtSrrNodeState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrNodeState_Enum>`
                                
                                .. attribute:: nodes_not_on_ring
                                
                                	nodes not in topology map
                                	**type**\: list of :py:class:`NodesNotOnRing <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo.NodesNotOnRing>`
                                
                                .. attribute:: nodes_on_ring
                                
                                	List of nodes on the ring info
                                	**type**\: list of :py:class:`NodesOnRing <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo.NodesOnRing>`
                                
                                .. attribute:: outer_fail_type
                                
                                	Outer fail type
                                	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                
                                .. attribute:: packet_send_timer
                                
                                	SRR packet send timer interval in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: single_ring_bw
                                
                                	Single ring bandwidth Mbps
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: version_number
                                
                                	Version number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wtr_time
                                
                                	SRR Wait To Restore interval delay in seconds
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wtr_timer_remaining_inner_ring
                                
                                	Time remaining in seconds until next inner ring wrap removal
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: wtr_timer_remaining_outer_ring
                                
                                	Time remaining in seconds until next outer ring wrap removal
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.inner_fail_type = None
                                    self.is_announce = None
                                    self.is_inner_ring_in_use = None
                                    self.is_outer_ring_in_use = None
                                    self.is_wrong_version_received = None
                                    self.last_wrong_version_receive_time = None
                                    self.mac_address = None
                                    self.next_srr_packet_send_time = None
                                    self.node_state = None
                                    self.nodes_not_on_ring = YList()
                                    self.nodes_not_on_ring.parent = self
                                    self.nodes_not_on_ring.name = 'nodes_not_on_ring'
                                    self.nodes_on_ring = YList()
                                    self.nodes_on_ring.parent = self
                                    self.nodes_on_ring.name = 'nodes_on_ring'
                                    self.outer_fail_type = None
                                    self.packet_send_timer = None
                                    self.single_ring_bw = None
                                    self.version_number = None
                                    self.wtr_time = None
                                    self.wtr_timer_remaining_inner_ring = None
                                    self.wtr_timer_remaining_outer_ring = None


                                class NodesNotOnRing(object):
                                    """
                                    nodes not in topology map
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\: str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self.mac_address = None
                                        self.node_name = None
                                        self.outer_failure = None
                                        self.srr_entry_exits = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nodes-not-on-ring'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.inner_failure is not None:
                                            return True

                                        if self.is_last_announce_received is not None:
                                            return True

                                        if self.last_announce_received_time is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        if self.outer_failure is not None:
                                            return True

                                        if self.srr_entry_exits is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo.NodesNotOnRing']['meta_info']


                                class NodesOnRing(object):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: inner_failure
                                    
                                    	Inner failure
                                    	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                    
                                    .. attribute:: is_last_announce_received
                                    
                                    	Announce last received ?
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: last_announce_received_time
                                    
                                    	Announce last received
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mac_address
                                    
                                    	node mac address
                                    	**type**\: str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    .. attribute:: outer_failure
                                    
                                    	Outer failure
                                    	**type**\: :py:class:`SrpMgmtSrrFailure_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.SrpMgmtSrrFailure_Enum>`
                                    
                                    .. attribute:: srr_entry_exits
                                    
                                    	Does the SRR information exist for this node
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.inner_failure = None
                                        self.is_last_announce_received = None
                                        self.last_announce_received_time = None
                                        self.mac_address = None
                                        self.node_name = None
                                        self.outer_failure = None
                                        self.srr_entry_exits = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nodes-on-ring'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.inner_failure is not None:
                                            return True

                                        if self.is_last_announce_received is not None:
                                            return True

                                        if self.last_announce_received_time is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        if self.outer_failure is not None:
                                            return True

                                        if self.srr_entry_exits is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo.NodesOnRing']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srr-detailed-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.inner_fail_type is not None:
                                        return True

                                    if self.is_announce is not None:
                                        return True

                                    if self.is_inner_ring_in_use is not None:
                                        return True

                                    if self.is_outer_ring_in_use is not None:
                                        return True

                                    if self.is_wrong_version_received is not None:
                                        return True

                                    if self.last_wrong_version_receive_time is not None:
                                        return True

                                    if self.mac_address is not None:
                                        return True

                                    if self.next_srr_packet_send_time is not None:
                                        return True

                                    if self.node_state is not None:
                                        return True

                                    if self.nodes_not_on_ring is not None:
                                        for child_ref in self.nodes_not_on_ring:
                                            if child_ref._has_data():
                                                return True

                                    if self.nodes_on_ring is not None:
                                        for child_ref in self.nodes_on_ring:
                                            if child_ref._has_data():
                                                return True

                                    if self.outer_fail_type is not None:
                                        return True

                                    if self.packet_send_timer is not None:
                                        return True

                                    if self.single_ring_bw is not None:
                                        return True

                                    if self.version_number is not None:
                                        return True

                                    if self.wtr_time is not None:
                                        return True

                                    if self.wtr_timer_remaining_inner_ring is not None:
                                        return True

                                    if self.wtr_timer_remaining_outer_ring is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo.SrrDetailedInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srr-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.is_admin_down is not None:
                                    return True

                                if self.is_srr_enabled is not None:
                                    return True

                                if self.srr_detailed_info is not None:
                                    for child_ref in self.srr_detailed_info:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.SrrInfo']['meta_info']


                        class TopologyInfo(object):
                            """
                            SRP topology information
                            
                            .. attribute:: is_admin_down
                            
                            	Is the interfaceadministratively down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: local_information
                            
                            	Detailed SRP topology information
                            	**type**\: list of :py:class:`LocalInformation <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo.LocalInformation>`
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.is_admin_down = None
                                self.local_information = YList()
                                self.local_information.parent = self
                                self.local_information.name = 'local_information'


                            class LocalInformation(object):
                                """
                                Detailed SRP topology information
                                
                                .. attribute:: next_topology_packet_delay
                                
                                	Time remaining until next topo pkt sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: number_of_nodes_on_ring
                                
                                	Number of nodes on ring
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: ring_node
                                
                                	List of nodes on the ring info
                                	**type**\: list of :py:class:`RingNode <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo.LocalInformation.RingNode>`
                                
                                .. attribute:: time_since_last_topology_change
                                
                                	Time since last topology change
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_since_last_topology_packet_received
                                
                                	Time since last topo pkt was received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: topology_timer
                                
                                	How often a topology pkt is sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'pfi-im-cmd-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.next_topology_packet_delay = None
                                    self.number_of_nodes_on_ring = None
                                    self.ring_node = YList()
                                    self.ring_node.parent = self
                                    self.ring_node.name = 'ring_node'
                                    self.time_since_last_topology_change = None
                                    self.time_since_last_topology_packet_received = None
                                    self.topology_timer = None


                                class RingNode(object):
                                    """
                                    List of nodes on the ring info
                                    
                                    .. attribute:: hop_count
                                    
                                    	Outer\-ring hops to reach this node
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: is_srr_supported
                                    
                                    	SRR protocol supported
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: is_wrapped
                                    
                                    	Wrap state
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: mac_address
                                    
                                    	MAC address
                                    	**type**\: str
                                    
                                    .. attribute:: node_name
                                    
                                    	Node name
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'pfi-im-cmd-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.hop_count = None
                                        self.ipv4_address = None
                                        self.is_srr_supported = None
                                        self.is_wrapped = None
                                        self.mac_address = None
                                        self.node_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ring-node'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.is_presence():
                                            return True
                                        if self.hop_count is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.is_srr_supported is not None:
                                            return True

                                        if self.is_wrapped is not None:
                                            return True

                                        if self.mac_address is not None:
                                            return True

                                        if self.node_name is not None:
                                            return True

                                        return False

                                    def is_presence(self):
                                        ''' Returns True if this instance represents presence container else returns False '''
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo.LocalInformation.RingNode']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:local-information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    if self.next_topology_packet_delay is not None:
                                        return True

                                    if self.number_of_nodes_on_ring is not None:
                                        return True

                                    if self.ring_node is not None:
                                        for child_ref in self.ring_node:
                                            if child_ref._has_data():
                                                return True

                                    if self.time_since_last_topology_change is not None:
                                        return True

                                    if self.time_since_last_topology_packet_received is not None:
                                        return True

                                    if self.topology_timer is not None:
                                        return True

                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo.LocalInformation']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:topology-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.is_admin_down is not None:
                                    return True

                                if self.local_information is not None:
                                    for child_ref in self.local_information:
                                        if child_ref._has_data():
                                            return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation.TopologyInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-information'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.ips_info is not None and self.ips_info._has_data():
                                return True

                            if self.ips_info is not None and self.ips_info.is_presence():
                                return True

                            if self.rate_limit_info is not None and self.rate_limit_info._has_data():
                                return True

                            if self.rate_limit_info is not None and self.rate_limit_info.is_presence():
                                return True

                            if self.srr_info is not None and self.srr_info._has_data():
                                return True

                            if self.srr_info is not None and self.srr_info.is_presence():
                                return True

                            if self.topology_info is not None and self.topology_info._has_data():
                                return True

                            if self.topology_info is not None and self.topology_info.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpInformation']['meta_info']


                    class SrpStatistics(object):
                        """
                        SRP\-specific packet and byte counters
                        
                        .. attribute:: data_rate_interval
                        
                        	Data rate interval (5 mins or 30 seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: side_a_data_rate
                        
                        	Data rates for side A interface
                        	**type**\: :py:class:`SideADataRate <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate>`
                        
                        .. attribute:: side_a_errors
                        
                        	Errors for side A interface
                        	**type**\: :py:class:`SideAErrors <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors>`
                        
                        .. attribute:: side_b_data_rate
                        
                        	Data rates for side B interface
                        	**type**\: :py:class:`SideBDataRate <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate>`
                        
                        .. attribute:: side_b_errors
                        
                        	Errors for side B interface
                        	**type**\: :py:class:`SideBErrors <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.data_rate_interval = None
                            self.side_a_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate()
                            self.side_a_data_rate.parent = self
                            self.side_a_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors()
                            self.side_a_errors.parent = self
                            self.side_b_data_rate = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate()
                            self.side_b_data_rate.parent = self
                            self.side_b_errors = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors()
                            self.side_b_errors.parent = self


                        class SideADataRate(object):
                            """
                            Data rates for side A interface
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bit_rate_received = None
                                self.bit_rate_sent = None
                                self.packet_rate_received = None
                                self.packet_rate_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a-data-rate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bit_rate_received is not None:
                                    return True

                                if self.bit_rate_sent is not None:
                                    return True

                                if self.packet_rate_received is not None:
                                    return True

                                if self.packet_rate_sent is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideADataRate']['meta_info']


                        class SideAErrors(object):
                            """
                            Errors for side A interface
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.crc_errors = None
                                self.error_packets_received = None
                                self.framer_aborts_received = None
                                self.framer_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_giant_packets_received = None
                                self.mac_runt_packets_received = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-a-errors'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.crc_errors is not None:
                                    return True

                                if self.error_packets_received is not None:
                                    return True

                                if self.framer_aborts_received is not None:
                                    return True

                                if self.framer_giant_packets_received is not None:
                                    return True

                                if self.framer_runt_packets_received is not None:
                                    return True

                                if self.input_insufficient_resource_events is not None:
                                    return True

                                if self.mac_aborts_received is not None:
                                    return True

                                if self.mac_giant_packets_received is not None:
                                    return True

                                if self.mac_runt_packets_received is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideAErrors']['meta_info']


                        class SideBDataRate(object):
                            """
                            Data rates for side B interface
                            
                            .. attribute:: bit_rate_received
                            
                            	Received bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bit_rate_sent
                            
                            	Sent bit rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_received
                            
                            	Received packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: packet_rate_sent
                            
                            	Sent packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.bit_rate_received = None
                                self.bit_rate_sent = None
                                self.packet_rate_received = None
                                self.packet_rate_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b-data-rate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.bit_rate_received is not None:
                                    return True

                                if self.bit_rate_sent is not None:
                                    return True

                                if self.packet_rate_received is not None:
                                    return True

                                if self.packet_rate_sent is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBDataRate']['meta_info']


                        class SideBErrors(object):
                            """
                            Errors for side B interface
                            
                            .. attribute:: crc_errors
                            
                            	Input CRC errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: error_packets_received
                            
                            	Error packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_aborts_received
                            
                            	Aborts received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_giant_packets_received
                            
                            	Too large packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: framer_runt_packets_received
                            
                            	Too small packets received at framer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_insufficient_resource_events
                            
                            	Input insufficient resources events
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_aborts_received
                            
                            	Aborts received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_giant_packets_received
                            
                            	Too large packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_runt_packets_received
                            
                            	Too small packets received at MAC/RAC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'pfi-im-cmd-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.crc_errors = None
                                self.error_packets_received = None
                                self.framer_aborts_received = None
                                self.framer_giant_packets_received = None
                                self.framer_runt_packets_received = None
                                self.input_insufficient_resource_events = None
                                self.mac_aborts_received = None
                                self.mac_giant_packets_received = None
                                self.mac_runt_packets_received = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:side-b-errors'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.crc_errors is not None:
                                    return True

                                if self.error_packets_received is not None:
                                    return True

                                if self.framer_aborts_received is not None:
                                    return True

                                if self.framer_giant_packets_received is not None:
                                    return True

                                if self.framer_runt_packets_received is not None:
                                    return True

                                if self.input_insufficient_resource_events is not None:
                                    return True

                                if self.mac_aborts_received is not None:
                                    return True

                                if self.mac_giant_packets_received is not None:
                                    return True

                                if self.mac_runt_packets_received is not None:
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                                return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics.SideBErrors']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-statistics'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.data_rate_interval is not None:
                                return True

                            if self.side_a_data_rate is not None and self.side_a_data_rate._has_data():
                                return True

                            if self.side_a_data_rate is not None and self.side_a_data_rate.is_presence():
                                return True

                            if self.side_a_errors is not None and self.side_a_errors._has_data():
                                return True

                            if self.side_a_errors is not None and self.side_a_errors.is_presence():
                                return True

                            if self.side_b_data_rate is not None and self.side_b_data_rate._has_data():
                                return True

                            if self.side_b_data_rate is not None and self.side_b_data_rate.is_presence():
                                return True

                            if self.side_b_errors is not None and self.side_b_errors._has_data():
                                return True

                            if self.side_b_errors is not None and self.side_b_errors.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation.SrpStatistics']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:srp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.srp_information is not None and self.srp_information._has_data():
                            return True

                        if self.srp_information is not None and self.srp_information.is_presence():
                            return True

                        if self.srp_statistics is not None and self.srp_statistics._has_data():
                            return True

                        if self.srp_statistics is not None and self.srp_statistics.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.SrpInformation']['meta_info']


                class TunnelGreInformation(object):
                    """
                    Tunnel GRE interface information
                    
                    .. attribute:: destination_ip_address
                    
                    	Tunnel destination IP address
                    	**type**\: :py:class:`DestinationIpAddress <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress>`
                    
                    .. attribute:: df_bit_state
                    
                    	DF Bit State
                    	**type**\: :py:class:`TunnelKaDfState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfState_Enum>`
                    
                    .. attribute:: keepalive_maximum_retry
                    
                    	Keepalive retry
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: keepalive_period
                    
                    	Keepalive period in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: keepalive_state
                    
                    	Keepalive State
                    	**type**\: :py:class:`TunnelKaDfState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKaDfState_Enum>`
                    
                    .. attribute:: key
                    
                    	Key value for GRE Packet
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: key_bit_state
                    
                    	Key Config State
                    	**type**\: :py:class:`TunnelKeyState_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelKeyState_Enum>`
                    
                    .. attribute:: source_ip_address
                    
                    	Tunnel source IP address
                    	**type**\: :py:class:`SourceIpAddress <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress>`
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\: str
                    
                    .. attribute:: tunnel_mode
                    
                    	Tunnel GRE Mode
                    	**type**\: :py:class:`TunnelGreMode_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunnelGreMode_Enum>`
                    
                    .. attribute:: tunnel_tos
                    
                    	GRE tunnel TOS
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tunnel_ttl
                    
                    	GRE tunnel TTL
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress()
                        self.destination_ip_address.parent = self
                        self.df_bit_state = None
                        self.keepalive_maximum_retry = None
                        self.keepalive_period = None
                        self.keepalive_state = None
                        self.key = None
                        self.key_bit_state = None
                        self.source_ip_address = Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress()
                        self.source_ip_address.parent = self
                        self.source_name = None
                        self.tunnel_mode = None
                        self.tunnel_tos = None
                        self.tunnel_ttl = None


                    class DestinationIpAddress(object):
                        """
                        Tunnel destination IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\: :py:class:`TunlPfiAfId_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfId_Enum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:destination-ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.afi is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.DestinationIpAddress']['meta_info']


                    class SourceIpAddress(object):
                        """
                        Tunnel source IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\: :py:class:`TunlPfiAfId_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.TunlPfiAfId_Enum>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.afi = None
                            self.ipv4 = None
                            self.ipv6 = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:source-ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.afi is not None:
                                return True

                            if self.ipv4 is not None:
                                return True

                            if self.ipv6 is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation.SourceIpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tunnel-gre-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.destination_ip_address is not None and self.destination_ip_address._has_data():
                            return True

                        if self.destination_ip_address is not None and self.destination_ip_address.is_presence():
                            return True

                        if self.df_bit_state is not None:
                            return True

                        if self.keepalive_maximum_retry is not None:
                            return True

                        if self.keepalive_period is not None:
                            return True

                        if self.keepalive_state is not None:
                            return True

                        if self.key is not None:
                            return True

                        if self.key_bit_state is not None:
                            return True

                        if self.source_ip_address is not None and self.source_ip_address._has_data():
                            return True

                        if self.source_ip_address is not None and self.source_ip_address.is_presence():
                            return True

                        if self.source_name is not None:
                            return True

                        if self.tunnel_mode is not None:
                            return True

                        if self.tunnel_tos is not None:
                            return True

                        if self.tunnel_ttl is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelGreInformation']['meta_info']


                class TunnelInformation(object):
                    """
                    Tunnel interface information
                    
                    .. attribute:: destination_ipv4_address
                    
                    	Tunnel destination IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: key
                    
                    	GRE tunnel key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_ipv4_address
                    
                    	Tunnel source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: source_name
                    
                    	Tunnel source name
                    	**type**\: str
                    
                    .. attribute:: ttl
                    
                    	GRE tunnel TTL
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tunnel_type
                    
                    	Tunnel protocol/transport
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_ipv4_address = None
                        self.key = None
                        self.source_ipv4_address = None
                        self.source_name = None
                        self.ttl = None
                        self.tunnel_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:tunnel-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.destination_ipv4_address is not None:
                            return True

                        if self.key is not None:
                            return True

                        if self.source_ipv4_address is not None:
                            return True

                        if self.source_name is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        if self.tunnel_type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation.TunnelInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.bundle_information is not None and self.bundle_information._has_data():
                        return True

                    if self.bundle_information is not None and self.bundle_information.is_presence():
                        return True

                    if self.cem_information is not None and self.cem_information._has_data():
                        return True

                    if self.cem_information is not None and self.cem_information.is_presence():
                        return True

                    if self.gcc_information is not None and self.gcc_information._has_data():
                        return True

                    if self.gcc_information is not None and self.gcc_information.is_presence():
                        return True

                    if self.interface_type_info is not None:
                        return True

                    if self.pseudowire_head_end_information is not None and self.pseudowire_head_end_information._has_data():
                        return True

                    if self.pseudowire_head_end_information is not None and self.pseudowire_head_end_information.is_presence():
                        return True

                    if self.serial_information is not None and self.serial_information._has_data():
                        return True

                    if self.serial_information is not None and self.serial_information.is_presence():
                        return True

                    if self.sonet_pos_information is not None and self.sonet_pos_information._has_data():
                        return True

                    if self.sonet_pos_information is not None and self.sonet_pos_information.is_presence():
                        return True

                    if self.srp_information is not None and self.srp_information._has_data():
                        return True

                    if self.srp_information is not None and self.srp_information.is_presence():
                        return True

                    if self.tunnel_gre_information is not None and self.tunnel_gre_information._has_data():
                        return True

                    if self.tunnel_gre_information is not None and self.tunnel_gre_information.is_presence():
                        return True

                    if self.tunnel_information is not None and self.tunnel_information._has_data():
                        return True

                    if self.tunnel_information is not None and self.tunnel_information.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.InterfaceTypeInformation']['meta_info']


            class IpInformation(object):
                """
                Interface IP address info
                
                .. attribute:: ip_address
                
                	Interface IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: subnet_mask_length
                
                	Interface subnet mask length
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ip_address = None
                    self.subnet_mask_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:ip-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.ip_address is not None:
                        return True

                    if self.subnet_mask_length is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.IpInformation']['meta_info']


            class L2InterfaceStatistics(object):
                """
                L2 Protocol Statistics
                
                .. attribute:: block_array
                
                	Block Array
                	**type**\: list of :py:class:`BlockArray <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray>`
                
                .. attribute:: contents
                
                	Bag contents
                	**type**\: :py:class:`StatsTypeContents_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.StatsTypeContents_Enum>`
                
                .. attribute:: element_array
                
                	Element Array
                	**type**\: list of :py:class:`ElementArray <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray>`
                
                .. attribute:: stats_id
                
                	Identifier
                	**type**\: :py:class:`StatsId <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId>`
                
                .. attribute:: stats_type
                
                	Stats type value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.block_array = YList()
                    self.block_array.parent = self
                    self.block_array.name = 'block_array'
                    self.contents = None
                    self.element_array = YList()
                    self.element_array.parent = self
                    self.element_array.name = 'element_array'
                    self.stats_id = Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId()
                    self.stats_id.parent = self
                    self.stats_type = None


                class BlockArray(object):
                    """
                    Block Array
                    
                    .. attribute:: count
                    
                    	count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: type
                    
                    	type
                    	**type**\: :py:class:`StatsCounter_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounter_Enum>`
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.count = None
                        self.data = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:block-array'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.count is not None:
                            return True

                        if self.data is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.BlockArray']['meta_info']


                class ElementArray(object):
                    """
                    Element Array
                    
                    .. attribute:: block_array
                    
                    	block array
                    	**type**\: list of :py:class:`BlockArray <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray>`
                    
                    .. attribute:: key
                    
                    	key
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.block_array = YList()
                        self.block_array.parent = self
                        self.block_array.name = 'block_array'
                        self.key = None


                    class BlockArray(object):
                        """
                        block array
                        
                        .. attribute:: count
                        
                        	count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: data
                        
                        	data
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: type
                        
                        	type
                        	**type**\: :py:class:`StatsCounter_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.StatsCounter_Enum>`
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.count = None
                            self.data = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:block-array'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.count is not None:
                                return True

                            if self.data is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray.BlockArray']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:element-array'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.block_array is not None:
                            for child_ref in self.block_array:
                                if child_ref._has_data():
                                    return True

                        if self.key is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.ElementArray']['meta_info']


                class StatsId(object):
                    """
                    Identifier
                    
                    .. attribute:: feature_id
                    
                    	Feature ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id
                    
                    	ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id_type
                    
                    	id type
                    	**type**\: :py:class:`StatsId_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.StatsId_Enum>`
                    
                    .. attribute:: interface_handle
                    
                    	Interface Handle
                    	**type**\: str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: node_id
                    
                    	Node ID
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: unused
                    
                    	Unused
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.feature_id = None
                        self.id = None
                        self.id_type = None
                        self.interface_handle = None
                        self.node_id = None
                        self.unused = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:stats-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.feature_id is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.id_type is not None:
                            return True

                        if self.interface_handle is not None:
                            return True

                        if self.node_id is not None:
                            return True

                        if self.unused is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics.StatsId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:l2-interface-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.block_array is not None:
                        for child_ref in self.block_array:
                            if child_ref._has_data():
                                return True

                    if self.contents is not None:
                        return True

                    if self.element_array is not None:
                        for child_ref in self.element_array:
                            if child_ref._has_data():
                                return True

                    if self.stats_id is not None and self.stats_id._has_data():
                        return True

                    if self.stats_id is not None and self.stats_id.is_presence():
                        return True

                    if self.stats_type is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.L2InterfaceStatistics']['meta_info']


            class MacAddress(object):
                """
                Interface MAC address
                
                .. attribute:: address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:mac-address'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.address is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.MacAddress']['meta_info']


            class NvOptical(object):
                """
                nV Optical Controller Information
                
                .. attribute:: controller
                
                	Controller that nV controller maps to
                	**type**\: str
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.controller = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-pfi-im-cmd-oper:nv-optical'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.controller is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InterfaceXr.Interface.NvOptical']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-xr/Cisco-IOS-XR-pfi-im-cmd-oper:interface[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_name is not None:
                    return True

                if self.arp_information is not None and self.arp_information._has_data():
                    return True

                if self.arp_information is not None and self.arp_information.is_presence():
                    return True

                if self.bandwidth is not None:
                    return True

                if self.burned_in_address is not None and self.burned_in_address._has_data():
                    return True

                if self.burned_in_address is not None and self.burned_in_address.is_presence():
                    return True

                if self.carrier_delay is not None and self.carrier_delay._has_data():
                    return True

                if self.carrier_delay is not None and self.carrier_delay.is_presence():
                    return True

                if self.crc_length is not None:
                    return True

                if self.dampening_information is not None and self.dampening_information._has_data():
                    return True

                if self.dampening_information is not None and self.dampening_information.is_presence():
                    return True

                if self.data_rates is not None and self.data_rates._has_data():
                    return True

                if self.data_rates is not None and self.data_rates.is_presence():
                    return True

                if self.description is not None:
                    return True

                if self.duplexity is not None:
                    return True

                if self.encapsulation is not None:
                    return True

                if self.encapsulation_information is not None and self.encapsulation_information._has_data():
                    return True

                if self.encapsulation_information is not None and self.encapsulation_information.is_presence():
                    return True

                if self.encapsulation_type_string is not None:
                    return True

                if self.hardware_type_string is not None:
                    return True

                if self.in_flow_control is not None:
                    return True

                if self.interface_handle is not None:
                    return True

                if self.interface_statistics is not None and self.interface_statistics._has_data():
                    return True

                if self.interface_statistics is not None and self.interface_statistics.is_presence():
                    return True

                if self.interface_type is not None:
                    return True

                if self.interface_type_information is not None and self.interface_type_information._has_data():
                    return True

                if self.interface_type_information is not None and self.interface_type_information.is_presence():
                    return True

                if self.ip_information is not None and self.ip_information._has_data():
                    return True

                if self.ip_information is not None and self.ip_information.is_presence():
                    return True

                if self.is_dampening_enabled is not None:
                    return True

                if self.is_data_inverted is not None:
                    return True

                if self.is_l2_looped is not None:
                    return True

                if self.is_l2_transport_enabled is not None:
                    return True

                if self.is_maintenance_enabled is not None:
                    return True

                if self.is_scramble_enabled is not None:
                    return True

                if self.keepalive is not None:
                    return True

                if self.l2_interface_statistics is not None and self.l2_interface_statistics._has_data():
                    return True

                if self.l2_interface_statistics is not None and self.l2_interface_statistics.is_presence():
                    return True

                if self.last_state_transition_time is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.link_type is not None:
                    return True

                if self.loopback_configuration is not None:
                    return True

                if self.mac_address is not None and self.mac_address._has_data():
                    return True

                if self.mac_address is not None and self.mac_address.is_presence():
                    return True

                if self.max_bandwidth is not None:
                    return True

                if self.media_type is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.nv_optical is not None and self.nv_optical._has_data():
                    return True

                if self.nv_optical is not None and self.nv_optical.is_presence():
                    return True

                if self.out_flow_control is not None:
                    return True

                if self.parent_interface_name is not None:
                    return True

                if self.speed is not None:
                    return True

                if self.state is not None:
                    return True

                if self.state_transition_count is not None:
                    return True

                if self.transport_mode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InterfaceXr.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface-xr'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InterfaceXr']['meta_info']


    class Interfaces(object):
        """
        Descriptions for interfaces
        
        .. attribute:: interface
        
        	Description for a particular interface
        	**type**\: list of :py:class:`Interface <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.Interfaces.Interface>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Description for a particular interface
            
            .. attribute:: interface_name
            
            	The name of the interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: description
            
            	Interface description string
            	**type**\: str
            
            .. attribute:: interface
            
            	Interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: line_state
            
            	Line protocol state with no translation of error disable or shutdown
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            .. attribute:: state
            
            	Operational state with no translation of error disable or shutdown
            	**type**\: :py:class:`ImStateEnum_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.ImStateEnum_Enum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.description = None
                self.interface = None
                self.line_state = None
                self.state = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interface[Cisco-IOS-XR-pfi-im-cmd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_name is not None:
                    return True

                if self.description is not None:
                    return True

                if self.interface is not None:
                    return True

                if self.line_state is not None:
                    return True

                if self.state is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.Interfaces']['meta_info']


    class InventorySummary(object):
        """
        Inventory summary information
        
        .. attribute:: interface_counts
        
        	Counts for all interfaces
        	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceCounts>`
        
        .. attribute:: interface_type
        
        	List of per interface type summary information
        	**type**\: list of :py:class:`InterfaceType <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface_counts = Interfaces.InventorySummary.InterfaceCounts()
            self.interface_counts.parent = self
            self.interface_type = YList()
            self.interface_type.parent = self
            self.interface_type.name = 'interface_type'


        class InterfaceCounts(object):
            """
            Counts for all interfaces
            
            .. attribute:: admin_down_interface_count
            
            	Number of interfaces in an ADMINDOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: down_interface_count
            
            	Number of interfaces in DOWN state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_count
            
            	Number of interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_interface_count
            
            	Number of interfaces in UP state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.admin_down_interface_count = None
                self.down_interface_count = None
                self.interface_count = None
                self.up_interface_count = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.admin_down_interface_count is not None:
                    return True

                if self.down_interface_count is not None:
                    return True

                if self.interface_count is not None:
                    return True

                if self.up_interface_count is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InventorySummary.InterfaceCounts']['meta_info']


        class InterfaceType(object):
            """
            List of per interface type summary information
            
            .. attribute:: interface_counts
            
            	Counts for interfaces of this type
            	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.InventorySummary.InterfaceType.InterfaceCounts>`
            
            .. attribute:: interface_type_description
            
            	Description of the interface type
            	**type**\: str
            
            .. attribute:: interface_type_name
            
            	Name of the interface type
            	**type**\: str
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_counts = Interfaces.InventorySummary.InterfaceType.InterfaceCounts()
                self.interface_counts.parent = self
                self.interface_type_description = None
                self.interface_type_name = None


            class InterfaceCounts(object):
                """
                Counts for interfaces of this type
                
                .. attribute:: admin_down_interface_count
                
                	Number of interfaces in an ADMINDOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: down_interface_count
                
                	Number of interfaces in DOWN state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_count
                
                	Number of interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_interface_count
                
                	Number of interfaces in UP state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.admin_down_interface_count = None
                    self.down_interface_count = None
                    self.interface_count = None
                    self.up_interface_count = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.admin_down_interface_count is not None:
                        return True

                    if self.down_interface_count is not None:
                        return True

                    if self.interface_count is not None:
                        return True

                    if self.up_interface_count is not None:
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.InventorySummary.InterfaceType.InterfaceCounts']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_counts is not None and self.interface_counts._has_data():
                    return True

                if self.interface_counts is not None and self.interface_counts.is_presence():
                    return True

                if self.interface_type_description is not None:
                    return True

                if self.interface_type_name is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.InventorySummary.InterfaceType']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:inventory-summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.interface_counts is not None and self.interface_counts._has_data():
                return True

            if self.interface_counts is not None and self.interface_counts.is_presence():
                return True

            if self.interface_type is not None:
                for child_ref in self.interface_type:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.InventorySummary']['meta_info']


    class NodeTypeSets(object):
        """
        Node and/or interface type specific view of
        interface summary data
        
        .. attribute:: node_type_set
        
        	Summary data for all interfaces on a particular node
        	**type**\: list of :py:class:`NodeTypeSet <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet>`
        
        

        """

        _prefix = 'pfi-im-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_type_set = YList()
            self.node_type_set.parent = self
            self.node_type_set.name = 'node_type_set'


        class NodeTypeSet(object):
            """
            Summary data for all interfaces on a particular
            node
            
            .. attribute:: interface_summary
            
            	Interface summary information
            	**type**\: :py:class:`InterfaceSummary <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary>`
            
            .. attribute:: node_name
            
            	The location to filter on
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: type_set_name
            
            	The interface type to filter on
            	**type**\: :py:class:`InterfaceTypeSet_Enum <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.InterfaceTypeSet_Enum>`
            
            

            """

            _prefix = 'pfi-im-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_summary = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary()
                self.interface_summary.parent = self
                self.node_name = None
                self.type_set_name = None


            class InterfaceSummary(object):
                """
                Interface summary information
                
                .. attribute:: interface_counts
                
                	Counts for all interfaces
                	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts>`
                
                .. attribute:: interface_type
                
                	List of per interface type summary information
                	**type**\: list of :py:class:`InterfaceType <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType>`
                
                

                """

                _prefix = 'pfi-im-cmd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts()
                    self.interface_counts.parent = self
                    self.interface_type = YList()
                    self.interface_type.parent = self
                    self.interface_type.name = 'interface_type'


                class InterfaceCounts(object):
                    """
                    Counts for all interfaces
                    
                    .. attribute:: admin_down_interface_count
                    
                    	Number of interfaces in an ADMINDOWN state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: down_interface_count
                    
                    	Number of interfaces in DOWN state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_count
                    
                    	Number of interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up_interface_count
                    
                    	Number of interfaces in UP state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.admin_down_interface_count = None
                        self.down_interface_count = None
                        self.interface_count = None
                        self.up_interface_count = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.admin_down_interface_count is not None:
                            return True

                        if self.down_interface_count is not None:
                            return True

                        if self.interface_count is not None:
                            return True

                        if self.up_interface_count is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceCounts']['meta_info']


                class InterfaceType(object):
                    """
                    List of per interface type summary information
                    
                    .. attribute:: interface_counts
                    
                    	Counts for interfaces of this type
                    	**type**\: :py:class:`InterfaceCounts <ydk.models.pfi.Cisco_IOS_XR_pfi_im_cmd_oper.Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts>`
                    
                    .. attribute:: interface_type_description
                    
                    	Description of the interface type
                    	**type**\: str
                    
                    .. attribute:: interface_type_name
                    
                    	Name of the interface type
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'pfi-im-cmd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_counts = Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts()
                        self.interface_counts.parent = self
                        self.interface_type_description = None
                        self.interface_type_name = None


                    class InterfaceCounts(object):
                        """
                        Counts for interfaces of this type
                        
                        .. attribute:: admin_down_interface_count
                        
                        	Number of interfaces in an ADMINDOWN state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: down_interface_count
                        
                        	Number of interfaces in DOWN state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_count
                        
                        	Number of interfaces
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: up_interface_count
                        
                        	Number of interfaces in UP state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'pfi-im-cmd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.admin_down_interface_count = None
                            self.down_interface_count = None
                            self.interface_count = None
                            self.up_interface_count = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type/Cisco-IOS-XR-pfi-im-cmd-oper:interface-counts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.admin_down_interface_count is not None:
                                return True

                            if self.down_interface_count is not None:
                                return True

                            if self.interface_count is not None:
                                return True

                            if self.up_interface_count is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                            return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType.InterfaceCounts']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary/Cisco-IOS-XR-pfi-im-cmd-oper:interface-type'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.interface_counts is not None and self.interface_counts._has_data():
                            return True

                        if self.interface_counts is not None and self.interface_counts.is_presence():
                            return True

                        if self.interface_type_description is not None:
                            return True

                        if self.interface_type_name is not None:
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                        return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary.InterfaceType']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set/Cisco-IOS-XR-pfi-im-cmd-oper:interface-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.interface_counts is not None and self.interface_counts._has_data():
                        return True

                    if self.interface_counts is not None and self.interface_counts.is_presence():
                        return True

                    if self.interface_type is not None:
                        for child_ref in self.interface_type:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                    return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet.InterfaceSummary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-set'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.interface_summary is not None and self.interface_summary._has_data():
                    return True

                if self.interface_summary is not None and self.interface_summary.is_presence():
                    return True

                if self.node_name is not None:
                    return True

                if self.type_set_name is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
                return meta._meta_table['Interfaces.NodeTypeSets.NodeTypeSet']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces/Cisco-IOS-XR-pfi-im-cmd-oper:node-type-sets'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.node_type_set is not None:
                for child_ref in self.node_type_set:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
            return meta._meta_table['Interfaces.NodeTypeSets']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-pfi-im-cmd-oper:interfaces'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.interface_briefs is not None and self.interface_briefs._has_data():
            return True

        if self.interface_briefs is not None and self.interface_briefs.is_presence():
            return True

        if self.interface_summary is not None and self.interface_summary._has_data():
            return True

        if self.interface_summary is not None and self.interface_summary.is_presence():
            return True

        if self.interface_xr is not None and self.interface_xr._has_data():
            return True

        if self.interface_xr is not None and self.interface_xr.is_presence():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.interfaces is not None and self.interfaces.is_presence():
            return True

        if self.inventory_summary is not None and self.inventory_summary._has_data():
            return True

        if self.inventory_summary is not None and self.inventory_summary.is_presence():
            return True

        if self.node_type_sets is not None and self.node_type_sets._has_data():
            return True

        if self.node_type_sets is not None and self.node_type_sets.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.pfi._meta import _Cisco_IOS_XR_pfi_im_cmd_oper as meta
        return meta._meta_table['Interfaces']['meta_info']


