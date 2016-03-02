


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CiiMetricStyle_Enum' : _MetaInfoEnum('CiiMetricStyle_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'narrow':'NARROW',
            'wide':'WIDE',
            'both':'BOTH',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CiiLevelState_Enum' : _MetaInfoEnum('CiiLevelState_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'off':'OFF',
            'on':'ON',
            'waiting':'WAITING',
            'overloaded':'OVERLOADED',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CiiSupportedProtocol_Enum' : _MetaInfoEnum('CiiSupportedProtocol_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'iso8473':'ISO8473',
            'ipV6':'IPV6',
            'ip':'IP',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CiiAdminState_Enum' : _MetaInfoEnum('CiiAdminState_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'on':'ON',
            'off':'OFF',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CiiMetricType_Enum' : _MetaInfoEnum('CiiMetricType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'internal':'INTERNAL',
            'external':'EXTERNAL',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CiiISLevel_Enum' : _MetaInfoEnum('CiiISLevel_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'none':'NONE',
            'area':'AREA',
            'domain':'DOMAIN',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiAreaAddrTable.CiiAreaAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiAreaAddrTable.CiiAreaAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiAreaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                An area address reported in a Level 1 LSP.
                ''',
                'ciiareaaddr',
                'CISCO-IETF-ISIS-MIB', True),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiAreaAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiAreaAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiAreaAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiAreaAddrEntry', REFERENCE_LIST, 'CiiAreaAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiAreaAddrTable.CiiAreaAddrEntry', 
                [], [], 
                '''                Each entry contains one area address reported in a
                Level 1 LSP generated or received by this Intermediate
                System.
                ''',
                'ciiareaaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiAreaAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCirc' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCirc',
            False, 
            [
            _MetaInfoClassMember('ciiNextCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object is used to assign values to
                ciiCircIndex as described in 'Textual
                Conventions for SNMPv2'.  The network manager
                reads this object, and then writes the value
                back as the ciiCircIndex in a SET that creates
                a new instance of ciiCircEntry.  If the SET
                fails with the code 'inconsistentValue', then
                the process must be repeated; If the SET succeeds,
                then the object is incremented, and the new
                ciiCircEntry is created according to the manager's
                directions.
                ''',
                'ciinextcircindex',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCirc',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry.CiiCircLevelIndex_Enum' : _MetaInfoEnum('CiiCircLevelIndex_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1IS':'LEVEL1IS',
            'level2IS':'LEVEL2IS',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiCircLevelIndex', REFERENCE_ENUM_CLASS, 'CiiCircLevelIndex_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry.CiiCircLevelIndex_Enum', 
                [], [], 
                '''                The level that this entry describes.
                ''',
                'ciicirclevelindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiCircLevelCSNPInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 600)], [], 
                '''                Interval of time, in seconds, between periodic
                transmission of a complete set of CSNPs on
                multiaccess networks if this router is the
                designated router at this level.
                
                This object follows the resettingTimer behavior.
                ''',
                'ciicirclevelcsnpinterval',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelDesIS', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (7, None)], [], 
                '''                The ID of the LAN Designated Intermediate System
                on this circuit at this level. If, for any reason,
                this system is not partaking in the relevant
                Designated Intermediate System election process,
                then the value returned is the zero length OCTET STRING.
                ''',
                'ciicircleveldesis',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelDRHelloTimer', ATTRIBUTE, 'int' , None, None, 
                [(10, 120000)], [], 
                '''                Period, in milliseconds, between Hello PDUs on
                multiaccess networks when this IS is the Designated
                Intermediate System.  This object follows the
                resettingTimer behavior.
                ''',
                'ciicircleveldrhellotimer',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelHelloMultiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 100)], [], 
                '''                This value is multiplied by the corresponding HelloTimer
                and the result in seconds (rounded up) is used as the
                holding time in transmitted hellos, to be used by
                receivers of hello packets from this IS
                ''',
                'ciicirclevelhellomultiplier',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelHelloTimer', ATTRIBUTE, 'int' , None, None, 
                [(10, 600000)], [], 
                '''                Maximum period, in milliseconds, between IIH PDUs
                on multiaccess networks at this level for LANs.
                The value at L1 is used as the period between
                Hellos on L1L2 point to point circuits.  Setting
                this value at level 2 on an L1L2 point to point
                circuit will result in an error of InconsistentValue.
                
                This object follows the resettingTimer behavior.
                ''',
                'ciicirclevelhellotimer',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelID', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (7, None)], [], 
                '''                On a point to point circuit with a fully initialized
                adjacency to a peer IS, the value of this object is
                the circuit ID negotiated during adjacency initialization.
                On a point to point circuit without such an adjacency,
                the value is the concatenation of the local system ID
                and the one byte ciiCircLevelIDOctet for this circuit
                i.e. the value that would be proposed for the circuit ID.
                
                On other circuit types, the value returned is the zero
                length OCTET STRING.
                ''',
                'ciicirclevelid',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelIDOctet', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                A one byte identifier that can be used in protocol packets
                to identify a circuit.  Values of ciiCircLevelIDOctet
                do not need to be unique.  They are only required to
                differ on LANs where the Intermediate System is the
                Designated Intermediate System.
                ''',
                'ciicirclevelidoctet',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelISPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 127)], [], 
                '''                The priority for becoming LAN Designated
                Intermediate System at this level.
                ''',
                'ciicirclevelispriority',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelLSPThrottle', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Minimal interval of time, in milliseconds, between
                transmissions of LSPs on an interface at this level.
                ''',
                'ciicirclevellspthrottle',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The metric value of this circuit for this level.
                ''',
                'ciicirclevelmetric',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelMinLSPRetransInt', ATTRIBUTE, 'int' , None, None, 
                [(1, 300)], [], 
                '''                Minimum interval, in seconds, between re-transmission of
                an LSP at this level. This object follows the
                resettingTimer behavior.
                
                Note that ciiCircLevelLSPThrottle controls
                how fast we send back to back LSPs.  This variable
                controls how fast we re-send the same LSP.
                ''',
                'ciicirclevelminlspretransint',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelPartSNPInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 120)], [], 
                '''                Minimum interval in seconds between sending Partial
                Sequence Number PDUs at this level. This object
                follows the resettingTimer behavior.
                ''',
                'ciicirclevelpartsnpinterval',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelWideMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 16777215)], [], 
                '''                The wide metric value of this circuit for this level.
                ''',
                'ciicirclevelwidemetric',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircLevelEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircLevelTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircLevelTable',
            False, 
            [
            _MetaInfoClassMember('ciiCircLevelEntry', REFERENCE_LIST, 'CiiCircLevelEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry', 
                [], [], 
                '''                An ciiCircLevelEntry exists for each level on
                each circuit used by Integrated IS-IS on this system.
                ''',
                'ciicirclevelentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircLevelTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircLevel_Enum' : _MetaInfoEnum('CiiCircLevel_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1':'LEVEL1',
            'level2':'LEVEL2',
            'level1L2':'LEVEL1L2',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircMeshGroupEnabled_Enum' : _MetaInfoEnum('CiiCircMeshGroupEnabled_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'inactive':'INACTIVE',
            'blocked':'BLOCKED',
            'set':'SET',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircType_Enum' : _MetaInfoEnum('CiiCircType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'broadcast':'BROADCAST',
            'ptToPt':'PTTOPT',
            'staticIn':'STATICIN',
            'staticOut':'STATICOUT',
            'dA':'DA',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircTable.CiiCircEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The identifier of this circuit, unique within the
                Intermediate System.  This object follows
                the index behavior.  This is for SNMP Indexing
                purposes only and need not have any relation to
                any protocol value.
                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiCirc3WayEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this circuit enabled to run 3Way handshake?
                ''',
                'ciicirc3wayenabled',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircAdminState', REFERENCE_ENUM_CLASS, 'CiiAdminState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiAdminState_Enum', 
                [], [], 
                '''                The administrative state of the circuit. This
                object follows the CiiAdminState behavior.
                ''',
                'ciicircadminstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The existence state of this circuit. This object follows
                the RowStatus behavior.  Setting the state to
                'notInService' halts the generation and processing of
                IS-IS protocol PDUs on this circuit.  Setting the state
                to 'destroy' will also erase any configuration associated
                with the circuit.
                ''',
                'ciicircexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircExtDomain', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, suppress normal transmission of and
                interpretation of Intra-domain IS-IS PDUs on this
                circuit.
                ''',
                'ciicircextdomain',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircExtendedCircID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value to be used as the extended circuit ID in
                3Way handshake.  This value is only used if
                ciiCirc3WayEnabled is true, and must be unique across
                all circuits on this IS.
                ''',
                'ciicircextendedcircid',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The value of ifIndex for the interface to which this
                circuit corresponds.   This object cannot be modified
                after creation
                ''',
                'ciicircifindex',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircIfSubIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                A specifier for the part of the interface ifIndex to which
                this circuit corresponds, such as a DLCI or VPI/VCI.
                This object cannot be modified after creation
                ''',
                'ciicircifsubindex',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLastUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If the circuit is enabled, the value of sysUpTime
                when ciiCircAdminState most recently entered
                the state 'on'.  If the circuit is not 'on',
                the value of sysUpTime when the circuit last
                entered state 'on', 0 if the circuit has never
                been 'on'.
                ''',
                'ciicirclastuptime',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevel', REFERENCE_ENUM_CLASS, 'CiiCircLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircLevel_Enum', 
                [], [], 
                '''                Indicates which type of packets will be sent and
                accepted on this circuit. The values used will be
                modified by the settings of ciiSysType. This
                object follows the replaceOnlyWhileDisabled behavior.
                ''',
                'ciicirclevel',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircMeshGroup', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Circuits in the same mesh group act as a virtual
                multiaccess network.  LSPs seen on one circuit in
                a mesh group will not be flooded to another circuit
                in the same mesh group.  If ciiCircMeshGroupEnabled
                is inactive or blocked, this value is ignored.
                ''',
                'ciicircmeshgroup',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircMeshGroupEnabled', REFERENCE_ENUM_CLASS, 'CiiCircMeshGroupEnabled_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircMeshGroupEnabled_Enum', 
                [], [], 
                '''                Is this port a member of a mesh group, or blocked?
                Circuits in the same mesh group act as a virtual
                multiaccess network.  LSPs seen on one circuit in
                a mesh group will not be flooded to another circuit
                in the same mesh group.
                ''',
                'ciicircmeshgroupenabled',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircPassiveCircuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Should we include this interface in LSPs, even if
                it is not running the IS-IS Protocol?
                ''',
                'ciicircpassivecircuit',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircSmallHellos', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Can we send unpadded hellos on LAN circuits?  'false'
                means LAN Hellos must be padded.
                Implementations should allow the administrator to read
                this value.  An implementation need not be able to
                support unpadded hellos to be conformant.
                ''',
                'ciicircsmallhellos',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircType', REFERENCE_ENUM_CLASS, 'CiiCircType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry.CiiCircType_Enum', 
                [], [], 
                '''                The type of the circuit. This object follows the
                replaceOnlyWhileDisabled behavior. The type specified
                must be compatible with the type of the interface defined
                by the value of ciiCircIfIndex.
                ''',
                'ciicirctype',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircTable',
            False, 
            [
            _MetaInfoClassMember('ciiCircEntry', REFERENCE_LIST, 'CiiCircEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircTable.CiiCircEntry', 
                [], [], 
                '''                An ciiCircEntry exists for each circuit used by
                Integrated IS-IS on this system.
                ''',
                'ciicircentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry.CiiCircuitType_Enum' : _MetaInfoEnum('CiiCircuitType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'lanlevel1':'LANLEVEL1',
            'lanlevel2':'LANLEVEL2',
            'p2pcircuit':'P2PCIRCUIT',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiCircuitType', REFERENCE_ENUM_CLASS, 'CiiCircuitType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry.CiiCircuitType_Enum', 
                [], [], 
                '''                What type of circuit saw these counts?
                
                The point to point Hello PDU includes
                both L1 and L2, and ISs form a single
                adjacency on point to point links.
                Thus we combine counts on
                point to point links into one group.
                ''',
                'ciicircuittype',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiCircAdjChanges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an adjacency state change has
                occurred on this circuit.
                ''',
                'ciicircadjchanges',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an IS-IS control PDU with
                the correct auth type has failed to pass authentication
                validation.
                ''',
                'ciicircauthfails',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircAuthTypeFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an IS-IS control PDU with
                an auth type field different to that for this
                system has been received.
                ''',
                'ciicircauthtypefails',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircIDFieldLenMismatches', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an IS-IS control PDU with an ID
                field length different to that for this system has been
                received.
                ''',
                'ciicircidfieldlenmismatches',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircInitFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times initialization of this circuit has
                failed.  This counts events such as PPP NCP failures.
                Failures to form an adjacency are counted by
                ciiCircRejAdjs.
                ''',
                'ciicircinitfails',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLANDesISChanges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the Designated IS has changed
                on this circuit at this level.  If the circuit is
                point to point, this count is zero.
                ''',
                'ciicirclandesischanges',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircMaxAreaAddrMismatches', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an IS-IS control PDU with a
                max area address field different to that for this
                system has been received.
                ''',
                'ciicircmaxareaaddrmismatches',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircNumAdj', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of adjacencies on this circuit.
                ''',
                'ciicircnumadj',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircRejAdjs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an adjacency has been rejected on
                this circuit.
                ''',
                'ciicircrejadjs',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircuitCounterEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiCircuitCounterTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiCircuitCounterTable',
            False, 
            [
            _MetaInfoClassMember('ciiCircuitCounterEntry', REFERENCE_LIST, 'CiiCircuitCounterEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry', 
                [], [], 
                '''                An ciiCircuitCounterEntry exists for each circuit
                used by Integrated IS-IS on this system.
                ''',
                'ciicircuitcounterentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiCircuitCounterTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry.CiiIPRASourceType_Enum' : _MetaInfoEnum('CiiIPRASourceType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'static':'STATIC',
            'direct':'DIRECT',
            'ospfv2':'OSPFV2',
            'ospfv3':'OSPFV3',
            'isis':'ISIS',
            'rip':'RIP',
            'igrp':'IGRP',
            'eigrp':'EIGRP',
            'bgp':'BGP',
            'other':'OTHER',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry.CiiIPRAType_Enum' : _MetaInfoEnum('CiiIPRAType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'manual':'MANUAL',
            'automatic':'AUTOMATIC',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry',
            False, 
            [
            _MetaInfoClassMember('ciiIPRADest', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The destination of this IP Reachable Address. This is
                either a network address, subnetwork address or host
                address. This object follows the ManualOrAutomatic
                behavior.
                ''',
                'ciiipradest',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiIPRADestPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                The length of the IP Netmask for Reachability Address.
                This object follows the ManualOrAutomatic behavior.
                ''',
                'ciiipradestprefixlen',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiIPRADestType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of this IP Reachable Address.  This object
                follows the ManualOrAutomatic behavior.
                ''',
                'ciiipradesttype',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiIPRANextHopIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Index of next hop.  Used when there are multiple Equal
                Cost Multipath alternatives for the same destination.
                ''',
                'ciiipranexthopindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiIPRAAdminState', REFERENCE_ENUM_CLASS, 'CiiAdminState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiAdminState_Enum', 
                [], [], 
                '''                The administrative state of the IP Reachable Address. This
                object follows the CiiAdminState and ManualOrAutomatic
                behaviors.
                ''',
                'ciiipraadminstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRAExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The state of this IP Reachable Address. This object
                follows the ExistenceState and ManualOrAutomatic
                behaviors.
                ''',
                'ciiipraexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRAFullMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The wide metric value for reaching the specified
                destination over this circuit. This object follows the
                ManualOrAutomatic behavior.
                ''',
                'ciiiprafullmetric',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRAMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The metric value for reaching the specified
                destination over this circuit. This object follows the
                ManualOrAutomatic behavior.
                ''',
                'ciiiprametric',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRAMetricType', REFERENCE_ENUM_CLASS, 'CiiMetricType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiMetricType_Enum', 
                [], [], 
                '''                Indicates whether the metric is internal or
                external. This object follows the ManualOrAutomatic
                behavior.
                ''',
                'ciiiprametrictype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRANextHop', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP next hop to this destination.
                ''',
                'ciiipranexthop',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRANextHopType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of the IP next hop address.
                ''',
                'ciiipranexthoptype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRASNPAAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                The SNPA Address to which a PDU may be forwarded in
                order to reach a destination which matches this IP
                Reachable Address. This object follows the
                ManualOrAutomatic behavior.
                ''',
                'ciiiprasnpaaddress',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRASourceType', REFERENCE_ENUM_CLASS, 'CiiIPRASourceType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry.CiiIPRASourceType_Enum', 
                [], [], 
                '''                The origin of this route.
                ''',
                'ciiiprasourcetype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRAType', REFERENCE_ENUM_CLASS, 'CiiIPRAType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry.CiiIPRAType_Enum', 
                [], [], 
                '''                The type of this IP Reachable Address. Those of type
                manual are created by the network manager. Those of type
                automatic are created through propagation of routing
                information from another routing protocol.  This object
                follows the ManualOrAutomatic behavior.
                ''',
                'ciiipratype',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiIPRAEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiIPRATable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiIPRATable',
            False, 
            [
            _MetaInfoClassMember('ciiIPRAEntry', REFERENCE_LIST, 'CiiIPRAEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry', 
                [], [], 
                '''                Each entry defines an IP Reachable Address to a network,
                subnetwork or host.
                
                Each IP Reachable Address may have multiple entries in the
                table, one for each equal cost path to the reachable address.
                ''',
                'ciiipraentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiIPRATable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjAreaAddrTable.CiiISAdjAreaAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjAreaAddrTable.CiiISAdjAreaAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjAreaAddrIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                An index for the areas associated with one neighbor.
                This provides a simple way to walk the table.
                ''',
                'ciiisadjareaaddrindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                ''',
                'ciiisadjindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjAreaAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                One Area Address as reported in IIH PDUs received from
                the neighbor.
                ''',
                'ciiisadjareaaddress',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjAreaAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjAreaAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjAreaAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiISAdjAreaAddrEntry', REFERENCE_LIST, 'CiiISAdjAreaAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjAreaAddrTable.CiiISAdjAreaAddrEntry', 
                [], [], 
                '''                Each entry contains one Area Address reported by a
                neighboring Intermediate System in its IIH PDUs.
                ''',
                'ciiisadjareaaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjAreaAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjIPAddrTable.CiiISAdjIPAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjIPAddrTable.CiiISAdjIPAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                ''',
                'ciiisadjindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIPAddrIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                An index to this table which identifies the IP addresses
                to which this entry belongs.
                ''',
                'ciiisadjipaddrindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIPAddrAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                One IP Address as reported in IIH PDUs received from the
                neighbor.
                ''',
                'ciiisadjipaddraddress',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjIPAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The type of one IP Address as reported in IIH PDUs
                received from the neighbor.
                ''',
                'ciiisadjipaddrtype',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjIPAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjIPAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjIPAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiISAdjIPAddrEntry', REFERENCE_LIST, 'CiiISAdjIPAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjIPAddrTable.CiiISAdjIPAddrEntry', 
                [], [], 
                '''                Each entry contains one IP Address reported by a
                neighboring Intermediate System in its IIH PDUs.
                ''',
                'ciiisadjipaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjIPAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjProtSuppTable.CiiISAdjProtSuppEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjProtSuppTable.CiiISAdjProtSuppEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                ''',
                'ciiisadjindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjProtSuppProtocol', REFERENCE_ENUM_CLASS, 'CiiSupportedProtocol_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiSupportedProtocol_Enum', 
                [], [], 
                '''                One supported protocol as reported in IIH PDUs received
                from the neighbor.
                ''',
                'ciiisadjprotsuppprotocol',
                'CISCO-IETF-ISIS-MIB', True),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjProtSuppEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjProtSuppTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjProtSuppTable',
            False, 
            [
            _MetaInfoClassMember('ciiISAdjProtSuppEntry', REFERENCE_LIST, 'CiiISAdjProtSuppEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjProtSuppTable.CiiISAdjProtSuppEntry', 
                [], [], 
                '''                Each entry contains one protocol supported by a
                neighboring Intermediate System as reported in its IIH
                PDUs.
                ''',
                'ciiisadjprotsuppentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjProtSuppTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdj3WayState_Enum' : _MetaInfoEnum('CiiISAdj3WayState_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'up':'UP',
            'initializing':'INITIALIZING',
            'down':'DOWN',
            'failed':'FAILED',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjNeighSysType_Enum' : _MetaInfoEnum('CiiISAdjNeighSysType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'l1IntermediateSystem':'L1INTERMEDIATESYSTEM',
            'l2IntermediateSystem':'L2INTERMEDIATESYSTEM',
            'l1L2IntermediateSystem':'L1L2INTERMEDIATESYSTEM',
            'unknown':'UNKNOWN',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjState_Enum' : _MetaInfoEnum('CiiISAdjState_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'down':'DOWN',
            'initializing':'INITIALIZING',
            'up':'UP',
            'failed':'FAILED',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjUsage_Enum' : _MetaInfoEnum('CiiISAdjUsage_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1':'LEVEL1',
            'level2':'LEVEL2',
            'level1and2':'LEVEL1AND2',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdjIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                A unique value identifying the IS adjacency from all
                other such adjacencies on this circuit. This value is
                automatically assigned by the system when the adjacency
                is created.
                ''',
                'ciiisadjindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiISAdj3WayState', REFERENCE_ENUM_CLASS, 'CiiISAdj3WayState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdj3WayState_Enum', 
                [], [], 
                '''                The 3Way state of the adjacency.  These are picked
                to match the historical on-the-wire representation
                of the 3Way state, and are not intended to match
                ciiISAdjState.
                ''',
                'ciiisadj3waystate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjHoldTimer', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The holding time in seconds for this adjacency.
                This value is based on received IIH PDUs and
                the elapsed time since receipt.
                ''',
                'ciiisadjholdtimer',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjLastUpTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If the ciiISAdjState is in state 'up', the value
                of sysUpTime when the adjacency most recently
                entered the state 'up',  or 0 if it has never
                been in state 'up'.
                ''',
                'ciiisadjlastuptime',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjNbrExtendedCircID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The 4 byte Extended Circuit ID learned from the
                Neighbor during 3-way handshake, or 0.
                ''',
                'ciiisadjnbrextendedcircid',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjNeighPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 127)], [], 
                '''                Priority of the neighboring Intermediate System for
                becoming the Designated Intermediate System.
                ''',
                'ciiisadjneighpriority',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjNeighSNPAAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                The SNPA address of the neighboring system.
                ''',
                'ciiisadjneighsnpaaddress',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjNeighSysID', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The system ID of the neighboring Intermediate
                System.
                ''',
                'ciiisadjneighsysid',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjNeighSysType', REFERENCE_ENUM_CLASS, 'CiiISAdjNeighSysType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjNeighSysType_Enum', 
                [], [], 
                '''                The type of the neighboring system.
                ''',
                'ciiisadjneighsystype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjState', REFERENCE_ENUM_CLASS, 'CiiISAdjState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjState_Enum', 
                [], [], 
                '''                The state of the adjacency
                ''',
                'ciiisadjstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjUsage', REFERENCE_ENUM_CLASS, 'CiiISAdjUsage_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry.CiiISAdjUsage_Enum', 
                [], [], 
                '''                How is the adjacency used?  On a point-to-point link,
                this might be level1and2, but on a LAN, the usage will
                be level1 on the adjacency between peers at L1,
                and level2 for the adjacency between peers at L2.
                ''',
                'ciiisadjusage',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiISAdjTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiISAdjTable',
            False, 
            [
            _MetaInfoClassMember('ciiISAdjEntry', REFERENCE_LIST, 'CiiISAdjEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry', 
                [], [], 
                '''                Each entry corresponds to one adjacency to an
                Intermediate System on this system.
                ''',
                'ciiisadjentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiISAdjTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiLSPSummaryTable.CiiLSPSummaryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiLSPSummaryTable.CiiLSPSummaryEntry',
            False, 
            [
            _MetaInfoClassMember('ciiLSPID', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (8, None)], [], 
                '''                The 8 byte LSP ID, consisting of the SystemID,
                Circuit ID, and Fragment Number.
                ''',
                'ciilspid',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiLSPLevel', REFERENCE_ENUM_CLASS, 'CiiISLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiISLevel_Enum', 
                [], [], 
                '''                At which level does this LSP appear?
                ''',
                'ciilsplevel',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiLSPAttributes', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Flags carried by the LSP.
                ''',
                'ciilspattributes',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPChecksum', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The 16 bit Fletcher Checksum.
                ''',
                'ciilspchecksum',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPLifetimeRemain', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The remaining lifetime in seconds for this LSP.
                ''',
                'ciilsplifetimeremain',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPPDULength', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The length of this LSP.
                ''',
                'ciilsppdulength',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPSeq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sequence number for this LSP.
                ''',
                'ciilspseq',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPZeroLife', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this LSP being purged by this System?
                ''',
                'ciilspzerolife',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiLSPSummaryEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiLSPSummaryTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiLSPSummaryTable',
            False, 
            [
            _MetaInfoClassMember('ciiLSPSummaryEntry', REFERENCE_LIST, 'CiiLSPSummaryEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiLSPSummaryTable.CiiLSPSummaryEntry', 
                [], [], 
                '''                Each entry provides a summary describing an
                LSP currently stored in the system.
                ''',
                'ciilspsummaryentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiLSPSummaryTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiLSPTLVTable.CiiLSPTLVEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiLSPTLVTable.CiiLSPTLVEntry',
            False, 
            [
            _MetaInfoClassMember('ciiLSPID', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (8, None)], [], 
                '''                ''',
                'ciilspid',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiLSPLevel', REFERENCE_ENUM_CLASS, 'CiiISLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiISLevel_Enum', 
                [], [], 
                '''                ''',
                'ciilsplevel',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiLSPTLVIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of this TLV in the LSP.  The first TLV has index 1
                and the Nth TLV has an index of N.
                ''',
                'ciilsptlvindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiLSPTLVChecksum', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The 16 bit Fletcher Checksum.
                ''',
                'ciilsptlvchecksum',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPTLVLen', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The length of this TLV.
                ''',
                'ciilsptlvlen',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPTLVSeq', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sequence number for this LSP.
                ''',
                'ciilsptlvseq',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPTLVType', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The type of this TLV.
                ''',
                'ciilsptlvtype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPTLVValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of this TLV.
                ''',
                'ciilsptlvvalue',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiLSPTLVEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiLSPTLVTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiLSPTLVTable',
            False, 
            [
            _MetaInfoClassMember('ciiLSPTLVEntry', REFERENCE_LIST, 'CiiLSPTLVEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiLSPTLVTable.CiiLSPTLVEntry', 
                [], [], 
                '''                Each entry describes an LSP current stored in the
                system.
                ''',
                'ciilsptlventry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiLSPTLVTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiManAreaAddrTable.CiiManAreaAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiManAreaAddrTable.CiiManAreaAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiManAreaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                A manually configured area address for this system. This
                object follows the index behavior.
                
                Note: an index for the entry {1, {49.0001} active} in
                this table would be the ordered pair
                (1, (0x03 0x49 0x00 0x01)), as the length of an Octet
                string is part of the OID.
                ''',
                'ciimanareaaddr',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiManAreaAddrExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The state of the ciiManAreaAddrEntry. This object
                follows the Row Status behavior. If the ciiSysAdminState
                for this Intermediate System is 'on', and an
                attempt is made to set this object to the value 'destroy'
                or 'notInService' when this is the only
                ciiManAreaAddrEntry in state 'active' for this
                Intermediate System should return inconsistentValue.
                ''',
                'ciimanareaaddrexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiManAreaAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiManAreaAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiManAreaAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiManAreaAddrEntry', REFERENCE_LIST, 'CiiManAreaAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiManAreaAddrTable.CiiManAreaAddrEntry', 
                [], [], 
                '''                Each entry contains one area address manually configured
                on this system
                ''',
                'ciimanareaaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiManAreaAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry.CiiPacketCountDirection_Enum' : _MetaInfoEnum('CiiPacketCountDirection_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'sending':'SENDING',
            'receiving':'RECEIVING',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry.CiiPacketCountLevel_Enum' : _MetaInfoEnum('CiiPacketCountLevel_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1':'LEVEL1',
            'level2':'LEVEL2',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiPacketCountDirection', REFERENCE_ENUM_CLASS, 'CiiPacketCountDirection_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry.CiiPacketCountDirection_Enum', 
                [], [], 
                '''                Were we sending or receiving these PDUs?
                ''',
                'ciipacketcountdirection',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiPacketCountLevel', REFERENCE_ENUM_CLASS, 'CiiPacketCountLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry.CiiPacketCountLevel_Enum', 
                [], [], 
                '''                The level at which these PDU counts have been collected.
                ''',
                'ciipacketcountlevel',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiPacketCountCSNPs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IS-IS CSNP frames seen in this
                direction at this level.
                ''',
                'ciipacketcountcsnps',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountESHellos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ES Hello PDU frames seen in this
                direction.  ESH PDUs are counted at the
                lowest enabled level: at L1 on L1 or L1L2
                circuits, and at L2 otherwise.
                ''',
                'ciipacketcounteshellos',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountIIHellos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IS-IS Hello PDU frames seen in this
                direction at this level.
                
                Point-to-Point IIH PDUs are counted at
                the lowest enabled level: at L1 on L1 or L1L2 circuits,
                and at L2 otherwise.
                ''',
                'ciipacketcountiihellos',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountISHellos', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of ES-IS Hello PDU frames seen in this
                direction.  ISH PDUs are counted at the
                lowest enabled level: at L1 on L1 or L1L2
                circuits, and at L2 otherwise.
                ''',
                'ciipacketcountishellos',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountLSPs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IS-IS LSP frames seen in this
                direction at this level.
                ''',
                'ciipacketcountlsps',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountPSNPs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of IS-IS PSNP frames seen in this
                direction at this level.
                ''',
                'ciipacketcountpsnps',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCountUnknowns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of unknown IS-IS PDU frames seen
                at this level.
                ''',
                'ciipacketcountunknowns',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiPacketCounterEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiPacketCounterTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiPacketCounterTable',
            False, 
            [
            _MetaInfoClassMember('ciiPacketCounterEntry', REFERENCE_LIST, 'CiiPacketCounterEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry', 
                [], [], 
                '''                Information about IS-IS protocol traffic at one level
                on one circuit in one direction
                ''',
                'ciipacketcounterentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiPacketCounterTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRATable.CiiRAEntry.CiiRAMapType_Enum' : _MetaInfoEnum('CiiRAMapType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'none':'NONE',
            'explicit':'EXPLICIT',
            'extractIDI':'EXTRACTIDI',
            'extractDSP':'EXTRACTDSP',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiRATable.CiiRAEntry.CiiRAType_Enum' : _MetaInfoEnum('CiiRAType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'manual':'MANUAL',
            'automatic':'AUTOMATIC',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiRATable.CiiRAEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRATable.CiiRAEntry',
            False, 
            [
            _MetaInfoClassMember('ciiCircIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ciicircindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRAIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2000000000)], [], 
                '''                The identifier for this ciiRAEntry. This value must be
                unique amongst all Reachable Addresses on the same parent
                Circuit. This object follows the index and ManualOrAutomatic
                behaviors.
                ''',
                'ciiraindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRAAddrPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                The destination of this Reachable Address. This is an
                Address Prefix. This object follows the
                replaceOnlyWhileDisabled and ManualOrAutomatic
                behaviors.
                ''',
                'ciiraaddrprefix',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAAdminState', REFERENCE_ENUM_CLASS, 'CiiAdminState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiAdminState_Enum', 
                [], [], 
                '''                The administrative state of the Reachable Address. This
                object follows the CiiAdminState and ManualOrAutomatic
                behaviors.
                ''',
                'ciiraadminstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The existence state of this Reachable Address. This
                object follows the ManualOrAutomatic behaviors.
                ''',
                'ciiraexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAMapType', REFERENCE_ENUM_CLASS, 'CiiRAMapType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRATable.CiiRAEntry.CiiRAMapType_Enum', 
                [], [], 
                '''                The type of mapping to be employed to ascertain the SNPA
                Address which should be used in forwarding PDUs for this
                Reachable Address prefix. This object follows the
                ManualOrAutomatic behavior. The following values of
                mapping type are defined:
                
                    none: The mapping is null because the neighbor SNPA is
                          implicit by nature of the subnetwork (e.g. a
                          point-to-point linkage).
                
                    explicit: The subnetwork addresses in the object
                          ciiRASNPAAddress is to be used.
                
                    extractIDI: The SNPA is embedded in the IDI of
                          the destination NSAP Address. The mapping
                          algorithm extracts the SNPA to be used
                          according to the format and encoding rules of
                          ISO8473/Add2. This SNPA extraction algorithm can
                          be used in conjunction with Reachable Address
                          prefixes from the X.121, F.69, E.163 and E.164
                          addressing subdomains.
                
                    extractDSP: All, or a suffix, of the SNPA is embedded
                          in the DSP of the destination address. This SNPA
                          extraction algorithm extracts the embedded
                          subnetwork addressing information by performing a
                          logical AND of the ciiRASNPAMask object value
                          with the destination address. The part of the
                          SNPA extracted from the destination NSAP is
                          appended to the ciiRASNPAPrefix object value to
                          form the next hop subnetwork addressing
                          information.
                ''',
                'ciiramaptype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The metric value for reaching the specified
                prefix over this circuit. This object follows the
                ManualOrAutomatic behavior.
                ''',
                'ciirametric',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAMetricType', REFERENCE_ENUM_CLASS, 'CiiMetricType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiMetricType_Enum', 
                [], [], 
                '''                Indicates whether the metric is internal or
                external. This object follows the ManualOrAutomatic
                behavior.
                ''',
                'ciirametrictype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRASNPAAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                The SNPA Address to which a PDU may be forwarded in
                order to reach a destination which matches the address
                prefix of the Reachable Address. This object follows the
                ManualOrAutomatic behavior.
                ''',
                'ciirasnpaaddress',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRASNPAMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                A bit mask with 1 bits indicating the positions in the
                effective destination address from which embedded SNPA
                information is to be extracted. For the extraction the
                first octet of the ciiRASNPAMask object value is aligned
                with the first octet (AFI) of the NSAP Address. If the
                ciiRASNPAMask object value and NSAP Address are of
                different lengths, the shorter of the two is logically
                padded with zeros before performing the extraction. This
                object follows the ManualOrAutomatic behavior.
                ''',
                'ciirasnpamask',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRASNPAPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                A fixed SNPA prefix for use when the ciiRAMapType is
                extractDSP. The SNPA Address to use is formed by
                concatenating the fixed SNPA prefix with a variable SNPA
                part that is extracted from the effective destination
                address. For Reachable Address prefixes in which the
                entire SNPA is embedded in the DSP the SNPA Prefix shall
                be null. This object follows the ManualOrAutomatic
                behavior.
                ''',
                'ciirasnpaprefix',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRAType', REFERENCE_ENUM_CLASS, 'CiiRAType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRATable.CiiRAEntry.CiiRAType_Enum', 
                [], [], 
                '''                The type of Reachable address. Those of type
                manual are created by the network manager. Those
                of type automatic are created through propagation
                of routing information from another routing
                protocol (eg. IDRP). 
                ''',
                'ciiratype',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRAEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRATable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRATable',
            False, 
            [
            _MetaInfoClassMember('ciiRAEntry', REFERENCE_LIST, 'CiiRAEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRATable.CiiRAEntry', 
                [], [], 
                '''                Each entry defines a Reachable Address to a NSAP or
                Address Prefix.
                ''',
                'ciiraentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRATable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRedistributeAddrTable.CiiRedistributeAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRedistributeAddrTable.CiiRedistributeAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiRedistributeAddrAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP Address value for this summary address.
                This object follows the index behavior.
                ''',
                'ciiredistributeaddraddress',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRedistributeAddrPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                The Length of the IP NetMask for this summary address.
                ''',
                'ciiredistributeaddrprefixlen',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRedistributeAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Type of IP address for this summary address.
                This object follows the index behavior.
                ''',
                'ciiredistributeaddrtype',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRedistributeAddrExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The existence state of this summary address. This object
                follows the row status behavior.
                ''',
                'ciiredistributeaddrexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRedistributeAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRedistributeAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRedistributeAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiRedistributeAddrEntry', REFERENCE_LIST, 'CiiRedistributeAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRedistributeAddrTable.CiiRedistributeAddrEntry', 
                [], [], 
                '''                Each entry contains one IP summary address to
                manage leaking L2 addresses into L1.
                ''',
                'ciiredistributeaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRedistributeAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRouterTable.CiiRouterEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRouterTable.CiiRouterEntry',
            False, 
            [
            _MetaInfoClassMember('ciiRouterLevel', REFERENCE_ENUM_CLASS, 'CiiISLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiISLevel_Enum', 
                [], [], 
                '''                The level of this Intermediate System.
                ''',
                'ciirouterlevel',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRouterSysID', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The System ID of the Router Peer.
                ''',
                'ciiroutersysid',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiRouterHostName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The hostname listed in LSP, or zero-length string if none.
                ''',
                'ciirouterhostname',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRouterID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Router ID of the Peer found in LSP, or zero if none.
                ''',
                'ciirouterid',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRouterEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiRouterTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiRouterTable',
            False, 
            [
            _MetaInfoClassMember('ciiRouterEntry', REFERENCE_LIST, 'CiiRouterEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRouterTable.CiiRouterEntry', 
                [], [], 
                '''                Each entry tracks information about one peer at
                one level.
                ''',
                'ciirouterentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiRouterTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSummAddrTable.CiiSummAddrEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSummAddrTable.CiiSummAddrEntry',
            False, 
            [
            _MetaInfoClassMember('ciiSummAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, None), (16, None)], [], 
                '''                The IP Address value for this summary address.
                This object follows the index behavior.
                ''',
                'ciisummaddress',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSummAddressType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                The Type of IP address for this summary address.
                This object follows the index behavior.
                ''',
                'ciisummaddresstype',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSummAddrPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [(0, 128)], [], 
                '''                The Length of the IP NetMask for this summary address.
                ''',
                'ciisummaddrprefixlen',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSummAddrExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The existence state of this summary address. This object
                follows the row status behavior.
                ''',
                'ciisummaddrexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSummAddrFullMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The wide metric value to announce this summary
                address with in LSPs generated by this system.
                ''',
                'ciisummaddrfullmetric',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSummAddrMetric', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                The metric value to announce this summary
                address with in LSPs generated by this system.
                ''',
                'ciisummaddrmetric',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSummAddrEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSummAddrTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSummAddrTable',
            False, 
            [
            _MetaInfoClassMember('ciiSummAddrEntry', REFERENCE_LIST, 'CiiSummAddrEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSummAddrTable.CiiSummAddrEntry', 
                [], [], 
                '''                Each entry contains one IP summary address.
                ''',
                'ciisummaddrentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSummAddrTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry.CiiSysLevelIndex_Enum' : _MetaInfoEnum('CiiSysLevelIndex_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1IS':'LEVEL1IS',
            'level2IS':'LEVEL2IS',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry',
            False, 
            [
            _MetaInfoClassMember('ciiSysLevelIndex', REFERENCE_ENUM_CLASS, 'CiiSysLevelIndex_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry.CiiSysLevelIndex_Enum', 
                [], [], 
                '''                The level that this entry describes.
                ''',
                'ciisyslevelindex',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSysLevelMetricStyle', REFERENCE_ENUM_CLASS, 'CiiMetricStyle_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiMetricStyle_Enum', 
                [], [], 
                '''                Which style of Metric do we generate in our LSPs
                at this level? This object follows the
                replaceOnlyWhileDisabled behavior.
                ''',
                'ciisyslevelmetricstyle',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelMinLSPGenInt', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Minimum interval, in seconds, between successive
                generation of LSPs with the same LSPID at this level
                by this Intermediate System.  This object
                follows the resettingTimer behavior.
                ''',
                'ciisyslevelminlspgenint',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelOrigLSPBuffSize', ATTRIBUTE, 'int' , None, None, 
                [(512, 16000)], [], 
                '''                The maximum size of LSPs and SNPs originated by
                this Intermediate System at this level.
                This object follows the replaceOnlyWhileDisabled
                behavior.
                ''',
                'ciisysleveloriglspbuffsize',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelOverloadState', REFERENCE_ENUM_CLASS, 'CiiLevelState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiLevelState_Enum', 
                [], [], 
                '''                The state of the database at this level.
                The value 'off' indicates that IS-IS is not active at
                this level.
                The value 'on' indicates that IS-IS is active at this
                level, and not overloaded.
                The value 'waiting' indicates a database that is low on
                an essential resource, such as memory.
                The administrator may force the state to 'overloaded'
                by setting the object ciiSysLevelSetOverload.
                If the state is 'waiting' or 'overloaded', we originate
                LSPs with the Overload bit set.
                ''',
                'ciisysleveloverloadstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelSetOverload', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Administratively set the overload bit for the level.
                The overload bit will continue to be set if the
                implementation runs out of memory, independent of
                this variable
                ''',
                'ciisyslevelsetoverload',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelSetOverloadUntil', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If set, the overload bit should be set, and cleared
                after sysUpTime exceeds this value.
                ''',
                'ciisyslevelsetoverloaduntil',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelSPFConsiders', REFERENCE_ENUM_CLASS, 'CiiMetricStyle_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiMetricStyle_Enum', 
                [], [], 
                '''                Which style of Metric do we consider in our
                SPF computation at this level?
                ''',
                'ciisyslevelspfconsiders',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelTEEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do we do Traffic Engineering at this level?
                ''',
                'ciisyslevelteenabled',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSysLevelEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSysLevelTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSysLevelTable',
            False, 
            [
            _MetaInfoClassMember('ciiSysLevelEntry', REFERENCE_LIST, 'CiiSysLevelEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry', 
                [], [], 
                '''                Describe variables defined for Area or Domain.
                ''',
                'ciisyslevelentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSysLevelTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSysObject.CiiSysType_Enum' : _MetaInfoEnum('CiiSysType_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1IS':'LEVEL1IS',
            'level2IS':'LEVEL2IS',
            'level1L2IS':'LEVEL1L2IS',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiSysObject.CiiSysVersion_Enum' : _MetaInfoEnum('CiiSysVersion_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'unknown':'UNKNOWN',
            'one':'ONE',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiSysObject' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSysObject',
            False, 
            [
            _MetaInfoClassMember('ciiSysAdminState', REFERENCE_ENUM_CLASS, 'CiiAdminState_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiAdminState_Enum', 
                [], [], 
                '''                The administrative state of this Intermediate
                System.  Setting this object to the value 'on'
                when its current value is 'off' enables
                the Intermediate System.
                ''',
                'ciisysadminstate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysID', ATTRIBUTE, 'str' , None, None, 
                [(6, None)], [], 
                '''                The ID for this Intermediate System.
                This value is appended to each of the
                area addresses to form the Network Entity Titles.
                The derivation of a value for this object is
                implementation-specific.  Some implementations may
                automatically assign values and not permit an
                SNMP write, while others may require the value
                to be set manually.
                ''',
                'ciisysid',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysL2toL1Leaking', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, allow the router to leak L2 routes into L1.
                ''',
                'ciisysl2tol1leaking',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysMaxAge', ATTRIBUTE, 'int' , None, None, 
                [(350, 65535)], [], 
                '''                Value to place in RemainingLifeTime field of
                the LSPs we generate.
                This should be at least 300 seconds greater than
                ciiSysMaxLSPGenInt.
                ''',
                'ciisysmaxage',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysMaxLSPGenInt', ATTRIBUTE, 'int' , None, None, 
                [(1, 65235)], [], 
                '''                Maximum interval, in seconds, between generated LSPs
                by this Intermediate System. This object follows
                the resettingTimer behavior.  The value must be
                greater than any value configured for
                ciiSysLevelMinLSPGenInt, and should be at least 300
                seconds less than ciiSysMaxAge.
                ''',
                'ciisysmaxlspgenint',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysMaxPathSplits', ATTRIBUTE, 'int' , None, None, 
                [(1, 32)], [], 
                '''                Maximum number of paths with equal routing metric value
                which it is permitted to split between. This object
                follows the replaceOnlyWhileDisabled behavior.
                ''',
                'ciisysmaxpathsplits',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysPollESHelloRate', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value, in seconds, to be used for the suggested ES
                configuration timer in ISH PDUs when soliciting the ES
                configuration.
                ''',
                'ciisyspolleshellorate',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysReceiveLSPBufferSize', ATTRIBUTE, 'int' , None, None, 
                [(1492, 16000)], [], 
                '''                Size of the largest Buffer we are designed or
                configured to store.  This should be at least
                as big as the maximum ciiSysLevelOrigLSPBuffSize
                supported by the system.
                
                If resources allow, we will store and flood LSPs
                larger than ciiSysReceiveLSPBufferSize, as this
                can help avoid problems in networks with different
                values for ciiSysLevelOrigLSPBuffSize.
                ''',
                'ciisysreceivelspbuffersize',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysType', REFERENCE_ENUM_CLASS, 'CiiSysType_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysObject.CiiSysType_Enum', 
                [], [], 
                '''                At which levels is the Intermediate System
                running? This object follows the
                replaceOnlyWhileDisabled behavior.
                ''',
                'ciisystype',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysVersion', REFERENCE_ENUM_CLASS, 'CiiSysVersion_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysObject.CiiSysVersion_Enum', 
                [], [], 
                '''                The version number of the IS-IS protocol that
                is implemented.
                ''',
                'ciisysversion',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysWaitTime', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Number of seconds to delay in 'waiting' state before
                entering 'on' state. This object follows the resettingTimer
                behavior.
                ''',
                'ciisyswaittime',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSysObject',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSysProtSuppTable.CiiSysProtSuppEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSysProtSuppTable.CiiSysProtSuppEntry',
            False, 
            [
            _MetaInfoClassMember('ciiSysProtSuppProtocol', REFERENCE_ENUM_CLASS, 'CiiSupportedProtocol_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CiiSupportedProtocol_Enum', 
                [], [], 
                '''                One supported protocol. This object follows the index
                behavior.
                ''',
                'ciisysprotsuppprotocol',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSysProtSuppExistState', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The state of the ciiSysProtSuppEntry. This object
                follows the RowStatus behavior.
                ''',
                'ciisysprotsuppexiststate',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSysProtSuppEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSysProtSuppTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSysProtSuppTable',
            False, 
            [
            _MetaInfoClassMember('ciiSysProtSuppEntry', REFERENCE_LIST, 'CiiSysProtSuppEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysProtSuppTable.CiiSysProtSuppEntry', 
                [], [], 
                '''                Each entry contains one protocol supported by
                this Intermediate System.
                ''',
                'ciisysprotsuppentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSysProtSuppTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry.CiiSysStatLevel_Enum' : _MetaInfoEnum('CiiSysStatLevel_Enum', 'ydk.models.ietf.CISCO_IETF_ISIS_MIB',
        {
            'level1IS':'LEVEL1IS',
            'level2IS':'LEVEL2IS',
        }, 'CISCO-IETF-ISIS-MIB', _yang_ns._namespaces['CISCO-IETF-ISIS-MIB']),
    'CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry',
            False, 
            [
            _MetaInfoClassMember('ciiSysStatLevel', REFERENCE_ENUM_CLASS, 'CiiSysStatLevel_Enum' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry.CiiSysStatLevel_Enum', 
                [], [], 
                '''                The level that this entry describes.
                ''',
                'ciisysstatlevel',
                'CISCO-IETF-ISIS-MIB', True),
            _MetaInfoClassMember('ciiSysStatAttmptToExMaxSeqNums', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times the IS has attempted to exceed the
                maximum sequence number.
                ''',
                'ciisysstatattmpttoexmaxseqnums',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatAuthFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of frames with authentication failures
                recognized by this Intermediate System.
                ''',
                'ciisysstatauthfails',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatAuthTypeFails', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of frames with authentication type mismatches
                recognized by this Intermediate System.
                ''',
                'ciisysstatauthtypefails',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatCorrLSPs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of corrupted in-memory LSP frames detected.
                
                LSPs received from the wire with a bad checksum
                are silently dropped and not counted.
                
                LSPs received from the wire with parse errors
                are counted by ciiSysStatLSPErrors.
                ''',
                'ciisysstatcorrlsps',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatIDFieldLenMismatches', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times a PDU is received with a different value
                for ID field length to that of the receiving system.
                ''',
                'ciisysstatidfieldlenmismatches',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatLSPDbaseOloads', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times the LSP database has become
                overloaded.
                ''',
                'ciisysstatlspdbaseoloads',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatLSPErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of LSP frames with errors we have received.
                ''',
                'ciisysstatlsperrors',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatManAddrDropFromAreas', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times a manual address has been dropped from
                the area.
                ''',
                'ciisysstatmanaddrdropfromareas',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatOwnLSPPurges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times a zero-aged copy of the system's own LSP
                is received from some other node.
                ''',
                'ciisysstatownlsppurges',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatPartChanges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Partition changes
                ''',
                'ciisysstatpartchanges',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatSeqNumSkips', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times a sequence number skip has occurred.
                ''',
                'ciisysstatseqnumskips',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysStatSPFRuns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of times we ran SPF at this level.
                ''',
                'ciisysstatspfruns',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSystemCounterEntry',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB.CiiSystemCounterTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB.CiiSystemCounterTable',
            False, 
            [
            _MetaInfoClassMember('ciiSystemCounterEntry', REFERENCE_LIST, 'CiiSystemCounterEntry' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry', 
                [], [], 
                '''                System-wide IS-IS counters.
                ''',
                'ciisystemcounterentry',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'ciiSystemCounterTable',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
    'CISCOIETFISISMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIETFISISMIB',
            False, 
            [
            _MetaInfoClassMember('ciiAreaAddrTable', REFERENCE_CLASS, 'CiiAreaAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiAreaAddrTable', 
                [], [], 
                '''                The union of the sets of area addresses reported in all
                Level 1 LSPs with fragment number zero generated by this
                Intermediate System, or received from other Intermediate
                Systems which are reachable via Level 1 routing.
                ''',
                'ciiareaaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCirc', REFERENCE_CLASS, 'CiiCirc' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCirc', 
                [], [], 
                '''                ''',
                'ciicirc',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircLevelTable', REFERENCE_CLASS, 'CiiCircLevelTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircLevelTable', 
                [], [], 
                '''                Level specific information about circuits used by IS-IS
                ''',
                'ciicircleveltable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircTable', REFERENCE_CLASS, 'CiiCircTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircTable', 
                [], [], 
                '''                The table of circuits used by this
                Intermediate System.
                ''',
                'ciicirctable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiCircuitCounterTable', REFERENCE_CLASS, 'CiiCircuitCounterTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiCircuitCounterTable', 
                [], [], 
                '''                Circuit specific counters for this
                Intermediate System.
                ''',
                'ciicircuitcountertable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiIPRATable', REFERENCE_CLASS, 'CiiIPRATable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiIPRATable', 
                [], [], 
                '''                The table of IP Reachable Addresses to networks,
                subnetworks or hosts either manually configured or
                learned from another protocol.
                ''',
                'ciiipratable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjAreaAddrTable', REFERENCE_CLASS, 'CiiISAdjAreaAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjAreaAddrTable', 
                [], [], 
                '''                This table contains the set of Area Addresses of
                neighboring Intermediate Systems as reported in received
                IIH PDUs.
                ''',
                'ciiisadjareaaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjIPAddrTable', REFERENCE_CLASS, 'CiiISAdjIPAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjIPAddrTable', 
                [], [], 
                '''                This table contains the set of IP Addresses of
                neighboring Intermediate Systems as reported in received
                IIH PDUs.
                ''',
                'ciiisadjipaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjProtSuppTable', REFERENCE_CLASS, 'CiiISAdjProtSuppTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjProtSuppTable', 
                [], [], 
                '''                This table contains the set of protocols supported by
                neighboring Intermediate Systems as reported in received
                IIH PDUs.
                ''',
                'ciiisadjprotsupptable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiISAdjTable', REFERENCE_CLASS, 'CiiISAdjTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiISAdjTable', 
                [], [], 
                '''                The table of adjacencies to Intermediate Systems.
                ''',
                'ciiisadjtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPSummaryTable', REFERENCE_CLASS, 'CiiLSPSummaryTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiLSPSummaryTable', 
                [], [], 
                '''                The table of LSP Headers.
                ''',
                'ciilspsummarytable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiLSPTLVTable', REFERENCE_CLASS, 'CiiLSPTLVTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiLSPTLVTable', 
                [], [], 
                '''                The contents of each LSP.
                ''',
                'ciilsptlvtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiManAreaAddrTable', REFERENCE_CLASS, 'CiiManAreaAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiManAreaAddrTable', 
                [], [], 
                '''                The set of manual area addresses configured on this
                Intermediate System.
                ''',
                'ciimanareaaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiPacketCounterTable', REFERENCE_CLASS, 'CiiPacketCounterTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiPacketCounterTable', 
                [], [], 
                '''                Information about IS-IS protocol traffic at one level
                on one circuit in one direction
                ''',
                'ciipacketcountertable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRATable', REFERENCE_CLASS, 'CiiRATable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRATable', 
                [], [], 
                '''                The table of Reachable Addresses to NSAPs or Address
                Prefixes.
                ''',
                'ciiratable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRedistributeAddrTable', REFERENCE_CLASS, 'CiiRedistributeAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRedistributeAddrTable', 
                [], [], 
                '''                This table provides criteria to decide if a route should
                be leaked from L2 to L1 when Domain Wide Prefix leaking is
                enabled.
                
                Addresses that match the summary mask in the table will
                be announced at L1 by routers when ciiSysL2toL1Leaking
                is enabled.  Routes that fall into the ranges specified
                are announced as is, without being summarized.  Routes
                that do not match a summary mask are not announced.
                ''',
                'ciiredistributeaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiRouterTable', REFERENCE_CLASS, 'CiiRouterTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiRouterTable', 
                [], [], 
                '''                The set of hostnames and router ID.
                ''',
                'ciiroutertable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSummAddrTable', REFERENCE_CLASS, 'CiiSummAddrTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSummAddrTable', 
                [], [], 
                '''                The set of IP summary addresses to use in forming
                summary TLVs originated by this Intermediate System.
                
                An administrator may use a summary address to combine
                and modify IP Reachability announcements.  If the
                Intermediate system can reach any subset of the summary
                address, the summary address will be announced instead,
                at the configured metric.
                ''',
                'ciisummaddrtable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysLevelTable', REFERENCE_CLASS, 'CiiSysLevelTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysLevelTable', 
                [], [], 
                '''                Level specific information about the System.
                ''',
                'ciisysleveltable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysObject', REFERENCE_CLASS, 'CiiSysObject' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysObject', 
                [], [], 
                '''                ''',
                'ciisysobject',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSysProtSuppTable', REFERENCE_CLASS, 'CiiSysProtSuppTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSysProtSuppTable', 
                [], [], 
                '''                This table contains the manually configured set of
                protocols supported by this Intermediate System.
                ''',
                'ciisysprotsupptable',
                'CISCO-IETF-ISIS-MIB', False),
            _MetaInfoClassMember('ciiSystemCounterTable', REFERENCE_CLASS, 'CiiSystemCounterTable' , 'ydk.models.ietf.CISCO_IETF_ISIS_MIB', 'CISCOIETFISISMIB.CiiSystemCounterTable', 
                [], [], 
                '''                System wide counters for this Intermediate System.
                ''',
                'ciisystemcountertable',
                'CISCO-IETF-ISIS-MIB', False),
            ],
            'CISCO-IETF-ISIS-MIB',
            'CISCO-IETF-ISIS-MIB',
            _yang_ns._namespaces['CISCO-IETF-ISIS-MIB'],
        'ydk.models.ietf.CISCO_IETF_ISIS_MIB'
        ),
    },
}
_meta_table['CISCOIETFISISMIB.CiiAreaAddrTable.CiiAreaAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiAreaAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircLevelTable.CiiCircLevelEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiCircLevelTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircTable.CiiCircEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiCircTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircuitCounterTable.CiiCircuitCounterEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiCircuitCounterTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiIPRATable.CiiIPRAEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiIPRATable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjAreaAddrTable.CiiISAdjAreaAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiISAdjAreaAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjIPAddrTable.CiiISAdjIPAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiISAdjIPAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjProtSuppTable.CiiISAdjProtSuppEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiISAdjProtSuppTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjTable.CiiISAdjEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiISAdjTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiLSPSummaryTable.CiiLSPSummaryEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiLSPSummaryTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiLSPTLVTable.CiiLSPTLVEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiLSPTLVTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiManAreaAddrTable.CiiManAreaAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiManAreaAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiPacketCounterTable.CiiPacketCounterEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiPacketCounterTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRATable.CiiRAEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiRATable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRedistributeAddrTable.CiiRedistributeAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiRedistributeAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRouterTable.CiiRouterEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiRouterTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSummAddrTable.CiiSummAddrEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiSummAddrTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSysLevelTable.CiiSysLevelEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiSysLevelTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSysProtSuppTable.CiiSysProtSuppEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiSysProtSuppTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSystemCounterTable.CiiSystemCounterEntry']['meta_info'].parent =_meta_table['CISCOIETFISISMIB.CiiSystemCounterTable']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiAreaAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCirc']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircLevelTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiCircuitCounterTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiIPRATable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjAreaAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjIPAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjProtSuppTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiISAdjTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiLSPSummaryTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiLSPTLVTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiManAreaAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiPacketCounterTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRATable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRedistributeAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiRouterTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSummAddrTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSysLevelTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSysObject']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSysProtSuppTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
_meta_table['CISCOIETFISISMIB.CiiSystemCounterTable']['meta_info'].parent =_meta_table['CISCOIETFISISMIB']['meta_info']
