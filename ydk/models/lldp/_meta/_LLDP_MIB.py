


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LldpPortIdSubtype_Enum' : _MetaInfoEnum('LldpPortIdSubtype_Enum', 'ydk.models.lldp.LLDP_MIB',
        {
            'interfaceAlias':'INTERFACEALIAS',
            'portComponent':'PORTCOMPONENT',
            'macAddress':'MACADDRESS',
            'networkAddress':'NETWORKADDRESS',
            'interfaceName':'INTERFACENAME',
            'agentCircuitId':'AGENTCIRCUITID',
            'local':'LOCAL',
        }, 'LLDP-MIB', _yang_ns._namespaces['LLDP-MIB']),
    'LldpChassisIdSubtype_Enum' : _MetaInfoEnum('LldpChassisIdSubtype_Enum', 'ydk.models.lldp.LLDP_MIB',
        {
            'chassisComponent':'CHASSISCOMPONENT',
            'interfaceAlias':'INTERFACEALIAS',
            'portComponent':'PORTCOMPONENT',
            'macAddress':'MACADDRESS',
            'networkAddress':'NETWORKADDRESS',
            'interfaceName':'INTERFACENAME',
            'local':'LOCAL',
        }, 'LLDP-MIB', _yang_ns._namespaces['LLDP-MIB']),
    'LldpManAddrIfSubtype_Enum' : _MetaInfoEnum('LldpManAddrIfSubtype_Enum', 'ydk.models.lldp.LLDP_MIB',
        {
            'unknown':'UNKNOWN',
            'ifIndex':'IFINDEX',
            'systemPortNumber':'SYSTEMPORTNUMBER',
        }, 'LLDP-MIB', _yang_ns._namespaces['LLDP-MIB']),
    'LLDPMIB.LldpConfiguration' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpConfiguration',
            False, 
            [
            _MetaInfoClassMember('lldpMessageTxHoldMultiplier', ATTRIBUTE, 'int' , None, None, 
                [(2, 10)], [], 
                '''                The time-to-live value expressed as a multiple of the
                lldpMessageTxInterval object.  The actual time-to-live value
                used in LLDP frames, transmitted on behalf of this LLDP agent,
                can be expressed by the following formula: TTL = min(65535,
                (lldpMessageTxInterval * lldpMessageTxHoldMultiplier)) For
                example, if the value of lldpMessageTxInterval is '30', and
                the value of lldpMessageTxHoldMultiplier is '4', then the
                value '120' is encoded in the TTL field in the LLDP header.
                
                The default value for lldpMessageTxHoldMultiplier object is 4.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldpmessagetxholdmultiplier',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpMessageTxInterval', ATTRIBUTE, 'int' , None, None, 
                [(5, 32768)], [], 
                '''                The interval at which LLDP frames are transmitted on
                behalf of this LLDP agent.
                
                The default value for lldpMessageTxInterval object is
                30 seconds.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldpmessagetxinterval',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpNotificationInterval', ATTRIBUTE, 'int' , None, None, 
                [(5, 3600)], [], 
                '''                This object controls the transmission of LLDP notifications.
                
                the agent must not generate more than one lldpRemTablesChange
                notification-event in the indicated period, where a
                'notification-event' is the transmission of a single
                notification PDU type to a list of notification destinations.
                If additional changes in lldpRemoteSystemsData object
                groups occur within the indicated throttling period,
                then these trap- events must be suppressed by the
                agent. An NMS should periodically check the value of
                lldpStatsRemTableLastChangeTime to detect any missed
                lldpRemTablesChange notification-events, e.g. due to
                throttling or transmission loss.
                
                If notification transmission is enabled for particular ports,
                the suggested default throttling period is 5 seconds.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldpnotificationinterval',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpReinitDelay', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                The lldpReinitDelay indicates the delay (in units of
                seconds) from when lldpPortConfigAdminStatus object of a
                particular port becomes 'disabled' until re-initialization
                will be attempted.
                
                The default value for lldpReintDelay object is two seconds.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldpreinitdelay',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpTxDelay', ATTRIBUTE, 'int' , None, None, 
                [(1, 8192)], [], 
                '''                The lldpTxDelay indicates the delay (in units
                of seconds) between successive LLDP frame transmissions 
                initiated by value/status changes in the LLDP local systems
                MIB.  The recommended value for the lldpTxDelay is set by the
                following  formula:
                
                   1 <= lldpTxDelay <= (0.25 * lldpMessageTxInterval)
                
                The default value for lldpTxDelay object is two seconds.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldptxdelay',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpConfiguration',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry',
            False, 
            [
            _MetaInfoClassMember('lldpLocManAddr', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                The string value used to identify the management address
                component associated with the local system.  The purpose of
                this address is to contact the management entity.
                ''',
                'lldplocmanaddr',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpLocManAddrSubtype', REFERENCE_ENUM_CLASS, 'AddressFamilyNumbers_Enum' , 'ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers_Enum', 
                [], [], 
                '''                The type of management address identifier encoding used in
                the associated 'lldpLocManagmentAddr' object.
                ''',
                'lldplocmanaddrsubtype',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpConfigManAddrPortsTxEnable', ATTRIBUTE, 'str' , None, None, 
                [(0, 512)], [], 
                '''                A set of ports that are identified by a PortList, in which
                each port is represented as a bit.  The corresponding local
                system management address instance will be transmitted on the
                member ports of the lldpManAddrPortsTxEnable.  
                
                The default value for lldpConfigManAddrPortsTxEnable object
                is empty binary string, which means no ports are specified
                for advertising indicated management address instance.
                ''',
                'lldpconfigmanaddrportstxenable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocManAddrIfId', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The integer value used to identify the interface number
                regarding the management address component associated with
                the local system.
                ''',
                'lldplocmanaddrifid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocManAddrIfSubtype', REFERENCE_ENUM_CLASS, 'LldpManAddrIfSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpManAddrIfSubtype_Enum', 
                [], [], 
                '''                The enumeration value that identifies the interface numbering
                method used for defining the interface number, associated
                with the local system.
                ''',
                'lldplocmanaddrifsubtype',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocManAddrLen', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The total length of the management address subtype and the
                management address fields in LLDPDUs transmitted by the
                local LLDP agent.
                
                The management address length field is needed so that the
                receiving systems that do not implement SNMP will not be
                required to implement an iana family numbers/address length
                equivalency table in order to decode the management adress.
                ''',
                'lldplocmanaddrlen',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocManAddrOID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The OID value used to identify the type of hardware component
                or protocol entity associated with the management address
                advertised by the local system agent.
                ''',
                'lldplocmanaddroid',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpLocManAddrEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpLocManAddrTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpLocManAddrTable',
            False, 
            [
            _MetaInfoClassMember('lldpLocManAddrEntry', REFERENCE_LIST, 'LldpLocManAddrEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry', 
                [], [], 
                '''                Management address information about a particular chassis
                component.  There may be multiple management addresses
                configured on the system identified by a particular
                lldpLocChassisId.  Each management address should have
                distinct 'management address type' (lldpLocManAddrSubtype) and
                'management address' (lldpLocManAddr.)
                
                Entries may be created and deleted in this table by the
                agent.
                ''',
                'lldplocmanaddrentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpLocManAddrTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpLocPortTable.LldpLocPortEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpLocPortTable.LldpLocPortEntry',
            False, 
            [
            _MetaInfoClassMember('lldpLocPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The index value used to identify the port component
                (contained in the local chassis with the LLDP agent)
                associated with this entry.
                
                The value of this object is used as a port index to the
                lldpLocPortTable.
                ''',
                'lldplocportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpLocPortDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the 802 LAN station's port
                description associated with the local system.  If the local
                agent supports IETF RFC 2863, lldpLocPortDesc object should
                have the same value of ifDescr object.
                ''',
                'lldplocportdesc',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocPortId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The string value used to identify the port component
                associated with a given port in the local system.
                ''',
                'lldplocportid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocPortIdSubtype', REFERENCE_ENUM_CLASS, 'LldpPortIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpPortIdSubtype_Enum', 
                [], [], 
                '''                The type of port identifier encoding used in the associated
                'lldpLocPortId' object.
                ''',
                'lldplocportidsubtype',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpLocPortEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpLocPortTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpLocPortTable',
            False, 
            [
            _MetaInfoClassMember('lldpLocPortEntry', REFERENCE_LIST, 'LldpLocPortEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpLocPortTable.LldpLocPortEntry', 
                [], [], 
                '''                Information about a particular port component.
                
                Entries may be created and deleted in this table by the
                agent.
                ''',
                'lldplocportentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpLocPortTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpLocalSystemData' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpLocalSystemData',
            False, 
            [
            _MetaInfoClassMember('lldpLocChassisId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The string value used to identify the chassis component
                associated with the local system.
                ''',
                'lldplocchassisid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocChassisIdSubtype', REFERENCE_ENUM_CLASS, 'LldpChassisIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpChassisIdSubtype_Enum', 
                [], [], 
                '''                The type of encoding used to identify the chassis
                associated with the local system.
                ''',
                'lldplocchassisidsubtype',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocSysCapEnabled', REFERENCE_BITS, 'LldpSystemCapabilitiesMap_Bits' , 'ydk.models.lldp.LLDP_MIB', 'LldpSystemCapabilitiesMap_Bits', 
                [], [], 
                '''                The bitmap value used to identify which system capabilities
                are enabled on the local system.
                ''',
                'lldplocsyscapenabled',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocSysCapSupported', REFERENCE_BITS, 'LldpSystemCapabilitiesMap_Bits' , 'ydk.models.lldp.LLDP_MIB', 'LldpSystemCapabilitiesMap_Bits', 
                [], [], 
                '''                The bitmap value used to identify which system capabilities
                are supported on the local system.
                ''',
                'lldplocsyscapsupported',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocSysDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the system description
                of the local system.  If the local agent supports IETF RFC 3418,
                lldpLocSysDesc object should have the same value of sysDesc
                object.
                ''',
                'lldplocsysdesc',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocSysName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the system name of the
                local system.  If the local agent supports IETF RFC 3418,
                lldpLocSysName object should have the same value of sysName
                object.
                ''',
                'lldplocsysname',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpLocalSystemData',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus_Enum' : _MetaInfoEnum('LldpPortConfigAdminStatus_Enum', 'ydk.models.lldp.LLDP_MIB',
        {
            'txOnly':'TXONLY',
            'rxOnly':'RXONLY',
            'txAndRx':'TXANDRX',
            'disabled':'DISABLED',
        }, 'LLDP-MIB', _yang_ns._namespaces['LLDP-MIB']),
    'LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry',
            False, 
            [
            _MetaInfoClassMember('lldpPortConfigPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The index value used to identify the port component
                (contained in the local chassis with the LLDP agent)
                associated with this entry.
                
                The value of this object is used as a port index to the
                lldpPortConfigTable.
                ''',
                'lldpportconfigportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpPortConfigAdminStatus', REFERENCE_ENUM_CLASS, 'LldpPortConfigAdminStatus_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus_Enum', 
                [], [], 
                '''                The administratively desired status of the local LLDP agent.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'txOnly(1)', then LLDP agent will transmit LLDP
                frames on this port and it will not store any information
                about the remote systems connected.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'rxOnly(2)', then the LLDP agent will receive,
                but it will not transmit LLDP frames on this port.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'txAndRx(3)', then the LLDP agent will transmit
                and receive LLDP frames on this port.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'disabled(4)', then LLDP agent will not transmit or
                receive LLDP frames on this port.  If there is remote systems
                information which is received on this port and stored in
                other tables, before the port's lldpPortConfigAdminStatus
                becomes disabled, then the information will naturally age out.
                ''',
                'lldpportconfigadminstatus',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpPortConfigNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The lldpPortConfigNotificationEnable controls, on a per
                port basis,  whether or not notifications from the agent
                are enabled. The value true(1) means that notifications are
                enabled; the value false(2) means that they are not.
                ''',
                'lldpportconfignotificationenable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpPortConfigTLVsTxEnable', REFERENCE_BITS, 'LldpPortConfigTLVsTxEnable_Bits' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigTLVsTxEnable_Bits', 
                [], [], 
                '''                The lldpPortConfigTLVsTxEnable, defined as a bitmap,
                includes the basic set of LLDP TLVs whose transmission is
                allowed on the local LLDP agent by the network management.
                Each bit in the bitmap corresponds to a TLV type associated
                with a specific optional TLV.
                
                It should be noted that the organizationally-specific TLVs
                are excluded from the lldpTLVsTxEnable bitmap.
                
                LLDP Organization Specific Information Extension MIBs should
                have similar configuration object to control transmission
                of their organizationally defined TLVs.
                
                The bit 'portDesc(0)' indicates that LLDP agent should
                transmit 'Port Description TLV'.
                
                The bit 'sysName(1)' indicates that LLDP agent should transmit
                'System Name TLV'.
                
                The bit 'sysDesc(2)' indicates that LLDP agent should transmit
                'System Description TLV'.
                
                The bit 'sysCap(3)' indicates that LLDP agent should transmit
                'System Capabilities TLV'.
                
                There is no bit reserved for the management address TLV type
                since transmission of management address TLVs are controlled
                by another object, lldpConfigManAddrTable.
                
                The default value for lldpPortConfigTLVsTxEnable object is
                empty set, which means no enumerated values are set.
                
                The value of this object must be restored from non-volatile
                storage after a re-initialization of the management system.
                ''',
                'lldpportconfigtlvstxenable',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpPortConfigEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpPortConfigTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpPortConfigTable',
            False, 
            [
            _MetaInfoClassMember('lldpPortConfigEntry', REFERENCE_LIST, 'LldpPortConfigEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry', 
                [], [], 
                '''                LLDP configuration information for a particular port.
                This configuration parameter controls the transmission and
                the reception of LLDP frames on those ports whose rows are
                created in this table.
                ''',
                'lldpportconfigentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpPortConfigTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry',
            False, 
            [
            _MetaInfoClassMember('lldpRemIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'lldpremindex',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemLocalPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                ''',
                'lldpremlocalportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemManAddr', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                The string value used to identify the management address
                component associated with the remote system.  The purpose
                of this address is to contact the management entity.
                ''',
                'lldpremmanaddr',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemManAddrSubtype', REFERENCE_ENUM_CLASS, 'AddressFamilyNumbers_Enum' , 'ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers_Enum', 
                [], [], 
                '''                The type of management address identifier encoding used in
                the associated 'lldpRemManagmentAddr' object.
                ''',
                'lldpremmanaddrsubtype',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'lldpremtimemark',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemManAddrIfId', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The integer value used to identify the interface number
                regarding the management address component associated with
                the remote system.
                ''',
                'lldpremmanaddrifid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemManAddrIfSubtype', REFERENCE_ENUM_CLASS, 'LldpManAddrIfSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpManAddrIfSubtype_Enum', 
                [], [], 
                '''                The enumeration value that identifies the interface numbering
                method used for defining the interface number, associated
                with the remote system.
                ''',
                'lldpremmanaddrifsubtype',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemManAddrOID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The OID value used to identify the type of hardware component
                or protocol entity associated with the management address
                advertised by the remote system agent.
                ''',
                'lldpremmanaddroid',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemManAddrEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemManAddrTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemManAddrTable',
            False, 
            [
            _MetaInfoClassMember('lldpRemManAddrEntry', REFERENCE_LIST, 'LldpRemManAddrEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry', 
                [], [], 
                '''                Management address information about a particular chassis
                component.  There may be multiple management addresses
                configured on the remote system identified by a particular
                lldpRemIndex whose information is received on
                lldpRemLocalPortNum of the local system.  Each management
                address should have distinct 'management address
                type' (lldpRemManAddrSubtype) and 'management address'
                (lldpRemManAddr.)
                
                Entries may be created and deleted in this table by the
                agent.
                ''',
                'lldpremmanaddrentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemManAddrTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry',
            False, 
            [
            _MetaInfoClassMember('lldpRemIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'lldpremindex',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemLocalPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                ''',
                'lldpremlocalportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemOrgDefInfoIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object represents an arbitrary local integer value
                used by this agent to identify a particular unrecognized
                organizationally defined information instance, unique only
                for the lldpRemOrgDefInfoOUI and lldpRemOrgDefInfoSubtype
                from the same remote system.
                
                An agent is encouraged to assign monotonically increasing
                index values to new entries, starting with one, after each
                reboot.  It is considered unlikely that the
                lldpRemOrgDefInfoIndex will wrap between reboots.
                ''',
                'lldpremorgdefinfoindex',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemOrgDefInfoOUI', ATTRIBUTE, 'str' , None, None, 
                [(3, None)], [], 
                '''                The Organizationally Unique Identifier (OUI), as defined
                in IEEE std 802-2001, is a 24 bit (three octets) globally
                unique assigned number referenced by various standards,
                of the information received from the remote system.
                ''',
                'lldpremorgdefinfooui',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemOrgDefInfoSubtype', ATTRIBUTE, 'int' , None, None, 
                [(1, 255)], [], 
                '''                The integer value used to identify the subtype of the
                organizationally defined information received from the
                remote system.
                
                The subtype value is required to identify different instances
                of organizationally defined information that could not be
                retrieved without a unique identifier that indicates the
                particular type of information contained in the information
                string.
                ''',
                'lldpremorgdefinfosubtype',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'lldpremtimemark',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemOrgDefInfo', ATTRIBUTE, 'str' , None, None, 
                [(0, 507)], [], 
                '''                The string value used to identify the organizationally
                defined information of the remote system.  The encoding for
                this object should be as defined for SnmpAdminString TC.
                ''',
                'lldpremorgdefinfo',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemOrgDefInfoEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemOrgDefInfoTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemOrgDefInfoTable',
            False, 
            [
            _MetaInfoClassMember('lldpRemOrgDefInfoEntry', REFERENCE_LIST, 'LldpRemOrgDefInfoEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry', 
                [], [], 
                '''                Information about the unrecognized organizationally
                defined information advertised by the remote system.
                The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex,
                lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and
                lldpRemOrgDefInfoIndex are indexes to this table.  If there is
                an lldpRemOrgDefInfoEntry associated with a particular remote
                system identified by the lldpRemLocalPortNum and lldpRemIndex,
                there must be an lldpRemEntry associated with the same
                instance (i.e, using same indexes.)  When the lldpRemEntry
                for the same index is removed from the lldpRemTable, the
                associated lldpRemOrgDefInfoEntry should be removed from
                the lldpRemOrgDefInfoTable.
                
                Entries may be created and deleted in this table by the
                agent.
                ''',
                'lldpremorgdefinfoentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemOrgDefInfoTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemTable.LldpRemEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemTable.LldpRemEntry',
            False, 
            [
            _MetaInfoClassMember('lldpRemIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                This object represents an arbitrary local integer value used
                by this agent to identify a particular connection instance,
                unique only for the indicated remote system.
                
                An agent is encouraged to assign monotonically increasing
                index values to new entries, starting with one, after each
                reboot.  It is considered unlikely that the lldpRemIndex
                will wrap between reboots.
                ''',
                'lldpremindex',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemLocalPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The index value used to identify the port component
                (contained in the local chassis with the LLDP agent)
                associated with this entry.  The lldpRemLocalPortNum
                identifies the port on which the remote system information
                is received.
                
                The value of this object is used as a port index to the
                lldpRemTable.
                ''',
                'lldpremlocalportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention in IETF RFC 2021 and 
                http://www.ietf.org/IESG/Implementations/RFC2021-Implementation.txt
                to see how TimeFilter works.
                ''',
                'lldpremtimemark',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemChassisId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The string value used to identify the chassis component
                associated with the remote system.
                ''',
                'lldpremchassisid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemChassisIdSubtype', REFERENCE_ENUM_CLASS, 'LldpChassisIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpChassisIdSubtype_Enum', 
                [], [], 
                '''                The type of encoding used to identify the chassis associated
                with the remote system.
                ''',
                'lldpremchassisidsubtype',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemPortDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the description of
                the given port associated with the remote system.
                ''',
                'lldpremportdesc',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemPortId', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The string value used to identify the port component
                associated with the remote system.
                ''',
                'lldpremportid',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemPortIdSubtype', REFERENCE_ENUM_CLASS, 'LldpPortIdSubtype_Enum' , 'ydk.models.lldp.LLDP_MIB', 'LldpPortIdSubtype_Enum', 
                [], [], 
                '''                The type of port identifier encoding used in the associated
                'lldpRemPortId' object.
                ''',
                'lldpremportidsubtype',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemSysCapEnabled', REFERENCE_BITS, 'LldpSystemCapabilitiesMap_Bits' , 'ydk.models.lldp.LLDP_MIB', 'LldpSystemCapabilitiesMap_Bits', 
                [], [], 
                '''                The bitmap value used to identify which system capabilities
                are enabled on the remote system.
                ''',
                'lldpremsyscapenabled',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemSysCapSupported', REFERENCE_BITS, 'LldpSystemCapabilitiesMap_Bits' , 'ydk.models.lldp.LLDP_MIB', 'LldpSystemCapabilitiesMap_Bits', 
                [], [], 
                '''                The bitmap value used to identify which system capabilities
                are supported on the remote system.
                ''',
                'lldpremsyscapsupported',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemSysDesc', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the system description
                of the remote system.
                ''',
                'lldpremsysdesc',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemSysName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The string value used to identify the system name of the
                remote system.
                ''',
                'lldpremsysname',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemTable',
            False, 
            [
            _MetaInfoClassMember('lldpRemEntry', REFERENCE_LIST, 'LldpRemEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemTable.LldpRemEntry', 
                [], [], 
                '''                Information about a particular physical network connection.
                Entries may be created and deleted in this table by the agent,
                if a physical topology discovery process is active.
                ''',
                'lldprementry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry',
            False, 
            [
            _MetaInfoClassMember('lldpRemIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'lldpremindex',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemLocalPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                ''',
                'lldpremlocalportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'lldpremtimemark',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemUnknownTLVType', ATTRIBUTE, 'int' , None, None, 
                [(9, 126)], [], 
                '''                This object represents the value extracted from the type
                field of the TLV.
                ''',
                'lldpremunknowntlvtype',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpRemUnknownTLVInfo', ATTRIBUTE, 'str' , None, None, 
                [(0, 511)], [], 
                '''                This object represents the value extracted from the value
                field of the TLV.
                ''',
                'lldpremunknowntlvinfo',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemUnknownTLVEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpRemUnknownTLVTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpRemUnknownTLVTable',
            False, 
            [
            _MetaInfoClassMember('lldpRemUnknownTLVEntry', REFERENCE_LIST, 'LldpRemUnknownTLVEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry', 
                [], [], 
                '''                Information about an unrecognized TLV received from a
                physical network connection.  Entries may be created and
                deleted in this table by the agent, if a physical topology
                discovery process is active.
                ''',
                'lldpremunknowntlventry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpRemUnknownTLVTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpStatistics' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpStatistics',
            False, 
            [
            _MetaInfoClassMember('lldpStatsRemTablesAgeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the complete set of information
                advertised by a particular MSAP has been deleted from tables
                contained in lldpRemoteSystemsData and lldpExtensions objects
                because the information timeliness interval has expired.
                
                This counter should be incremented only once when the complete
                set of information is completely invalidated (aged out)
                from all related tables.  Partial aging, similar to deletion
                case, is not allowed, and thus, should not change the value
                of this counter.
                ''',
                'lldpstatsremtablesageouts',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRemTablesDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the complete set of information
                advertised by a particular MSAP has been deleted from
                tables contained in lldpRemoteSystemsData and lldpExtensions
                objects.
                
                This counter should be incremented only once when the
                complete set of information is completely deleted from all
                related tables.  Partial deletions, such as deletion of
                rows associated with a particular MSAP from some tables,
                but not from all tables are not allowed, thus should not
                change the value of this counter.
                ''',
                'lldpstatsremtablesdeletes',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRemTablesDrops', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the complete set of information
                advertised by a particular MSAP could not be entered into
                tables contained in lldpRemoteSystemsData and lldpExtensions
                objects because of insufficient resources.
                ''',
                'lldpstatsremtablesdrops',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRemTablesInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the complete set of information
                advertised by a particular MSAP has been inserted into tables
                contained in lldpRemoteSystemsData and lldpExtensions objects.
                
                The complete set of information received from a particular
                MSAP should be inserted into related tables.  If partial
                information cannot be inserted for a reason such as lack
                of resources, all of the complete set of information should
                be removed.
                
                This counter should be incremented only once after the
                complete set of information is successfully recorded
                in all related tables.  Any failures during inserting
                information set which result in deletion of previously
                inserted information should not trigger any changes in
                lldpStatsRemTablesInserts since the insert is not completed
                yet or or in lldpStatsRemTablesDeletes, since the deletion
                would only be a partial deletion. If the failure was the
                result of lack of resources, the lldpStatsRemTablesDrops
                counter should be incremented once.
                ''',
                'lldpstatsremtablesinserts',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRemTablesLastChangeTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime object (defined in IETF RFC 3418)
                at the time an entry is created, modified, or deleted in the
                in tables associated with the lldpRemoteSystemsData objects
                and all LLDP extension objects associated with remote systems.
                
                An NMS can use this object to reduce polling of the
                lldpRemoteSystemsData objects.
                ''',
                'lldpstatsremtableslastchangetime',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpStatistics',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry',
            False, 
            [
            _MetaInfoClassMember('lldpStatsRxPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The index value used to identify the port component
                (contained in the local chassis with the LLDP agent)
                associated with this entry.
                
                The value of this object is used as a port index to the
                lldpStatsTable.
                ''',
                'lldpstatsrxportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpStatsRxPortAgeoutsTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The counter that represents the number of age-outs that
                occurred on a given port.  An age-out is the number of
                times the complete set of information advertised by a
                particular MSAP has been deleted from tables contained in
                lldpRemoteSystemsData and lldpExtensions objects because
                the information timeliness interval has expired.
                
                This counter is similar to lldpStatsRemTablesAgeouts, except
                that the counter is on a per port basis.  This enables NMS to
                poll tables associated with the lldpRemoteSystemsData objects
                and all LLDP extension objects associated with remote systems
                on the indicated port only.
                
                This counter should be set to zero during agent initialization
                and its value should not be saved in non-volatile storage.
                When a port's admin status changes from 'disabled' to
                'rxOnly', 'txOnly' or 'txAndRx', the counter associated with
                the same port should reset to 0.  The agent should also flush
                all remote system information associated with the same port.
                
                This counter should be incremented only once when the
                complete set of information is invalidated (aged out) from
                all related tables on a particular port.  Partial aging
                is not allowed, and thus, should not change the value of
                this counter.
                ''',
                'lldpstatsrxportageoutstotal',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortFramesDiscardedTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of LLDP frames received by this LLDP agent on
                the indicated port, and then discarded for any reason.
                This counter can provide an indication that LLDP header
                formating problems may exist with the local LLDP agent in
                the sending system or that LLDPDU validation problems may
                exist with the local LLDP agent in the receiving system.
                ''',
                'lldpstatsrxportframesdiscardedtotal',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortFramesErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of invalid LLDP frames received by this LLDP
                agent on the indicated port, while this LLDP agent is enabled.
                ''',
                'lldpstatsrxportframeserrors',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortFramesTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid LLDP frames received by this LLDP agent
                on the indicated port, while this LLDP agent is enabled.
                ''',
                'lldpstatsrxportframestotal',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortTLVsDiscardedTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of LLDP TLVs discarded for any reason by this LLDP
                agent on the indicated port.
                ''',
                'lldpstatsrxporttlvsdiscardedtotal',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortTLVsUnrecognizedTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of LLDP TLVs received on the given port that
                are not recognized by this LLDP agent on the indicated port.
                
                An unrecognized TLV is referred to as the TLV whose type value
                is in the range of reserved TLV types (000 1001 - 111 1110)
                in Table 9.1 of IEEE Std 802.1AB-2005.  An unrecognized
                TLV may be a basic management TLV from a later LLDP version.
                ''',
                'lldpstatsrxporttlvsunrecognizedtotal',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpStatsRxPortEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpStatsRxPortTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpStatsRxPortTable',
            False, 
            [
            _MetaInfoClassMember('lldpStatsRxPortEntry', REFERENCE_LIST, 'LldpStatsRxPortEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry', 
                [], [], 
                '''                LLDP frame reception statistics for a particular port.
                The port must be contained in the same chassis as the
                LLDP agent.
                
                All counter values in a particular entry shall be
                maintained on a continuing basis and shall not be deleted
                upon expiration of rxInfoTTL timing counters in the LLDP
                remote systems MIB of the receipt of a shutdown frame from
                a remote LLDP agent.
                
                All statistical counters associated with a particular
                port on the local LLDP agent become frozen whenever the
                adminStatus is disabled for the same port.
                ''',
                'lldpstatsrxportentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpStatsRxPortTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry',
            False, 
            [
            _MetaInfoClassMember('lldpStatsTxPortNum', ATTRIBUTE, 'int' , None, None, 
                [(1, 4096)], [], 
                '''                The index value used to identify the port component
                (contained in the local chassis with the LLDP agent)
                associated with this entry.
                
                The value of this object is used as a port index to the
                lldpStatsTable.
                ''',
                'lldpstatstxportnum',
                'LLDP-MIB', True),
            _MetaInfoClassMember('lldpStatsTxPortFramesTotal', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of LLDP frames transmitted by this LLDP agent
                on the indicated port.
                ''',
                'lldpstatstxportframestotal',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpStatsTxPortEntry',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB.LldpStatsTxPortTable' : {
        'meta_info' : _MetaInfoClass('LLDPMIB.LldpStatsTxPortTable',
            False, 
            [
            _MetaInfoClassMember('lldpStatsTxPortEntry', REFERENCE_LIST, 'LldpStatsTxPortEntry' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry', 
                [], [], 
                '''                LLDP frame transmission statistics for a particular port.
                The port must be contained in the same chassis as the
                LLDP agent.
                
                All counter values in a particular entry shall be
                maintained on a continuing basis and shall not be deleted
                upon expiration of rxInfoTTL timing counters in the LLDP
                remote systems MIB of the receipt of a shutdown frame from
                a remote LLDP agent.
                
                All statistical counters associated with a particular
                port on the local LLDP agent become frozen whenever the
                adminStatus is disabled for the same port.
                ''',
                'lldpstatstxportentry',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'lldpStatsTxPortTable',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
    'LLDPMIB' : {
        'meta_info' : _MetaInfoClass('LLDPMIB',
            False, 
            [
            _MetaInfoClassMember('lldpConfiguration', REFERENCE_CLASS, 'LldpConfiguration' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpConfiguration', 
                [], [], 
                '''                ''',
                'lldpconfiguration',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocalSystemData', REFERENCE_CLASS, 'LldpLocalSystemData' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpLocalSystemData', 
                [], [], 
                '''                ''',
                'lldplocalsystemdata',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocManAddrTable', REFERENCE_CLASS, 'LldpLocManAddrTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpLocManAddrTable', 
                [], [], 
                '''                This table contains management address information on the
                local system known to this agent.
                ''',
                'lldplocmanaddrtable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpLocPortTable', REFERENCE_CLASS, 'LldpLocPortTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpLocPortTable', 
                [], [], 
                '''                This table contains one or more rows per port information
                associated with the local system known to this agent.
                ''',
                'lldplocporttable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpPortConfigTable', REFERENCE_CLASS, 'LldpPortConfigTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpPortConfigTable', 
                [], [], 
                '''                The table that controls LLDP frame transmission on individual
                ports.
                ''',
                'lldpportconfigtable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemManAddrTable', REFERENCE_CLASS, 'LldpRemManAddrTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemManAddrTable', 
                [], [], 
                '''                This table contains one or more rows per management address
                information on the remote system learned on a particular port
                contained in the local chassis known to this agent.
                ''',
                'lldpremmanaddrtable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemOrgDefInfoTable', REFERENCE_CLASS, 'LldpRemOrgDefInfoTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemOrgDefInfoTable', 
                [], [], 
                '''                This table contains one or more rows per physical network
                connection which advertises the organizationally defined
                information.
                
                Note that this table contains one or more rows of
                organizationally defined information that is not recognized
                by the local agent.
                
                If the local system is capable of recognizing any
                organizationally defined information, appropriate extension
                MIBs from the organization should be used for information
                retrieval.
                ''',
                'lldpremorgdefinfotable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemTable', REFERENCE_CLASS, 'LldpRemTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemTable', 
                [], [], 
                '''                This table contains one or more rows per physical network
                connection known to this agent.  The agent may wish to ensure
                that only one lldpRemEntry is present for each local port,
                or it may choose to maintain multiple lldpRemEntries for
                the same local port.
                
                The following procedure may be used to retrieve remote
                systems information updates from an LLDP agent:
                
                   1. NMS polls all tables associated with remote systems
                      and keeps a local copy of the information retrieved.
                      NMS polls periodically the values of the following
                      objects:
                         a. lldpStatsRemTablesInserts
                         b. lldpStatsRemTablesDeletes
                         c. lldpStatsRemTablesDrops
                         d. lldpStatsRemTablesAgeouts
                         e. lldpStatsRxPortAgeoutsTotal for all ports.
                
                   2. LLDP agent updates remote systems MIB objects, and
                      sends out notifications to a list of notification
                      destinations.
                
                   3. NMS receives the notifications and compares the new
                      values of objects listed in step 1.  
                
                      Periodically, NMS should poll the object
                      lldpStatsRemTablesLastChangeTime to find out if anything
                      has changed since the last poll.  if something has
                      changed, NMS will poll the objects listed in step 1 to
                      figure out what kind of changes occurred in the tables.
                
                      if value of lldpStatsRemTablesInserts has changed,
                      then NMS will walk all tables by employing TimeFilter
                      with the last-polled time value.  This request will
                      return new objects or objects whose values are updated
                      since the last poll.
                
                      if value of lldpStatsRemTablesAgeouts has changed,
                      then NMS will walk the lldpStatsRxPortAgeoutsTotal and
                      compare the new values with previously recorded ones.
                      For ports whose lldpStatsRxPortAgeoutsTotal value is
                      greater than the recorded value, NMS will have to
                      retrieve objects associated with those ports from
                      table(s) without employing a TimeFilter (which is
                      performed by specifying 0 for the TimeFilter.)
                
                      lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops
                      objects are provided for informational purposes.
                ''',
                'lldpremtable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpRemUnknownTLVTable', REFERENCE_CLASS, 'LldpRemUnknownTLVTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpRemUnknownTLVTable', 
                [], [], 
                '''                This table contains information about an incoming TLV which
                is not recognized by the receiving LLDP agent.  The TLV may
                be from a later version of the basic management set.
                
                This table should only contain TLVs that are found in
                a single LLDP frame.  Entries in this table, associated
                with an MAC service access point (MSAP, the access point
                for MAC services provided to the LCC sublayer, defined
                in IEEE 100, which is also identified with a particular
                lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with
                most recently received unrecognized TLV from the same MSAP,
                or they will naturally age out when the rxInfoTTL timer
                (associated with the MSAP) expires.
                ''',
                'lldpremunknowntlvtable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatistics', REFERENCE_CLASS, 'LldpStatistics' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpStatistics', 
                [], [], 
                '''                ''',
                'lldpstatistics',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsRxPortTable', REFERENCE_CLASS, 'LldpStatsRxPortTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpStatsRxPortTable', 
                [], [], 
                '''                A table containing LLDP reception statistics for individual
                ports.  Entries are not required to exist in this table while
                the lldpPortConfigEntry object is equal to 'disabled(4)'.
                ''',
                'lldpstatsrxporttable',
                'LLDP-MIB', False),
            _MetaInfoClassMember('lldpStatsTxPortTable', REFERENCE_CLASS, 'LldpStatsTxPortTable' , 'ydk.models.lldp.LLDP_MIB', 'LLDPMIB.LldpStatsTxPortTable', 
                [], [], 
                '''                A table containing LLDP transmission statistics for
                individual ports.  Entries are not required to exist in
                this table while the lldpPortConfigEntry object is equal to
                'disabled(4)'.
                ''',
                'lldpstatstxporttable',
                'LLDP-MIB', False),
            ],
            'LLDP-MIB',
            'LLDP-MIB',
            _yang_ns._namespaces['LLDP-MIB'],
        'ydk.models.lldp.LLDP_MIB'
        ),
    },
}
_meta_table['LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpLocManAddrTable']['meta_info']
_meta_table['LLDPMIB.LldpLocPortTable.LldpLocPortEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpLocPortTable']['meta_info']
_meta_table['LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpPortConfigTable']['meta_info']
_meta_table['LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpRemManAddrTable']['meta_info']
_meta_table['LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpRemOrgDefInfoTable']['meta_info']
_meta_table['LLDPMIB.LldpRemTable.LldpRemEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpRemTable']['meta_info']
_meta_table['LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpRemUnknownTLVTable']['meta_info']
_meta_table['LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpStatsRxPortTable']['meta_info']
_meta_table['LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry']['meta_info'].parent =_meta_table['LLDPMIB.LldpStatsTxPortTable']['meta_info']
_meta_table['LLDPMIB.LldpConfiguration']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpLocManAddrTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpLocPortTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpLocalSystemData']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpPortConfigTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpRemManAddrTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpRemOrgDefInfoTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpRemTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpRemUnknownTLVTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpStatistics']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpStatsRxPortTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
_meta_table['LLDPMIB.LldpStatsTxPortTable']['meta_info'].parent =_meta_table['LLDPMIB']['meta_info']
