


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IfStateTypeEnum' : _MetaInfoEnum('IfStateTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Down':'Down',
            'Loopback':'Loopback',
            'Waiting':'Waiting',
            'Point-to-Point':'Point_to_Point',
            'DR':'DR',
            'BDR':'BDR',
            'DR-Other':'DR_Other',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'PacketTypeEnum' : _MetaInfoEnum('PacketTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Hello':'Hello',
            'Database-Descripton':'Database_Descripton',
            'Link-State-Request':'Link_State_Request',
            'Link-State-Update':'Link_State_Update',
            'Link-State-Ack':'Link_State_Ack',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'NssaTranslatorStateTypeEnum' : _MetaInfoEnum('NssaTranslatorStateTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Enabled':'Enabled',
            'Elected':'Elected',
            'Disabled':'Disabled',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'RestartExitReasonTypeEnum' : _MetaInfoEnum('RestartExitReasonTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'None':'None_',
            'InProgress':'InProgress',
            'Completed':'Completed',
            'TimedOut':'TimedOut',
            'TopologyChanged':'TopologyChanged',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'NbrStateTypeEnum' : _MetaInfoEnum('NbrStateTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Down':'Down',
            'Attempt':'Attempt',
            'Init':'Init',
            '2-Way':'Y_2_Way',
            'ExStart':'ExStart',
            'Exchange':'Exchange',
            'Loading':'Loading',
            'Full':'Full',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'RestartStatusTypeEnum' : _MetaInfoEnum('RestartStatusTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Not-Restarting':'Not_Restarting',
            'Planned-Restart':'Planned_Restart',
            'Unplanned-Restart':'Unplanned_Restart',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'RestartHelperStatusTypeEnum' : _MetaInfoEnum('RestartHelperStatusTypeEnum', 'ydk.models.ietf.ietf_ospf',
        {
            'Not-Helping':'Not_Helping',
            'Helping':'Helping',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'Ospfv3Identity' : {
        'meta_info' : _MetaInfoClass('Ospfv3Identity',
            False, 
            [
            ],
            'ietf-ospf',
            'ospfv3',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'OperationModeIdentity' : {
        'meta_info' : _MetaInfoClass('OperationModeIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'operation-mode',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'Ospfv2Identity' : {
        'meta_info' : _MetaInfoClass('Ospfv2Identity',
            False, 
            [
            ],
            'ietf-ospf',
            'ospfv2',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'IfLinkTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IfLinkTypeIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'if-link-type',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'OspfIdentity' : {
        'meta_info' : _MetaInfoClass('OspfIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'ospf',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'AreaTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AreaTypeIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'area-type',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'IfLinkTypeShamLinkIdentity' : {
        'meta_info' : _MetaInfoClass('IfLinkTypeShamLinkIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'if-link-type-sham-link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'ShipsInTheNightIdentity' : {
        'meta_info' : _MetaInfoClass('ShipsInTheNightIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'ships-in-the-night',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'NormalIdentity' : {
        'meta_info' : _MetaInfoClass('NormalIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'normal',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'StubIdentity' : {
        'meta_info' : _MetaInfoClass('StubIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'stub',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'NssaIdentity' : {
        'meta_info' : _MetaInfoClass('NssaIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'nssa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'IfLinkTypeNormalIdentity' : {
        'meta_info' : _MetaInfoClass('IfLinkTypeNormalIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'if-link-type-normal',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
    'IfLinkTypeVirtualLinkIdentity' : {
        'meta_info' : _MetaInfoClass('IfLinkTypeVirtualLinkIdentity',
            False, 
            [
            ],
            'ietf-ospf',
            'if-link-type-virtual-link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_ospf'
        ),
    },
}
