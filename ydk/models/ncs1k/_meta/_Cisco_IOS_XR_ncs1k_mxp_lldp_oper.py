


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'LldpSnoopData.EthernetControllerNames.EthernetControllerName' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames.EthernetControllerName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', True),
            _MetaInfoClassMember('lldp-neighbor', ATTRIBUTE, 'str' , None, None, 
                [(0, 40)], [], 
                '''                LldpNeighbor
                ''',
                'lldp_neighbor',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'ethernet-controller-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames',
            False, 
            [
            _MetaInfoClassMember('ethernet-controller-name', REFERENCE_LIST, 'EthernetControllerName' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames.EthernetControllerName', 
                [], [], 
                '''                port Name
                ''',
                'ethernet_controller_name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'ethernet-controller-names',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData',
            False, 
            [
            _MetaInfoClassMember('ethernet-controller-names', REFERENCE_CLASS, 'EthernetControllerNames' , 'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames', 
                [], [], 
                '''                Ethernet controller snoop data
                ''',
                'ethernet_controller_names',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'lldp-snoop-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.ncs1k.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
}
_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName']['meta_info'].parent =_meta_table['LldpSnoopData.EthernetControllerNames']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames']['meta_info'].parent =_meta_table['LldpSnoopData']['meta_info']
