


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IkeHashAlgo_Enum' : _MetaInfoEnum('IkeHashAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'none':'NONE',
            'md5':'MD5',
            'sha':'SHA',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'CryptomapType_Enum' : _MetaInfoEnum('CryptomapType_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'cryptomapTypeNONE':'CRYPTOMAPTYPENONE',
            'cryptomapTypeMANUAL':'CRYPTOMAPTYPEMANUAL',
            'cryptomapTypeISAKMP':'CRYPTOMAPTYPEISAKMP',
            'cryptomapTypeCET':'CRYPTOMAPTYPECET',
            'cryptomapTypeDYNAMIC':'CRYPTOMAPTYPEDYNAMIC',
            'cryptomapTypeDYNAMICDISCOVERY':'CRYPTOMAPTYPEDYNAMICDISCOVERY',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'IkeIdentityType_Enum' : _MetaInfoEnum('IkeIdentityType_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'isakmpIdTypeUNKNOWN':'ISAKMPIDTYPEUNKNOWN',
            'isakmpIdTypeADDRESS':'ISAKMPIDTYPEADDRESS',
            'isakmpIdTypeHOSTNAME':'ISAKMPIDTYPEHOSTNAME',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'TrapStatus_Enum' : _MetaInfoEnum('TrapStatus_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'EncryptAlgo_Enum' : _MetaInfoEnum('EncryptAlgo_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'none':'NONE',
            'des':'DES',
            'des3':'DES3',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'IkeAuthMethod_Enum' : _MetaInfoEnum('IkeAuthMethod_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'none':'NONE',
            'preSharedKey':'PRESHAREDKEY',
            'rsaSig':'RSASIG',
            'rsaEncrypt':'RSAENCRYPT',
            'revPublicKey':'REVPUBLICKEY',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'CryptomapSetBindStatus_Enum' : _MetaInfoEnum('CryptomapSetBindStatus_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'unknown':'UNKNOWN',
            'attached':'ATTACHED',
            'detached':'DETACHED',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'DiffHellmanGrp_Enum' : _MetaInfoEnum('DiffHellmanGrp_Enum', 'ydk.models.ipsec.CISCO_IPSEC_MIB',
        {
            'none':'NONE',
            'dhGroup1':'DHGROUP1',
            'dhGroup2':'DHGROUP2',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsCryptomapSetIfStatus', REFERENCE_ENUM_CLASS, 'CryptomapSetBindStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CryptomapSetBindStatus_Enum', 
                [], [], 
                '''                This object identifies the status of the binding 
                of the specified cryptomap set with the specified
                interface. The value when queried is always 'attached'. 
                When set to 'detached', the cryptomap set if detached 
                from the specified interface. The effect of this is same 
                as the CLI command
                
                	config-if# no crypto map cryptomapSetName
                
                Setting the value to 'attached' will result in 
                SNMP General Error.
                ''',
                'cipscryptomapsetifstatus',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCryptomapSetIfVirtual', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of this object identifies if the
                interface to which the cryptomap set is attached
                is a tunnel (such as a GRE or PPTP tunnel).
                ''',
                'cipscryptomapsetifvirtual',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsCryptomapSetIfEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsCryptomapSetIfTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsCryptomapSetIfTable',
            False, 
            [
            _MetaInfoClassMember('cipsCryptomapSetIfEntry', REFERENCE_LIST, 'CipsCryptomapSetIfEntry' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry', 
                [], [], 
                '''                Each entry contains the record of
                the association between an interface
                and a cryptomap set (static) that is defined
                on the managed entity.
                
                Note that the cryptomap set identified in 
                this binding must static. Dynamic cryptomaps cannot
                be bound to interfaces.
                ''',
                'cipscryptomapsetifentry',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsCryptomapSetIfTable',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry',
            False, 
            [
            _MetaInfoClassMember('cipsDynamicCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The index of the dynamic cryptomap table. 
                The value of the string is the one assigned 
                by the operator in defining the cryptomap set.
                ''',
                'cipsdynamiccryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsDynamicCryptomapSetNumAssoc', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of static cryptomap sets with which
                this dynamic cryptomap is associated.  
                ''',
                'cipsdynamiccryptomapsetnumassoc',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsDynamicCryptomapSetSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of cryptomap entries in this cryptomap.
                ''',
                'cipsdynamiccryptomapsetsize',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsDynamicCryptomapSetEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsDynamicCryptomapSetTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsDynamicCryptomapSetTable',
            False, 
            [
            _MetaInfoClassMember('cipsDynamicCryptomapSetEntry', REFERENCE_LIST, 'CipsDynamicCryptomapSetEntry' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry', 
                [], [], 
                '''                Each entry contains the attributes associated
                with a single dynamic cryptomap template.
                ''',
                'cipsdynamiccryptomapsetentry',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsDynamicCryptomapSetTable',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsIPsecGlobals' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsIPsecGlobals',
            False, 
            [
            _MetaInfoClassMember('cipsNumCETCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of static Cryptomap Sets that have 
                at least one CET cryptomap element
                as a member of the set.
                ''',
                'cipsnumcetcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumDynamicCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of dynamic IPSec Policy templates
                (called 'dynamic cryptomap templates') configured
                on the managed entity.
                ''',
                'cipsnumdynamiccryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumStaticCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of Cryptomap Sets that are are fully
                configured. Statically defined cryptomap sets 
                are ones where the operator has fully specified
                all the parameters required set up IPSec 
                Virtual Private Networks (VPNs).
                ''',
                'cipsnumstaticcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of static Cryptomap Sets that have 
                at least one dynamic cryptomap template 
                bound to them which has the Tunnel Endpoint Discovery
                (TED) enabled.
                ''',
                'cipsnumtedcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSALifesize', ATTRIBUTE, 'int' , None, None, 
                [(2560, 536870912)], [], 
                '''                The default lifesize in KBytes assigned to an SA 
                as a global policy (unless overridden in cryptomap 
                definition)
                ''',
                'cipssalifesize',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSALifetime', ATTRIBUTE, 'int' , None, None, 
                [(120, 86400)], [], 
                '''                The default lifetime (in seconds) assigned 
                to an SA as a global policy (maybe overridden 
                in specific cryptomap definitions).
                ''',
                'cipssalifetime',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsIPsecGlobals',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsIPsecStatistics' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsIPsecStatistics',
            False, 
            [
            _MetaInfoClassMember('cipsNumTEDFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TED probes that were dispatched by 
                the local entity and that failed to locate crypto 
                endpoint.  Not affected by any CLI operation.
                ''',
                'cipsnumtedfailures',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDProbesReceived', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TED probes that were received by this 
                managed entity since bootup. Not affected by any 
                CLI operation.
                ''',
                'cipsnumtedprobesreceived',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDProbesSent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of TED probes that were dispatched by all
                the dynamic cryptomaps in this managed entity since 
                bootup. Not affected by any CLI operation.
                ''',
                'cipsnumtedprobessent',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsIPsecStatistics',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsIsakmpGroup' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsIsakmpGroup',
            False, 
            [
            _MetaInfoClassMember('cipsIsakmpEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of this object is TRUE if ISAKMP
                has been enabled on the managed entity. Otherise
                the value of this object is FALSE.
                ''',
                'cipsisakmpenabled',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpIdentity', REFERENCE_ENUM_CLASS, 'IkeIdentityType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'IkeIdentityType_Enum', 
                [], [], 
                '''                The value of this object is shows the type of
                identity used by the managed entity in ISAKMP
                negotiations with another peer.
                ''',
                'cipsisakmpidentity',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpKeepaliveInterval', ATTRIBUTE, 'int' , None, None, 
                [(10, 3600)], [], 
                '''                The value of this object is time interval in
                seconds between successive ISAKMP keepalive
                heartbeats issued to the peers to which IKE
                tunnels have been setup.
                ''',
                'cipsisakmpkeepaliveinterval',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumIsakmpPolicies', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The value of this object is the number of
                ISAKMP policies that have been configured on the 
                managed entity.
                ''',
                'cipsnumisakmppolicies',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsIsakmpGroup',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry',
            False, 
            [
            _MetaInfoClassMember('cipsIsakmpPolPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The priotity of this ISAKMP Policy entry.
                This is also the index of this table.
                ''',
                'cipsisakmppolpriority',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsIsakmpPolAuth', REFERENCE_ENUM_CLASS, 'IkeAuthMethod_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'IkeAuthMethod_Enum', 
                [], [], 
                '''                The peer authentication mthod specified by
                this ISAKMP policy specification. If this policy
                entity is selected for negotiation with a peer,
                the local entity would authenticate the peer using 
                the method specified by this object.
                ''',
                'cipsisakmppolauth',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolEncr', REFERENCE_ENUM_CLASS, 'EncryptAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'EncryptAlgo_Enum', 
                [], [], 
                '''                The encryption transform specified by this 
                ISAKMP policy specification. The Internet Key Exchange
                (IKE) tunnels setup using this policy item would
                use the specified encryption transform to protect the
                ISAKMP PDUs.
                ''',
                'cipsisakmppolencr',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolGroup', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                This object specifies the Oakley group used 
                for Diffie Hellman exchange in the Main Mode. 
                If this policy item is selected to negotiate
                Main Mode with an IKE peer, the local entity 
                chooses the group specified by this object to
                perform Diffie Hellman exchange with the
                peer.
                ''',
                'cipsisakmppolgroup',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolHash', REFERENCE_ENUM_CLASS, 'IkeHashAlgo_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'IkeHashAlgo_Enum', 
                [], [], 
                '''                The hash transform specified by this 
                ISAKMP policy specification. The IKE tunnels
                setup using this policy item would use the 
                specified hash transform to protect the
                ISAKMP PDUs.
                ''',
                'cipsisakmppolhash',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolLifetime', ATTRIBUTE, 'int' , None, None, 
                [(60, 86400)], [], 
                '''                This object specifies the lifetime in seconds
                of the IKE tunnels generated using this 
                policy specification.
                ''',
                'cipsisakmppollifetime',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsIsakmpPolicyEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsIsakmpPolicyTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsIsakmpPolicyTable',
            False, 
            [
            _MetaInfoClassMember('cipsIsakmpPolicyEntry', REFERENCE_LIST, 'CipsIsakmpPolicyEntry' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry', 
                [], [], 
                '''                Each entry contains the attributes 
                associated with a single ISAKMP
                Policy entry.
                ''',
                'cipsisakmppolicyentry',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsIsakmpPolicyTable',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The index of the static cryptomap table. The value 
                of the string is the name string assigned by the 
                operator in defining the cryptomap set.
                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumCET', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of cryptomaps of type 'ipsec-cisco' 
                associated with this cryptomap set. Such
                cryptomap elements implement Cisco Encryption Technology
                based Virtual Private Networks.
                ''',
                'cipsstaticcryptomapsetnumcet',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumDisc', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of dynamic cryptomap templates
                linked to this cryptomap set that have Tunnel Endpoint
                Discovery (TED) enabled.
                ''',
                'cipsstaticcryptomapsetnumdisc',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumDynamic', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of dynamic cryptomap templates
                linked to this cryptomap set.
                ''',
                'cipsstaticcryptomapsetnumdynamic',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumIsakmp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of cryptomaps associated with this 
                cryptomap set that use ISAKMP protocol to do key
                exchange.
                ''',
                'cipsstaticcryptomapsetnumisakmp',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumManual', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of cryptomaps associated with this 
                cryptomap set that require the operator to manually
                setup the keys and SPIs.
                ''',
                'cipsstaticcryptomapsetnummanual',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumSAs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of and IPsec Security Associations
                that are active and were setup using this cryptomap.  
                ''',
                'cipsstaticcryptomapsetnumsas',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of cryptomap entries contained in
                this cryptomap set. 
                ''',
                'cipsstaticcryptomapsetsize',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsStaticCryptomapSetEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsStaticCryptomapSetTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsStaticCryptomapSetTable',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetEntry', REFERENCE_LIST, 'CipsStaticCryptomapSetEntry' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry', 
                [], [], 
                '''                Each entry contains the attributes 
                associated with a single static 
                cryptomap set.
                ''',
                'cipsstaticcryptomapsetentry',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsStaticCryptomapSetTable',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The priority of the cryptomap entry in the 
                cryptomap set. This is the second index component
                of this table.
                ''',
                'cipsstaticcryptomappriority',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapDescr', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The description string entered by the operatoir
                while creating this cryptomap. The string generally
                identifies a description and the purpose of this
                policy.
                ''',
                'cipsstaticcryptomapdescr',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapLevelHost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object identifies the granularity of the
                IPSec SAs created using this IPSec policy entry. 
                If this value is TRUE, distinct SA bundles are created
                for distinct hosts at the end of the application traffic.
                ''',
                'cipsstaticcryptomaplevelhost',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapLifesize', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (2560, 536870912)], [], 
                '''                This object identifies the lifesize (maximum traffic
                in bytes that may be carried) of the IPSec SAs
                created using this IPSec policy entry. 
                If this value is zero, the lifetime assumes the 
                value specified by the global lifesize parameter.
                ''',
                'cipsstaticcryptomaplifesize',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapLifetime', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (120, 86400)], [], 
                '''                This object identifies the lifetime of the IPSec
                Security Associations (SA) created using this IPSec policy
                entry. If this value is zero, the lifetime assumes the 
                value specified by the global lifetime parameter.
                ''',
                'cipsstaticcryptomaplifetime',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapNumPeers', ATTRIBUTE, 'int' , None, None, 
                [(0, 40)], [], 
                '''                The number of peers associated with this cryptomap 
                entry. The peers other than the one identified by 
                'cipsStaticCryptomapPeer' are backup peers. 
                
                Manual cryptomaps may have only one peer.
                ''',
                'cipsstaticcryptomapnumpeers',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapPeer', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP address of the current peer associated with 
                this IPSec policy item. Traffic that is protected by
                this cryptomap is protected by a tunnel that terminates
                at the device whose IP address is specified by this
                object.
                ''',
                'cipsstaticcryptomappeer',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapPfs', REFERENCE_ENUM_CLASS, 'DiffHellmanGrp_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'DiffHellmanGrp_Enum', 
                [], [], 
                '''                This object identifies if the tunnels instantiated
                due to this policy item should use Perfect Forward Secrecy 
                (PFS) and if so, what group of Oakley they should use.
                ''',
                'cipsstaticcryptomappfs',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapType', REFERENCE_ENUM_CLASS, 'CryptomapType_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CryptomapType_Enum', 
                [], [], 
                '''                The type of the cryptomap entry. This can be an ISAKMP
                cryptomap, CET or manual. Dynamic cryptomaps are not
                counted in this table.
                ''',
                'cipsstaticcryptomaptype',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsStaticCryptomapEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsStaticCryptomapTable' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsStaticCryptomapTable',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapEntry', REFERENCE_LIST, 'CipsStaticCryptomapEntry' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry', 
                [], [], 
                '''                Each entry contains the attributes 
                associated with a single static 
                (fully specified) cryptomap entry.
                This table does not include the members 
                of dynamic cryptomap sets that may be
                linked with the parent static cryptomap set.
                ''',
                'cipsstaticcryptomapentry',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsStaticCryptomapTable',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsSysCapacityGroup' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsSysCapacityGroup',
            False, 
            [
            _MetaInfoClassMember('cips3DesCapable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value of this object is TRUE if the 
                managed entity has the hardware nad software 
                features to support 3DES encryption algorithm.
                
                Not affected by any CLI operation.
                ''',
                'cips3descapable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsMaxSAs', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The maximum number of IPsec Security Associations
                that can be established on this managed entity.
                If no theoretical limit exists, this
                returns value 0.
                
                Not affected by any CLI operation.
                ''',
                'cipsmaxsas',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsSysCapacityGroup',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB.CipsTrapCntlGroup' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB.CipsTrapCntlGroup',
            False, 
            [
            _MetaInfoClassMember('cipsCntlCryptomapAdded', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec Cryptomap Add trap.
                ''',
                'cipscntlcryptomapadded',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapDeleted', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec Cryptomap Delete trap.
                ''',
                'cipscntlcryptomapdeleted',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapSetAttached', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec trap that is issued
                when a cryptomap set is attached to an interface.
                ''',
                'cipscntlcryptomapsetattached',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapSetDetached', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec trap that is issued
                when a cryptomap set is detached from an interface.
                to which it was earlier bound.
                ''',
                'cipscntlcryptomapsetdetached',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlIsakmpPolicyAdded', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec ISAKMP Policy Add trap.
                ''',
                'cipscntlisakmppolicyadded',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlIsakmpPolicyDeleted', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec ISAKMP Policy Delete trap.
                ''',
                'cipscntlisakmppolicydeleted',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlTooManySAs', REFERENCE_ENUM_CLASS, 'TrapStatus_Enum' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'TrapStatus_Enum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec trap that is issued
                when the number of SAs crosses the maximum
                number of SAs that may be supported on
                the managed entity.
                ''',
                'cipscntltoomanysas',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsTrapCntlGroup',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
    'CISCOIPSECMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIPSECMIB',
            False, 
            [
            _MetaInfoClassMember('cipsCryptomapSetIfTable', REFERENCE_CLASS, 'CipsCryptomapSetIfTable' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsCryptomapSetIfTable', 
                [], [], 
                '''                The table lists the binding of cryptomap sets
                to the interfaces of the managed entity.
                ''',
                'cipscryptomapsetiftable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsDynamicCryptomapSetTable', REFERENCE_CLASS, 'CipsDynamicCryptomapSetTable' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsDynamicCryptomapSetTable', 
                [], [], 
                '''                The table containing the list of all dynamic
                cryptomaps that use IKE, defined on 
                 the managed entity.
                ''',
                'cipsdynamiccryptomapsettable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIPsecGlobals', REFERENCE_CLASS, 'CipsIPsecGlobals' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsIPsecGlobals', 
                [], [], 
                '''                ''',
                'cipsipsecglobals',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIPsecStatistics', REFERENCE_CLASS, 'CipsIPsecStatistics' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsIPsecStatistics', 
                [], [], 
                '''                ''',
                'cipsipsecstatistics',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpGroup', REFERENCE_CLASS, 'CipsIsakmpGroup' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsIsakmpGroup', 
                [], [], 
                '''                ''',
                'cipsisakmpgroup',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolicyTable', REFERENCE_CLASS, 'CipsIsakmpPolicyTable' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsIsakmpPolicyTable', 
                [], [], 
                '''                The table containing the list of all
                ISAKMP policy entries configured by the operator.
                ''',
                'cipsisakmppolicytable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetTable', REFERENCE_CLASS, 'CipsStaticCryptomapSetTable' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsStaticCryptomapSetTable', 
                [], [], 
                '''                The table containing the list of all
                cryptomap sets that are fully specified
                and are not wild-carded.
                
                The operator may include different types of
                cryptomaps in such a set - manual, CET,
                ISAKMP or dynamic.
                ''',
                'cipsstaticcryptomapsettable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapTable', REFERENCE_CLASS, 'CipsStaticCryptomapTable' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsStaticCryptomapTable', 
                [], [], 
                '''                The table ilisting the member cryptomaps
                of the cryptomap sets that are configured
                on the managed entity.
                ''',
                'cipsstaticcryptomaptable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSysCapacityGroup', REFERENCE_CLASS, 'CipsSysCapacityGroup' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsSysCapacityGroup', 
                [], [], 
                '''                ''',
                'cipssyscapacitygroup',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsTrapCntlGroup', REFERENCE_CLASS, 'CipsTrapCntlGroup' , 'ydk.models.ipsec.CISCO_IPSEC_MIB', 'CISCOIPSECMIB.CipsTrapCntlGroup', 
                [], [], 
                '''                ''',
                'cipstrapcntlgroup',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'CISCO-IPSEC-MIB',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.ipsec.CISCO_IPSEC_MIB'
        ),
    },
}
_meta_table['CISCOIPSECMIB.CipsCryptomapSetIfTable.CipsCryptomapSetIfEntry']['meta_info'].parent =_meta_table['CISCOIPSECMIB.CipsCryptomapSetIfTable']['meta_info']
_meta_table['CISCOIPSECMIB.CipsDynamicCryptomapSetTable.CipsDynamicCryptomapSetEntry']['meta_info'].parent =_meta_table['CISCOIPSECMIB.CipsDynamicCryptomapSetTable']['meta_info']
_meta_table['CISCOIPSECMIB.CipsIsakmpPolicyTable.CipsIsakmpPolicyEntry']['meta_info'].parent =_meta_table['CISCOIPSECMIB.CipsIsakmpPolicyTable']['meta_info']
_meta_table['CISCOIPSECMIB.CipsStaticCryptomapSetTable.CipsStaticCryptomapSetEntry']['meta_info'].parent =_meta_table['CISCOIPSECMIB.CipsStaticCryptomapSetTable']['meta_info']
_meta_table['CISCOIPSECMIB.CipsStaticCryptomapTable.CipsStaticCryptomapEntry']['meta_info'].parent =_meta_table['CISCOIPSECMIB.CipsStaticCryptomapTable']['meta_info']
_meta_table['CISCOIPSECMIB.CipsCryptomapSetIfTable']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsDynamicCryptomapSetTable']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsIPsecGlobals']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsIPsecStatistics']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsIsakmpGroup']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsIsakmpPolicyTable']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsStaticCryptomapSetTable']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsStaticCryptomapTable']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsSysCapacityGroup']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
_meta_table['CISCOIPSECMIB.CipsTrapCntlGroup']['meta_info'].parent =_meta_table['CISCOIPSECMIB']['meta_info']
