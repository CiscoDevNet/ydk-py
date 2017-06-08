


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Proxy.TargetList' : {
        'meta_info' : _MetaInfoClass('Proxy.TargetList',
            False, 
            [
            _MetaInfoClassMember('target-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target ID
                ''',
                'target_id',
                'ietf-netconf-proxy', True),
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication
                ''',
                'authentication',
                'ietf-netconf-proxy', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Support protocols
                ''',
                'protocol',
                'ietf-netconf-proxy', False),
            ],
            'ietf-netconf-proxy',
            'target-list',
            _yang_ns._namespaces['ietf-netconf-proxy'],
        'ydk.models.ietf.ietf_netconf_proxy'
        ),
    },
    'Proxy' : {
        'meta_info' : _MetaInfoClass('Proxy',
            False, 
            [
            _MetaInfoClassMember('proxy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Proxy name
                ''',
                'proxy_name',
                'ietf-netconf-proxy', False),
            _MetaInfoClassMember('target-list', REFERENCE_LIST, 'TargetList' , 'ydk.models.ietf.ietf_netconf_proxy', 'Proxy.TargetList', 
                [], [], 
                '''                List for target information
                ''',
                'target_list',
                'ietf-netconf-proxy', False),
            ],
            'ietf-netconf-proxy',
            'proxy',
            _yang_ns._namespaces['ietf-netconf-proxy'],
        'ydk.models.ietf.ietf_netconf_proxy'
        ),
    },
}
_meta_table['Proxy.TargetList']['meta_info'].parent =_meta_table['Proxy']['meta_info']
