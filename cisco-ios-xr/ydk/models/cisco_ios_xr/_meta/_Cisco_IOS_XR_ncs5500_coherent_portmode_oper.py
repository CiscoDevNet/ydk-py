


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ControllerPortMode.OpticsName.PortModeInfo' : {
        'meta_info' : _MetaInfoClass('ControllerPortMode.OpticsName.PortModeInfo',
            False, 
            [
            _MetaInfoClassMember('diff', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics diff
                ''',
                'diff',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            _MetaInfoClassMember('fec', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics fec
                ''',
                'fec',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            _MetaInfoClassMember('modulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics modulation
                ''',
                'modulation',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics speed
                ''',
                'speed',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-portmode-oper',
            'port-mode-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-portmode-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper'
        ),
    },
    'ControllerPortMode.OpticsName' : {
        'meta_info' : _MetaInfoClass('ControllerPortMode.OpticsName',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', True),
            _MetaInfoClassMember('port-mode-info', REFERENCE_CLASS, 'PortModeInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper', 'ControllerPortMode.OpticsName.PortModeInfo', 
                [], [], 
                '''                PortMode  operational data
                ''',
                'port_mode_info',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-portmode-oper',
            'optics-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-portmode-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper'
        ),
    },
    'ControllerPortMode' : {
        'meta_info' : _MetaInfoClass('ControllerPortMode',
            False, 
            [
            _MetaInfoClassMember('optics-name', REFERENCE_LIST, 'OpticsName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper', 'ControllerPortMode.OpticsName', 
                [], [], 
                '''                Name of optics controller
                ''',
                'optics_name',
                'Cisco-IOS-XR-ncs5500-coherent-portmode-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-portmode-oper',
            'controller-port-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-portmode-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_portmode_oper'
        ),
    },
}
_meta_table['ControllerPortMode.OpticsName.PortModeInfo']['meta_info'].parent =_meta_table['ControllerPortMode.OpticsName']['meta_info']
_meta_table['ControllerPortMode.OpticsName']['meta_info'].parent =_meta_table['ControllerPortMode']['meta_info']
