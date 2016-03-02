


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry',
            False, 
            [
            _MetaInfoClassMember('dot3StatsIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'dot3statsindex',
                'CISCO-ETHERLIKE-EXT-MIB', True),
            _MetaInfoClassMember('ceeDot3PauseExtAdminMode', REFERENCE_BITS, 'CeeDot3PauseExtAdminMode_Bits' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtAdminMode_Bits', 
                [], [], 
                '''                Indicates preference to send or process pause
                frames on this interface.
                txDesired(0)  -  indicates preference to send pause 
                                 frames, but autonegotiates flow 
                                 control. This bit can only be 
                                 turned on when the corresponding 
                                 instance of dot3PauseAdminMode 
                                 has the value of 'enabledXmit' or 
                                 'enabledXmitAndRcv'.
                rxDesired(1)  -  indicates preference to process 
                                 pause frames, but autonegotiates 
                                 flow control. This bit can only be 
                                 turned on when the corresponding 
                                 instance of dot3PauseAdminMode 
                                 has the value of 'enabledRcv' or 
                                 'enabledXmitAndRcv'.
                ''',
                'ceedot3pauseextadminmode',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            _MetaInfoClassMember('ceeDot3PauseExtOperMode', REFERENCE_BITS, 'CeeDot3PauseExtOperMode_Bits' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtOperMode_Bits', 
                [], [], 
                '''                Provides additional information about the flow
                control operational status on this interface.
                txDisagree(0) - the transmit pause function on 
                                this interface is disabled due to 
                                disagreement from the far end on 
                                negotiation.
                rxDisagree(1) - the receive pause function on  
                                this interface is disabled due to 
                                disagreement from the far end on 
                                negotiation.
                txDesired(2)  - the transmit pause function on 
                                this interface is desired.
                rxDesired(3)  - the receive pause function on  
                                this interface is desired.
                ''',
                'ceedot3pauseextopermode',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            ],
            'CISCO-ETHERLIKE-EXT-MIB',
            'ceeDot3PauseExtEntry',
            _yang_ns._namespaces['CISCO-ETHERLIKE-EXT-MIB'],
        'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB'
        ),
    },
    'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable' : {
        'meta_info' : _MetaInfoClass('CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable',
            False, 
            [
            _MetaInfoClassMember('ceeDot3PauseExtEntry', REFERENCE_LIST, 'CeeDot3PauseExtEntry' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry', 
                [], [], 
                '''                An entry in the table, containing additional
                information about the MAC Control PAUSE function 
                on a single ethernet-like interface, in extension 
                to dot3PauseEntry in Etherlike-MIB.
                ''',
                'ceedot3pauseextentry',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            ],
            'CISCO-ETHERLIKE-EXT-MIB',
            'ceeDot3PauseExtTable',
            _yang_ns._namespaces['CISCO-ETHERLIKE-EXT-MIB'],
        'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB'
        ),
    },
    'CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-ETHERLIKE-EXT-MIB', True),
            _MetaInfoClassMember('ceeSubInterfaceCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the number of subinterfaces
                created on a Ethernet-like interface.
                ''',
                'ceesubinterfacecount',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            ],
            'CISCO-ETHERLIKE-EXT-MIB',
            'ceeSubInterfaceEntry',
            _yang_ns._namespaces['CISCO-ETHERLIKE-EXT-MIB'],
        'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB'
        ),
    },
    'CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable' : {
        'meta_info' : _MetaInfoClass('CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('ceeSubInterfaceEntry', REFERENCE_LIST, 'CeeSubInterfaceEntry' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry', 
                [], [], 
                '''                This table contains a row for each Ethernet-like interface
                by it's ifTable ifIndex in the system, which supports the
                sub-interface.
                
                An entry is created by an agent, when it detects a
                Ethernet-like interface is created in ifTable and it 
                can support sub-interface.
                
                An entry is deleted by an agent, when the ifTable entry
                associated to the Ethernet-like interface is deleted.
                Typically, when the card is removed from the device.
                ''',
                'ceesubinterfaceentry',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            ],
            'CISCO-ETHERLIKE-EXT-MIB',
            'ceeSubInterfaceTable',
            _yang_ns._namespaces['CISCO-ETHERLIKE-EXT-MIB'],
        'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB'
        ),
    },
    'CISCOETHERLIKEEXTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOETHERLIKEEXTMIB',
            False, 
            [
            _MetaInfoClassMember('ceeDot3PauseExtTable', REFERENCE_CLASS, 'CeeDot3PauseExtTable' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable', 
                [], [], 
                '''                A list of additional descriptive and status
                information about the MAC Control PAUSE 
                function on the ethernet-like interfaces 
                attached to a particular system, in extension to
                dot3PauseTable in EtherLike-MIB. There will be 
                one row in this table for each ethernet-like 
                interface in the system which supports the MAC 
                Control PAUSE function.
                ''',
                'ceedot3pauseexttable',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            _MetaInfoClassMember('ceeSubInterfaceTable', REFERENCE_CLASS, 'CeeSubInterfaceTable' , 'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB', 'CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable', 
                [], [], 
                '''                This table provides the subinterface related information
                associated to the Ethernet-like interfaces.
                
                The subinterface is a division of one physical interface into
                multiple logical interfaces. As an example of what a typical
                subinterface setup might look like on a device, a single
                Ethernet port such as GigabitEthernet0/0 would be subdivided
                into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as
                if it were a separate interface.
                ''',
                'ceesubinterfacetable',
                'CISCO-ETHERLIKE-EXT-MIB', False),
            ],
            'CISCO-ETHERLIKE-EXT-MIB',
            'CISCO-ETHERLIKE-EXT-MIB',
            _yang_ns._namespaces['CISCO-ETHERLIKE-EXT-MIB'],
        'ydk.models.etherlike.CISCO_ETHERLIKE_EXT_MIB'
        ),
    },
}
_meta_table['CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry']['meta_info'].parent =_meta_table['CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable']['meta_info']
_meta_table['CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry']['meta_info'].parent =_meta_table['CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable']['meta_info']
_meta_table['CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable']['meta_info'].parent =_meta_table['CISCOETHERLIKEEXTMIB']['meta_info']
_meta_table['CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable']['meta_info'].parent =_meta_table['CISCOETHERLIKEEXTMIB']['meta_info']
