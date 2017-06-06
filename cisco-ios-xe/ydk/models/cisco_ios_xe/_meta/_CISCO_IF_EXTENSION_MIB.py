


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IfindexpersistencestateEnum' : _MetaInfoEnum('IfindexpersistencestateEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'disable':'disable',
            'enable':'enable',
            'global':'global_',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Ciscoifextsystemconfig.CiestandardlinkupdownvarbindsEnum' : _MetaInfoEnum('CiestandardlinkupdownvarbindsEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'standard':'standard',
            'additional':'additional',
            'other':'other',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Ciscoifextsystemconfig' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Ciscoifextsystemconfig',
            False, 
            [
            _MetaInfoClassMember('cieDelayedLinkUpDownNotifDelay', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                This object specifies the interval of time an interface's
                operational status must remain stable following a transition
                before the system will generate a cieDelayedLinkUpDownNotif.
                ''',
                'ciedelayedlinkupdownnotifdelay',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieDelayedLinkUpDownNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system generates a
                cieDelayedLinkUpDownNotif notification.
                ''',
                'ciedelayedlinkupdownnotifenable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIndexGlobalPersistence', REFERENCE_ENUM_CLASS, 'IfindexpersistencestateEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'IfindexpersistencestateEnum', 
                [], [], 
                '''                This object specifies whether ifIndex values persist across
                reinitialization of the device.
                
                ifIndex persistence means that the mapping between the ifDescr
                object values and the ifIndex object values will be retained
                across reboots.
                
                Applications such as device inventory, billing, and fault
                detection depend on the maintenance of the correspondence
                between particular ifIndex values and their interfaces. During
                reboot or insertion of a new card, the data to correlate the
                interfaces to the ifIndex may become invalid in absence of
                ifIndex persistence feature.
                
                ifIndex persistence for an interface ensures ifIndex value for
                the interface will remain the same after a system reboot. Hence,
                this feature allows users to avoid the workarounds required for
                consistent interface identification across reinitialization.
                
                The allowed values for this object are either enable or disable.
                global value is not allowed.
                ''',
                'cieifindexglobalpersistence',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIndexPersistence', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether ifIndex values persist across
                reinitialization of the device.
                
                ifIndex persistence means that the mapping between the ifDescr
                object values and the ifIndex object values will be retained
                across reboots.
                
                Applications such as device inventory, billing, and fault
                detection depend on the maintenance of the correspondence
                between particular ifIndex values and their interfaces. During
                reboot or insertion of a new card, the data to correlate the
                interfaces to the ifIndex may become invalid in absence of
                ifIndex persistence feature.
                
                ifIndex persistence for an interface ensures ifIndex value for
                the interface will remain the same after a system reboot.
                Hence, this feature allows users to avoid the workarounds
                required for consistent interface identification across
                reinitialization.
                
                Due to change in syntax, this object is deprecated by
                cieIfIndexGlobalPersistence.
                ''',
                'cieifindexpersistence',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieLinkUpDownConfig', REFERENCE_BITS, 'Cielinkupdownconfig' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownconfig', 
                [], [], 
                '''                This object specifies whether standard mib-II defined linkUp/
                linkDown, extended linkUp/linkDown (with extra varbinds in
                addition to the varbinds defined in linkUp/linkDown) or
                cieLinkUp/cieLinkDown notifications should be generated for
                the interfaces in the system.
                
                'standardLinkUp'     - generate standard defined mib-II 
                                       linkUp notification if 
                                       'ifLinkUpDownTrapEnable' for the 
                                       interface is 'enabled'.
                'standardLinkDown'   - generate standard defined mib-II 
                                       linkDown notification if 
                                       'ifLinkUpDownTrapEnable' for the 
                                       interface is 'enabled'.  
                'additionalLinkUp'   - generate linkUp notification with
                                       additional varbinds if 
                                       'ifLinkUpDownTrapEnable' for the 
                                       interface is 'enabled'.  
                'additionalLinkDown' - generate linkDown notification with
                                       additional varbinds if 
                                       'ifLinkUpDownTrapEnable' for the 
                                       interface is 'enabled'.
                'ciscoLinkUp'        - generate cieLinkUp notification
                                       if the 'ifLinkUpDownTrapEnable' for the
                                       interface is 'enabled'.
                'ciscoLinkDown'      - generate cieLinkDown notification
                                       if the 'ifLinkUpDownTrapEnable' for the
                                       interface is 'enabled'.
                
                If multiple bits are set then multiple notifications will
                be generated for an interface if the 'ifLinkUpDownTrapEnable' 
                for the interface is 'enabled'.
                ''',
                'cielinkupdownconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieLinkUpDownEnable', REFERENCE_BITS, 'Cielinkupdownenable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Ciscoifextsystemconfig.Cielinkupdownenable', 
                [], [], 
                '''                Indicates whether cieLinkUp/cieLinkDown
                or standard mib-II defined linkUp/Down or
                both, notifications should be generated
                for the interfaces in the system.
                
                'standard'  - only generate standard defined
                              mib-II linkUp/linkDown notification
                              if 'ifLinkUpDownTrapEnable' for 
                              the interface is 'enabled'.
                'cisco'     - only generate cieLinkUp/cieLinkDown
                              notifications for an interface if
                              the 'ifLinkUpDownTrapEnable' for the
                              interface is 'enabled'.
                
                If both bits are selected then linkUp/linkDown and
                cieLinkUp/cieLinkDown are both generated for an 
                interface if the 'ifLinkUpDownTrapEnable' for the
                interface is 'enabled'.
                ''',
                'cielinkupdownenable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieStandardLinkUpDownVarbinds', REFERENCE_ENUM_CLASS, 'CiestandardlinkupdownvarbindsEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Ciscoifextsystemconfig.CiestandardlinkupdownvarbindsEnum', 
                [], [], 
                '''                Indicates whether to send the extra
                varbinds in addition to the varbinds defined 
                in linkUp/linkDown notifications.
                
                'standard'   - only send the varbinds defined in
                               the standard linkUp/linkDown
                               notification.  
                'additional' - send the extra varbinds in addition 
                               to the defined ones.
                'other'      - any other config not covered by the above.
                               This value is read-only.
                ''',
                'ciestandardlinkupdownvarbinds',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieSystemMtu', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Global system MTU in octets.
                This object specifies the MTU on all interfaces.
                However, the value specified by cieIfMtu
                takes precedence for an interface, which means
                that the interface's MTU uses the value
                specified by cieIfMtu, if it is configured.
                ''',
                'ciesystemmtu',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'ciscoIfExtSystemConfig',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfInAbortErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of input packets which were dropped
                because the receiver aborted.
                
                Examples of this could be when an abort
                sequence aborted the input frame or when
                there is a collision in an ethernet segment.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinaborterrs',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInFramingErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets on a physical
                interface which were misaligned or had
                framing errors. This happens when the 
                format of the incoming packet on a physical
                interface is incorrect.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinframingerrs',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInGiantsErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets on a particular
                physical interface which were dropped as 
                they were larger than the ifMtu (largest 
                permitted  size of a packet which can be 
                sent/received on an interface).
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifingiantserrs',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInIgnored', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets which were simply
                ignored by this physical interface due to 
                insufficient resources to handle the incoming
                packets.
                
                For example, this could indicate that the input
                receive buffers are not available or that the
                receiver lost a packet.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinignored',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInOverrunErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets which arrived
                on a particular physical interface which 
                were too quick for the hardware to receive
                and hence the receiver ran out of buffers.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinoverrunerrs',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInputQueueDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of input packets which were
                dropped.
                
                Some reasons why this object could be 
                incremented are:
                
                o  Input queue is full.
                o  Errors at the receiver hardware 
                   while receiving the packet.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinputqueuedrops',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInRuntsErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets input on a particular
                physical interface which were dropped as
                they were smaller than the minimum allowable 
                physical media limit.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifinruntserrs',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfLastInTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the elapsed time in
                milliseconds since last protocol input 
                packet was received.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieiflastintime',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfLastOutHangTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the elapsed time in
                milliseconds since last protocol    output
                packet could not be successfully transmitted.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieiflastouthangtime',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfLastOutTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the elapsed time in
                milliseconds since last protocol  output 
                packet was transmitted.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieiflastouttime',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOutputQueueDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the  number of output
                packets dropped by the interface even though
                no error had been detected to prevent them
                being transmitted. 
                
                The packet could be dropped for many reasons,
                which could range from the interface being
                down to errors in the format of the packet.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfPacketDiscontinuityTime.
                ''',
                'cieifoutputqueuedrops',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfPacketDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent
                occasion at which this interface's  counters
                suffered a discontinuity. 
                
                If no such discontinuities have occurred 
                since the last re-initialization of the 
                local management subsystem, then this 
                object contains a value of zero.
                ''',
                'cieifpacketdiscontinuitytime',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfPacketStatsEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifpacketstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifpacketstatstable',
            False, 
            [
            _MetaInfoClassMember('cieIfPacketStatsEntry', REFERENCE_LIST, 'Cieifpacketstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry', 
                [], [], 
                '''                An entry into the cieIfPacketStatsTable.
                ''',
                'cieifpacketstatsentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfPacketStatsTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiffillpatternconfigEnum' : _MetaInfoEnum('CieiffillpatternconfigEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'arbff8G':'arbff8G',
            'idle8G':'idle8G',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifsharedconfigEnum' : _MetaInfoEnum('CieifsharedconfigEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'notApplicable':'notApplicable',
            'ownerDedicated':'ownerDedicated',
            'ownerShared':'ownerShared',
            'sharedOnly':'sharedOnly',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifspeedgroupconfigEnum' : _MetaInfoEnum('CieifspeedgroupconfigEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'notApplicable':'notApplicable',
            'tenG':'tenG',
            'oneTwoFourEightG':'oneTwoFourEightG',
            'twoFourEightSixteenG':'twoFourEightSixteenG',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiftransceiverfrequencyconfigEnum' : _MetaInfoEnum('CieiftransceiverfrequencyconfigEnum', 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB',
        {
            'notApplicable':'notApplicable',
            'fibreChannel':'fibreChannel',
            'ethernet':'ethernet',
        }, 'CISCO-IF-EXTENSION-MIB', _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB']),
    'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfCarrierTransitionCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times interface saw the carrier
                signal transition.
                
                For example, if a T1 line is unplugged, 
                then framer will detect the loss of signal 
                (LOS) on the line  and will count it as a
                transition.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfInterfaceDiscontinuityTime.
                ''',
                'cieifcarriertransitioncount',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfContextName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The ContextName denotes the interface
                'context' and is used to logically separate
                the MIB management.
                RFC 2571 and RFC 2737 describe this approach.
                When the agent supports a different SNMP 
                context, as detailed in RFC 2571 and 
                RFC 2737, for different interfaces, then the
                value of this object specifies the context
                name used for this interface.
                ''',
                'cieifcontextname',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDhcpMode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The DHCP mode configured by the
                administrator.
                If 'true' the DHCP is enabled. In which
                case an IP address is requested in DHCP.
                This is in addition to any that are 
                configured by the administrator in
                'ciiIPAddressTable' or 'ciiIPIfAddressTable'
                in CISCO-IP-IF-MIB.
                If 'false' the DHCP is disabled. In which
                case all IP addresses are configured by the
                administrator in 'ciiIPAddressTable' or 
                'ciiIPIfAddressTable'.
                For interfaces, for which DHCP cannot be or
                is not supported, then this object has the
                value 'false'.
                ''',
                'cieifdhcpmode',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfFillPatternConfig', REFERENCE_ENUM_CLASS, 'CieiffillpatternconfigEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiffillpatternconfigEnum', 
                [], [], 
                '''                This object specifies the current switchport fill pattern
                configuration on the given interface.
                
                'arbff8G' - the inter frame gap fill pattern is
                			ARBFF for 8G speed.
                'idle8G' - the inter frame gap fill pattern is
                		   IDLE for 8G speed.
                ''',
                'cieiffillpatternconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfHighSpeedReceive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An estimate of the interface's current receive bandwidth in
                units of 1,000,000 bits per second.  If this object reports a
                value of `n' then the speed of the interface is somewhere in the
                range of `n-500,000' to `n+499,999'.  For interfaces which do
                not vary in bandwidth or for those where no accurate estimation
                can be made, this object should contain the nominal bandwidth. 
                For a sub-layer which has no concept of bandwidth, this object
                should be zero.
                ''',
                'cieifhighspeedreceive',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIgnoreBitErrorsConfig', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the current switchport biterrors
                configuration on the given interface.
                
                If 'true(1)' the ignore bit errors is enabled.In which case
                the interface ignores bit errors.
                If 'false(2)' the ignore bit errors is disabled. In which 
                case the interface acts on the bit errors. 
                For interfaces, for which bit errors 
                is not supported, then this object has the
                value 'true(1)'.
                ''',
                'cieifignorebiterrorsconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIgnoreInterruptThresholdConfig', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the current interrupt threshold
                configuration on the given interface.
                
                'If 'true(1)' the ignore interrupt thresholds is enabled.
                In which case the interface ignores interrupt thresholds.
                If 'false(2)' the ignore interrupt thresholds is disabled.
                In which case the interface acts on the interrupt 
                thresholds. 
                For interfaces, for which interrupt thresholds 
                is not supported, then this object has the 
                value 'true(1)'.
                ''',
                'cieifignoreinterruptthresholdconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInterfaceDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent
                occasion at which this interface's  counters 
                suffered  a discontinuity. 
                
                If no such discontinuities have occurred 
                since the last re-initialization of the 
                local management subsystem, then this 
                object contains a value of zero.
                ''',
                'cieifinterfacediscontinuitytime',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfKeepAliveEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A keepalive is a small, layer-2 message
                that is transmitted by a network device 
                to let directly-connected network devices
                know of its presence.
                
                This object returns 'true' if keepalives
                are enabled on this interface. If keepalives
                are not enabled, 'false' is returned.
                
                Setting this object to TRUE or FALSE enables
                or disables (respectively) keepalive on this 
                interface.
                ''',
                'cieifkeepaliveenabled',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfMtu', ATTRIBUTE, 'int' , None, None, 
                [('40', '2147483647')], [], 
                '''                The MTU configured by the administrator.
                This object is exactly same as 'ifMtu' in 
                ifTable from IF-MIB for the same ifIndex
                value , except that it is configurable by the
                administrator. For more description of this
                object refer to 'ifMtu' in IF-MIB.
                ''',
                'cieifmtu',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOperStatusCause', REFERENCE_ENUM_CLASS, 'IfoperstatusreasonEnum' , 'ydk.models.cisco_ios_xe.CISCO_TC', 'IfoperstatusreasonEnum', 
                [], [], 
                '''                This object represents the detailed
                operational cause reason for the current 
                operational state of the interface. 
                The current operational state of the interface 
                is given by the 'ifOperStatus' defined 
                in IF-MIB. 
                
                The corresponding instance of 
                'cieIfOperStatusCauseDescr' must be used to 
                get the information about the operational 
                cause value mentioned in this object.
                
                For interfaces whose 'ifOperStatus' is 'down' 
                the objects 'cieIfOperStatusCause' and 
                'cieIfOperStatusCauseDescr' together provides 
                the information about the operational cause 
                reason and the description of the cause. 
                
                The value of this object will be 'none' for
                all the 'ifOperStatus' values except for 
                'down'. Its value will be one status cause 
                defined in the 'IfOperStatusReason' textual 
                convention if 'ifOperStatus' is 'down'. 
                
                The value of this object will be 'other' 
                if the operational status cause is not one 
                defined in 'IfOperStatusReason'.
                ''',
                'cieifoperstatuscause',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOperStatusCauseDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The description for the cause of current
                operational state of the interface, given 
                by the object 'cieIfOperStatusCause'.
                
                For an interface whose 'ifOperStatus' is not
                'down' the value of this object will be 
                'none'.
                ''',
                'cieifoperstatuscausedescr',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                This data type is used to model an administratively assigned
                name of the current owner of the interface resource. This 
                information is taken from the NVT ASCII character set.  It is 
                suggested that this name contain one or more of the following: 
                SnmpEngineID, IP address, management station name, network 
                manager's name, location, or phone number.
                SNMP access control is articulated entirely in terms of the 
                contents of MIB views; access to a particular SNMP object 
                instance depends only upon its presence or absence in a 
                particular MIB view and never upon its value or the value of 
                related object instances.
                Thus, this object affords resolution of resource contention 
                only among cooperating managers; this object realizes no access
                control function with respect to uncooperative parties.
                ''',
                'cieifowner',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfResetCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface was
                internally reset and brought up.
                
                Some of the actions which can cause this
                counter to increment are :
                
                o  Bringing an interface up using the 
                   interface CLI command.
                
                o  Clearing the interface with the exec
                   CLI command.
                
                o  Bringing the interface up via SNMP.
                
                Discontinuities in the value of this variable
                can occur at re-initialization of the
                management system, and at other times as 
                indicated by the values of 
                cieIfInterfaceDiscontinuityTime.
                ''',
                'cieifresetcount',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfSharedConfig', REFERENCE_ENUM_CLASS, 'CieifsharedconfigEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifsharedconfigEnum', 
                [], [], 
                '''                This object indicates the current configuration of
                interface sharing on the given interface.
                
                'notApplicable' - the interface sharing configuration on 
                            this interface is not applicable. 
                'ownerDedicated' - the interface is in the dedicated mode
                            to the binding physical interface.
                'ownerShared' - the interface is shared amongst virtual switches
                         and this interface physically belongs to a its 
                         virtual switch.  
                'sharedOnly' - the interface is in purely shared mode.
                ''',
                'cieifsharedconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfSpeedGroupConfig', REFERENCE_ENUM_CLASS, 'CieifspeedgroupconfigEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieifspeedgroupconfigEnum', 
                [], [], 
                '''                This object specifies the current speed group
                configuration on the given interface.
                
                'notApplicable' - the interface speed group configuration on
                            this interface is not applicable. It is a 
                            read-only value.
                '10G' - the interface speed group configuration on
                            this interface as 10G.
                '1G-2G-4G-8G' - the interface speed group configuration 
                            on this interface as 1G-2G-4G-8G.
                '2G-4G-8G-16G' - the interface speed group configuration 
                            on this interface as 2G-4G-8G-16G.
                ''',
                'cieifspeedgroupconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfSpeedReceive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An estimate of the interface's current receive bandwidth in
                bits per second.  This object is provided for interface with
                asymmetric interface speeds like ADSL and should be used in
                conjunction with ifSpeed object.  For interfaces which do not
                vary in bandwidth or for those where no accurate estimation can
                be made, this object should contain the nominal bandwidth. If
                the bandwidth of the interface is greater than the maximum value
                reportable by this object then this object should report its
                maximum value (4,294,967,295) and ifHighSpeed must be used to
                report the interace's speed.  For a sub-layer which has no
                concept of bandwidth, this object should be zero.
                ''',
                'cieifspeedreceive',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfStateChangeReason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object displays a human-readable
                textual string which describes the 
                cause of the last state change of the 
                interface.
                
                Examples of the values this object
                can take are:
                
                o  'Lost Carrier'
                o  'administratively down'
                o  'up'
                o  'down'
                ''',
                'cieifstatechangereason',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfTransceiverFrequencyConfig', REFERENCE_ENUM_CLASS, 'CieiftransceiverfrequencyconfigEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry.CieiftransceiverfrequencyconfigEnum', 
                [], [], 
                '''                This object specifies the current transceiver frequency
                configuration on the given interface.
                
                'notApplicable' - the interface transceiver frequency 
                				  configuration on this interface 
                				  is not applicable. It is a read-only value.
                'FibreChannel' - the interface transceiver frequency
                				 configuration on this interface as 
                                 Fibre Channel.
                'Ethernet'	  -  the interface transceiver frequency on
                				 this interface as Ethernet.
                ''',
                'cieiftransceiverfrequencyconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfInterfaceEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifinterfacetable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifinterfacetable',
            False, 
            [
            _MetaInfoClassMember('cieIfInterfaceEntry', REFERENCE_LIST, 'Cieifinterfaceentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry', 
                [], [], 
                '''                An entry into the cieIfInterfaceTable.
                ''',
                'cieifinterfaceentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfInterfaceTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfStatusListIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '33554432')], [], 
                '''                An arbitrary integer value, greater than
                zero, which identifies a list of 64 interfaces
                within a module.
                ''',
                'cieifstatuslistindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieInterfaceOwnershipBitmap', ATTRIBUTE, 'str' , None, None, 
                [(0, 8)], [], 
                '''                This object indicates the status for a set of 64 interfaces
                in a module regarding whether or not each interface is 
                administratively assigned a name of the current owner of the 
                interface resource as per cieIfOwner.
                ''',
                'cieinterfaceownershipbitmap',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieInterfacesIndex', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                This object represents the 'ifIndex' for a
                set of 64 interfaces in the module.
                ''',
                'cieinterfacesindex',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieInterfacesOperCause', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object represents the operational status
                cause for a set of 64 interfaces in the 
                module.
                ''',
                'cieinterfacesopercause',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieInterfacesOperMode', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                This object represents the operational mode
                for a set of 64 interfaces in the module.
                ''',
                'cieinterfacesopermode',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfStatusListEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifstatuslisttable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifstatuslisttable',
            False, 
            [
            _MetaInfoClassMember('cieIfStatusListEntry', REFERENCE_LIST, 'Cieifstatuslistentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry', 
                [], [], 
                '''                Each entry represents the 'ifIndex',
                interface operational mode and interface 
                operational cause for a set of 64 interfaces 
                in a module.
                ''',
                'cieifstatuslistentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfStatusListTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfDropVlInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of input
                octets on all Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifdropvlinoctets',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDropVlInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of input
                packets on all Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifdropvlinpkts',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDropVlOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of output
                octets on all Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifdropvloutoctets',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDropVlOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of output
                packets on all Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifdropvloutpkts',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfNoDropVlInOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of input
                octets on all No-Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifnodropvlinoctets',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfNoDropVlInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of input
                packets on all No-Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifnodropvlinpkts',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfNoDropVlOutOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of output
                octets on all No-Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifnodropvloutoctets',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfNoDropVlOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object indicates the number of output
                packets on all No-Drop Virtual Links belonged 
                to this interface.
                ''',
                'cieifnodropvloutpkts',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfVlStatsEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifvlstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifvlstatstable',
            False, 
            [
            _MetaInfoClassMember('cieIfVlStatsEntry', REFERENCE_LIST, 'Cieifvlstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry', 
                [], [], 
                '''                Each row contains managed objects for
                Virtual Link statistics on interface capable of 
                providing this information.
                ''',
                'cieifvlstatsentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfVlStatsTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfIndexPersistenceControl', REFERENCE_ENUM_CLASS, 'IfindexpersistencestateEnum' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'IfindexpersistencestateEnum', 
                [], [], 
                '''                This object specifies whether the interface's ifIndex value
                persist across reinitialization. In global state, the interface
                uses the global setting data for persistence i.e.
                cieIfIndexGlobalPersistence.
                ''',
                'cieifindexpersistencecontrol',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIndexPersistenceEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the interface's ifIndex value
                persist across reinitialization.
                
                Due to change in syntax, this object is deprecated by
                cieIfIndexPersistenceControl.
                ''',
                'cieifindexpersistenceenabled',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfIndexPersistenceEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifindexpersistencetable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifindexpersistencetable',
            False, 
            [
            _MetaInfoClassMember('cieIfIndexPersistenceEntry', REFERENCE_LIST, 'Cieifindexpersistenceentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry', 
                [], [], 
                '''                Each entry represents ifindex persistence configuration for an
                interface specified by ifIndex. Whenever an interface which
                supports ifindex persistence is created/destroyed in the
                ifTable, the corresponding ifindex persistence entry is
                created/destroyed respectively. Some of the interfaces may not
                support ifindex persistence, for example, a dynamic interface,
                such as a PPP connection or a IP subscriber interface.
                ''',
                'cieifindexpersistenceentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfIndexPersistenceTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfDot1qCustomAdminEtherType', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Dot1qEtherType allow administrator
                to select a non-standard (other than 0x8100)
                2-byte ethertype for the interface to 
                interoperate with third party vendor's system
                that do not use the standard 0x8100 ethertype
                to identify 802.1q-tagged frames.
                
                The current administrative value of the 
                802.1q ethertype for the interface.  The
                administrative 802.1q ethertype value may 
                differ from the operational 802.1q ethertype
                value.  On some platforms, 802.1q ethertype
                may be assigned per group rather than per port.
                If multiple ports belong to a port group,
                the 802.1q ethertype assigned to any of
                the ports in such group will apply to all
                ports in the same group.
                
                To configure non-standard dot1q ethertype
                is only recommended when the Cisco device
                is connected to any third party vendor device.
                Also be advised that the custom ethertype value
                needs to be changed in the whole cloud of 
                Cisco device with the same custom ethertype 
                value if the third party device are separated 
                by number of Cisco device in the middle.
                ''',
                'cieifdot1qcustomadminethertype',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDot1qCustomOperEtherType', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The current operational value of the
                802.1q ethertype for the interface.
                ''',
                'cieifdot1qcustomoperethertype',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfDot1qCustomEtherTypeEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable',
            False, 
            [
            _MetaInfoClassMember('cieIfDot1qCustomEtherTypeEntry', REFERENCE_LIST, 'Cieifdot1Qcustomethertypeentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry', 
                [], [], 
                '''                An entry containing the custom EtherType
                information for the interface.
                
                Only interfaces with custom 802.1q
                ethertype control are listed in the 
                table.
                ''',
                'cieifdot1qcustomethertypeentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfDot1qCustomEtherTypeTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfInOctetRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                By default, this is the five minute
                exponentially-decayed moving average of the
                inbound octet rate for this interface.
                However, if the corresponding instance of
                cieIfInterval is instantiated with a value
                which specifies an interval different from
                5-minutes, then cieIfInOctetRate is the
                exponentially-decayed moving average of inbound
                octet rate over this different time interval.
                ''',
                'cieifinoctetrate',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                By default, this is the five minute
                exponentially-decayed moving average of the
                inbound packet rate for this interface.
                However, if the corresponding instance of
                cieIfInterval is instantiated with a value
                which specifies an interval different from
                5-minutes, then cieIfInPktRate is the
                exponentially-decayed moving average of inbound
                packet rate over this different time interval.
                ''',
                'cieifinpktrate',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object specifies the time interval over which
                the inbound and outbound traffic rates are
                calculated for this interface.
                ''',
                'cieifinterval',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOutOctetRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                By default, this is the five minute
                exponentially-decayed moving average of the
                outbound octet rate for this interface.
                However, if the corresponding instance of
                cieIfInterval is instantiated with a value
                which specifies an interval different from
                5-minutes, then cieIfOutOctetRate is the
                exponentially-decayed moving average of outbound
                octet rate over this different time interval.
                ''',
                'cieifoutoctetrate',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfOutPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                By default, this is the five minute
                exponentially-decayed moving average of the
                outbound packet rate for this interface.
                However, if the corresponding instance of
                cieIfInterval is instantiated with a value
                which specifies an interval different from
                5-minutes, then cieIfOutPktRate is the
                exponentially-decayed moving average of outbound
                packet rate over this different time interval.
                ''',
                'cieifoutpktrate',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfUtilEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifutiltable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifutiltable',
            False, 
            [
            _MetaInfoClassMember('cieIfUtilEntry', REFERENCE_LIST, 'Cieifutilentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry', 
                [], [], 
                '''                An entry containing utilization rates for the
                interface.
                
                Every interface for which the  inbound and 
                outbound traffic information is available
                has a corresponding entry in this table.
                ''',
                'cieifutilentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfUtilTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfDot1dBaseMappingPort', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The dot1dBasePort value for this interface.
                ''',
                'cieifdot1dbasemappingport',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfDot1dBaseMappingEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifdot1Dbasemappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifdot1Dbasemappingtable',
            False, 
            [
            _MetaInfoClassMember('cieIfDot1dBaseMappingEntry', REFERENCE_LIST, 'Cieifdot1Dbasemappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry', 
                [], [], 
                '''                An entry containing the mapping between
                the ifIndex value of an interface and its
                corresponding dot1dBasePort value.
                
                Every interface which has been assigned
                a dot1dBasePort value by the system
                has a corresponding entry in this table.
                ''',
                'cieifdot1dbasemappingentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfDot1dBaseMappingTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry',
            False, 
            [
            _MetaInfoClassMember('cieIfName', ATTRIBUTE, 'str' , None, None, 
                [(1, 112)], [], 
                '''                Represents an interface name mentioned
                in the 'ifName' object of this system.
                ''',
                'cieifname',
                'CISCO-IF-EXTENSION-MIB', True),
            _MetaInfoClassMember('cieIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object represents the 'ifIndex'
                corresponding to the interface name mentioned
                in the 'cieIfName' object of this instance.
                If the 'ifName' mentioned in the 'cieIfName' 
                object of this instance corresponds to multiple
                'ifIndex' values, then the value of this object
                is the numerically smallest of those multiple 
                'ifIndex' values.
                ''',
                'cieifindex',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfNameMappingEntry',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib.Cieifnamemappingtable' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib.Cieifnamemappingtable',
            False, 
            [
            _MetaInfoClassMember('cieIfNameMappingEntry', REFERENCE_LIST, 'Cieifnamemappingentry' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry', 
                [], [], 
                '''                An entry into the cieIfNameMappingTable.
                ''',
                'cieifnamemappingentry',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'cieIfNameMappingTable',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
    'CiscoIfExtensionMib' : {
        'meta_info' : _MetaInfoClass('CiscoIfExtensionMib',
            False, 
            [
            _MetaInfoClassMember('cieIfDot1dBaseMappingTable', REFERENCE_CLASS, 'Cieifdot1Dbasemappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifdot1Dbasemappingtable', 
                [], [], 
                '''                This table contains the mappings of the
                ifIndex of an interface to its
                corresponding dot1dBasePort value.
                ''',
                'cieifdot1dbasemappingtable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfDot1qCustomEtherTypeTable', REFERENCE_CLASS, 'Cieifdot1Qcustomethertypetable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable', 
                [], [], 
                '''                A list of the interfaces that support
                the 802.1q custom Ethertype feature.
                ''',
                'cieifdot1qcustomethertypetable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfIndexPersistenceTable', REFERENCE_CLASS, 'Cieifindexpersistencetable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifindexpersistencetable', 
                [], [], 
                '''                This table lists configuration data relating to ifIndex
                persistence.
                
                This table has a sparse dependent relationship on the ifTable,
                containing a row for each ifEntry corresponding to an interface
                for which ifIndex persistence is supported.
                ''',
                'cieifindexpersistencetable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfInterfaceTable', REFERENCE_CLASS, 'Cieifinterfacetable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifinterfacetable', 
                [], [], 
                '''                This  table contains objects which provide
                more information about interface  
                properties not available in IF-MIB
                (RFC 2863).
                
                Some objects defined in this table may be
                applicable to physical interfaces only.
                As a result, this table may be sparse for
                logical interfaces.
                ''',
                'cieifinterfacetable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfNameMappingTable', REFERENCE_CLASS, 'Cieifnamemappingtable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifnamemappingtable', 
                [], [], 
                '''                This table contains objects for providing
                the 'ifName' to 'ifIndex' mapping.
                This table contains one entry for each
                valid 'ifName' available in the system.
                Upon the first request, the implementation
                of this table will get all the available
                ifNames, and it will populate the entries
                in this table, it maintains this ifNames
                in a cache for ~30 seconds.
                ''',
                'cieifnamemappingtable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfPacketStatsTable', REFERENCE_CLASS, 'Cieifpacketstatstable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifpacketstatstable', 
                [], [], 
                '''                This  table contains interface packet
                statistics which are not available in 
                IF-MIB(RFC2863). 
                
                As an example, some interfaces to which
                objects in this table are applicable are
                as follows :
                
                        o Ethernet
                        o FastEthernet
                        o ATM
                        o BRI
                        o Sonet
                        o GigabitEthernet
                
                Some objects defined in this table may be 
                applicable to physical interfaces only.
                As a result, this table may be sparse for
                some logical interfaces.
                ''',
                'cieifpacketstatstable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfStatusListTable', REFERENCE_CLASS, 'Cieifstatuslisttable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifstatuslisttable', 
                [], [], 
                '''                This table contains objects for providing
                the 'ifIndex', interface operational mode and 
                interface operational cause for all the 
                interfaces in the modules.
                
                This table contains one entry for each 
                64 interfaces in an module.
                
                This table provides efficient way of encoding 
                'ifIndex', interface operational mode and
                interface operational cause, from the point 
                of retrieval, by combining the values a set 
                of 64 interfaces in a single MIB object.
                ''',
                'cieifstatuslisttable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfUtilTable', REFERENCE_CLASS, 'Cieifutiltable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifutiltable', 
                [], [], 
                '''                This table contains the interface utilization
                rates for inbound and outbound traffic on an
                interface.
                ''',
                'cieifutiltable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('cieIfVlStatsTable', REFERENCE_CLASS, 'Cieifvlstatstable' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Cieifvlstatstable', 
                [], [], 
                '''                This table contains VL (Virtual Link) statistics
                for a capable interface.
                
                Objects defined in this table may be 
                applicable to physical interfaces only.
                ''',
                'cieifvlstatstable',
                'CISCO-IF-EXTENSION-MIB', False),
            _MetaInfoClassMember('ciscoIfExtSystemConfig', REFERENCE_CLASS, 'Ciscoifextsystemconfig' , 'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB', 'CiscoIfExtensionMib.Ciscoifextsystemconfig', 
                [], [], 
                '''                ''',
                'ciscoifextsystemconfig',
                'CISCO-IF-EXTENSION-MIB', False),
            ],
            'CISCO-IF-EXTENSION-MIB',
            'CISCO-IF-EXTENSION-MIB',
            _yang_ns._namespaces['CISCO-IF-EXTENSION-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IF_EXTENSION_MIB'
        ),
    },
}
_meta_table['CiscoIfExtensionMib.Cieifpacketstatstable.Cieifpacketstatsentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifpacketstatstable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifinterfacetable.Cieifinterfaceentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifinterfacetable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifstatuslisttable.Cieifstatuslistentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifstatuslisttable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifvlstatstable.Cieifvlstatsentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifvlstatstable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifindexpersistencetable.Cieifindexpersistenceentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifindexpersistencetable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable.Cieifdot1Qcustomethertypeentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifutiltable.Cieifutilentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifutiltable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifdot1Dbasemappingtable.Cieifdot1Dbasemappingentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifdot1Dbasemappingtable']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifnamemappingtable.Cieifnamemappingentry']['meta_info'].parent =_meta_table['CiscoIfExtensionMib.Cieifnamemappingtable']['meta_info']
_meta_table['CiscoIfExtensionMib.Ciscoifextsystemconfig']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifpacketstatstable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifinterfacetable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifstatuslisttable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifvlstatstable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifindexpersistencetable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifdot1Qcustomethertypetable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifutiltable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifdot1Dbasemappingtable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
_meta_table['CiscoIfExtensionMib.Cieifnamemappingtable']['meta_info'].parent =_meta_table['CiscoIfExtensionMib']['meta_info']
