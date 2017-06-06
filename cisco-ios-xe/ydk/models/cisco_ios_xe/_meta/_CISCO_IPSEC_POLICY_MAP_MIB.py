


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry',
            False, 
            [
            _MetaInfoClassMember('ikePolMapTunIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index of the IPSec Phase-1 Tunnel to Policy
                Map Table.  The value of the index is the number
                used to represent this IPSec Phase-1 Tunnel in
                the IPSec MIB (ikeTunIndex in the
                ikeTunnelTable).
                ''',
                'ikepolmaptunindex',
                'CISCO-IPSEC-POLICY-MAP-MIB', True),
            _MetaInfoClassMember('ikePolMapPolicyNum', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The number of the locally defined ISAKMP policy
                used to establish the IPSec IKE Phase-1 Tunnel.
                This is the number which was used on the crypto
                command. For example, if the configuration command
                was:
                
                 ==>  crypto isakmp policy 15
                
                then the value of this object would be 15.
                If ISAKMP was not used to establish this tunnel,
                then the value of this object will be zero.
                ''',
                'ikepolmappolicynum',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            ],
            'CISCO-IPSEC-POLICY-MAP-MIB',
            'ikePolMapEntry',
            _yang_ns._namespaces['CISCO-IPSEC-POLICY-MAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CiscoIpsecPolicyMapMib.Ikepolmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecPolicyMapMib.Ikepolmaptable',
            False, 
            [
            _MetaInfoClassMember('ikePolMapEntry', REFERENCE_LIST, 'Ikepolmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB', 'CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry', 
                [], [], 
                '''                Each entry contains the attributes associated
                with mapping an active IPSec Phase-1 IKE Tunnel
                to it's configured Policy definition.
                ''',
                'ikepolmapentry',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            ],
            'CISCO-IPSEC-POLICY-MAP-MIB',
            'ikePolMapTable',
            _yang_ns._namespaces['CISCO-IPSEC-POLICY-MAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry',
            False, 
            [
            _MetaInfoClassMember('ipSecPolMapTunIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The index of the IPSec Phase-2 Tunnel to Policy
                Map Table. The value of the index is the number
                used to represent this IPSec Phase-2 Tunnel in
                the IPSec MIB (ipSecTunIndex in the
                ipSecTunnelTable).
                ''',
                'ipsecpolmaptunindex',
                'CISCO-IPSEC-POLICY-MAP-MIB', True),
            _MetaInfoClassMember('ipSecPolMapAceString', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of this object is the access control 
                entry (ACE) within the ACL that caused this IPSec 
                tunnel to be established. 
                
                For instance, if an ACL defines access for two
                traffic streams (FTP and SNMP) as follows:
                
                access-list 101 permit tcp 172.16.14.0 0.0.0.255
                                 172.16.16.0 0.0.0.255 eq ftp
                access-list 101 permit udp 172.16.14.0 0.0.0.255
                                 host 172.16.16.1 eq 161
                
                
                When associated with an IPSec policy, the second
                element of the ACL gives rise to an IPSec tunnel
                in the wake of SNMP traffic. The value of the
                object 'ipSecPolMapAceString' for the IPSec tunnel
                would be then the string
                'access-list 101 permit udp 172.16.14.0 0.0.0.255
                                 host 172.16.16.1 eq 161'
                ''',
                'ipsecpolmapacestring',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            _MetaInfoClassMember('ipSecPolMapAclString', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of this object is the number or
                the name of the access control string (ACL) 
                that caused this IPSec tunnel to be established. 
                 The ACL that causes an IPSec tunnel
                 to be established is referenced by the 
                 cryptomap of the tunnel.
                
                 The ACL identifies the traffic that requires
                 protection as defined by the policy.
                
                 For instance, the ACL that requires FTP
                 traffic between local subnet 172.16.14.0 and a
                 remote subnet 172.16.16.0 to be protected
                 is defined as
                
                 ==>access-list 101 permit tcp 172.16.14.0 0.0.0.255
                                  172.16.16.0 0.0.0.255 eq ftp
                
                 When this command causes an IPSec tunnel to be
                  established, the object 'ipSecPolMapAclString'
                  assumes the string value '101'.
                
                 If the ACL is a named list such as
                  ==> ip access-list standard myAcl
                       permit 172.16.16.8 0.0.0.0
                
                 then the value of this MIB element corresponding to 
                  IPSec tunnel that was created by this ACL would
                  be 'myAcl'.
                ''',
                'ipsecpolmapaclstring',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            _MetaInfoClassMember('ipSecPolMapCryptoMapName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of this object should be the name of 
                the IPSec Policy (cryptomap) as assigned by the 
                operator while configuring the policy of 
                the IPSec traffic.
                
                For instance, on an IOS router, the if the command
                entered to configure the IPSec policy was 
                
                ==>  crypto map ftpPolicy 10 ipsec-isakmp
                
                then the value of this object would be 'ftpPolicy'.
                ''',
                'ipsecpolmapcryptomapname',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            _MetaInfoClassMember('ipSecPolMapCryptoMapNum', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The value of this object should be the priority
                of the IPSec Policy (cryptomap) assigned by the 
                operator while configuring the policy of 
                this IPSec tunnel.
                
                For instance, on an IOS router, the if the command
                entered to configure the IPSec policy was 
                
                ==>  crypto map ftpPolicy 10 ipsec-isakmp
                
                then the value of this object would be 10.
                ''',
                'ipsecpolmapcryptomapnum',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            ],
            'CISCO-IPSEC-POLICY-MAP-MIB',
            'ipSecPolMapEntry',
            _yang_ns._namespaces['CISCO-IPSEC-POLICY-MAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CiscoIpsecPolicyMapMib.Ipsecpolmaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecPolicyMapMib.Ipsecpolmaptable',
            False, 
            [
            _MetaInfoClassMember('ipSecPolMapEntry', REFERENCE_LIST, 'Ipsecpolmapentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB', 'CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry', 
                [], [], 
                '''                Each entry contains the attributes associated
                with mapping an active IPSec Phase-2 Tunnel
                to its configured Policy definition.
                ''',
                'ipsecpolmapentry',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            ],
            'CISCO-IPSEC-POLICY-MAP-MIB',
            'ipSecPolMapTable',
            _yang_ns._namespaces['CISCO-IPSEC-POLICY-MAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CiscoIpsecPolicyMapMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecPolicyMapMib',
            False, 
            [
            _MetaInfoClassMember('ikePolMapTable', REFERENCE_CLASS, 'Ikepolmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB', 'CiscoIpsecPolicyMapMib.Ikepolmaptable', 
                [], [], 
                '''                The IPSec Phase-1 Internet Key Exchange Tunnel
                to Policy Mapping Table. There is one entry in
                this table for each active IPSec Phase-1
                Tunnel.
                ''',
                'ikepolmaptable',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            _MetaInfoClassMember('ipSecPolMapTable', REFERENCE_CLASS, 'Ipsecpolmaptable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB', 'CiscoIpsecPolicyMapMib.Ipsecpolmaptable', 
                [], [], 
                '''                The IPSec Phase-2 Tunnel to Policy Mapping Table.
                There is one entry in this table for each active
                IPSec Phase-2 Tunnel.
                ''',
                'ipsecpolmaptable',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            ],
            'CISCO-IPSEC-POLICY-MAP-MIB',
            'CISCO-IPSEC-POLICY-MAP-MIB',
            _yang_ns._namespaces['CISCO-IPSEC-POLICY-MAP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
}
_meta_table['CiscoIpsecPolicyMapMib.Ikepolmaptable.Ikepolmapentry']['meta_info'].parent =_meta_table['CiscoIpsecPolicyMapMib.Ikepolmaptable']['meta_info']
_meta_table['CiscoIpsecPolicyMapMib.Ipsecpolmaptable.Ipsecpolmapentry']['meta_info'].parent =_meta_table['CiscoIpsecPolicyMapMib.Ipsecpolmaptable']['meta_info']
_meta_table['CiscoIpsecPolicyMapMib.Ikepolmaptable']['meta_info'].parent =_meta_table['CiscoIpsecPolicyMapMib']['meta_info']
_meta_table['CiscoIpsecPolicyMapMib.Ipsecpolmaptable']['meta_info'].parent =_meta_table['CiscoIpsecPolicyMapMib']['meta_info']
