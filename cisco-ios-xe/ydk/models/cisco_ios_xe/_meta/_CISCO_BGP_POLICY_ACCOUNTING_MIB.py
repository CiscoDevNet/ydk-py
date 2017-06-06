


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry' : {
        'meta_info' : _MetaInfoClass('CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', True),
            _MetaInfoClassMember('cbpAcctTrafficIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An integer value greater than 0, that uniquely identifies
                a traffic-type. The traffic-type has no intrinsic meaning.
                It just means the traffic coming into an interface can be
                differentiated into different types. It is up to the user to
                give meaning to and configure the various traffic-types on an 
                interface.
                ''',
                'cbpaccttrafficindex',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', True),
            _MetaInfoClassMember('cbpAcctInOctetCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received for a particular
                traffic-type on an interface.
                ''',
                'cbpacctinoctetcount',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            _MetaInfoClassMember('cbpAcctInPacketCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets received for a particular
                traffic-type on an interface.
                ''',
                'cbpacctinpacketcount',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            _MetaInfoClassMember('cbpAcctOutOctetCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets transmitted for a particular
                traffic-type on an interface.
                ''',
                'cbpacctoutoctetcount',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            _MetaInfoClassMember('cbpAcctOutPacketCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets transmitted for a particular
                traffic-type on an interface.
                ''',
                'cbpacctoutpacketcount',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            ],
            'CISCO-BGP-POLICY-ACCOUNTING-MIB',
            'cbpAcctEntry',
            _yang_ns._namespaces['CISCO-BGP-POLICY-ACCOUNTING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB'
        ),
    },
    'CiscoBgpPolicyAccountingMib.Cbpaccttable' : {
        'meta_info' : _MetaInfoClass('CiscoBgpPolicyAccountingMib.Cbpaccttable',
            False, 
            [
            _MetaInfoClassMember('cbpAcctEntry', REFERENCE_LIST, 'Cbpacctentry' , 'ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB', 'CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry', 
                [], [], 
                '''                Each cbpAcctEntry provides statistics for traffic of interest
                on an ingress and/or egress interfaces. The traffic of interest 
                may be used for purposes like billing, and is referred to from 
                here on in the MIB by the term 'traffic-type', which corresponds
                to cbpAcctTrafficIndex. Traffic-types are configured by the user
                on a per interface basis.
                
                The statistics include ingress packet counts, ingress octet
                counts, egress packet counts and egress octet counts. Entries 
                are created when traffic-type is configured on an interface.
                Entries are deleted automatically when the user 
                removes the corresponding traffic-type configuration from an
                interface.
                ''',
                'cbpacctentry',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            ],
            'CISCO-BGP-POLICY-ACCOUNTING-MIB',
            'cbpAcctTable',
            _yang_ns._namespaces['CISCO-BGP-POLICY-ACCOUNTING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB'
        ),
    },
    'CiscoBgpPolicyAccountingMib' : {
        'meta_info' : _MetaInfoClass('CiscoBgpPolicyAccountingMib',
            False, 
            [
            _MetaInfoClassMember('cbpAcctTable', REFERENCE_CLASS, 'Cbpaccttable' , 'ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB', 'CiscoBgpPolicyAccountingMib.Cbpaccttable', 
                [], [], 
                '''                The cbpAcctTable provides statistics about ingress and egress 
                traffic on an interface. This data could be used for purposes 
                like billing.
                ''',
                'cbpaccttable',
                'CISCO-BGP-POLICY-ACCOUNTING-MIB', False),
            ],
            'CISCO-BGP-POLICY-ACCOUNTING-MIB',
            'CISCO-BGP-POLICY-ACCOUNTING-MIB',
            _yang_ns._namespaces['CISCO-BGP-POLICY-ACCOUNTING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_BGP_POLICY_ACCOUNTING_MIB'
        ),
    },
}
_meta_table['CiscoBgpPolicyAccountingMib.Cbpaccttable.Cbpacctentry']['meta_info'].parent =_meta_table['CiscoBgpPolicyAccountingMib.Cbpaccttable']['meta_info']
_meta_table['CiscoBgpPolicyAccountingMib.Cbpaccttable']['meta_info'].parent =_meta_table['CiscoBgpPolicyAccountingMib']['meta_info']
