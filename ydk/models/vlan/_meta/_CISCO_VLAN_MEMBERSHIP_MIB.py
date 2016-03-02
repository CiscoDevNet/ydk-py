


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOVLANMEMBERSHIPMIB.VmMembership.VmVlanCreationMode_Enum' : _MetaInfoEnum('VmVlanCreationMode_Enum', 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB',
        {
            'automatic':'AUTOMATIC',
            'manual':'MANUAL',
        }, 'CISCO-VLAN-MEMBERSHIP-MIB', _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB']),
    'CISCOVLANMEMBERSHIPMIB.VmMembership' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembership',
            False, 
            [
            _MetaInfoClassMember('vmVlanCreationMode', REFERENCE_ENUM_CLASS, 'VmVlanCreationMode_Enum' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembership.VmVlanCreationMode_Enum', 
                [], [], 
                '''                This object is used to determine whether or not
                a non-existing VLAN will be created automatically
                by the system after assigned to a port.
                
                automatic(1):  a non-existing VLAN will be created
                               automatically by the system after
                               assigned to a port.
                
                manual(2):     a non-existing VLAN will not be created
                               automatically by the system and need to be
                               manually created by the users after assigned
                               to a port.
                ''',
                'vmvlancreationmode',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembership',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry',
            False, 
            [
            _MetaInfoClassMember('vmMembershipPortRangeIndex', REFERENCE_ENUM_CLASS, 'CiscoPortListRange_Enum' , 'ydk.models.tc.CISCO_TC', 'CiscoPortListRange_Enum', 
                [], [], 
                '''                The bridge port range index of this row.
                ''',
                'vmmembershipportrangeindex',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmMembershipSummaryVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                ''',
                'vmmembershipsummaryvlanindex',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmMembershipSummaryExtPorts', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The set of the device's member ports that belong
                to the VLAN. It has the VLAN membership information
                of up to 2k ports with the port number starting from
                the information indicated in vmMembershipPortRangeIndex
                object of the same row. For example, if the value
                of vmMembershipPortRangeIndex is 'twoKto4K', the
                port number indicated in this object starting from
                2049 and ending to 4096. 
                
                A port number is the value of dot1dBasePort for
                the port in the BRIDGE-MIB (RFC 1493).
                ''',
                'vmmembershipsummaryextports',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipSummaryExtEntry',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable',
            False, 
            [
            _MetaInfoClassMember('vmMembershipSummaryExtEntry', REFERENCE_LIST, 'VmMembershipSummaryExtEntry' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry', 
                [], [], 
                '''                An entry (conceptual row) in the
                vmMembershipSummaryExtTable.
                ''',
                'vmmembershipsummaryextentry',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipSummaryExtTable',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('vmMembershipSummaryVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VLAN id of the VLAN.
                ''',
                'vmmembershipsummaryvlanindex',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmMembershipSummaryMember2kPorts', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The set of the device's member ports that belong
                to the VLAN. It has the VLAN membership information
                of up to 2048 ports with the port number from 1 to 
                2048.
                
                Each octet within the value of this object specifies a
                set of eight ports, with the first octet specifying 
                ports 1 through 8, the second octet specifying ports 9
                through 16, etc.   Within each octet, the most
                significant bit represents the lowest numbered
                port, and the least significant bit represents the
                highest numbered port.  Thus, each port of the
                VLAN is represented by a single bit within the
                value of this object.  If that bit has a value of
                '1' then that port is included in the set of
                ports; the port is not included if its bit has a
                value of '0'.
                
                A port number is the value of dot1dBasePort for
                the port in the BRIDGE-MIB (RFC 1493).
                ''',
                'vmmembershipsummarymember2kports',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmMembershipSummaryMemberPorts', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The set of the device's member ports that belong
                to the VLAN.
                
                Each octet within the value of this object specifies a
                set of eight ports, with the first octet specifying ports
                1 through 8, the second octet specifying ports 9
                through 16, etc.   Within each octet, the most
                significant bit represents the lowest numbered
                port, and the least significant bit represents the
                highest numbered port.  Thus, each port of the
                VLAN is represented by a single bit within the
                value of this object.  If that bit has a value of
                '1' then that port is included in the set of
                ports; the port is not included if its bit has a
                value of '0'.
                
                A port number is the value of dot1dBasePort for
                the port in the BRIDGE-MIB (RFC 1493).
                ''',
                'vmmembershipsummarymemberports',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipSummaryEntry',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable',
            False, 
            [
            _MetaInfoClassMember('vmMembershipSummaryEntry', REFERENCE_LIST, 'VmMembershipSummaryEntry' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry', 
                [], [], 
                '''                An entry (conceptual row) in the
                vmMembershipSummaryTable.
                ''',
                'vmmembershipsummaryentry',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipSummaryTable',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmPortStatus_Enum' : _MetaInfoEnum('VmPortStatus_Enum', 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB',
        {
            'inactive':'INACTIVE',
            'active':'ACTIVE',
            'shutdown':'SHUTDOWN',
        }, 'CISCO-VLAN-MEMBERSHIP-MIB', _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB']),
    'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmVlanType_Enum' : _MetaInfoEnum('VmVlanType_Enum', 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB',
        {
            'static':'STATIC',
            'dynamic':'DYNAMIC',
            'multiVlan':'MULTIVLAN',
        }, 'CISCO-VLAN-MEMBERSHIP-MIB', _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB']),
    'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmPortStatus', REFERENCE_ENUM_CLASS, 'VmPortStatus_Enum' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmPortStatus_Enum', 
                [], [], 
                '''                An indication of the current VLAN status of the port.
                A status of inactive(1) indicates that a dynamic port
                does not yet have a VLAN assigned, or a port is 
                assigned to a VLAN that is currently not active. A 
                status of active(2) indicates that the currently 
                assigned VLAN is active. A status of shutdown(3) 
                indicates that the port has been disabled as a result
                of VQP shutdown response.
                ''',
                'vmportstatus',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The VLAN id of the VLAN the port is assigned to
                when vmVlanType is set to static or dynamic.
                This object is not instantiated if not applicable.
                
                The value may be 0 if the port is not assigned
                to a VLAN.
                
                If vmVlanType is static, the port is always
                assigned to a VLAN and the object may not be
                set to 0.
                
                If vmVlanType is dynamic the object's value is
                0 if the port is currently not assigned to a VLAN.
                In addition, the object may be set to 0 only.
                ''',
                'vmvlan',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlans', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The VLAN(s) the port is assigned to when the
                port's vmVlanType is set to multiVlan.
                This object is not instantiated if not applicable.
                
                The port is always assigned to one or more VLANs
                and the object may not be set so that there are
                no vlans assigned.
                
                Each octet within the value of this object specifies a
                set of eight VLANs, with the first octet specifying
                VLAN id 1 through 8, the second octet specifying VLAN
                ids 9 through 16, etc.   Within each octet, the most
                significant bit represents the lowest numbered
                VLAN id, and the least significant bit represents the
                highest numbered VLAN id.  Thus, each VLAN of the
                port is represented by a single bit within the
                value of this object.  If that bit has a value of
                '1' then that VLAN is included in the set of
                VLANs; the VLAN is not included if its bit has a
                value of '0'.
                ''',
                'vmvlans',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlans2k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The VLAN(s) the port is assigned to when the
                port's vmVlanType is set to multiVlan.
                This object is not instantiated if not applicable.
                
                The port is always assigned to one or more VLANs
                and the object may not be set so that there are
                no vlans assigned.
                
                Each octet within the value of this object specifies a
                set of eight VLANs, with the first octet specifying
                VLAN id 1024 through 1031, the second octet specifying 
                VLAN ids 1032 through 1039, etc.  Within each octet, 
                the most significant bit represents the lowest 
                numbered VLAN id, and the least significant bit 
                represents the highest numbered VLAN id.  Thus, each 
                VLAN of the port is represented by a single bit within
                the value of this object.  If that bit has a value of
                '1' then that VLAN is included in the set of
                VLANs; the VLAN is not included if its bit has a
                value of '0'.
                ''',
                'vmvlans2k',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlans3k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The VLAN(s) the port is assigned to when the
                port's vmVlanType is set to multiVlan.
                This object is not instantiated if not applicable.
                
                The port is always assigned to one or more VLANs
                and the object may not be set so that there are
                no vlans assigned.
                
                Each octet within the value of this object specifies a
                set of eight VLANs, with the first octet specifying
                VLAN id 2048 through 2055, the second octet specifying 
                VLAN ids 2056 through 2063, etc.   Within each octet, 
                the most significant bit represents the lowest 
                numbered VLAN id, and the least significant bit 
                represents the highest numbered VLAN id.  Thus, each
                VLAN of the port is represented by a single bit within
                the value of this object.  If that bit has a value of
                '1' then that VLAN is included in the set of
                VLANs; the VLAN is not included if its bit has a
                value of '0'.
                ''',
                'vmvlans3k',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlans4k', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                The VLAN(s) the port is assigned to when the
                port's vmVlanType is set to multiVlan.
                This object is not instantiated if not applicable.
                
                The port is always assigned to one or more VLANs
                and the object may not be set so that there are
                no vlans assigned.
                
                Each octet within the value of this object specifies a
                set of eight VLANs, with the first octet specifying
                VLAN id 3072 through 3079, the second octet specifying 
                VLAN ids 3040 through 3047, etc.   Within each octet, 
                the most significant bit represents the lowest 
                numbered VLAN id, and the least significant bit 
                represents the highest numbered VLAN id.  Thus, each
                VLAN of the port is represented by a single bit within
                the value of this object.  If that bit has a value of
                '1' then that VLAN is included in the set of
                VLANs; the VLAN is not included if its bit has a
                value of '0'.
                ''',
                'vmvlans4k',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVlanType', REFERENCE_ENUM_CLASS, 'VmVlanType_Enum' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmVlanType_Enum', 
                [], [], 
                '''                The type of VLAN membership assigned to this port.
                A port with static vlan membership is assigned to a
                single VLAN directly. A port with dynamic membership
                is assigned a single VLAN based on content of packets
                received on the port and via VQP queries to VMPS.
                A port with multiVlan membership may be assigned to
                one or more VLANs directly.
                
                A static or dynamic port membership is specified
                by the value of vmVlan. A multiVlan port membership is
                specified by the value of vmVlans.
                ''',
                'vmvlantype',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipEntry',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmMembershipTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmMembershipTable',
            False, 
            [
            _MetaInfoClassMember('vmMembershipEntry', REFERENCE_LIST, 'VmMembershipEntry' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry', 
                [], [], 
                '''                An entry (conceptual row) in the vmMembershipTable.
                ''',
                'vmmembershipentry',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmMembershipTable',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmStatistics' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmStatistics',
            False, 
            [
            _MetaInfoClassMember('vmInsufficientResources', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, a VQP response indicates 
                insufficient resources. An insufficient resources 
                response indicates that the VMPS used does not 
                have the required resources to verify the
                membership assignment requested.
                ''',
                'vminsufficientresources',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsChanges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, the current VMPS was changed. The
                current VMPS is changed whenever the VMPS fails to 
                response after vmVmpsRetries of a VQP request.
                ''',
                'vmvmpschanges',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPDenied', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, a VQP response indicates 
                'denied'. A 'denied' response is a result of 
                the membership policy configured at a VMPS
                by the administrator.
                ''',
                'vmvqpdenied',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPQueries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of VQP requests sent by this device
                to all VMPS since last system re-initialization.
                ''',
                'vmvqpqueries',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPResponses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of VQP responses received by this device
                from all VMPS since last system re-initialization.
                ''',
                'vmvqpresponses',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPShutdown', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, a VQP response indicates 
                'shutdown'. A 'shutdown' response is a result of 
                the membership policy configured at a VMPS
                by the administrator.
                ''',
                'vmvqpshutdown',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPWrongDomain', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, a VQP response indicates wrong 
                management domain. A wrong management domain 
                response indicates that the VMPS used serves a 
                management domain that is different
                from the device's management domain.
                ''',
                'vmvqpwrongdomain',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVQPWrongVersion', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times, since last system
                re-initialization, a VQP response indicates wrong 
                VQP version. A wrong VQP version response 
                indicates that the VMPS used supports a VQP 
                version that is different from the device's 
                VQP version.
                ''',
                'vmvqpwrongversion',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmStatistics',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmStatus' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmStatus',
            False, 
            [
            _MetaInfoClassMember('vmNotificationsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the notifications/traps
                defined in this MIB are enabled.
                ''',
                'vmnotificationsenabled',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmStatus',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirmResult_Enum' : _MetaInfoEnum('VmVmpsReconfirmResult_Enum', 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB',
        {
            'other':'OTHER',
            'inProgress':'INPROGRESS',
            'success':'SUCCESS',
            'noResponse':'NORESPONSE',
            'noVmps':'NOVMPS',
            'noDynamicPort':'NODYNAMICPORT',
            'noHostConnected':'NOHOSTCONNECTED',
        }, 'CISCO-VLAN-MEMBERSHIP-MIB', _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB']),
    'CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirm_Enum' : _MetaInfoEnum('VmVmpsReconfirm_Enum', 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB',
        {
            'ready':'READY',
            'execute':'EXECUTE',
        }, 'CISCO-VLAN-MEMBERSHIP-MIB', _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB']),
    'CISCOVLANMEMBERSHIPMIB.VmVmps' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmVmps',
            False, 
            [
            _MetaInfoClassMember('vmVmpsCurrent', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This is the IpAddress of the current VMPS used.
                ''',
                'vmvmpscurrent',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsReconfirm', REFERENCE_ENUM_CLASS, 'VmVmpsReconfirm_Enum' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirm_Enum', 
                [], [], 
                '''                Setting this object to execute(2) causes the switch
                to reconfirm membership of every dynamic port.
                Reading this object always return ready(1).
                ''',
                'vmvmpsreconfirm',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsReconfirmInterval', ATTRIBUTE, 'int' , None, None, 
                [(0, 120)], [], 
                '''                The switch will reconfirm membership of addresses on
                each port with VMPS periodically. This object specifies
                the interval to perform reconfirmation. If the value is
                set to 0, the switch does not reconfirm membership with
                VMPS.
                ''',
                'vmvmpsreconfirminterval',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsReconfirmResult', REFERENCE_ENUM_CLASS, 'VmVmpsReconfirmResult_Enum' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirmResult_Enum', 
                [], [], 
                '''                This object returns the result of the last request
                that sets vmVmpsReconfirm to execute(2). The
                semantics of the possible results are as follows:
                
                     other(1)           - none of following
                     inProgress(2)      - reconfirm in progress
                     success(3)         - reconfirm completed successfully
                     noResponse(4)      - reconfirm failed because no
                                          VMPS responded
                     noVmps(5)          - No VMPS configured
                     noDynamicPort(6)   - No dynamic ports configured
                     noHostConnected(7) - No hosts on dynamic ports
                ''',
                'vmvmpsreconfirmresult',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsRetries', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                The number of retries for VQP requests to a VMPS before
                using the next available VMPS.
                ''',
                'vmvmpsretries',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsVQPVersion', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The VLAN Query Protocol (VQP) version supported on
                the device. VQP is the protocol used to query
                VLAN Membership Policy Server (VMPS) for VLAN
                membership assignments of dynamic VLAN ports.
                A VMPS provides VLAN membership policy
                assignments based on the content of the packets
                received on a port.
                ''',
                'vmvmpsvqpversion',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmVmps',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry',
            False, 
            [
            _MetaInfoClassMember('vmVmpsIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Ip Address of the VMPS.
                ''',
                'vmvmpsipaddress',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmVmpsPrimary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The status of the VMPS. Setting this value
                to true will make this VMPS the primary server
                and make the switch use this as the current server.
                Setting this entry to true causes other rows
                to transition to false. Attempting to write
                a value of false after creation will result in
                a return of bad value. Deleting an entry whose
                value is true will result in the first entry
                in the table being set to true.
                ''',
                'vmvmpsprimary',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this conceptual row.
                ''',
                'vmvmpsrowstatus',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmVmpsEntry',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmVmpsTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmVmpsTable',
            False, 
            [
            _MetaInfoClassMember('vmVmpsEntry', REFERENCE_LIST, 'VmVmpsEntry' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry', 
                [], [], 
                '''                An entry (conceptual row) in the vmVmpsTable.
                ''',
                'vmvmpsentry',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmVmpsTable',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-VLAN-MEMBERSHIP-MIB', True),
            _MetaInfoClassMember('vmVoiceVlanCdpVerifyEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or Disable the feature of CDP message
                verification of voice VLANs.
                
                true   - The voice VLAN vmVoiceVlan is enabled 
                         only after CDP messages are received 
                         from the IP phone.
                
                false -  The voice VLAN vmVoiceVlan is enabled
                         as soon as the IP phone interface is
                         up. There is no verification needed 
                         from CDP messages from the IP phone.
                ''',
                'vmvoicevlancdpverifyenable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVoiceVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4096)], [], 
                '''                The Voice Vlan ID (VVID) to which this
                port belongs to.
                
                0    -    The CDP packets transmitting 
                          through this port would contain
                          Appliance VLAN-ID TLV with value 
                          of 0. VoIP and related packets 
                          are expected to be sent and 
                          received with VLAN-id=0 and an 
                          802.1p priority. 
                
                1..4094 - The CDP packets transmitting
                          through this port would contain
                          Appliance VLAN-ID TLV with N.
                          VoIP and related packets are
                          expected to be sent and received
                          with VLAN-id=N and an 802.1p
                          priority.
                
                4095  -   The CDP packets transmitting
                          through this port would contain
                          Appliance VLAN-ID TLV with value
                          of 4095. VoIP and related packets
                          are expected to be sent and 
                          received untagged without an 
                          802.1p priority.
                
                4096  -   The CDP packets transmitting 
                          through this port would not 
                          include Appliance VLAN-ID TLV; 
                          or, if the VVID is not supported 
                          on the port, this MIB object will
                          not be configurable and will 
                          return 4096.
                ''',
                'vmvoicevlanid',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmVoiceVlanEntry',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable',
            False, 
            [
            _MetaInfoClassMember('vmVoiceVlanEntry', REFERENCE_LIST, 'VmVoiceVlanEntry' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry', 
                [], [], 
                '''                An entry (conceptual row) in the vmVoiceVlanTable.
                Only interfaces which support Voice Vlan feature
                are shown.
                ''',
                'vmvoicevlanentry',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'vmVoiceVlanTable',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
    'CISCOVLANMEMBERSHIPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOVLANMEMBERSHIPMIB',
            False, 
            [
            _MetaInfoClassMember('vmMembership', REFERENCE_CLASS, 'VmMembership' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembership', 
                [], [], 
                '''                ''',
                'vmmembership',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmMembershipSummaryExtTable', REFERENCE_CLASS, 'VmMembershipSummaryExtTable' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable', 
                [], [], 
                '''                A summary of VLAN membership of non-trunk
                bridge ports. This table is used for 
                retrieving VLAN membership information
                for the device which supports dot1dBasePort 
                with value greater than 2048.
                
                A row is created for a VLAN and a particular
                bridge port range, where at least one port 
                in the range is assigned to this VLAN.
                
                VLAN membership can only be modified via the
                vmMembershipTable.
                ''',
                'vmmembershipsummaryexttable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmMembershipSummaryTable', REFERENCE_CLASS, 'VmMembershipSummaryTable' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable', 
                [], [], 
                '''                A summary of VLAN membership of non-trunk
                bridge ports. This is a convenience table
                for retrieving VLAN membership information.
                
                A row is created for a VLAN if:
                a) the VLAN exists, or
                b) a port is assigned to a non-existent VLAN.
                
                VLAN membership can only be modified via the
                vmMembershipTable.
                ''',
                'vmmembershipsummarytable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmMembershipTable', REFERENCE_CLASS, 'VmMembershipTable' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmMembershipTable', 
                [], [], 
                '''                A table for configuring VLAN port membership.
                There is one row for each bridge port that is
                assigned to a static or dynamic access port. Trunk
                ports are not  represented in this table.  An entry
                may be created and deleted when ports are created or
                deleted via SNMP or the management console on a 
                device.
                ''',
                'vmmembershiptable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmStatistics', REFERENCE_CLASS, 'VmStatistics' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmStatistics', 
                [], [], 
                '''                ''',
                'vmstatistics',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmStatus', REFERENCE_CLASS, 'VmStatus' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmStatus', 
                [], [], 
                '''                ''',
                'vmstatus',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmps', REFERENCE_CLASS, 'VmVmps' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVmps', 
                [], [], 
                '''                ''',
                'vmvmps',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVmpsTable', REFERENCE_CLASS, 'VmVmpsTable' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVmpsTable', 
                [], [], 
                '''                A table of VMPS to use. The device will use
                the the primary VMPS by default. If the
                device is unable to reach the primary server
                after vmVmpsRetries retries, it uses the first
                secondary server in the table until it runs out
                of secondary servers, in which case it will return
                to using the primary server. Entries in this table
                may be created and deleted via this MIB or
                the management console on a device.
                ''',
                'vmvmpstable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            _MetaInfoClassMember('vmVoiceVlanTable', REFERENCE_CLASS, 'VmVoiceVlanTable' , 'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable', 
                [], [], 
                '''                A table for configuring the Voice VLAN-ID
                for the ports. An entry will exist for each
                interface which supports Voice Vlan feature.
                ''',
                'vmvoicevlantable',
                'CISCO-VLAN-MEMBERSHIP-MIB', False),
            ],
            'CISCO-VLAN-MEMBERSHIP-MIB',
            'CISCO-VLAN-MEMBERSHIP-MIB',
            _yang_ns._namespaces['CISCO-VLAN-MEMBERSHIP-MIB'],
        'ydk.models.vlan.CISCO_VLAN_MEMBERSHIP_MIB'
        ),
    },
}
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipTable']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB.VmVmpsTable']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembership']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmMembershipTable']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmStatistics']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmStatus']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmVmps']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmVmpsTable']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
_meta_table['CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable']['meta_info'].parent =_meta_table['CISCOVLANMEMBERSHIPMIB']['meta_info']
