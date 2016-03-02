""" IEEE8021_CFM_MIB 

Connectivity Fault Management module for managing IEEE 802.1ag

Unless otherwise indicated, the references in this MIB
module are to IEEE 802.1Q\-2005 as amended by IEEE 802.1ad,
IEEE 802.1ak, IEEE 802.1ag and IEEE 802.1ah.

Copyright (C) IEEE.

This version of this MIB module is part of IEEE802.1Q;
see the draft itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.lldp.LLDP_MIB import LldpChassisIdSubtype_Enum
from ydk.models.lldp.LLDP_MIB import LldpPortIdSubtype_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class Dot1agCfmCcmInterval_Enum(Enum):
    """
    Dot1agCfmCcmInterval_Enum

    Indicates the interval at which CCMs are sent by a MEP.
    The possible values are\:
    intervalInvalid(0) No CCMs are sent (disabled).
    interval300Hz(1)   CCMs are sent every 3 1/3 milliseconds
                       (300Hz).
    interval10ms(2)    CCMs are sent every 10 milliseconds.
    interval100ms(3)   CCMs are sent every 100 milliseconds.
    interval1s(4)      CCMs are sent every 1 second.
    interval10s(5)     CCMs are sent every 10 seconds.
    interval1min(6)    CCMs are sent every minute.
    interval10min(7)   CCMs are sent every 10 minutes.
    
    Note\: enumerations start at zero to match the 'CCM Interval
          field' protocol field.

    """

    INTERVALINVALID = 0

    INTERVAL300HZ = 1

    INTERVAL10MS = 2

    INTERVAL100MS = 3

    INTERVAL1S = 4

    INTERVAL10S = 5

    INTERVAL1MIN = 6

    INTERVAL10MIN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmCcmInterval_Enum']


class Dot1agCfmEgressActionFieldValue_Enum(Enum):
    """
    Dot1agCfmEgressActionFieldValue_Enum

    Possible values returned in the egress action field

    """

    EGRNOTLV = 0

    EGROK = 1

    EGRDOWN = 2

    EGRBLOCKED = 3

    EGRVID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmEgressActionFieldValue_Enum']


class Dot1agCfmFngState_Enum(Enum):
    """
    Dot1agCfmFngState_Enum

    Indicates the diferent states of the MEP Fault Notification
    Generator State Machine.
    
    fngReset(1)            No defect has been present since the
                           dot1agCfmMepFngResetTime timer
                           expired, or since the state machine
                           was last reset.
    
    fngDefect(2)           A defect is present, but not for a
                           long enough time to be reported 
                           (dot1agCfmMepFngAlarmTime).
    
    fngReportDefect(3)     A momentary state during which the
                           defect is reported by sending a
                           dot1agCfmFaultAlarm notification,
                           if that action is enabled.
    
    fngDefectReported(4)   A defect is present, and some defect
                           has been reported.
    
    fngDefectClearing(5)   No defect is present, but the
                           dot1agCfmMepFngResetTime timer has
                           not yet expired.

    """

    FNGRESET = 1

    FNGDEFECT = 2

    FNGREPORTDEFECT = 3

    FNGDEFECTREPORTED = 4

    FNGDEFECTCLEARING = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmFngState_Enum']


class Dot1agCfmHighestDefectPri_Enum(Enum):
    """
    Dot1agCfmHighestDefectPri_Enum

    An enumerated value, equal to the contents of the variable
    highestDefect (20.33.9 and Table 20\-1), indicating the
    highest\-priority defect that has been present since the MEP
    Fault Notification Generator State Machine was last in the 
    FNG\_RESET state, either\:
    
    none(0)           no defects since FNG\_RESET
    defRDICCM(1)      DefRDICCM
    defMACstatus(2)   DefMACstatus
    defRemoteCCM(3)   DefRemoteCCM
    defErrorCCM(4)    DefErrorCCM
    defXconCCM(5)     DefXconCCM
    
    The value 0 is used for no defects so that additional higher
    priority values can be added, if needed, at a later time, and
    so that these values correspond with those in
    Dot1agCfmLowestAlarmPri.

    """

    NONE = 0

    DEFRDICCM = 1

    DEFMACSTATUS = 2

    DEFREMOTECCM = 3

    DEFERRORCCM = 4

    DEFXCONCCM = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmHighestDefectPri_Enum']


class Dot1agCfmIdPermission_Enum(Enum):
    """
    Dot1agCfmIdPermission_Enum

    Indicates what, if anything, is to be included in the Sender
    ID TLV transmitted in CCMs, LBMs, LTMs, and LTRs.  The valid
    values are\:
    
    sendIdNone(1)      The Sender ID TLV is not to be sent.
    sendIdChassis(2)   The Chassis ID Length, Chassis ID
                       Subtype, and Chassis ID fields of  the
                       Sender ID TLV are to be sent.
    sendIdManage(3)    The Management Address Length and
                       Management Address of the Sender ID TLV
                       are to be sent.
    sendIdChassisManage(4) The Chassis ID Length, Chassis ID
                       Subtype, Chassis ID, Management Address
                       Length and Management Address fields are
                       all to be sent.
    sendIdDefer(5)     The contents of the Sender ID TLV are
                       determined by the corresponding
                       Maintenance Domain variable
                       (dot1agCfmMaCompIdPermission).

    """

    SENDIDNONE = 1

    SENDIDCHASSIS = 2

    SENDIDMANAGE = 3

    SENDIDCHASSISMANAGE = 4

    SENDIDDEFER = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmIdPermission_Enum']


class Dot1agCfmIngressActionFieldValue_Enum(Enum):
    """
    Dot1agCfmIngressActionFieldValue_Enum

    Possible values returned in the ingress action field.

    """

    INGNOTLV = 0

    INGOK = 1

    INGDOWN = 2

    INGBLOCKED = 3

    INGVID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmIngressActionFieldValue_Enum']


class Dot1agCfmInterfaceStatus_Enum(Enum):
    """
    Dot1agCfmInterfaceStatus_Enum

    An enumerated value from the Interface Status TLV from the 
    last CCM received from the last MEP. It indicates the status
    of the Interface within which the MEP transmitting the CCM
    is configured, or the next lower Interface in the Interface
    Stack, if the MEP is not configured within an Interface.
    
    isNoInterfaceStatusTLV(0)  Indicates either that no CCM has been
                      received or that no interface status TLV
                      was present in the last CCM received.
    
    isUp(1)               The interface is ready to pass packets.
    
    isDown(2)             The interface cannot pass packets
    
    isTesting(3)          The interface is in some test mode.
    
    isUnknown(4)          The interface status cannot be determined
                      for some reason.
    
    isDormant(5)          The interface is not in a state to pass
                      packets but is in a pending state, waiting
                      for some external event.
    
    isNotPresent(6)       Some component of the interface is missing
    
    isLowerLayerDown(7)   The interface is down due to state of the
                      lower layer interfaces
    
    NOTE\: A 0 value is used for isNoInterfaceStatusTLV, so that
          these code points can be kept consistent with new code
          points added to ifOperStatus in the IF\-MIB.

    """

    ISNOINTERFACESTATUSTLV = 0

    ISUP = 1

    ISDOWN = 2

    ISTESTING = 3

    ISUNKNOWN = 4

    ISDORMANT = 5

    ISNOTPRESENT = 6

    ISLOWERLAYERDOWN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmInterfaceStatus_Enum']


class Dot1agCfmLowestAlarmPri_Enum(Enum):
    """
    Dot1agCfmLowestAlarmPri_Enum

    An integer value specifying the lowest priority defect
    that is allowed to generate a Fault Alarm (20.9.5), either\:
    
    allDef(1)           DefRDICCM, DefMACstatus, DefRemoteCCM,
                        DefErrorCCM, and DefXconCCM;
    macRemErrXcon(2)    Only DefMACstatus, DefRemoteCCM,
                        DefErrorCCM, and DefXconCCM (default);
    remErrXcon(3)       Only DefRemoteCCM, DefErrorCCM,
                        and DefXconCCM;
    errXcon(4)          Only DefErrorCCM and DefXconCCM;
    xcon(5)             Only DefXconCCM; or
    noXcon(6)           No defects DefXcon or lower are to be
                        reported;

    """

    ALLDEF = 1

    MACREMERRXCON = 2

    REMERRXCON = 3

    ERRXCON = 4

    XCON = 5

    NOXCON = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmLowestAlarmPri_Enum']


class Dot1agCfmMaintAssocNameType_Enum(Enum):
    """
    Dot1agCfmMaintAssocNameType_Enum

    A value that represents a type (and thereby the format)
    of a Dot1agCfmMaintAssocName.  The value can be one of
    the following\:
    
    ieeeReserved(0)   Reserved for definition by IEEE 802.1
                      recommend to not use zero unless
                      absolutely needed.
    primaryVid(1)     Primary VLAN ID.
                      12 bits represented in a 2\-octet integer\:
                      \- 4 least significant bits of the first
                        byte contains the 4 most significant 
                        bits of the 12 bits primary VID
                      \- second byte contains the 8 least
                        significant bits of the primary VID
    
                             0 1 2 3 4 5 6 7 8
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|0 0 0 0\| (MSB) \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|  VID   LSB    \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
    
    charString(2)     RFC2579 DisplayString, except that the
                      character codes 0\-31 (decimal) are not
                      used. (1..45) octets
    unsignedInt16 (3) 2\-octet integer/big endian
    rfc2865VpnId(4)   RFC 2685 VPN ID
                      3 octet VPN authority Organizationally
                      Unique Identifier followed by 4 octet VPN
                      index identifying VPN according to the OUI\:
    
                             0 1 2 3 4 5 6 7 8
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \| VPN OUI (MSB) \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|   VPN OUI     \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \| VPN OUI (LSB) \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|VPN Index (MSB)\|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|  VPN Index    \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|  VPN Index    \|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
                             \|VPN Index (LSB)\|
                             +\-+\-+\-+\-+\-+\-+\-+\-+
    
    ieeeReserved(xx)  Reserved for definition by IEEE 802.1
                      xx values can be [5..31] and [64..255]
    ituReserved(xx)   Reserved for definition by  ITU\-T Y.1731
                      xx values range from [32..63]
    
    To support future extensions, the Dot1agCfmMaintAssocNameType
    textual convention SHOULD NOT be sub\-typed in object type
    definitions.  It MAY be sub\-typed in compliance statements in
    order to require only a subset of these address types for a
    compliant implementation.
    
    Implementations MUST ensure that Dot1agCfmMaintAssocNameType
    objects and any dependent objects (e.g.,
    Dot1agCfmMaintAssocName objects) are consistent.  An
    inconsistentValue error MUST be generated if an attempt to
    change an Dot1agCfmMaintAssocNameType object would, for
    example, lead to an undefined Dot1agCfmMaintAssocName value.
    In particular,
    Dot1agCfmMaintAssocNameType/Dot1agCfmMaintAssocName pairs
    MUST be changed together if the nameType changes.
    
    The Maintenance Domain name and Maintenance Association name,
    when put together into the CCM PDU, MUST total 48 octets or
    less.  If the Dot1agCfmMaintDomainNameType object contains
    none(1), then the Dot1agCfmMaintAssocName object MUST be
    45 octets or less in length.  Otherwise, the length of
    the Dot1agCfmMaintDomainName object plus the length of the
    Dot1agCfmMaintAssocName object, added together, MUST total
    less than or equal to 44 octets.

    """

    PRIMARYVID = 1

    CHARSTRING = 2

    UNSIGNEDINT16 = 3

    RFC2865VPNID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmMaintAssocNameType_Enum']


class Dot1agCfmMaintDomainNameType_Enum(Enum):
    """
    Dot1agCfmMaintDomainNameType_Enum

    A value that represents a type (and thereby the format)
    of a Dot1agCfmMaintDomainName.  The value can be one of
    the following\:
    
    
    ieeeReserved(0)   Reserved for definition by IEEE 802.1
                      recommend to not use zero unless
                      absolutely needed.
    none(1)           No format specified, usually because
                      there is not (yet) a Maintenance
                      Domain Name. In this case, a zero
                      length OCTET STRING for the Domain
                      Name field is acceptable.
    dnsLikeName(2)    Domain Name like string, globally unique
                      text string derived from a DNS name.
    macAddrAndUint(3) MAC address + 2\-octet (unsigned) integer.
    charString(4)     RFC2579 DisplayString, except that the
                      character codes 0\-31 (decimal) are not
                      used.
    ieeeReserved(xx)  Reserved for definition by IEEE 802.1
                      xx values can be [5..31] and [64..255]
    ituReserved(xx)   Reserved for definition by  ITU\-T Y.1731
                      xx values range from [32..63]
    
    To support future extensions, the Dot1agCfmMaintDomainNameType
    textual convention SHOULD NOT be sub\-typed in object type
    definitions.  It MAY be sub\-typed in compliance statements in
    order to require only a subset of these address types for a
    compliant implementation.
    
    Implementations MUST ensure that Dot1agCfmMaintDomainNameType
    objects and any dependent objects (e.g.,
    Dot1agCfmMaintDomainName objects) are consistent.  An
    inconsistentValue error MUST be generated if an attempt to
    change an Dot1agCfmMaintDomainNameType object would, for
    example, lead to an undefined Dot1agCfmMaintDomainName value.
    In particular,
    Dot1agCfmMaintDomainNameType/Dot1agCfmMaintDomainName pairs
    MUST be changed together if the nameType changes.

    """

    NONE = 1

    DNSLIKENAME = 2

    MACADDRESSANDUINT = 3

    CHARSTRING = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmMaintDomainNameType_Enum']


class Dot1agCfmMhfCreation_Enum(Enum):
    """
    Dot1agCfmMhfCreation_Enum

    Indicates if the Management Entity can create MHFs.
    The valid values are\:
    
    defMHFnone(1)      No MHFs can be created for this VID.
    defMHFdefault(2)   MHFs can be created on this VID on any
                       Bridge port through which this VID can
                       pass.
    defMHFexplicit(3)  MHFs can be created for this VID only on
                       Bridge ports through which this VID can
                       pass, and only if a MEP is created at some
                       lower MD Level.
    defMHFdefer(4)     The creation of MHFs is determined by the
                       corresponding Maintenance Domain variable
                       (dot1agCfmMaCompMhfCreation).

    """

    DEFMHFNONE = 1

    DEFMHFDEFAULT = 2

    DEFMHFEXPLICIT = 3

    DEFMHFDEFER = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmMhfCreation_Enum']


class Dot1agCfmMpDirection_Enum(Enum):
    """
    Dot1agCfmMpDirection_Enum

    Indicates the direction in which the Maintenance
    association (MEP or MIP) faces on the bridge port\:
    
    down(1)    Sends Continuity Check Messages away from the
               MAC Relay Entity.
    up(2)      Sends Continuity Check Messages towards the
               MAC Relay Entity.

    """

    DOWN = 1

    UP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmMpDirection_Enum']


class Dot1agCfmPortStatus_Enum(Enum):
    """
    Dot1agCfmPortStatus_Enum

    An enumerated value from he Port Status TLV from the last CCM
    received from the last MEP. It indicates the ability of the
    Bridge Port on which the transmitting MEP resides to pass
    ordinary data, regardless of the status of the MAC
    (Table 21\-10).
    
    psNoPortStateTLV(0) Indicates either that no CCM has been
                        received or that no port status TLV was
                        present in the last CCM received.
    
    psBlocked(1)        Ordinary data cannot pass freely through
                        the port on which the remote MEP resides.
                        Value of enableRmepDefect is equal to
                        false.
    
    psUp(2)\:            Ordinary data can pass freely through
                        the port on which the remote MEP resides.
                        Value of enableRmepDefect is equal to
                        true.
    
    NOTE\: A 0 value is used for psNoPortStateTLV, so that
          additional code points can be added in a manner
          consistent with the Dot1agCfmInterfaceStatus textual
          convention.

    """

    PSNOPORTSTATETLV = 0

    PSBLOCKED = 1

    PSUP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmPortStatus_Enum']


class Dot1agCfmRelayActionFieldValue_Enum(Enum):
    """
    Dot1agCfmRelayActionFieldValue_Enum

    Possible values the Relay action field can take.

    """

    RLYHIT = 1

    RLYFDB = 2

    RLYMPDB = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmRelayActionFieldValue_Enum']


class Dot1agCfmRemoteMepState_Enum(Enum):
    """
    Dot1agCfmRemoteMepState_Enum

    Operational state of the remote MEP state machine.  This
    state machine monitors the reception of valid CCMs from a
    remote MEP with a specific MEPID.  It uses a timer that
    expires in 3.5 times the length of time indicated by the
    dot1agCfmMaNetCcmInterval object.
    
    rMepIdle(1)            Momentary state during reset.
    
    rMepStart(2)           The timer has not expired since the
                           state machine was reset, and no valid
                           CCM has yet been received.
    
    rMepFailed(3)          The timer has expired, both since the
                           state machine was reset, and since a
                           valid CCM was received.
    
    rMepOk(4)              The timer has not expired since a
                           valid CCM was received.

    """

    RMEPIDLE = 1

    RMEPSTART = 2

    RMEPFAILED = 3

    RMEPOK = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['Dot1agCfmRemoteMepState_Enum']


class Dot1agCfmConfigErrors_Bits(FixedBitsDict):
    """
    Dot1agCfmConfigErrors_Bits

    While making the MIP creation evaluation described in 802.1ag
    clause 22.2.3, the management entity can encounter errors in
    the configuration. These are possible errors that can be
    encountered\:
    
    CFMleak(0)   MA x is associated with a specific VID list,
                 one or more of the VIDs in MA x can pass through
                 the Bridge Port, no Down MEP is configured on
                 any Bridge Port for MA x, and some other MA y,
                 at a higher MD Level than MA x, and associated
                 with at least one of the VID(s) also in MA x,
                 does have a MEP configured on the Bridge Port.
    
    conflictingVids(1)  MA x is associated with a specific VID
                 list, an Up MEP is configured on MA x on the
                 Bridge Port, and some other MA y, associated
                 with at least one of the VID(s) also in MA x,
                 also has an Up MEP configured on some Bridge
                 Port.
    
    ExcessiveLevels(2)  The number of different MD Levels at
                 which MIPs are to be created on this port
                 exceeds the Bridge's capabilities (see
                 subclause 22.3).
    
    OverlappedLevels(3) A MEP is created for one VID at one MD
                 Level, but a MEP is configured on another
                 VID at that MD Level or higher, exceeding
                 the Bridge's capabilities.
    Keys are:- conflictingVids , cfmLeak , excessiveLevels , overlappedLevels

    """

    def __init__(self):
        self._dictionary = { 
            'conflictingVids':False,
            'cfmLeak':False,
            'excessiveLevels':False,
            'overlappedLevels':False,
        }
        self._pos_map = { 
            'conflictingVids':1,
            'cfmLeak':0,
            'excessiveLevels':2,
            'overlappedLevels':3,
        }

class Dot1agCfmMepDefects_Bits(FixedBitsDict):
    """
    Dot1agCfmMepDefects_Bits

    A MEP can detect and report a number of defects, and multiple
    defects can be present at the same time. These defects are\:
    
    bDefRDICCM(0) A remote MEP is reported the RDI bit in its
                 last CCM.
    bDefMACstatus(1) Either some remote MEP is reporting its
                 Interface Status TLV as not isUp, or all remote
                 MEPs are reporting a Port Status TLV that
                 contains some value other than psUp.
    bDefRemoteCCM(2) The MEP is not receiving valid CCMs from at
                 least one of the remote MEPs.
    bDefErrorCCM(3) The MEP has received at least one invalid CCM
                 whose CCM Interval has not yet timed out.
    bDefXconCCM(4) The MEP has received at least one CCM from
                 either another MAID or a lower MD Level whose
                 CCM Interval has not yet timed out.
    Keys are:- bDefRemoteCCM , bDefMACstatus , bDefRDICCM , bDefXconCCM , bDefErrorCCM

    """

    def __init__(self):
        self._dictionary = { 
            'bDefRemoteCCM':False,
            'bDefMACstatus':False,
            'bDefRDICCM':False,
            'bDefXconCCM':False,
            'bDefErrorCCM':False,
        }
        self._pos_map = { 
            'bDefRemoteCCM':2,
            'bDefMACstatus':1,
            'bDefRDICCM':0,
            'bDefXconCCM':4,
            'bDefErrorCCM':3,
        }


class IEEE8021CFMMIB(object):
    """
    
    
    .. attribute:: dot1agcfmconfigerrorlisttable
    
    	The CFM Configuration Error List table provides a list of Interfaces and VIDs that are incorrectly configured. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
    	**type**\: :py:class:`Dot1agCfmConfigErrorListTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable>`
    
    .. attribute:: dot1agcfmdefaultmd
    
    	
    	**type**\: :py:class:`Dot1agCfmDefaultMd <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmDefaultMd>`
    
    .. attribute:: dot1agcfmdefaultmdtable
    
    	For each bridge component, the Default MD Level Managed Object controls MHF creation for VIDs that are not attached to a specific Maintenance Association Managed Object, and Sender ID TLV transmission by those MHFs.  For each Bridge Port, and for each VLAN ID whose data can pass through that Bridge Port, an entry in this table is used by the algorithm in subclause 22.2.3 only if there is no entry in the Maintenance Association table defining an MA for the same VLAN ID and MD Level as this table's entry, and on which MA an Up MEP is defined.  If there exists such an MA, that MA's objects are used by the algorithm in subclause 22.2.3 in place of this table entry's objects.  The agent maintains the value of dot1agCfmDefaultMdStatus to indicate whether this entry is overridden by an MA.  When first initialized, the agent creates this table automatically with entries for all VLAN IDs, with the default values specified for each object.  After this initialization, the writable objects in this table need to be persistent upon reboot or restart of a device. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
    	**type**\: :py:class:`Dot1agCfmDefaultMdTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmDefaultMdTable>`
    
    .. attribute:: dot1agcfmltrtable
    
    	This table extends the MEP table and contains a list of Linktrace replies received by a specific MEP in response to a linktrace message.  SNMP SMI does not allow to state in a MIB that an object in a table is an array.  The solution is to take the index (or indices) of the first table and add one or more indices
    	**type**\: :py:class:`Dot1agCfmLtrTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmLtrTable>`
    
    .. attribute:: dot1agcfmmacomptable
    
    	The Maintenance Association table.  Each row in the table represents an MA.  An MA is a set of MEPs, each configured with a single service instance.  This is the part of the complete MA table that is variable across the Bridges in a Maintenance Domain, or across the components of a single Bridge.  That part of the MA table that is constant across the Bridges and their components in a Maintenance Domain is contained in the dot1agCfmMaNetTable.  This table uses three indices, first index is the Dot1agCfmPbbComponentIdentifier that identifies the component within the Bridge for which the information in the dot1agCfmMaCompEntry applies.  The second is the index of the Maintenance Domain table.  The third index is the same as the index of the dot1agCfmMaNetEntry for the same MA.  The writable objects in this table need to be persistent upon reboot or restart of a device.  \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
    	**type**\: :py:class:`Dot1agCfmMaCompTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaCompTable>`
    
    .. attribute:: dot1agcfmmameplisttable
    
    	List of MEPIDs that belong to this MA.  Clause 12.14.6.1.3 specifies that a list of MEPIDs in all bridges in that MA, but since SNMP SMI does not allow to state in a MIB that an object in a table is an array, the  information has to be stored in another table with two indices, being the first index, the index of the table that  contains the list or array.  For all bridges in which the same MAID {dot1agCfmMdFormat, dot1agCfmMdName, dot1agCfmMaNetFormat, and dot1agCfmMaNetName} is configured, the same set of dot1agCfmMaMepListIdentifiers MUST be configured in the bridges' dot1agCfmMaMepListTables. This allows each MEP to determine whether or not it is receiving CCMs from all of the other MEPs in the MA.  For example, if one were creating a new MA whose MAID were {charString, 'Dom1', charString, 'MA1'}, that had 2 MEPs, whose MEPIDs were 1 and 3, one could, in Bridge A\:  1. Get a new MD index d from dot1agCfmMdTableNextIndex.  2. Create the Maintenance Domain {charString, 'Dom1'}.  3. Get a new MA index a from dot1agCfmMdMaNextIndex [d].  4. Create the Maintenance Association {charString, 'MA1'}.  5. Create a new dot1agCfmMaMepListEntry for each of the MEPs     in the MA\: [d, a, 1] and [d, a, 3].  6. Create one of the new MEPs, say [d, a, 1]. Then, in Bridge B\:  7. Do all of these steps 1\-6, except for using the other MEPID     for the new MEP in Step 6, in this example, MEPID 3. Note that, when creating the MA, MEP List Table, and MEP entries in the second bridge, the indices 'd' and 'a' identifying the MAID {charString, 'Dom1', charString, 'MA1'} may have different values than those in the first Bridge
    	**type**\: :py:class:`Dot1agCfmMaMepListTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaMepListTable>`
    
    .. attribute:: dot1agcfmmanettable
    
    	The Maintenance Association table.  Each row in the table represents an MA.  An MA is a set of MEPs, each configured with a single service instance.  This is the part of the complete MA table that is constant across all Bridges in a Maintenance Domain, and across all components of a single Bridge.  That part of the MA table that can vary from Bridge component to Bridge component is contained in the dot1agCfmMaCompTable.  Creation of a Service Instance establishes a connectionless association among the selected DSAPs.  Configuring a Maintenance association End Point (MEP) at each of the DSAPs creates a Maintenance Association (MA) to monitor that connectionless connectivity.  The MA is identified by a Short MA Name that is unique within the Maintenance Domain and chosen to facilitate easy identification of the Service Instance.  Together, the Maintenance Domain Name and the Short MA Name form the Maintenance Association Identifier (MAID) that is carried in CFM Messages to identify incorrect connectivity among Service Instances.  A small integer, the Maintenance association End Point Identifier (MEPID), identifies each MEP among those configured on a single MA (802.1ag clauses 3.19 and 18.2).  This table uses two indices, first index is the index of the Maintenance Domain table.  The second index is the same as the index of the dot1agCfmMaCompEntry for the same MA.  The writable objects in this table need to be persistent upon reboot or restart of a device
    	**type**\: :py:class:`Dot1agCfmMaNetTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaNetTable>`
    
    .. attribute:: dot1agcfmmd
    
    	
    	**type**\: :py:class:`Dot1agCfmMd <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMd>`
    
    .. attribute:: dot1agcfmmdtable
    
    	The Maintenance Domain table. Each row in the table represents a different Maintenance Domain.  A Maintenance Domain is described in 802.1ag (3.22) as the network or the part of the network for which faults in connectivity are to be managed. The boundary of a Maintenance Domain is defined by a set of DSAPs, each of which can become a point of connectivity to a service instance
    	**type**\: :py:class:`Dot1agCfmMdTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMdTable>`
    
    .. attribute:: dot1agcfmmepdbtable
    
    	The MEP Database. A database, maintained by every MEP, that maintains received information about other MEPs in the Maintenance Domain.  The SMI does not allow to state in a MIB that an object in a table is an array. The solution is to take the index (or indices) of the first table and add one or more indices
    	**type**\: :py:class:`Dot1agCfmMepDbTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMepDbTable>`
    
    .. attribute:: dot1agcfmmeptable
    
    	The Maintenance Association End Point (MEP) table.  Each row in the table represents a different MEP.  A MEP is an actively managed CFM entity, associated with a specific DSAP of a Service Instance, which can generate and receive CFM PDUs and track any responses.  It is an end point of a single Maintenance Association, and is an endpoint of a separate Maintenance Entity for each of the other MEPs in the same Maintenance Association (802.1ag clause 3.19).  This table uses three indices. The first two indices are the indices of the Maintenance Domain and MA tables, the reason being that a MEP is always related to an MA and Maintenance Domain.  The MEP table also stores all the managed objects for sending LBM and LTM.  \*LBM Managed objects  LBM Managed objects in the MEP table enables the management entity to initiate transmission of Loopback messages.  It will signal the MEP that it SHOULD transmit some number of Loopback messages and detect the detection (or lack thereof) of the corresponding Loopback messages.  Steps to use entries in this table\:  1) Wait for dot1agCfmMepTransmitLbmStatus value to be    false.  To do this do this sequence\:    a. an SNMP GET for both SnmpSetSerialNo and       dot1agCfmMepTransmitLbmStatus objects (in same SNMP       PDU).    b. Check if value for dot1agCfmMepTransmitLbmStatus is false.       \- if not, wait x seconds, go to step a above.       \- if yes, save the value of SnmpSetSerialNo and go         to step 2) below 2) Change dot1agCfmMepTransmitLbmStatus value from false to    true to ensure no other management entity will use    the service. In order to not disturb a possible other NMS    do this by sending an SNMP SET for both SnmpSetSerialNo    and dot1agCfmMepTransmitLbmStatus objects (in same SNMP    PDU,  and make sure SNmpSetSerialNo is the first varBind).    For the SnmpSetSerialNo varBind, use the value that you    obtained in step 1)a.. This ensures that two cooperating    NMSes will not step on each others toes.    Setting this MIB object does not set the corresponding    LBIactive state machine variable. 3) Setup the different data to be sent (number of messages,    optional TLVs,...), except do not set    dot1agCfmMepTransmitLbmMessages. 4) Record the current values of dot1agCfmMepLbrIn,    dot1agCfmMepLbrInOutOfOrder, and dot1agCfmMepLbrBadMsdu. 6) Set dot1agCfmMepTransmitLbmMessages to a non\-zero value to    initiate transmission of Loopback messages.    The dot1agCfmMepTransmitLbmMessages indicates the    number of LBMs to be sent and is not decremented as    loopbacks are actually sent. dot1agCfmMepTransmitLbmMessages    is not equivalent to the LBMsToSend state machine variable. 7) Check the value of dot1agCfmMepTransmitLbmResultOK to    find out if the operation was successfully initiated or    not. 8) Monitor the value of dot1agCfmMepTransmitLbmStatus.    When it is reset to false, the last LBM has been transmitted.    Wait an additional 5 seconds to ensure that all LBRs have    been returned. 9) Compare dot1agCfmMepLbrIn, dot1agCfmMepLbrInOutOfOrder,    and dot1agCfmMepLbrBadMsdu to their old values from step    4, above, to get the results of the test.  \*LTM Managed objects The LTM Managed objects in the MEP table are used in a manner similar to that described for LBM transmission, above.  Upon successfully initiating the transmission, the variables dot1agCfmMepTransmitLtmSeqNumber and dot1agCfmMepTransmitLtmEgressIdentifier return the information required to recover the results of the LTM from the dot1agCfmLtrTable
    	**type**\: :py:class:`Dot1agCfmMepTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMepTable>`
    
    .. attribute:: dot1agcfmstacktable
    
    	There is one CFM Stack table per bridge. It permits the retrieval of information about the Maintenance Points configured on any given interface. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
    	**type**\: :py:class:`Dot1agCfmStackTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmStackTable>`
    
    .. attribute:: dot1agcfmvlantable
    
    	This table defines the association of VIDs into VLANs.  There is an entry in this table, for each component of the bridge, for each VID that is\:     a) a VID belonging to a VLAN associated with more than        one VID; and     b) not the Primary VLAN of that VID. The entry in this table contains the Primary VID of the VLAN.  By default, this table is empty, meaning that every VID is the Primary VID of a single\-VID VLAN.  VLANs that are associated with only one VID SHOULD NOT have an entry in this table.  The writable objects in this table need to be persistent upon reboot or restart of a device. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
    	**type**\: :py:class:`Dot1agCfmVlanTable <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmVlanTable>`
    
    

    """

    _prefix = 'ieee8021-cfm'
    _revision = '2008-10-15'

    def __init__(self):
        self.dot1agcfmconfigerrorlisttable = IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable()
        self.dot1agcfmconfigerrorlisttable.parent = self
        self.dot1agcfmdefaultmd = IEEE8021CFMMIB.Dot1agCfmDefaultMd()
        self.dot1agcfmdefaultmd.parent = self
        self.dot1agcfmdefaultmdtable = IEEE8021CFMMIB.Dot1agCfmDefaultMdTable()
        self.dot1agcfmdefaultmdtable.parent = self
        self.dot1agcfmltrtable = IEEE8021CFMMIB.Dot1agCfmLtrTable()
        self.dot1agcfmltrtable.parent = self
        self.dot1agcfmmacomptable = IEEE8021CFMMIB.Dot1agCfmMaCompTable()
        self.dot1agcfmmacomptable.parent = self
        self.dot1agcfmmameplisttable = IEEE8021CFMMIB.Dot1agCfmMaMepListTable()
        self.dot1agcfmmameplisttable.parent = self
        self.dot1agcfmmanettable = IEEE8021CFMMIB.Dot1agCfmMaNetTable()
        self.dot1agcfmmanettable.parent = self
        self.dot1agcfmmd = IEEE8021CFMMIB.Dot1agCfmMd()
        self.dot1agcfmmd.parent = self
        self.dot1agcfmmdtable = IEEE8021CFMMIB.Dot1agCfmMdTable()
        self.dot1agcfmmdtable.parent = self
        self.dot1agcfmmepdbtable = IEEE8021CFMMIB.Dot1agCfmMepDbTable()
        self.dot1agcfmmepdbtable.parent = self
        self.dot1agcfmmeptable = IEEE8021CFMMIB.Dot1agCfmMepTable()
        self.dot1agcfmmeptable.parent = self
        self.dot1agcfmstacktable = IEEE8021CFMMIB.Dot1agCfmStackTable()
        self.dot1agcfmstacktable.parent = self
        self.dot1agcfmvlantable = IEEE8021CFMMIB.Dot1agCfmVlanTable()
        self.dot1agcfmvlantable.parent = self


    class Dot1agCfmConfigErrorListTable(object):
        """
        The CFM Configuration Error List table provides a list of
        Interfaces and VIDs that are incorrectly configured.
        \*\*NOTE\: this object is deprecated due to re\-indexing of the 
        	table.
        
        .. attribute:: dot1agcfmconfigerrorlistentry
        
        	The Config Error List Table  entry \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: list of :py:class:`Dot1agCfmConfigErrorListEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmconfigerrorlistentry = YList()
            self.dot1agcfmconfigerrorlistentry.parent = self
            self.dot1agcfmconfigerrorlistentry.name = 'dot1agcfmconfigerrorlistentry'


        class Dot1agCfmConfigErrorListEntry(object):
            """
            The Config Error List Table  entry
            \*\*NOTE\: this object is deprecated due to re\-indexing of the 
            	table.
            
            .. attribute:: dot1agcfmconfigerrorlistifindex
            
            	This object is the IfIndex of the interface.  Upon a restart of the system, the system SHALL, if necessary, change the value of this variable so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart.  If no such entry exists, then the system SHALL delete any entries in dot1agCfmConfigErrorListTable indexed by that InterfaceIndex value. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1agcfmconfigerrorlistvid
            
            	The VLAN ID of the VLAN with interfaces in error. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: dot1agcfmconfigerrorlisterrortype
            
            	A vector of Boolean error conditions from 22.2.4, any of which may be true\:  0) CFMleak; 1) ConflictingVids; 2) ExcessiveLevels; 3) OverlappedLevels. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmConfigErrors_Bits <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmConfigErrors_Bits>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmconfigerrorlistifindex = None
                self.dot1agcfmconfigerrorlistvid = None
                self.dot1agcfmconfigerrorlisterrortype = Dot1agCfmConfigErrors_Bits()

            @property
            def _common_path(self):
                if self.dot1agcfmconfigerrorlistifindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmconfigerrorlistifindex is None')
                if self.dot1agcfmconfigerrorlistvid is None:
                    raise YPYDataValidationError('Key property dot1agcfmconfigerrorlistvid is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmConfigErrorListTable/IEEE8021-CFM-MIB:dot1agCfmConfigErrorListEntry[IEEE8021-CFM-MIB:dot1agCfmConfigErrorListIfIndex = ' + str(self.dot1agcfmconfigerrorlistifindex) + '][IEEE8021-CFM-MIB:dot1agCfmConfigErrorListVid = ' + str(self.dot1agcfmconfigerrorlistvid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmconfigerrorlistifindex is not None:
                    return True

                if self.dot1agcfmconfigerrorlistvid is not None:
                    return True

                if self.dot1agcfmconfigerrorlisterrortype is not None:
                    if self.dot1agcfmconfigerrorlisterrortype._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable.Dot1agCfmConfigErrorListEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmConfigErrorListTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmconfigerrorlistentry is not None:
                for child_ref in self.dot1agcfmconfigerrorlistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmConfigErrorListTable']['meta_info']


    class Dot1agCfmDefaultMd(object):
        """
        
        
        .. attribute:: dot1agcfmdefaultmddefidpermission
        
        	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MHFs created by the Default Maintenance Domain, for each dot1agCfmDefaultMdEntry whose dot1agCfmDefaultMdIdPermission object contains the value sendIdDefer.  Since, in this variable, there is no encompassing Maintenance Domain, the value sendIdDefer is not allowed.  After this initialization, this object needs to be persistent upon reboot or restart of a device
        	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
        
        .. attribute:: dot1agcfmdefaultmddeflevel
        
        	A value indicating the MD Level at which MHFs are to be created, and Sender ID TLV transmission by those MHFs is to be controlled, for each dot1agCfmDefaultMdEntry whose dot1agCfmDefaultMdLevel object contains the value \-1.  After this initialization, this object needs to be persistent upon reboot or restart of a device. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: int
        
        	**range:** 0..7
        
        .. attribute:: dot1agcfmdefaultmddefmhfcreation
        
        	A value indicating if the Management entity can create MHFs (MIP Half Function) for the VID, for each dot1agCfmDefaultMdEntry whose dot1agCfmDefaultMdMhfCreation object contains the value defMHFdefer.  Since, in this variable, there is no encompassing Maintenance Domain, the value defMHFdefer is not allowed.  After this initialization, this object needs to be persistent upon reboot or restart of a device
        	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmdefaultmddefidpermission = None
            self.dot1agcfmdefaultmddeflevel = None
            self.dot1agcfmdefaultmddefmhfcreation = None

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmDefaultMd'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmdefaultmddefidpermission is not None:
                return True

            if self.dot1agcfmdefaultmddeflevel is not None:
                return True

            if self.dot1agcfmdefaultmddefmhfcreation is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMd']['meta_info']


    class Dot1agCfmDefaultMdTable(object):
        """
        For each bridge component, the Default MD Level Managed Object
        controls MHF creation for VIDs that are not attached to a
        specific Maintenance Association Managed Object, and Sender ID
        TLV transmission by those MHFs.
        
        For each Bridge Port, and for each VLAN ID whose data can
        pass through that Bridge Port, an entry in this table is
        used by the algorithm in subclause 22.2.3 only if there is no
        entry in the Maintenance Association table defining an MA
        for the same VLAN ID and MD Level as this table's entry, and
        on which MA an Up MEP is defined.  If there exists such an
        MA, that MA's objects are used by the algorithm in
        subclause 22.2.3 in place of this table entry's objects.  The
        agent maintains the value of dot1agCfmDefaultMdStatus to
        indicate whether this entry is overridden by an MA.
        
        When first initialized, the agent creates this table
        automatically with entries for all VLAN IDs,
        with the default values specified for each object.
        
        After this initialization, the writable objects in this
        table need to be persistent upon reboot or restart of a
        device.
        \*\*NOTE\: this object is deprecated due to re\-indexing of the 
        	table.
        
        .. attribute:: dot1agcfmdefaultmdentry
        
        	The Default MD Level table entry. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: list of :py:class:`Dot1agCfmDefaultMdEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmdefaultmdentry = YList()
            self.dot1agcfmdefaultmdentry.parent = self
            self.dot1agcfmdefaultmdentry.name = 'dot1agcfmdefaultmdentry'


        class Dot1agCfmDefaultMdEntry(object):
            """
            The Default MD Level table entry.
            \*\*NOTE\: this object is deprecated due to re\-indexing of the 
            	table.
            
            .. attribute:: dot1agcfmdefaultmdcomponentid
            
            	The bridge component within the system to which the information in this dot1agCfmDefaultMdEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmdefaultmdprimaryvid
            
            	The Primary VID of the VLAN to which this entry's objects apply. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: dot1agcfmdefaultmdidpermission
            
            	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MHFs created by the Default Maintenance Domain.  If this object has the value sendIdDefer, Sender ID TLV transmission for this VLAN is controlled by dot1agCfmDefaultMdDefIdPermission.  The value of this variable is meaningless if the values of dot1agCfmDefaultMdStatus is false. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
            
            .. attribute:: dot1agcfmdefaultmdlevel
            
            	A value indicating the MD Level at which MHFs are to be created, and Sender ID TLV transmission by those MHFs is to be controlled, for the VLAN to which this entry's objects apply.  If this object has the value \-1, the MD Level for MHF creation for this VLAN is controlled by dot1agCfmDefaultMdDefLevel. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** \-1..7
            
            .. attribute:: dot1agcfmdefaultmdmhfcreation
            
            	A value indicating if the Management entity can create MHFs (MIP Half Function) for this VID at this MD Level.  If this object has the value defMHFdefer, MHF creation for this VLAN is controlled by dot1agCfmDefaultMdDefMhfCreation.  The value of this variable is meaningless if the values of dot1agCfmDefaultMdStatus is false. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
            
            .. attribute:: dot1agcfmdefaultmdstatus
            
            	State of this Default MD Level table entry.  True if there is no entry in the Maintenance Association table defining an MA for the same VLAN ID and MD Level as this table's entry, and on which MA an Up MEP is defined, else false. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: bool
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmdefaultmdcomponentid = None
                self.dot1agcfmdefaultmdprimaryvid = None
                self.dot1agcfmdefaultmdidpermission = None
                self.dot1agcfmdefaultmdlevel = None
                self.dot1agcfmdefaultmdmhfcreation = None
                self.dot1agcfmdefaultmdstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmdefaultmdcomponentid is None:
                    raise YPYDataValidationError('Key property dot1agcfmdefaultmdcomponentid is None')
                if self.dot1agcfmdefaultmdprimaryvid is None:
                    raise YPYDataValidationError('Key property dot1agcfmdefaultmdprimaryvid is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmDefaultMdTable/IEEE8021-CFM-MIB:dot1agCfmDefaultMdEntry[IEEE8021-CFM-MIB:dot1agCfmDefaultMdComponentId = ' + str(self.dot1agcfmdefaultmdcomponentid) + '][IEEE8021-CFM-MIB:dot1agCfmDefaultMdPrimaryVid = ' + str(self.dot1agcfmdefaultmdprimaryvid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmdefaultmdcomponentid is not None:
                    return True

                if self.dot1agcfmdefaultmdprimaryvid is not None:
                    return True

                if self.dot1agcfmdefaultmdidpermission is not None:
                    return True

                if self.dot1agcfmdefaultmdlevel is not None:
                    return True

                if self.dot1agcfmdefaultmdmhfcreation is not None:
                    return True

                if self.dot1agcfmdefaultmdstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMdTable.Dot1agCfmDefaultMdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmDefaultMdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmdefaultmdentry is not None:
                for child_ref in self.dot1agcfmdefaultmdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmDefaultMdTable']['meta_info']


    class Dot1agCfmLtrTable(object):
        """
        This table extends the MEP table and contains a list of
        Linktrace replies received by a specific MEP in response to
        a linktrace message.
        
        SNMP SMI does not allow to state in a MIB that an object in
        a table is an array.  The solution is to take the index (or
        indices) of the first table and add one or more indices.
        
        .. attribute:: dot1agcfmltrentry
        
        	The Linktrace Reply table entry
        	**type**\: list of :py:class:`Dot1agCfmLtrEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmltrentry = YList()
            self.dot1agcfmltrentry.parent = self
            self.dot1agcfmltrentry.name = 'dot1agcfmltrentry'


        class Dot1agCfmLtrEntry(object):
            """
            The Linktrace Reply table entry.
            
            .. attribute:: dot1agcfmltrreceiveorder
            
            	An index to distinguish among multiple LTRs with the same LTR Transaction Identifier field value.  dot1agCfmLtrReceiveOrder are assigned sequentially from 1, in the order that the Linktrace Initiator received the LTRs
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmltrseqnumber
            
            	Transaction identifier/Sequence number returned by a previous transmit linktrace message command, indicating which LTM's response is going to be returned
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmepidentifier
            
            	
            	**type**\: int
            
            	**range:** 1..8191
            
            .. attribute:: dot1agcfmltrchassisid
            
            	The Chassis ID returned in the Sender ID TLV of the LTR, if any. The format of this object is determined by the value of the dot1agCfmLtrChassisIdSubtype object
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: dot1agcfmltrchassisidsubtype
            
            	This object specifies the format of the Chassis ID returned in the Sender ID TLV of the LTR, if any.  This value is meaningless if the dot1agCfmLtrChassisId has a length of 0
            	**type**\: :py:class:`LldpChassisIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpChassisIdSubtype_Enum>`
            
            .. attribute:: dot1agcfmltregress
            
            	The value returned in the Egress Action Field of the LTM. The value egrNoTlv(0) indicates that no Reply Egress TLV was returned in the LTM
            	**type**\: :py:class:`Dot1agCfmEgressActionFieldValue_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmEgressActionFieldValue_Enum>`
            
            .. attribute:: dot1agcfmltregressmac
            
            	MAC address returned in the egress MAC address field. If the dot1agCfmLtrEgress object contains the value egrNoTlv(0), then the contents of this object are meaningless
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmltregressportid
            
            	Egress Port ID. The format of this object is determined by the value of the dot1agCfmLtrEgressPortIdSubtype object. If the dot1agCfmLtrEgress object contains the value egrNoTlv(0), then the contents of this object are meaningless
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: dot1agcfmltregressportidsubtype
            
            	Format of the egress Port ID. If the dot1agCfmLtrEgress object contains the value egrNoTlv(0), then the contents of this object are meaningless
            	**type**\: :py:class:`LldpPortIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpPortIdSubtype_Enum>`
            
            .. attribute:: dot1agcfmltrforwarded
            
            	Indicates if a LTM was forwarded by the responding MP, as returned in the 'FwdYes' flag of the flags field
            	**type**\: bool
            
            .. attribute:: dot1agcfmltringress
            
            	The value returned in the Ingress Action Field of the LTM. The value ingNoTlv(0) indicates that no Reply Ingress TLV was returned in the LTM
            	**type**\: :py:class:`Dot1agCfmIngressActionFieldValue_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIngressActionFieldValue_Enum>`
            
            .. attribute:: dot1agcfmltringressmac
            
            	MAC address returned in the ingress MAC address field. If the dot1agCfmLtrIngress object contains the value ingNoTlv(0), then the contents of this object are meaningless
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmltringressportid
            
            	Ingress Port ID. The format of this object is determined by the value of the dot1agCfmLtrIngressPortIdSubtype object. If the dot1agCfmLtrIngress object contains the value ingNoTlv(0), then the contents of this object are meaningless
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: dot1agcfmltringressportidsubtype
            
            	Format of the Ingress Port ID. If the dot1agCfmLtrIngress object contains the value ingNoTlv(0), then the contents of this object are meaningless
            	**type**\: :py:class:`LldpPortIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpPortIdSubtype_Enum>`
            
            .. attribute:: dot1agcfmltrlastegressidentifier
            
            	An octet field holding the Last Egress Identifier returned in the LTR Egress Identifier TLV of the LTR. The Last Egress Identifier identifies the MEP Linktrace  Initiator that originated, or the Linktrace Responder that  forwarded, the LTM to which this LTR is the response.  This is the same value as the Egress Identifier TLV of that LTM
            	**type**\: str
            
            	**range:** 8
            
            .. attribute:: dot1agcfmltrmanaddress
            
            	The TAddress that can be used to access the SNMP agent of the system transmitting the CCM, received in the CCM Sender ID TLV from that system.  If the related object dot1agCfmLtrManAddressDomain contains the value 'zeroDotZero', this object dot1agCfmLtrManAddress MUST have a zero\-length OCTET STRING as a value
            	**type**\: str
            
            	**pattern:** (\\d\*(.\\d\*)\*)?
            
            .. attribute:: dot1agcfmltrmanaddressdomain
            
            	The TDomain that identifies the type and format of the related dot1agCfmMepDbManAddress object, used to access the SNMP agent of the system transmitting the LTR.  Received in the LTR Sender ID TLV from that system.  Typical values will be one of (not all inclusive) list\:      snmpUDPDomain          (from SNMPv2\-TM, RFC3417)    snmpIeee802Domain      (from SNMP\-IEEE802\-TM\-MIB, RFC4789)  The value 'zeroDotZero' (from RFC2578) indicates 'no management address was present in the LTR', in which case the related object dot1agCfmMepDbManAddress MUST have a zero\-length OCTET STRING as a value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: dot1agcfmltrnextegressidentifier
            
            	An octet field holding the Next Egress Identifier returned in the LTR Egress Identifier TLV of the LTR.  The Next Egress Identifier Identifies the Linktrace Responder that transmitted this LTR, and can forward the LTM to the next hop.  This is the same value as the Egress Identifier TLV of the forwarded LTM, if any. If the FwdYes bit of the Flags field is false, the contents of this field are undefined, i.e., any value can be transmitted, and the field is ignored by the receiver
            	**type**\: str
            
            	**range:** 8
            
            .. attribute:: dot1agcfmltrorganizationspecifictlv
            
            	All Organization specific TLVs returned in the LTR, if any.  Includes all octets including and following the TLV Length field of each TLV, concatenated together
            	**type**\: str
            
            	**range:** 0 \| 4..1500
            
            .. attribute:: dot1agcfmltrrelay
            
            	Value returned in the Relay Action field
            	**type**\: :py:class:`Dot1agCfmRelayActionFieldValue_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmRelayActionFieldValue_Enum>`
            
            .. attribute:: dot1agcfmltrterminalmep
            
            	A boolean value stating whether the forwarded LTM reached a MEP enclosing its MA, as returned in the Terminal MEP flag of the Flags field
            	**type**\: bool
            
            .. attribute:: dot1agcfmltrttl
            
            	TTL field value for a returned LTR
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmltrreceiveorder = None
                self.dot1agcfmltrseqnumber = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmepidentifier = None
                self.dot1agcfmltrchassisid = None
                self.dot1agcfmltrchassisidsubtype = None
                self.dot1agcfmltregress = None
                self.dot1agcfmltregressmac = None
                self.dot1agcfmltregressportid = None
                self.dot1agcfmltregressportidsubtype = None
                self.dot1agcfmltrforwarded = None
                self.dot1agcfmltringress = None
                self.dot1agcfmltringressmac = None
                self.dot1agcfmltringressportid = None
                self.dot1agcfmltringressportidsubtype = None
                self.dot1agcfmltrlastegressidentifier = None
                self.dot1agcfmltrmanaddress = None
                self.dot1agcfmltrmanaddressdomain = None
                self.dot1agcfmltrnextegressidentifier = None
                self.dot1agcfmltrorganizationspecifictlv = None
                self.dot1agcfmltrrelay = None
                self.dot1agcfmltrterminalmep = None
                self.dot1agcfmltrttl = None

            @property
            def _common_path(self):
                if self.dot1agcfmltrreceiveorder is None:
                    raise YPYDataValidationError('Key property dot1agcfmltrreceiveorder is None')
                if self.dot1agcfmltrseqnumber is None:
                    raise YPYDataValidationError('Key property dot1agcfmltrseqnumber is None')
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')
                if self.dot1agcfmmepidentifier is None:
                    raise YPYDataValidationError('Key property dot1agcfmmepidentifier is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmLtrTable/IEEE8021-CFM-MIB:dot1agCfmLtrEntry[IEEE8021-CFM-MIB:dot1agCfmLtrReceiveOrder = ' + str(self.dot1agcfmltrreceiveorder) + '][IEEE8021-CFM-MIB:dot1agCfmLtrSeqNumber = ' + str(self.dot1agcfmltrseqnumber) + '][IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + '][IEEE8021-CFM-MIB:dot1agCfmMepIdentifier = ' + str(self.dot1agcfmmepidentifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmltrreceiveorder is not None:
                    return True

                if self.dot1agcfmltrseqnumber is not None:
                    return True

                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmepidentifier is not None:
                    return True

                if self.dot1agcfmltrchassisid is not None:
                    return True

                if self.dot1agcfmltrchassisidsubtype is not None:
                    return True

                if self.dot1agcfmltregress is not None:
                    return True

                if self.dot1agcfmltregressmac is not None:
                    return True

                if self.dot1agcfmltregressportid is not None:
                    return True

                if self.dot1agcfmltregressportidsubtype is not None:
                    return True

                if self.dot1agcfmltrforwarded is not None:
                    return True

                if self.dot1agcfmltringress is not None:
                    return True

                if self.dot1agcfmltringressmac is not None:
                    return True

                if self.dot1agcfmltringressportid is not None:
                    return True

                if self.dot1agcfmltringressportidsubtype is not None:
                    return True

                if self.dot1agcfmltrlastegressidentifier is not None:
                    return True

                if self.dot1agcfmltrmanaddress is not None:
                    return True

                if self.dot1agcfmltrmanaddressdomain is not None:
                    return True

                if self.dot1agcfmltrnextegressidentifier is not None:
                    return True

                if self.dot1agcfmltrorganizationspecifictlv is not None:
                    return True

                if self.dot1agcfmltrrelay is not None:
                    return True

                if self.dot1agcfmltrterminalmep is not None:
                    return True

                if self.dot1agcfmltrttl is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmLtrTable.Dot1agCfmLtrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmLtrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmltrentry is not None:
                for child_ref in self.dot1agcfmltrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmLtrTable']['meta_info']


    class Dot1agCfmMaCompTable(object):
        """
        The Maintenance Association table.  Each row in the table
        represents an MA.  An MA is a set of MEPs, each configured
        with a single service instance.
        
        This is the part of the complete MA table that is variable
        across the Bridges in a Maintenance Domain, or across the
        components of a single Bridge.  That part of the MA table that
        is constant across the Bridges and their components in a
        Maintenance Domain is contained in the dot1agCfmMaNetTable.
        
        This table uses three indices, first index is the
        Dot1agCfmPbbComponentIdentifier that identifies the component
        within the Bridge for which the information in the
        dot1agCfmMaCompEntry applies.  The second is the index of the
        Maintenance Domain table.  The third index is the same as the
        index of the dot1agCfmMaNetEntry for the same MA.
        
        The writable objects in this table need to be persistent
        upon reboot or restart of a device.
        
        \*\*NOTE\: this object is deprecated due to re\-indexing of the 
        	table.
        
        .. attribute:: dot1agcfmmacompentry
        
        	The MA table entry. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: list of :py:class:`Dot1agCfmMaCompEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmacompentry = YList()
            self.dot1agcfmmacompentry.parent = self
            self.dot1agcfmmacompentry.name = 'dot1agcfmmacompentry'


        class Dot1agCfmMaCompEntry(object):
            """
            The MA table entry.
            \*\*NOTE\: this object is deprecated due to re\-indexing of the 
            	table.
            
            .. attribute:: dot1agcfmmacomponentid
            
            	The bridge component within the system to which the information in this dot1agCfmMaCompEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1. 	\*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmacompidpermission
            
            	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MPs configured in this MA. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
            
            .. attribute:: dot1agcfmmacompmhfcreation
            
            	Indicates if the Management entity can create MHFs (MIP Half Function) for this MA. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
            
            .. attribute:: dot1agcfmmacompnumberofvids
            
            	The number of VIDs associated with the MA. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmacompprimaryvlanid
            
            	The Primary VLAN ID with which the Maintenance Association is associated, or 0 if the MA is not attached to any VID.  If the MA is associated with more than one VID, the dot1agCfmVlanTable lists them. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: dot1agcfmmacomprowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmacomponentid = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmacompidpermission = None
                self.dot1agcfmmacompmhfcreation = None
                self.dot1agcfmmacompnumberofvids = None
                self.dot1agcfmmacompprimaryvlanid = None
                self.dot1agcfmmacomprowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmmacomponentid is None:
                    raise YPYDataValidationError('Key property dot1agcfmmacomponentid is None')
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaCompTable/IEEE8021-CFM-MIB:dot1agCfmMaCompEntry[IEEE8021-CFM-MIB:dot1agCfmMaComponentId = ' + str(self.dot1agcfmmacomponentid) + '][IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmacomponentid is not None:
                    return True

                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmacompidpermission is not None:
                    return True

                if self.dot1agcfmmacompmhfcreation is not None:
                    return True

                if self.dot1agcfmmacompnumberofvids is not None:
                    return True

                if self.dot1agcfmmacompprimaryvlanid is not None:
                    return True

                if self.dot1agcfmmacomprowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaCompTable.Dot1agCfmMaCompEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaCompTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmacompentry is not None:
                for child_ref in self.dot1agcfmmacompentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaCompTable']['meta_info']


    class Dot1agCfmMaMepListTable(object):
        """
        List of MEPIDs that belong to this MA.
        
        Clause 12.14.6.1.3 specifies that a list of MEPIDs in all
        bridges in that MA, but since SNMP SMI does not allow to
        state in a MIB that an object in a table is an array, the 
        information has to be stored in another table with two
        indices, being the first index, the index of the table that 
        contains the list or array.
        
        For all bridges in which the same MAID {dot1agCfmMdFormat,
        dot1agCfmMdName, dot1agCfmMaNetFormat, and dot1agCfmMaNetName}
        is configured, the same set of dot1agCfmMaMepListIdentifiers
        MUST be configured in the bridges' dot1agCfmMaMepListTables.
        This allows each MEP to determine whether or not it is
        receiving CCMs from all of the other MEPs in the MA.
        
        For example, if one were creating a new MA whose MAID were
        {charString, 'Dom1', charString, 'MA1'}, that had 2 MEPs, whose
        MEPIDs were 1 and 3, one could, in Bridge A\:
         1. Get a new MD index d from dot1agCfmMdTableNextIndex.
         2. Create the Maintenance Domain {charString, 'Dom1'}.
         3. Get a new MA index a from dot1agCfmMdMaNextIndex [d].
         4. Create the Maintenance Association {charString, 'MA1'}.
         5. Create a new dot1agCfmMaMepListEntry for each of the MEPs
            in the MA\: [d, a, 1] and [d, a, 3].
         6. Create one of the new MEPs, say [d, a, 1].
        Then, in Bridge B\:
         7. Do all of these steps 1\-6, except for using the other MEPID
            for the new MEP in Step 6, in this example, MEPID 3.
        Note that, when creating the MA, MEP List Table, and MEP
        entries in the second bridge, the indices 'd' and 'a'
        identifying the MAID {charString, 'Dom1', charString, 'MA1'}
        may have different values than those in the first Bridge.
        
        .. attribute:: dot1agcfmmameplistentry
        
        	The known MEPS table entry
        	**type**\: list of :py:class:`Dot1agCfmMaMepListEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmameplistentry = YList()
            self.dot1agcfmmameplistentry.parent = self
            self.dot1agcfmmameplistentry.name = 'dot1agcfmmameplistentry'


        class Dot1agCfmMaMepListEntry(object):
            """
            The known MEPS table entry.
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmameplistidentifier
            
            	MEPID
            	**type**\: int
            
            	**range:** 1..8191
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmameplistrowstatus
            
            	The status of the row. Read SNMPv2\-TC (RFC1903) for an explanation of the possible values this object can take
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmameplistidentifier = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmameplistrowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmameplistidentifier is None:
                    raise YPYDataValidationError('Key property dot1agcfmmameplistidentifier is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaMepListTable/IEEE8021-CFM-MIB:dot1agCfmMaMepListEntry[IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMaMepListIdentifier = ' + str(self.dot1agcfmmameplistidentifier) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmameplistidentifier is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmameplistrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaMepListTable.Dot1agCfmMaMepListEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaMepListTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmameplistentry is not None:
                for child_ref in self.dot1agcfmmameplistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaMepListTable']['meta_info']


    class Dot1agCfmMaNetTable(object):
        """
        The Maintenance Association table.  Each row in the table
        represents an MA.  An MA is a set of MEPs, each configured
        with a single service instance.
        
        This is the part of the complete MA table that is constant
        across all Bridges in a Maintenance Domain, and across all
        components of a single Bridge.  That part of the MA table that
        can vary from Bridge component to Bridge component is contained
        in the dot1agCfmMaCompTable.
        
        Creation of a Service Instance establishes a connectionless
        association among the selected DSAPs.  Configuring a
        Maintenance association End Point (MEP) at each of the
        DSAPs creates a Maintenance Association (MA) to monitor
        that connectionless connectivity.  The MA is identified by a
        Short MA Name that is unique within the Maintenance Domain
        and chosen to facilitate easy identification of the Service
        Instance.  Together, the Maintenance Domain Name and the
        Short MA Name form the Maintenance Association Identifier
        (MAID) that is carried in CFM Messages to identify
        incorrect connectivity among Service Instances.  A small
        integer, the Maintenance association End Point Identifier
        (MEPID), identifies each MEP among those configured on a
        single MA (802.1ag clauses 3.19 and 18.2).
        
        This table uses two indices, first index is the index of the
        Maintenance Domain table.  The second index is the same as the
        index of the dot1agCfmMaCompEntry for the same MA.
        
        The writable objects in this table need to be persistent
        upon reboot or restart of a device.
        
        .. attribute:: dot1agcfmmanetentry
        
        	The MA table entry
        	**type**\: list of :py:class:`Dot1agCfmMaNetEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmanetentry = YList()
            self.dot1agcfmmanetentry.parent = self
            self.dot1agcfmmanetentry.name = 'dot1agcfmmanetentry'


        class Dot1agCfmMaNetEntry(object):
            """
            The MA table entry.
            
            .. attribute:: dot1agcfmmaindex
            
            	Index of the MA table dot1agCfmMdMaNextIndex needs to be inspected to find an available index for row\-creation
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmanetccminterval
            
            	Interval between CCM transmissions to be used by all MEPs in the MA
            	**type**\: :py:class:`Dot1agCfmCcmInterval_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmCcmInterval_Enum>`
            
            .. attribute:: dot1agcfmmanetformat
            
            	The type (and thereby format) of the Maintenance Association Name
            	**type**\: :py:class:`Dot1agCfmMaintAssocNameType_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMaintAssocNameType_Enum>`
            
            .. attribute:: dot1agcfmmanetname
            
            	The Short Maintenance Association name. The type/format of this object is determined by the value of the dot1agCfmMaNetNameType object.  This name MUST be unique within a maintenance domain
            	**type**\: str
            
            	**range:** 1..45
            
            .. attribute:: dot1agcfmmanetrowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmanetccminterval = None
                self.dot1agcfmmanetformat = None
                self.dot1agcfmmanetname = None
                self.dot1agcfmmanetrowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaNetTable/IEEE8021-CFM-MIB:dot1agCfmMaNetEntry[IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmanetccminterval is not None:
                    return True

                if self.dot1agcfmmanetformat is not None:
                    return True

                if self.dot1agcfmmanetname is not None:
                    return True

                if self.dot1agcfmmanetrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaNetTable.Dot1agCfmMaNetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMaNetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmanetentry is not None:
                for child_ref in self.dot1agcfmmanetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMaNetTable']['meta_info']


    class Dot1agCfmMd(object):
        """
        
        
        .. attribute:: dot1agcfmmdtablenextindex
        
        	This object contains an unused value for dot1agCfmMdIndex in the dot1agCfmMdTable, or a zero to indicate that none exist
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmdtablenextindex = None

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMd'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmdtablenextindex is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMd']['meta_info']


    class Dot1agCfmMdTable(object):
        """
        The Maintenance Domain table. Each row in the table
        represents a different Maintenance Domain.
        
        A Maintenance Domain is described in 802.1ag (3.22) as the
        network or the part of the network for which faults in
        connectivity are to be managed. The boundary of a Maintenance
        Domain is defined by a set of DSAPs, each of which can become
        a point of connectivity to a service instance.
        
        .. attribute:: dot1agcfmmdentry
        
        	The Maintenance Domain table entry. This entry is not lost upon reboot. It is backed up by stable storage
        	**type**\: list of :py:class:`Dot1agCfmMdEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmdentry = YList()
            self.dot1agcfmmdentry.parent = self
            self.dot1agcfmmdentry.name = 'dot1agcfmmdentry'


        class Dot1agCfmMdEntry(object):
            """
            The Maintenance Domain table entry. This entry is not lost
            upon reboot. It is backed up by stable storage.
            
            .. attribute:: dot1agcfmmdindex
            
            	The index to the Maintenance Domain table.  dot1agCfmMdTableNextIndex needs to be inspected to find an available index for row\-creation.  Referential integrity is required, i.e., the index needs to be persistent upon a reboot or restart of a device.  The index can never be reused for other Maintenance Domain.  The index value SHOULD keep increasing up to the time that they wrap around. This is to facilitate access control based on OID
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdformat
            
            	The type (and thereby format) of the Maintenance Domain Name
            	**type**\: :py:class:`Dot1agCfmMaintDomainNameType_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMaintDomainNameType_Enum>`
            
            .. attribute:: dot1agcfmmdmanextindex
            
            	Value to be used as the index of the MA table entries, both the dot1agCfmMaNetTable and the dot1agCfmMaCompTable, for this Maintenance Domain when the management entity wants to create a new row in those tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmdmdlevel
            
            	The Maintenance Domain Level
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1agcfmmdmhfcreation
            
            	Enumerated value indicating whether the management entity can create MHFs (MIP Half Function) for this Maintenance Domain. Since, in this variable, there is no encompassing Maintenance Domain, the value defMHFdefer is not allowed
            	**type**\: :py:class:`Dot1agCfmMhfCreation_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMhfCreation_Enum>`
            
            .. attribute:: dot1agcfmmdmhfidpermission
            
            	Enumerated value indicating what, if anything, is to be included in the Sender ID TLV (21.5.3) transmitted by MPs configured in this Maintenance Domain.  Since, in this variable, there is no encompassing Maintenance Domain, the value sendIdDefer is not allowed
            	**type**\: :py:class:`Dot1agCfmIdPermission_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmIdPermission_Enum>`
            
            .. attribute:: dot1agcfmmdname
            
            	The Maintenance Domain name. The type/format of this object is determined by the value of the dot1agCfmMdNameType object.    Each Maintenance Domain has unique name amongst all those used or available to a service provider or operator.  It facilitates easy identification of administrative responsibility for each Maintenance Domain.  Clause 3.24 defines a Maintenance Domain name as the identifier, unique over the domain for which CFM is to protect against accidental concatenation of Service Instances, of a particular Maintenance Domain
            	**type**\: str
            
            	**range:** 1..43
            
            .. attribute:: dot1agcfmmdrowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmdformat = None
                self.dot1agcfmmdmanextindex = None
                self.dot1agcfmmdmdlevel = None
                self.dot1agcfmmdmhfcreation = None
                self.dot1agcfmmdmhfidpermission = None
                self.dot1agcfmmdname = None
                self.dot1agcfmmdrowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMdTable/IEEE8021-CFM-MIB:dot1agCfmMdEntry[IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmdformat is not None:
                    return True

                if self.dot1agcfmmdmanextindex is not None:
                    return True

                if self.dot1agcfmmdmdlevel is not None:
                    return True

                if self.dot1agcfmmdmhfcreation is not None:
                    return True

                if self.dot1agcfmmdmhfidpermission is not None:
                    return True

                if self.dot1agcfmmdname is not None:
                    return True

                if self.dot1agcfmmdrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMdTable.Dot1agCfmMdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmdentry is not None:
                for child_ref in self.dot1agcfmmdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMdTable']['meta_info']


    class Dot1agCfmMepDbTable(object):
        """
        The MEP Database. A database, maintained by every MEP, that
        maintains received information about other MEPs in the
        Maintenance Domain.
        
        The SMI does not allow to state in a MIB that an object in
        a table is an array. The solution is to take the index (or
        indices) of the first table and add one or more indices.
        
        .. attribute:: dot1agcfmmepdbentry
        
        	The MEP Database table entry
        	**type**\: list of :py:class:`Dot1agCfmMepDbEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmepdbentry = YList()
            self.dot1agcfmmepdbentry.parent = self
            self.dot1agcfmmepdbentry.name = 'dot1agcfmmepdbentry'


        class Dot1agCfmMepDbEntry(object):
            """
            The MEP Database table entry.
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmepdbrmepidentifier
            
            	Maintenance association End Point Identifier of a remote MEP whose information from the MEP Database is to be returned
            	**type**\: int
            
            	**range:** 1..8191
            
            .. attribute:: dot1agcfmmepidentifier
            
            	
            	**type**\: int
            
            	**range:** 1..8191
            
            .. attribute:: dot1agcfmmepdbchassisid
            
            	The Chassis ID. The format of this object is determined by the value of the dot1agCfmLtrChassisIdSubtype object
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: dot1agcfmmepdbchassisidsubtype
            
            	This object specifies the format of the Chassis ID received in the last CCM
            	**type**\: :py:class:`LldpChassisIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpChassisIdSubtype_Enum>`
            
            .. attribute:: dot1agcfmmepdbinterfacestatustlv
            
            	An enumerated value of the Interface status TLV received in the last CCM from the remote MEP or the default value isNoInterfaceStatus TLV indicating either no CCM has been received, or that no interface status TLV was received in the last CCM
            	**type**\: :py:class:`Dot1agCfmInterfaceStatus_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmInterfaceStatus_Enum>`
            
            .. attribute:: dot1agcfmmepdbmacaddress
            
            	The MAC address of the remote MEP
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmmepdbmanaddress
            
            	The TAddress that can be used to access the SNMP agent of the system transmitting the CCM, received in the CCM Sender ID TLV from that system.  If the related object dot1agCfmMepDbManAddressDomain contains the value 'zeroDotZero', this object dot1agCfmMepDbManAddress MUST have a zero\-length OCTET STRING as a value
            	**type**\: str
            
            	**pattern:** (\\d\*(.\\d\*)\*)?
            
            .. attribute:: dot1agcfmmepdbmanaddressdomain
            
            	The TDomain that identifies the type and format of the related dot1agCfmMepDbManAddress object, used to access the SNMP agent of the system transmitting the CCM.  Received in the CCM Sender ID TLV from that system.  Typical values will be one of (not all inclusive) list\:      snmpUDPDomain          (from SNMPv2\-TM, RFC3417)    snmpIeee802Domain      (from SNMP\-IEEE802\-TM\-MIB, RFC4789)  The value 'zeroDotZero' (from RFC2578) indicates 'no management address was present in the LTR', in which case the related object dot1agCfmMepDbManAddress MUST have a zero\-length OCTET STRING as a value
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: dot1agcfmmepdbportstatustlv
            
            	An enumerated value of the Port status TLV received in the last CCM from the remote MEP or the default value psNoPortStateTLV indicating either no CCM has been received, or that nor port status TLV was received in the last CCM
            	**type**\: :py:class:`Dot1agCfmPortStatus_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmPortStatus_Enum>`
            
            .. attribute:: dot1agcfmmepdbrdi
            
            	State of the RDI bit in the last received CCM (true for RDI=1), or false if none has been received
            	**type**\: bool
            
            .. attribute:: dot1agcfmmepdbrmepfailedoktime
            
            	The time (SysUpTime) at which the IFF Remote MEP state machine last entered either the RMEP\_FAILED or RMEP\_OK state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepdbrmepstate
            
            	The operational state of the remote MEP IFF State machines
            	**type**\: :py:class:`Dot1agCfmRemoteMepState_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmRemoteMepState_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmepdbrmepidentifier = None
                self.dot1agcfmmepidentifier = None
                self.dot1agcfmmepdbchassisid = None
                self.dot1agcfmmepdbchassisidsubtype = None
                self.dot1agcfmmepdbinterfacestatustlv = None
                self.dot1agcfmmepdbmacaddress = None
                self.dot1agcfmmepdbmanaddress = None
                self.dot1agcfmmepdbmanaddressdomain = None
                self.dot1agcfmmepdbportstatustlv = None
                self.dot1agcfmmepdbrdi = None
                self.dot1agcfmmepdbrmepfailedoktime = None
                self.dot1agcfmmepdbrmepstate = None

            @property
            def _common_path(self):
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')
                if self.dot1agcfmmepdbrmepidentifier is None:
                    raise YPYDataValidationError('Key property dot1agcfmmepdbrmepidentifier is None')
                if self.dot1agcfmmepidentifier is None:
                    raise YPYDataValidationError('Key property dot1agcfmmepidentifier is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMepDbTable/IEEE8021-CFM-MIB:dot1agCfmMepDbEntry[IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + '][IEEE8021-CFM-MIB:dot1agCfmMepDbRMepIdentifier = ' + str(self.dot1agcfmmepdbrmepidentifier) + '][IEEE8021-CFM-MIB:dot1agCfmMepIdentifier = ' + str(self.dot1agcfmmepidentifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmepdbrmepidentifier is not None:
                    return True

                if self.dot1agcfmmepidentifier is not None:
                    return True

                if self.dot1agcfmmepdbchassisid is not None:
                    return True

                if self.dot1agcfmmepdbchassisidsubtype is not None:
                    return True

                if self.dot1agcfmmepdbinterfacestatustlv is not None:
                    return True

                if self.dot1agcfmmepdbmacaddress is not None:
                    return True

                if self.dot1agcfmmepdbmanaddress is not None:
                    return True

                if self.dot1agcfmmepdbmanaddressdomain is not None:
                    return True

                if self.dot1agcfmmepdbportstatustlv is not None:
                    return True

                if self.dot1agcfmmepdbrdi is not None:
                    return True

                if self.dot1agcfmmepdbrmepfailedoktime is not None:
                    return True

                if self.dot1agcfmmepdbrmepstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMepDbTable.Dot1agCfmMepDbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMepDbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmepdbentry is not None:
                for child_ref in self.dot1agcfmmepdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMepDbTable']['meta_info']


    class Dot1agCfmMepTable(object):
        """
        The Maintenance Association End Point (MEP) table.
        
        Each row in the table represents a different MEP.  A MEP is
        an actively managed CFM entity, associated with a specific
        DSAP of a Service Instance, which can generate and receive
        CFM PDUs and track any responses.  It is an end point of a
        single Maintenance Association, and is an endpoint of a
        separate Maintenance Entity for each of the other MEPs in
        the same Maintenance Association (802.1ag clause 3.19).
        
        This table uses three indices. The first two indices are the
        indices of the Maintenance Domain and MA tables, the reason
        being that a MEP is always related to an MA and Maintenance
        Domain.
        
        The MEP table also stores all the managed objects for sending
        LBM and LTM.
        
        \*LBM Managed objects
        
        LBM Managed objects in the MEP table
        enables the management entity to initiate
        transmission of Loopback messages.  It will signal the MEP
        that it SHOULD transmit some number of Loopback messages
        and detect the detection (or lack thereof) of the
        corresponding Loopback messages.
        
        Steps to use entries in this table\:
        
        1) Wait for dot1agCfmMepTransmitLbmStatus value to be
           false.  To do this do this sequence\:
           a. an SNMP GET for both SnmpSetSerialNo and
              dot1agCfmMepTransmitLbmStatus objects (in same SNMP
              PDU).
           b. Check if value for dot1agCfmMepTransmitLbmStatus is false.
              \- if not, wait x seconds, go to step a above.
              \- if yes, save the value of SnmpSetSerialNo and go
                to step 2) below
        2) Change dot1agCfmMepTransmitLbmStatus value from false to
           true to ensure no other management entity will use
           the service. In order to not disturb a possible other NMS
           do this by sending an SNMP SET for both SnmpSetSerialNo
           and dot1agCfmMepTransmitLbmStatus objects (in same SNMP
           PDU,  and make sure SNmpSetSerialNo is the first varBind).
           For the SnmpSetSerialNo varBind, use the value that you
           obtained in step 1)a.. This ensures that two cooperating
           NMSes will not step on each others toes.
           Setting this MIB object does not set the corresponding
           LBIactive state machine variable.
        3) Setup the different data to be sent (number of messages,
           optional TLVs,...), except do not set
           dot1agCfmMepTransmitLbmMessages.
        4) Record the current values of dot1agCfmMepLbrIn,
           dot1agCfmMepLbrInOutOfOrder, and dot1agCfmMepLbrBadMsdu.
        6) Set dot1agCfmMepTransmitLbmMessages to a non\-zero value to
           initiate transmission of Loopback messages.
           The dot1agCfmMepTransmitLbmMessages indicates the
           number of LBMs to be sent and is not decremented as
           loopbacks are actually sent. dot1agCfmMepTransmitLbmMessages
           is not equivalent to the LBMsToSend state machine variable.
        7) Check the value of dot1agCfmMepTransmitLbmResultOK to
           find out if the operation was successfully initiated or
           not.
        8) Monitor the value of dot1agCfmMepTransmitLbmStatus.
           When it is reset to false, the last LBM has been transmitted.
           Wait an additional 5 seconds to ensure that all LBRs have
           been returned.
        9) Compare dot1agCfmMepLbrIn, dot1agCfmMepLbrInOutOfOrder,
           and dot1agCfmMepLbrBadMsdu to their old values from step
           4, above, to get the results of the test.
        
        \*LTM Managed objects
        The LTM Managed objects in the MEP table are used in a manner
        similar to that described for LBM transmission, above.  Upon
        successfully initiating the transmission, the variables
        dot1agCfmMepTransmitLtmSeqNumber and
        dot1agCfmMepTransmitLtmEgressIdentifier return the information
        required to recover the results of the LTM from the
        dot1agCfmLtrTable.
        
        .. attribute:: dot1agcfmmepentry
        
        	The MEP table entry
        	**type**\: list of :py:class:`Dot1agCfmMepEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmmepentry = YList()
            self.dot1agcfmmepentry.parent = self
            self.dot1agcfmmepentry.name = 'dot1agcfmmepentry'


        class Dot1agCfmMepEntry(object):
            """
            The MEP table entry
            
            .. attribute:: dot1agcfmmaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmdindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmmepidentifier
            
            	Integer that is unique among all the MEPs in the same MA. Other definition is\: a small integer, unique over a given Maintenance Association, identifying a specific Maintenance association End Point (3.19).  MEP Identifier is also known as the MEPID
            	**type**\: int
            
            	**range:** 1..8191
            
            .. attribute:: dot1agcfmmepactive
            
            	Administrative state of the MEP  A Boolean indicating the administrative state of the MEP.  True indicates that the MEP is to function normally, and false that it is to cease functioning
            	**type**\: bool
            
            .. attribute:: dot1agcfmmepccienabled
            
            	If set to true, the MEP will generate CCM messages
            	**type**\: bool
            
            .. attribute:: dot1agcfmmepccisentccms
            
            	Total number of Continuity Check messages transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepccmltmpriority
            
            	The priority value for CCMs and LTMs transmitted by the MEP. Default Value is the highest priority value allowed to pass through the bridge port for any of this MEPs VIDs. The management entity can obtain the default value for this  variable from the priority regeneration table by extracting the  highest priority value in this table on this MEPs bridge port. (1 is lowest, then 2, then 0, then 3\-7)
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1agcfmmepccmsequenceerrors
            
            	The total number of out\-of\-sequence CCMs received from all remote MEPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepdefects
            
            	A vector of Boolean error conditions from Table 20\-1, any of which may be true\:  DefRDICCM(0) DefMACstatus(1) DefRemoteCCM(2) DefErrorCCM(3) DefXconCCM(4)
            	**type**\: :py:class:`Dot1agCfmMepDefects_Bits <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMepDefects_Bits>`
            
            .. attribute:: dot1agcfmmepdirection
            
            	The direction in which the MEP faces on the Bridge port
            	**type**\: :py:class:`Dot1agCfmMpDirection_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMpDirection_Enum>`
            
            .. attribute:: dot1agcfmmeperrorccmlastfailure
            
            	The last\-received CCM that triggered an DefErrorCCM fault
            	**type**\: str
            
            	**range:** 1..1522
            
            .. attribute:: dot1agcfmmepfngalarmtime
            
            	The time that defects MUST be present before a Fault Alarm is issued (fngAlarmTime. 20.33.3) (default 2.5s)
            	**type**\: int
            
            	**range:** 250..1000
            
            .. attribute:: dot1agcfmmepfngresettime
            
            	The time that defects MUST be absent before resetting a Fault Alarm (fngResetTime, 20.33.4) (default 10s)
            	**type**\: int
            
            	**range:** 250..1000
            
            .. attribute:: dot1agcfmmepfngstate
            
            	Current state of the MEP Fault Notification Generator State Machine
            	**type**\: :py:class:`Dot1agCfmFngState_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmFngState_Enum>`
            
            .. attribute:: dot1agcfmmephighestprdefect
            
            	The highest priority defect that has been present since the MEPs Fault Notification Generator State Machine was last in the FNG\_RESET state
            	**type**\: :py:class:`Dot1agCfmHighestDefectPri_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmHighestDefectPri_Enum>`
            
            .. attribute:: dot1agcfmmepifindex
            
            	This object is the interface index of the interface either a bridge port, or an aggregated IEEE 802.1 link within a bridge port, to which the MEP is attached.  Upon a restart of the system, the system SHALL, if necessary, change the value of this variable so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart.  If no such entry exists, then the system SHALL set this variable to 0
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1agcfmmeplbrbadmsdu
            
            	The total number of LBRs received whose mac\_service\_data\_unit did not match (except for the OpCode) that of the corresponding LBM (20.2.3)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeplbrin
            
            	Total number of valid, in\-order Loopback Replies received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeplbrinoutoforder
            
            	The total number of valid, out\-of\-order Loopback Replies received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeplbrout
            
            	Total number of Loopback Replies transmitted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeplowprdef
            
            	An integer value specifying the lowest priority defect  that is allowed to generate fault alarm
            	**type**\: :py:class:`Dot1agCfmLowestAlarmPri_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmLowestAlarmPri_Enum>`
            
            .. attribute:: dot1agcfmmepltmnextseqnumber
            
            	Next transaction identifier/sequence number to be sent in a Linktrace message. This sequence number can be zero because it wraps around
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepmacaddress
            
            	MAC address of the MEP
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmmepnextlbmtransid
            
            	Next sequence number/transaction identifier to be sent in a Loopback message. This sequence number can be zero because it wraps around
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepprimaryvid
            
            	An integer indicating the Primary VID of the MEP, always one of the VIDs assigned to the MEP's MA.  The value 0 indicates that either the Primary VID is that of the MEP's MA, or that the MEP's MA is associated with no VID
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: dot1agcfmmeprowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: dot1agcfmmeptransmitlbmdatatlv
            
            	An arbitrary amount of data to be included in the Data TLV, if the Data TLV is selected to be sent.  The intent is to be able to fill the frame carrying the CFM PDU to its maximum length. This may lead to fragmentation in some cases
            	**type**\: str
            
            .. attribute:: dot1agcfmmeptransmitlbmdestismepid
            
            	True indicates that MEPID of the target MEP is used for Loopback transmission. False indicates that unicast destination MAC address of the target MEP is used for Loopback transmission
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitlbmdestmacaddress
            
            	The Target MAC Address Field to be transmitted\: A unicast destination MAC address. This address will be used if the value of the column dot1agCfmMepTransmitLbmDestIsMepId is 'false'
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmmeptransmitlbmdestmepid
            
            	The Maintenance association End Point Identifier of another MEP in the same Maintenance Association to which the LBM is to be sent. This address will be used if the value of the column dot1agCfmMepTransmitLbmDestIsMepId is 'true'
            	**type**\: int
            
            	**range:** 0..8191
            
            .. attribute:: dot1agcfmmeptransmitlbmmessages
            
            	The number of Loopback messages to be transmitted
            	**type**\: int
            
            	**range:** 1..1024
            
            .. attribute:: dot1agcfmmeptransmitlbmresultok
            
            	Indicates the result of the operation\:  \- true       The Loopback Message(s) will be              (or has been) sent. \- false      The Loopback Message(s) will not              be sent
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitlbmseqnumber
            
            	The Loopback Transaction Identifier (dot1agCfmMepNextLbmTransId) of the first LBM (to be) sent.  The value returned is undefined if  dot1agCfmMepTransmitLbmResultOK is false
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeptransmitlbmstatus
            
            	A Boolean flag set to true by the MEP Loopback Initiator State Machine or an MIB manager to indicate that another LBM is being transmitted. Reset to false by the MEP Loopback Initiator State Machine
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitlbmvlandropenable
            
            	Drop Enable bit value to be used in the VLAN tag, if present in the transmitted frame.  For more information about VLAN Drop Enable, please check IEEE 802.1ad
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitlbmvlanpriority
            
            	Priority. 3 bit value to be used in the VLAN tag, if present in the transmitted frame.  The default value is CCM priority
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1agcfmmeptransmitltmegressidentifier
            
            	Identifies the MEP Linktrace Initiator that is originating, or the Linktrace Responder that is forwarding, this LTM. The low\-order six octets contain a 48\-bit IEEE MAC address unique to the system in which the MEP Linktrace Initiator or Linktrace Responder resides.  The high\-order two octets contain a value sufficient to uniquely identify the MEP Linktrace Initiator or Linktrace Responder within that system.  For most Bridges, the address of any MAC attached to the Bridge will suffice for the low\-order six octets, and 0 for the high\-order octets.  In some situations, e.g., if multiple virtual Bridges utilizing emulated LANs are implemented in a single physical system, the high\-order two octets can be used to differentiate among the transmitting entities.  The value returned is undefined if dot1agCfmMepTransmitLtmResult is false
            	**type**\: str
            
            	**range:** 8
            
            .. attribute:: dot1agcfmmeptransmitltmflags
            
            	The flags field for LTMs transmitted by the MEP
            	**type**\: :py:class:`Dot1agCfmMepTransmitLtmFlags_Bits <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry.Dot1agCfmMepTransmitLtmFlags_Bits>`
            
            .. attribute:: dot1agcfmmeptransmitltmresult
            
            	Indicates the result of the operation\:  \- true    The Linktrace Message will be (or has been) sent. \- false   The Linktrace Message will not be sent
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitltmseqnumber
            
            	The LTM Transaction Identifier (dot1agCfmMepLtmNextSeqNumber) of the LTM sent. The value returned is undefined if dot1agCfmMepTransmitLtmResult is false
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmeptransmitltmstatus
            
            	A Boolean flag set to true by the bridge port to indicate that another LTM may be transmitted.  Reset to false by the MEP Linktrace Initiator State Machine
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitltmtargetismepid
            
            	True indicates that MEPID of the target MEP is used for Linktrace transmission. False indicates that unicast destination MAC address of the target MEP is used for Loopback transmission
            	**type**\: bool
            
            .. attribute:: dot1agcfmmeptransmitltmtargetmacaddress
            
            	The Target MAC Address Field to be transmitted\: A unicast destination MAC address. This address will be used if the value of the column dot1agCfmMepTransmitLtmTargetIsMepId is 'false'
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmmeptransmitltmtargetmepid
            
            	An indication of the Target MAC Address Field to be transmitted\: The Maintenance association End Point Identifier of another MEP in the same Maintenance Association This address will be used if the value of the column dot1agCfmMepTransmitLtmTargetIsMepId is 'true'
            	**type**\: int
            
            	**range:** 0..8191
            
            .. attribute:: dot1agcfmmeptransmitltmttl
            
            	The LTM TTL field. Default value, if not specified, is 64. The TTL field indicates the number of hops remaining to the LTM.  Decremented by 1 by each Linktrace Responder that handles the LTM.  The value returned in the LTR is one less than that received in the LTM.  If the LTM TTL is 0 or 1, the LTM is not forwarded to the next hop, and if 0, no LTR is generated
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: dot1agcfmmepunexpltrin
            
            	The total number of unexpected LTRs received (20.39.1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmmepxconccmlastfailure
            
            	The last\-received CCM that triggered a DefXconCCM fault
            	**type**\: str
            
            	**range:** 1..1522
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmmaindex = None
                self.dot1agcfmmdindex = None
                self.dot1agcfmmepidentifier = None
                self.dot1agcfmmepactive = None
                self.dot1agcfmmepccienabled = None
                self.dot1agcfmmepccisentccms = None
                self.dot1agcfmmepccmltmpriority = None
                self.dot1agcfmmepccmsequenceerrors = None
                self.dot1agcfmmepdefects = Dot1agCfmMepDefects_Bits()
                self.dot1agcfmmepdirection = None
                self.dot1agcfmmeperrorccmlastfailure = None
                self.dot1agcfmmepfngalarmtime = None
                self.dot1agcfmmepfngresettime = None
                self.dot1agcfmmepfngstate = None
                self.dot1agcfmmephighestprdefect = None
                self.dot1agcfmmepifindex = None
                self.dot1agcfmmeplbrbadmsdu = None
                self.dot1agcfmmeplbrin = None
                self.dot1agcfmmeplbrinoutoforder = None
                self.dot1agcfmmeplbrout = None
                self.dot1agcfmmeplowprdef = None
                self.dot1agcfmmepltmnextseqnumber = None
                self.dot1agcfmmepmacaddress = None
                self.dot1agcfmmepnextlbmtransid = None
                self.dot1agcfmmepprimaryvid = None
                self.dot1agcfmmeprowstatus = None
                self.dot1agcfmmeptransmitlbmdatatlv = None
                self.dot1agcfmmeptransmitlbmdestismepid = None
                self.dot1agcfmmeptransmitlbmdestmacaddress = None
                self.dot1agcfmmeptransmitlbmdestmepid = None
                self.dot1agcfmmeptransmitlbmmessages = None
                self.dot1agcfmmeptransmitlbmresultok = None
                self.dot1agcfmmeptransmitlbmseqnumber = None
                self.dot1agcfmmeptransmitlbmstatus = None
                self.dot1agcfmmeptransmitlbmvlandropenable = None
                self.dot1agcfmmeptransmitlbmvlanpriority = None
                self.dot1agcfmmeptransmitltmegressidentifier = None
                self.dot1agcfmmeptransmitltmflags = IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry.Dot1agCfmMepTransmitLtmFlags_Bits()
                self.dot1agcfmmeptransmitltmresult = None
                self.dot1agcfmmeptransmitltmseqnumber = None
                self.dot1agcfmmeptransmitltmstatus = None
                self.dot1agcfmmeptransmitltmtargetismepid = None
                self.dot1agcfmmeptransmitltmtargetmacaddress = None
                self.dot1agcfmmeptransmitltmtargetmepid = None
                self.dot1agcfmmeptransmitltmttl = None
                self.dot1agcfmmepunexpltrin = None
                self.dot1agcfmmepxconccmlastfailure = None

            class Dot1agCfmMepTransmitLtmFlags_Bits(FixedBitsDict):
                """
                Dot1agCfmMepTransmitLtmFlags_Bits

                The flags field for LTMs transmitted by the MEP.
                Keys are:- useFDBonly

                """

                def __init__(self):
                    self._dictionary = { 
                        'useFDBonly':False,
                    }
                    self._pos_map = { 
                        'useFDBonly':0,
                    }

            @property
            def _common_path(self):
                if self.dot1agcfmmaindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmaindex is None')
                if self.dot1agcfmmdindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmmdindex is None')
                if self.dot1agcfmmepidentifier is None:
                    raise YPYDataValidationError('Key property dot1agcfmmepidentifier is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMepTable/IEEE8021-CFM-MIB:dot1agCfmMepEntry[IEEE8021-CFM-MIB:dot1agCfmMaIndex = ' + str(self.dot1agcfmmaindex) + '][IEEE8021-CFM-MIB:dot1agCfmMdIndex = ' + str(self.dot1agcfmmdindex) + '][IEEE8021-CFM-MIB:dot1agCfmMepIdentifier = ' + str(self.dot1agcfmmepidentifier) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmmaindex is not None:
                    return True

                if self.dot1agcfmmdindex is not None:
                    return True

                if self.dot1agcfmmepidentifier is not None:
                    return True

                if self.dot1agcfmmepactive is not None:
                    return True

                if self.dot1agcfmmepccienabled is not None:
                    return True

                if self.dot1agcfmmepccisentccms is not None:
                    return True

                if self.dot1agcfmmepccmltmpriority is not None:
                    return True

                if self.dot1agcfmmepccmsequenceerrors is not None:
                    return True

                if self.dot1agcfmmepdefects is not None:
                    if self.dot1agcfmmepdefects._has_data():
                        return True

                if self.dot1agcfmmepdirection is not None:
                    return True

                if self.dot1agcfmmeperrorccmlastfailure is not None:
                    return True

                if self.dot1agcfmmepfngalarmtime is not None:
                    return True

                if self.dot1agcfmmepfngresettime is not None:
                    return True

                if self.dot1agcfmmepfngstate is not None:
                    return True

                if self.dot1agcfmmephighestprdefect is not None:
                    return True

                if self.dot1agcfmmepifindex is not None:
                    return True

                if self.dot1agcfmmeplbrbadmsdu is not None:
                    return True

                if self.dot1agcfmmeplbrin is not None:
                    return True

                if self.dot1agcfmmeplbrinoutoforder is not None:
                    return True

                if self.dot1agcfmmeplbrout is not None:
                    return True

                if self.dot1agcfmmeplowprdef is not None:
                    return True

                if self.dot1agcfmmepltmnextseqnumber is not None:
                    return True

                if self.dot1agcfmmepmacaddress is not None:
                    return True

                if self.dot1agcfmmepnextlbmtransid is not None:
                    return True

                if self.dot1agcfmmepprimaryvid is not None:
                    return True

                if self.dot1agcfmmeprowstatus is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmdatatlv is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmdestismepid is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmdestmacaddress is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmdestmepid is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmmessages is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmresultok is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmseqnumber is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmstatus is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmvlandropenable is not None:
                    return True

                if self.dot1agcfmmeptransmitlbmvlanpriority is not None:
                    return True

                if self.dot1agcfmmeptransmitltmegressidentifier is not None:
                    return True

                if self.dot1agcfmmeptransmitltmflags is not None:
                    if self.dot1agcfmmeptransmitltmflags._has_data():
                        return True

                if self.dot1agcfmmeptransmitltmresult is not None:
                    return True

                if self.dot1agcfmmeptransmitltmseqnumber is not None:
                    return True

                if self.dot1agcfmmeptransmitltmstatus is not None:
                    return True

                if self.dot1agcfmmeptransmitltmtargetismepid is not None:
                    return True

                if self.dot1agcfmmeptransmitltmtargetmacaddress is not None:
                    return True

                if self.dot1agcfmmeptransmitltmtargetmepid is not None:
                    return True

                if self.dot1agcfmmeptransmitltmttl is not None:
                    return True

                if self.dot1agcfmmepunexpltrin is not None:
                    return True

                if self.dot1agcfmmepxconccmlastfailure is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMepTable.Dot1agCfmMepEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmMepTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmmepentry is not None:
                for child_ref in self.dot1agcfmmepentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmMepTable']['meta_info']


    class Dot1agCfmStackTable(object):
        """
        There is one CFM Stack table per bridge. It permits
        the retrieval of information about the Maintenance Points
        configured on any given interface.
        \*\*NOTE\: this object is deprecated due to re\-indexing of the 
        	table.
        
        .. attribute:: dot1agcfmstackentry
        
        	The Stack table entry \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: list of :py:class:`Dot1agCfmStackEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmstackentry = YList()
            self.dot1agcfmstackentry.parent = self
            self.dot1agcfmstackentry.name = 'dot1agcfmstackentry'


        class Dot1agCfmStackEntry(object):
            """
            The Stack table entry
            \*\*NOTE\: this object is deprecated due to re\-indexing of the 
            	table.
            
            .. attribute:: dot1agcfmstackdirection
            
            	Direction in which the MP faces on the Bridge Port \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`Dot1agCfmMpDirection_Enum <ydk.models.ieee8021.IEEE8021_CFM_MIB.Dot1agCfmMpDirection_Enum>`
            
            .. attribute:: dot1agcfmstackifindex
            
            	This object represents the  Bridge Port or aggregated port on which MEPs or MHFs might be configured.  Upon a restart of the system, the system SHALL, if necessary, change the value of this variable, and  rearrange the dot1agCfmStackTable, so that it indexes the entry in the interface table with the same value of ifAlias that it indexed before the system restart.  If no such entry exists, then the system SHALL delete all entries in the dot1agCfmStackTable with the interface index. \*\*NOTE\: this object is deprecated due to re\-indexing of 	the table. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1agcfmstackmdlevel
            
            	MD Level of the Maintenance Point. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: dot1agcfmstackvlanidornone
            
            	VLAN ID to which the MP is attached, or 0, if none. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: dot1agcfmstackmacaddress
            
            	MAC address of the MP. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1agcfmstackmaindex
            
            	The index of the MA in the dot1agCfmMaNetTable and dot1agCfmMaCompTable to which the MP is associated, or 0, if none. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmstackmdindex
            
            	The index of the Maintenance Domain in the dot1agCfmMdTable to which the MP is associated, or 0, if none
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1agcfmstackmepid
            
            	If an MEP is configured, the MEPID, else 0
            	**type**\: int
            
            	**range:** 0..8191
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmstackdirection = None
                self.dot1agcfmstackifindex = None
                self.dot1agcfmstackmdlevel = None
                self.dot1agcfmstackvlanidornone = None
                self.dot1agcfmstackmacaddress = None
                self.dot1agcfmstackmaindex = None
                self.dot1agcfmstackmdindex = None
                self.dot1agcfmstackmepid = None

            @property
            def _common_path(self):
                if self.dot1agcfmstackdirection is None:
                    raise YPYDataValidationError('Key property dot1agcfmstackdirection is None')
                if self.dot1agcfmstackifindex is None:
                    raise YPYDataValidationError('Key property dot1agcfmstackifindex is None')
                if self.dot1agcfmstackmdlevel is None:
                    raise YPYDataValidationError('Key property dot1agcfmstackmdlevel is None')
                if self.dot1agcfmstackvlanidornone is None:
                    raise YPYDataValidationError('Key property dot1agcfmstackvlanidornone is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmStackTable/IEEE8021-CFM-MIB:dot1agCfmStackEntry[IEEE8021-CFM-MIB:dot1agCfmStackDirection = ' + str(self.dot1agcfmstackdirection) + '][IEEE8021-CFM-MIB:dot1agCfmStackifIndex = ' + str(self.dot1agcfmstackifindex) + '][IEEE8021-CFM-MIB:dot1agCfmStackMdLevel = ' + str(self.dot1agcfmstackmdlevel) + '][IEEE8021-CFM-MIB:dot1agCfmStackVlanIdOrNone = ' + str(self.dot1agcfmstackvlanidornone) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmstackdirection is not None:
                    return True

                if self.dot1agcfmstackifindex is not None:
                    return True

                if self.dot1agcfmstackmdlevel is not None:
                    return True

                if self.dot1agcfmstackvlanidornone is not None:
                    return True

                if self.dot1agcfmstackmacaddress is not None:
                    return True

                if self.dot1agcfmstackmaindex is not None:
                    return True

                if self.dot1agcfmstackmdindex is not None:
                    return True

                if self.dot1agcfmstackmepid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmStackTable.Dot1agCfmStackEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmStackTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmstackentry is not None:
                for child_ref in self.dot1agcfmstackentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmStackTable']['meta_info']


    class Dot1agCfmVlanTable(object):
        """
        This table defines the association of VIDs into VLANs.  There
        is an entry in this table, for each component of the bridge,
        for each VID that is\:
            a) a VID belonging to a VLAN associated with more than
               one VID; and
            b) not the Primary VLAN of that VID.
        The entry in this table contains the Primary VID of the VLAN.
        
        By default, this table is empty, meaning that every VID is
        the Primary VID of a single\-VID VLAN.
        
        VLANs that are associated with only one VID SHOULD NOT have
        an entry in this table.
        
        The writable objects in this table need to be persistent
        upon reboot or restart of a device.
        \*\*NOTE\: this object is deprecated due to re\-indexing of the 
        	table.
        
        .. attribute:: dot1agcfmvlanentry
        
        	The VLAN table entry. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
        	**type**\: list of :py:class:`Dot1agCfmVlanEntry <ydk.models.ieee8021.IEEE8021_CFM_MIB.IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry>`
        
        

        """

        _prefix = 'ieee8021-cfm'
        _revision = '2008-10-15'

        def __init__(self):
            self.parent = None
            self.dot1agcfmvlanentry = YList()
            self.dot1agcfmvlanentry.parent = self
            self.dot1agcfmvlanentry.name = 'dot1agcfmvlanentry'


        class Dot1agCfmVlanEntry(object):
            """
            The VLAN table entry.
            \*\*NOTE\: this object is deprecated due to re\-indexing of the 
            	table.
            
            .. attribute:: dot1agcfmvlancomponentid
            
            	The bridge component within the system to which the information in this dot1agCfmVlanEntry applies.  If the system is not a Bridge, or if only one component is present in the Bridge, then this variable (index) MUST be equal to 1. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: dot1agcfmvlanvid
            
            	This is a VLAN ID belonging to a VLAN that is associated with more than one VLAN ID, and this is not the Primary VID of the VLAN. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: dot1agcfmvlanprimaryvid
            
            	This is the Primary VLAN ID of the VLAN with which this entry's dot1agCfmVlanVid is associated.  This value MUST not equal the value of dot1agCfmVlanVid. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: dot1agcfmvlanrowstatus
            
            	The status of the row.  The writable columns in a row can not be changed if the row is active. All columns MUST have a valid value before a row can be activated. \*\*NOTE\: this object is deprecated due to re\-indexing of the  	table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'ieee8021-cfm'
            _revision = '2008-10-15'

            def __init__(self):
                self.parent = None
                self.dot1agcfmvlancomponentid = None
                self.dot1agcfmvlanvid = None
                self.dot1agcfmvlanprimaryvid = None
                self.dot1agcfmvlanrowstatus = None

            @property
            def _common_path(self):
                if self.dot1agcfmvlancomponentid is None:
                    raise YPYDataValidationError('Key property dot1agcfmvlancomponentid is None')
                if self.dot1agcfmvlanvid is None:
                    raise YPYDataValidationError('Key property dot1agcfmvlanvid is None')

                return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmVlanTable/IEEE8021-CFM-MIB:dot1agCfmVlanEntry[IEEE8021-CFM-MIB:dot1agCfmVlanComponentId = ' + str(self.dot1agcfmvlancomponentid) + '][IEEE8021-CFM-MIB:dot1agCfmVlanVid = ' + str(self.dot1agcfmvlanvid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot1agcfmvlancomponentid is not None:
                    return True

                if self.dot1agcfmvlanvid is not None:
                    return True

                if self.dot1agcfmvlanprimaryvid is not None:
                    return True

                if self.dot1agcfmvlanrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
                return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmVlanTable.Dot1agCfmVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB/IEEE8021-CFM-MIB:dot1agCfmVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot1agcfmvlanentry is not None:
                for child_ref in self.dot1agcfmvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
            return meta._meta_table['IEEE8021CFMMIB.Dot1agCfmVlanTable']['meta_info']

    @property
    def _common_path(self):

        return '/IEEE8021-CFM-MIB:IEEE8021-CFM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.dot1agcfmconfigerrorlisttable is not None and self.dot1agcfmconfigerrorlisttable._has_data():
            return True

        if self.dot1agcfmconfigerrorlisttable is not None and self.dot1agcfmconfigerrorlisttable.is_presence():
            return True

        if self.dot1agcfmdefaultmd is not None and self.dot1agcfmdefaultmd._has_data():
            return True

        if self.dot1agcfmdefaultmd is not None and self.dot1agcfmdefaultmd.is_presence():
            return True

        if self.dot1agcfmdefaultmdtable is not None and self.dot1agcfmdefaultmdtable._has_data():
            return True

        if self.dot1agcfmdefaultmdtable is not None and self.dot1agcfmdefaultmdtable.is_presence():
            return True

        if self.dot1agcfmltrtable is not None and self.dot1agcfmltrtable._has_data():
            return True

        if self.dot1agcfmltrtable is not None and self.dot1agcfmltrtable.is_presence():
            return True

        if self.dot1agcfmmacomptable is not None and self.dot1agcfmmacomptable._has_data():
            return True

        if self.dot1agcfmmacomptable is not None and self.dot1agcfmmacomptable.is_presence():
            return True

        if self.dot1agcfmmameplisttable is not None and self.dot1agcfmmameplisttable._has_data():
            return True

        if self.dot1agcfmmameplisttable is not None and self.dot1agcfmmameplisttable.is_presence():
            return True

        if self.dot1agcfmmanettable is not None and self.dot1agcfmmanettable._has_data():
            return True

        if self.dot1agcfmmanettable is not None and self.dot1agcfmmanettable.is_presence():
            return True

        if self.dot1agcfmmd is not None and self.dot1agcfmmd._has_data():
            return True

        if self.dot1agcfmmd is not None and self.dot1agcfmmd.is_presence():
            return True

        if self.dot1agcfmmdtable is not None and self.dot1agcfmmdtable._has_data():
            return True

        if self.dot1agcfmmdtable is not None and self.dot1agcfmmdtable.is_presence():
            return True

        if self.dot1agcfmmepdbtable is not None and self.dot1agcfmmepdbtable._has_data():
            return True

        if self.dot1agcfmmepdbtable is not None and self.dot1agcfmmepdbtable.is_presence():
            return True

        if self.dot1agcfmmeptable is not None and self.dot1agcfmmeptable._has_data():
            return True

        if self.dot1agcfmmeptable is not None and self.dot1agcfmmeptable.is_presence():
            return True

        if self.dot1agcfmstacktable is not None and self.dot1agcfmstacktable._has_data():
            return True

        if self.dot1agcfmstacktable is not None and self.dot1agcfmstacktable.is_presence():
            return True

        if self.dot1agcfmvlantable is not None and self.dot1agcfmvlantable._has_data():
            return True

        if self.dot1agcfmvlantable is not None and self.dot1agcfmvlantable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ieee8021._meta import _IEEE8021_CFM_MIB as meta
        return meta._meta_table['IEEE8021CFMMIB']['meta_info']


