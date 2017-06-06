


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Snmpv2Mib.System' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib.System',
            False, 
            [
            _MetaInfoClassMember('sysContact', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The textual identification of the contact person for
                this managed node, together with information on how
                to contact this person.  If no contact information is
                known, the value is the zero-length string.
                ''',
                'syscontact',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A textual description of the entity.  This value should
                include the full name and version identification of
                the system's hardware type, software operating-system,
                and networking software.
                ''',
                'sysdescr',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysLocation', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The physical location of this node (e.g., 'telephone
                closet, 3rd floor').  If the location is unknown, the
                value is the zero-length string.
                ''',
                'syslocation',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An administratively-assigned name for this managed
                node.  By convention, this is the node's fully-qualified
                domain name.  If the name is unknown, the value is
                the zero-length string.
                ''',
                'sysname',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysObjectID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The vendor's authoritative identification of the
                network management subsystem contained in the entity.
                This value is allocated within the SMI enterprises
                subtree (1.3.6.1.4.1) and provides an easy and
                unambiguous means for determining `what kind of box' is
                being managed.  For example, if vendor `Flintstones,
                Inc.' was assigned the subtree 1.3.6.1.4.1.424242,
                it could assign the identifier 1.3.6.1.4.1.424242.1.1
                to its `Fred Router'.
                ''',
                'sysobjectid',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysORLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the most recent
                change in state or value of any instance of sysORID.
                ''',
                'sysorlastchange',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysServices', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                A value which indicates the set of services that this
                entity may potentially offer.  The value is a sum.
                This sum initially takes the value zero. Then, for
                each layer, L, in the range 1 through 7, that this node
                performs transactions for, 2 raised to (L - 1) is added
                to the sum.  For example, a node which performs only
                routing functions would have a value of 4 (2^(3-1)).
                In contrast, a node which is a host offering application
                services would have a value of 72 (2^(4-1) + 2^(7-1)).
                Note that in the context of the Internet suite of
                protocols, values should be calculated accordingly:
                
                     layer      functionality
                       1        physical (e.g., repeaters)
                       2        datalink/subnetwork (e.g., bridges)
                       3        internet (e.g., supports the IP)
                       4        end-to-end  (e.g., supports the TCP)
                       7        applications (e.g., supports the SMTP)
                
                For systems including OSI protocols, layers 5 and 6
                may also be counted.
                ''',
                'sysservices',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time (in hundredths of a second) since the
                network management portion of the system was last
                re-initialized.
                ''',
                'sysuptime',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'system',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
    'Snmpv2Mib.Snmp.SnmpenableauthentrapsEnum' : _MetaInfoEnum('SnmpenableauthentrapsEnum', 'ydk.models.cisco_ios_xe.SNMPv2_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'SNMPv2-MIB', _yang_ns._namespaces['SNMPv2-MIB']),
    'Snmpv2Mib.Snmp' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib.Snmp',
            False, 
            [
            _MetaInfoClassMember('snmpEnableAuthenTraps', REFERENCE_ENUM_CLASS, 'SnmpenableauthentrapsEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.Snmp.SnmpenableauthentrapsEnum', 
                [], [], 
                '''                Indicates whether the SNMP entity is permitted to
                generate authenticationFailure traps.  The value of this
                object overrides any configuration information; as such,
                it provides a means whereby all authenticationFailure
                traps may be disabled.
                
                Note that it is strongly recommended that this object
                be stored in non-volatile memory so that it remains
                constant across re-initializations of the network
                management system.
                ''',
                'snmpenableauthentraps',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInASNParseErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of ASN.1 or BER errors encountered by
                the SNMP entity when decoding received SNMP messages.
                ''',
                'snmpinasnparseerrs',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInBadCommunityNames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of community-based SNMP messages (for
                example,  SNMPv1) delivered to the SNMP entity which
                used an SNMP community name not known to said entity.
                Also, implementations which authenticate community-based
                SNMP messages using check(s) in addition to matching
                the community name (for example, by also checking
                whether the message originated from a transport address
                allowed to use a specified community name) MAY include
                in this value the number of messages which failed the
                additional check(s).  It is strongly RECOMMENDED that
                the documentation for any security model which is used
                to authenticate community-based SNMP messages specify
                the precise conditions that contribute to this value.
                ''',
                'snmpinbadcommunitynames',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInBadCommunityUses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of community-based SNMP messages (for
                example, SNMPv1) delivered to the SNMP entity which
                represented an SNMP operation that was not allowed for
                the SNMP community named in the message.  The precise
                conditions under which this counter is incremented
                (if at all) depend on how the SNMP entity implements
                its access control mechanism and how its applications
                interact with that access control mechanism.  It is
                strongly RECOMMENDED that the documentation for any
                access control mechanism which is used to control access
                to and visibility of MIB instrumentation specify the
                precise conditions that contribute to this value.
                ''',
                'snmpinbadcommunityuses',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInBadValues', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field was
                `badValue'.
                ''',
                'snmpinbadvalues',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInBadVersions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP messages which were delivered
                to the SNMP entity and were for an unsupported SNMP
                version.
                ''',
                'snmpinbadversions',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInGenErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were delivered
                to the SNMP protocol entity and for which the value
                of the error-status field was `genErr'.
                ''',
                'snmpingenerrs',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInGetNexts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Next PDUs which have been
                accepted and processed by the SNMP protocol entity.
                ''',
                'snmpingetnexts',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInGetRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Request PDUs which
                have been accepted and processed by the SNMP
                protocol entity.
                ''',
                'snmpingetrequests',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInGetResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Response PDUs which
                have been accepted and processed by the SNMP protocol
                entity.
                ''',
                'snmpingetresponses',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInNoSuchNames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field was
                `noSuchName'.
                ''',
                'snmpinnosuchnames',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of messages delivered to the SNMP
                entity from the transport service.
                ''',
                'snmpinpkts',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInReadOnlys', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number valid SNMP PDUs which were delivered
                to the SNMP protocol entity and for which the value
                of the error-status field was `readOnly'.  It should
                be noted that it is a protocol error to generate an
                SNMP PDU which contains the value `readOnly' in the
                error-status field, as such this object is provided
                as a means of detecting incorrect implementations of
                the SNMP.
                ''',
                'snmpinreadonlys',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInSetRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Set-Request PDUs which
                have been accepted and processed by the SNMP protocol
                entity.
                ''',
                'snmpinsetrequests',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInTooBigs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were
                delivered to the SNMP protocol entity and for
                which the value of the error-status field was
                `tooBig'.
                ''',
                'snmpintoobigs',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInTotalReqVars', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MIB objects which have been
                retrieved successfully by the SNMP protocol entity
                as the result of receiving valid SNMP Get-Request
                and Get-Next PDUs.
                ''',
                'snmpintotalreqvars',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInTotalSetVars', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of MIB objects which have been
                altered successfully by the SNMP protocol entity as
                the result of receiving valid SNMP Set-Request PDUs.
                ''',
                'snmpintotalsetvars',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpInTraps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Trap PDUs which have been
                accepted and processed by the SNMP protocol entity.
                ''',
                'snmpintraps',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutBadValues', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were generated
                by the SNMP protocol entity and for which the value
                of the error-status field was `badValue'.
                ''',
                'snmpoutbadvalues',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutGenErrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were generated
                by the SNMP protocol entity and for which the value
                of the error-status field was `genErr'.
                ''',
                'snmpoutgenerrs',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutGetNexts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Next PDUs which have
                been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetnexts',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutGetRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Request PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetrequests',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutGetResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Get-Response PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutgetresponses',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutNoSuchNames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were generated
                by the SNMP protocol entity and for which the value
                of the error-status was `noSuchName'.
                ''',
                'snmpoutnosuchnames',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutPkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Messages which were
                passed from the SNMP protocol entity to the
                transport service.
                ''',
                'snmpoutpkts',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutSetRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Set-Request PDUs which
                have been generated by the SNMP protocol entity.
                ''',
                'snmpoutsetrequests',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutTooBigs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP PDUs which were generated
                by the SNMP protocol entity and for which the value
                of the error-status field was `tooBig.'
                ''',
                'snmpouttoobigs',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpOutTraps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of SNMP Trap PDUs which have
                been generated by the SNMP protocol entity.
                ''',
                'snmpouttraps',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpProxyDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Confirmed Class PDUs
                (such as GetRequest-PDUs, GetNextRequest-PDUs,
                GetBulkRequest-PDUs, SetRequest-PDUs, and
                InformRequest-PDUs) delivered to the SNMP entity which
                were silently dropped because the transmission of
                the (possibly translated) message to a proxy target
                failed in a manner (other than a time-out) such that
                no Response Class PDU (such as a Response-PDU) could
                be returned.
                ''',
                'snmpproxydrops',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpSilentDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Confirmed Class PDUs (such as
                GetRequest-PDUs, GetNextRequest-PDUs,
                GetBulkRequest-PDUs, SetRequest-PDUs, and
                InformRequest-PDUs) delivered to the SNMP entity which
                were silently dropped because the size of a reply
                containing an alternate Response Class PDU (such as a
                Response-PDU) with an empty variable-bindings field
                was greater than either a local constraint or the
                maximum message size associated with the originator of
                the request.
                ''',
                'snmpsilentdrops',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'snmp',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
    'Snmpv2Mib.Snmpset' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib.Snmpset',
            False, 
            [
            _MetaInfoClassMember('snmpSetSerialNo', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                An advisory lock used to allow several cooperating
                command generator applications to coordinate their
                use of the SNMP set operation.
                
                This object is used for coarse-grain coordination.
                To achieve fine-grain coordination, one or more similar
                objects might be defined within each MIB group, as
                appropriate.
                ''',
                'snmpsetserialno',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'snmpSet',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
    'Snmpv2Mib.Sysortable.Sysorentry' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib.Sysortable.Sysorentry',
            False, 
            [
            _MetaInfoClassMember('sysORIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The auxiliary variable used for identifying instances
                of the columnar objects in the sysORTable.
                ''',
                'sysorindex',
                'SNMPv2-MIB', True),
            _MetaInfoClassMember('sysORDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the capabilities identified
                by the corresponding instance of sysORID.
                ''',
                'sysordescr',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysORID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                An authoritative identification of a capabilities
                statement with respect to various MIB modules supported
                by the local SNMP application acting as a command
                responder.
                ''',
                'sysorid',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysORUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this conceptual
                row was last instantiated.
                ''',
                'sysoruptime',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'sysOREntry',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
    'Snmpv2Mib.Sysortable' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib.Sysortable',
            False, 
            [
            _MetaInfoClassMember('sysOREntry', REFERENCE_LIST, 'Sysorentry' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.Sysortable.Sysorentry', 
                [], [], 
                '''                An entry (conceptual row) in the sysORTable.
                ''',
                'sysorentry',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'sysORTable',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
    'Snmpv2Mib' : {
        'meta_info' : _MetaInfoClass('Snmpv2Mib',
            False, 
            [
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.Snmp', 
                [], [], 
                '''                ''',
                'snmp',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('snmpSet', REFERENCE_CLASS, 'Snmpset' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.Snmpset', 
                [], [], 
                '''                ''',
                'snmpset',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('sysORTable', REFERENCE_CLASS, 'Sysortable' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.Sysortable', 
                [], [], 
                '''                The (conceptual) table listing the capabilities of
                the local SNMP application acting as a command
                responder with respect to various MIB modules.
                SNMP entities having dynamically-configurable support
                of MIB modules will have a dynamically-varying number
                of conceptual rows.
                ''',
                'sysortable',
                'SNMPv2-MIB', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System' , 'ydk.models.cisco_ios_xe.SNMPv2_MIB', 'Snmpv2Mib.System', 
                [], [], 
                '''                ''',
                'system',
                'SNMPv2-MIB', False),
            ],
            'SNMPv2-MIB',
            'SNMPv2-MIB',
            _yang_ns._namespaces['SNMPv2-MIB'],
        'ydk.models.cisco_ios_xe.SNMPv2_MIB'
        ),
    },
}
_meta_table['Snmpv2Mib.Sysortable.Sysorentry']['meta_info'].parent =_meta_table['Snmpv2Mib.Sysortable']['meta_info']
_meta_table['Snmpv2Mib.System']['meta_info'].parent =_meta_table['Snmpv2Mib']['meta_info']
_meta_table['Snmpv2Mib.Snmp']['meta_info'].parent =_meta_table['Snmpv2Mib']['meta_info']
_meta_table['Snmpv2Mib.Snmpset']['meta_info'].parent =_meta_table['Snmpv2Mib']['meta_info']
_meta_table['Snmpv2Mib.Sysortable']['meta_info'].parent =_meta_table['Snmpv2Mib']['meta_info']
