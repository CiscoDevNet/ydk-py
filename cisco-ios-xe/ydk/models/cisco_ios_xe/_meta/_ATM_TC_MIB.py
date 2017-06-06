


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AtmconncasttypeEnum' : _MetaInfoEnum('AtmconncasttypeEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'p2p':'p2p',
            'p2mpRoot':'p2mpRoot',
            'p2mpLeaf':'p2mpLeaf',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmconnkindEnum' : _MetaInfoEnum('AtmconnkindEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'pvc':'pvc',
            'svcIncoming':'svcIncoming',
            'svcOutgoing':'svcOutgoing',
            'spvcInitiator':'spvcInitiator',
            'spvcTarget':'spvcTarget',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmvorxadminstatusEnum' : _MetaInfoEnum('AtmvorxadminstatusEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmservicecategoryEnum' : _MetaInfoEnum('AtmservicecategoryEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'other':'other',
            'cbr':'cbr',
            'rtVbr':'rtVbr',
            'nrtVbr':'nrtVbr',
            'abr':'abr',
            'ubr':'ubr',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmvorxoperstatusEnum' : _MetaInfoEnum('AtmvorxoperstatusEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'up':'up',
            'down':'down',
            'unknown':'unknown',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtminterfacetypeEnum' : _MetaInfoEnum('AtminterfacetypeEnum', 'ydk.models.cisco_ios_xe.ATM_TC_MIB',
        {
            'other':'other',
            'autoConfig':'autoConfig',
            'ituDss2':'ituDss2',
            'atmfUni3Dot0':'atmfUni3Dot0',
            'atmfUni3Dot1':'atmfUni3Dot1',
            'atmfUni4Dot0':'atmfUni4Dot0',
            'atmfIispUni3Dot0':'atmfIispUni3Dot0',
            'atmfIispUni3Dot1':'atmfIispUni3Dot1',
            'atmfIispUni4Dot0':'atmfIispUni4Dot0',
            'atmfPnni1Dot0':'atmfPnni1Dot0',
            'atmfBici2Dot0':'atmfBici2Dot0',
            'atmfUniPvcOnly':'atmfUniPvcOnly',
            'atmfNniPvcOnly':'atmfNniPvcOnly',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmclptransparentscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclptransparentscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTransparentScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclpnotaggingmcrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclpnotaggingmcrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingMcr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnoclpnoscrcdvtIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnoclpnoscrcdvtIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpNoScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclptaggingscrcdvtIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclptaggingscrcdvtIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclpnotaggingscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclpnotaggingscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnoclpscrcdvtIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnoclpscrcdvtIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnotrafficdescriptorIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnotrafficdescriptorIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoTrafficDescriptor',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclptransparentnoscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclptransparentnoscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTransparentNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclptaggingscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclptaggingscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnoclpnoscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnoclpnoscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnoclpscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnoclpscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclpnotaggingnoscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclpnotaggingnoscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclptaggingnoscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclptaggingnoscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmclpnotaggingscrcdvtIdentity' : {
        'meta_info' : _MetaInfoClass('AtmclpnotaggingscrcdvtIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
    'AtmnoclptaggingnoscrIdentity' : {
        'meta_info' : _MetaInfoClass('AtmnoclptaggingnoscrIdentity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.cisco_ios_xe.ATM_TC_MIB'
        ),
    },
}
