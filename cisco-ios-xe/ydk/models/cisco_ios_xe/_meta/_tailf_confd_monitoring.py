


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ConfdState.Smp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Smp',
            False, 
            [
            _MetaInfoClassMember('number-of-threads', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of threads used by the daemon.
                ''',
                'number_of_threads',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'smp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Ha.ModeEnum' : _MetaInfoEnum('ModeEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'none':'none',
            'slave':'slave',
            'master':'master',
            'relay-slave':'relay_slave',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Ha' : {
        'meta_info' : _MetaInfoClass('ConfdState.Ha',
            False, 
            [
            _MetaInfoClassMember('connected-slave', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The node identifiers of the currently connected slaves.
                ''',
                'connected_slave',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('master-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The node identifier of this node's parent node.
                This is the HA cluster's master node unless relay slaves
                are used.
                ''',
                'master_node_id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Ha.ModeEnum', 
                [], [], 
                '''                The current HA mode of the node in the HA cluster.
                ''',
                'mode',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The node identifier of this node in the HA cluster.
                ''',
                'node_id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('pending-slave', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The node identifiers of slaves with pending acknowledgement
                of synchronous replication.
                ''',
                'pending_slave',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'ha',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.LoadedDataModels.DataModel.ExportedToEnum' : _MetaInfoEnum('ExportedToEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'netconf':'netconf',
            'cli':'cli',
            'webui':'webui',
            'rest':'rest',
            'snmp':'snmp',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.LoadedDataModels.DataModel' : {
        'meta_info' : _MetaInfoClass('ConfdState.LoadedDataModels.DataModel',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The YANG module name.
                ''',
                'name',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('exported-to', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                A list of the contexts (northbound interfaces) this module
                is exported to.
                ''',
                'exported_to',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('exported-to', REFERENCE_LEAFLIST, 'ConfdState.LoadedDataModels.DataModel.ExportedToEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.LoadedDataModels.DataModel.ExportedToEnum', 
                        [], [], 
                        '''                        A list of the contexts (northbound interfaces) this module
                        is exported to.
                        ''',
                        'exported_to',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('exported-to', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [], 
                        '''                        A list of the contexts (northbound interfaces) this module
                        is exported to.
                        ''',
                        'exported_to',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('exported-to-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                This leaf is present if the module is exported to all
                northbound interfaces.
                ''',
                'exported_to_all',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('namespace', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The YANG module namespace.
                ''',
                'namespace',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The prefix defined in the YANG module.
                ''',
                'prefix',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The YANG module revision.
                ''',
                'revision',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'data-model',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.LoadedDataModels' : {
        'meta_info' : _MetaInfoClass('ConfdState.LoadedDataModels',
            False, 
            [
            _MetaInfoClassMember('data-model', REFERENCE_LIST, 'DataModel' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.LoadedDataModels.DataModel', 
                [], [], 
                '''                This list contains all loaded YANG data modules.
                
                This list is a superset of the 'schema' list defined in
                ietf-netconf-monitoring, which only lists modules exported
                through NETCONF.
                ''',
                'data_model',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'loaded-data-models',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Netconf.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen.Tcp',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Netconf.Listen.Ssh' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen.Ssh',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'ssh',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Netconf.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf.Listen',
            False, 
            [
            _MetaInfoClassMember('ssh', REFERENCE_LIST, 'Ssh' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Netconf.Listen.Ssh', 
                [], [], 
                '''                ''',
                'ssh',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Netconf.Listen.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Netconf' : {
        'meta_info' : _MetaInfoClass('ConfdState.Netconf',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Netconf.Listen', 
                [], [], 
                '''                The transport addresses the NETCONF server is listening on.
                
                Note that other mechanisms can be put in front of the TCP
                addresses below, e.g., an OpenSSH server.  Such mechanisms
                are not known to the daemon and not listed here.
                ''',
                'listen',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'netconf',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Cli.Listen.Ssh' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli.Listen.Ssh',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'ssh',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Cli.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli.Listen',
            False, 
            [
            _MetaInfoClassMember('ssh', REFERENCE_LIST, 'Ssh' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Cli.Listen.Ssh', 
                [], [], 
                '''                ''',
                'ssh',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Cli' : {
        'meta_info' : _MetaInfoClass('ConfdState.Cli',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Cli.Listen', 
                [], [], 
                '''                The transport addresses the CLI server is listening on.
                
                In addition to the SSH addresses listen below, the CLI can
                always be invoked through the daemons IPC port.
                
                Note that other mechanisms can be put in front of the IPC
                port, e.g., an OpenSSH server.  Such mechanisms are not
                known to the daemon and not listed here.
                ''',
                'listen',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'cli',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Webui.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen.Tcp',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Webui.Listen.Ssl' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen.Ssl',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'ssl',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Webui.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui.Listen',
            False, 
            [
            _MetaInfoClassMember('ssl', REFERENCE_LIST, 'Ssl' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Webui.Listen.Ssl', 
                [], [], 
                '''                ''',
                'ssl',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Webui.Listen.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Webui' : {
        'meta_info' : _MetaInfoClass('ConfdState.Webui',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Webui.Listen', 
                [], [], 
                '''                The transport addresses the WebUI server is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'webui',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Rest.Listen.Tcp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen.Tcp',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'tcp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Rest.Listen.Ssl' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen.Ssl',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'ssl',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Rest.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest.Listen',
            False, 
            [
            _MetaInfoClassMember('ssl', REFERENCE_LIST, 'Ssl' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Rest.Listen.Ssl', 
                [], [], 
                '''                ''',
                'ssl',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('tcp', REFERENCE_LIST, 'Tcp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Rest.Listen.Tcp', 
                [], [], 
                '''                ''',
                'tcp',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Rest' : {
        'meta_info' : _MetaInfoClass('ConfdState.Rest',
            False, 
            [
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Rest.Listen', 
                [], [], 
                '''                The transport addresses the REST server is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'rest',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Snmp.Listen.Udp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Listen.Udp',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'port',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'udp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Snmp.Listen' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Listen',
            False, 
            [
            _MetaInfoClassMember('udp', REFERENCE_LIST, 'Udp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Snmp.Listen.Udp', 
                [], [], 
                '''                ''',
                'udp',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'listen',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Snmp.Version' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp.Version',
            False, 
            [
            _MetaInfoClassMember('v1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'v1',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('v2c', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'v2c',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('v3', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'v3',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'version',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Snmp' : {
        'meta_info' : _MetaInfoClass('ConfdState.Snmp',
            False, 
            [
            _MetaInfoClassMember('engine-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]){2}(:([0-9a-fA-F]){2}){4,31}'], 
                '''                The local Engine ID specified as a list of colon-specified
                hexadecimal octets e.g. '4F:4C:41:71'.
                ''',
                'engine_id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('listen', REFERENCE_CLASS, 'Listen' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Snmp.Listen', 
                [], [], 
                '''                The transport addresses the SNMP agent is listening on.
                ''',
                'listen',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('mib', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                MIBs loaded by the SNMP agent.
                ''',
                'mib',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('version', REFERENCE_CLASS, 'Version' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Snmp.Version', 
                [], [], 
                '''                SNMP version used by the engine.
                ''',
                'version',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'snmp',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Callpoint.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Callpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Callpoint',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'callpoint',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Validationpoint.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Validationpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Validationpoint',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'validationpoint',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Actionpoint.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Actionpoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Actionpoint',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'actionpoint',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpInformCallback.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpInformCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpInformCallback',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'snmp-inform-callback',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.SnmpNotificationSubscription' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.SnmpNotificationSubscription',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'snmp-notification-subscription',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.ErrorFormattingCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.ErrorFormattingCallback',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'error-formatting-callback',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.Typepoint.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.Typepoint' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.Typepoint',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Callpoint id
                ''',
                'id',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'typepoint',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupportEnum' : _MetaInfoEnum('ReplaySupportEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'none':'none',
            'builtin':'builtin',
            'external':'external',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.NotificationStreamReplay' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.NotificationStreamReplay',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the notification stream.
                ''',
                'name',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('replay-support', REFERENCE_ENUM_CLASS, 'ReplaySupportEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay.ReplaySupportEnum', 
                [], [], 
                '''                ''',
                'replay_support',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'notification-stream-replay',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthenticationCallback.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthenticationCallback' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthenticationCallback',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ''',
                'enabled',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'authentication-callback',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the daemon registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numerical id assigned to the application daemon
                that has registered for a callpoint.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the application daemon that has
                registered for a callpoint.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'daemon',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                If this leaf exists, this is a default registration
                - in this case 'lower' and 'upper' do not exist.
                ''',
                'default',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lower', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the lower
                endpoint of the range for a non-default registration.
                ''',
                'lower',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upper', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The space-separated set of keys that defines the upper
                endpoint of the range for a non-default registration.
                ''',
                'upper',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'range',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'NOT-REGISTERED':'NOT_REGISTERED',
            'UNKNOWN':'UNKNOWN',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Callpoints.AuthorizationCallbacks' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints.AuthorizationCallbacks',
            False, 
            [
            _MetaInfoClassMember('daemon', REFERENCE_CLASS, 'Daemon' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon', 
                [], [], 
                '''                ''',
                'daemon',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ''',
                'enabled',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                with the callpoint registration.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the shared object implementing the type
                for a typepoint.
                ''',
                'file',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path of the list that a range registration
                pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range', 
                [], [], 
                '''                ''',
                'range',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'authorization-callbacks',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Callpoints' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Callpoints',
            False, 
            [
            _MetaInfoClassMember('actionpoint', REFERENCE_LIST, 'Actionpoint' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Actionpoint', 
                [], [], 
                '''                ''',
                'actionpoint',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('authentication-callback', REFERENCE_CLASS, 'AuthenticationCallback' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthenticationCallback', 
                [], [], 
                '''                ''',
                'authentication_callback',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('authorization-callbacks', REFERENCE_CLASS, 'AuthorizationCallbacks' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.AuthorizationCallbacks', 
                [], [], 
                '''                ''',
                'authorization_callbacks',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('callpoint', REFERENCE_LIST, 'Callpoint' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Callpoint', 
                [], [], 
                '''                ''',
                'callpoint',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error-formatting-callback', REFERENCE_LIST, 'ErrorFormattingCallback' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.ErrorFormattingCallback', 
                [], [], 
                '''                ''',
                'error_formatting_callback',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('notification-stream-replay', REFERENCE_LIST, 'NotificationStreamReplay' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.NotificationStreamReplay', 
                [], [], 
                '''                ''',
                'notification_stream_replay',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('snmp-inform-callback', REFERENCE_LIST, 'SnmpInformCallback' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpInformCallback', 
                [], [], 
                '''                ''',
                'snmp_inform_callback',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('snmp-notification-subscription', REFERENCE_LIST, 'SnmpNotificationSubscription' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.SnmpNotificationSubscription', 
                [], [], 
                '''                ''',
                'snmp_notification_subscription',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('typepoint', REFERENCE_LIST, 'Typepoint' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Typepoint', 
                [], [], 
                '''                ''',
                'typepoint',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('validationpoint', REFERENCE_LIST, 'Validationpoint' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints.Validationpoint', 
                [], [], 
                '''                ''',
                'validationpoint',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'callpoints',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the client that is the recipient of the
                notification.
                ''',
                'client_name',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('subscription-ids', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subscription identifiers for the subscriptions that
                generated the notification.
                ''',
                'subscription_ids',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'notification',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemainingEnum' : _MetaInfoEnum('TimeRemainingEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'infinity':'infinity',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync',
            False, 
            [
            _MetaInfoClassMember('notification', REFERENCE_LIST, 'Notification' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification', 
                [], [], 
                '''                ''',
                'notification',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The priority of the subscriptions that generated the
                notifications that are waiting for acknowledgement.
                Not present for the 'operational' datastore.
                ''',
                'priority',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('time-remaining', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The remaining time in seconds until subscribing clients
                that have not acknowledged their notifications are
                considered unresponsive and will be disconnected. See
                /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                page. The value 'infinity' means that no timeout has been
                configured in confd.conf.
                ''',
                'time_remaining',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                        [('0', '18446744073709551615')], [], 
                        '''                        The remaining time in seconds until subscribing clients
                        that have not acknowledged their notifications are
                        considered unresponsive and will be disconnected. See
                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                        page. The value 'infinity' means that no timeout has been
                        configured in confd.conf.
                        ''',
                        'time_remaining',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('time-remaining', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemainingEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.TimeRemainingEnum', 
                        [], [], 
                        '''                        The remaining time in seconds until subscribing clients
                        that have not acknowledged their notifications are
                        considered unresponsive and will be disconnected. See
                        /confdConfig/cdb/clientTimeout in the confd.conf(5) manual
                        page. The value 'infinity' means that no timeout has been
                        configured in confd.conf.
                        ''',
                        'time_remaining',
                        'tailf-confd-monitoring', False),
                ]),
            ],
            'tailf-confd-monitoring',
            'pending-subscription-sync',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the client that is the recipient of the
                notification.
                ''',
                'client_name',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The priority of the subscriptions that generated the
                notification. Not present for the the 'operational'
                datastore.
                ''',
                'priority',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('subscription-ids', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subscription identifiers for the subscriptions that
                generated the notification.
                ''',
                'subscription_ids',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'notification',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue',
            False, 
            [
            _MetaInfoClassMember('notification', REFERENCE_LIST, 'Notification' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification', 
                [], [], 
                '''                ''',
                'notification',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'pending-notification-queue',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Datastore' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Datastore',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreNameEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreNameEnum', 
                [], [], 
                '''                ''',
                'name',
                'tailf-confd-monitoring', True),
            _MetaInfoClassMember('disk-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The size of the file that is used for persistent storage
                for the datastore. Only present if 'filename' is present.
                ''',
                'disk_size',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('filename', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The pathname of the file that is used for persistent storage
                for the datastore. Not present for 'running' when 'startup'
                exists.
                ''',
                'filename',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('pending-notification-queue', REFERENCE_LIST, 'PendingNotificationQueue' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue', 
                [], [], 
                '''                Queues of notifications that have been generated but not
                yet delivered to subscribing clients. Not present for the
                'startup' datastore.
                ''',
                'pending_notification_queue',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('pending-subscription-sync', REFERENCE_CLASS, 'PendingSubscriptionSync' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync', 
                [], [], 
                '''                Information pertaining to subscription notifications that have
                been delivered to, but not yet acknowledged by, subscribing
                clients. Not present for the 'startup' datastore.
                ''',
                'pending_subscription_sync',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('ram-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The size of the in-memory representation of the datastore.
                ''',
                'ram_size',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('read-locks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of read locks on the datastore. Not present for
                the 'operational' data store.
                ''',
                'read_locks',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('subscription-lock-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether a subscription lock is in effect for the
                'operational' datastore.
                ''',
                'subscription_lock_set',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('transaction-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The id of the last committed transaction for the 'running'
                datastore, or the last update for the 'operational' datastore.
                For the 'operational' datastore, it is only present when HA
                is enabled.
                ''',
                'transaction_id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('waiting-for-replication-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether synchronous replication from HA master to
                HA slave is in progress for the datastore. Not present for the
                'operational' datastore.
                ''',
                'waiting_for_replication_sync',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('write-lock-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether a write lock is in effect for the datastore.
                Not present for the 'operational' datastore.
                ''',
                'write_lock_set',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('write-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending write requests for the 'operational'
                datastore on a HA slave that is in the process of syncronizing
                with the master.
                ''',
                'write_queue',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'datastore',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Client.Subscription.ErrorEnum' : _MetaInfoEnum('ErrorEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'PENDING':'PENDING',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.Subscription' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Client.Subscription',
            False, 
            [
            _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreNameEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreNameEnum', 
                [], [], 
                '''                The name of the datastore for the subscription - only
                'running' and 'operational' can have subscriptions.
                ''',
                'datastore',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('error', REFERENCE_ENUM_CLASS, 'ErrorEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Subscription.ErrorEnum', 
                [], [], 
                '''                If this leaf exists, there is a problem
                 with the subscription.
                ''',
                'error',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subscription identifier for the subscription.
                ''',
                'id',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The path that the subscription pertains to.
                ''',
                'path',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The priority of the subscription.
                ''',
                'priority',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('twophase', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Present if this is a 'twophase' subscription, i.e.
                notifications will be delivered at 'prepare' in addition
                to 'commit'. Only for the 'running' datastore.
                ''',
                'twophase',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'subscription',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb.Client.DatastoreEnum' : _MetaInfoEnum('DatastoreEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'pre_commit_running':'pre_commit_running',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.LockEnum' : _MetaInfoEnum('LockEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'read':'read',
            'subscription':'subscription',
            'pending-read':'pending_read',
            'pending-subscription':'pending_subscription',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'inactive':'inactive',
            'client':'client',
            'subscriber':'subscriber',
            'waiting':'waiting',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal.Cdb.Client' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb.Client',
            False, 
            [
            _MetaInfoClassMember('datastore', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The name of the datastore when 'type' = 'client'. The value
                'pre_commit_running' is the 'pseudo' datastore representing
                'running' before a commit.
                ''',
                'datastore',
                'tailf-confd-monitoring', False, [
                    _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.DatastoreNameEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.DatastoreNameEnum', 
                        [], [], 
                        '''                        The name of the datastore when 'type' = 'client'. The value
                        'pre_commit_running' is the 'pseudo' datastore representing
                        'running' before a commit.
                        ''',
                        'datastore',
                        'tailf-confd-monitoring', False),
                    _MetaInfoClassMember('datastore', REFERENCE_ENUM_CLASS, 'ConfdState.Internal.Cdb.Client.DatastoreEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.DatastoreEnum', 
                        [], [], 
                        '''                        The name of the datastore when 'type' = 'client'. The value
                        'pre_commit_running' is the 'pseudo' datastore representing
                        'running' before a commit.
                        ''',
                        'datastore',
                        'tailf-confd-monitoring', False),
                ]),
            _MetaInfoClassMember('info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Additional information about the client obtained at connect
                time. If present, it consists of client PID and socket file
                descriptor number.
                ''',
                'info',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('lock', REFERENCE_ENUM_CLASS, 'LockEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.LockEnum', 
                [], [], 
                '''                Set when 'type' = 'client' and the client has requested or
                acquired a lock on the datastore. The 'pending-read' and
                'pending-subscription' values indicate that the client has
                requested but not yet acquired the corresponding lock.
                A 'read' lock is never taken for the 'operational' datastore,
                a 'subscription' lock is never taken for any other datastore
                than 'operational'.
                ''',
                'lock',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The client name.
                ''',
                'name',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('subscription', REFERENCE_LIST, 'Subscription' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.Subscription', 
                [], [], 
                '''                ''',
                'subscription',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client.TypeEnum', 
                [], [], 
                '''                The type of client: 'inactive' is a client connection without
                any specific state. 'client' means that the client has an
                active session towards a datastore. A 'subscriber' has made
                one or more subscriptions. 'waiting' means that the client is
                waiting for completion of a call such as cdb_wait_start().
                ''',
                'type',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'client',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.Cdb' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal.Cdb',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Client', 
                [], [], 
                '''                ''',
                'client',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('datastore', REFERENCE_LIST, 'Datastore' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb.Datastore', 
                [], [], 
                '''                ''',
                'datastore',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'cdb',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.Internal.DatastoreNameEnum' : _MetaInfoEnum('DatastoreNameEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'running':'running',
            'startup':'startup',
            'operational':'operational',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState.Internal' : {
        'meta_info' : _MetaInfoClass('ConfdState.Internal',
            False, 
            [
            _MetaInfoClassMember('callpoints', REFERENCE_CLASS, 'Callpoints' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Callpoints', 
                [], [], 
                '''                ''',
                'callpoints',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('cdb', REFERENCE_CLASS, 'Cdb' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal.Cdb', 
                [], [], 
                '''                ''',
                'cdb',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'internal',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
    'ConfdState.DaemonStatusEnum' : _MetaInfoEnum('DaemonStatusEnum', 'ydk.models.cisco_ios_xe.tailf_confd_monitoring',
        {
            'starting':'starting',
            'phase0':'phase0',
            'phase1':'phase1',
            'started':'started',
            'stopping':'stopping',
        }, 'tailf-common-monitoring', _yang_ns._namespaces['tailf-common-monitoring']),
    'ConfdState' : {
        'meta_info' : _MetaInfoClass('ConfdState',
            False, 
            [
            _MetaInfoClassMember('cli', REFERENCE_CLASS, 'Cli' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Cli', 
                [], [], 
                '''                ''',
                'cli',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('daemon-status', REFERENCE_ENUM_CLASS, 'DaemonStatusEnum' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.DaemonStatusEnum', 
                [], [], 
                '''                ''',
                'daemon_status',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('epoll', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether an enhanced poll() function is used
                ''',
                'epoll',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('ha', REFERENCE_CLASS, 'Ha' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Ha', 
                [], [], 
                '''                ''',
                'ha',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('internal', REFERENCE_CLASS, 'Internal' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Internal', 
                [], [], 
                '''                ''',
                'internal',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('loaded-data-models', REFERENCE_CLASS, 'LoadedDataModels' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.LoadedDataModels', 
                [], [], 
                '''                ''',
                'loaded_data_models',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('netconf', REFERENCE_CLASS, 'Netconf' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Netconf', 
                [], [], 
                '''                ''',
                'netconf',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('read-only-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'read_only_mode',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('rest', REFERENCE_CLASS, 'Rest' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Rest', 
                [], [], 
                '''                ''',
                'rest',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('smp', REFERENCE_CLASS, 'Smp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Smp', 
                [], [], 
                '''                ''',
                'smp',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Snmp', 
                [], [], 
                '''                ''',
                'snmp',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('upgrade-mode', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Note that if the node is in upgrade mode, it is not possible to
                get any information from the system over NETCONF.
                The error-app-tag will be upgrade-in-progress.
                
                Existing CLI sessions can get system information.
                ''',
                'upgrade_mode',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tail-f product version number.
                ''',
                'version',
                'tailf-confd-monitoring', False),
            _MetaInfoClassMember('webui', REFERENCE_CLASS, 'Webui' , 'ydk.models.cisco_ios_xe.tailf_confd_monitoring', 'ConfdState.Webui', 
                [], [], 
                '''                ''',
                'webui',
                'tailf-confd-monitoring', False),
            ],
            'tailf-confd-monitoring',
            'confd-state',
            _yang_ns._namespaces['tailf-confd-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_confd_monitoring'
        ),
    },
}
_meta_table['ConfdState.LoadedDataModels.DataModel']['meta_info'].parent =_meta_table['ConfdState.LoadedDataModels']['meta_info']
_meta_table['ConfdState.Netconf.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Netconf.Listen']['meta_info']
_meta_table['ConfdState.Netconf.Listen.Ssh']['meta_info'].parent =_meta_table['ConfdState.Netconf.Listen']['meta_info']
_meta_table['ConfdState.Netconf.Listen']['meta_info'].parent =_meta_table['ConfdState.Netconf']['meta_info']
_meta_table['ConfdState.Cli.Listen.Ssh']['meta_info'].parent =_meta_table['ConfdState.Cli.Listen']['meta_info']
_meta_table['ConfdState.Cli.Listen']['meta_info'].parent =_meta_table['ConfdState.Cli']['meta_info']
_meta_table['ConfdState.Webui.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Webui.Listen']['meta_info']
_meta_table['ConfdState.Webui.Listen.Ssl']['meta_info'].parent =_meta_table['ConfdState.Webui.Listen']['meta_info']
_meta_table['ConfdState.Webui.Listen']['meta_info'].parent =_meta_table['ConfdState.Webui']['meta_info']
_meta_table['ConfdState.Rest.Listen.Tcp']['meta_info'].parent =_meta_table['ConfdState.Rest.Listen']['meta_info']
_meta_table['ConfdState.Rest.Listen.Ssl']['meta_info'].parent =_meta_table['ConfdState.Rest.Listen']['meta_info']
_meta_table['ConfdState.Rest.Listen']['meta_info'].parent =_meta_table['ConfdState.Rest']['meta_info']
_meta_table['ConfdState.Snmp.Listen.Udp']['meta_info'].parent =_meta_table['ConfdState.Snmp.Listen']['meta_info']
_meta_table['ConfdState.Snmp.Listen']['meta_info'].parent =_meta_table['ConfdState.Snmp']['meta_info']
_meta_table['ConfdState.Snmp.Version']['meta_info'].parent =_meta_table['ConfdState.Snmp']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Daemon']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks.Range']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Callpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Validationpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Actionpoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpInformCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.SnmpNotificationSubscription']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.ErrorFormattingCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.Typepoint']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.NotificationStreamReplay']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthenticationCallback']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Callpoints.AuthorizationCallbacks']['meta_info'].parent =_meta_table['ConfdState.Internal.Callpoints']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync.Notification']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue.Notification']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingSubscriptionSync']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore.PendingNotificationQueue']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Client.Subscription']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb.Client']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Datastore']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb']['meta_info']
_meta_table['ConfdState.Internal.Cdb.Client']['meta_info'].parent =_meta_table['ConfdState.Internal.Cdb']['meta_info']
_meta_table['ConfdState.Internal.Callpoints']['meta_info'].parent =_meta_table['ConfdState.Internal']['meta_info']
_meta_table['ConfdState.Internal.Cdb']['meta_info'].parent =_meta_table['ConfdState.Internal']['meta_info']
_meta_table['ConfdState.Smp']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Ha']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.LoadedDataModels']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Netconf']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Cli']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Webui']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Rest']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Snmp']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
_meta_table['ConfdState.Internal']['meta_info'].parent =_meta_table['ConfdState']['meta_info']
