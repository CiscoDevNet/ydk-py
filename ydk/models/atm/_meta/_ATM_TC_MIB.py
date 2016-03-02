


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AtmVorXAdminStatus_Enum' : _MetaInfoEnum('AtmVorXAdminStatus_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmServiceCategory_Enum' : _MetaInfoEnum('AtmServiceCategory_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'other':'OTHER',
            'cbr':'CBR',
            'rtVbr':'RTVBR',
            'nrtVbr':'NRTVBR',
            'abr':'ABR',
            'ubr':'UBR',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmInterfaceType_Enum' : _MetaInfoEnum('AtmInterfaceType_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'other':'OTHER',
            'autoConfig':'AUTOCONFIG',
            'ituDss2':'ITUDSS2',
            'atmfUni3Dot0':'ATMFUNI3DOT0',
            'atmfUni3Dot1':'ATMFUNI3DOT1',
            'atmfUni4Dot0':'ATMFUNI4DOT0',
            'atmfIispUni3Dot0':'ATMFIISPUNI3DOT0',
            'atmfIispUni3Dot1':'ATMFIISPUNI3DOT1',
            'atmfIispUni4Dot0':'ATMFIISPUNI4DOT0',
            'atmfPnni1Dot0':'ATMFPNNI1DOT0',
            'atmfBici2Dot0':'ATMFBICI2DOT0',
            'atmfUniPvcOnly':'ATMFUNIPVCONLY',
            'atmfNniPvcOnly':'ATMFNNIPVCONLY',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmConnKind_Enum' : _MetaInfoEnum('AtmConnKind_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'pvc':'PVC',
            'svcIncoming':'SVCINCOMING',
            'svcOutgoing':'SVCOUTGOING',
            'spvcInitiator':'SPVCINITIATOR',
            'spvcTarget':'SPVCTARGET',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmVorXOperStatus_Enum' : _MetaInfoEnum('AtmVorXOperStatus_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'unknown':'UNKNOWN',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmConnCastType_Enum' : _MetaInfoEnum('AtmConnCastType_Enum', 'ydk.models.atm.ATM_TC_MIB',
        {
            'p2p':'P2P',
            'p2mpRoot':'P2MPROOT',
            'p2mpLeaf':'P2MPLEAF',
        }, 'ATM-TC-MIB', _yang_ns._namespaces['ATM-TC-MIB']),
    'AtmClpNoTaggingMcr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpNoTaggingMcr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingMcr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpNoTaggingNoScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpNoTaggingNoScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpNoTaggingScrCdvt_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpNoTaggingScrCdvt_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpNoTaggingScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpNoTaggingScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpNoTaggingScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpTaggingNoScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpTaggingNoScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpTaggingScrCdvt_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpTaggingScrCdvt_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpTaggingScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpTaggingScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTaggingScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpTransparentNoScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpTransparentNoScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTransparentNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmClpTransparentScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmClpTransparentScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmClpTransparentScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoClpNoScrCdvt_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoClpNoScrCdvt_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpNoScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoClpNoScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoClpNoScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoClpScrCdvt_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoClpScrCdvt_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpScrCdvt',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoClpScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoClpScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoClpTaggingNoScr_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoClpTaggingNoScr_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoClpTaggingNoScr',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
    'AtmNoTrafficDescriptor_Identity' : {
        'meta_info' : _MetaInfoClass('AtmNoTrafficDescriptor_Identity',
            False, 
            [
            ],
            'ATM-TC-MIB',
            'atmNoTrafficDescriptor',
            _yang_ns._namespaces['ATM-TC-MIB'],
        'ydk.models.atm.ATM_TC_MIB'
        ),
    },
}
