


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SubscriberManager.Accounting.SendStop' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.SendStop',
            False, 
            [
            _MetaInfoClassMember('setup-failure', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set up failure feature
                ''',
                'setup_failure',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'send-stop',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager.Accounting.Interim.Variation' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.Interim.Variation',
            False, 
            [
            _MetaInfoClassMember('maximum-percentage-variation', ATTRIBUTE, 'int' , None, None, 
                [('0', '50')], [], 
                '''                maximum percentage variation (maximum
                absolute variation is 15 minutes)
                ''',
                'maximum_percentage_variation',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'variation',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager.Accounting.Interim' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting.Interim',
            False, 
            [
            _MetaInfoClassMember('variation', REFERENCE_CLASS, 'Variation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.Interim.Variation', 
                [], [], 
                '''                variation of first session or service interim
                record from configured timeout
                ''',
                'variation',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'interim',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager.Accounting' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Accounting',
            False, 
            [
            _MetaInfoClassMember('interim', REFERENCE_CLASS, 'Interim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.Interim', 
                [], [], 
                '''                interim accounting related
                ''',
                'interim',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('send-stop', REFERENCE_CLASS, 'SendStop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting.SendStop', 
                [], [], 
                '''                Accounting send stop feature
                ''',
                'send_stop',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager.Srg' : {
        'meta_info' : _MetaInfoClass('SubscriberManager.Srg',
            False, 
            [
            _MetaInfoClassMember('sync-account-session-id', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                sync account session id from master to slave
                ''',
                'sync_account_session_id',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'srg',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberManager' : {
        'meta_info' : _MetaInfoClass('SubscriberManager',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Accounting', 
                [], [], 
                '''                iEdge accounting feature
                ''',
                'accounting',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('srg', REFERENCE_CLASS, 'Srg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberManager.Srg', 
                [], [], 
                '''                SRG specific config
                ''',
                'srg',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'subscriber-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberFeaturette.IdentityChange' : {
        'meta_info' : _MetaInfoClass('SubscriberFeaturette.IdentityChange',
            False, 
            [
            _MetaInfoClassMember('identity-change', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                identity change
                ''',
                'identity_change',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                instance of identity-change
                ''',
                'enable',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'identity-change',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubscriberFeaturette' : {
        'meta_info' : _MetaInfoClass('SubscriberFeaturette',
            False, 
            [
            _MetaInfoClassMember('identity-change', REFERENCE_LIST, 'IdentityChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubscriberFeaturette.IdentityChange', 
                [], [], 
                '''                enable identity change processing
                ''',
                'identity_change',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'subscriber-featurette',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'IedgeLicenseManager.Node' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The node id to filter on. For eg., 0/1/CPU0
                ''',
                'node_name',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session limit configured on linecard
                ''',
                'session_limit',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('session-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session threshold configured on linecard
                ''',
                'session_threshold',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'IedgeLicenseManager' : {
        'meta_info' : _MetaInfoClass('IedgeLicenseManager',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'IedgeLicenseManager.Node', 
                [], [], 
                '''                Location. For eg., 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'iedge-license-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubManager.Location.Trace' : {
        'meta_info' : _MetaInfoClass('SubManager.Location.Trace',
            False, 
            [
            _MetaInfoClassMember('trace-level', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Subscriber manager trace level
                ''',
                'trace_level',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'trace',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubManager.Location' : {
        'meta_info' : _MetaInfoClass('SubManager.Location',
            False, 
            [
            _MetaInfoClassMember('location1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Specify location
                ''',
                'location1',
                'Cisco-IOS-XR-iedge4710-cfg', True),
            _MetaInfoClassMember('history', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable history for subscriber manager
                ''',
                'history',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            _MetaInfoClassMember('trace', REFERENCE_CLASS, 'Trace' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubManager.Location.Trace', 
                [], [], 
                '''                Subscriber manager trace
                ''',
                'trace',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'location',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
    'SubManager' : {
        'meta_info' : _MetaInfoClass('SubManager',
            False, 
            [
            _MetaInfoClassMember('location', REFERENCE_LIST, 'Location' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg', 'SubManager.Location', 
                [], [], 
                '''                Select location
                ''',
                'location',
                'Cisco-IOS-XR-iedge4710-cfg', False),
            ],
            'Cisco-IOS-XR-iedge4710-cfg',
            'sub-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-iedge4710-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg'
        ),
    },
}
_meta_table['SubscriberManager.Accounting.Interim.Variation']['meta_info'].parent =_meta_table['SubscriberManager.Accounting.Interim']['meta_info']
_meta_table['SubscriberManager.Accounting.SendStop']['meta_info'].parent =_meta_table['SubscriberManager.Accounting']['meta_info']
_meta_table['SubscriberManager.Accounting.Interim']['meta_info'].parent =_meta_table['SubscriberManager.Accounting']['meta_info']
_meta_table['SubscriberManager.Accounting']['meta_info'].parent =_meta_table['SubscriberManager']['meta_info']
_meta_table['SubscriberManager.Srg']['meta_info'].parent =_meta_table['SubscriberManager']['meta_info']
_meta_table['SubscriberFeaturette.IdentityChange']['meta_info'].parent =_meta_table['SubscriberFeaturette']['meta_info']
_meta_table['IedgeLicenseManager.Node']['meta_info'].parent =_meta_table['IedgeLicenseManager']['meta_info']
_meta_table['SubManager.Location.Trace']['meta_info'].parent =_meta_table['SubManager.Location']['meta_info']
_meta_table['SubManager.Location']['meta_info'].parent =_meta_table['SubManager']['meta_info']
