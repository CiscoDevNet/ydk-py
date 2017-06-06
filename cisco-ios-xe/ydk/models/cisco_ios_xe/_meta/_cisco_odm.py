


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ParsernameIdentity' : {
        'meta_info' : _MetaInfoClass('ParsernameIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'parsername',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'BridgedomainIdentity' : {
        'meta_info' : _MetaInfoClass('BridgedomainIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'BridgeDomain',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'MplsforwardingtableIdentity' : {
        'meta_info' : _MetaInfoClass('MplsforwardingtableIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'MPLSForwardingTable',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'MplsstaticbindingIdentity' : {
        'meta_info' : _MetaInfoClass('MplsstaticbindingIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'MPLSStaticBinding',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'IprouteIdentity' : {
        'meta_info' : _MetaInfoClass('IprouteIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'IPRoute',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'BgpIdentity' : {
        'meta_info' : _MetaInfoClass('BgpIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'BGP',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'BfdneighborsIdentity' : {
        'meta_info' : _MetaInfoClass('BfdneighborsIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'BFDNeighbors',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'VirtualserviceIdentity' : {
        'meta_info' : _MetaInfoClass('VirtualserviceIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'VirtualService',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'MplsldpneighborsIdentity' : {
        'meta_info' : _MetaInfoClass('MplsldpneighborsIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'MPLSLDPNeighbors',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'FlowmonitorIdentity' : {
        'meta_info' : _MetaInfoClass('FlowmonitorIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'FlowMonitor',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'PlatformsoftwareIdentity' : {
        'meta_info' : _MetaInfoClass('PlatformsoftwareIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'PlatformSoftware',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'OspfIdentity' : {
        'meta_info' : _MetaInfoClass('OspfIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'OSPF',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'DiffservIdentity' : {
        'meta_info' : _MetaInfoClass('DiffservIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'Diffserv',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
    'EthernetcfmstatsIdentity' : {
        'meta_info' : _MetaInfoClass('EthernetcfmstatsIdentity',
            False, 
            [
            ],
            'cisco-odm',
            'EthernetCFMStats',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_odm'
        ),
    },
}
