


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIPSECPOLICYMAPMIB.IkePolMapTable.IkePolMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECPOLICYMAPMIB.IkePolMapTable.IkePolMapEntry',
            False, 
            [
            _MetaInfoClassMember('ikePolMapTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPSec Phase-1 Tunnel to Policy
                Map Table.  The value of the index is the number
                used to represent this IPSec Phase-1 Tunnel in
                the IPSec MIB (ikeTunIndex in the
                ikeTunnelTable).
                ''',
                'ikepolmaptunindex',
                'CISCO-IPSEC-POLICY-MAP-MIB', True),
            _MetaInfoClassMember('ikePolMapPolicyNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
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
        'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CISCOIPSECPOLICYMAPMIB.IkePolMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECPOLICYMAPMIB.IkePolMapTable',
            False, 
            [
            _MetaInfoClassMember('ikePolMapEntry', REFERENCE_LIST, 'IkePolMapEntry' , 'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB', 'CISCOIPSECPOLICYMAPMIB.IkePolMapTable.IkePolMapEntry', 
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
        'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable.IpSecPolMapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable.IpSecPolMapEntry',
            False, 
            [
            _MetaInfoClassMember('ipSecPolMapTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the IPSec Phase-2 Tunnel to Policy
                Map Table. The value of the index is the number
                used to represent this IPSec Phase-2 Tunnel in
                the IPSec MIB (ipSecTunIndex in the
                ipSecTunnelTable).
                ''',
                'ipsecpolmaptunindex',
                'CISCO-IPSEC-POLICY-MAP-MIB', True),
            _MetaInfoClassMember('ipSecPolMapAceString', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
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
                [], ['\\p{IsBasicLatin}{0,255}'], 
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
                [], ['\\p{IsBasicLatin}{0,255}'], 
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
                [(1, 2147483647)], [], 
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
        'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable',
            False, 
            [
            _MetaInfoClassMember('ipSecPolMapEntry', REFERENCE_LIST, 'IpSecPolMapEntry' , 'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB', 'CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable.IpSecPolMapEntry', 
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
        'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
    'CISCOIPSECPOLICYMAPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECPOLICYMAPMIB',
            False, 
            [
            _MetaInfoClassMember('ikePolMapTable', REFERENCE_CLASS, 'IkePolMapTable' , 'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB', 'CISCOIPSECPOLICYMAPMIB.IkePolMapTable', 
                [], [], 
                '''                The IPSec Phase-1 Internet Key Exchange Tunnel
                to Policy Mapping Table. There is one entry in
                this table for each active IPSec Phase-1
                Tunnel.
                ''',
                'ikepolmaptable',
                'CISCO-IPSEC-POLICY-MAP-MIB', False),
            _MetaInfoClassMember('ipSecPolMapTable', REFERENCE_CLASS, 'IpSecPolMapTable' , 'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB', 'CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable', 
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
        'ydk.models.ipsec.CISCO_IPSEC_POLICY_MAP_MIB'
        ),
    },
}
_meta_table['CISCOIPSECPOLICYMAPMIB.IkePolMapTable.IkePolMapEntry']['meta_info'].parent =_meta_table['CISCOIPSECPOLICYMAPMIB.IkePolMapTable']['meta_info']
_meta_table['CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable.IpSecPolMapEntry']['meta_info'].parent =_meta_table['CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable']['meta_info']
_meta_table['CISCOIPSECPOLICYMAPMIB.IkePolMapTable']['meta_info'].parent =_meta_table['CISCOIPSECPOLICYMAPMIB']['meta_info']
_meta_table['CISCOIPSECPOLICYMAPMIB.IpSecPolMapTable']['meta_info'].parent =_meta_table['CISCOIPSECPOLICYMAPMIB']['meta_info']
