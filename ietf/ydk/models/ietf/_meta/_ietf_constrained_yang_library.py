


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ModuleSetIdentity' : {
        'meta_info' : _MetaInfoClass('ModuleSetIdentity',
            False, 
            [
            ],
            'ietf-constrained-yang-library',
            'module-set',
            _yang_ns._namespaces['ietf-constrained-yang-library'],
        'ydk.models.ietf.ietf_constrained_yang_library'
        ),
    },
    'ModulesState.Module.Deviation' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module.Deviation',
            False, 
            [
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Revision date assigned to this module or submodule.
                A zero-length binary string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-constrained-yang-library', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SID assigned to this module or submodule.
                ''',
                'sid',
                'ietf-constrained-yang-library', True),
            ],
            'ietf-constrained-yang-library',
            'deviation',
            _yang_ns._namespaces['ietf-constrained-yang-library'],
        'ydk.models.ietf.ietf_constrained_yang_library'
        ),
    },
    'ModulesState.Module.Submodule' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module.Submodule',
            False, 
            [
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Revision date assigned to this module or submodule.
                A zero-length binary string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-constrained-yang-library', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SID assigned to this module or submodule.
                ''',
                'sid',
                'ietf-constrained-yang-library', True),
            ],
            'ietf-constrained-yang-library',
            'submodule',
            _yang_ns._namespaces['ietf-constrained-yang-library'],
        'ydk.models.ietf.ietf_constrained_yang_library'
        ),
    },
    'ModulesState.Module.ConformanceTypeEnum' : _MetaInfoEnum('ConformanceTypeEnum', 'ydk.models.ietf.ietf_constrained_yang_library',
        {
            'implement':'implement',
            'import':'import_',
        }, 'ietf-constrained-yang-library', _yang_ns._namespaces['ietf-constrained-yang-library']),
    'ModulesState.Module' : {
        'meta_info' : _MetaInfoClass('ModulesState.Module',
            False, 
            [
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Revision date assigned to this module or submodule.
                A zero-length binary string is used if no revision statement
                is present in the YANG module or submodule.
                ''',
                'revision',
                'ietf-constrained-yang-library', True),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SID assigned to this module or submodule.
                ''',
                'sid',
                'ietf-constrained-yang-library', True),
            _MetaInfoClassMember('conformance-type', REFERENCE_ENUM_CLASS, 'ConformanceTypeEnum' , 'ydk.models.ietf.ietf_constrained_yang_library', 'ModulesState.Module.ConformanceTypeEnum', 
                [], [], 
                '''                Indicates the type of conformance the server is claiming
                for the YANG module identified by this entry.
                ''',
                'conformance_type',
                'ietf-constrained-yang-library', False),
            _MetaInfoClassMember('deviation', REFERENCE_LIST, 'Deviation' , 'ydk.models.ietf.ietf_constrained_yang_library', 'ModulesState.Module.Deviation', 
                [], [], 
                '''                List of YANG deviation modules used by this server
                to modify the conformance of the module associated
                with this entry.  Note that the same module can be
                used for deviations for multiple modules, so the
                same entry MAY appear within multiple 'module' entries.
                
                The deviation module MUST be present in the 'module'
                list, with the same sid and revision values.
                The 'conformance-type' value will be 'implement' for
                the deviation module.
                ''',
                'deviation',
                'ietf-constrained-yang-library', False),
            _MetaInfoClassMember('feature', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                List of YANG features from this module that are
                supported by the server, regardless whether
                they are defined in the module or in any included
                submodule.
                ''',
                'feature',
                'ietf-constrained-yang-library', False),
            _MetaInfoClassMember('submodule', REFERENCE_LIST, 'Submodule' , 'ydk.models.ietf.ietf_constrained_yang_library', 'ModulesState.Module.Submodule', 
                [], [], 
                '''                Each entry represents one submodule within the
                parent module.
                ''',
                'submodule',
                'ietf-constrained-yang-library', False),
            ],
            'ietf-constrained-yang-library',
            'module',
            _yang_ns._namespaces['ietf-constrained-yang-library'],
        'ydk.models.ietf.ietf_constrained_yang_library'
        ),
    },
    'ModulesState' : {
        'meta_info' : _MetaInfoClass('ModulesState',
            False, 
            [
            _MetaInfoClassMember('module', REFERENCE_LIST, 'Module' , 'ydk.models.ietf.ietf_constrained_yang_library', 'ModulesState.Module', 
                [], [], 
                '''                Each entry represents one revision of one module
                currently supported by the server.
                ''',
                'module',
                'ietf-constrained-yang-library', False),
            _MetaInfoClassMember('module-set-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Identifier representing the current set of modules
                and submodules listed in the 'module' list. This
                identifier is server-specific when implemented as
                unit32 or shared between multiple servers when
                implemented as identityref. The server MUST change
                the value of this leaf each time the content of the
                'module' list instance change.
                ''',
                'module_set_id',
                'ietf-constrained-yang-library', False, [
                    _MetaInfoClassMember('module-set-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Identifier representing the current set of modules
                        and submodules listed in the 'module' list. This
                        identifier is server-specific when implemented as
                        unit32 or shared between multiple servers when
                        implemented as identityref. The server MUST change
                        the value of this leaf each time the content of the
                        'module' list instance change.
                        ''',
                        'module_set_id',
                        'ietf-constrained-yang-library', False),
                    _MetaInfoClassMember('module-set-id', REFERENCE_IDENTITY_CLASS, 'ModuleSetIdentity' , 'ydk.models.ietf.ietf_constrained_yang_library', 'ModuleSetIdentity', 
                        [], [], 
                        '''                        Identifier representing the current set of modules
                        and submodules listed in the 'module' list. This
                        identifier is server-specific when implemented as
                        unit32 or shared between multiple servers when
                        implemented as identityref. The server MUST change
                        the value of this leaf each time the content of the
                        'module' list instance change.
                        ''',
                        'module_set_id',
                        'ietf-constrained-yang-library', False),
                ]),
            ],
            'ietf-constrained-yang-library',
            'modules-state',
            _yang_ns._namespaces['ietf-constrained-yang-library'],
        'ydk.models.ietf.ietf_constrained_yang_library'
        ),
    },
}
_meta_table['ModulesState.Module.Deviation']['meta_info'].parent =_meta_table['ModulesState.Module']['meta_info']
_meta_table['ModulesState.Module.Submodule']['meta_info'].parent =_meta_table['ModulesState.Module']['meta_info']
_meta_table['ModulesState.Module']['meta_info'].parent =_meta_table['ModulesState']['meta_info']
