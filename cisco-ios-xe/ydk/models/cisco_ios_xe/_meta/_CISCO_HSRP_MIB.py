


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HsrpstateEnum' : _MetaInfoEnum('HsrpstateEnum', 'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB',
        {
            'initial':'initial',
            'learn':'learn',
            'listen':'listen',
            'speak':'speak',
            'standby':'standby',
            'active':'active',
        }, 'CISCO-HSRP-MIB', _yang_ns._namespaces['CISCO-HSRP-MIB']),
    'CiscoHsrpMib.Chsrpglobalconfig' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpMib.Chsrpglobalconfig',
            False, 
            [
            _MetaInfoClassMember('cHsrpConfigTimeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                The amount of time in minutes a row in cHsrpGrpTable can
                remain in a state other than active before being timed out.
                ''',
                'chsrpconfigtimeout',
                'CISCO-HSRP-MIB', False),
            ],
            'CISCO-HSRP-MIB',
            'cHsrpGlobalConfig',
            _yang_ns._namespaces['CISCO-HSRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB'
        ),
    },
    'CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-HSRP-MIB', True),
            _MetaInfoClassMember('cHsrpGrpNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object along with the ifIndex of a particular interface
                uniquely identifies an HSRP group.
                
                Group numbers 0,1 and 2 are the only valid group numbers
                for TokenRing interfaces. For other media types, numbers
                range from 0 to 255. Each interface has its own set of group
                numbers. There's no relationship between the groups
                configured on different interfaces. Using a group number
                on one interface doesn't preclude using the same group
                number on a different interface. For example, there can be
                a group 1 on an Ethernet and a group 1 on Token Ring. More
                details can be found from RFC 2281.
                ''',
                'chsrpgrpnumber',
                'CISCO-HSRP-MIB', True),
            _MetaInfoClassMember('cHsrpGrpActiveRouter', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Ip Address of the currently active router for this group.
                ''',
                'chsrpgrpactiverouter',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpAuth', ATTRIBUTE, 'str' , None, None, 
                [(0, 8)], [], 
                '''                This is an unencrypted authentication string which is
                carried in all HSRP messages. An authentication string
                mismatch prevents a router interface from learning the
                designated IP address or HSRP timer values from
                other HSRP-enabled routers with the same group number.
                
                The function of this object is not to supply any sort of
                security-like authentication but rather to confirm that
                what's happening is what's intended. In other words, this
                is meant for sanity checking only.
                ''',
                'chsrpgrpauth',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpConfiguredHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If cHsrpGrpUseConfiguredTimers is true,
                cHsrpGrpConfiguredHelloTime is used when this router is an
                active router. Otherwise, the Hellotime learned from the
                current active router is used. All routers on a particular
                LAN segment must use the same Hellotime.
                ''',
                'chsrpgrpconfiguredhellotime',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpConfiguredHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If cHsrpGrpUseConfiguredTimers is true,
                cHsrpGrpConfiguredHoldTime is used when this router is an
                active router. Otherwise, the Holdtime learned from the
                current active router is used. All routers on a particular
                LAN segment should use the same Holdtime. Also, the
                Holdtime should be at least three times the value of the
                Hellotime and must be greater than the Hellotime.
                ''',
                'chsrpgrpconfiguredholdtime',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpEntryRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The control that allows modification, creation, and
                deletion of entries.  For detailed rules see the
                DESCRIPTION for cHsrpGrpEntry.
                ''',
                'chsrpgrpentryrowstatus',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpIpNone', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the disable HSRP IPv4 virtual
                IP address.
                ''',
                'chsrpgrpipnone',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpLearnedHelloTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the Hellotime is not configured on a router, it can be
                learned from the Hello messages from active router,
                provided the Hello message is authenticated. If the
                Hellotime is not learned from a Hello message from the
                active router and it is not manually configured, a default
                value of 3 seconds is recommended.
                ''',
                'chsrpgrplearnedhellotime',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpLearnedHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the Holdtime is not configured on a router, it can be
                learned from the Hello message from the active router.
                Holdtime should be learned only if the Hello message is
                authenticated. If the Holdtime is not learned and it is
                not manually configured, a default value of 10 seconds is 
                recommended.
                ''',
                'chsrpgrplearnedholdtime',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpPreempt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object, if TRUE, indicates that the current router
                should attempt to overthrow a lower priority active router
                and attempt to become the active router. If this object is
                FALSE, the router will become the active router only if
                there is no such router (or if an active router fails).
                ''',
                'chsrpgrppreempt',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpPreemptDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                This delay is the time difference between a router power
                up and the time it can actually start preempting the
                currently active router.
                
                When a router first comes up, it doesn't have a complete
                routing table. If it's configured to preempt, then it will
                become the Active router, but it will not be able to
                provide adequate routing services. The solution to this is
                to allow for a configurable delay before the router
                actually preempts the currently active router.
                ''',
                'chsrpgrppreemptdelay',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The cHsrpGrpPriority helps to select the active and the
                standby routers. The router with the highest priority is
                selected as the active router. In the priority range of 0
                to 255, 0 is the lowest priority and 255 is the highest
                priority.
                
                If two (or more) routers in a group have the same priority,
                the one with the highest ip address of the interface is the
                active router. When the active router fails to send a Hello
                message within a configurable period of time, the standby
                router with the highest priority becomes the active
                router.
                
                A router with highest priority will only attempt to
                overthrow a lower priority active router if it is
                configured to preempt.  But, if there is more than one
                router which is not active, the highest priority non-active
                router becomes the standby router.
                ''',
                'chsrpgrppriority',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpStandbyRouter', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Ip Address of the currently standby router for this
                group.
                ''',
                'chsrpgrpstandbyrouter',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpStandbyState', REFERENCE_ENUM_CLASS, 'HsrpstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB', 'HsrpstateEnum', 
                [], [], 
                '''                The current HSRP state of this group on this interface.
                ''',
                'chsrpgrpstandbystate',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpUseConfiguredTimers', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                HSRP routers learn a group's Hellotime or Holdtime from
                hello messages.
                
                The Hellotime is used to determine the frequency of
                generating hello messages when this router becomes the
                active or standby router. The Holdtime is the interval
                between the receipt of a Hello message and the presumption
                that the sending router has failed.
                
                If this object is TRUE, the cHsrpGrpConfiguredHelloTime and
                cHsrpGrpConfiguredHoldTime will be used. If it is FALSE,
                the Hellotime and Holdtime values are learned.
                ''',
                'chsrpgrpuseconfiguredtimers',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpUseConfigVirtualIpAddr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is TRUE, cHsrpGrpVirtualIpAddr was a
                configured one. Otherwise, it indicates that 
                cHsrpGrpVirtualIpAddr was a learned one.
                ''',
                'chsrpgrpuseconfigvirtualipaddr',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpVirtualIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This is the primary virtual IP address used by this
                group.  If this address is configured (i.e a non zero ip
                address), this value is used. Otherwise, the agent will
                attempt to discover the virtual address through a discovery
                process (which scans the hello messages).
                ''',
                'chsrpgrpvirtualipaddr',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpVirtualMacAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Mac Addresses used are as specified in RFC 2281. For
                ethernet and fddi interfaces, a MAC address will be in the
                range 00:00:0c:07:ac:00 through 00:00:0c:07:ac:ff. The last
                octet is the hexadecimal equivalent of cHsrpGrpNumber
                (0-255).
                
                Some Ethernet and FDDI interfaces allow a unicast MAC
                address for each HSRP group. Certain Ethernet
                chipsets(LANCE Ethernet, VGANYLAN and QUICC Ethernet) only
                support a single Unicast Mac Address. In this case, only
                one HSRP group is allowed.
                
                For TokenRing interfaces, the following three MAC 
                addresses are permitted (functional addresses):
                             C0:00:00:01:00:00
                             C0:00:00:02:00:00
                             C0:00:00:04:00:00.
                ''',
                'chsrpgrpvirtualmacaddr',
                'CISCO-HSRP-MIB', False),
            ],
            'CISCO-HSRP-MIB',
            'cHsrpGrpEntry',
            _yang_ns._namespaces['CISCO-HSRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB'
        ),
    },
    'CiscoHsrpMib.Chsrpgrptable' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpMib.Chsrpgrptable',
            False, 
            [
            _MetaInfoClassMember('cHsrpGrpEntry', REFERENCE_LIST, 'Chsrpgrpentry' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB', 'CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry', 
                [], [], 
                '''                Information about an HSRP group. Management applications
                use cHsrpGrpRowStatus to control entry modification,
                creation and deletion.
                
                Setting cHsrpGrpRowStatus to 'active' causes the router to
                communicate using HSRP.
                
                The value of cHsrpGrpRowStatus may be set to 'destroy' at
                any time.
                
                Entries may not be created via SNMP without explicitly 
                setting cHsrpGrpRowStatus to either 'createAndGo' or 
                'createAndWait'.
                
                Entries can be created and modified via the management 
                protocol or by the device's local management interface.
                
                A management application wishing to create an entry should
                choose the ifIndex of the interface which is to be added
                as part of an HSRP group. Also, a cHsrpGrpNumber should
                be chosen. A group number is unique only amongst the groups 
                on a particular interface. The value of the group number
                appears in packets which are transmitted and received on a 
                LAN segment to which the router is connected. The application
                must select the group number as explained in the description
                for cHsrpGrpNumber.
                
                If the row is not active, and a local management interface
                command modifies that row, the row may transition to active
                state.
                
                A row which is not in active state will timeout after a
                configurable period (five minutes by default). This timeout 
                period can be changed by setting cHsrpConfigTimeout.
                ''',
                'chsrpgrpentry',
                'CISCO-HSRP-MIB', False),
            ],
            'CISCO-HSRP-MIB',
            'cHsrpGrpTable',
            _yang_ns._namespaces['CISCO-HSRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB'
        ),
    },
    'CiscoHsrpMib' : {
        'meta_info' : _MetaInfoClass('CiscoHsrpMib',
            False, 
            [
            _MetaInfoClassMember('cHsrpGlobalConfig', REFERENCE_CLASS, 'Chsrpglobalconfig' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB', 'CiscoHsrpMib.Chsrpglobalconfig', 
                [], [], 
                '''                ''',
                'chsrpglobalconfig',
                'CISCO-HSRP-MIB', False),
            _MetaInfoClassMember('cHsrpGrpTable', REFERENCE_CLASS, 'Chsrpgrptable' , 'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB', 'CiscoHsrpMib.Chsrpgrptable', 
                [], [], 
                '''                A table containing information on each HSRP group
                for each interface.
                ''',
                'chsrpgrptable',
                'CISCO-HSRP-MIB', False),
            ],
            'CISCO-HSRP-MIB',
            'CISCO-HSRP-MIB',
            _yang_ns._namespaces['CISCO-HSRP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_HSRP_MIB'
        ),
    },
}
_meta_table['CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry']['meta_info'].parent =_meta_table['CiscoHsrpMib.Chsrpgrptable']['meta_info']
_meta_table['CiscoHsrpMib.Chsrpglobalconfig']['meta_info'].parent =_meta_table['CiscoHsrpMib']['meta_info']
_meta_table['CiscoHsrpMib.Chsrpgrptable']['meta_info'].parent =_meta_table['CiscoHsrpMib']['meta_info']
