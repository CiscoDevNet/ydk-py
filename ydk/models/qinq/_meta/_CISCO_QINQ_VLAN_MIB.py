


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CqvEncapsulationType_Enum' : _MetaInfoEnum('CqvEncapsulationType_Enum', 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB',
        {
            'isl':'ISL',
            'dot1Q':'DOT1Q',
        }, 'CISCO-QINQ-VLAN-MIB', _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB']),
    'CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry',
            False, 
            [
            _MetaInfoClassMember('cqvTerminationCeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The VLAN ID of the inner tag of a QinQ frame.
                ''',
                'cqvterminationcevlanid',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('cqvTerminationPeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The VLAN ID of the outer tag of a QinQ frame.
                ''',
                'cqvterminationpevlanid',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('cqvTerminationPeEncap', REFERENCE_ENUM_CLASS, 'CqvEncapsulationType_Enum' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CqvEncapsulationType_Enum', 
                [], [], 
                '''                The encapsulation type of the PE VLAN
                (cqvTerminationPeVlanId) of a QinQ frame.
                ''',
                'cqvterminationpeencap',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTerminationRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or deletion
                of a conceptual row in this table.
                ''',
                'cqvterminationrowstatus',
                'CISCO-QINQ-VLAN-MIB', False),
            ],
            'CISCO-QINQ-VLAN-MIB',
            'cqvTerminationEntry',
            _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB'],
        'ydk.models.qinq.CISCO_QINQ_VLAN_MIB'
        ),
    },
    'CISCOQINQVLANMIB.CqvTerminationTable' : {
        'meta_info' : _MetaInfoClass('CISCOQINQVLANMIB.CqvTerminationTable',
            False, 
            [
            _MetaInfoClassMember('cqvTerminationEntry', REFERENCE_LIST, 'CqvTerminationEntry' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry', 
                [], [], 
                '''                An entry in this table defines a QinQ terminated interface.
                ''',
                'cqvterminationentry',
                'CISCO-QINQ-VLAN-MIB', False),
            ],
            'CISCO-QINQ-VLAN-MIB',
            'cqvTerminationTable',
            _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB'],
        'ydk.models.qinq.CISCO_QINQ_VLAN_MIB'
        ),
    },
    'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationCosPBits_Enum' : _MetaInfoEnum('CqvTranslationCosPBits_Enum', 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB',
        {
            'copyFromOuterTag':'COPYFROMOUTERTAG',
            'copyFromInnerTag':'COPYFROMINNERTAG',
        }, 'CISCO-QINQ-VLAN-MIB', _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB']),
    'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationType_Enum' : _MetaInfoEnum('CqvTranslationType_Enum', 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB',
        {
            'doubleToSingle':'DOUBLETOSINGLE',
            'doubleToDouble':'DOUBLETODOUBLE',
            'doubleToDoubleOutOfRange':'DOUBLETODOUBLEOUTOFRANGE',
        }, 'CISCO-QINQ-VLAN-MIB', _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB']),
    'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry' : {
        'meta_info' : _MetaInfoClass('CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry',
            False, 
            [
            _MetaInfoClassMember('cqvTranslationInternalCeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                The QinQ inner VLAN ID of an internal double tagged frame.
                
                This object will have the value of zero as described in the
                cqvTranslationType object.
                ''',
                'cqvtranslationinternalcevlanid',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('cqvTranslationInternalPeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                The QinQ outer VLAN ID of an internal double tagged frame.
                
                This object will have the value of zero as described in the
                cqvTranslationType object.
                ''',
                'cqvtranslationinternalpevlanid',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-QINQ-VLAN-MIB', True),
            _MetaInfoClassMember('cqvTranslationCosPBits', REFERENCE_ENUM_CLASS, 'CqvTranslationCosPBits_Enum' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationCosPBits_Enum', 
                [], [], 
                '''                This object indicates how the IEEE 802.1P bits (P bits) in the
                IEEE 802.1Q header of the trunk VLAN are to be set.  The P bits
                in the trunk VLAN can be set by copying the P bits of the
                outer PE tag or the inner CE tag.
                
                    'copyFromOuterTag' - Copy the P bits from the outer PE tag.
                
                    'copyFromInnerTag' - Copy the P bits from the inner CE tag.
                ''',
                'cqvtranslationcospbits',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTranslationRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object facilitates the creation, modification, or deletion
                of a conceptual row in this table.
                ''',
                'cqvtranslationrowstatus',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTranslationTrunkCeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                The QinQ inner VLAN ID of a trunk VLAN frame.
                
                This object will have the value of zero as described in the
                cqvTranslationType object.
                ''',
                'cqvtranslationtrunkcevlanid',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTranslationTrunkPeVlanId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4094)], [], 
                '''                The QinQ outer VLAN ID of a trunk VLAN frame.
                
                This object will have the value of zero as described in the
                cqvTranslationType object.
                ''',
                'cqvtranslationtrunkpevlanid',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTranslationType', REFERENCE_ENUM_CLASS, 'CqvTranslationType_Enum' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry.CqvTranslationType_Enum', 
                [], [], 
                '''                The QinQ translation type being performed on the interface.
                
                'doubleToSingle' - Double tagged to single tagged traffic.
                                   The value of cqvTranslationTrunkPeVlanId
                                   will be zero.  This indicates that the PE
                                   VLAN tag will be absent in the trunk
                                   interface.
                
                'doubleToDouble' - Double tagged to double tagged traffic.
                                   The value of the internal PE and CE, and
                                   the trunk PE and CE VLAN IDs are
                                   non-zero.
                
                'doubleToDoubleOutOfRange' - Double tagged to double tagged
                                   traffic that does not have a defined
                                   translation. The value of
                                   cqvTranslationInternalCeVlanId  will be
                                   zero.  This indicates that the CE
                                   VLAN tag is being used as a wildcard.
                ''',
                'cqvtranslationtype',
                'CISCO-QINQ-VLAN-MIB', False),
            ],
            'CISCO-QINQ-VLAN-MIB',
            'cqvTranslationEntry',
            _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB'],
        'ydk.models.qinq.CISCO_QINQ_VLAN_MIB'
        ),
    },
    'CISCOQINQVLANMIB.CqvTranslationTable' : {
        'meta_info' : _MetaInfoClass('CISCOQINQVLANMIB.CqvTranslationTable',
            False, 
            [
            _MetaInfoClassMember('cqvTranslationEntry', REFERENCE_LIST, 'CqvTranslationEntry' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry', 
                [], [], 
                '''                An entry in this table contains translation information for
                a particular QinQ interface.
                ''',
                'cqvtranslationentry',
                'CISCO-QINQ-VLAN-MIB', False),
            ],
            'CISCO-QINQ-VLAN-MIB',
            'cqvTranslationTable',
            _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB'],
        'ydk.models.qinq.CISCO_QINQ_VLAN_MIB'
        ),
    },
    'CISCOQINQVLANMIB' : {
        'meta_info' : _MetaInfoClass('CISCOQINQVLANMIB',
            False, 
            [
            _MetaInfoClassMember('cqvTerminationTable', REFERENCE_CLASS, 'CqvTerminationTable' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTerminationTable', 
                [], [], 
                '''                This table contains attributes pertaining to QinQ
                terminated interfaces.
                
                The ifIndex in the INDEX clause identifies the interface
                that terminates QinQ traffic.
                
                A management application can create a conceptual row in this
                table by setting the cqvTerminationRowStatus to
                'createAndWait' or 'createAndGo'.
                
                A conceptual row in this table cannot be modified while
                cqvTerminationRowStatus is set to 'active'.
                ''',
                'cqvterminationtable',
                'CISCO-QINQ-VLAN-MIB', False),
            _MetaInfoClassMember('cqvTranslationTable', REFERENCE_CLASS, 'CqvTranslationTable' , 'ydk.models.qinq.CISCO_QINQ_VLAN_MIB', 'CISCOQINQVLANMIB.CqvTranslationTable', 
                [], [], 
                '''                This table defines the translations performed on QinQ capable
                interfaces.
                
                The ifIndex in the INDEX clause identifies the QinQ interface.
                
                A QinQ interface performs the following translations:
                
                - Double Tagged to Single Tagged - the inner and outer tags of
                  the frames internal to the switch are replaced with a single
                  trunk VLAN tag when the outgoing frame is transmitted.
                
                - Double Tagged to Double Tagged - the outer tag of the frames
                  internal to the switch are replaced with an outer trunk
                  VLAN tag when the outgoing frame is transmitted.  The inner
                  tag remains unchanged in the transmitted frame.
                
                The following picture illustrates QinQ translations.
                
                       <----- Provider Side -----|----- Customer Side ----->
                
                             Switch
                +--------------------------------+
                |                                |
                |  +---------------+     +-------|     +------------------+
                |  | Double Tagged |     |  QinQ |     | Single or Double |
                |  | Frames        | --> |  Intf | --> | Tagged Frames    |
                |  +---------------+     +-------|     +------------------+
                |                                |
                +--------------------------------+
                
                Also, the QinQ interface sets the IEEE 802.1P prioritization
                bits (P bits) in the outgoing frames by copying the P bits
                either from the internal frame's outer or inner VLAN tag.
                
                A management application can create a conceptual row in this
                table by setting the cqvTranslationRowStatus to
                'createAndWait' or 'createAndGo'.
                
                A conceptual row in this table cannot be modified while
                cqvTranslationRowStatus is set to 'active'.
                ''',
                'cqvtranslationtable',
                'CISCO-QINQ-VLAN-MIB', False),
            ],
            'CISCO-QINQ-VLAN-MIB',
            'CISCO-QINQ-VLAN-MIB',
            _yang_ns._namespaces['CISCO-QINQ-VLAN-MIB'],
        'ydk.models.qinq.CISCO_QINQ_VLAN_MIB'
        ),
    },
}
_meta_table['CISCOQINQVLANMIB.CqvTerminationTable.CqvTerminationEntry']['meta_info'].parent =_meta_table['CISCOQINQVLANMIB.CqvTerminationTable']['meta_info']
_meta_table['CISCOQINQVLANMIB.CqvTranslationTable.CqvTranslationEntry']['meta_info'].parent =_meta_table['CISCOQINQVLANMIB.CqvTranslationTable']['meta_info']
_meta_table['CISCOQINQVLANMIB.CqvTerminationTable']['meta_info'].parent =_meta_table['CISCOQINQVLANMIB']['meta_info']
_meta_table['CISCOQINQVLANMIB.CqvTranslationTable']['meta_info'].parent =_meta_table['CISCOQINQVLANMIB']['meta_info']
