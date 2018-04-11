""" cisco_self_mgmt 

Copyright (c) 2016 by Cisco Systems, Inc.All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NetconfYang(Entity):
    """
    Top level container shared by cisco\-ia and cisco\-odm models
    
    .. attribute:: cisco_ia
    
    	Customize the behavior of the DMI applications
    	**type**\:  :py:class:`CiscoIa <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa>`
    
    

    """

    _prefix = 'cisco-sfm'
    _revision = '2016-05-14'

    def __init__(self):
        super(NetconfYang, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-yang"
        self.yang_parent_name = "cisco-self-mgmt"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cisco-ia:cisco-ia", ("cisco_ia", NetconfYang.CiscoIa))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cisco_ia = NetconfYang.CiscoIa()
        self.cisco_ia.parent = self
        self._children_name_map["cisco_ia"] = "cisco-ia:cisco-ia"
        self._children_yang_names.add("cisco-ia:cisco-ia")
        self._segment_path = lambda: "cisco-self-mgmt:netconf-yang"


    class CiscoIa(Entity):
        """
        Customize the behavior of the DMI applications
        
        .. attribute:: auto_sync
        
        	Enables automatic synchronization of the network element's running configuration with the DMI database
        	**type**\:  :py:class:`CiaSyncType <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncType>`
        
        	**default value**\: without-defaults
        
        .. attribute:: init_sync
        
        	Enables synchronization of the network element's running configuration with the DMI database when DMI initializes
        	**type**\:  :py:class:`CiaSyncType <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncType>`
        
        	**default value**\: without-defaults
        
        .. attribute:: intelligent_sync
        
        	When enabled, intelligent\-sync monitors all  ttys for configuration changes and replays  these changes to the DMI database once the tty exits configuration mode.  When  disabled, the complete running\-configuration is used to synchronize the DMI database whenever a CLI configuration change is  detected
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: snmp_trap_control
        
        	This container describes the configuration parameters for SNMP Trap to NetConf notification processing
        	**type**\:  :py:class:`SnmpTrapControl <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.SnmpTrapControl>`
        
        .. attribute:: message_diag_level
        
        	0 = Disabled,  1 = Save input message, DMI debugs, and response,  2 = Level 1 + Save "before" and "after"      running\-config, 3 = Level 2 + rollback file and configuration diff
        	**type**\: int
        
        	**range:** 0..3
        
        	**default value**\: 0
        
        .. attribute:: max_diag_messages_saved
        
        	The maximum number of messages whose diagnostic data  in kept in persistent storage
        	**type**\: int
        
        	**range:** 0..199
        
        	**default value**\: 30
        
        .. attribute:: post_sync_acl_process
        
        	Run "show ip access\-list" and send to ConfD
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: config_change_delay
        
        	Delay in ms before applying CDB change to NE
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**default value**\: 0
        
        .. attribute:: process_missing_prc
        
        	Process any parser output from configuration changes as a possible error
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: snmp_community_string
        
        	The community string for communication with the SNMP         agent
        	**type**\: str
        
        	**default value**\: private
        
        .. attribute:: preserve_paths_enabled
        
        	Preserve specified model paths in the NED model when performing a sync from the  network element
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: preserve_ned_path
        
        	Model paths from the NED model to preserve upon a sync from the network element. These paths are not cleared from the  running data store prior to the sync. These are expressed as nodes separated by  slash '/', e.g.  /native/ip/access\-list
        	**type**\: list of  		 :py:class:`PreserveNedPath <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.PreserveNedPath>`
        
        .. attribute:: parser_msg_ignore
        
        	Parser output from configuration  change that is informational only, not an error. This is a read only list containing known informational  messages
        	**type**\: list of  		 :py:class:`ParserMsgIgnore <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ParserMsgIgnore>`
        
        .. attribute:: conf_parser_msg_ignore
        
        	Parser output from configuration  change that is informational only, not an error
        	**type**\: list of  		 :py:class:`ConfParserMsgIgnore <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfParserMsgIgnore>`
        
        .. attribute:: full_sync_cli
        
        	IOS commands that result in other automatic configurations being applied for which a complete sync is required
        	**type**\: list of  		 :py:class:`FullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.FullSyncCli>`
        
        .. attribute:: conf_full_sync_cli
        
        	A user\-configurable list of IOS commands  that result in other automatic configurations  being applied for which a complete sync  is required
        	**type**\: list of  		 :py:class:`ConfFullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfFullSyncCli>`
        
        .. attribute:: nes_ttynum
        
        	TTY number used by NetworkElementSynchronizer
        	**type**\: int
        
        	**range:** \-32768..32767
        
        .. attribute:: restored
        
        	Indicates if CDB restored from NES running\-config
        	**type**\: bool
        
        	**default value**\: false
        
        .. attribute:: logging
        
        	Controls logging behavior of DMI applications
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Logging>`
        
        .. attribute:: blocking
        
        	Controls blocking of command lines, either  from the NE to Confd or disallowing manual input from the console/vty
        	**type**\:  :py:class:`Blocking <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-01-22'

        def __init__(self):
            super(NetconfYang.CiscoIa, self).__init__()

            self.yang_name = "cisco-ia"
            self.yang_parent_name = "netconf-yang"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("snmp-trap-control", ("snmp_trap_control", NetconfYang.CiscoIa.SnmpTrapControl)), ("logging", ("logging", NetconfYang.CiscoIa.Logging)), ("blocking", ("blocking", NetconfYang.CiscoIa.Blocking))])
            self._child_list_classes = OrderedDict([("preserve-ned-path", ("preserve_ned_path", NetconfYang.CiscoIa.PreserveNedPath)), ("parser-msg-ignore", ("parser_msg_ignore", NetconfYang.CiscoIa.ParserMsgIgnore)), ("conf-parser-msg-ignore", ("conf_parser_msg_ignore", NetconfYang.CiscoIa.ConfParserMsgIgnore)), ("full-sync-cli", ("full_sync_cli", NetconfYang.CiscoIa.FullSyncCli)), ("conf-full-sync-cli", ("conf_full_sync_cli", NetconfYang.CiscoIa.ConfFullSyncCli))])
            self._leafs = OrderedDict([
                ('auto_sync', YLeaf(YType.enumeration, 'auto-sync')),
                ('init_sync', YLeaf(YType.enumeration, 'init-sync')),
                ('intelligent_sync', YLeaf(YType.boolean, 'intelligent-sync')),
                ('message_diag_level', YLeaf(YType.int16, 'message-diag-level')),
                ('max_diag_messages_saved', YLeaf(YType.int16, 'max-diag-messages-saved')),
                ('post_sync_acl_process', YLeaf(YType.boolean, 'post-sync-acl-process')),
                ('config_change_delay', YLeaf(YType.int16, 'config-change-delay')),
                ('process_missing_prc', YLeaf(YType.boolean, 'process-missing-prc')),
                ('snmp_community_string', YLeaf(YType.str, 'snmp-community-string')),
                ('preserve_paths_enabled', YLeaf(YType.boolean, 'preserve-paths-enabled')),
                ('nes_ttynum', YLeaf(YType.int16, 'nes-ttynum')),
                ('restored', YLeaf(YType.boolean, 'restored')),
            ])
            self.auto_sync = None
            self.init_sync = None
            self.intelligent_sync = None
            self.message_diag_level = None
            self.max_diag_messages_saved = None
            self.post_sync_acl_process = None
            self.config_change_delay = None
            self.process_missing_prc = None
            self.snmp_community_string = None
            self.preserve_paths_enabled = None
            self.nes_ttynum = None
            self.restored = None

            self.snmp_trap_control = NetconfYang.CiscoIa.SnmpTrapControl()
            self.snmp_trap_control.parent = self
            self._children_name_map["snmp_trap_control"] = "snmp-trap-control"
            self._children_yang_names.add("snmp-trap-control")

            self.logging = NetconfYang.CiscoIa.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"
            self._children_yang_names.add("logging")

            self.blocking = NetconfYang.CiscoIa.Blocking()
            self.blocking.parent = self
            self._children_name_map["blocking"] = "blocking"
            self._children_yang_names.add("blocking")

            self.preserve_ned_path = YList(self)
            self.parser_msg_ignore = YList(self)
            self.conf_parser_msg_ignore = YList(self)
            self.full_sync_cli = YList(self)
            self.conf_full_sync_cli = YList(self)
            self._segment_path = lambda: "cisco-ia:cisco-ia"
            self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfYang.CiscoIa, ['auto_sync', 'init_sync', 'intelligent_sync', 'message_diag_level', 'max_diag_messages_saved', 'post_sync_acl_process', 'config_change_delay', 'process_missing_prc', 'snmp_community_string', 'preserve_paths_enabled', 'nes_ttynum', 'restored'], name, value)


        class SnmpTrapControl(Entity):
            """
            This container describes the configuration parameters
            for SNMP Trap to NetConf notification processing.
            
            .. attribute:: global_forwarding
            
            	This leaf enables or disables forwarding for all SNMP traps
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: trap_list
            
            	This list describes SNMP Traps that are  supported for automatic translation to NetConf notifications
            	**type**\: list of  		 :py:class:`TrapList <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.SnmpTrapControl.TrapList>`
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.SnmpTrapControl, self).__init__()

                self.yang_name = "snmp-trap-control"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("trap-list", ("trap_list", NetconfYang.CiscoIa.SnmpTrapControl.TrapList))])
                self._leafs = OrderedDict([
                    ('global_forwarding', YLeaf(YType.boolean, 'global-forwarding')),
                ])
                self.global_forwarding = None

                self.trap_list = YList(self)
                self._segment_path = lambda: "snmp-trap-control"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.SnmpTrapControl, ['global_forwarding'], name, value)


            class TrapList(Entity):
                """
                This list describes SNMP Traps that are 
                supported for automatic translation to NetConf
                notifications.
                
                .. attribute:: trap_oid  (key)
                
                	This leaf contains the OID for the  SNMP trap to be forwarded
                	**type**\: str
                
                	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
                
                .. attribute:: description
                
                	This leaf contains the name of the SNMP trap to be  forwarded
                	**type**\: str
                
                .. attribute:: forward
                
                	This leaf enables or disables forwarding for this SNMP trap
                	**type**\: bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2018-01-22'

                def __init__(self):
                    super(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, self).__init__()

                    self.yang_name = "trap-list"
                    self.yang_parent_name = "snmp-trap-control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['trap_oid']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('trap_oid', YLeaf(YType.str, 'trap-oid')),
                        ('description', YLeaf(YType.str, 'description')),
                        ('forward', YLeaf(YType.boolean, 'forward')),
                    ])
                    self.trap_oid = None
                    self.description = None
                    self.forward = None
                    self._segment_path = lambda: "trap-list" + "[trap-oid='" + str(self.trap_oid) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/snmp-trap-control/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, ['trap_oid', 'description', 'forward'], name, value)


        class PreserveNedPath(Entity):
            """
            Model paths from the NED model to preserve
            upon a sync from the network element.
            These paths are not cleared from the 
            running data store prior to the sync.
            These are expressed as nodes separated by 
            slash '/', e.g.  /native/ip/access\-list
            
            .. attribute:: xpath  (key)
            
            	An XPath from the NED model
            	**type**\: str
            
            	**length:** 1..1024
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.PreserveNedPath, self).__init__()

                self.yang_name = "preserve-ned-path"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['xpath']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('xpath', YLeaf(YType.str, 'xpath')),
                ])
                self.xpath = None
                self._segment_path = lambda: "preserve-ned-path" + "[xpath='" + str(self.xpath) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.PreserveNedPath, ['xpath'], name, value)


        class ParserMsgIgnore(Entity):
            """
            Parser output from configuration 
            change that is informational only,
            not an error. This is a read only
            list containing known informational 
            messages
            
            .. attribute:: message  (key)
            
            	A regular expression to match parser output to be ignored
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.ParserMsgIgnore, self).__init__()

                self.yang_name = "parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', YLeaf(YType.str, 'message')),
                ])
                self.message = None
                self._segment_path = lambda: "parser-msg-ignore" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ParserMsgIgnore, ['message'], name, value)


        class ConfParserMsgIgnore(Entity):
            """
            Parser output from configuration 
            change that is informational only,
            not an error
            
            .. attribute:: message  (key)
            
            	A regular expression to match parser output to be ignored
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.ConfParserMsgIgnore, self).__init__()

                self.yang_name = "conf-parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', YLeaf(YType.str, 'message')),
                ])
                self.message = None
                self._segment_path = lambda: "conf-parser-msg-ignore" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ConfParserMsgIgnore, ['message'], name, value)


        class FullSyncCli(Entity):
            """
            IOS commands that result in other
            automatic configurations being applied
            for which a complete sync is required
            
            .. attribute:: command  (key)
            
            	A regular expression matching command lines which cause other automatic configuration changes
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.FullSyncCli, self).__init__()

                self.yang_name = "full-sync-cli"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['command']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('command', YLeaf(YType.str, 'command')),
                ])
                self.command = None
                self._segment_path = lambda: "full-sync-cli" + "[command='" + str(self.command) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.FullSyncCli, ['command'], name, value)


        class ConfFullSyncCli(Entity):
            """
            A user\-configurable list of IOS commands 
            that result in other automatic configurations 
            being applied for which a complete sync 
            is required
            
            .. attribute:: command  (key)
            
            	A regular expression matching command lines which cause other automatic configuration changes
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.ConfFullSyncCli, self).__init__()

                self.yang_name = "conf-full-sync-cli"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['command']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('command', YLeaf(YType.str, 'command')),
                ])
                self.command = None
                self._segment_path = lambda: "conf-full-sync-cli" + "[command='" + str(self.command) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ConfFullSyncCli, ['command'], name, value)


        class Logging(Entity):
            """
            Controls logging behavior of DMI applications
            
            .. attribute:: confd_log_level
            
            	Logging level for Confd
            	**type**\:  :py:class:`SyslogSeverity <ydk.models.cisco_ios_xe.cisco_ia.SyslogSeverity>`
            
            	**default value**\: error
            
            .. attribute:: ciaauthd_log_level
            
            	Logging level for CiaAuthDaemon
            	**type**\:  :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: nes_log_level
            
            	Logging level for Network Element Synchronizer
            	**type**\:  :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: onep_log_level
            
            	Logging level for ONEP
            	**type**\:  :py:class:`OnepLogLevel <ydk.models.cisco_ios_xe.cisco_ia.OnepLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: odm_log_level
            
            	Logging level for  Operational Data Manager
            	**type**\:  :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            	**status**\: obsolete
            
            .. attribute:: sync_log_level
            
            	Logging level for Sync\-From Daemon
            	**type**\:  :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('confd_log_level', YLeaf(YType.enumeration, 'confd-log-level')),
                    ('ciaauthd_log_level', YLeaf(YType.enumeration, 'ciaauthd-log-level')),
                    ('nes_log_level', YLeaf(YType.enumeration, 'nes-log-level')),
                    ('onep_log_level', YLeaf(YType.enumeration, 'onep-log-level')),
                    ('odm_log_level', YLeaf(YType.enumeration, 'odm-log-level')),
                    ('sync_log_level', YLeaf(YType.enumeration, 'sync-log-level')),
                ])
                self.confd_log_level = None
                self.ciaauthd_log_level = None
                self.nes_log_level = None
                self.onep_log_level = None
                self.odm_log_level = None
                self.sync_log_level = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.Logging, ['confd_log_level', 'ciaauthd_log_level', 'nes_log_level', 'onep_log_level', 'odm_log_level', 'sync_log_level'], name, value)


        class Blocking(Entity):
            """
            Controls blocking of command lines, either 
            from the NE to Confd or disallowing
            manual input from the console/vty
            
            .. attribute:: cli_blocking_enabled
            
            	Enables blocking of designated command lines via the  network element's CLI
            	**type**\: bool
            
            	**default value**\: false
            
            .. attribute:: network_element_command
            
            	Command line pattern to disallow via the network element's CLI
            	**type**\: list of  		 :py:class:`NetworkElementCommand <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking.NetworkElementCommand>`
            
            .. attribute:: confd_cfg_blocking_enabled
            
            	Enables blocking of designated command lines via the  network element's CLI
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: confd_cfg_command
            
            	Command line pattern to omit syncing to Confd CDB
            	**type**\: list of  		 :py:class:`ConfdCfgCommand <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking.ConfdCfgCommand>`
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-01-22'

            def __init__(self):
                super(NetconfYang.CiscoIa.Blocking, self).__init__()

                self.yang_name = "blocking"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("network-element-command", ("network_element_command", NetconfYang.CiscoIa.Blocking.NetworkElementCommand)), ("confd-cfg-command", ("confd_cfg_command", NetconfYang.CiscoIa.Blocking.ConfdCfgCommand))])
                self._leafs = OrderedDict([
                    ('cli_blocking_enabled', YLeaf(YType.boolean, 'cli-blocking-enabled')),
                    ('confd_cfg_blocking_enabled', YLeaf(YType.boolean, 'confd-cfg-blocking-enabled')),
                ])
                self.cli_blocking_enabled = None
                self.confd_cfg_blocking_enabled = None

                self.network_element_command = YList(self)
                self.confd_cfg_command = YList(self)
                self._segment_path = lambda: "blocking"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.Blocking, ['cli_blocking_enabled', 'confd_cfg_blocking_enabled'], name, value)


            class NetworkElementCommand(Entity):
                """
                Command line pattern to disallow via the
                network element's CLI
                
                .. attribute:: command  (key)
                
                	A regular expression matching command lines which should be blocked from entry via console/vty
                	**type**\: str
                
                	**length:** 1..255
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2018-01-22'

                def __init__(self):
                    super(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, self).__init__()

                    self.yang_name = "network-element-command"
                    self.yang_parent_name = "blocking"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('command', YLeaf(YType.str, 'command')),
                    ])
                    self.command = None
                    self._segment_path = lambda: "network-element-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, ['command'], name, value)


            class ConfdCfgCommand(Entity):
                """
                Command line pattern to omit syncing to Confd CDB
                
                .. attribute:: command  (key)
                
                	A regular expression matching command lines which should be blocked from being sent to Confd from the network element
                	**type**\: str
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2018-01-22'

                def __init__(self):
                    super(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, self).__init__()

                    self.yang_name = "confd-cfg-command"
                    self.yang_parent_name = "blocking"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('command', YLeaf(YType.str, 'command')),
                    ])
                    self.command = None
                    self._segment_path = lambda: "confd-cfg-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, ['command'], name, value)

    def clone_ptr(self):
        self._top_entity = NetconfYang()
        return self._top_entity

