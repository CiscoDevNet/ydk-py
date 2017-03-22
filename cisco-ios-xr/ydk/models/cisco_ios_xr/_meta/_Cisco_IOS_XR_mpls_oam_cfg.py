


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsOam.ReplyMode.ControlChannel' : {
        'meta_info' : _MetaInfoClass('MplsOam.ReplyMode.ControlChannel',
            False, 
            [
            _MetaInfoClassMember('allow-reverse-lsp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use Reverse LSP as the control channel
                ''',
                'allow_reverse_lsp',
                'Cisco-IOS-XR-mpls-oam-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-oam-cfg',
            'control-channel',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg'
        ),
    },
    'MplsOam.ReplyMode' : {
        'meta_info' : _MetaInfoClass('MplsOam.ReplyMode',
            False, 
            [
            _MetaInfoClassMember('control-channel', REFERENCE_CLASS, 'ControlChannel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg', 'MplsOam.ReplyMode.ControlChannel', 
                [], [], 
                '''                Configure control channel reply mode
                ''',
                'control_channel',
                'Cisco-IOS-XR-mpls-oam-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-oam-cfg',
            'reply-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg'
        ),
    },
    'MplsOam' : {
        'meta_info' : _MetaInfoClass('MplsOam',
            False, 
            [
            _MetaInfoClassMember('disable-vendor-extension', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable vendor extension
                ''',
                'disable_vendor_extension',
                'Cisco-IOS-XR-mpls-oam-cfg', False),
            _MetaInfoClassMember('enable-oam', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS OAM globally.Without
                creating this object the MPLS OAM feature will
                not be enabled. Deleting this object will stop
                the MPLS OAM feature.
                ''',
                'enable_oam',
                'Cisco-IOS-XR-mpls-oam-cfg', False),
            _MetaInfoClassMember('reply-mode', REFERENCE_CLASS, 'ReplyMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg', 'MplsOam.ReplyMode', 
                [], [], 
                '''                Echo request reply mode attributes
                ''',
                'reply_mode',
                'Cisco-IOS-XR-mpls-oam-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-oam-cfg',
            'mpls-oam',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_cfg'
        ),
    },
}
_meta_table['MplsOam.ReplyMode.ControlChannel']['meta_info'].parent =_meta_table['MplsOam.ReplyMode']['meta_info']
_meta_table['MplsOam.ReplyMode']['meta_info'].parent =_meta_table['MplsOam']['meta_info']
