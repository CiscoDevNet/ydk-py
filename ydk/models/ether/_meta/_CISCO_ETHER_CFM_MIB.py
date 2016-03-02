


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventCode_Enum' : _MetaInfoEnum('CEtherCfmEventCode_Enum', 'ydk.models.ether.CISCO_ETHER_CFM_MIB',
        {
            'new':'NEW',
            'returning':'RETURNING',
            'portState':'PORTSTATE',
            'lastGasp':'LASTGASP',
            'timeout':'TIMEOUT',
            'configClear':'CONFIGCLEAR',
            'loopClear':'LOOPCLEAR',
            'xconnectClear':'XCONNECTCLEAR',
            'unknownClear':'UNKNOWNCLEAR',
        }, 'CISCO-ETHER-CFM-MIB', _yang_ns._namespaces['CISCO-ETHER-CFM-MIB']),
    'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventDeleteRow_Enum' : _MetaInfoEnum('CEtherCfmEventDeleteRow_Enum', 'ydk.models.ether.CISCO_ETHER_CFM_MIB',
        {
            'noop':'NOOP',
            'delete':'DELETE',
        }, 'CISCO-ETHER-CFM-MIB', _yang_ns._namespaces['CISCO-ETHER-CFM-MIB']),
    'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventRmtPortState_Enum' : _MetaInfoEnum('CEtherCfmEventRmtPortState_Enum', 'ydk.models.ether.CISCO_ETHER_CFM_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'adminDown':'ADMINDOWN',
            'test':'TEST',
            'remoteExcessiveErrors':'REMOTEEXCESSIVEERRORS',
            'localExcessiveErrors':'LOCALEXCESSIVEERRORS',
            'localNoData':'LOCALNODATA',
        }, 'CISCO-ETHER-CFM-MIB', _yang_ns._namespaces['CISCO-ETHER-CFM-MIB']),
    'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventType_Enum' : _MetaInfoEnum('CEtherCfmEventType_Enum', 'ydk.models.ether.CISCO_ETHER_CFM_MIB',
        {
            'mepUp':'MEPUP',
            'mepDown':'MEPDOWN',
            'xconnect':'XCONNECT',
            'loop':'LOOP',
            'config':'CONFIG',
            'xcheckMissing':'XCHECKMISSING',
            'xcheckUnknown':'XCHECKUNKNOWN',
            'xcheckServiceUp':'XCHECKSERVICEUP',
        }, 'CISCO-ETHER-CFM-MIB', _yang_ns._namespaces['CISCO-ETHER-CFM-MIB']),
    'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry' : {
        'meta_info' : _MetaInfoClass('CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry',
            False, 
            [
            _MetaInfoClassMember('cEtherCfmEventDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object represents the ID which uniquely identifies 
                a CFM maintenance domain on the device. Every domain can
                be uniquely identified by its user-defined 
                name (cEtherCfmEventDomainName) or device-assigned ID (this
                object).
                ''',
                'cethercfmeventdomainindex',
                'CISCO-ETHER-CFM-MIB', True),
            _MetaInfoClassMember('cEtherCfmEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A monotonically increasing integer for the sole purpose of
                indexing CFM events.  When it reaches the maximum value 
                supported by the agent, as defined in the 
                cEtherCfmMaxEventIndex object, the agent wraps the value
                back to 1 and may flush existing entries.
                ''',
                'cethercfmeventindex',
                'CISCO-ETHER-CFM-MIB', True),
            _MetaInfoClassMember('cEtherCfmEventSvlan', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The service VLAN identifier of the customer service 
                instance to which the event belongs.
                ''',
                'cethercfmeventsvlan',
                'CISCO-ETHER-CFM-MIB', True),
            _MetaInfoClassMember('cEtherCfmEventCode', REFERENCE_ENUM_CLASS, 'CEtherCfmEventCode_Enum' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventCode_Enum', 
                [], [], 
                '''                This object is used in decoding 'mepUp' and 'mepDown' events. 
                
                ** For 'mepUp', the following codes are relevant:
                
                    'new'           - This is the very first time the device 
                                      receives a CC message from the remote MEP.
                
                    'returning'     - The device received a CC message from a 
                                      remote MEP for which it had an expired 
                                      CCDB entry.
                
                    'portState'     - The device received a CC message from a 
                                      remote MEP for which it has a valid CCDB 
                                      entry, and the message indicates a port 
                                      status change.
                
                ** For 'mepDown', the following codes are relevant:
                
                    'lastGasp'      - The device received a CC message from a
                                      remote MEP with zero lifetime.
                
                    'timeout'       - The local CCDB entry for the remote MEP 
                                      expired.
                
                    'configClear'   - A previous CC message from a MEP that
                                      triggered a configuration error event
                                      is cleared.
                    
                    'loopClear'     - A previous CC message from a MEP that
                                      triggered a loop error event is cleared.
                
                    'xconnectClear' - A previous CC message from a MEP that
                                      triggered a crossconnect error event 
                                      is cleared.
                
                    'unknownClear'  - A previous CC message from a MEP that
                                      triggered an unknown MEP event is 
                                      cleared.
                ''',
                'cethercfmeventcode',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventDeleteRow', REFERENCE_ENUM_CLASS, 'CEtherCfmEventDeleteRow_Enum' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventDeleteRow_Enum', 
                [], [], 
                '''                This object allows the management station to 
                delete a row in the cEtherCfmEventTable in order
                to free system resources.
                
                When reading this object the value of 'noop' will be 
                returned. This object can only be set to 'delete'. 
                
                When this object is set to 'delete', the conceptual
                row corresponding to this object will be deleted to
                free system resources. This is equivalent to clearing
                the event log. Should the trigger that caused the event
                to be logged reoccur, the event will be re-asserted but
                in a different conceptual row.
                ''',
                'cethercfmeventdeleterow',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventDomainName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                The name of the CFM maintenance domain.
                ''',
                'cethercfmeventdomainname',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time when this row was created.
                ''',
                'cethercfmeventlastchange',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventLclIfCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local interfaces affected by the event.
                ''',
                'cethercfmeventlclifcount',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventLclMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address of the device reporting the event.
                ''',
                'cethercfmeventlclmacaddress',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventLclMepCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of local MEPs affected by the event.
                ''',
                'cethercfmeventlclmepcount',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventLclMepid', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                The identifier of the local MEP impacted by the event.
                ''',
                'cethercfmeventlclmepid',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventRmtMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address of the remote maintenance point for which
                the event entry is being logged.
                ''',
                'cethercfmeventrmtmacaddress',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventRmtMepid', ATTRIBUTE, 'int' , None, None, 
                [(0, 8191)], [], 
                '''                The maintenance end-point identifier of the remote 
                MEP causing the event entry to be logged.
                ''',
                'cethercfmeventrmtmepid',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventRmtPortState', REFERENCE_ENUM_CLASS, 'CEtherCfmEventRmtPortState_Enum' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventRmtPortState_Enum', 
                [], [], 
                '''                The operational state of the port on which the 
                remote MEP is configured. This information is 
                derived from the port-state as indicated in the 
                CC message. The possible values are:
                
                'up'                    - The port is operationally up.
                
                'down'                  - The port is operationally (but not
                                          administratively) down.
                
                'adminDown'             - The port is administratively down.
                
                'test'                  - The port is in test mode (perhaps 
                                          due to an IEEE Standard 802.3ah OAM
                                          intrusive loopback operation).
                
                'remoteExcessiveErrors' - 802.3ah OAM reports that the other 
                                          end of the link is receiving an 
                                          excessive number of invalid frames.
                
                'localExcessiveErrors'  - 802.3ah OAM reports that this end of
                                          the link is receiving an excessive 
                                          number of invalid frames.
                
                'localNoData'           - No data and no CFM messages have been
                                          received for an excessive length of 
                                          time.
                ''',
                'cethercfmeventrmtportstate',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventRmtServiceId', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                The ID that the remote device has configured for the 
                customer service instance (VLAN).
                ''',
                'cethercfmeventrmtserviceid',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventServiceId', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                The customer service instance to which the event belongs.
                ''',
                'cethercfmeventserviceid',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventType', REFERENCE_ENUM_CLASS, 'CEtherCfmEventType_Enum' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry.CEtherCfmEventType_Enum', 
                [], [], 
                '''                This object informs the management station of how to interpret
                the rest of the objects within a row, as summarized in the 
                following table:
                
                Legend I: Ignored Object 
                       V: Valid Object
                
                Object                                 cEtherCfmEventType
                                               | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
                ================================================================
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventDomainIndex      | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventSvlan            | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventIndex            | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventLastChange       | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventServiceId        | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventDomainName       | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventLclMepid         | I | I | I | V | V | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventLclMacAddress    | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventLclMepCount      | V | V | I | I | I | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventLclIfCount       | V | V | I | I | I | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventRmtMepid         | V | V | V | I | I | V | V | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventRmtMacAddress    | V | V | V | I | V | V | V | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventRmtPortState     | V | I | I | I | I | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventRmtServiceId     | I | I | V | I | I | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventCode             | V | V | I | I | I | I | I | I
                                               |   |   |   |   |   |   |   |
                cEtherCfmEventDeleteRow        | V | V | V | V | V | V | V | V
                                               |   |   |   |   |   |   |   |
                
                Note: When reading any ignored object, a value of 0 will 
                be returned by the agent.
                ''',
                'cethercfmeventtype',
                'CISCO-ETHER-CFM-MIB', False),
            ],
            'CISCO-ETHER-CFM-MIB',
            'cEtherCfmEventEntry',
            _yang_ns._namespaces['CISCO-ETHER-CFM-MIB'],
        'ydk.models.ether.CISCO_ETHER_CFM_MIB'
        ),
    },
    'CISCOETHERCFMMIB.CEtherCfmEventTable' : {
        'meta_info' : _MetaInfoClass('CISCOETHERCFMMIB.CEtherCfmEventTable',
            False, 
            [
            _MetaInfoClassMember('cEtherCfmEventEntry', REFERENCE_LIST, 'CEtherCfmEventEntry' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry', 
                [], [], 
                '''                An entry in this table is created for every event reported
                by Ethernet CFM.
                ''',
                'cethercfmevententry',
                'CISCO-ETHER-CFM-MIB', False),
            ],
            'CISCO-ETHER-CFM-MIB',
            'cEtherCfmEventTable',
            _yang_ns._namespaces['CISCO-ETHER-CFM-MIB'],
        'ydk.models.ether.CISCO_ETHER_CFM_MIB'
        ),
    },
    'CISCOETHERCFMMIB.CecCfmEvents' : {
        'meta_info' : _MetaInfoClass('CISCOETHERCFMMIB.CecCfmEvents',
            False, 
            [
            _MetaInfoClassMember('cEtherCfmMaxEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                This object specifies the maximum upper value supported 
                for the cEtherCfmEventIndex index by this agent.
                ''',
                'cethercfmmaxeventindex',
                'CISCO-ETHER-CFM-MIB', False),
            ],
            'CISCO-ETHER-CFM-MIB',
            'cecCfmEvents',
            _yang_ns._namespaces['CISCO-ETHER-CFM-MIB'],
        'ydk.models.ether.CISCO_ETHER_CFM_MIB'
        ),
    },
    'CISCOETHERCFMMIB' : {
        'meta_info' : _MetaInfoClass('CISCOETHERCFMMIB',
            False, 
            [
            _MetaInfoClassMember('cecCfmEvents', REFERENCE_CLASS, 'CecCfmEvents' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CecCfmEvents', 
                [], [], 
                '''                ''',
                'ceccfmevents',
                'CISCO-ETHER-CFM-MIB', False),
            _MetaInfoClassMember('cEtherCfmEventTable', REFERENCE_CLASS, 'CEtherCfmEventTable' , 'ydk.models.ether.CISCO_ETHER_CFM_MIB', 'CISCOETHERCFMMIB.CEtherCfmEventTable', 
                [], [], 
                '''                This table contains a collection of Ethernet CFM notifications
                generated by the device. The notifications correspond to events
                recognized by the device and fall into the following classes:
                
                - MEP-Up
                
                - MEP-Down
                
                - Configuration Error
                
                - Forwarding Loop
                
                - Cross-connected Ethernet Connection
                
                - Crosscheck Missing MEP
                
                - Crosscheck Unknown MEP
                
                - Crosscheck Service Up
                
                A conceptual row is created in this table whenever the device 
                encounters one of the events listed above. Rows can only be
                created by the agent, and not at the request of the management
                station.
                
                Rows are deleted at the request of a management station by 
                setting the cEtherCfmEventDeleteRow object to 'delete'.
                Another way of deleting rows is through the CLI.
                
                Although this table may be indexed uniquely by the 
                cEtherCfmEventIndex index, the first two indices 
                (cEtherCfmEventDomainIndex and cEtherCfmEventSvlan) are used
                to speed-up queries per maintenance domain and per customer
                service instance. Furthermore, these two indices will help
                in defining the MIB views easily in order to restrict access
                to the MIB to particular entities (be it a service provider,
                or operator, or customer).
                ''',
                'cethercfmeventtable',
                'CISCO-ETHER-CFM-MIB', False),
            ],
            'CISCO-ETHER-CFM-MIB',
            'CISCO-ETHER-CFM-MIB',
            _yang_ns._namespaces['CISCO-ETHER-CFM-MIB'],
        'ydk.models.ether.CISCO_ETHER_CFM_MIB'
        ),
    },
}
_meta_table['CISCOETHERCFMMIB.CEtherCfmEventTable.CEtherCfmEventEntry']['meta_info'].parent =_meta_table['CISCOETHERCFMMIB.CEtherCfmEventTable']['meta_info']
_meta_table['CISCOETHERCFMMIB.CEtherCfmEventTable']['meta_info'].parent =_meta_table['CISCOETHERCFMMIB']['meta_info']
_meta_table['CISCOETHERCFMMIB.CecCfmEvents']['meta_info'].parent =_meta_table['CISCOETHERCFMMIB']['meta_info']
