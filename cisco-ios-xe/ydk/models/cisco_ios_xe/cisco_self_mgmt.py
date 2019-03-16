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
        self._child_classes = OrderedDict([("cisco-ia:cisco-ia", ("cisco_ia", NetconfYang.CiscoIa))])
        self._leafs = OrderedDict()

        self.cisco_ia = NetconfYang.CiscoIa()
        self.cisco_ia.parent = self
        self._children_name_map["cisco_ia"] = "cisco-ia:cisco-ia"
        self._segment_path = lambda: "cisco-self-mgmt:netconf-yang"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NetconfYang, [], name, value)


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
        
        .. attribute:: missing_prc_method
        
        	Process any parser output from configuration changes and compare against either a known set of errors  (blacklist) or a known set of messages to ignore  (whitelist)
        	**type**\:  :py:class:`ParserMsgProcessingMethod <ydk.models.cisco_ios_xe.cisco_ia.ParserMsgProcessingMethod>`
        
        	**default value**\: blacklist
        
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
        
        	**config**\: False
        
        .. attribute:: conf_parser_msg_ignore
        
        	Parser output from configuration  change that is informational only, not an error
        	**type**\: list of  		 :py:class:`ConfParserMsgIgnore <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfParserMsgIgnore>`
        
        .. attribute:: parser_msg_error
        
        	Parser output from configuration  change that indicates an error that cannot be ignored (must abort the transaction). This is a read only list containing known error messages
        	**type**\: list of  		 :py:class:`ParserMsgError <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ParserMsgError>`
        
        	**config**\: False
        
        .. attribute:: conf_parser_msg_error
        
        	Parser output from configuration  change that indicates an error that cannot be ignored (must abort the transaction)
        	**type**\: list of  		 :py:class:`ConfParserMsgError <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfParserMsgError>`
        
        .. attribute:: full_sync_cli
        
        	IOS commands that result in other automatic configurations being applied for which a complete sync is required
        	**type**\: list of  		 :py:class:`FullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.FullSyncCli>`
        
        	**config**\: False
        
        .. attribute:: conf_full_sync_cli
        
        	A user\-configurable list of IOS commands  that result in other automatic configurations  being applied for which a complete sync  is required
        	**type**\: list of  		 :py:class:`ConfFullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfFullSyncCli>`
        
        .. attribute:: nes_ttynum
        
        	TTY number used by NetworkElementSynchronizer
        	**type**\: int
        
        	**range:** \-32768..32767
        
        	**config**\: False
        
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
        
        .. attribute:: pivot_commands
        
        	WARNING\: These configuration commands should not be used unless          directed to by Cisco. Some IOS configuration commands may have a vitally important relationship to other IOS configuration commands. These so called pivotal commands have to be handled as an  execption to the normal processing flow. The pivotal commands and their special handling actions are described in this list
        	**type**\:  :py:class:`PivotCommands <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.PivotCommands>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2018-08-03'

        def __init__(self):
            super(NetconfYang.CiscoIa, self).__init__()

            self.yang_name = "cisco-ia"
            self.yang_parent_name = "netconf-yang"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snmp-trap-control", ("snmp_trap_control", NetconfYang.CiscoIa.SnmpTrapControl)), ("preserve-ned-path", ("preserve_ned_path", NetconfYang.CiscoIa.PreserveNedPath)), ("parser-msg-ignore", ("parser_msg_ignore", NetconfYang.CiscoIa.ParserMsgIgnore)), ("conf-parser-msg-ignore", ("conf_parser_msg_ignore", NetconfYang.CiscoIa.ConfParserMsgIgnore)), ("parser-msg-error", ("parser_msg_error", NetconfYang.CiscoIa.ParserMsgError)), ("conf-parser-msg-error", ("conf_parser_msg_error", NetconfYang.CiscoIa.ConfParserMsgError)), ("full-sync-cli", ("full_sync_cli", NetconfYang.CiscoIa.FullSyncCli)), ("conf-full-sync-cli", ("conf_full_sync_cli", NetconfYang.CiscoIa.ConfFullSyncCli)), ("logging", ("logging", NetconfYang.CiscoIa.Logging)), ("blocking", ("blocking", NetconfYang.CiscoIa.Blocking)), ("pivot-commands", ("pivot_commands", NetconfYang.CiscoIa.PivotCommands))])
            self._leafs = OrderedDict([
                ('auto_sync', (YLeaf(YType.enumeration, 'auto-sync'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaSyncType', '')])),
                ('init_sync', (YLeaf(YType.enumeration, 'init-sync'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaSyncType', '')])),
                ('intelligent_sync', (YLeaf(YType.boolean, 'intelligent-sync'), ['bool'])),
                ('message_diag_level', (YLeaf(YType.int16, 'message-diag-level'), ['int'])),
                ('max_diag_messages_saved', (YLeaf(YType.int16, 'max-diag-messages-saved'), ['int'])),
                ('post_sync_acl_process', (YLeaf(YType.boolean, 'post-sync-acl-process'), ['bool'])),
                ('config_change_delay', (YLeaf(YType.int16, 'config-change-delay'), ['int'])),
                ('process_missing_prc', (YLeaf(YType.boolean, 'process-missing-prc'), ['bool'])),
                ('missing_prc_method', (YLeaf(YType.enumeration, 'missing-prc-method'), [('ydk.models.cisco_ios_xe.cisco_ia', 'ParserMsgProcessingMethod', '')])),
                ('snmp_community_string', (YLeaf(YType.str, 'snmp-community-string'), ['str'])),
                ('preserve_paths_enabled', (YLeaf(YType.boolean, 'preserve-paths-enabled'), ['bool'])),
                ('nes_ttynum', (YLeaf(YType.int16, 'nes-ttynum'), ['int'])),
                ('restored', (YLeaf(YType.boolean, 'restored'), ['bool'])),
            ])
            self.auto_sync = None
            self.init_sync = None
            self.intelligent_sync = None
            self.message_diag_level = None
            self.max_diag_messages_saved = None
            self.post_sync_acl_process = None
            self.config_change_delay = None
            self.process_missing_prc = None
            self.missing_prc_method = None
            self.snmp_community_string = None
            self.preserve_paths_enabled = None
            self.nes_ttynum = None
            self.restored = None

            self.snmp_trap_control = NetconfYang.CiscoIa.SnmpTrapControl()
            self.snmp_trap_control.parent = self
            self._children_name_map["snmp_trap_control"] = "snmp-trap-control"

            self.logging = NetconfYang.CiscoIa.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"

            self.blocking = NetconfYang.CiscoIa.Blocking()
            self.blocking.parent = self
            self._children_name_map["blocking"] = "blocking"

            self.pivot_commands = NetconfYang.CiscoIa.PivotCommands()
            self.pivot_commands.parent = self
            self._children_name_map["pivot_commands"] = "pivot-commands"

            self.preserve_ned_path = YList(self)
            self.parser_msg_ignore = YList(self)
            self.conf_parser_msg_ignore = YList(self)
            self.parser_msg_error = YList(self)
            self.conf_parser_msg_error = YList(self)
            self.full_sync_cli = YList(self)
            self.conf_full_sync_cli = YList(self)
            self._segment_path = lambda: "cisco-ia:cisco-ia"
            self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfYang.CiscoIa, ['auto_sync', 'init_sync', 'intelligent_sync', 'message_diag_level', 'max_diag_messages_saved', 'post_sync_acl_process', 'config_change_delay', 'process_missing_prc', 'missing_prc_method', 'snmp_community_string', 'preserve_paths_enabled', 'nes_ttynum', 'restored'], name, value)


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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.SnmpTrapControl, self).__init__()

                self.yang_name = "snmp-trap-control"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("trap-list", ("trap_list", NetconfYang.CiscoIa.SnmpTrapControl.TrapList))])
                self._leafs = OrderedDict([
                    ('global_forwarding', (YLeaf(YType.boolean, 'global-forwarding'), ['bool'])),
                ])
                self.global_forwarding = None

                self.trap_list = YList(self)
                self._segment_path = lambda: "snmp-trap-control"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2018-08-03'

                def __init__(self):
                    super(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, self).__init__()

                    self.yang_name = "trap-list"
                    self.yang_parent_name = "snmp-trap-control"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['trap_oid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('trap_oid', (YLeaf(YType.str, 'trap-oid'), ['str'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('forward', (YLeaf(YType.boolean, 'forward'), ['bool'])),
                    ])
                    self.trap_oid = None
                    self.description = None
                    self.forward = None
                    self._segment_path = lambda: "trap-list" + "[trap-oid='" + str(self.trap_oid) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/snmp-trap-control/%s" % self._segment_path()
                    self._is_frozen = True

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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.PreserveNedPath, self).__init__()

                self.yang_name = "preserve-ned-path"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['xpath']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('xpath', (YLeaf(YType.str, 'xpath'), ['str'])),
                ])
                self.xpath = None
                self._segment_path = lambda: "preserve-ned-path" + "[xpath='" + str(self.xpath) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
            
            	**config**\: False
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.ParserMsgIgnore, self).__init__()

                self.yang_name = "parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', (YLeaf(YType.str, 'message'), ['str'])),
                ])
                self.message = None
                self._segment_path = lambda: "parser-msg-ignore" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.ConfParserMsgIgnore, self).__init__()

                self.yang_name = "conf-parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', (YLeaf(YType.str, 'message'), ['str'])),
                ])
                self.message = None
                self._segment_path = lambda: "conf-parser-msg-ignore" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ConfParserMsgIgnore, ['message'], name, value)



        class ParserMsgError(Entity):
            """
            Parser output from configuration 
            change that indicates an error
            that cannot be ignored (must abort
            the transaction). This is a read only
            list containing known error messages.
            
            .. attribute:: message  (key)
            
            	A regular expression to match parser output to be considered an error
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.ParserMsgError, self).__init__()

                self.yang_name = "parser-msg-error"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', (YLeaf(YType.str, 'message'), ['str'])),
                ])
                self.message = None
                self._segment_path = lambda: "parser-msg-error" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ParserMsgError, ['message'], name, value)



        class ConfParserMsgError(Entity):
            """
            Parser output from configuration 
            change that indicates an error
            that cannot be ignored (must abort
            the transaction).
            
            .. attribute:: message  (key)
            
            	A regular expression to match parser output to be considered an error
            	**type**\: str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.ConfParserMsgError, self).__init__()

                self.yang_name = "conf-parser-msg-error"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['message']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('message', (YLeaf(YType.str, 'message'), ['str'])),
                ])
                self.message = None
                self._segment_path = lambda: "conf-parser-msg-error" + "[message='" + str(self.message) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.ConfParserMsgError, ['message'], name, value)



        class FullSyncCli(Entity):
            """
            IOS commands that result in other
            automatic configurations being applied
            for which a complete sync is required
            
            .. attribute:: command  (key)
            
            	A regular expression matching command lines which cause other automatic configuration changes
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.FullSyncCli, self).__init__()

                self.yang_name = "full-sync-cli"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['command']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('command', (YLeaf(YType.str, 'command'), ['str'])),
                ])
                self.command = None
                self._segment_path = lambda: "full-sync-cli" + "[command='" + str(self.command) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.ConfFullSyncCli, self).__init__()

                self.yang_name = "conf-full-sync-cli"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['command']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('command', (YLeaf(YType.str, 'command'), ['str'])),
                ])
                self.command = None
                self._segment_path = lambda: "conf-full-sync-cli" + "[command='" + str(self.command) + "']"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('confd_log_level', (YLeaf(YType.enumeration, 'confd-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'SyslogSeverity', '')])),
                    ('ciaauthd_log_level', (YLeaf(YType.enumeration, 'ciaauthd-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevel', '')])),
                    ('nes_log_level', (YLeaf(YType.enumeration, 'nes-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevel', '')])),
                    ('onep_log_level', (YLeaf(YType.enumeration, 'onep-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'OnepLogLevel', '')])),
                    ('odm_log_level', (YLeaf(YType.enumeration, 'odm-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevel', '')])),
                    ('sync_log_level', (YLeaf(YType.enumeration, 'sync-log-level'), [('ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevel', '')])),
                ])
                self.confd_log_level = None
                self.ciaauthd_log_level = None
                self.nes_log_level = None
                self.onep_log_level = None
                self.odm_log_level = None
                self.sync_log_level = None
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.Blocking, self).__init__()

                self.yang_name = "blocking"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("network-element-command", ("network_element_command", NetconfYang.CiscoIa.Blocking.NetworkElementCommand)), ("confd-cfg-command", ("confd_cfg_command", NetconfYang.CiscoIa.Blocking.ConfdCfgCommand))])
                self._leafs = OrderedDict([
                    ('cli_blocking_enabled', (YLeaf(YType.boolean, 'cli-blocking-enabled'), ['bool'])),
                    ('confd_cfg_blocking_enabled', (YLeaf(YType.boolean, 'confd-cfg-blocking-enabled'), ['bool'])),
                ])
                self.cli_blocking_enabled = None
                self.confd_cfg_blocking_enabled = None

                self.network_element_command = YList(self)
                self.confd_cfg_command = YList(self)
                self._segment_path = lambda: "blocking"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

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
                _revision = '2018-08-03'

                def __init__(self):
                    super(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, self).__init__()

                    self.yang_name = "network-element-command"
                    self.yang_parent_name = "blocking"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('command', (YLeaf(YType.str, 'command'), ['str'])),
                    ])
                    self.command = None
                    self._segment_path = lambda: "network-element-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self._segment_path()
                    self._is_frozen = True

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
                _revision = '2018-08-03'

                def __init__(self):
                    super(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, self).__init__()

                    self.yang_name = "confd-cfg-command"
                    self.yang_parent_name = "blocking"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('command', (YLeaf(YType.str, 'command'), ['str'])),
                    ])
                    self.command = None
                    self._segment_path = lambda: "confd-cfg-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, ['command'], name, value)




        class PivotCommands(Entity):
            """
            WARNING\: These configuration commands should not be used unless
                     directed to by Cisco.
            Some IOS configuration commands may have a vitally important
            relationship to other IOS configuration commands.
            These so called pivotal commands have to be handled as an 
            execption to the normal processing flow. The pivotal commands
            and their special handling actions are described in this list.
            
            .. attribute:: pivot_command
            
            	Static list of pivot commands
            	**type**\: list of  		 :py:class:`PivotCommand <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.PivotCommands.PivotCommand>`
            
            	**config**\: False
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2018-08-03'

            def __init__(self):
                super(NetconfYang.CiscoIa.PivotCommands, self).__init__()

                self.yang_name = "pivot-commands"
                self.yang_parent_name = "cisco-ia"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("pivot-command", ("pivot_command", NetconfYang.CiscoIa.PivotCommands.PivotCommand))])
                self._leafs = OrderedDict()

                self.pivot_command = YList(self)
                self._segment_path = lambda: "pivot-commands"
                self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.CiscoIa.PivotCommands, [], name, value)


            class PivotCommand(Entity):
                """
                Static list of pivot commands.
                
                .. attribute:: command  (key)
                
                	The command prefix to match.  Leading spaces are counted towards the match
                	**type**\: str
                
                	**length:** 1..255
                
                	**config**\: False
                
                .. attribute:: retry
                
                	Whether or not the command will be retried if it fails and associated parameters
                	**type**\:  :py:class:`Retry <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.PivotCommands.PivotCommand.Retry>`
                
                	**presence node**\: True
                
                	**config**\: False
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2018-08-03'

                def __init__(self):
                    super(NetconfYang.CiscoIa.PivotCommands.PivotCommand, self).__init__()

                    self.yang_name = "pivot-command"
                    self.yang_parent_name = "pivot-commands"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_classes = OrderedDict([("retry", ("retry", NetconfYang.CiscoIa.PivotCommands.PivotCommand.Retry))])
                    self._leafs = OrderedDict([
                        ('command', (YLeaf(YType.str, 'command'), ['str'])),
                    ])
                    self.command = None

                    self.retry = None
                    self._children_name_map["retry"] = "retry"
                    self._segment_path = lambda: "pivot-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/pivot-commands/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.CiscoIa.PivotCommands.PivotCommand, ['command'], name, value)


                class Retry(Entity):
                    """
                    Whether or not the command will be retried if it
                    fails and associated parameters.
                    
                    .. attribute:: min_retry_time
                    
                    	The minimum time to wait before retrying a failed command
                    	**type**\: int
                    
                    	**range:** 10..60000
                    
                    	**config**\: False
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: max_retry_time
                    
                    	The maximum time to wait before retrying a failed command.  Commands that continue to fail after having waited this amount of time are considered to have permanently failed
                    	**type**\: int
                    
                    	**range:** 10..60000
                    
                    	**config**\: False
                    
                    	**units**\: milliseconds
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'cisco-ia'
                    _revision = '2018-08-03'

                    def __init__(self):
                        super(NetconfYang.CiscoIa.PivotCommands.PivotCommand.Retry, self).__init__()

                        self.yang_name = "retry"
                        self.yang_parent_name = "pivot-command"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('min_retry_time', (YLeaf(YType.uint16, 'min-retry-time'), ['int'])),
                            ('max_retry_time', (YLeaf(YType.uint16, 'max-retry-time'), ['int'])),
                        ])
                        self.min_retry_time = None
                        self.max_retry_time = None
                        self._segment_path = lambda: "retry"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetconfYang.CiscoIa.PivotCommands.PivotCommand.Retry, ['min_retry_time', 'max_retry_time'], name, value)





    def clone_ptr(self):
        self._top_entity = NetconfYang()
        return self._top_entity



