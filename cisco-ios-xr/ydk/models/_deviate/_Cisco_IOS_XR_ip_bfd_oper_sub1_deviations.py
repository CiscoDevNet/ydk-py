
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.providers._importer import _yang_ns


_deviation_table = {
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteHeadSessionDetails.Ipv4BfDoMplsteHeadSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4BfDoMplsteTailSessionDetails.Ipv4BfDoMplsteTailSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4MultiHopSessionDetails.Ipv4MultiHopSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv4SingleHopSessionDetails.Ipv4SingleHopSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6MultiHopSessionDetails.Ipv6MultiHopSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.Ipv6SingleHopSessionDetails.Ipv6SingleHopSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.LabelSessionDetails.LabelSessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingRxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastErrorTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.SessionDetails.SessionDetail.LspPingInfo.LspPingTxLastTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
    'Bfd.SessionDetails.SessionDetail.MpDownloadState.ChangeTime.seconds' : {
        'deviation_typ' : 'replace',
        'keyword_value' : [
            ('type', 
                _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                    [('0', '4294967295')], [], 
                    '''                    seconds
                    ''',
                    'seconds',
                    'Cisco-IOS-XR-ip-bfd-oper', False),
            ),
        ]
    },
}
