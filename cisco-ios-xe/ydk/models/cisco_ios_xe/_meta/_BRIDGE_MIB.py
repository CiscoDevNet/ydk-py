


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BridgeMib.Dot1Dbase.Dot1DbasetypeEnum' : _MetaInfoEnum('Dot1DbasetypeEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'unknown':'unknown',
            'transparent-only':'transparent_only',
            'sourceroute-only':'sourceroute_only',
            'srt':'srt',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dbase' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dbase',
            False, 
            [
            _MetaInfoClassMember('dot1dBaseBridgeAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address used by this bridge when it must be
                referred to in a unique fashion.  It is recommended
                that this be the numerically smallest MAC address of
                all ports that belong to this bridge.  However, it is only
                
                required to be unique.  When concatenated with
                dot1dStpPriority, a unique BridgeIdentifier is formed,
                which is used in the Spanning Tree Protocol.
                ''',
                'dot1dbasebridgeaddress',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBaseNumPorts', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of ports controlled by this bridging
                entity.
                ''',
                'dot1dbasenumports',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBaseType', REFERENCE_ENUM_CLASS, 'Dot1DbasetypeEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dbase.Dot1DbasetypeEnum', 
                [], [], 
                '''                Indicates what type of bridging this bridge can
                perform.  If a bridge is actually performing a
                certain type of bridging, this will be indicated by
                entries in the port table for the given type.
                ''',
                'dot1dbasetype',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dBase',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dstp.Dot1DstpprotocolspecificationEnum' : _MetaInfoEnum('Dot1DstpprotocolspecificationEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'unknown':'unknown',
            'decLb100':'decLb100',
            'ieee8021d':'ieee8021d',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dstp' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dstp',
            False, 
            [
            _MetaInfoClassMember('dot1dStpBridgeForwardDelay', ATTRIBUTE, 'int' , None, None, 
                [('400', '3000')], [], 
                '''                The value that all bridges use for ForwardDelay when
                this bridge is acting as the root.  Note that
                802.1D-1998 specifies that the range for this parameter
                is related to the value of dot1dStpBridgeMaxAge.  The
                granularity of this timer is specified by 802.1D-1998 to
                be 1 second.  An agent may return a badValue error if a
                set is attempted to a value that is not a whole number
                of seconds.
                ''',
                'dot1dstpbridgeforwarddelay',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpBridgeHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('100', '1000')], [], 
                '''                The value that all bridges use for HelloTime when this
                bridge is acting as the root.  The granularity of this
                timer is specified by 802.1D-1998 to be 1 second.  An
                agent may return a badValue error if a set is attempted
                
                to a value that is not a whole number of seconds.
                ''',
                'dot1dstpbridgehellotime',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpBridgeMaxAge', ATTRIBUTE, 'int' , None, None, 
                [('600', '4000')], [], 
                '''                The value that all bridges use for MaxAge when this
                bridge is acting as the root.  Note that 802.1D-1998
                specifies that the range for this parameter is related
                to the value of dot1dStpBridgeHelloTime.  The
                granularity of this timer is specified by 802.1D-1998 to
                be 1 second.  An agent may return a badValue error if a
                set is attempted to a value that is not a whole number
                of seconds.
                ''',
                'dot1dstpbridgemaxage',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpDesignatedRoot', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The bridge identifier of the root of the spanning
                tree, as determined by the Spanning Tree Protocol,
                as executed by this node.  This value is used as
                the Root Identifier parameter in all Configuration
                Bridge PDUs originated by this node.
                ''',
                'dot1dstpdesignatedroot',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpForwardDelay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This time value, measured in units of hundredths of a
                second, controls how fast a port changes its spanning
                state when moving towards the Forwarding state.  The
                value determines how long the port stays in each of the
                Listening and Learning states, which precede the
                Forwarding state.  This value is also used when a
                topology change has been detected and is underway, to
                age all dynamic entries in the Forwarding Database.
                [Note that this value is the one that this bridge is
                currently using, in contrast to
                dot1dStpBridgeForwardDelay, which is the value that this
                bridge and all others would start using if/when this
                bridge were to become the root.]
                ''',
                'dot1dstpforwarddelay',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The amount of time between the transmission of
                Configuration bridge PDUs by this node on any port when
                it is the root of the spanning tree, or trying to become
                so, in units of hundredths of a second.  This is the
                actual value that this bridge is currently using.
                ''',
                'dot1dstphellotime',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This time value determines the interval length
                during which no more than two Configuration bridge
                PDUs shall be transmitted by this node, in units
                of hundredths of a second.
                ''',
                'dot1dstpholdtime',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpMaxAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum age of Spanning Tree Protocol information
                learned from the network on any port before it is
                discarded, in units of hundredths of a second.  This is
                the actual value that this bridge is currently using.
                ''',
                'dot1dstpmaxage',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The value of the write-able portion of the Bridge ID
                (i.e., the first two octets of the (8 octet long) Bridge
                ID).  The other (last) 6 octets of the Bridge ID are
                given by the value of dot1dBaseBridgeAddress.
                On bridges supporting IEEE 802.1t or IEEE 802.1w,
                permissible values are 0-61440, in steps of 4096.
                ''',
                'dot1dstppriority',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpProtocolSpecification', REFERENCE_ENUM_CLASS, 'Dot1DstpprotocolspecificationEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstp.Dot1DstpprotocolspecificationEnum', 
                [], [], 
                '''                An indication of what version of the Spanning Tree
                Protocol is being run.  The value 'decLb100(2)'
                indicates the DEC LANbridge 100 Spanning Tree protocol.
                IEEE 802.1D implementations will return 'ieee8021d(3)'.
                If future versions of the IEEE Spanning Tree Protocol
                that are incompatible with the current version
                are released a new value will be defined.
                ''',
                'dot1dstpprotocolspecification',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpRootCost', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The cost of the path to the root as seen from
                this bridge.
                ''',
                'dot1dstprootcost',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpRootPort', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The port number of the port that offers the lowest
                cost path from this bridge to the root bridge.
                ''',
                'dot1dstprootport',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpTimeSinceTopologyChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time (in hundredths of a second) since the
                last time a topology change was detected by the
                bridge entity.
                For RSTP, this reports the time since the tcWhile
                timer for any port on this Bridge was nonzero.
                ''',
                'dot1dstptimesincetopologychange',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpTopChanges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of topology changes detected by
                this bridge since the management entity was last
                reset or initialized.
                ''',
                'dot1dstptopchanges',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dStp',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dtp' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dtp',
            False, 
            [
            _MetaInfoClassMember('dot1dTpAgingTime', ATTRIBUTE, 'int' , None, None, 
                [('10', '1000000')], [], 
                '''                The timeout period in seconds for aging out
                dynamically-learned forwarding information.
                802.1D-1998 recommends a default of 300 seconds.
                ''',
                'dot1dtpagingtime',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpLearnedEntryDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Forwarding Database entries that
                have been or would have been learned, but have been
                discarded due to a lack of storage space in the
                Forwarding Database.  If this counter is increasing, it
                indicates that the Forwarding Database is regularly
                becoming full (a condition that has unpleasant
                performance effects on the subnetwork).  If this counter
                has a significant value but is not presently increasing,
                it indicates that the problem has been occurring but is
                not persistent.
                ''',
                'dot1dtplearnedentrydiscards',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dTp',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The port number of the port for which this entry
                contains bridge management information.
                ''',
                'dot1dbaseport',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dBasePortCircuit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                For a port that (potentially) has the same value of
                dot1dBasePortIfIndex as another port on the same bridge.
                This object contains the name of an object instance
                unique to this port.  For example, in the case where
                multiple ports correspond one-to-one with multiple X.25
                virtual circuits, this value might identify an (e.g.,
                the first) object instance associated with the X.25
                virtual circuit corresponding to this port.
                
                For a port which has a unique value of
                dot1dBasePortIfIndex, this object can have the value
                { 0 0 }.
                ''',
                'dot1dbaseportcircuit',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBasePortDelayExceededDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames discarded by this port due
                to excessive transit delay through the bridge.  It
                is incremented by both transparent and source
                route bridges.
                ''',
                'dot1dbaseportdelayexceededdiscards',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBasePortIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The value of the instance of the ifIndex object,
                defined in IF-MIB, for the interface corresponding
                to this port.
                ''',
                'dot1dbaseportifindex',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBasePortMtuExceededDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames discarded by this port due
                to an excessive size.  It is incremented by both
                transparent and source route bridges.
                ''',
                'dot1dbaseportmtuexceededdiscards',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortCapabilities', REFERENCE_BITS, 'Dot1Dportcapabilities' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Dportcapabilities', 
                [], [], 
                '''                Indicates the parts of IEEE 802.1D and 802.1Q that are
                optional on a per-port basis, that are implemented by
                this device, and that are manageable through this MIB.
                
                dot1qDot1qTagging(0), -- supports 802.1Q VLAN tagging of
                                      -- frames and GVRP.
                dot1qConfigurableAcceptableFrameTypes(1),
                                      -- allows modified values of
                                      -- dot1qPortAcceptableFrameTypes.
                dot1qIngressFiltering(2)
                                      -- supports the discarding of any
                                      -- frame received on a Port whose
                                      -- VLAN classification does not
                                      -- include that Port in its Member
                                      -- set.
                ''',
                'dot1dportcapabilities',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortDefaultUserPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The default ingress User Priority for this port.  This
                only has effect on media, such as Ethernet, that do not
                support native User Priority.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportdefaultuserpriority',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGarpJoinTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The GARP Join time, in centiseconds.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportgarpjointime',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGarpLeaveAllTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The GARP LeaveAll time, in centiseconds.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportgarpleavealltime',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGarpLeaveTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The GARP Leave time, in centiseconds.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportgarpleavetime',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGmrpFailedRegistrations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of failed GMRP registrations, for any
                reason, in all VLANs, on this port.
                ''',
                'dot1dportgmrpfailedregistrations',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGmrpLastPduOrigin', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The Source MAC Address of the last GMRP message
                received on this port.
                ''',
                'dot1dportgmrplastpduorigin',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortGmrpStatus', REFERENCE_ENUM_CLASS, 'EnabledstatusEnum' , 'ydk.models.cisco_ios_xe.P_BRIDGE_MIB', 'EnabledstatusEnum', 
                [], [], 
                '''                The administrative state of GMRP operation on this port.  The
                value enabled(1) indicates that GMRP is enabled on this port
                in all VLANs as long as dot1dGmrpStatus is also enabled(1).
                A value of disabled(2) indicates that GMRP is disabled on
                this port in all VLANs: any GMRP packets received will
                be silently discarded, and no GMRP registrations will be
                propagated from other ports.  Setting this to a value of
                enabled(1) will be stored by the agent but will only take
                effect on the GMRP protocol operation if dot1dGmrpStatus
                also indicates the value enabled(1).  This object affects
                all GMRP Applicant and Registrar state machines on this
                port.  A transition from disabled(2) to enabled(1) will
                cause a reset of all GMRP state machines on this port.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportgmrpstatus',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortNumTrafficClasses', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                The number of egress traffic classes supported on this
                port.  This object may optionally be read-only.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportnumtrafficclasses',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortRestrictedGroupRegistration', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The state of Restricted Group Registration on this port.
                If the value of this control is true(1), then creation
                of a new dynamic entry is permitted only if there is a
                Static Filtering Entry for the VLAN concerned, in which
                the Registrar Administrative Control value is Normal
                Registration.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dportrestrictedgroupregistration',
                'P-BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dBasePortEntry',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dbaseporttable' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dbaseporttable',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePortEntry', REFERENCE_LIST, 'Dot1Dbaseportentry' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry', 
                [], [], 
                '''                A list of information for each port of the bridge.
                ''',
                'dot1dbaseportentry',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dBasePortTable',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportenableEnum' : _MetaInfoEnum('Dot1DstpportenableEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportstateEnum' : _MetaInfoEnum('Dot1DstpportstateEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'disabled':'disabled',
            'blocking':'blocking',
            'listening':'listening',
            'learning':'learning',
            'forwarding':'forwarding',
            'broken':'broken',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry',
            False, 
            [
            _MetaInfoClassMember('dot1dStpPort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The port number of the port for which this entry
                contains Spanning Tree Protocol management information.
                ''',
                'dot1dstpport',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dStpPortDesignatedBridge', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The Bridge Identifier of the bridge that this
                port considers to be the Designated Bridge for
                this port's segment.
                ''',
                'dot1dstpportdesignatedbridge',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortDesignatedCost', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The path cost of the Designated Port of the segment
                connected to this port.  This value is compared to the
                Root Path Cost field in received bridge PDUs.
                ''',
                'dot1dstpportdesignatedcost',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortDesignatedPort', ATTRIBUTE, 'str' , None, None, 
                [(2, None)], [], 
                '''                The Port Identifier of the port on the Designated
                Bridge for this port's segment.
                ''',
                'dot1dstpportdesignatedport',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortDesignatedRoot', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The unique Bridge Identifier of the Bridge
                recorded as the Root in the Configuration BPDUs
                transmitted by the Designated Bridge for the
                segment to which the port is attached.
                ''',
                'dot1dstpportdesignatedroot',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortEnable', REFERENCE_ENUM_CLASS, 'Dot1DstpportenableEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportenableEnum', 
                [], [], 
                '''                The enabled/disabled status of the port.
                ''',
                'dot1dstpportenable',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortForwardTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this port has transitioned
                from the Learning state to the Forwarding state.
                ''',
                'dot1dstpportforwardtransitions',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortPathCost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The contribution of this port to the path cost of
                paths towards the spanning tree root which include
                this port.  802.1D-1998 recommends that the default
                value of this parameter be in inverse proportion to
                
                the speed of the attached LAN.
                
                New implementations should support dot1dStpPortPathCost32.
                If the port path costs exceeds the maximum value of this
                object then this object should report the maximum value,
                namely 65535.  Applications should try to read the
                dot1dStpPortPathCost32 object if this object reports
                the maximum value.
                ''',
                'dot1dstpportpathcost',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortPathCost32', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000000')], [], 
                '''                The contribution of this port to the path cost of
                paths towards the spanning tree root which include
                this port.  802.1D-1998 recommends that the default
                value of this parameter be in inverse proportion to
                the speed of the attached LAN.
                
                This object replaces dot1dStpPortPathCost to support
                IEEE 802.1t.
                ''',
                'dot1dstpportpathcost32',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The value of the priority field that is contained in
                the first (in network byte order) octet of the (2 octet
                long) Port ID.  The other octet of the Port ID is given
                by the value of dot1dStpPort.
                On bridges supporting IEEE 802.1t or IEEE 802.1w,
                permissible values are 0-240, in steps of 16.
                ''',
                'dot1dstpportpriority',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortState', REFERENCE_ENUM_CLASS, 'Dot1DstpportstateEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportstateEnum', 
                [], [], 
                '''                The port's current state, as defined by application of
                the Spanning Tree Protocol.  This state controls what
                action a port takes on reception of a frame.  If the
                bridge has detected a port that is malfunctioning, it
                will place that port into the broken(6) state.  For
                ports that are disabled (see dot1dStpPortEnable), this
                object will have a value of disabled(1).
                ''',
                'dot1dstpportstate',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('stpxLongStpPortPathCost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The contribution of this port to the path cost (in 32
                bits value) of paths towards the spanning tree root which
                include this port.
                
                This object is used to configure the spanning tree port
                path cost in 32 bits value range when the
                stpxSpanningTreePathCostOperMode is long(2).
                
                If the stpxSpanningTreePathCostOperMode is short(1), this 
                MIB object is not instantiated.
                ''',
                'stpxlongstpportpathcost',
                'CISCO-STP-EXTENSIONS-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dStpPortEntry',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dstpporttable' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dstpporttable',
            False, 
            [
            _MetaInfoClassMember('dot1dStpPortEntry', REFERENCE_LIST, 'Dot1Dstpportentry' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry', 
                [], [], 
                '''                A list of information maintained by every port about
                the Spanning Tree Protocol state for that port.
                ''',
                'dot1dstpportentry',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dStpPortTable',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1DtpfdbstatusEnum' : _MetaInfoEnum('Dot1DtpfdbstatusEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'other':'other',
            'invalid':'invalid',
            'learned':'learned',
            'self':'self',
            'mgmt':'mgmt',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry',
            False, 
            [
            _MetaInfoClassMember('dot1dTpFdbAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A unicast MAC address for which the bridge has
                forwarding and/or filtering information.
                ''',
                'dot1dtpfdbaddress',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTpFdbPort', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Either the value '0', or the port number of the port on
                which a frame having a source address equal to the value
                of the corresponding instance of dot1dTpFdbAddress has
                been seen.  A value of '0' indicates that the port
                number has not been learned, but that the bridge does
                have some forwarding/filtering information about this
                address (e.g., in the dot1dStaticTable).  Implementors
                are encouraged to assign the port value to this object
                whenever it is learned, even for addresses for which the
                corresponding value of dot1dTpFdbStatus is not
                learned(3).
                ''',
                'dot1dtpfdbport',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpFdbStatus', REFERENCE_ENUM_CLASS, 'Dot1DtpfdbstatusEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1DtpfdbstatusEnum', 
                [], [], 
                '''                The status of this entry.  The meanings of the
                values are:
                    other(1) - none of the following.  This would
                        include the case where some other MIB object
                        (not the corresponding instance of
                        dot1dTpFdbPort, nor an entry in the
                        dot1dStaticTable) is being used to determine if
                        and how frames addressed to the value of the
                        corresponding instance of dot1dTpFdbAddress are
                        being forwarded.
                    invalid(2) - this entry is no longer valid (e.g.,
                        it was learned but has since aged out), but has
                        not yet been flushed from the table.
                    learned(3) - the value of the corresponding instance
                        of dot1dTpFdbPort was learned, and is being
                        used.
                    self(4) - the value of the corresponding instance of
                        dot1dTpFdbAddress represents one of the bridge's
                        addresses.  The corresponding instance of
                        dot1dTpFdbPort indicates which of the bridge's
                        ports has this address.
                    mgmt(5) - the value of the corresponding instance of
                        dot1dTpFdbAddress is also the value of an
                        existing instance of dot1dStaticAddress.
                ''',
                'dot1dtpfdbstatus',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dTpFdbEntry',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dtpfdbtable' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dtpfdbtable',
            False, 
            [
            _MetaInfoClassMember('dot1dTpFdbEntry', REFERENCE_LIST, 'Dot1Dtpfdbentry' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry', 
                [], [], 
                '''                Information about a specific unicast MAC address
                for which the bridge has some forwarding and/or
                filtering information.
                ''',
                'dot1dtpfdbentry',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dTpFdbTable',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry',
            False, 
            [
            _MetaInfoClassMember('dot1dTpPort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The port number of the port for which this entry
                contains Transparent bridging management information.
                ''',
                'dot1dtpport',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTpPortInDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of received valid frames that were discarded
                (i.e., filtered) by the Forwarding Process.
                ''',
                'dot1dtpportindiscards',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortInFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames that have been received by this
                port from its segment.  Note that a frame received on the
                interface corresponding to this port is only counted by
                this object if and only if it is for a protocol being
                processed by the local bridging function, including
                bridge management frames.
                ''',
                'dot1dtpportinframes',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortMaxInfo', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum size of the INFO (non-MAC) field that
                
                this port will receive or transmit.
                ''',
                'dot1dtpportmaxinfo',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortOutFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames that have been transmitted by this
                port to its segment.  Note that a frame transmitted on
                the interface corresponding to this port is only counted
                by this object if and only if it is for a protocol being
                processed by the local bridging function, including
                bridge management frames.
                ''',
                'dot1dtpportoutframes',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dTpPortEntry',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dtpporttable' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dtpporttable',
            False, 
            [
            _MetaInfoClassMember('dot1dTpPortEntry', REFERENCE_LIST, 'Dot1Dtpportentry' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry', 
                [], [], 
                '''                A list of information for each port of a transparent
                bridge.
                ''',
                'dot1dtpportentry',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dTpPortTable',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dstatictable.Dot1Dstaticentry.Dot1DstaticstatusEnum' : _MetaInfoEnum('Dot1DstaticstatusEnum', 'ydk.models.cisco_ios_xe.BRIDGE_MIB',
        {
            'other':'other',
            'invalid':'invalid',
            'permanent':'permanent',
            'deleteOnReset':'deleteOnReset',
            'deleteOnTimeout':'deleteOnTimeout',
        }, 'BRIDGE-MIB', _yang_ns._namespaces['BRIDGE-MIB']),
    'BridgeMib.Dot1Dstatictable.Dot1Dstaticentry' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dstatictable.Dot1Dstaticentry',
            False, 
            [
            _MetaInfoClassMember('dot1dStaticAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address in a frame to which this
                entry's filtering information applies.  This object can
                take the value of a unicast address, a group address, or
                the broadcast address.
                ''',
                'dot1dstaticaddress',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dStaticReceivePort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Either the value '0', or the port number of the port
                from which a frame must be received in order for this
                entry's filtering information to apply.  A value of zero
                indicates that this entry applies on all ports of the
                bridge for which there is no other applicable entry.
                ''',
                'dot1dstaticreceiveport',
                'BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dStaticAllowedToGoTo', ATTRIBUTE, 'str' , None, None, 
                [(0, 512)], [], 
                '''                The set of ports to which frames received from a
                specific port and destined for a specific MAC address,
                are allowed to be forwarded.  Each octet within the
                value of this object specifies a set of eight ports,
                with the first octet specifying ports 1 through 8, the
                second octet specifying ports 9 through 16, etc.  Within
                each octet, the most significant bit represents the
                lowest numbered port, and the least significant bit
                represents the highest numbered port.  Thus, each port
                of the bridge is represented by a single bit within the
                value of this object.  If that bit has a value of '1',
                then that port is included in the set of ports; the port
                is not included if its bit has a value of '0'.  (Note
                that the setting of the bit corresponding to the port
                from which a frame is received is irrelevant.)  The
                default value of this object is a string of ones of
                appropriate length.
                
                The value of this object may exceed the required minimum
                maximum message size of some SNMP transport (484 bytes,
                in the case of SNMP over UDP, see RFC 3417, section 3.2).
                SNMP engines on bridges supporting a large number of
                ports must support appropriate maximum message sizes.
                ''',
                'dot1dstaticallowedtogoto',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStaticStatus', REFERENCE_ENUM_CLASS, 'Dot1DstaticstatusEnum' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstatictable.Dot1Dstaticentry.Dot1DstaticstatusEnum', 
                [], [], 
                '''                This object indicates the status of this entry.
                The default value is permanent(3).
                    other(1) - this entry is currently in use but the
                        conditions under which it will remain so are
                        different from each of the following values.
                    invalid(2) - writing this value to the object
                        removes the corresponding entry.
                    permanent(3) - this entry is currently in use and
                        will remain so after the next reset of the
                        bridge.
                    deleteOnReset(4) - this entry is currently in use
                        and will remain so until the next reset of the
                        bridge.
                    deleteOnTimeout(5) - this entry is currently in use
                        and will remain so until it is aged out.
                ''',
                'dot1dstaticstatus',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dStaticEntry',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib.Dot1Dstatictable' : {
        'meta_info' : _MetaInfoClass('BridgeMib.Dot1Dstatictable',
            False, 
            [
            _MetaInfoClassMember('dot1dStaticEntry', REFERENCE_LIST, 'Dot1Dstaticentry' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstatictable.Dot1Dstaticentry', 
                [], [], 
                '''                Filtering information configured into the bridge by
                (local or network) management specifying the set of
                ports to which frames received from a specific port and
                containing a specific destination address are allowed to
                be forwarded.
                ''',
                'dot1dstaticentry',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'dot1dStaticTable',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
    'BridgeMib' : {
        'meta_info' : _MetaInfoClass('BridgeMib',
            False, 
            [
            _MetaInfoClassMember('dot1dBase', REFERENCE_CLASS, 'Dot1Dbase' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dbase', 
                [], [], 
                '''                ''',
                'dot1dbase',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dBasePortTable', REFERENCE_CLASS, 'Dot1Dbaseporttable' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dbaseporttable', 
                [], [], 
                '''                A table that contains generic information about every
                port that is associated with this bridge.  Transparent,
                source-route, and srt ports are included.
                ''',
                'dot1dbaseporttable',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStaticTable', REFERENCE_CLASS, 'Dot1Dstatictable' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstatictable', 
                [], [], 
                '''                A table containing filtering information configured
                into the bridge by (local or network) management
                specifying the set of ports to which frames received
                from specific ports and containing specific destination
                addresses are allowed to be forwarded.  The value of
                zero in this table, as the port number from which frames
                with a specific destination address are received, is
                used to specify all ports for which there is no specific
                entry in this table for that particular destination
                address.  Entries are valid for unicast and for
                group/broadcast addresses.
                ''',
                'dot1dstatictable',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStp', REFERENCE_CLASS, 'Dot1Dstp' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstp', 
                [], [], 
                '''                ''',
                'dot1dstp',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dStpPortTable', REFERENCE_CLASS, 'Dot1Dstpporttable' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dstpporttable', 
                [], [], 
                '''                A table that contains port-specific information
                for the Spanning Tree Protocol.
                ''',
                'dot1dstpporttable',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTp', REFERENCE_CLASS, 'Dot1Dtp' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtp', 
                [], [], 
                '''                ''',
                'dot1dtp',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpFdbTable', REFERENCE_CLASS, 'Dot1Dtpfdbtable' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtpfdbtable', 
                [], [], 
                '''                A table that contains information about unicast
                entries for which the bridge has forwarding and/or
                filtering information.  This information is used
                by the transparent bridging function in
                determining how to propagate a received frame.
                ''',
                'dot1dtpfdbtable',
                'BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortTable', REFERENCE_CLASS, 'Dot1Dtpporttable' , 'ydk.models.cisco_ios_xe.BRIDGE_MIB', 'BridgeMib.Dot1Dtpporttable', 
                [], [], 
                '''                A table that contains information about every port that
                is associated with this transparent bridge.
                ''',
                'dot1dtpporttable',
                'BRIDGE-MIB', False),
            ],
            'BRIDGE-MIB',
            'BRIDGE-MIB',
            _yang_ns._namespaces['BRIDGE-MIB'],
        'ydk.models.cisco_ios_xe.BRIDGE_MIB'
        ),
    },
}
_meta_table['BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry']['meta_info'].parent =_meta_table['BridgeMib.Dot1Dbaseporttable']['meta_info']
_meta_table['BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry']['meta_info'].parent =_meta_table['BridgeMib.Dot1Dstpporttable']['meta_info']
_meta_table['BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry']['meta_info'].parent =_meta_table['BridgeMib.Dot1Dtpfdbtable']['meta_info']
_meta_table['BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry']['meta_info'].parent =_meta_table['BridgeMib.Dot1Dtpporttable']['meta_info']
_meta_table['BridgeMib.Dot1Dstatictable.Dot1Dstaticentry']['meta_info'].parent =_meta_table['BridgeMib.Dot1Dstatictable']['meta_info']
_meta_table['BridgeMib.Dot1Dbase']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dstp']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dtp']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dbaseporttable']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dstpporttable']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dtpfdbtable']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dtpporttable']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
_meta_table['BridgeMib.Dot1Dstatictable']['meta_info'].parent =_meta_table['BridgeMib']['meta_info']
