


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'UnicastrpftypeEnum' : _MetaInfoEnum('UnicastrpftypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB',
        {
            'strict':'strict',
            'loose':'loose',
            'disabled':'disabled',
        }, 'CISCO-IP-URPF-MIB', _yang_ns._namespaces['CISCO-IP-URPF-MIB']),
    'CiscoIpUrpfMib.Cipurpfscalar' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfscalar',
            False, 
            [
            _MetaInfoClassMember('cipUrpfComputeInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                The time between rate computations. This global value
                applies for the computation of all URPF rates, global
                and per-interface.
                
                When the value of cipUrpfComputeInterval is changed,
                the interval in-progress proceeds as though the value
                had not changed. The change will apply to the length
                of subsequent intervals.
                
                The cipUrpfComputeInterval must be less than or equal 
                to the cipUrpfDropRateWindow.
                ''',
                'cipurpfcomputeinterval',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfDropNotifyHoldDownTime', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                The minimum time between issuance of
                cipUrpfIfDropRateNotify notifications for a 
                particular interface and packet forwarding type.
                
                Notifications are generated for each interface and
                packet forwarding type that exceeds the drop-rate. 
                When a Notify is sent because the drop-rate is 
                exceeded for a particular interface and forwarding
                type, the time specified by this object is used to 
                specify the minimum time that must elapse before 
                another Notify can be sent for that interface and
                forwarding type. The time is specified globally but 
                used individually.
                ''',
                'cipurpfdropnotifyholddowntime',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfDropRateWindow', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                The window of time in the recent past over which the drop
                count used in the drop rate computation is collected. 
                This global value applies for the computation of all URPF 
                rates, global and per-interface. 
                
                Once the period over which computations have been 
                performed exceeds cipUrpfDropRateWindow, every time a 
                computation is performed, the window slides up to end 
                at the current time and start at cipUrpfDropRateWindow 
                seconds before. 
                
                The cipUrpfDropRateWindow must be greater than
                or equal to the interval between computations 
                (cipUrpfComputeInterval).
                
                Since the agent must save the drop count values
                for each compute interval in order to slide the window,
                the number of counts saved is the quotient of
                cipUrpfDropRateWindow divided by cipUrpfComputeInterval.
                ''',
                'cipurpfdropratewindow',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfScalar',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpftable.Cipurpfentry.CipurpfipversionEnum' : _MetaInfoEnum('CipurpfipversionEnum', 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'CISCO-IP-URPF-MIB', _yang_ns._namespaces['CISCO-IP-URPF-MIB']),
    'CiscoIpUrpfMib.Cipurpftable.Cipurpfentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpftable.Cipurpfentry',
            False, 
            [
            _MetaInfoClassMember('cipUrpfIpVersion', REFERENCE_ENUM_CLASS, 'CipurpfipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpftable.Cipurpfentry.CipurpfipversionEnum', 
                [], [], 
                '''                Specifies the version of IP forwarding on an interface
                to which the table row URPF counts, rates, and
                configuration apply.
                ''',
                'cipurpfipversion',
                'CISCO-IP-URPF-MIB', True),
            _MetaInfoClassMember('cipUrpfDropRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The rate of packet drops of IP version cipUrpfIpVersion
                packets due to URPF for the managed device. The
                per-interface drop rate notification is issued on rates
                exceeding a limit (rising rate). This dropping may indicate
                an security attack on the network. To determine whether the
                attack/event is over, the NMS must consult the managed
                device. This object can be polled to determine the recent
                drop rate for the managed device as a whole, in addition to
                querying particular interface objects. 
                This object is the
                average rate of dropping over the most recent window of
                time. The rate is computed by dividing the number of packets
                dropped over a window by the window time in seconds. The
                window time is specified by cipUrpfDropRateWindow. Each time
                the drop rate is computed, and at system startup, a snapshot
                is taken of the latest value of cipUrpfDrops. Subtracting
                from this the snapshot of cipUrpfDrops at the start of the
                current window of time gives the number of packets dropped.
                The drop rate is computed every cipUrpfComputeInterval
                seconds. As an example, let cipUrpfDropRateWindow be 300
                seconds, and cipUrpfComputeInterval 30 seconds. Every 30
                seconds, the drop count five minutes previous is subtracted
                from the current drop count, and the result is divided by
                300 to arrive at the drop rate. 
                At device start-up, until
                the device has been up more than cipUrpfDropRateWindow, when
                drop rate is computed, the value of cipUrpfDrops is divided
                by the time the device has been up. 
                After the device has
                been up for cipUrpfDropRateWindow, when drop rate is
                computed, the number of packet drops counted from interval
                start time to the computation time is divided by
                cipUrpfDropRateWindow. 
                Changes to cipUrpfDropRateWindow are
                not reflected in this object until the next computation
                time. 
                The rate from the most recent computation is the
                value fetched until the subsequent computation is
                performed.
                ''',
                'cipurpfdroprate',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sum of dropped IP version cipUrpfIpVersion packets failing
                a URPF check. This value is the sum of drops of packets 
                received on all interfaces of the managed device.
                ''',
                'cipurpfdrops',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfEntry',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpftable' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpftable',
            False, 
            [
            _MetaInfoClassMember('cipUrpfEntry', REFERENCE_LIST, 'Cipurpfentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpftable.Cipurpfentry', 
                [], [], 
                '''                If the managed device supports URPF dropping,
                a row exists for each IP version type (v4 and v6).
                A row contains summary information on URPF
                dropping over the entire managed device.
                ''',
                'cipurpfentry',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfTable',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifcheckstrictEnum' : _MetaInfoEnum('CipurpfifcheckstrictEnum', 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'CISCO-IP-URPF-MIB', _yang_ns._namespaces['CISCO-IP-URPF-MIB']),
    'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifipversionEnum' : _MetaInfoEnum('CipurpfifipversionEnum', 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'CISCO-IP-URPF-MIB', _yang_ns._namespaces['CISCO-IP-URPF-MIB']),
    'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifwhichroutetableidEnum' : _MetaInfoEnum('CipurpfifwhichroutetableidEnum', 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB',
        {
            'default':'default',
            'vrf':'vrf',
        }, 'CISCO-IP-URPF-MIB', _yang_ns._namespaces['CISCO-IP-URPF-MIB']),
    'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IP-URPF-MIB', True),
            _MetaInfoClassMember('cipUrpfIfIpVersion', REFERENCE_ENUM_CLASS, 'CipurpfifipversionEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifipversionEnum', 
                [], [], 
                '''                Specifies the version of IP forwarding on an interface
                to which the table row URPF counts, rates, and 
                configuration apply.
                ''',
                'cipurpfifipversion',
                'CISCO-IP-URPF-MIB', True),
            _MetaInfoClassMember('cipUrpfIfCheckStrict', REFERENCE_ENUM_CLASS, 'CipurpfifcheckstrictEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifcheckstrictEnum', 
                [], [], 
                '''                Interface configuration indicating the strictness of
                the reachability check performed 
                on the interface.
                - strict: check that source addr is reachable via 
                          the interface it came in on.
                - loose : check that source addr is reachable via 
                          some interface on the device.
                ''',
                'cipurpfifcheckstrict',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent
                occasion at which this interface's  counters
                suffered  a discontinuity.
                If no such discontinuities have occurred
                since the last re-initialization of the
                local management subsystem, then this
                object contains a value of zero.
                ''',
                'cipurpfifdiscontinuitytime',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfDropRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The rate of packet drops of IP version cipUrpfIfIpVersion
                packets due to URPF on the interface. 
                
                This object is the average rate of dropping over the most 
                recent interval of time. The rate is computed by dividing
                the number of packets dropped over an interval by the 
                interval time in seconds. Each time the drop rate
                is computed, and at system startup, a snapshot is taken
                of the latest value of cipUrpfIfDrops. Subtracting from this
                the snapshot of cipUrpfIfDrops at the start of the current
                interval of time gives the number of packets dropped.
                The drop rate is computed every cipUrpfComputeInterval
                seconds.
                
                When drop rate is computed, if time since the creation of 
                a row in cipUrpfIfMonTable is less than 
                cipUrpfDropRateWindow, the value of cipUrpfIfDrops is 
                divided by the time since row was created.
                
                After the row has been in existence for 
                cipUrpfDropRateWindow, when drop rate is computed, the 
                number of packet drops counted on the interface from 
                interval start time to the computation time is divided 
                by cipUrpfDropRateWindow.
                
                Changes to cipUrpfDropRateWindow are not reflected in this
                object until the next computation time.
                
                The rate from the  most recent computation is the value 
                fetched until the subsequent computation is performed.
                ''',
                'cipurpfifdroprate',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfDropRateNotifyEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the system produces the
                cipUrpfIfDropRateNotify notification as a result of URPF 
                dropping of version cipUrpfIfIpVersion IP packets on this 
                interface. A false value prevents such notifications from 
                being generated by this system.
                ''',
                'cipurpfifdropratenotifyenable',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP packets of version cipUrpfIfIpVersion
                failing the URPF check and dropped by the managed device
                on a particular interface.
                
                Discontinuities in the value of this variable can occur 
                at re-initialization of the management system, and at 
                other times as indicated by the values of 
                cipUrpfIfDiscontinuityTime.
                ''',
                'cipurpfifdrops',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfNotifyDrHoldDownReset', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Setting this object to true causes the five-minute
                hold-down timer for emitting URPF drop rate 
                notifications for IP version cipUrpfIfIpVersion on 
                the interface to be short-circuited.  If a notification 
                is due and would be emitted for the interface if the 
                five-minutes elapsed, setting this object will cause 
                the notification to be sent.
                
                This is a trigger, and doesn't hold information. It is
                set and an action is performed. Therefore a get for 
                this object always returns false.
                ''',
                'cipurpfifnotifydrholddownreset',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfNotifyDropRateThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the calculated rate of URPF packet drops
                (cipUrpfIfDropRate) meets or exceeds the value 
                specified by this object, a cipUrpfIfDropRateNotify 
                notification is sent if cipUrpfIfDropRateNotifyEnable 
                is set to true, and no such notification for the
                IP version has been sent for this interface for the 
                hold-down period.
                
                Note that due to the calculation used for drop rate, 
                if there are less than n drop events in an n-second
                period the notification will not be generated. To allow
                for the detection of a small number of drop events, the
                value 0 (zero) is used to indicate that if any drop events
                occur during the interval, a notification is generated.
                ''',
                'cipurpfifnotifydropratethreshold',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfSuppressedDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP packets of version cipUrpfIfIpVersion
                failing the URPF check but given a reprieve and not 
                dropped by the managed device. Depending on the 
                device configuration and capabilities, the following 
                cases may cause incrementing of the counter: 
                - if the managed device is configured to allow self-pings 
                  and the managed device pings itself.
                - if the managed device is configured for loose URPF (if any
                  interface has a route to the source), and the strict
                  case fails while the loose case passes.
                - DHCP Request packets (src 0.0.0.0 dst 255.255.255.255) 
                  will pass after initially being marked for drop.
                - RIP routing on unnumbered interfaces will pass after 
                  initially being marked for drop.
                - multicast packets will pass after initially being marked 
                  for drop
                - ACL's can be applied to permit packets after initially 
                  being marked for drop.
                
                Discontinuities in the value of this variable can occur 
                at re-initialization of the management system, and at 
                other times as indicated by the values of 
                cipUrpfIfDiscontinuityTime.
                ''',
                'cipurpfifsuppresseddrops',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                If the value of cipUrpfIfWhichRouteTableID is 'vrf',
                the name of the VRF Table. Otherwise a zero-length
                string.
                ''',
                'cipurpfifvrfname',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfIfWhichRouteTableID', REFERENCE_ENUM_CLASS, 'CipurpfifwhichroutetableidEnum' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry.CipurpfifwhichroutetableidEnum', 
                [], [], 
                '''                Interface configuration indicating the routing table
                consulted for the reachability check:
                - default: the non-private routing table for of the 
                           managed system.
                - vrf   : a particular VPN routing table.
                ''',
                'cipurpfifwhichroutetableid',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfIfMonEntry',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfifmontable' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfifmontable',
            False, 
            [
            _MetaInfoClassMember('cipUrpfIfMonEntry', REFERENCE_LIST, 'Cipurpfifmonentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry', 
                [], [], 
                '''                If IPv4 packet forwarding is configured on an interface,
                and is configured to perform URPF checking, a row appears
                in this table with indices [ifIndex][ipv4]. If IPv4
                packet forwarding is deconfigured, or URPF checking
                is deconfigured, the row disappears.
                
                If IPv6 packet forwarding is configured on an interface,
                and is configured to perform URPF checking, a row appears
                in the table with indices [ifIndex][ipv6].  If IPv6
                packet forwarding is deconfigured, or URPF checking
                is deconfigured, the row disappears.
                ''',
                'cipurpfifmonentry',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfIfMonTable',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry',
            False, 
            [
            _MetaInfoClassMember('cipUrpfVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ''',
                'cipurpfvrfname',
                'CISCO-IP-URPF-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IP-URPF-MIB', True),
            _MetaInfoClassMember('cipUrpfVrfIfDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which the URPF counters for this VRF on this interface 
                suffered  a discontinuity.  If no such discontinuities 
                have occurred since the last re-initialization of the
                local management subsystem, then this object contains a 
                value of zero.
                ''',
                'cipurpfvrfifdiscontinuitytime',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfVrfIfDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets failing the URPF check for a VRF on
                the interface and dropped by the managed device.
                
                Discontinuities in the value of this variable can occur 
                at re-initialization of the management system, and at 
                other times as indicated by the values of 
                cipUrpfVrfIfDiscontinuityTime.
                ''',
                'cipurpfvrfifdrops',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfVrfIfEntry',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfvrfiftable' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfvrfiftable',
            False, 
            [
            _MetaInfoClassMember('cipUrpfVrfIfEntry', REFERENCE_LIST, 'Cipurpfvrfifentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry', 
                [], [], 
                '''                An entry exists for a VRF and interface if and only
                if the VRF associated with the interface is configured 
                to perform IP URPF checking using the routing 
                table for the VRF.
                ''',
                'cipurpfvrfifentry',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfVrfIfTable',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry',
            False, 
            [
            _MetaInfoClassMember('cipUrpfVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VRF Table
                name.
                ''',
                'cipurpfvrfname',
                'CISCO-IP-URPF-MIB', True),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfVrfEntry',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib.Cipurpfvrftable' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib.Cipurpfvrftable',
            False, 
            [
            _MetaInfoClassMember('cipUrpfVrfEntry', REFERENCE_LIST, 'Cipurpfvrfentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry', 
                [], [], 
                '''                An entry exists for a VRF if and only if the VRF
                is associated with an interface that is configured
                to perform IP URPF checking using the routing table 
                for that VRF.
                ''',
                'cipurpfvrfentry',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'cipUrpfVrfTable',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
    'CiscoIpUrpfMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpUrpfMib',
            False, 
            [
            _MetaInfoClassMember('cipUrpfIfMonTable', REFERENCE_CLASS, 'Cipurpfifmontable' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfifmontable', 
                [], [], 
                '''                This table contains information on URPF dropping on
                an interface.
                ''',
                'cipurpfifmontable',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfScalar', REFERENCE_CLASS, 'Cipurpfscalar' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfscalar', 
                [], [], 
                '''                ''',
                'cipurpfscalar',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfTable', REFERENCE_CLASS, 'Cipurpftable' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpftable', 
                [], [], 
                '''                This table contains summary information for the
                managed device on URPF dropping.
                ''',
                'cipurpftable',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfVrfIfTable', REFERENCE_CLASS, 'Cipurpfvrfiftable' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfvrfiftable', 
                [], [], 
                '''                This table contains statistics information for interfaces
                performing URPF using VRF table to determine reachability.
                ''',
                'cipurpfvrfiftable',
                'CISCO-IP-URPF-MIB', False),
            _MetaInfoClassMember('cipUrpfVrfTable', REFERENCE_CLASS, 'Cipurpfvrftable' , 'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB', 'CiscoIpUrpfMib.Cipurpfvrftable', 
                [], [], 
                '''                This table enables indexing URPF drop statistics
                by Virtual Routing and Forwarding instances.
                ''',
                'cipurpfvrftable',
                'CISCO-IP-URPF-MIB', False),
            ],
            'CISCO-IP-URPF-MIB',
            'CISCO-IP-URPF-MIB',
            _yang_ns._namespaces['CISCO-IP-URPF-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_URPF_MIB'
        ),
    },
}
_meta_table['CiscoIpUrpfMib.Cipurpftable.Cipurpfentry']['meta_info'].parent =_meta_table['CiscoIpUrpfMib.Cipurpftable']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfifmontable.Cipurpfifmonentry']['meta_info'].parent =_meta_table['CiscoIpUrpfMib.Cipurpfifmontable']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfvrfiftable.Cipurpfvrfifentry']['meta_info'].parent =_meta_table['CiscoIpUrpfMib.Cipurpfvrfiftable']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfvrftable.Cipurpfvrfentry']['meta_info'].parent =_meta_table['CiscoIpUrpfMib.Cipurpfvrftable']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfscalar']['meta_info'].parent =_meta_table['CiscoIpUrpfMib']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpftable']['meta_info'].parent =_meta_table['CiscoIpUrpfMib']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfifmontable']['meta_info'].parent =_meta_table['CiscoIpUrpfMib']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfvrfiftable']['meta_info'].parent =_meta_table['CiscoIpUrpfMib']['meta_info']
_meta_table['CiscoIpUrpfMib.Cipurpfvrftable']['meta_info'].parent =_meta_table['CiscoIpUrpfMib']['meta_info']
