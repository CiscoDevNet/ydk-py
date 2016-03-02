


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-PPPOE-MIB', True),
            _MetaInfoClassMember('cPppoeFwdedSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of PPPoE sessions which are in Forwarded(FWDED)
                state on a particular physical interface.
                ''',
                'cpppoefwdedsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoePerInterfaceSessionLossPercent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object is used to monitor the percentage of PPPoE 
                sessions loss on a particular physical interface 
                including all of its sub-interfaces. If during a 
                configured interval of time, percentage of PPPoE 
                sessions lost on a physical interface is above this 
                object value we send a trap.
                ''',
                'cpppoeperinterfacesessionlosspercent',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoePerInterfaceSessionLossThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object is used to monitor number of active PPPoE 
                sessions, initiated from a particular physical interface. 
                The sssion count is accumulation of all the pppoe session 
                came on a physical and its sub-interfaces. If this count 
                drops below this object water mark, we expect some 
                problem and send out trap indicating drop of sessions 
                below watermark.
                ''',
                'cpppoeperinterfacesessionlossthreshold',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoePtaSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of PPPoE sessions which are in PPP Termination  
                Aggregation(PTA) state on a particular physical 
                interface.
                ''',
                'cpppoeptasessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeTotalSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of PPPoE sessions which includes PPP
                Termination Aggregation(PTA), Forwarded(FWDED) and 
                Transient(TRANS) state on a physical interface. 
                ''',
                'cpppoetotalsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeTransSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of PPPoE sessions which are in Transient(TRANS)
                state on a particular physical interface.
                ''',
                'cpppoetranssessions',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'cPppoeSessionsPerInterfaceEntry',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
    'CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('cPppoeSessionsPerInterfaceEntry', REFERENCE_LIST, 'CPppoeSessionsPerInterfaceEntry' , 'ydk.models.pppoe.CISCO_PPPOE_MIB', 'CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry', 
                [], [], 
                '''                An entry in the table containing PPPoE sessions 
                information such as count information of various 
                states like PPP Termination Aggregation(PTA), 
                Forwarded(FWDED), Transient (TRANS) and TOTAL count and 
                the configured loss threshold per given physical 
                interface
                ''',
                'cpppoesessionsperinterfaceentry',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'cPppoeSessionsPerInterfaceTable',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
    'CISCOPPPOEMIB.CPppoeSystemSessionInfo' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB.CPppoeSystemSessionInfo',
            False, 
            [
            _MetaInfoClassMember('cPppoeSystemCurrSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of active PPPoE sessions within 
                this system.
                ''',
                'cpppoesystemcurrsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemExceededSessionErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The accumulated number of errors for 
                establishing PPPoE session in the system due 
                to the cPppoeSystemCurrSessions value exceeds 
                the cPppoeSystemMaxAllowedSessions value.
                ''',
                'cpppoesystemexceededsessionerrors',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemHighWaterSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The high water mark of the established PPPoE 
                sessions since the system was initialized.
                ''',
                'cpppoesystemhighwatersessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemMaxAllowedSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum number of allowed PPPoE sessions within
                the system.
                ''',
                'cpppoesystemmaxallowedsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerMacIWFSessionlimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides limit on number of PPPoE sessions 
                with interworking flag(IWF) enabled, from a single client
                MAC address. If the limit is reached new session request 
                would be denied.
                ''',
                'cpppoesystempermaciwfsessionlimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerMacSessionlimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides limit on number of PPPoE sessions
                for a single client Ethernet MAC address. If the limit 
                is reached new session request from the client would 
                be denied
                ''',
                'cpppoesystempermacsessionlimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerMacThrottleRatelimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the rate limit at which PPPoE 
                session were created from a single client MAC address. 
                During a configured time interval, once the number of 
                new session requests coming from a particular client 
                MAC address reaches this limit, it's expected to have 
                delay in response for those clients.
                ''',
                'cpppoesystempermacthrottleratelimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerVClimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides limit on number of PPPoE sessions on 
                a particular ATM-VC. If the limit is reached new session 
                request on this VC would be denied.
                ''',
                'cpppoesystempervclimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerVCThrottleRatelimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the rate limit at which PPPoE 
                session were created on an ATM-VC. During a configured 
                time interval, once the number of new session requests 
                coming on an ATM-VC reaches this limit, it's expected to 
                have delay in response for those clients on this VC.
                ''',
                'cpppoesystempervcthrottleratelimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerVLANlimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides limit on number of PPPoE sessions 
                on a particular Vlan. If the limit is reached new session 
                request on this vlan would be denied.
                ''',
                'cpppoesystempervlanlimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemPerVLANthrottleRatelimit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the rate limit at which PPPoE 
                session were created on a Vlan. During a configured
                time interval once the number of new session requests 
                coming on a particular Vlan reaches this limit, 
                it's expected to have delay in response for client 
                on this Vlan.
                ''',
                'cpppoesystempervlanthrottleratelimit',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemSessionLossPercent', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This object is used to monitor the percentage of PPPoE 
                sessions going down at a configured time interval.
                   
                During a time interval if percentage of PPPoE sessions 
                lost, falls above this object value, we send trap 
                indicating loss of sessions above percentage expected.
                ''',
                'cpppoesystemsessionlosspercent',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemSessionLossThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object is used to monitor number of active PPPoE 
                sessions above a healthy watermark. If number of PPPoE
                sessions falls below this watermark then we can expect
                something wrong happened.  So we send out trap to user
                indicating session loss below watermark.
                ''',
                'cpppoesystemsessionlossthreshold',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemThresholdSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Threshold value of the established PPPoE sessions 
                within the system. Default value is equal to
                cPppoeSystemMaxSessionsConfigurable
                ''',
                'cpppoesystemthresholdsessions',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'cPppoeSystemSessionInfo',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
    'CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry',
            False, 
            [
            _MetaInfoClassMember('atmVclVci', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                ''',
                'atmvclvci',
                'CISCO-PPPOE-MIB', True),
            _MetaInfoClassMember('atmVclVpi', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'atmvclvpi',
                'CISCO-PPPOE-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-PPPOE-MIB', True),
            _MetaInfoClassMember('cPppoeVcCurrSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of active PPPoE sessions on 
                the VCL.
                ''',
                'cpppoevccurrsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeVcExceededSessionErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The accumulated number of errors for 
                establishing PPPoE session in the VC 
                due to the cPppoeVcCurrSessions value
                exceeds the cPppoeVcMaxAllowedSessions 
                value.
                ''',
                'cpppoevcexceededsessionerrors',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeVcHighWaterSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The high water mark of the established PPPoE 
                sessions on the VCL.
                ''',
                'cpppoevchighwatersessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeVcMaxAllowedSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of allowed PPPoE sessions on 
                the VCL.
                ''',
                'cpppoevcmaxallowedsessions',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeVcThresholdSessions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Threshold value of the established PPPoE 
                sessions on the VCL. Default value is equal to 
                cPppoeVcMaxAllowedSessions.
                ''',
                'cpppoevcthresholdsessions',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'cPppoeVcSessionsEntry',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
    'CISCOPPPOEMIB.CPppoeVcSessionsTable' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB.CPppoeVcSessionsTable',
            False, 
            [
            _MetaInfoClassMember('cPppoeVcSessionsEntry', REFERENCE_LIST, 'CPppoeVcSessionsEntry' , 'ydk.models.pppoe.CISCO_PPPOE_MIB', 'CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry', 
                [], [], 
                '''                An entry in the table containing PPPoE session
                related information on a VCL. The entry of this
                table is created when the value of cPppoeVcEnable 
                object is set to `true` for the entry associated 
                VCL. The entry of this table is deleted when the
                of cPppoeVcEnable object set to `false` or the
                entry associated VCL is deleted from 
                atmVclTable.
                ''',
                'cpppoevcsessionsentry',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'cPppoeVcSessionsTable',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
    'CISCOPPPOEMIB' : {
        'meta_info' : _MetaInfoClass('CISCOPPPOEMIB',
            False, 
            [
            _MetaInfoClassMember('cPppoeSessionsPerInterfaceTable', REFERENCE_CLASS, 'CPppoeSessionsPerInterfaceTable' , 'ydk.models.pppoe.CISCO_PPPOE_MIB', 'CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable', 
                [], [], 
                '''                A list of interfaces' PPPoE session information.
                ''',
                'cpppoesessionsperinterfacetable',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeSystemSessionInfo', REFERENCE_CLASS, 'CPppoeSystemSessionInfo' , 'ydk.models.pppoe.CISCO_PPPOE_MIB', 'CISCOPPPOEMIB.CPppoeSystemSessionInfo', 
                [], [], 
                '''                ''',
                'cpppoesystemsessioninfo',
                'CISCO-PPPOE-MIB', False),
            _MetaInfoClassMember('cPppoeVcSessionsTable', REFERENCE_CLASS, 'CPppoeVcSessionsTable' , 'ydk.models.pppoe.CISCO_PPPOE_MIB', 'CISCOPPPOEMIB.CPppoeVcSessionsTable', 
                [], [], 
                '''                Table of configuration and statistics about the 
                number of PPPoE sessions on a list of VCLs(ATM 
                Interface Virtual Channel Link).
                ''',
                'cpppoevcsessionstable',
                'CISCO-PPPOE-MIB', False),
            ],
            'CISCO-PPPOE-MIB',
            'CISCO-PPPOE-MIB',
            _yang_ns._namespaces['CISCO-PPPOE-MIB'],
        'ydk.models.pppoe.CISCO_PPPOE_MIB'
        ),
    },
}
_meta_table['CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable.CPppoeSessionsPerInterfaceEntry']['meta_info'].parent =_meta_table['CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable']['meta_info']
_meta_table['CISCOPPPOEMIB.CPppoeVcSessionsTable.CPppoeVcSessionsEntry']['meta_info'].parent =_meta_table['CISCOPPPOEMIB.CPppoeVcSessionsTable']['meta_info']
_meta_table['CISCOPPPOEMIB.CPppoeSessionsPerInterfaceTable']['meta_info'].parent =_meta_table['CISCOPPPOEMIB']['meta_info']
_meta_table['CISCOPPPOEMIB.CPppoeSystemSessionInfo']['meta_info'].parent =_meta_table['CISCOPPPOEMIB']['meta_info']
_meta_table['CISCOPPPOEMIB.CPppoeVcSessionsTable']['meta_info'].parent =_meta_table['CISCOPPPOEMIB']['meta_info']
