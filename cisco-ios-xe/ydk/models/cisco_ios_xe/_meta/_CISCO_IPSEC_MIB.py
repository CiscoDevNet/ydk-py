


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CryptomapsetbindstatusEnum' : _MetaInfoEnum('CryptomapsetbindstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'unknown':'unknown',
            'attached':'attached',
            'detached':'detached',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'IkeidentitytypeEnum' : _MetaInfoEnum('IkeidentitytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'isakmpIdTypeUNKNOWN':'isakmpIdTypeUNKNOWN',
            'isakmpIdTypeADDRESS':'isakmpIdTypeADDRESS',
            'isakmpIdTypeHOSTNAME':'isakmpIdTypeHOSTNAME',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'CryptomaptypeEnum' : _MetaInfoEnum('CryptomaptypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'cryptomapTypeNONE':'cryptomapTypeNONE',
            'cryptomapTypeMANUAL':'cryptomapTypeMANUAL',
            'cryptomapTypeISAKMP':'cryptomapTypeISAKMP',
            'cryptomapTypeCET':'cryptomapTypeCET',
            'cryptomapTypeDYNAMIC':'cryptomapTypeDYNAMIC',
            'cryptomapTypeDYNAMICDISCOVERY':'cryptomapTypeDYNAMICDISCOVERY',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'EncryptalgoEnum' : _MetaInfoEnum('EncryptalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'none':'none',
            'des':'des',
            'des3':'des3',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'DiffhellmangrpEnum' : _MetaInfoEnum('DiffhellmangrpEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'none':'none',
            'dhGroup1':'dhGroup1',
            'dhGroup2':'dhGroup2',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'IkeauthmethodEnum' : _MetaInfoEnum('IkeauthmethodEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'none':'none',
            'preSharedKey':'preSharedKey',
            'rsaSig':'rsaSig',
            'rsaEncrypt':'rsaEncrypt',
            'revPublicKey':'revPublicKey',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'TrapstatusEnum' : _MetaInfoEnum('TrapstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'IkehashalgoEnum' : _MetaInfoEnum('IkehashalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB',
        {
            'none':'none',
            'md5':'md5',
            'sha':'sha',
        }, 'CISCO-IPSEC-MIB', _yang_ns._namespaces['CISCO-IPSEC-MIB']),
    'CiscoIpsecMib.Cipsisakmpgroup' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsisakmpgroup',
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
            _MetaInfoClassMember('cipsIsakmpIdentity', REFERENCE_ENUM_CLASS, 'IkeidentitytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'IkeidentitytypeEnum', 
                [], [], 
                '''                The value of this object is shows the type of
                identity used by the managed entity in ISAKMP
                negotiations with another peer.
                ''',
                'cipsisakmpidentity',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpKeepaliveInterval', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                The value of this object is time interval in
                seconds between successive ISAKMP keepalive
                heartbeats issued to the peers to which IKE
                tunnels have been setup.
                ''',
                'cipsisakmpkeepaliveinterval',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumIsakmpPolicies', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsipsecglobals' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsipsecglobals',
            False, 
            [
            _MetaInfoClassMember('cipsNumCETCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of static Cryptomap Sets that have 
                at least one CET cryptomap element
                as a member of the set.
                ''',
                'cipsnumcetcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumDynamicCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of dynamic IPSec Policy templates
                (called 'dynamic cryptomap templates') configured
                on the managed entity.
                ''',
                'cipsnumdynamiccryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumStaticCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of Cryptomap Sets that are are fully
                configured. Statically defined cryptomap sets 
                are ones where the operator has fully specified
                all the parameters required set up IPSec 
                Virtual Private Networks (VPNs).
                ''',
                'cipsnumstaticcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDCryptomapSets', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of static Cryptomap Sets that have 
                at least one dynamic cryptomap template 
                bound to them which has the Tunnel Endpoint Discovery
                (TED) enabled.
                ''',
                'cipsnumtedcryptomapsets',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSALifesize', ATTRIBUTE, 'int' , None, None, 
                [('2560', '536870912')], [], 
                '''                The default lifesize in KBytes assigned to an SA 
                as a global policy (unless overridden in cryptomap 
                definition)
                ''',
                'cipssalifesize',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSALifetime', ATTRIBUTE, 'int' , None, None, 
                [('120', '86400')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsipsecstatistics' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsipsecstatistics',
            False, 
            [
            _MetaInfoClassMember('cipsNumTEDFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of TED probes that were dispatched by 
                the local entity and that failed to locate crypto 
                endpoint.  Not affected by any CLI operation.
                ''',
                'cipsnumtedfailures',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDProbesReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of TED probes that were received by this 
                managed entity since bootup. Not affected by any 
                CLI operation.
                ''',
                'cipsnumtedprobesreceived',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsNumTEDProbesSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipssyscapacitygroup' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipssyscapacitygroup',
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
                [('0', '65535')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipstrapcntlgroup' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipstrapcntlgroup',
            False, 
            [
            _MetaInfoClassMember('cipsCntlCryptomapAdded', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec Cryptomap Add trap.
                ''',
                'cipscntlcryptomapadded',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapDeleted', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec Cryptomap Delete trap.
                ''',
                'cipscntlcryptomapdeleted',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapSetAttached', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec trap that is issued
                when a cryptomap set is attached to an interface.
                ''',
                'cipscntlcryptomapsetattached',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlCryptomapSetDetached', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec trap that is issued
                when a cryptomap set is detached from an interface.
                to which it was earlier bound.
                ''',
                'cipscntlcryptomapsetdetached',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlIsakmpPolicyAdded', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec ISAKMP Policy Add trap.
                ''',
                'cipscntlisakmppolicyadded',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlIsakmpPolicyDeleted', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
                [], [], 
                '''                This object defines the administrative state of 
                sending the IOS IPsec ISAKMP Policy Delete trap.
                ''',
                'cipscntlisakmppolicydeleted',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsCntlTooManySAs', REFERENCE_ENUM_CLASS, 'TrapstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'TrapstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry',
            False, 
            [
            _MetaInfoClassMember('cipsIsakmpPolPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The priotity of this ISAKMP Policy entry.
                This is also the index of this table.
                ''',
                'cipsisakmppolpriority',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsIsakmpPolAuth', REFERENCE_ENUM_CLASS, 'IkeauthmethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'IkeauthmethodEnum', 
                [], [], 
                '''                The peer authentication mthod specified by
                this ISAKMP policy specification. If this policy
                entity is selected for negotiation with a peer,
                the local entity would authenticate the peer using 
                the method specified by this object.
                ''',
                'cipsisakmppolauth',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolEncr', REFERENCE_ENUM_CLASS, 'EncryptalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'EncryptalgoEnum', 
                [], [], 
                '''                The encryption transform specified by this 
                ISAKMP policy specification. The Internet Key Exchange
                (IKE) tunnels setup using this policy item would
                use the specified encryption transform to protect the
                ISAKMP PDUs.
                ''',
                'cipsisakmppolencr',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolGroup', REFERENCE_ENUM_CLASS, 'DiffhellmangrpEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'DiffhellmangrpEnum', 
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
            _MetaInfoClassMember('cipsIsakmpPolHash', REFERENCE_ENUM_CLASS, 'IkehashalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'IkehashalgoEnum', 
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
                [('60', '86400')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsisakmppolicytable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsisakmppolicytable',
            False, 
            [
            _MetaInfoClassMember('cipsIsakmpPolicyEntry', REFERENCE_LIST, 'Cipsisakmppolicyentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The index of the static cryptomap table. The value 
                of the string is the name string assigned by the 
                operator in defining the cryptomap set.
                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumCET', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of cryptomaps of type 'ipsec-cisco' 
                associated with this cryptomap set. Such
                cryptomap elements implement Cisco Encryption Technology
                based Virtual Private Networks.
                ''',
                'cipsstaticcryptomapsetnumcet',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumDisc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of dynamic cryptomap templates
                linked to this cryptomap set that have Tunnel Endpoint
                Discovery (TED) enabled.
                ''',
                'cipsstaticcryptomapsetnumdisc',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumDynamic', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of dynamic cryptomap templates
                linked to this cryptomap set.
                ''',
                'cipsstaticcryptomapsetnumdynamic',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumIsakmp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of cryptomaps associated with this 
                cryptomap set that use ISAKMP protocol to do key
                exchange.
                ''',
                'cipsstaticcryptomapsetnumisakmp',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumManual', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of cryptomaps associated with this 
                cryptomap set that require the operator to manually
                setup the keys and SPIs.
                ''',
                'cipsstaticcryptomapsetnummanual',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetNumSAs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of and IPsec Security Associations
                that are active and were setup using this cryptomap.  
                ''',
                'cipsstaticcryptomapsetnumsas',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of cryptomap entries contained in
                this cryptomap set. 
                ''',
                'cipsstaticcryptomapsetsize',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsStaticCryptomapSetEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsstaticcryptomapsettable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsstaticcryptomapsettable',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetEntry', REFERENCE_LIST, 'Cipsstaticcryptomapsetentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry',
            False, 
            [
            _MetaInfoClassMember('cipsDynamicCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The index of the dynamic cryptomap table. 
                The value of the string is the one assigned 
                by the operator in defining the cryptomap set.
                ''',
                'cipsdynamiccryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsDynamicCryptomapSetNumAssoc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of static cryptomap sets with which
                this dynamic cryptomap is associated.  
                ''',
                'cipsdynamiccryptomapsetnumassoc',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsDynamicCryptomapSetSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of cryptomap entries in this cryptomap.
                ''',
                'cipsdynamiccryptomapsetsize',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'cipsDynamicCryptomapSetEntry',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsdynamiccryptomapsettable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsdynamiccryptomapsettable',
            False, 
            [
            _MetaInfoClassMember('cipsDynamicCryptomapSetEntry', REFERENCE_LIST, 'Cipsdynamiccryptomapsetentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The priority of the cryptomap entry in the 
                cryptomap set. This is the second index component
                of this table.
                ''',
                'cipsstaticcryptomappriority',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
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
                [('0', 'None'), ('2560', '536870912')], [], 
                '''                This object identifies the lifesize (maximum traffic
                in bytes that may be carried) of the IPSec SAs
                created using this IPSec policy entry. 
                If this value is zero, the lifetime assumes the 
                value specified by the global lifesize parameter.
                ''',
                'cipsstaticcryptomaplifesize',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapLifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('120', '86400')], [], 
                '''                This object identifies the lifetime of the IPSec
                Security Associations (SA) created using this IPSec policy
                entry. If this value is zero, the lifetime assumes the 
                value specified by the global lifetime parameter.
                ''',
                'cipsstaticcryptomaplifetime',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapNumPeers', ATTRIBUTE, 'int' , None, None, 
                [('0', '40')], [], 
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
            _MetaInfoClassMember('cipsStaticCryptomapPfs', REFERENCE_ENUM_CLASS, 'DiffhellmangrpEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'DiffhellmangrpEnum', 
                [], [], 
                '''                This object identifies if the tunnels instantiated
                due to this policy item should use Perfect Forward Secrecy 
                (PFS) and if so, what group of Oakley they should use.
                ''',
                'cipsstaticcryptomappfs',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapType', REFERENCE_ENUM_CLASS, 'CryptomaptypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CryptomaptypeEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipsstaticcryptomaptable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipsstaticcryptomaptable',
            False, 
            [
            _MetaInfoClassMember('cipsStaticCryptomapEntry', REFERENCE_LIST, 'Cipsstaticcryptomapentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsStaticCryptomapSetName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'cipsstaticcryptomapsetname',
                'CISCO-IPSEC-MIB', True),
            _MetaInfoClassMember('cipsCryptomapSetIfStatus', REFERENCE_ENUM_CLASS, 'CryptomapsetbindstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CryptomapsetbindstatusEnum', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib.Cipscryptomapsetiftable' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib.Cipscryptomapsetiftable',
            False, 
            [
            _MetaInfoClassMember('cipsCryptomapSetIfEntry', REFERENCE_LIST, 'Cipscryptomapsetifentry' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
    'CiscoIpsecMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpsecMib',
            False, 
            [
            _MetaInfoClassMember('cipsCryptomapSetIfTable', REFERENCE_CLASS, 'Cipscryptomapsetiftable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipscryptomapsetiftable', 
                [], [], 
                '''                The table lists the binding of cryptomap sets
                to the interfaces of the managed entity.
                ''',
                'cipscryptomapsetiftable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsDynamicCryptomapSetTable', REFERENCE_CLASS, 'Cipsdynamiccryptomapsettable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsdynamiccryptomapsettable', 
                [], [], 
                '''                The table containing the list of all dynamic
                cryptomaps that use IKE, defined on 
                 the managed entity.
                ''',
                'cipsdynamiccryptomapsettable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIPsecGlobals', REFERENCE_CLASS, 'Cipsipsecglobals' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsipsecglobals', 
                [], [], 
                '''                ''',
                'cipsipsecglobals',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIPsecStatistics', REFERENCE_CLASS, 'Cipsipsecstatistics' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsipsecstatistics', 
                [], [], 
                '''                ''',
                'cipsipsecstatistics',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpGroup', REFERENCE_CLASS, 'Cipsisakmpgroup' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsisakmpgroup', 
                [], [], 
                '''                ''',
                'cipsisakmpgroup',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsIsakmpPolicyTable', REFERENCE_CLASS, 'Cipsisakmppolicytable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsisakmppolicytable', 
                [], [], 
                '''                The table containing the list of all
                ISAKMP policy entries configured by the operator.
                ''',
                'cipsisakmppolicytable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsStaticCryptomapSetTable', REFERENCE_CLASS, 'Cipsstaticcryptomapsettable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsstaticcryptomapsettable', 
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
            _MetaInfoClassMember('cipsStaticCryptomapTable', REFERENCE_CLASS, 'Cipsstaticcryptomaptable' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipsstaticcryptomaptable', 
                [], [], 
                '''                The table ilisting the member cryptomaps
                of the cryptomap sets that are configured
                on the managed entity.
                ''',
                'cipsstaticcryptomaptable',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsSysCapacityGroup', REFERENCE_CLASS, 'Cipssyscapacitygroup' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipssyscapacitygroup', 
                [], [], 
                '''                ''',
                'cipssyscapacitygroup',
                'CISCO-IPSEC-MIB', False),
            _MetaInfoClassMember('cipsTrapCntlGroup', REFERENCE_CLASS, 'Cipstrapcntlgroup' , 'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB', 'CiscoIpsecMib.Cipstrapcntlgroup', 
                [], [], 
                '''                ''',
                'cipstrapcntlgroup',
                'CISCO-IPSEC-MIB', False),
            ],
            'CISCO-IPSEC-MIB',
            'CISCO-IPSEC-MIB',
            _yang_ns._namespaces['CISCO-IPSEC-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IPSEC_MIB'
        ),
    },
}
_meta_table['CiscoIpsecMib.Cipsisakmppolicytable.Cipsisakmppolicyentry']['meta_info'].parent =_meta_table['CiscoIpsecMib.Cipsisakmppolicytable']['meta_info']
_meta_table['CiscoIpsecMib.Cipsstaticcryptomapsettable.Cipsstaticcryptomapsetentry']['meta_info'].parent =_meta_table['CiscoIpsecMib.Cipsstaticcryptomapsettable']['meta_info']
_meta_table['CiscoIpsecMib.Cipsdynamiccryptomapsettable.Cipsdynamiccryptomapsetentry']['meta_info'].parent =_meta_table['CiscoIpsecMib.Cipsdynamiccryptomapsettable']['meta_info']
_meta_table['CiscoIpsecMib.Cipsstaticcryptomaptable.Cipsstaticcryptomapentry']['meta_info'].parent =_meta_table['CiscoIpsecMib.Cipsstaticcryptomaptable']['meta_info']
_meta_table['CiscoIpsecMib.Cipscryptomapsetiftable.Cipscryptomapsetifentry']['meta_info'].parent =_meta_table['CiscoIpsecMib.Cipscryptomapsetiftable']['meta_info']
_meta_table['CiscoIpsecMib.Cipsisakmpgroup']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsipsecglobals']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsipsecstatistics']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipssyscapacitygroup']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipstrapcntlgroup']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsisakmppolicytable']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsstaticcryptomapsettable']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsdynamiccryptomapsettable']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipsstaticcryptomaptable']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
_meta_table['CiscoIpsecMib.Cipscryptomapsetiftable']['meta_info'].parent =_meta_table['CiscoIpsecMib']['meta_info']
