""" CISCO_TC 

This module defines textual conventions used throughout
cisco enterprise mibs.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CiscoAlarmSeverity_Enum(Enum):
    """
    CiscoAlarmSeverity_Enum

    Represents the perceived alarm severity associated
    with a service or safety affecting condition and/or
    event.  These are based on ITU severities, except
    that info(7) is added.
    
        cleared(1) \-
            Indicates a previous alarm condition has been
            cleared.  It is not required (unless specifically
            stated elsewhere on a case by case basis) that an
            alarm condition that has been cleared will produce
            a notification or other event containing an
            alarm severity with this value.
    
        indeterminate(2) \-
            Indicates that the severity level cannot be
            determined. 
    
        critical(3) \-
            Indicates that a service or safety affecting
            condition has occurred and an immediate
            corrective action is required.
    
        major(4) \-
            Indicates that a service affecting condition has
            occurred and an urgent corrective action is
            required.
    
        minor(5) \-
            Indicates the existence of a non\-service affecting
            condition and that corrective action should be
            taken in order to prevent a more serious (for
            example, service or safety affecting) condition.
    
        warning(6) \-
            Indicates the detection of a potential or impending
            service or safety affecting condition, before any
            significant effects have been felt.
    
        info(7) \-
            Indicates an alarm condition that does not
            meet any other severity definition.  This can
            include important, but non\-urgent, notices or
            informational events.

    """

    CLEARED = 1

    INDETERMINATE = 2

    CRITICAL = 3

    MAJOR = 4

    MINOR = 5

    WARNING = 6

    INFO = 7


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['CiscoAlarmSeverity_Enum']


class CiscoLocationClass_Enum(Enum):
    """
    CiscoLocationClass_Enum

    An enumerated value which provides an indication of
    the general location type of a particular physical and/or
    logical interface.
    chassis \- a system framework for mounting one or more 
              shelves/slots/cards.
    shelf \- a cabinet that holds one or more slots.
    slot \-  card or subSlot holder.
    subSlot \- daughter\-card holder.
    port \- a physical port (e.g., a DS1 or DS3 physical port).
    subPort \- a logical port on a physical port (e.g., a DS1 
              subPort on a DS3 physical port).
    channel \- a logical interface (e.g., a DS0 channel, signaling
              channel, ATM port, other virtual interfaces).
    subChannel \- a sub\-channel on a logical interface.

    """

    CHASSIS = 1

    SHELF = 2

    SLOT = 3

    SUBSLOT = 4

    PORT = 5

    SUBPORT = 6

    CHANNEL = 7

    SUBCHANNEL = 8


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['CiscoLocationClass_Enum']


class CiscoNetworkProtocol_Enum(Enum):
    """
    CiscoNetworkProtocol_Enum

    Represents the different types of network layer protocols.

    """

    IP = 1

    DECNET = 2

    PUP = 3

    CHAOS = 4

    XNS = 5

    X121 = 6

    APPLETALK = 7

    CLNS = 8

    LAT = 9

    VINES = 10

    CONS = 11

    APOLLO = 12

    STUN = 13

    NOVELL = 14

    QLLC = 15

    SNAPSHOT = 16

    ATMILMI = 17

    BSTUN = 18

    X25PVC = 19

    IPV6 = 20

    CDM = 21

    NBF = 22

    BPXIGX = 23

    CLNSPFX = 24

    HTTP = 25

    UNKNOWN = 65535


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['CiscoNetworkProtocol_Enum']


class CiscoPortListRange_Enum(Enum):
    """
    CiscoPortListRange_Enum

    Indicates the port range.
    
    oneto2K(1) indicates that the port number range is
    from 1 to 2048.
    
    twoKto4K(2) indicates that the port number range is
    from 2049 to 4096.
    
    fourKto6K(3) indicates that the port number range is
    from 4097 to 6144.
    
    sixKto8K(4) indicates that the port number range is
    from 6145 to 8192.
    
    eightKto10K(5) indicates that the port number range is
    from 8193 to 10240.
    
    tenKto12K(6) indicates that the port number range is
    from 10241 to 12288.
    
    twelveKto14K(7) indicates that the port number range is
    from 12289 to 14336.
    
    fourteenKto16K(8) indicates that the port number range is
    from 14337 to 16384.
    
    When an object is defined with this textual convention,
    it must be accompanied by an object of CiscoPortList
    syntax.

    """

    ONETO2K = 1

    TWOKTO4K = 2

    FOURKTO6K = 3

    SIXKTO8K = 4

    EIGHTKTO10K = 5

    TENKTO12K = 6

    TWELVEKTO14K = 7

    FOURTEENKTO16K = 8


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['CiscoPortListRange_Enum']


class CiscoRowOperStatus_Enum(Enum):
    """
    CiscoRowOperStatus_Enum

    Represents the operational status of an table entry.
    This textual convention allows explicitly representing
    the states of rows dependent on rows in other tables.
    
    active(1) \-
        Indicates this entry's RowStatus is active
        and the RowStatus for each dependency is active.
    
    activeDependencies(2) \-
        Indicates that the RowStatus for each dependency
        is active, but the entry's RowStatus is not active.
    
    inactiveDependency(3) \-
        Indicates that the RowStatus for at least one
        dependency is not active.
    
    missingDependency(4) \-
        Indicates that at least one dependency does
        not exist in it's table.

    """

    ACTIVE = 1

    ACTIVEDEPENDENCIES = 2

    INACTIVEDEPENDENCY = 3

    MISSINGDEPENDENCY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['CiscoRowOperStatus_Enum']


class IfOperStatusReason_Enum(Enum):
    """
    IfOperStatusReason_Enum

    The cause of current operational state of the
    interface.
    
    GLOSSARY\:
    
            BB        \- Buffer\-to\-Buffer.
    
    BB\_Credit \- Buffer\-to\-Buffer credit, a link level flow
                control mechanism.
    
    B\_Port    \- A Fibre Channel, Bridging port.
    
    BPDU      \- Bridge Protocol Data Unit.
    
    CDP       \- Cisco Discovery Protocol.
    
    Class F   \- A connectionless service with notification on 
                non\-delivery between E\_Ports, used for control, 
                coordination, and configuration of the Fabric.
    
    Class N   \- Refers to any class of service (different types
                of frame delivery services) other than Class F.
    
    E\_D\_TOV   \- Error Detect Timeout Value.
    
    ENM       \- Egress Non\-Multicast.
    
    ELP       \- Exchange Link Parameter.
    
    E\-mode    \- A fibre channel port providing E\_Port 
                functionality. 
    
    E\_Port    \- A Fabric Expansion Port.  
    
    EPP       \- Exchange Peer Parameters.
    
    ESC       \- Exchange Switch Capabilities.
    
    Fabric    \- The set of physically connected fibre channel
                switches.
    
    FEX       \- Fabric EXtender.
    
    FC\-FS     \- Fibre Channel Framing and Signaling.
    
    FCIP      \- Fibre Channel over IP protocol.
    
    FCID      \- Fibre Channel Domain ID.
    
    FCOE      \- Fibre Channel Over Ethernet.
    
    FCOT      \- Fibre channel optical transmitter.
    
    FC\-PH     \- The Fibre Channel Physical and Signaling 
                standard.
    
    FCSP      \- Fibre Channel Security Protocol. 
    
    Fibre Channel \- The primary protocol for building SANs. 
    
    FICON     \- An I\\O protocol used between IBM (and compatible) 
                mainframes and storage.
    
    FLOGI     \- Fabric Login, used by a node port to establish a
                session with the fabric.
    
    GBIC      \- Gigabit Interface Converter; a removable 
                transceiver module permitting Fibre Channel and 
                Gigabit Ethernet physical\-layer transport.
    
    Interconnect\_Ports \- Switch Ports that assume either the
                E\_Port or B\_Port mode are generally referred to 
                as Interconnect\_Ports.
    
    LACP      \- Link Access Control Protocol.
    
    LIP       \- Loop Initialization Primitive sequence.
    
    LR        \- Link Reset, the FC\-PH defined primitive sequence 
                used to initiate a link reset.
    
    MTU       \- Maximun transmission unit. 
    
    NOS       \- Not Operational Sequence, the FC\-PH defined 
                primitive sequence to indicate that the 
                transmitting port has detected a link failure (or)
                offline condition.
    
    VIC       \- Virtual Interface Card.
    
    VPC       \- Virtual Port Channel.
    
    NPIV      \- N Port Identifier Virtualization.
    
    NPV       \- NPort Virtualizer.
    
    Nx\_Port   \- A Fiber Channel Node Port. 
    
    OLS       \- Offline Sequence, the FC\-PH defined primitive 
                sequence to indicate that the port is entering
                into offline state.
    
    OHMS      \- Online Health Management System.
    
    PMON      \- Port Monitor.
    
    R\_A\_TOV   \- Resource Allocation Timeout Value.
    
    RCF       \- Reconfigure Fabric. 
    
    Rxbbcredit \- Receive BB credit value configured for 
                 a FC interface.
    
    SAN       \- Storage Area Network; a network linking computing 
                devices to disk or tape arrays and other devices 
                over Fibre Channel.
    
    SIF       \- Service Information Field.
    
    SDM       \- Security Device Manager.
    
    SDP       \- Secure Device Provisioning.
    
    SFP       \- Small Formfactor Pluggable.
    
    TE\_Port   \- Trunking E\_Port.
    
    TOV       \- Time out value.
    
    UDLD      \- Uni Directional Link Detection.
    
    VDC       \- Virtual Device Context.
    
    VEM       \- Virtual Ethernet Module.
    
    VFC       \- Virtual Fibre Channel.
    
    VRF       \- VPN Routing and Forwarding.
    
    VSAN      \- Virtual Storage Area Network.
    
    WWN       \- World Wide Name.
    
    xE\_Port   \- A Fiber channel port that can assume either 
                E\_Port or TE\_Port mode.
    
    The enumerated values which provides the cause of the current
    operational state of the interface are,
    
       'other(1)' \- reasons other than defined here.
    
       'none(2)' \- no failure.
    
       'hwFailure(3)' \- hardware failure.  
    
       'loopbackDiagFailure(4)' \- loopback diagnostics failure.
    
       'errorDisabled(5)' \- the port is not operational due to 
           some error conditions that require administrative 
           attention.
    
       'swFailure(6)' \- software failure.
    
       'linkFailure(7)' \- physical link failure.
    
       'offline(8)' \-  physical link is in offline state as 
           defined in the FC\-FS standards.
    
       'nonParticipating(9)' \- during loop initialization, the 
           port is not allowed to participate in loop operations.
    
       'initializing(10)' \- port is being initialized. 
    
       'vsanInactive(11)'\- port VSAN is inactive. The port becomes 
           operational again when the port VSAN is active. 
    
       'adminDown(12)' \- ifAdminStatus is 'down'.
    
       'channelAdminDown(13)' \- this port is a member of a port 
           channel and that port channel's ifAdminStatus is 
           'down'. 
    
       'channelOperSuspended(14)' \- this port is a member of a 
           port channel and its operational parameters are 
           incompatible with the port channel parameters.  
    
       'channelConfigurationInProgress(15)' \- this port is 
           undergoing a port channel configuration.
    
       'rcfInProgress(16)' \- an isolated xE\_port is transmitting 
           an reconfigure fabric, requesting a disruptive 
           reconfiguration in an attempt to build a single, 
           non\-isolated fabric. Only the Interconnect\_Ports can 
           become isolated. 
    
       'elpFailureIsolation(17)' \- during a port initialization 
           the prospective Interconnect\_Ports find incompatible 
           link parameters.
    
       'escFailureIsolation(18) \- during a port initialization the 
           prospective Interconnect\_Ports are unable to proceed 
           with initialization as a result of ESC.
    
       'domainOverlapIsolation(19)' \- there is a overlap in 
           domains while attempting to connect two existing 
           fabrics.
    
       'domainAddrAssignFailureIsolation(20)' \- the elected 
           principal switch is not capable of performing domain 
           address manager functions so no Nx\_port traffic can be 
           forwarded across switches, hence all Interconnect\_Ports 
           in the switch are isolated.
    
       'domainOtherSideEportIsolation(21)' \- the peer E\_port is 
           isolated.
    
       'domainInvalidRcfReceived(22)' \- invalid RCF received.
    
       'domainManagerDisabled(23) \- domain manager is disabled.
    
       'zoneMergeFailureIsolation(24)' \- the two Interconnect\_Ports 
           cannot merge zoning configuration after having exchanged 
           merging request for zoning.
    
       'vsanMismatchIsolation(25)' \- this VSAN is not configured 
           on both sides of a trunk port.
    
       'parentDown(26)' \- the physical port to which this interface 
           is bound is down.
    
       'srcPortNotBound(27)'\- no source port is specified for this 
           interface.
    
       'interfaceRemoved(28)' \- interface is being removed.
    
       'fcotNotPresent(29)' \- FCOT (GBIC) not present.
    
       'fcotVendorNotSupported(30)' \- FCOT (GBIC) vendor is not 
           supported. 
    
       'incompatibleAdminMode(31)' \- port administrative mode is 
           incompatible with port capabilities. 
    
       'incompatibleAdminSpeed(32)' \- port speed is incompatible 
           with port capabilities. 
    
       'suspendedByMode(33)' \- port that belongs to a port channel
           is suspended due to incompatible operational mode.
    
       'suspendedBySpeed(34)' \- port that belongs to a port channel
           is suspended due to incompatible operational speed.
    
       'suspendedByWwn(35)' \- port that belongs to a port channel 
           is suspended due to incompatible remote switch WWN.
    
       'domainMaxReTxFailure(36)' \- domain manager failure after 
           maximum retries.
    
       'eppFailure(37)' \- trunk negotiation protocol failure after 
           maximum retries.
    
       'portVsanMismatchIsolation(38)' \- an attempt is made to 
           connect two switches using non\-trunking ports having 
           different port VSANs. 
    
       'loopbackIsolation(39)' \- port is connected to another port 
           in the same switch.
    
       'upgradeInProgress(40)' \- linecard upgrade in progress.
    
       'incompatibleAdminRxBbCredit(41)' \- receive BB credit is 
           incompatible.
    
       'incompatibleAdminRxBufferSize(42)' \- receive buffer size 
           is incompatible.
    
       'portChannelMembersDown(43)' \- no operational members.
    
       'zoneRemoteNoRespIsolation(44)' \- isolation due to remote 
           zone server not responding.
    
       'firstPortUpAsEport(45)' \- in a over subscribed line card, 
           when the first port in a group is up in E\-mode, other 
           ports in that group cannot be brought up.
    
       'firstPortNotUp(46)' \- in a over subscribed line card, 
           first port cannot be brought up in E\-mode when the 
           other ports in the group are up.
    
       'peerFcipPortClosedConnection(47)' \- port went down because 
           peer FCIP port closed TCP connection.    
    
       'peerFcipPortResetConnection(48)' \- port went down because 
           the TCP connection was reset by the peer FCIP port.
    
       'fcipPortMaxReTx(49)' \- FCIP port went down due to maximum 
           TCP re\-transmissions reached the configured limit.
    
       'fcipPortKeepAliveTimerExpire(50)' \- FCIP port went down 
           due to TCP keep alive timer expired.
    
       'fcipPortPersistTimerExpire(51)' \- FCIP port went down due 
           to TCP persist timer expired.
    
       'fcipPortSrcLinkDown(52)' \- FCIP port went down due to 
           Ethernet link down.
    
       'fcipPortSrcAdminDown(53)' \- FCIP port went down because 
           the source Ethernet link was administratively shutdown.
    
       'fcipPortAdminCfgChange(54)' \- FCIP port went down due to 
           configuration change. 
    
       'fcipSrcPortRemoved(55)' \- FCIP port went down due to source 
           port removal.
    
       'fcipSrcModuleNotOnline(56)' \- FCIP port went down due to 
           source module not online.
    
       'invalidConfig(57)' \- this port has a misconfiguration with 
           respect to port channels.
    
       'portBindFailure(58)' \- port got isolated due to port bind 
           failure.  
    
       'portFabricBindFailure(59)' \- port got isolated due to 
           fabric bind failure.    
    
       'noCommonVsanIsolation(60)' \- trunk is isolated because 
           there are no common VSANs with peer.
    
       'ficonVsanDown (61)' \- FICON VSAN down.
    
       'invalidAttachment (62)' \-  invalid attachment.
    
       'portBlocked (63)' \- port blocked due to FICON. 
    
       'incomAdminRxBbCreditPerBuf (64)' \- disabled due to 
           incompatible administrative port rxbbcredit, 
           performance buffers.
    
       'tooManyInvalidFlogis (65)' \- suspended due to too many 
           invalid FLOGIs. 
    
       'deniedDueToPortBinding (66)' \- suspended due to port 
           binding.
    
       'elpFailureRevMismatch (67)' \- isolated for ELP failure due 
           to revision mismatch.
    
       'elpFailureClassFParamErr (68)' \- isolated for ELP failure 
           due to Class F parameter error.
    
       'elpFailureClassNParamErr (69)' \- isolated for ELP failure 
           due to Class N parameter error.
    
       'elpFailureUnknownFlowCtlCode (70)' \- isolated for ELP 
           failure due to invalid flow control code.
    
       'elpFailureInvalidFlowCtlParam (71)' \- isolated for ELP 
           failure due to invalid flow control parameter.
    
       'elpFailureInvalidPortName(72)' \- isolated for ELP failure 
           due to invalid port name.
    
       'elpFailureInvalidSwitchName (73)' \- isolated for ELP 
           failure due to invalid switch name.
    
       'elpFailureRatovEdtovMismatch (74)' \- isolated for ELP 
           failure due to R\_A\_TOV or E\_D\_TOV mismatch.
    
       'elpFailureLoopbackDetected (75)' \- isolated for ELP 
           failure due to loopback detected.
    
       'elpFailureInvalidTxBbCredit (76)' \- isolated for ELP 
           failure due to invalid transmit BB credit.
    
       'elpFailureInvalidPayloadSize (77)' \- isolated for ELP 
           failure due to invalid payload size.
    
       'bundleMisCfg (78)' \- misconfiguration in port channel 
           membership detected.
    
       'bitErrRuntimeThreshExceeded (79)' \- bit error rate too 
           high. It has exceeded the run time threshold.
    
       'linkFailLinkReset (80)' \- link failure due to link reset.
    
       'linkFailPortInitFail (81)' \- link failure due to port 
           initialization failure.
    
       'linkFailPortUnusable (82)' \- link failure due to port 
           unusable.
    
       'linkFailLossOfSignal (83)' \- link failure due to loss of 
           signal. 
    
       'linkFailLossOfSync (84)' \- link failure due to loss of 
           sync.
    
       'linkFailNosRcvd (85)' \- link failure due to non\-operational 
           sequences received.
    
       'linkFailOLSRcvd (86)' \- link failure due to offline 
           sequences received.
    
       'linkFailDebounceTimeout (87)' \- link failure due to 
           re\-negotiation failed.
    
       'linkFailLrRcvd (88)' \- link failure when link reset(LR) 
           operation fails due to non\-empty receive queue.  
    
       'linkFailCreditLoss (89)' \- link failure due to excessive 
           credit loss indications.
    
       'linkFailRxQOverflow (90)' \- link failure due to receive 
           queue overflow.
    
       'linkFailTooManyInterrupts (91)' \- link failure due to 
           excessive port interrupts.
    
       'linkFailLipRcvdBb (92)' \- link failure when loop 
           initialization(LIP) operation fails due to non empty 
           receive queue.
    
       'linkFailBbCreditLoss (93)' \- link failure when link 
           reset(LR) operation fails due to queue not empty.
    
       'linkFailOpenPrimSignalTimeout (94)' \- link failure due to
           open primitive signal timeout while receive queue
           not empty.
    
       'linkFailOpenPrimSignalReturned (95)' \- link failure due to
           open primitive signal returned while receive queue 
           not empty. 
    
       'linkFailLipF8Rcvd (96)' \- link failure due to F8 LIP 
           received.
    
       'linkFailLineCardPortShutdown (97)' \- link failure due to 
           port shutdown.
    
       'fcspAuthenFailure (98)' \- fibre channel security protocol 
           authorization fail.
    
       'fcotChecksumError (99)' \- FCOT SPROM checksum error. 
    
       'ohmsExtLoopbackTest (100)' \- link suspended due to external 
           loopback diagnostics failure.
    
       'invalidFabricBindExchange (101)' \- invalid fabric binding 
           exchange.
    
       'tovMismatch (102)' \- link isolation due to TOV mismatch.
    
       'ficonNotEnabled (103)' \- FICON not enabled.
    
       'ficonNoPortNumber (104)' \- no FICON port number.
    
       'ficonBeingEnabled (105)' \- FICON is being enabled.
    
       'ePortProhibited (106)' \- port down because FICON prohibit 
           mask in place for E/TE port.
    
       'portGracefulShutdown (107)' \- port has been shutdown 
           gracefully.
    
       'trunkNotFullyActive (108)' \- some of the VSANs which are 
           common with the peer are not up.
    
       'fabricBindingSwitchWwnNotFound (109)' \- peer switch WWN not 
           found in fabric binding active database.
    
       'fabricBindingDomainInvalid (110)' \- peer domain ID is 
           invalid in fabric binding active database.
    
       'fabricBindingDbMismatch (111)' \- fabric binding active 
           database mismatch with peer. 
    
       'fabricBindingNoRspFromPeer (112)' \- fabric binding no 
           response from peer.
    
       'dpvmVsanSuspended (113)' \- dpvm vsan is suspended.
    
       'dpvmVsanNotFound (114)' \- dpvm vsan not found.
    
       'trackedPortDown (115)' \- port down because tracked
           port is down.
    
       'ecSuspendedOnLoop (116)' \- port suspended because extended
           BB credits are configured on loop port.
    
       'isolateBundleMisCfg (117)' \- port isolated due to bundle
           mis\-configuration.
    
       'noPeerBundleSupport (118)' \- peer port does not support
           bundle.
    
       'portBringupIsolation (119)' \- trunk port isolated during 
           bringup time.
    
       'domainNotAllowedIsolated (120)' \- port isolated due to
           domain not allowed.
    
       'virtualIvrDomainOverlapIsolation (121)' \- port isolated
                  due to virtual IVR domain overlap.
    
       'outOfService (122)' \- port is in out of service state.
    
       'portAuthFailed (123)' \- port has encountered an 802.1x 
        authentication failure.
    
       'bundleStandby (124)' \- port cannot be brought up in 
               a bundle, since the bundle has max members.
    
       'portConnectorTypeErr (125)' \- Error in the port connector 
        type (SFP).
    
       'errorDisabledReInitLmtReached (126)' \- the port is not 
        operational after trying to initialize the port multiple 
        times due to some erorrs.
    
       'ficonDupPortNum (127)' \- the ficon vsan has a duplicate 
        port number.
    
       'localRcf (128)' \- fcdomain applied a locally disruptive
        reconfiguration (the local domain became invalid; no 
        RCF frames have been sent outside the local switch).
    
        'twoSwitchesWithSameWWN (129)' \- merge attempt between
        VSANs containing the same WWN. If the user attempts to 
        merge two different VSANs and both have at least one 
        switch with the same WWN then the link in between the 
        VSANs is isolated.
    
        'invalidOtherSidePrincEFPReqRecd (130)' \- EFP request frame
        indicating a principal switch other than the locally 
        known one.
    
        'domainOther (131)' \- other domain manager reasons not 
        defined here.
    
        'elpFailureAllZeroPeerWWNRcvd (132)' \- isolated for ELP 
        failure due to peer WWN is received with all zeros.
    
        'preferredPathIsolation (133)' \- port isolated due to
         preferred path not able to program the routes.
    
        'fcRedirectIsolation (134)' \- port isolated due to
                FC Redirect not being able to program routes.
    
         'portActLicenseNotAvailable (135)' \- port not brought up
            due to lack of port activation licenses.
    
         'sdmIsolation (136)' \- port isolated due to SDM 
            (Security Device Manager) not being
            able to program routes.
    
         'fcidAllocationFailed (137)' \- port down due to failure
            in FCID (Fibre Channel Domain ID) allocation.   
    
         'externallyDisabled (138)' \- port externally disabled.
    
         'unavailableNPVUpstreamPort (139)' \- NPV 
                 (NPort Virtualizer) upstream port not available.
    
         'unavailableNPVPrefUpstreamPort (140)' \- NPV 
            (NPort Virtualizer) preferred 
            upstream port not available.
    
         'sfpReadError (141)' \- the port is not operational due to 
                 SFP (Small Formfactor Pluggable) read error.
    
         'stickyDownOnLinkFailure (142)' \- the port is 
                 not operational due to link failure 
                 in the sticky down mode.
    
         'tooManyLinkFlapsErr (143)' \- too many link flaps 
                 on the port in a short interval.
    
         'unidirectionalUDLD (144)' \- unidirectional UDLD 
            (Uni Directional Link Detection) detected.
    
         'txRxLoopUDLD (145)' \- UDLD (Uni Directional 
                 Link Detection) Tx Rx loop.
    
         'neighborMismatchUDLD (146)' \- UDLD 
            (Uni Directional Link Detection) neighbor mismatch.
    
         'authzPending (147)' \- authorization pending.
    
         'hotStdbyInBundle (148)' \- hot standby in bundle.
    
         'incompleteConfig (149)' \- all parameters on the port 
                          have not been configured.
    
         'incompleteTunnelCfg (150)' \- incomplete tunnel config.
    
         'hwProgrammingFailed (151)' \- hardware programming failed.
    
         'tunnelDstUnreachable (152)' \- no route to 
                 tunnel destination address.
    
         'suspendByMtu (153)' \- MTU allocation failed.
    
         'sfpInvalid (154)' \- SFP (Small Formfactor Pluggable) 
            is not Cisco certified.
    
         'sfpAbsent (155)' \- SFP (Small Formfactor 
                 Pluggable) is absent.
    
        'portCapabilitiesUnknown (156)' \- the capabilities of the 
                port are unknown.
    
         'channelErrDisabled (157)' \- the port\-channel to which 
                 the port belongs is in error disabled state.
    
         'vrfMismatch (158)' \- Mismatch in source and transport VRF
                    (VPN Routing and Forwarding).
    
         'vrfForwardReferencing (159)' \- Forward referencing 
                 transport VRF (VPN Routing and Forwarding).
    
         'dupTunnelConfigDetected (160)' \- two tunnel interfaces 
                 with same configuration is not allowed.
    
         'primaryVLANDown (161)' \- primary VLAN is in down state.
    
         'vrfUnusable (162)' \- VRF (VPN Routing and Forwarding) 
                is unusable.
    
         'errDisableHandShkFailure (163)' \- port is not operational 
                         due to an internal handshake failure.
    
         'errDisabledBPDUGuard (164)' \- BPDUGuard 
         (Bridge Protocol Data Unit) triggered 
         error disable on the port.
    
         'dot1xSecViolationErrDisabled (165)' \- error disabled 
               due to dot1x security violation.
    
         'emptyEchoUDLD (166)' \- UDLD (Uni Directional 
                 Link Detection) empty echo.
    
         'vfTaggingCapErr (167)' \- VF Tagging capability 
                 mismatch error.
    
         'portDisabled (168)' \- Port disabled.
    
         'tunnelModeNotConfigured (169)' \- Tunnel Mode is not 
                         configured.
    
         'tunnelSrcNotConfigured (170)' \- Tunnel Source is not 
                         configured. 
    
         'tunnelDstNotConfigured (171)' \- Tunnel Destination 
                         is not configured.
    
         'tunnelUnableToResolveSrcIP (172)' \- Unable to resolve 
                         tunnel source IP address. 
    
         'tunnelUnableToResolveDstIP (173)' \- Unable to resolve 
                         tunnel destination IP address.
    
         'tunnelVrfDown (174)' \- Tunnel VRF down.
    
         'sifAdminDown (175)' \- SIF (Service Information Field) 
            is admin down.
    
         'phyIntfDown (176)' \- Physical interface is down.
    
         'ifSifLimitExceeded (177)' \- Interface SIF 
         (Service Information Field)limit is exceeded.
    
         'sifHoldDown (178)' \- SIF (Service Information Field) 
                 hold down.
    
         'noFcoe (179)' \- No FCOE (Fibre Channel Over Ethernet) 
            configuration.
    
         'dcxCompatMismatch (180)' \- DCX Compatibility Mismatch.
    
         'isolateBundleLimitExceeded (181)' \- Isolation due to 
                     bundle limit exceeded.
    
         'sifNotBound (182)' \- SIF (ervice Information Field) 
                 is not bound.
    
         'errDisabledLacpMiscfg (183)' \- Error Disabled due to 
                 LACP (Link Access Control Protocol) misconfig.
    
         'satFabricIfDown (184)' \- Satellite fabric interface down.
    
         'invalidSatFabricIf (185)' \- Invalid satellite fabric 
                         interface.
    
         'noRemoteChassis (186)' \- No remote chassis.
    
         'vicEnableNotReceived (187)' \- VIC enable not received.
    
         'vicDisableReceived (188)' \- VIC disable received.
    
         'vlanVsanMappingNotEnabled (189)' \- VLAN VSAN mapping not 
                         enabled.
    
         'stpNotFwdingInFcoeMappedVlan (190)' \- STP not forwarding 
                         in FCOE Mapped Vlan.
    
         'moduleOffline (191)' \- Module Offline.
    
         'udldAggModeLinkFailure (192)' \- UDLD (Uni Directional Link
            Detection) aggresive mode link failure.
    
         'stpInconsVpcPeerDisabled (193)' \- STP inconsistent 
                 VPC (Virtual Port Channel) peer disabled. 
    
         'setPortStateFailed (194)' \- Set port state failed.
    
         'suspendedByVpc (195)' \- Suspended by VPC 
                 (Virtual Port Channel).
    
         'vpcCfgInProgress (196)' \- VPC (Virtual Port Channel)
             configuration in progress.
    
         'vpcPeerLinkDown (197)' \- VPC (Virtual Port Channel)
             peer link down.
    
         'vpcNoRspFromPeer (198)' \- VPC (Virtual Port Channel) 
            no response from peer.
    
         'protoPortSuspend (199)' \- Proto port suspend.
    
         'tunnelSrcDown (200)' \- Tunnel source down.
    
         'cdpInfoUnavailable (201)' \- CDP 
         (Cisco Discovery Protocol) information unavailable.
    
         'fexSfpInvalid (202)' \- FEX (Fabric Extender) 
         SFP (Small Formfactor Pluggable) invalid.
    
         'errDisabledIpConflict (203)' \- Error Disabled due to IP
                          conflict.
    
         'fcotClkRateMismatch (204)' \- FCOT CLK rate mismatch.
    
         'portGuardTrustSecViolation (205)' \- Error disabled due 
             to port guard (Cisco Trusted Security Violation).
    
         'sdpTimeout (206)' \- SDP (Secure Device Provisioning)
                  timeout.
    
         'satIncompatTopo (207)' \- Satellite incompatible topology.
    
         'waitForFlogi (208)' \- Wait for FLOGI.
    
         'satNotConfigured (209)' \- Satellite not configured.
    
         'npivNotEnabledInUpstream (210)' \- NPIV (N Port Identifier
            Virtualization) not enabled in upstream.
    
         'vsanMismatchWithUpstreamSwPort (211)' \- VSAN 
                 mismatch with upstream switch port.
    
         'portGuardBitErrRate (212)' \- Error disabled due to port 
                         guard (Bit Error Rate).
    
         'portGuardSigLoss (213)' \- Error disabled due to 
                 port guard (Signal Loss).
    
         'portGuardSyncLoss (214)' \- Error disabled due to port 
                         guard (Sync Loss).
    
         'portGuardLinkReset (215)' \- Error disabled due to port
                         guard (Link Reset).
    
         'portGuardCreditLoss (216)' \- Error disabled due to port
                         guard (Credit Loss).
    
         'ipQosMgrPolicyAppFailure (217)' \- IP QOS Manager policy 
                      application failure.
    
         'pauseRateLimitErrDisabled (218)' \- Port error disabled due
                                    to pause rate limit condition.
    
         'lstGrpUplinkDown (219)' \- EthPM LSTGRP downstream link 
                         down due to upstream link down.
    
         'stickyDnLinkFailure (220)' \- Port kept in error disabled
                                     state due to Link Failure.
    
         'routerMacFailure (221)' \- Router MAC failure.
    
         'dcxMultipleMsapIds (222)' \- Port error disabled due to
                                    multiple MSAP IDs (DCX).
    
         'dcxHundredPdusRcvdNoAck (223)' \- Hundred PDUs received 
                         without ACK (DCX).
    
         'enmSatIncompatibleUplink (224)' \- Satellite Incompatible 
                         Uplink.
    
         'enmLoopDetected (225)' \- Loop Detected (ENM).
    
         'nonStickyExternallyDisabled (226)' \- Disabled by VPD 
                         Manager with shut/no shut allowed.
    
         'nonStickyExternallyDisabled (227)' \- Sub\-group ID 
                         not assigned.
    
         'vemUnlicensed (228)' \- VEM Unlicensed.
    
         'profileNotFound (229)' \- Profile not found.
    
         'nonExistentVlan (230)' \- VLAN does not exist.
    
         'vlanInvalidType (231)' \- Invalid VLAN type.
    
         'vlanDown (232)' \- VLAN down.
    
         'vpcPeerUpgrade (233)' \- VPC Peer Upgrade.
    
         'ipQosDcbxpCompatFailure (234)' \- IPQOS DCBXP compatibility
                       failure.
    
         'nonCiscoHbaVfTag (235)' \- Error Disabled due to Non\-Cisco 
                         HBA VF Tag.
    
         'domainIdConfigMismatch (236)' \- Domain ID config mismatch.
    
         'sfpSpeedMismatch (237)' \- SFP (Small Formfactor Pluggable)
             speed mismatch.
         'xcvrInitializing (238)' \- Transceiver initializing.
    
         'xcvrAbsent (239)' \- Transceiver absent.
    
         'xcvrInvalid (240)' \- Transceiver invalid.
    
         'vfcBindingInvalid (241)' \- Invalid VFC Binding.
    
         'vlanNotFcoeEnabled (242)' \- VLAN down due to FCOE 
                         disabled.
    
         'pvlanNativeVlanErr (243)' \- Private VLAN 
                         Native VLAN error.
    
         'ethL2VlanDown (244)' \- Ethernet L2 VLAN down.
    
         'ethIntfInvalidBinding (245)' \- Invalid Binding 
                 to Ethernet Interface.
    
         'pmonFailure (246)' \- PMON Failure.
    
         'l3NotReady (247)' \- L3 not ready.
    
         'speedMismatch (248)' \- Speed Mismatch.
    
         'flowControlMismatch (249)' \- Flow Control Mismatch.
    
         'vdcMode (250)' \- VDC mode 
    
         'suspendedDueToMinLinks (251)' \- Suspended due 
                         to Min Links.
    
         'enmPinFailLinkDown (252)' \- ENM Pin Fail Link Down.
    
         'inactiveM1PortFpathActiveVlan (253)' \- Inactive M1 Port
                                F Path Active VLAN.
    
         'parentPortDown (254)' \- Parent Port Down.
    
         'moduleRemoved (255)' \- Module Removed.
    
         'corePortMct (256)' \- Core Port MCT.
    
         'nonCorePortMct (257)' \- Non Core port MCT.
    
         'ficonInorderNotActive (258)'\- FICON Inorder Not Active.
    
         'invalidEncapsulation (259)' \- Invalid Encapsulation.
    
         'modemLineDeasserted (260)' \- Modem line Deasserted.
    
         'ipSecHndshkInProgress (261)' \- IP Sec Handshake in 
                                 progress.
    
         'sfpEthCompliantErr (262)' \- Sfp Ethernet compliant error.
    
         'cellularModemUnattached (263)' \- Cellular Modem 
                         unattached.
    
         'outOfGlblRxBuffers (264)' \- Out of Global Rx Buffers.
    
         'sfpFcCompliantErr (265)' \- Sfp Fc compliant Error.
    
         'ethIntfNotLicensed (266)' \- Ethernet Interface Not 
                                         Licensed.
    
         'domainIdsInvalid (267)' \- Domain IDs Invalid.
    
         'fabricNameInvalid (268)' \- Fabric Name Invalid.

    """

    OTHER = 1

    NONE = 2

    HWFAILURE = 3

    LOOPBACKDIAGFAILURE = 4

    ERRORDISABLED = 5

    SWFAILURE = 6

    LINKFAILURE = 7

    OFFLINE = 8

    NONPARTICIPATING = 9

    INITIALIZING = 10

    VSANINACTIVE = 11

    ADMINDOWN = 12

    CHANNELADMINDOWN = 13

    CHANNELOPERSUSPENDED = 14

    CHANNELCONFIGURATIONINPROGRESS = 15

    RCFINPROGRESS = 16

    ELPFAILUREISOLATION = 17

    ESCFAILUREISOLATION = 18

    DOMAINOVERLAPISOLATION = 19

    DOMAINADDRASSIGNFAILUREISOLATION = 20

    DOMAINOTHERSIDEEPORTISOLATION = 21

    DOMAININVALIDRCFRECEIVED = 22

    DOMAINMANAGERDISABLED = 23

    ZONEMERGEFAILUREISOLATION = 24

    VSANMISMATCHISOLATION = 25

    PARENTDOWN = 26

    SRCPORTNOTBOUND = 27

    INTERFACEREMOVED = 28

    FCOTNOTPRESENT = 29

    FCOTVENDORNOTSUPPORTED = 30

    INCOMPATIBLEADMINMODE = 31

    INCOMPATIBLEADMINSPEED = 32

    SUSPENDEDBYMODE = 33

    SUSPENDEDBYSPEED = 34

    SUSPENDEDBYWWN = 35

    DOMAINMAXRETXFAILURE = 36

    EPPFAILURE = 37

    PORTVSANMISMATCHISOLATION = 38

    LOOPBACKISOLATION = 39

    UPGRADEINPROGRESS = 40

    INCOMPATIBLEADMINRXBBCREDIT = 41

    INCOMPATIBLEADMINRXBUFFERSIZE = 42

    PORTCHANNELMEMBERSDOWN = 43

    ZONEREMOTENORESPISOLATION = 44

    FIRSTPORTUPASEPORT = 45

    FIRSTPORTNOTUP = 46

    PEERFCIPPORTCLOSEDCONNECTION = 47

    PEERFCIPPORTRESETCONNECTION = 48

    FCIPPORTMAXRETX = 49

    FCIPPORTKEEPALIVETIMEREXPIRE = 50

    FCIPPORTPERSISTTIMEREXPIRE = 51

    FCIPPORTSRCLINKDOWN = 52

    FCIPPORTSRCADMINDOWN = 53

    FCIPPORTADMINCFGCHANGE = 54

    FCIPSRCPORTREMOVED = 55

    FCIPSRCMODULENOTONLINE = 56

    INVALIDCONFIG = 57

    PORTBINDFAILURE = 58

    PORTFABRICBINDFAILURE = 59

    NOCOMMONVSANISOLATION = 60

    FICONVSANDOWN = 61

    INVALIDATTACHMENT = 62

    PORTBLOCKED = 63

    INCOMADMINRXBBCREDITPERBUF = 64

    TOOMANYINVALIDFLOGIS = 65

    DENIEDDUETOPORTBINDING = 66

    ELPFAILUREREVMISMATCH = 67

    ELPFAILURECLASSFPARAMERR = 68

    ELPFAILURECLASSNPARAMERR = 69

    ELPFAILUREUNKNOWNFLOWCTLCODE = 70

    ELPFAILUREINVALIDFLOWCTLPARAM = 71

    ELPFAILUREINVALIDPORTNAME = 72

    ELPFAILUREINVALIDSWITCHNAME = 73

    ELPFAILURERATOVEDTOVMISMATCH = 74

    ELPFAILURELOOPBACKDETECTED = 75

    ELPFAILUREINVALIDTXBBCREDIT = 76

    ELPFAILUREINVALIDPAYLOADSIZE = 77

    BUNDLEMISCFG = 78

    BITERRRUNTIMETHRESHEXCEEDED = 79

    LINKFAILLINKRESET = 80

    LINKFAILPORTINITFAIL = 81

    LINKFAILPORTUNUSABLE = 82

    LINKFAILLOSSOFSIGNAL = 83

    LINKFAILLOSSOFSYNC = 84

    LINKFAILNOSRCVD = 85

    LINKFAILOLSRCVD = 86

    LINKFAILDEBOUNCETIMEOUT = 87

    LINKFAILLRRCVD = 88

    LINKFAILCREDITLOSS = 89

    LINKFAILRXQOVERFLOW = 90

    LINKFAILTOOMANYINTERRUPTS = 91

    LINKFAILLIPRCVDBB = 92

    LINKFAILBBCREDITLOSS = 93

    LINKFAILOPENPRIMSIGNALTIMEOUT = 94

    LINKFAILOPENPRIMSIGNALRETURNED = 95

    LINKFAILLIPF8RCVD = 96

    LINKFAILLINECARDPORTSHUTDOWN = 97

    FCSPAUTHENFAILURE = 98

    FCOTCHECKSUMERROR = 99

    OHMSEXTLOOPBACKTEST = 100

    INVALIDFABRICBINDEXCHANGE = 101

    TOVMISMATCH = 102

    FICONNOTENABLED = 103

    FICONNOPORTNUMBER = 104

    FICONBEINGENABLED = 105

    EPORTPROHIBITED = 106

    PORTGRACEFULSHUTDOWN = 107

    TRUNKNOTFULLYACTIVE = 108

    FABRICBINDINGSWITCHWWNNOTFOUND = 109

    FABRICBINDINGDOMAININVALID = 110

    FABRICBINDINGDBMISMATCH = 111

    FABRICBINDINGNORSPFROMPEER = 112

    DPVMVSANSUSPENDED = 113

    DPVMVSANNOTFOUND = 114

    TRACKEDPORTDOWN = 115

    ECSUSPENDEDONLOOP = 116

    ISOLATEBUNDLEMISCFG = 117

    NOPEERBUNDLESUPPORT = 118

    PORTBRINGUPISOLATION = 119

    DOMAINNOTALLOWEDISOLATED = 120

    VIRTUALIVRDOMAINOVERLAPISOLATION = 121

    OUTOFSERVICE = 122

    PORTAUTHFAILED = 123

    BUNDLESTANDBY = 124

    PORTCONNECTORTYPEERR = 125

    ERRORDISABLEDREINITLMTREACHED = 126

    FICONDUPPORTNUM = 127

    LOCALRCF = 128

    TWOSWITCHESWITHSAMEWWN = 129

    INVALIDOTHERSIDEPRINCEFPREQRECD = 130

    DOMAINOTHER = 131

    ELPFAILUREALLZEROPEERWWNRCVD = 132

    PREFERREDPATHISOLATION = 133

    FCREDIRECTISOLATION = 134

    PORTACTLICENSENOTAVAILABLE = 135

    SDMISOLATION = 136

    FCIDALLOCATIONFAILED = 137

    EXTERNALLYDISABLED = 138

    UNAVAILABLENPVUPSTREAMPORT = 139

    UNAVAILABLENPVPREFUPSTREAMPORT = 140

    SFPREADERROR = 141

    STICKYDOWNONLINKFAILURE = 142

    TOOMANYLINKFLAPSERR = 143

    UNIDIRECTIONALUDLD = 144

    TXRXLOOPUDLD = 145

    NEIGHBORMISMATCHUDLD = 146

    AUTHZPENDING = 147

    HOTSTDBYINBUNDLE = 148

    INCOMPLETECONFIG = 149

    INCOMPLETETUNNELCFG = 150

    HWPROGRAMMINGFAILED = 151

    TUNNELDSTUNREACHABLE = 152

    SUSPENDBYMTU = 153

    SFPINVALID = 154

    SFPABSENT = 155

    PORTCAPABILITIESUNKNOWN = 156

    CHANNELERRDISABLED = 157

    VRFMISMATCH = 158

    VRFFORWARDREFERENCING = 159

    DUPTUNNELCONFIGDETECTED = 160

    PRIMARYVLANDOWN = 161

    VRFUNUSABLE = 162

    ERRDISABLEHANDSHKFAILURE = 163

    ERRDISABLEDBPDUGUARD = 164

    DOT1XSECVIOLATIONERRDISABLED = 165

    EMPTYECHOUDLD = 166

    VFTAGGINGCAPERR = 167

    PORTDISABLED = 168

    TUNNELMODENOTCONFIGURED = 169

    TUNNELSRCNOTCONFIGURED = 170

    TUNNELDSTNOTCONFIGURED = 171

    TUNNELUNABLETORESOLVESRCIP = 172

    TUNNELUNABLETORESOLVEDSTIP = 173

    TUNNELVRFDOWN = 174

    SIFADMINDOWN = 175

    PHYINTFDOWN = 176

    IFSIFLIMITEXCEEDED = 177

    SIFHOLDDOWN = 178

    NOFCOE = 179

    DCXCOMPATMISMATCH = 180

    ISOLATEBUNDLELIMITEXCEEDED = 181

    SIFNOTBOUND = 182

    ERRDISABLEDLACPMISCFG = 183

    SATFABRICIFDOWN = 184

    INVALIDSATFABRICIF = 185

    NOREMOTECHASSIS = 186

    VICENABLENOTRECEIVED = 187

    VICDISABLERECEIVED = 188

    VLANVSANMAPPINGNOTENABLED = 189

    STPNOTFWDINGINFCOEMAPPEDVLAN = 190

    MODULEOFFLINE = 191

    UDLDAGGMODELINKFAILURE = 192

    STPINCONSVPCPEERDISABLED = 193

    SETPORTSTATEFAILED = 194

    SUSPENDEDBYVPC = 195

    VPCCFGINPROGRESS = 196

    VPCPEERLINKDOWN = 197

    VPCNORSPFROMPEER = 198

    PROTOPORTSUSPEND = 199

    TUNNELSRCDOWN = 200

    CDPINFOUNAVAILABLE = 201

    FEXSFPINVALID = 202

    ERRDISABLEDIPCONFLICT = 203

    FCOTCLKRATEMISMATCH = 204

    PORTGUARDTRUSTSECVIOLATION = 205

    SDPTIMEOUT = 206

    SATINCOMPATTOPO = 207

    WAITFORFLOGI = 208

    SATNOTCONFIGURED = 209

    NPIVNOTENABLEDINUPSTREAM = 210

    VSANMISMATCHWITHUPSTREAMSWPORT = 211

    PORTGUARDBITERRRATE = 212

    PORTGUARDSIGLOSS = 213

    PORTGUARDSYNCLOSS = 214

    PORTGUARDLINKRESET = 215

    PORTGUARDCREDITLOSS = 216

    IPQOSMGRPOLICYAPPFAILURE = 217

    PAUSERATELIMITERRDISABLED = 218

    LSTGRPUPLINKDOWN = 219

    STICKYDNLINKFAILURE = 220

    ROUTERMACFAILURE = 221

    DCXMULTIPLEMSAPIDS = 222

    DCXHUNDREDPDUSRCVDNOACK = 223

    ENMSATINCOMPATIBLEUPLINK = 224

    ENMLOOPDETECTED = 225

    NONSTICKYEXTERNALLYDISABLED = 226

    SUBGROUPIDNOTASSIGNED = 227

    VEMUNLICENSED = 228

    PROFILENOTFOUND = 229

    NONEXISTENTVLAN = 230

    VLANINVALIDTYPE = 231

    VLANDOWN = 232

    VPCPEERUPGRADE = 233

    IPQOSDCBXPCOMPATFAILURE = 234

    NONCISCOHBAVFTAG = 235

    DOMAINIDCONFIGMISMATCH = 236

    SFPSPEEDMISMATCH = 237

    XCVRINITIALIZING = 238

    XCVRABSENT = 239

    XCVRINVALID = 240

    VFCBINDINGINVALID = 241

    VLANNOTFCOEENABLED = 242

    PVLANNATIVEVLANERR = 243

    ETHL2VLANDOWN = 244

    ETHINTFINVALIDBINDING = 245

    PMONFAILURE = 246

    L3NOTREADY = 247

    SPEEDMISMATCH = 248

    FLOWCONTROLMISMATCH = 249

    VDCMODE = 250

    SUSPENDEDDUETOMINLINKS = 251

    ENMPINFAILLINKDOWN = 252

    INACTIVEM1PORTFPATHACTIVEVLAN = 253

    PARENTPORTDOWN = 254

    MODULEREMOVED = 255

    COREPORTMCT = 256

    NONCOREPORTMCT = 257

    FICONINORDERNOTACTIVE = 258

    INVALIDENCAPSULATION = 259

    MODEMLINEDEASSERTED = 260

    IPSECHNDSHKINPROGRESS = 261

    SFPETHCOMPLIANTERR = 262

    CELLULARMODEMUNATTACHED = 263

    OUTOFGLBLRXBUFFERS = 264

    SFPFCCOMPLIANTERR = 265

    ETHINTFNOTLICENSED = 266

    DOMAINIDSINVALID = 267

    FABRICNAMEINVALID = 268


    @staticmethod
    def _meta_info():
        from ydk.models.tc._meta import _CISCO_TC as meta
        return meta._meta_table['IfOperStatusReason_Enum']


class CiscoCosList_Bits(FixedBitsDict):
    """
    CiscoCosList_Bits

    Each bit represents a CoS value (0 through 7).
    Keys are:- cos7 , cos6 , cos5 , cos4 , cos3 , cos2 , cos1 , cos0

    """

    def __init__(self):
        self._dictionary = { 
            'cos7':False,
            'cos6':False,
            'cos5':False,
            'cos4':False,
            'cos3':False,
            'cos2':False,
            'cos1':False,
            'cos0':False,
        }
        self._pos_map = { 
            'cos7':7,
            'cos6':6,
            'cos5':5,
            'cos4':4,
            'cos3':3,
            'cos2':2,
            'cos1':1,
            'cos0':0,
        }


