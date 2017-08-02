""" CISCO_TC 

This module defines textual conventions used throughout
cisco enterprise mibs.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ciscoalarmseverity(Enum):
    """
    Ciscoalarmseverity

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

    .. data:: cleared = 1

    .. data:: indeterminate = 2

    .. data:: critical = 3

    .. data:: major = 4

    .. data:: minor = 5

    .. data:: warning = 6

    .. data:: info = 7

    """

    cleared = Enum.YLeaf(1, "cleared")

    indeterminate = Enum.YLeaf(2, "indeterminate")

    critical = Enum.YLeaf(3, "critical")

    major = Enum.YLeaf(4, "major")

    minor = Enum.YLeaf(5, "minor")

    warning = Enum.YLeaf(6, "warning")

    info = Enum.YLeaf(7, "info")


class Ciscolocationclass(Enum):
    """
    Ciscolocationclass

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

    .. data:: chassis = 1

    .. data:: shelf = 2

    .. data:: slot = 3

    .. data:: subSlot = 4

    .. data:: port = 5

    .. data:: subPort = 6

    .. data:: channel = 7

    .. data:: subChannel = 8

    """

    chassis = Enum.YLeaf(1, "chassis")

    shelf = Enum.YLeaf(2, "shelf")

    slot = Enum.YLeaf(3, "slot")

    subSlot = Enum.YLeaf(4, "subSlot")

    port = Enum.YLeaf(5, "port")

    subPort = Enum.YLeaf(6, "subPort")

    channel = Enum.YLeaf(7, "channel")

    subChannel = Enum.YLeaf(8, "subChannel")


class Cisconetworkprotocol(Enum):
    """
    Cisconetworkprotocol

    Represents the different types of network layer protocols.

    .. data:: ip = 1

    .. data:: decnet = 2

    .. data:: pup = 3

    .. data:: chaos = 4

    .. data:: xns = 5

    .. data:: x121 = 6

    .. data:: appletalk = 7

    .. data:: clns = 8

    .. data:: lat = 9

    .. data:: vines = 10

    .. data:: cons = 11

    .. data:: apollo = 12

    .. data:: stun = 13

    .. data:: novell = 14

    .. data:: qllc = 15

    .. data:: snapshot = 16

    .. data:: atmIlmi = 17

    .. data:: bstun = 18

    .. data:: x25pvc = 19

    .. data:: ipv6 = 20

    .. data:: cdm = 21

    .. data:: nbf = 22

    .. data:: bpxIgx = 23

    .. data:: clnsPfx = 24

    .. data:: http = 25

    .. data:: unknown = 65535

    """

    ip = Enum.YLeaf(1, "ip")

    decnet = Enum.YLeaf(2, "decnet")

    pup = Enum.YLeaf(3, "pup")

    chaos = Enum.YLeaf(4, "chaos")

    xns = Enum.YLeaf(5, "xns")

    x121 = Enum.YLeaf(6, "x121")

    appletalk = Enum.YLeaf(7, "appletalk")

    clns = Enum.YLeaf(8, "clns")

    lat = Enum.YLeaf(9, "lat")

    vines = Enum.YLeaf(10, "vines")

    cons = Enum.YLeaf(11, "cons")

    apollo = Enum.YLeaf(12, "apollo")

    stun = Enum.YLeaf(13, "stun")

    novell = Enum.YLeaf(14, "novell")

    qllc = Enum.YLeaf(15, "qllc")

    snapshot = Enum.YLeaf(16, "snapshot")

    atmIlmi = Enum.YLeaf(17, "atmIlmi")

    bstun = Enum.YLeaf(18, "bstun")

    x25pvc = Enum.YLeaf(19, "x25pvc")

    ipv6 = Enum.YLeaf(20, "ipv6")

    cdm = Enum.YLeaf(21, "cdm")

    nbf = Enum.YLeaf(22, "nbf")

    bpxIgx = Enum.YLeaf(23, "bpxIgx")

    clnsPfx = Enum.YLeaf(24, "clnsPfx")

    http = Enum.YLeaf(25, "http")

    unknown = Enum.YLeaf(65535, "unknown")


class Ciscoportlistrange(Enum):
    """
    Ciscoportlistrange

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

    .. data:: oneto2k = 1

    .. data:: twoKto4K = 2

    .. data:: fourKto6K = 3

    .. data:: sixKto8K = 4

    .. data:: eightKto10K = 5

    .. data:: tenKto12K = 6

    .. data:: twelveKto14K = 7

    .. data:: fourteenKto16K = 8

    """

    oneto2k = Enum.YLeaf(1, "oneto2k")

    twoKto4K = Enum.YLeaf(2, "twoKto4K")

    fourKto6K = Enum.YLeaf(3, "fourKto6K")

    sixKto8K = Enum.YLeaf(4, "sixKto8K")

    eightKto10K = Enum.YLeaf(5, "eightKto10K")

    tenKto12K = Enum.YLeaf(6, "tenKto12K")

    twelveKto14K = Enum.YLeaf(7, "twelveKto14K")

    fourteenKto16K = Enum.YLeaf(8, "fourteenKto16K")


class Ciscorowoperstatus(Enum):
    """
    Ciscorowoperstatus

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

    .. data:: active = 1

    .. data:: activeDependencies = 2

    .. data:: inactiveDependency = 3

    .. data:: missingDependency = 4

    """

    active = Enum.YLeaf(1, "active")

    activeDependencies = Enum.YLeaf(2, "activeDependencies")

    inactiveDependency = Enum.YLeaf(3, "inactiveDependency")

    missingDependency = Enum.YLeaf(4, "missingDependency")


class Ifoperstatusreason(Enum):
    """
    Ifoperstatusreason

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

    .. data:: other = 1

    .. data:: none = 2

    .. data:: hwFailure = 3

    .. data:: loopbackDiagFailure = 4

    .. data:: errorDisabled = 5

    .. data:: swFailure = 6

    .. data:: linkFailure = 7

    .. data:: offline = 8

    .. data:: nonParticipating = 9

    .. data:: initializing = 10

    .. data:: vsanInactive = 11

    .. data:: adminDown = 12

    .. data:: channelAdminDown = 13

    .. data:: channelOperSuspended = 14

    .. data:: channelConfigurationInProgress = 15

    .. data:: rcfInProgress = 16

    .. data:: elpFailureIsolation = 17

    .. data:: escFailureIsolation = 18

    .. data:: domainOverlapIsolation = 19

    .. data:: domainAddrAssignFailureIsolation = 20

    .. data:: domainOtherSideEportIsolation = 21

    .. data:: domainInvalidRcfReceived = 22

    .. data:: domainManagerDisabled = 23

    .. data:: zoneMergeFailureIsolation = 24

    .. data:: vsanMismatchIsolation = 25

    .. data:: parentDown = 26

    .. data:: srcPortNotBound = 27

    .. data:: interfaceRemoved = 28

    .. data:: fcotNotPresent = 29

    .. data:: fcotVendorNotSupported = 30

    .. data:: incompatibleAdminMode = 31

    .. data:: incompatibleAdminSpeed = 32

    .. data:: suspendedByMode = 33

    .. data:: suspendedBySpeed = 34

    .. data:: suspendedByWWN = 35

    .. data:: domainMaxReTxFailure = 36

    .. data:: eppFailure = 37

    .. data:: portVsanMismatchIsolation = 38

    .. data:: loopbackIsolation = 39

    .. data:: upgradeInProgress = 40

    .. data:: incompatibleAdminRxBbCredit = 41

    .. data:: incompatibleAdminRxBufferSize = 42

    .. data:: portChannelMembersDown = 43

    .. data:: zoneRemoteNoRespIsolation = 44

    .. data:: firstPortUpAsEport = 45

    .. data:: firstPortNotUp = 46

    .. data:: peerFCIPPortClosedConnection = 47

    .. data:: peerFCIPPortResetConnection = 48

    .. data:: fcipPortMaxReTx = 49

    .. data:: fcipPortKeepAliveTimerExpire = 50

    .. data:: fcipPortPersistTimerExpire = 51

    .. data:: fcipPortSrcLinkDown = 52

    .. data:: fcipPortSrcAdminDown = 53

    .. data:: fcipPortAdminCfgChange = 54

    .. data:: fcipSrcPortRemoved = 55

    .. data:: fcipSrcModuleNotOnline = 56

    .. data:: invalidConfig = 57

    .. data:: portBindFailure = 58

    .. data:: portFabricBindFailure = 59

    .. data:: noCommonVsanIsolation = 60

    .. data:: ficonVsanDown = 61

    .. data:: invalidAttachment = 62

    .. data:: portBlocked = 63

    .. data:: incomAdminRxBbCreditPerBuf = 64

    .. data:: tooManyInvalidFlogis = 65

    .. data:: deniedDueToPortBinding = 66

    .. data:: elpFailureRevMismatch = 67

    .. data:: elpFailureClassFParamErr = 68

    .. data:: elpFailureClassNParamErr = 69

    .. data:: elpFailureUnknownFlowCtlCode = 70

    .. data:: elpFailureInvalidFlowCtlParam = 71

    .. data:: elpFailureInvalidPortName = 72

    .. data:: elpFailureInvalidSwitchName = 73

    .. data:: elpFailureRatovEdtovMismatch = 74

    .. data:: elpFailureLoopbackDetected = 75

    .. data:: elpFailureInvalidTxBbCredit = 76

    .. data:: elpFailureInvalidPayloadSize = 77

    .. data:: bundleMisCfg = 78

    .. data:: bitErrRuntimeThreshExceeded = 79

    .. data:: linkFailLinkReset = 80

    .. data:: linkFailPortInitFail = 81

    .. data:: linkFailPortUnusable = 82

    .. data:: linkFailLossOfSignal = 83

    .. data:: linkFailLossOfSync = 84

    .. data:: linkFailNosRcvd = 85

    .. data:: linkFailOLSRcvd = 86

    .. data:: linkFailDebounceTimeout = 87

    .. data:: linkFailLrRcvd = 88

    .. data:: linkFailCreditLoss = 89

    .. data:: linkFailRxQOverflow = 90

    .. data:: linkFailTooManyInterrupts = 91

    .. data:: linkFailLipRcvdBb = 92

    .. data:: linkFailBbCreditLoss = 93

    .. data:: linkFailOpenPrimSignalTimeout = 94

    .. data:: linkFailOpenPrimSignalReturned = 95

    .. data:: linkFailLipF8Rcvd = 96

    .. data:: linkFailLineCardPortShutdown = 97

    .. data:: fcspAuthenfailure = 98

    .. data:: fcotChecksumError = 99

    .. data:: ohmsExtLoopbackTest = 100

    .. data:: invalidFabricBindExchange = 101

    .. data:: tovMismatch = 102

    .. data:: ficonNotEnabled = 103

    .. data:: ficonNoPortNumber = 104

    .. data:: ficonBeingEnabled = 105

    .. data:: ePortProhibited = 106

    .. data:: portGracefulShutdown = 107

    .. data:: trunkNotFullyActive = 108

    .. data:: fabricBindingSwitchWwnNotFound = 109

    .. data:: fabricBindingDomainInvalid = 110

    .. data:: fabricBindingDbMismatch = 111

    .. data:: fabricBindingNoRspFromPeer = 112

    .. data:: dpvmVsanSuspended = 113

    .. data:: dpvmVsanNotFound = 114

    .. data:: trackedPortDown = 115

    .. data:: ecSuspendedOnLoop = 116

    .. data:: isolateBundleMisCfg = 117

    .. data:: noPeerBundleSupport = 118

    .. data:: portBringupIsolation = 119

    .. data:: domainNotAllowedIsolated = 120

    .. data:: virtualIvrDomainOverlapIsolation = 121

    .. data:: outOfService = 122

    .. data:: portAuthFailed = 123

    .. data:: bundleStandby = 124

    .. data:: portConnectorTypeErr = 125

    .. data:: errorDisabledReInitLmtReached = 126

    .. data:: ficonDupPortNum = 127

    .. data:: localRcf = 128

    .. data:: twoSwitchesWithSameWWN = 129

    .. data:: invalidOtherSidePrincEFPReqRecd = 130

    .. data:: domainOther = 131

    .. data:: elpFailureAllZeroPeerWWNRcvd = 132

    .. data:: preferredPathIsolation = 133

    .. data:: fcRedirectIsolation = 134

    .. data:: portActLicenseNotAvailable = 135

    .. data:: sdmIsolation = 136

    .. data:: fcidAllocationFailed = 137

    .. data:: externallyDisabled = 138

    .. data:: unavailableNPVUpstreamPort = 139

    .. data:: unavailableNPVPrefUpstreamPort = 140

    .. data:: sfpReadError = 141

    .. data:: stickyDownOnLinkFailure = 142

    .. data:: tooManyLinkFlapsErr = 143

    .. data:: unidirectionalUDLD = 144

    .. data:: txRxLoopUDLD = 145

    .. data:: neighborMismatchUDLD = 146

    .. data:: authzPending = 147

    .. data:: hotStdbyInBundle = 148

    .. data:: incompleteConfig = 149

    .. data:: incompleteTunnelCfg = 150

    .. data:: hwProgrammingFailed = 151

    .. data:: tunnelDstUnreachable = 152

    .. data:: suspendByMtu = 153

    .. data:: sfpInvalid = 154

    .. data:: sfpAbsent = 155

    .. data:: portCapabilitiesUnknown = 156

    .. data:: channelErrDisabled = 157

    .. data:: vrfMismatch = 158

    .. data:: vrfForwardReferencing = 159

    .. data:: dupTunnelConfigDetected = 160

    .. data:: primaryVLANDown = 161

    .. data:: vrfUnusable = 162

    .. data:: errDisableHandShkFailure = 163

    .. data:: errDisabledBPDUGuard = 164

    .. data:: dot1xSecViolationErrDisabled = 165

    .. data:: emptyEchoUDLD = 166

    .. data:: vfTaggingCapErr = 167

    .. data:: portDisabled = 168

    .. data:: tunnelModeNotConfigured = 169

    .. data:: tunnelSrcNotConfigured = 170

    .. data:: tunnelDstNotConfigured = 171

    .. data:: tunnelUnableToResolveSrcIP = 172

    .. data:: tunnelUnableToResolveDstIP = 173

    .. data:: tunnelVrfDown = 174

    .. data:: sifAdminDown = 175

    .. data:: phyIntfDown = 176

    .. data:: ifSifLimitExceeded = 177

    .. data:: sifHoldDown = 178

    .. data:: noFcoe = 179

    .. data:: dcxCompatMismatch = 180

    .. data:: isolateBundleLimitExceeded = 181

    .. data:: sifNotBound = 182

    .. data:: errDisabledLacpMiscfg = 183

    .. data:: satFabricIfDown = 184

    .. data:: invalidSatFabricIf = 185

    .. data:: noRemoteChassis = 186

    .. data:: vicEnableNotReceived = 187

    .. data:: vicDisableReceived = 188

    .. data:: vlanVsanMappingNotEnabled = 189

    .. data:: stpNotFwdingInFcoeMappedVlan = 190

    .. data:: moduleOffline = 191

    .. data:: udldAggModeLinkFailure = 192

    .. data:: stpInconsVpcPeerDisabled = 193

    .. data:: setPortStateFailed = 194

    .. data:: suspendedByVpc = 195

    .. data:: vpcCfgInProgress = 196

    .. data:: vpcPeerLinkDown = 197

    .. data:: vpcNoRspFromPeer = 198

    .. data:: protoPortSuspend = 199

    .. data:: tunnelSrcDown = 200

    .. data:: cdpInfoUnavailable = 201

    .. data:: fexSfpInvalid = 202

    .. data:: errDisabledIpConflict = 203

    .. data:: fcotClkRateMismatch = 204

    .. data:: portGuardTrustSecViolation = 205

    .. data:: sdpTimeout = 206

    .. data:: satIncompatTopo = 207

    .. data:: waitForFlogi = 208

    .. data:: satNotConfigured = 209

    .. data:: npivNotEnabledInUpstream = 210

    .. data:: vsanMismatchWithUpstreamSwPort = 211

    .. data:: portGuardBitErrRate = 212

    .. data:: portGuardSigLoss = 213

    .. data:: portGuardSyncLoss = 214

    .. data:: portGuardLinkReset = 215

    .. data:: portGuardCreditLoss = 216

    .. data:: ipQosMgrPolicyAppFailure = 217

    .. data:: pauseRateLimitErrDisabled = 218

    .. data:: lstGrpUplinkDown = 219

    .. data:: stickyDnLinkFailure = 220

    .. data:: routerMacFailure = 221

    .. data:: dcxMultipleMsapIds = 222

    .. data:: dcxHundredPdusRcvdNoAck = 223

    .. data:: enmSatIncompatibleUplink = 224

    .. data:: enmLoopDetected = 225

    .. data:: nonStickyExternallyDisabled = 226

    .. data:: subGroupIdNotAssigned = 227

    .. data:: vemUnlicensed = 228

    .. data:: profileNotFound = 229

    .. data:: nonExistentVlan = 230

    .. data:: vlanInvalidType = 231

    .. data:: vlanDown = 232

    .. data:: vpcPeerUpgrade = 233

    .. data:: ipQosDcbxpCompatFailure = 234

    .. data:: nonCiscoHbaVfTag = 235

    .. data:: domainIdConfigMismatch = 236

    .. data:: sfpSpeedMismatch = 237

    .. data:: xcvrInitializing = 238

    .. data:: xcvrAbsent = 239

    .. data:: xcvrInvalid = 240

    .. data:: vfcBindingInvalid = 241

    .. data:: vlanNotFcoeEnabled = 242

    .. data:: pvlanNativeVlanErr = 243

    .. data:: ethL2VlanDown = 244

    .. data:: ethIntfInvalidBinding = 245

    .. data:: pmonFailure = 246

    .. data:: l3NotReady = 247

    .. data:: speedMismatch = 248

    .. data:: flowControlMismatch = 249

    .. data:: vdcMode = 250

    .. data:: suspendedDueToMinLinks = 251

    .. data:: enmPinFailLinkDown = 252

    .. data:: inactiveM1PortFpathActiveVlan = 253

    .. data:: parentPortDown = 254

    .. data:: moduleRemoved = 255

    .. data:: corePortMct = 256

    .. data:: nonCorePortMct = 257

    .. data:: ficonInorderNotActive = 258

    .. data:: invalidEncapsulation = 259

    .. data:: modemLineDeasserted = 260

    .. data:: ipSecHndshkInProgress = 261

    .. data:: sfpEthCompliantErr = 262

    .. data:: cellularModemUnattached = 263

    .. data:: outOfGlblRxBuffers = 264

    .. data:: sfpFcCompliantErr = 265

    .. data:: ethIntfNotLicensed = 266

    .. data:: domainIdsInvalid = 267

    .. data:: fabricNameInvalid = 268

    """

    other = Enum.YLeaf(1, "other")

    none = Enum.YLeaf(2, "none")

    hwFailure = Enum.YLeaf(3, "hwFailure")

    loopbackDiagFailure = Enum.YLeaf(4, "loopbackDiagFailure")

    errorDisabled = Enum.YLeaf(5, "errorDisabled")

    swFailure = Enum.YLeaf(6, "swFailure")

    linkFailure = Enum.YLeaf(7, "linkFailure")

    offline = Enum.YLeaf(8, "offline")

    nonParticipating = Enum.YLeaf(9, "nonParticipating")

    initializing = Enum.YLeaf(10, "initializing")

    vsanInactive = Enum.YLeaf(11, "vsanInactive")

    adminDown = Enum.YLeaf(12, "adminDown")

    channelAdminDown = Enum.YLeaf(13, "channelAdminDown")

    channelOperSuspended = Enum.YLeaf(14, "channelOperSuspended")

    channelConfigurationInProgress = Enum.YLeaf(15, "channelConfigurationInProgress")

    rcfInProgress = Enum.YLeaf(16, "rcfInProgress")

    elpFailureIsolation = Enum.YLeaf(17, "elpFailureIsolation")

    escFailureIsolation = Enum.YLeaf(18, "escFailureIsolation")

    domainOverlapIsolation = Enum.YLeaf(19, "domainOverlapIsolation")

    domainAddrAssignFailureIsolation = Enum.YLeaf(20, "domainAddrAssignFailureIsolation")

    domainOtherSideEportIsolation = Enum.YLeaf(21, "domainOtherSideEportIsolation")

    domainInvalidRcfReceived = Enum.YLeaf(22, "domainInvalidRcfReceived")

    domainManagerDisabled = Enum.YLeaf(23, "domainManagerDisabled")

    zoneMergeFailureIsolation = Enum.YLeaf(24, "zoneMergeFailureIsolation")

    vsanMismatchIsolation = Enum.YLeaf(25, "vsanMismatchIsolation")

    parentDown = Enum.YLeaf(26, "parentDown")

    srcPortNotBound = Enum.YLeaf(27, "srcPortNotBound")

    interfaceRemoved = Enum.YLeaf(28, "interfaceRemoved")

    fcotNotPresent = Enum.YLeaf(29, "fcotNotPresent")

    fcotVendorNotSupported = Enum.YLeaf(30, "fcotVendorNotSupported")

    incompatibleAdminMode = Enum.YLeaf(31, "incompatibleAdminMode")

    incompatibleAdminSpeed = Enum.YLeaf(32, "incompatibleAdminSpeed")

    suspendedByMode = Enum.YLeaf(33, "suspendedByMode")

    suspendedBySpeed = Enum.YLeaf(34, "suspendedBySpeed")

    suspendedByWWN = Enum.YLeaf(35, "suspendedByWWN")

    domainMaxReTxFailure = Enum.YLeaf(36, "domainMaxReTxFailure")

    eppFailure = Enum.YLeaf(37, "eppFailure")

    portVsanMismatchIsolation = Enum.YLeaf(38, "portVsanMismatchIsolation")

    loopbackIsolation = Enum.YLeaf(39, "loopbackIsolation")

    upgradeInProgress = Enum.YLeaf(40, "upgradeInProgress")

    incompatibleAdminRxBbCredit = Enum.YLeaf(41, "incompatibleAdminRxBbCredit")

    incompatibleAdminRxBufferSize = Enum.YLeaf(42, "incompatibleAdminRxBufferSize")

    portChannelMembersDown = Enum.YLeaf(43, "portChannelMembersDown")

    zoneRemoteNoRespIsolation = Enum.YLeaf(44, "zoneRemoteNoRespIsolation")

    firstPortUpAsEport = Enum.YLeaf(45, "firstPortUpAsEport")

    firstPortNotUp = Enum.YLeaf(46, "firstPortNotUp")

    peerFCIPPortClosedConnection = Enum.YLeaf(47, "peerFCIPPortClosedConnection")

    peerFCIPPortResetConnection = Enum.YLeaf(48, "peerFCIPPortResetConnection")

    fcipPortMaxReTx = Enum.YLeaf(49, "fcipPortMaxReTx")

    fcipPortKeepAliveTimerExpire = Enum.YLeaf(50, "fcipPortKeepAliveTimerExpire")

    fcipPortPersistTimerExpire = Enum.YLeaf(51, "fcipPortPersistTimerExpire")

    fcipPortSrcLinkDown = Enum.YLeaf(52, "fcipPortSrcLinkDown")

    fcipPortSrcAdminDown = Enum.YLeaf(53, "fcipPortSrcAdminDown")

    fcipPortAdminCfgChange = Enum.YLeaf(54, "fcipPortAdminCfgChange")

    fcipSrcPortRemoved = Enum.YLeaf(55, "fcipSrcPortRemoved")

    fcipSrcModuleNotOnline = Enum.YLeaf(56, "fcipSrcModuleNotOnline")

    invalidConfig = Enum.YLeaf(57, "invalidConfig")

    portBindFailure = Enum.YLeaf(58, "portBindFailure")

    portFabricBindFailure = Enum.YLeaf(59, "portFabricBindFailure")

    noCommonVsanIsolation = Enum.YLeaf(60, "noCommonVsanIsolation")

    ficonVsanDown = Enum.YLeaf(61, "ficonVsanDown")

    invalidAttachment = Enum.YLeaf(62, "invalidAttachment")

    portBlocked = Enum.YLeaf(63, "portBlocked")

    incomAdminRxBbCreditPerBuf = Enum.YLeaf(64, "incomAdminRxBbCreditPerBuf")

    tooManyInvalidFlogis = Enum.YLeaf(65, "tooManyInvalidFlogis")

    deniedDueToPortBinding = Enum.YLeaf(66, "deniedDueToPortBinding")

    elpFailureRevMismatch = Enum.YLeaf(67, "elpFailureRevMismatch")

    elpFailureClassFParamErr = Enum.YLeaf(68, "elpFailureClassFParamErr")

    elpFailureClassNParamErr = Enum.YLeaf(69, "elpFailureClassNParamErr")

    elpFailureUnknownFlowCtlCode = Enum.YLeaf(70, "elpFailureUnknownFlowCtlCode")

    elpFailureInvalidFlowCtlParam = Enum.YLeaf(71, "elpFailureInvalidFlowCtlParam")

    elpFailureInvalidPortName = Enum.YLeaf(72, "elpFailureInvalidPortName")

    elpFailureInvalidSwitchName = Enum.YLeaf(73, "elpFailureInvalidSwitchName")

    elpFailureRatovEdtovMismatch = Enum.YLeaf(74, "elpFailureRatovEdtovMismatch")

    elpFailureLoopbackDetected = Enum.YLeaf(75, "elpFailureLoopbackDetected")

    elpFailureInvalidTxBbCredit = Enum.YLeaf(76, "elpFailureInvalidTxBbCredit")

    elpFailureInvalidPayloadSize = Enum.YLeaf(77, "elpFailureInvalidPayloadSize")

    bundleMisCfg = Enum.YLeaf(78, "bundleMisCfg")

    bitErrRuntimeThreshExceeded = Enum.YLeaf(79, "bitErrRuntimeThreshExceeded")

    linkFailLinkReset = Enum.YLeaf(80, "linkFailLinkReset")

    linkFailPortInitFail = Enum.YLeaf(81, "linkFailPortInitFail")

    linkFailPortUnusable = Enum.YLeaf(82, "linkFailPortUnusable")

    linkFailLossOfSignal = Enum.YLeaf(83, "linkFailLossOfSignal")

    linkFailLossOfSync = Enum.YLeaf(84, "linkFailLossOfSync")

    linkFailNosRcvd = Enum.YLeaf(85, "linkFailNosRcvd")

    linkFailOLSRcvd = Enum.YLeaf(86, "linkFailOLSRcvd")

    linkFailDebounceTimeout = Enum.YLeaf(87, "linkFailDebounceTimeout")

    linkFailLrRcvd = Enum.YLeaf(88, "linkFailLrRcvd")

    linkFailCreditLoss = Enum.YLeaf(89, "linkFailCreditLoss")

    linkFailRxQOverflow = Enum.YLeaf(90, "linkFailRxQOverflow")

    linkFailTooManyInterrupts = Enum.YLeaf(91, "linkFailTooManyInterrupts")

    linkFailLipRcvdBb = Enum.YLeaf(92, "linkFailLipRcvdBb")

    linkFailBbCreditLoss = Enum.YLeaf(93, "linkFailBbCreditLoss")

    linkFailOpenPrimSignalTimeout = Enum.YLeaf(94, "linkFailOpenPrimSignalTimeout")

    linkFailOpenPrimSignalReturned = Enum.YLeaf(95, "linkFailOpenPrimSignalReturned")

    linkFailLipF8Rcvd = Enum.YLeaf(96, "linkFailLipF8Rcvd")

    linkFailLineCardPortShutdown = Enum.YLeaf(97, "linkFailLineCardPortShutdown")

    fcspAuthenfailure = Enum.YLeaf(98, "fcspAuthenfailure")

    fcotChecksumError = Enum.YLeaf(99, "fcotChecksumError")

    ohmsExtLoopbackTest = Enum.YLeaf(100, "ohmsExtLoopbackTest")

    invalidFabricBindExchange = Enum.YLeaf(101, "invalidFabricBindExchange")

    tovMismatch = Enum.YLeaf(102, "tovMismatch")

    ficonNotEnabled = Enum.YLeaf(103, "ficonNotEnabled")

    ficonNoPortNumber = Enum.YLeaf(104, "ficonNoPortNumber")

    ficonBeingEnabled = Enum.YLeaf(105, "ficonBeingEnabled")

    ePortProhibited = Enum.YLeaf(106, "ePortProhibited")

    portGracefulShutdown = Enum.YLeaf(107, "portGracefulShutdown")

    trunkNotFullyActive = Enum.YLeaf(108, "trunkNotFullyActive")

    fabricBindingSwitchWwnNotFound = Enum.YLeaf(109, "fabricBindingSwitchWwnNotFound")

    fabricBindingDomainInvalid = Enum.YLeaf(110, "fabricBindingDomainInvalid")

    fabricBindingDbMismatch = Enum.YLeaf(111, "fabricBindingDbMismatch")

    fabricBindingNoRspFromPeer = Enum.YLeaf(112, "fabricBindingNoRspFromPeer")

    dpvmVsanSuspended = Enum.YLeaf(113, "dpvmVsanSuspended")

    dpvmVsanNotFound = Enum.YLeaf(114, "dpvmVsanNotFound")

    trackedPortDown = Enum.YLeaf(115, "trackedPortDown")

    ecSuspendedOnLoop = Enum.YLeaf(116, "ecSuspendedOnLoop")

    isolateBundleMisCfg = Enum.YLeaf(117, "isolateBundleMisCfg")

    noPeerBundleSupport = Enum.YLeaf(118, "noPeerBundleSupport")

    portBringupIsolation = Enum.YLeaf(119, "portBringupIsolation")

    domainNotAllowedIsolated = Enum.YLeaf(120, "domainNotAllowedIsolated")

    virtualIvrDomainOverlapIsolation = Enum.YLeaf(121, "virtualIvrDomainOverlapIsolation")

    outOfService = Enum.YLeaf(122, "outOfService")

    portAuthFailed = Enum.YLeaf(123, "portAuthFailed")

    bundleStandby = Enum.YLeaf(124, "bundleStandby")

    portConnectorTypeErr = Enum.YLeaf(125, "portConnectorTypeErr")

    errorDisabledReInitLmtReached = Enum.YLeaf(126, "errorDisabledReInitLmtReached")

    ficonDupPortNum = Enum.YLeaf(127, "ficonDupPortNum")

    localRcf = Enum.YLeaf(128, "localRcf")

    twoSwitchesWithSameWWN = Enum.YLeaf(129, "twoSwitchesWithSameWWN")

    invalidOtherSidePrincEFPReqRecd = Enum.YLeaf(130, "invalidOtherSidePrincEFPReqRecd")

    domainOther = Enum.YLeaf(131, "domainOther")

    elpFailureAllZeroPeerWWNRcvd = Enum.YLeaf(132, "elpFailureAllZeroPeerWWNRcvd")

    preferredPathIsolation = Enum.YLeaf(133, "preferredPathIsolation")

    fcRedirectIsolation = Enum.YLeaf(134, "fcRedirectIsolation")

    portActLicenseNotAvailable = Enum.YLeaf(135, "portActLicenseNotAvailable")

    sdmIsolation = Enum.YLeaf(136, "sdmIsolation")

    fcidAllocationFailed = Enum.YLeaf(137, "fcidAllocationFailed")

    externallyDisabled = Enum.YLeaf(138, "externallyDisabled")

    unavailableNPVUpstreamPort = Enum.YLeaf(139, "unavailableNPVUpstreamPort")

    unavailableNPVPrefUpstreamPort = Enum.YLeaf(140, "unavailableNPVPrefUpstreamPort")

    sfpReadError = Enum.YLeaf(141, "sfpReadError")

    stickyDownOnLinkFailure = Enum.YLeaf(142, "stickyDownOnLinkFailure")

    tooManyLinkFlapsErr = Enum.YLeaf(143, "tooManyLinkFlapsErr")

    unidirectionalUDLD = Enum.YLeaf(144, "unidirectionalUDLD")

    txRxLoopUDLD = Enum.YLeaf(145, "txRxLoopUDLD")

    neighborMismatchUDLD = Enum.YLeaf(146, "neighborMismatchUDLD")

    authzPending = Enum.YLeaf(147, "authzPending")

    hotStdbyInBundle = Enum.YLeaf(148, "hotStdbyInBundle")

    incompleteConfig = Enum.YLeaf(149, "incompleteConfig")

    incompleteTunnelCfg = Enum.YLeaf(150, "incompleteTunnelCfg")

    hwProgrammingFailed = Enum.YLeaf(151, "hwProgrammingFailed")

    tunnelDstUnreachable = Enum.YLeaf(152, "tunnelDstUnreachable")

    suspendByMtu = Enum.YLeaf(153, "suspendByMtu")

    sfpInvalid = Enum.YLeaf(154, "sfpInvalid")

    sfpAbsent = Enum.YLeaf(155, "sfpAbsent")

    portCapabilitiesUnknown = Enum.YLeaf(156, "portCapabilitiesUnknown")

    channelErrDisabled = Enum.YLeaf(157, "channelErrDisabled")

    vrfMismatch = Enum.YLeaf(158, "vrfMismatch")

    vrfForwardReferencing = Enum.YLeaf(159, "vrfForwardReferencing")

    dupTunnelConfigDetected = Enum.YLeaf(160, "dupTunnelConfigDetected")

    primaryVLANDown = Enum.YLeaf(161, "primaryVLANDown")

    vrfUnusable = Enum.YLeaf(162, "vrfUnusable")

    errDisableHandShkFailure = Enum.YLeaf(163, "errDisableHandShkFailure")

    errDisabledBPDUGuard = Enum.YLeaf(164, "errDisabledBPDUGuard")

    dot1xSecViolationErrDisabled = Enum.YLeaf(165, "dot1xSecViolationErrDisabled")

    emptyEchoUDLD = Enum.YLeaf(166, "emptyEchoUDLD")

    vfTaggingCapErr = Enum.YLeaf(167, "vfTaggingCapErr")

    portDisabled = Enum.YLeaf(168, "portDisabled")

    tunnelModeNotConfigured = Enum.YLeaf(169, "tunnelModeNotConfigured")

    tunnelSrcNotConfigured = Enum.YLeaf(170, "tunnelSrcNotConfigured")

    tunnelDstNotConfigured = Enum.YLeaf(171, "tunnelDstNotConfigured")

    tunnelUnableToResolveSrcIP = Enum.YLeaf(172, "tunnelUnableToResolveSrcIP")

    tunnelUnableToResolveDstIP = Enum.YLeaf(173, "tunnelUnableToResolveDstIP")

    tunnelVrfDown = Enum.YLeaf(174, "tunnelVrfDown")

    sifAdminDown = Enum.YLeaf(175, "sifAdminDown")

    phyIntfDown = Enum.YLeaf(176, "phyIntfDown")

    ifSifLimitExceeded = Enum.YLeaf(177, "ifSifLimitExceeded")

    sifHoldDown = Enum.YLeaf(178, "sifHoldDown")

    noFcoe = Enum.YLeaf(179, "noFcoe")

    dcxCompatMismatch = Enum.YLeaf(180, "dcxCompatMismatch")

    isolateBundleLimitExceeded = Enum.YLeaf(181, "isolateBundleLimitExceeded")

    sifNotBound = Enum.YLeaf(182, "sifNotBound")

    errDisabledLacpMiscfg = Enum.YLeaf(183, "errDisabledLacpMiscfg")

    satFabricIfDown = Enum.YLeaf(184, "satFabricIfDown")

    invalidSatFabricIf = Enum.YLeaf(185, "invalidSatFabricIf")

    noRemoteChassis = Enum.YLeaf(186, "noRemoteChassis")

    vicEnableNotReceived = Enum.YLeaf(187, "vicEnableNotReceived")

    vicDisableReceived = Enum.YLeaf(188, "vicDisableReceived")

    vlanVsanMappingNotEnabled = Enum.YLeaf(189, "vlanVsanMappingNotEnabled")

    stpNotFwdingInFcoeMappedVlan = Enum.YLeaf(190, "stpNotFwdingInFcoeMappedVlan")

    moduleOffline = Enum.YLeaf(191, "moduleOffline")

    udldAggModeLinkFailure = Enum.YLeaf(192, "udldAggModeLinkFailure")

    stpInconsVpcPeerDisabled = Enum.YLeaf(193, "stpInconsVpcPeerDisabled")

    setPortStateFailed = Enum.YLeaf(194, "setPortStateFailed")

    suspendedByVpc = Enum.YLeaf(195, "suspendedByVpc")

    vpcCfgInProgress = Enum.YLeaf(196, "vpcCfgInProgress")

    vpcPeerLinkDown = Enum.YLeaf(197, "vpcPeerLinkDown")

    vpcNoRspFromPeer = Enum.YLeaf(198, "vpcNoRspFromPeer")

    protoPortSuspend = Enum.YLeaf(199, "protoPortSuspend")

    tunnelSrcDown = Enum.YLeaf(200, "tunnelSrcDown")

    cdpInfoUnavailable = Enum.YLeaf(201, "cdpInfoUnavailable")

    fexSfpInvalid = Enum.YLeaf(202, "fexSfpInvalid")

    errDisabledIpConflict = Enum.YLeaf(203, "errDisabledIpConflict")

    fcotClkRateMismatch = Enum.YLeaf(204, "fcotClkRateMismatch")

    portGuardTrustSecViolation = Enum.YLeaf(205, "portGuardTrustSecViolation")

    sdpTimeout = Enum.YLeaf(206, "sdpTimeout")

    satIncompatTopo = Enum.YLeaf(207, "satIncompatTopo")

    waitForFlogi = Enum.YLeaf(208, "waitForFlogi")

    satNotConfigured = Enum.YLeaf(209, "satNotConfigured")

    npivNotEnabledInUpstream = Enum.YLeaf(210, "npivNotEnabledInUpstream")

    vsanMismatchWithUpstreamSwPort = Enum.YLeaf(211, "vsanMismatchWithUpstreamSwPort")

    portGuardBitErrRate = Enum.YLeaf(212, "portGuardBitErrRate")

    portGuardSigLoss = Enum.YLeaf(213, "portGuardSigLoss")

    portGuardSyncLoss = Enum.YLeaf(214, "portGuardSyncLoss")

    portGuardLinkReset = Enum.YLeaf(215, "portGuardLinkReset")

    portGuardCreditLoss = Enum.YLeaf(216, "portGuardCreditLoss")

    ipQosMgrPolicyAppFailure = Enum.YLeaf(217, "ipQosMgrPolicyAppFailure")

    pauseRateLimitErrDisabled = Enum.YLeaf(218, "pauseRateLimitErrDisabled")

    lstGrpUplinkDown = Enum.YLeaf(219, "lstGrpUplinkDown")

    stickyDnLinkFailure = Enum.YLeaf(220, "stickyDnLinkFailure")

    routerMacFailure = Enum.YLeaf(221, "routerMacFailure")

    dcxMultipleMsapIds = Enum.YLeaf(222, "dcxMultipleMsapIds")

    dcxHundredPdusRcvdNoAck = Enum.YLeaf(223, "dcxHundredPdusRcvdNoAck")

    enmSatIncompatibleUplink = Enum.YLeaf(224, "enmSatIncompatibleUplink")

    enmLoopDetected = Enum.YLeaf(225, "enmLoopDetected")

    nonStickyExternallyDisabled = Enum.YLeaf(226, "nonStickyExternallyDisabled")

    subGroupIdNotAssigned = Enum.YLeaf(227, "subGroupIdNotAssigned")

    vemUnlicensed = Enum.YLeaf(228, "vemUnlicensed")

    profileNotFound = Enum.YLeaf(229, "profileNotFound")

    nonExistentVlan = Enum.YLeaf(230, "nonExistentVlan")

    vlanInvalidType = Enum.YLeaf(231, "vlanInvalidType")

    vlanDown = Enum.YLeaf(232, "vlanDown")

    vpcPeerUpgrade = Enum.YLeaf(233, "vpcPeerUpgrade")

    ipQosDcbxpCompatFailure = Enum.YLeaf(234, "ipQosDcbxpCompatFailure")

    nonCiscoHbaVfTag = Enum.YLeaf(235, "nonCiscoHbaVfTag")

    domainIdConfigMismatch = Enum.YLeaf(236, "domainIdConfigMismatch")

    sfpSpeedMismatch = Enum.YLeaf(237, "sfpSpeedMismatch")

    xcvrInitializing = Enum.YLeaf(238, "xcvrInitializing")

    xcvrAbsent = Enum.YLeaf(239, "xcvrAbsent")

    xcvrInvalid = Enum.YLeaf(240, "xcvrInvalid")

    vfcBindingInvalid = Enum.YLeaf(241, "vfcBindingInvalid")

    vlanNotFcoeEnabled = Enum.YLeaf(242, "vlanNotFcoeEnabled")

    pvlanNativeVlanErr = Enum.YLeaf(243, "pvlanNativeVlanErr")

    ethL2VlanDown = Enum.YLeaf(244, "ethL2VlanDown")

    ethIntfInvalidBinding = Enum.YLeaf(245, "ethIntfInvalidBinding")

    pmonFailure = Enum.YLeaf(246, "pmonFailure")

    l3NotReady = Enum.YLeaf(247, "l3NotReady")

    speedMismatch = Enum.YLeaf(248, "speedMismatch")

    flowControlMismatch = Enum.YLeaf(249, "flowControlMismatch")

    vdcMode = Enum.YLeaf(250, "vdcMode")

    suspendedDueToMinLinks = Enum.YLeaf(251, "suspendedDueToMinLinks")

    enmPinFailLinkDown = Enum.YLeaf(252, "enmPinFailLinkDown")

    inactiveM1PortFpathActiveVlan = Enum.YLeaf(253, "inactiveM1PortFpathActiveVlan")

    parentPortDown = Enum.YLeaf(254, "parentPortDown")

    moduleRemoved = Enum.YLeaf(255, "moduleRemoved")

    corePortMct = Enum.YLeaf(256, "corePortMct")

    nonCorePortMct = Enum.YLeaf(257, "nonCorePortMct")

    ficonInorderNotActive = Enum.YLeaf(258, "ficonInorderNotActive")

    invalidEncapsulation = Enum.YLeaf(259, "invalidEncapsulation")

    modemLineDeasserted = Enum.YLeaf(260, "modemLineDeasserted")

    ipSecHndshkInProgress = Enum.YLeaf(261, "ipSecHndshkInProgress")

    sfpEthCompliantErr = Enum.YLeaf(262, "sfpEthCompliantErr")

    cellularModemUnattached = Enum.YLeaf(263, "cellularModemUnattached")

    outOfGlblRxBuffers = Enum.YLeaf(264, "outOfGlblRxBuffers")

    sfpFcCompliantErr = Enum.YLeaf(265, "sfpFcCompliantErr")

    ethIntfNotLicensed = Enum.YLeaf(266, "ethIntfNotLicensed")

    domainIdsInvalid = Enum.YLeaf(267, "domainIdsInvalid")

    fabricNameInvalid = Enum.YLeaf(268, "fabricNameInvalid")


class Ciscocoslist(Bits):
    """
    Ciscocoslist

    Each bit represents a CoS value (0 through 7).
    Keys are:- cos5 , cos2 , cos7 , cos4 , cos1 , cos0 , cos3 , cos6

    """

    def __init__(self):
        super(Ciscocoslist, self).__init__()


