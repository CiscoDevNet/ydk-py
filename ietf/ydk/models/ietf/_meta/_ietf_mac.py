


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DiscardtypeEnum' : _MetaInfoEnum('DiscardtypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'broadcastDiscard':'broadcastDiscard',
            'unknownMulticastDiscard':'unknownMulticastDiscard',
            'unknownUnicastDiscard':'unknownUnicastDiscard',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MacagetimetypeEnum' : _MetaInfoEnum('MacagetimetypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MacpwencaptypeEnum' : _MetaInfoEnum('MacpwencaptypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'ethernet':'ethernet',
            'vlan':'vlan',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MacenablestatusEnum' : _MetaInfoEnum('MacenablestatusEnum', 'ydk.models.ietf.ietf_mac',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MaclimitforwardEnum' : _MetaInfoEnum('MaclimitforwardEnum', 'ydk.models.ietf.ietf_mac',
        {
            'forward':'forward',
            'discard':'discard',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'LimittypeEnum' : _MetaInfoEnum('LimittypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'macLimit':'macLimit',
            'macApply':'macApply',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MactypeEnum' : _MetaInfoEnum('MactypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'static':'static',
            'dynamic':'dynamic',
            'blackHole':'blackHole',
            'sticky':'sticky',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'BroadcastdomaintypeEnum' : _MetaInfoEnum('BroadcastdomaintypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'VLAN':'VLAN',
            'VSI':'VSI',
            'BD':'BD',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'MacoutiftypeEnum' : _MetaInfoEnum('MacoutiftypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'ac':'ac',
            'pw':'pw',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'DirectiontypeEnum' : _MetaInfoEnum('DirectiontypeEnum', 'ydk.models.ietf.ietf_mac',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'ietf-mac', _yang_ns._namespaces['ietf-mac']),
    'Mac.Globalattribute' : {
        'meta_info' : _MetaInfoClass('Mac.Globalattribute',
            False, 
            [
            _MetaInfoClassMember('macAgeTimeEnable', REFERENCE_ENUM_CLASS, 'MacagetimetypeEnum' , 'ydk.models.ietf.ietf_mac', 'MacagetimetypeEnum', 
                [], [], 
                '''                Whether MAC address aging is enabled.
                ''',
                'macagetimeenable',
                'ietf-mac', False),
            _MetaInfoClassMember('macAgingTime', ATTRIBUTE, 'int' , None, None, 
                [('60', '1000000')], [], 
                '''                Aging time.
                ''',
                'macagingtime',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'globalAttribute',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip',
            False, 
            [
            _MetaInfoClassMember('outPeerIP', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Out Peer IP.
                ''',
                'outpeerip',
                'ietf-mac', True, [
                    _MetaInfoClassMember('outPeerIP', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Out Peer IP.
                        ''',
                        'outpeerip',
                        'ietf-mac', True),
                    _MetaInfoClassMember('outPeerIP', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Out Peer IP.
                        ''',
                        'outpeerip',
                        'ietf-mac', True),
                ]),
            ],
            'ietf-mac',
            'outPeerIP',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanfdbs.Vlanfdb.Outpeerips' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanfdbs.Vlanfdb.Outpeerips',
            False, 
            [
            _MetaInfoClassMember('outPeerIP', REFERENCE_LIST, 'Outpeerip' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip', 
                [], [], 
                '''                Out Peer IP.
                ''',
                'outpeerip',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'outPeerIPs',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanfdbs.Vlanfdb' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanfdbs.Vlanfdb',
            False, 
            [
            _MetaInfoClassMember('macAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address in the format of H-H-H.
                ''',
                'macaddress',
                'ietf-mac', True),
            _MetaInfoClassMember('slotId', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Slot ID.
                ''',
                'slotid',
                'ietf-mac', True),
            _MetaInfoClassMember('vlanId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                VLAN ID.
                ''',
                'vlanid',
                'ietf-mac', True),
            _MetaInfoClassMember('ceVlanId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                User VLAN ID.
                ''',
                'cevlanid',
                'ietf-mac', False),
            _MetaInfoClassMember('isCeDefault', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                CE default VLAN.
                ''',
                'iscedefault',
                'ietf-mac', False),
            _MetaInfoClassMember('isFlood', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flooding MAC.
                ''',
                'isflood',
                'ietf-mac', False),
            _MetaInfoClassMember('isIMac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ingress MAC.
                ''',
                'isimac',
                'ietf-mac', False),
            _MetaInfoClassMember('learnedPeriod', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967294')], [], 
                '''                Dynamic MAC Holding Time.
                ''',
                'learnedperiod',
                'ietf-mac', False),
            _MetaInfoClassMember('macType', REFERENCE_ENUM_CLASS, 'MactypeEnum' , 'ydk.models.ietf.ietf_mac', 'MactypeEnum', 
                [], [], 
                '''                MAC address type, such as blackhole, static, and dynamic.
                ''',
                'mactype',
                'ietf-mac', False),
            _MetaInfoClassMember('outIfName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outbound interface name.
                ''',
                'outifname',
                'ietf-mac', False),
            _MetaInfoClassMember('outNickname', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                Nickname.
                ''',
                'outnickname',
                'ietf-mac', False),
            _MetaInfoClassMember('outPeerIPs', REFERENCE_CLASS, 'Outpeerips' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanfdbs.Vlanfdb.Outpeerips', 
                [], [], 
                '''                Out Peer IPs.
                ''',
                'outpeerips',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vlanFdb',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanfdbs' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanfdbs',
            False, 
            [
            _MetaInfoClassMember('vlanFdb', REFERENCE_LIST, 'Vlanfdb' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanfdbs.Vlanfdb', 
                [], [], 
                '''                VLAN forwarding entry.
                ''',
                'vlanfdb',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vlanFdbs',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsifdbs.Vsifdb' : {
        'meta_info' : _MetaInfoClass('Mac.Vsifdbs.Vsifdb',
            False, 
            [
            _MetaInfoClassMember('macAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address in the format of H-H-H.
                ''',
                'macaddress',
                'ietf-mac', True),
            _MetaInfoClassMember('slotId', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Slot ID.
                ''',
                'slotid',
                'ietf-mac', True),
            _MetaInfoClassMember('vlanid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4094')], [], 
                '''                VLAN ID.
                ''',
                'vlanid',
                'ietf-mac', True),
            _MetaInfoClassMember('vsiName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                VSI Name.
                ''',
                'vsiname',
                'ietf-mac', True),
            _MetaInfoClassMember('cevid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Inner VLAN tag.
                ''',
                'cevid',
                'ietf-mac', False),
            _MetaInfoClassMember('isIMac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ingress MAC.
                ''',
                'isimac',
                'ietf-mac', False),
            _MetaInfoClassMember('learnedPeriod', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967294')], [], 
                '''                Dynamic MAC Holding Time.
                ''',
                'learnedperiod',
                'ietf-mac', False),
            _MetaInfoClassMember('macType', REFERENCE_ENUM_CLASS, 'MactypeEnum' , 'ydk.models.ietf.ietf_mac', 'MactypeEnum', 
                [], [], 
                '''                MAC Type of an interface.
                ''',
                'mactype',
                'ietf-mac', False),
            _MetaInfoClassMember('outIfName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outbound interface name.
                ''',
                'outifname',
                'ietf-mac', False),
            _MetaInfoClassMember('outIfType', REFERENCE_ENUM_CLASS, 'MacoutiftypeEnum' , 'ydk.models.ietf.ietf_mac', 'MacoutiftypeEnum', 
                [], [], 
                '''                Outbound interface type.
                ''',
                'outiftype',
                'ietf-mac', False),
            _MetaInfoClassMember('peerIp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer IP address.
                ''',
                'peerip',
                'ietf-mac', False, [
                    _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP address.
                        ''',
                        'peerip',
                        'ietf-mac', False),
                    _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP address.
                        ''',
                        'peerip',
                        'ietf-mac', False),
                ]),
            _MetaInfoClassMember('pevid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Outer VLAN tag.
                ''',
                'pevid',
                'ietf-mac', False),
            _MetaInfoClassMember('pwEncap', REFERENCE_ENUM_CLASS, 'MacpwencaptypeEnum' , 'ydk.models.ietf.ietf_mac', 'MacpwencaptypeEnum', 
                [], [], 
                '''                PW encapsulation type.
                ''',
                'pwencap',
                'ietf-mac', False),
            _MetaInfoClassMember('pwId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                PW ID.
                ''',
                'pwid',
                'ietf-mac', False),
            _MetaInfoClassMember('pwName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                PW Name.
                ''',
                'pwname',
                'ietf-mac', False),
            _MetaInfoClassMember('vlanifName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VLANIF interface.
                ''',
                'vlanifname',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiFdb',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsifdbs' : {
        'meta_info' : _MetaInfoClass('Mac.Vsifdbs',
            False, 
            [
            _MetaInfoClassMember('vsiFdb', REFERENCE_LIST, 'Vsifdb' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsifdbs.Vsifdb', 
                [], [], 
                '''                VSI Forwarding entry.
                ''',
                'vsifdb',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiFdbs',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsifdbdynamics.Vsifdbdynamic' : {
        'meta_info' : _MetaInfoClass('Mac.Vsifdbdynamics.Vsifdbdynamic',
            False, 
            [
            _MetaInfoClassMember('macAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address in the format of H-H-H.
                ''',
                'macaddress',
                'ietf-mac', True),
            _MetaInfoClassMember('outIfName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outbound interface name.
                ''',
                'outifname',
                'ietf-mac', True),
            _MetaInfoClassMember('slotId', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Slot ID.
                ''',
                'slotid',
                'ietf-mac', True),
            _MetaInfoClassMember('vlanid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4094')], [], 
                '''                VLAN ID.
                ''',
                'vlanid',
                'ietf-mac', True),
            _MetaInfoClassMember('vsiName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                VSI Name.
                ''',
                'vsiname',
                'ietf-mac', True),
            _MetaInfoClassMember('cevid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Inner VLAN tag.
                ''',
                'cevid',
                'ietf-mac', False),
            _MetaInfoClassMember('isIMac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ingress MAC.
                ''',
                'isimac',
                'ietf-mac', False),
            _MetaInfoClassMember('macType', REFERENCE_ENUM_CLASS, 'MactypeEnum' , 'ydk.models.ietf.ietf_mac', 'MactypeEnum', 
                [], [], 
                '''                MAC Type of an interface.
                ''',
                'mactype',
                'ietf-mac', False),
            _MetaInfoClassMember('outIfType', REFERENCE_ENUM_CLASS, 'MacoutiftypeEnum' , 'ydk.models.ietf.ietf_mac', 'MacoutiftypeEnum', 
                [], [], 
                '''                Outbound interface type.
                ''',
                'outiftype',
                'ietf-mac', False),
            _MetaInfoClassMember('peerIp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer IP address.
                ''',
                'peerip',
                'ietf-mac', False, [
                    _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP address.
                        ''',
                        'peerip',
                        'ietf-mac', False),
                    _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP address.
                        ''',
                        'peerip',
                        'ietf-mac', False),
                ]),
            _MetaInfoClassMember('pevid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Outer VLAN tag.
                ''',
                'pevid',
                'ietf-mac', False),
            _MetaInfoClassMember('pwEncap', REFERENCE_ENUM_CLASS, 'MacpwencaptypeEnum' , 'ydk.models.ietf.ietf_mac', 'MacpwencaptypeEnum', 
                [], [], 
                '''                PW encapsulation type.
                ''',
                'pwencap',
                'ietf-mac', False),
            _MetaInfoClassMember('pwId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                PW ID.
                ''',
                'pwid',
                'ietf-mac', False),
            _MetaInfoClassMember('pwName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                PW Name.
                ''',
                'pwname',
                'ietf-mac', False),
            _MetaInfoClassMember('vlanifName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VLANIF interface.
                ''',
                'vlanifname',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiFdbDynamic',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsifdbdynamics' : {
        'meta_info' : _MetaInfoClass('Mac.Vsifdbdynamics',
            False, 
            [
            _MetaInfoClassMember('vsiFdbDynamic', REFERENCE_LIST, 'Vsifdbdynamic' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsifdbdynamics.Vsifdbdynamic', 
                [], [], 
                '''                VSI Forwarding Table on Slot.
                ''',
                'vsifdbdynamic',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiFdbDynamics',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Bdfdbs.Bdfdb' : {
        'meta_info' : _MetaInfoClass('Mac.Bdfdbs.Bdfdb',
            False, 
            [
            _MetaInfoClassMember('bdId', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                ID of a bridge domain.
                ''',
                'bdid',
                'ietf-mac', True),
            _MetaInfoClassMember('macAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of a bridge domain.
                ''',
                'macaddress',
                'ietf-mac', True),
            _MetaInfoClassMember('slotId', ATTRIBUTE, 'str' , None, None, 
                [(1, 50)], [], 
                '''                Slot number.
                ''',
                'slotid',
                'ietf-mac', True),
            _MetaInfoClassMember('ceDefault', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                CE default VLAN.
                ''',
                'cedefault',
                'ietf-mac', False),
            _MetaInfoClassMember('cevid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Inner VLAN tag.
                ''',
                'cevid',
                'ietf-mac', False),
            _MetaInfoClassMember('learnedPeriod', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967294')], [], 
                '''                Dynamic MAC Holding Time.
                ''',
                'learnedperiod',
                'ietf-mac', False),
            _MetaInfoClassMember('macType', REFERENCE_ENUM_CLASS, 'MactypeEnum' , 'ydk.models.ietf.ietf_mac', 'MactypeEnum', 
                [], [], 
                '''                MAC address type of a bridge domain.
                ''',
                'mactype',
                'ietf-mac', False),
            _MetaInfoClassMember('outIfName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outbound interface name.
                ''',
                'outifname',
                'ietf-mac', False),
            _MetaInfoClassMember('peDefault', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PE default VLAN.
                ''',
                'pedefault',
                'ietf-mac', False),
            _MetaInfoClassMember('unTag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Packets without VLAN tags.
                ''',
                'untag',
                'ietf-mac', False),
            _MetaInfoClassMember('vid', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Outer VLAN tag.
                ''',
                'vid',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'bdFdb',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Bdfdbs' : {
        'meta_info' : _MetaInfoClass('Mac.Bdfdbs',
            False, 
            [
            _MetaInfoClassMember('bdFdb', REFERENCE_LIST, 'Bdfdb' , 'ydk.models.ietf.ietf_mac', 'Mac.Bdfdbs.Bdfdb', 
                [], [], 
                '''                BD forwarding entry.
                ''',
                'bdfdb',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'bdFdbs',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Maclimitrules.Maclimitrule' : {
        'meta_info' : _MetaInfoClass('Mac.Maclimitrules.Maclimitrule',
            False, 
            [
            _MetaInfoClassMember('ruleName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                Global MAC address learning limit rule name.
                ''',
                'rulename',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Discard or forward after the number of learned MAC 
                addresses reaches the maximum number.
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of 
                learned MAC addresses reaches the maximum number.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '131072')], [], 
                '''                Maximum number of MAC addresses that can be learned.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval at which MAC addresses are learned.
                ''',
                'rate',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'macLimitRule',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Maclimitrules' : {
        'meta_info' : _MetaInfoClass('Mac.Maclimitrules',
            False, 
            [
            _MetaInfoClassMember('macLimitRule', REFERENCE_LIST, 'Maclimitrule' , 'ydk.models.ietf.ietf_mac', 'Mac.Maclimitrules.Maclimitrule', 
                [], [], 
                '''                Global MAC address learning limit.
                ''',
                'maclimitrule',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'macLimitRules',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanmaclimits.Vlanmaclimit' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanmaclimits.Vlanmaclimit',
            False, 
            [
            _MetaInfoClassMember('vlanId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                VLAN ID.
                ''',
                'vlanid',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Discard or forward after the number of learned MAC 
                addresses reaches the maximum number in a VLAN.
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of learned 
                MAC addresses reaches the maximum number in a VLAN.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '130048')], [], 
                '''                Maximum number of MAC addresses that can be learned 
                in a VLAN.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval at which MAC addresses are learned in a VLAN.
                ''',
                'rate',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vlanMacLimit',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vlanmaclimits' : {
        'meta_info' : _MetaInfoClass('Mac.Vlanmaclimits',
            False, 
            [
            _MetaInfoClassMember('vlanMacLimit', REFERENCE_LIST, 'Vlanmaclimit' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanmaclimits.Vlanmaclimit', 
                [], [], 
                '''                VLAN MAC address limit.
                ''',
                'vlanmaclimit',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vlanMacLimits',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsimaclimits.Vsimaclimit' : {
        'meta_info' : _MetaInfoClass('Mac.Vsimaclimits.Vsimaclimit',
            False, 
            [
            _MetaInfoClassMember('vsiName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                VSI name.
                ''',
                'vsiname',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Discard or forward after the number of learned MAC 
                addresses reaches the maximum number in a VSI.
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of learned 
                MAC addresses reaches the maximum number in a VSI.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('downThreshold', ATTRIBUTE, 'int' , None, None, 
                [('60', '100')], [], 
                '''                Upper limit for the number of MAC addresses.
                ''',
                'downthreshold',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '524288')], [], 
                '''                Maximum number of MAC addresses that can be learned in a 
                VSI.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval at which MAC addresses are learned in a VSI.
                ''',
                'rate',
                'ietf-mac', False),
            _MetaInfoClassMember('upThreshold', ATTRIBUTE, 'int' , None, None, 
                [('80', '100')], [], 
                '''                Upper limit for the number of MAC addresses.
                ''',
                'upthreshold',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiMacLimit',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Vsimaclimits' : {
        'meta_info' : _MetaInfoClass('Mac.Vsimaclimits',
            False, 
            [
            _MetaInfoClassMember('vsiMacLimit', REFERENCE_LIST, 'Vsimaclimit' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsimaclimits.Vsimaclimit', 
                [], [], 
                '''                VSI MAC address limit.
                ''',
                'vsimaclimit',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'vsiMacLimits',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Bdmaclimits.Bdmaclimit' : {
        'meta_info' : _MetaInfoClass('Mac.Bdmaclimits.Bdmaclimit',
            False, 
            [
            _MetaInfoClassMember('bdId', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Specifies the ID of a bridge domain.
                ''',
                'bdid',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Forward or discard the packet.
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of learned 
                MAC addresses reaches the maximum number.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '130048')], [], 
                '''                Maximum number of MAC addresses that can be learned in a 
                BD.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval at which MAC addresses are learned in a BD.
                ''',
                'rate',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'bdMacLimit',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Bdmaclimits' : {
        'meta_info' : _MetaInfoClass('Mac.Bdmaclimits',
            False, 
            [
            _MetaInfoClassMember('bdMacLimit', REFERENCE_LIST, 'Bdmaclimit' , 'ydk.models.ietf.ietf_mac', 'Mac.Bdmaclimits.Bdmaclimit', 
                [], [], 
                '''                BD MAC address limit.
                ''',
                'bdmaclimit',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'bdMacLimits',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Ifmaclimits.Ifmaclimit' : {
        'meta_info' : _MetaInfoClass('Mac.Ifmaclimits.Ifmaclimit',
            False, 
            [
            _MetaInfoClassMember('ifName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name.
                ''',
                'ifname',
                'ietf-mac', True),
            _MetaInfoClassMember('limitType', REFERENCE_ENUM_CLASS, 'LimittypeEnum' , 'ydk.models.ietf.ietf_mac', 'LimittypeEnum', 
                [], [], 
                '''                Interface MAC limit type.
                ''',
                'limittype',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Discard or forward after the number of learned MAC 
                addresses reaches the maximum number on an interface
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of learned 
                MAC addresses reaches the maximum number on an interface.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '131072')], [], 
                '''                Maximum number of MAC addresses that can be learned 
                on an interface.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval (ms) at which MAC addresses are learned on 
                an interface.
                ''',
                'rate',
                'ietf-mac', False),
            _MetaInfoClassMember('ruleName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                Rule name.
                ''',
                'rulename',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'ifMacLimit',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Ifmaclimits' : {
        'meta_info' : _MetaInfoClass('Mac.Ifmaclimits',
            False, 
            [
            _MetaInfoClassMember('ifMacLimit', REFERENCE_LIST, 'Ifmaclimit' , 'ydk.models.ietf.ietf_mac', 'Mac.Ifmaclimits.Ifmaclimit', 
                [], [], 
                '''                Interface MAC address limit.
                ''',
                'ifmaclimit',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'ifMacLimits',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Ifvlanmaclimits.Ifvlanmaclimit' : {
        'meta_info' : _MetaInfoClass('Mac.Ifvlanmaclimits.Ifvlanmaclimit',
            False, 
            [
            _MetaInfoClassMember('ifName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of an interface. 
                ''',
                'ifname',
                'ietf-mac', True),
            _MetaInfoClassMember('limitType', REFERENCE_ENUM_CLASS, 'LimittypeEnum' , 'ydk.models.ietf.ietf_mac', 'LimittypeEnum', 
                [], [], 
                '''                Interface MAC limit type.
                ''',
                'limittype',
                'ietf-mac', True),
            _MetaInfoClassMember('vlanBegin', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Start VLAN ID.
                ''',
                'vlanbegin',
                'ietf-mac', True),
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MaclimitforwardEnum' , 'ydk.models.ietf.ietf_mac', 'MaclimitforwardEnum', 
                [], [], 
                '''                Discard or forward the packet.
                ''',
                'action',
                'ietf-mac', False),
            _MetaInfoClassMember('alarm', REFERENCE_ENUM_CLASS, 'MacenablestatusEnum' , 'ydk.models.ietf.ietf_mac', 'MacenablestatusEnum', 
                [], [], 
                '''                Whether an alarm is generated after the number of learned 
                MAC addresses reaches the maximum number.
                ''',
                'alarm',
                'ietf-mac', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '131072')], [], 
                '''                Maximum number of MAC addresses that can be learned on
                an interface.
                ''',
                'maximum',
                'ietf-mac', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Interval (ms) at which MAC addresses are learned on 
                an interface.
                ''',
                'rate',
                'ietf-mac', False),
            _MetaInfoClassMember('ruleName', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                Rule name.
                ''',
                'rulename',
                'ietf-mac', False),
            _MetaInfoClassMember('vlanEnd', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                End VLAN ID.
                ''',
                'vlanend',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'ifVlanMacLimit',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac.Ifvlanmaclimits' : {
        'meta_info' : _MetaInfoClass('Mac.Ifvlanmaclimits',
            False, 
            [
            _MetaInfoClassMember('ifVlanMacLimit', REFERENCE_LIST, 'Ifvlanmaclimit' , 'ydk.models.ietf.ietf_mac', 'Mac.Ifvlanmaclimits.Ifvlanmaclimit', 
                [], [], 
                '''                Interface + VLAN MAC address limit.
                ''',
                'ifvlanmaclimit',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'ifVlanMacLimits',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
    'Mac' : {
        'meta_info' : _MetaInfoClass('Mac',
            False, 
            [
            _MetaInfoClassMember('bdFdbs', REFERENCE_CLASS, 'Bdfdbs' , 'ydk.models.ietf.ietf_mac', 'Mac.Bdfdbs', 
                [], [], 
                '''                BD forwarding entries.
                ''',
                'bdfdbs',
                'ietf-mac', False),
            _MetaInfoClassMember('bdMacLimits', REFERENCE_CLASS, 'Bdmaclimits' , 'ydk.models.ietf.ietf_mac', 'Mac.Bdmaclimits', 
                [], [], 
                '''                BD MAC address limit list.
                ''',
                'bdmaclimits',
                'ietf-mac', False),
            _MetaInfoClassMember('globalAttribute', REFERENCE_CLASS, 'Globalattribute' , 'ydk.models.ietf.ietf_mac', 'Mac.Globalattribute', 
                [], [], 
                '''                MAC global attribute.
                ''',
                'globalattribute',
                'ietf-mac', False),
            _MetaInfoClassMember('ifMacLimits', REFERENCE_CLASS, 'Ifmaclimits' , 'ydk.models.ietf.ietf_mac', 'Mac.Ifmaclimits', 
                [], [], 
                '''                Interface MAC address limit list.
                ''',
                'ifmaclimits',
                'ietf-mac', False),
            _MetaInfoClassMember('ifVlanMacLimits', REFERENCE_CLASS, 'Ifvlanmaclimits' , 'ydk.models.ietf.ietf_mac', 'Mac.Ifvlanmaclimits', 
                [], [], 
                '''                Interface + VLAN MAC address limit list.
                ''',
                'ifvlanmaclimits',
                'ietf-mac', False),
            _MetaInfoClassMember('macLimitRules', REFERENCE_CLASS, 'Maclimitrules' , 'ydk.models.ietf.ietf_mac', 'Mac.Maclimitrules', 
                [], [], 
                '''                Global MAC address learning limit rule.
                ''',
                'maclimitrules',
                'ietf-mac', False),
            _MetaInfoClassMember('vlanFdbs', REFERENCE_CLASS, 'Vlanfdbs' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanfdbs', 
                [], [], 
                '''                VLAN forwarding table.
                ''',
                'vlanfdbs',
                'ietf-mac', False),
            _MetaInfoClassMember('vlanMacLimits', REFERENCE_CLASS, 'Vlanmaclimits' , 'ydk.models.ietf.ietf_mac', 'Mac.Vlanmaclimits', 
                [], [], 
                '''                VLAN MAC address limit list.
                ''',
                'vlanmaclimits',
                'ietf-mac', False),
            _MetaInfoClassMember('vsiFdbDynamics', REFERENCE_CLASS, 'Vsifdbdynamics' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsifdbdynamics', 
                [], [], 
                '''                VSI Forwarding Table on Slot.
                ''',
                'vsifdbdynamics',
                'ietf-mac', False),
            _MetaInfoClassMember('vsiFdbs', REFERENCE_CLASS, 'Vsifdbs' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsifdbs', 
                [], [], 
                '''                VSI forwarding table.
                ''',
                'vsifdbs',
                'ietf-mac', False),
            _MetaInfoClassMember('vsiMacLimits', REFERENCE_CLASS, 'Vsimaclimits' , 'ydk.models.ietf.ietf_mac', 'Mac.Vsimaclimits', 
                [], [], 
                '''                VSI MAC address limit list.
                ''',
                'vsimaclimits',
                'ietf-mac', False),
            ],
            'ietf-mac',
            'mac',
            _yang_ns._namespaces['ietf-mac'],
        'ydk.models.ietf.ietf_mac'
        ),
    },
}
_meta_table['Mac.Vlanfdbs.Vlanfdb.Outpeerips.Outpeerip']['meta_info'].parent =_meta_table['Mac.Vlanfdbs.Vlanfdb.Outpeerips']['meta_info']
_meta_table['Mac.Vlanfdbs.Vlanfdb.Outpeerips']['meta_info'].parent =_meta_table['Mac.Vlanfdbs.Vlanfdb']['meta_info']
_meta_table['Mac.Vlanfdbs.Vlanfdb']['meta_info'].parent =_meta_table['Mac.Vlanfdbs']['meta_info']
_meta_table['Mac.Vsifdbs.Vsifdb']['meta_info'].parent =_meta_table['Mac.Vsifdbs']['meta_info']
_meta_table['Mac.Vsifdbdynamics.Vsifdbdynamic']['meta_info'].parent =_meta_table['Mac.Vsifdbdynamics']['meta_info']
_meta_table['Mac.Bdfdbs.Bdfdb']['meta_info'].parent =_meta_table['Mac.Bdfdbs']['meta_info']
_meta_table['Mac.Maclimitrules.Maclimitrule']['meta_info'].parent =_meta_table['Mac.Maclimitrules']['meta_info']
_meta_table['Mac.Vlanmaclimits.Vlanmaclimit']['meta_info'].parent =_meta_table['Mac.Vlanmaclimits']['meta_info']
_meta_table['Mac.Vsimaclimits.Vsimaclimit']['meta_info'].parent =_meta_table['Mac.Vsimaclimits']['meta_info']
_meta_table['Mac.Bdmaclimits.Bdmaclimit']['meta_info'].parent =_meta_table['Mac.Bdmaclimits']['meta_info']
_meta_table['Mac.Ifmaclimits.Ifmaclimit']['meta_info'].parent =_meta_table['Mac.Ifmaclimits']['meta_info']
_meta_table['Mac.Ifvlanmaclimits.Ifvlanmaclimit']['meta_info'].parent =_meta_table['Mac.Ifvlanmaclimits']['meta_info']
_meta_table['Mac.Globalattribute']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Vlanfdbs']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Vsifdbs']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Vsifdbdynamics']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Bdfdbs']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Maclimitrules']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Vlanmaclimits']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Vsimaclimits']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Bdmaclimits']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Ifmaclimits']['meta_info'].parent =_meta_table['Mac']['meta_info']
_meta_table['Mac.Ifvlanmaclimits']['meta_info'].parent =_meta_table['Mac']['meta_info']
