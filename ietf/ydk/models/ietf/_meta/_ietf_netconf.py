


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EditOperationTypeEnum' : _MetaInfoEnum('EditOperationTypeEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'merge':'merge',
            'replace':'replace',
            'create':'create',
            'delete':'delete',
            'remove':'remove',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'ErrorTagTypeEnum' : _MetaInfoEnum('ErrorTagTypeEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'in-use':'in_use',
            'invalid-value':'invalid_value',
            'too-big':'too_big',
            'missing-attribute':'missing_attribute',
            'bad-attribute':'bad_attribute',
            'unknown-attribute':'unknown_attribute',
            'missing-element':'missing_element',
            'bad-element':'bad_element',
            'unknown-element':'unknown_element',
            'unknown-namespace':'unknown_namespace',
            'access-denied':'access_denied',
            'lock-denied':'lock_denied',
            'resource-denied':'resource_denied',
            'rollback-failed':'rollback_failed',
            'data-exists':'data_exists',
            'data-missing':'data_missing',
            'operation-not-supported':'operation_not_supported',
            'operation-failed':'operation_failed',
            'partial-operation':'partial_operation',
            'malformed-message':'malformed_message',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'ErrorSeverityTypeEnum' : _MetaInfoEnum('ErrorSeverityTypeEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'error':'error',
            'warning':'warning',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'GetConfigRpc.Input.Source' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc.Input.Source',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config source.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config source.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config source.
                This is optional-to-implement on the server because
                not all servers will support filtering for this
                datastore.
                ''',
                'startup',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'source',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetConfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.ietf.ietf_netconf', 'GetConfigRpc.Input.Source', 
                [], [], 
                '''                Particular configuration to retrieve.
                ''',
                'source',
                'ietf-netconf', False),
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Subtree or XPath filter to use.
                ''',
                'filter',
                'ietf-netconf', False),
            _MetaInfoClassMember('with-defaults', REFERENCE_ENUM_CLASS, 'WithDefaultsModeEnum' , 'ydk.models.ietf.ietf_netconf_with_defaults', 'WithDefaultsModeEnum', 
                [], [], 
                '''                The explicit defaults processing mode requested.
                ''',
                'with_defaults',
                'ietf-netconf-with-defaults', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetConfigRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc.Output',
            False, 
            [
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Copy of the source datastore subset that matched
                the filter criteria (if any).  An empty data container
                indicates that the request did not produce any results.
                ''',
                'data',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'output',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetConfigRpc' : {
        'meta_info' : _MetaInfoClass('GetConfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'GetConfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_netconf', 'GetConfigRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'get-config',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'EditConfigRpc.Input.Target' : {
        'meta_info' : _MetaInfoClass('EditConfigRpc.Input.Target',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config target.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config source.
                ''',
                'running',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'target',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'EditConfigRpc.Input.DefaultOperationEnum' : _MetaInfoEnum('DefaultOperationEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'merge':'merge',
            'replace':'replace',
            'none':'none',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'EditConfigRpc.Input.ErrorOptionEnum' : _MetaInfoEnum('ErrorOptionEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'stop-on-error':'stop_on_error',
            'continue-on-error':'continue_on_error',
            'rollback-on-error':'rollback_on_error',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'EditConfigRpc.Input.TestOptionEnum' : _MetaInfoEnum('TestOptionEnum', 'ydk.models.ietf.ietf_netconf',
        {
            'test-then-set':'test_then_set',
            'set':'set',
            'test-only':'test_only',
        }, 'ietf-netconf', _yang_ns._namespaces['ietf-netconf']),
    'EditConfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('EditConfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_netconf', 'EditConfigRpc.Input.Target', 
                [], [], 
                '''                Particular configuration to edit.
                ''',
                'target',
                'ietf-netconf', False),
            _MetaInfoClassMember('default-operation', REFERENCE_ENUM_CLASS, 'DefaultOperationEnum' , 'ydk.models.ietf.ietf_netconf', 'EditConfigRpc.Input.DefaultOperationEnum', 
                [], [], 
                '''                The default operation to use.
                ''',
                'default_operation',
                'ietf-netconf', False),
            _MetaInfoClassMember('test-option', REFERENCE_ENUM_CLASS, 'TestOptionEnum' , 'ydk.models.ietf.ietf_netconf', 'EditConfigRpc.Input.TestOptionEnum', 
                [], [], 
                '''                The test option to use.
                ''',
                'test_option',
                'ietf-netconf', False),
            _MetaInfoClassMember('error-option', REFERENCE_ENUM_CLASS, 'ErrorOptionEnum' , 'ydk.models.ietf.ietf_netconf', 'EditConfigRpc.Input.ErrorOptionEnum', 
                [], [], 
                '''                The error option to use.
                ''',
                'error_option',
                'ietf-netconf', False),
            _MetaInfoClassMember('config', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Inline Config content.
                ''',
                'config',
                'ietf-netconf', False),
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                URL-based config content.
                ''',
                'url',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'EditConfigRpc' : {
        'meta_info' : _MetaInfoClass('EditConfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'EditConfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'edit-config',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CopyConfigRpc.Input.Target' : {
        'meta_info' : _MetaInfoClass('CopyConfigRpc.Input.Target',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config target.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config target.
                This is optional-to-implement on the server.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config target.
                ''',
                'startup',
                'ietf-netconf', False),
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The URL-based configuration is the config target.
                ''',
                'url',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'target',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CopyConfigRpc.Input.Source' : {
        'meta_info' : _MetaInfoClass('CopyConfigRpc.Input.Source',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config source.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config source.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config source.
                ''',
                'startup',
                'ietf-netconf', False),
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The URL-based configuration is the config source.
                ''',
                'url',
                'ietf-netconf', False),
            _MetaInfoClassMember('config', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Inline Config content: <config> element.  Represents
                an entire configuration datastore, not
                a subset of the running datastore.
                ''',
                'config',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'source',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CopyConfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('CopyConfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_netconf', 'CopyConfigRpc.Input.Target', 
                [], [], 
                '''                Particular configuration to copy to.
                ''',
                'target',
                'ietf-netconf', False),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.ietf.ietf_netconf', 'CopyConfigRpc.Input.Source', 
                [], [], 
                '''                Particular configuration to copy from.
                ''',
                'source',
                'ietf-netconf', False),
            _MetaInfoClassMember('with-defaults', REFERENCE_ENUM_CLASS, 'WithDefaultsModeEnum' , 'ydk.models.ietf.ietf_netconf_with_defaults', 'WithDefaultsModeEnum', 
                [], [], 
                '''                The explicit defaults processing mode requested.
                ''',
                'with_defaults',
                'ietf-netconf-with-defaults', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CopyConfigRpc' : {
        'meta_info' : _MetaInfoClass('CopyConfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'CopyConfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'copy-config',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'DeleteConfigRpc.Input.Target' : {
        'meta_info' : _MetaInfoClass('DeleteConfigRpc.Input.Target',
            False, 
            [
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config target.
                ''',
                'startup',
                'ietf-netconf', False),
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The URL-based configuration is the config target.
                ''',
                'url',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'target',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'DeleteConfigRpc.Input' : {
        'meta_info' : _MetaInfoClass('DeleteConfigRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_netconf', 'DeleteConfigRpc.Input.Target', 
                [], [], 
                '''                Particular configuration to delete.
                ''',
                'target',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'DeleteConfigRpc' : {
        'meta_info' : _MetaInfoClass('DeleteConfigRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'DeleteConfigRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'delete-config',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'LockRpc.Input.Target' : {
        'meta_info' : _MetaInfoClass('LockRpc.Input.Target',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config target.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config target.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config target.
                ''',
                'startup',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'target',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'LockRpc.Input' : {
        'meta_info' : _MetaInfoClass('LockRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_netconf', 'LockRpc.Input.Target', 
                [], [], 
                '''                Particular configuration to lock.
                ''',
                'target',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'LockRpc' : {
        'meta_info' : _MetaInfoClass('LockRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'LockRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'lock',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'UnlockRpc.Input.Target' : {
        'meta_info' : _MetaInfoClass('UnlockRpc.Input.Target',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config target.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config target.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config target.
                ''',
                'startup',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'target',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'UnlockRpc.Input' : {
        'meta_info' : _MetaInfoClass('UnlockRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_netconf', 'UnlockRpc.Input.Target', 
                [], [], 
                '''                Particular configuration to unlock.
                ''',
                'target',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'UnlockRpc' : {
        'meta_info' : _MetaInfoClass('UnlockRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'UnlockRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'unlock',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetRpc.Input',
            False, 
            [
            _MetaInfoClassMember('filter', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                This parameter specifies the portion of the system
                configuration and state data to retrieve.
                ''',
                'filter',
                'ietf-netconf', False),
            _MetaInfoClassMember('with-defaults', REFERENCE_ENUM_CLASS, 'WithDefaultsModeEnum' , 'ydk.models.ietf.ietf_netconf_with_defaults', 'WithDefaultsModeEnum', 
                [], [], 
                '''                The explicit defaults processing mode requested.
                ''',
                'with_defaults',
                'ietf-netconf-with-defaults', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetRpc.Output',
            False, 
            [
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Copy of the running datastore subset and/or state
                data that matched the filter criteria (if any).
                An empty data container indicates that the request did not
                produce any results.
                ''',
                'data',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'output',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'GetRpc' : {
        'meta_info' : _MetaInfoClass('GetRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'GetRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_netconf', 'GetRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'get',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CloseSessionRpc' : {
        'meta_info' : _MetaInfoClass('CloseSessionRpc',
            False, 
            [
            ],
            'ietf-netconf',
            'close-session',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'KillSessionRpc.Input' : {
        'meta_info' : _MetaInfoClass('KillSessionRpc.Input',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Particular session to kill.
                ''',
                'session_id',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'KillSessionRpc' : {
        'meta_info' : _MetaInfoClass('KillSessionRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'KillSessionRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'kill-session',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CommitRpc.Input' : {
        'meta_info' : _MetaInfoClass('CommitRpc.Input',
            False, 
            [
            _MetaInfoClassMember('confirmed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Requests a confirmed commit.
                ''',
                'confirmed',
                'ietf-netconf', False),
            _MetaInfoClassMember('confirm-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The timeout interval for a confirmed commit.
                ''',
                'confirm_timeout',
                'ietf-netconf', False),
            _MetaInfoClassMember('persist', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter is used to make a confirmed commit
                persistent.  A persistent confirmed commit is not aborted
                if the NETCONF session terminates.  The only way to abort
                a persistent confirmed commit is to let the timer expire,
                or to use the <cancel-commit> operation.
                
                The value of this parameter is a token that must be given
                in the 'persist-id' parameter of <commit> or
                <cancel-commit> operations in order to confirm or cancel
                the persistent confirmed commit.
                
                The token should be a random string.
                ''',
                'persist',
                'ietf-netconf', False),
            _MetaInfoClassMember('persist-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter is given in order to commit a persistent
                confirmed commit.  The value must be equal to the value
                given in the 'persist' parameter to the <commit> operation.
                If it does not match, the operation fails with an
                'invalid-value' error.
                ''',
                'persist_id',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CommitRpc' : {
        'meta_info' : _MetaInfoClass('CommitRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'CommitRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'commit',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'DiscardChangesRpc' : {
        'meta_info' : _MetaInfoClass('DiscardChangesRpc',
            False, 
            [
            ],
            'ietf-netconf',
            'discard-changes',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CancelCommitRpc.Input' : {
        'meta_info' : _MetaInfoClass('CancelCommitRpc.Input',
            False, 
            [
            _MetaInfoClassMember('persist-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This parameter is given in order to cancel a persistent
                confirmed commit.  The value must be equal to the value
                given in the 'persist' parameter to the <commit> operation.
                If it does not match, the operation fails with an
                'invalid-value' error.
                ''',
                'persist_id',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'CancelCommitRpc' : {
        'meta_info' : _MetaInfoClass('CancelCommitRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'CancelCommitRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'cancel-commit',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'ValidateRpc.Input.Source' : {
        'meta_info' : _MetaInfoClass('ValidateRpc.Input.Source',
            False, 
            [
            _MetaInfoClassMember('candidate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The candidate configuration is the config source.
                ''',
                'candidate',
                'ietf-netconf', False),
            _MetaInfoClassMember('running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The running configuration is the config source.
                ''',
                'running',
                'ietf-netconf', False),
            _MetaInfoClassMember('startup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The startup configuration is the config source.
                ''',
                'startup',
                'ietf-netconf', False),
            _MetaInfoClassMember('url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The URL-based configuration is the config source.
                ''',
                'url',
                'ietf-netconf', False),
            _MetaInfoClassMember('config', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Inline Config content: <config> element.  Represents
                an entire configuration datastore, not
                a subset of the running datastore.
                ''',
                'config',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'source',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'ValidateRpc.Input' : {
        'meta_info' : _MetaInfoClass('ValidateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.ietf.ietf_netconf', 'ValidateRpc.Input.Source', 
                [], [], 
                '''                Particular configuration to validate.
                ''',
                'source',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'input',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
    'ValidateRpc' : {
        'meta_info' : _MetaInfoClass('ValidateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf', 'ValidateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf', False),
            ],
            'ietf-netconf',
            'validate',
            _yang_ns._namespaces['ietf-netconf'],
        'ydk.models.ietf.ietf_netconf'
        ),
    },
}
_meta_table['GetConfigRpc.Input.Source']['meta_info'].parent =_meta_table['GetConfigRpc.Input']['meta_info']
_meta_table['GetConfigRpc.Input']['meta_info'].parent =_meta_table['GetConfigRpc']['meta_info']
_meta_table['GetConfigRpc.Output']['meta_info'].parent =_meta_table['GetConfigRpc']['meta_info']
_meta_table['EditConfigRpc.Input.Target']['meta_info'].parent =_meta_table['EditConfigRpc.Input']['meta_info']
_meta_table['EditConfigRpc.Input']['meta_info'].parent =_meta_table['EditConfigRpc']['meta_info']
_meta_table['CopyConfigRpc.Input.Target']['meta_info'].parent =_meta_table['CopyConfigRpc.Input']['meta_info']
_meta_table['CopyConfigRpc.Input.Source']['meta_info'].parent =_meta_table['CopyConfigRpc.Input']['meta_info']
_meta_table['CopyConfigRpc.Input']['meta_info'].parent =_meta_table['CopyConfigRpc']['meta_info']
_meta_table['DeleteConfigRpc.Input.Target']['meta_info'].parent =_meta_table['DeleteConfigRpc.Input']['meta_info']
_meta_table['DeleteConfigRpc.Input']['meta_info'].parent =_meta_table['DeleteConfigRpc']['meta_info']
_meta_table['LockRpc.Input.Target']['meta_info'].parent =_meta_table['LockRpc.Input']['meta_info']
_meta_table['LockRpc.Input']['meta_info'].parent =_meta_table['LockRpc']['meta_info']
_meta_table['UnlockRpc.Input.Target']['meta_info'].parent =_meta_table['UnlockRpc.Input']['meta_info']
_meta_table['UnlockRpc.Input']['meta_info'].parent =_meta_table['UnlockRpc']['meta_info']
_meta_table['GetRpc.Input']['meta_info'].parent =_meta_table['GetRpc']['meta_info']
_meta_table['GetRpc.Output']['meta_info'].parent =_meta_table['GetRpc']['meta_info']
_meta_table['KillSessionRpc.Input']['meta_info'].parent =_meta_table['KillSessionRpc']['meta_info']
_meta_table['CommitRpc.Input']['meta_info'].parent =_meta_table['CommitRpc']['meta_info']
_meta_table['CancelCommitRpc.Input']['meta_info'].parent =_meta_table['CancelCommitRpc']['meta_info']
_meta_table['ValidateRpc.Input.Source']['meta_info'].parent =_meta_table['ValidateRpc.Input']['meta_info']
_meta_table['ValidateRpc.Input']['meta_info'].parent =_meta_table['ValidateRpc']['meta_info']
