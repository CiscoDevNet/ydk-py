""" cisco_self_mgmt 

Copyright (c) 2016 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class NetconfYang(object):
    """
    Top level container shared by cisco\-ia and cisco\-odm models
    
    .. attribute:: cisco_ia
    
    	Customize the behavior of the DMI applications
    	**type**\:   :py:class:`CiscoIa <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa>`
    
    .. attribute:: cisco_odm
    
    	
    	**type**\:   :py:class:`CiscoOdm <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoOdm>`
    
    

    """

    _prefix = 'cisco-sfm'
    _revision = '2016-05-14'

    def __init__(self):
        self.cisco_ia = NetconfYang.CiscoIa()
        self.cisco_ia.parent = self
        self.cisco_odm = NetconfYang.CiscoOdm()
        self.cisco_odm.parent = self


    class CiscoIa(object):
        """
        Customize the behavior of the DMI applications
        
        .. attribute:: auto_sync
        
        	Enables automatic synchronization of the network element's running configuration with the DMI database
        	**type**\:   :py:class:`CiaSyncTypeEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncTypeEnum>`
        
        	**default value**\: without-defaults
        
        .. attribute:: blocking
        
        	Controls blocking of command lines, either  from the NE to Confd or disallowing manual input from the console/vty
        	**type**\:   :py:class:`Blocking <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking>`
        
        .. attribute:: conf_full_sync_cli
        
        	A user\-configurable list of IOS commands  that result in other automatic configurations  being applied for which a complete sync  is required
        	**type**\: list of    :py:class:`ConfFullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfFullSyncCli>`
        
        .. attribute:: conf_parser_msg_ignore
        
        	Parser output from configuration  change that is informational only, not an error
        	**type**\: list of    :py:class:`ConfParserMsgIgnore <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ConfParserMsgIgnore>`
        
        .. attribute:: config_change_delay
        
        	Delay in ms before applying CDB change to NE
        	**type**\:  int
        
        	**range:** \-32768..32767
        
        	**default value**\: 0
        
        .. attribute:: full_sync_cli
        
        	IOS commands that result in other automatic configurations being applied for which a complete sync is required
        	**type**\: list of    :py:class:`FullSyncCli <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.FullSyncCli>`
        
        .. attribute:: init_sync
        
        	Enables synchronization of the network element's running configuration with the DMI database when DMI initializes
        	**type**\:   :py:class:`CiaSyncTypeEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncTypeEnum>`
        
        	**default value**\: without-defaults
        
        .. attribute:: intelligent_sync
        
        	When enabled, intelligent\-sync monitors all  ttys for configuration changes and replays  these changes to the DMI database once the tty exits configuration mode.  When  disabled, the complete running\-configuration is used to synchronize the DMI database whenever a CLI configuration change is  detected
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: logging
        
        	Controls logging behavior of DMI applications
        	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Logging>`
        
        .. attribute:: max_diag_messages_saved
        
        	The maximum number of messages whose diagnostic data  in kept in persistent storage
        	**type**\:  int
        
        	**range:** 0..199
        
        	**default value**\: 30
        
        .. attribute:: message_diag_level
        
        	0 = Disabled,  1 = Save input message, DMI debugs, and response,  2 = Level 1 + Save "before" and "after"      running\-config, 3 = Level 2 + rollback file and configuration diff
        	**type**\:  int
        
        	**range:** 0..3
        
        	**default value**\: 0
        
        .. attribute:: nes_ttynum
        
        	TTY number used by NetworkElementSynchronizer
        	**type**\:  int
        
        	**range:** \-32768..32767
        
        .. attribute:: parser_msg_ignore
        
        	Parser output from configuration  change that is informational only, not an error. This is a read only list containing known informational  messages
        	**type**\: list of    :py:class:`ParserMsgIgnore <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.ParserMsgIgnore>`
        
        .. attribute:: post_sync_acl_process
        
        	Run "show ip access\-list" and send to ConfD
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: preserve_ned_path
        
        	Model paths from the NED model to preserve upon a sync from the network element. These paths are not cleared from the  running data store prior to the sync. These are expressed as nodes separated by  slash '/', e.g.  /native/ip/access\-list
        	**type**\: list of    :py:class:`PreserveNedPath <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.PreserveNedPath>`
        
        .. attribute:: preserve_paths_enabled
        
        	Preserve specified model paths in the NED model when performing a sync from the  network element
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: process_missing_prc
        
        	Process any parser output from configuration changes as a possible error
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: restored
        
        	Indicates if CDB restored from NES running\-config
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: snmp_community_string
        
        	The community string for communication with the SNMP         agent
        	**type**\:  str
        
        	**default value**\: private
        
        .. attribute:: snmp_trap_control
        
        	This container describes the configuration parameters for SNMP Trap to NetConf notification processing
        	**type**\:   :py:class:`SnmpTrapControl <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.SnmpTrapControl>`
        
        

        """

        _prefix = 'cisco-ia'
        _revision = '2017-03-02'

        def __init__(self):
            self.parent = None
            self.auto_sync = None
            self.blocking = NetconfYang.CiscoIa.Blocking()
            self.blocking.parent = self
            self.conf_full_sync_cli = YList()
            self.conf_full_sync_cli.parent = self
            self.conf_full_sync_cli.name = 'conf_full_sync_cli'
            self.conf_parser_msg_ignore = YList()
            self.conf_parser_msg_ignore.parent = self
            self.conf_parser_msg_ignore.name = 'conf_parser_msg_ignore'
            self.config_change_delay = None
            self.full_sync_cli = YList()
            self.full_sync_cli.parent = self
            self.full_sync_cli.name = 'full_sync_cli'
            self.init_sync = None
            self.intelligent_sync = None
            self.logging = NetconfYang.CiscoIa.Logging()
            self.logging.parent = self
            self.max_diag_messages_saved = None
            self.message_diag_level = None
            self.nes_ttynum = None
            self.parser_msg_ignore = YList()
            self.parser_msg_ignore.parent = self
            self.parser_msg_ignore.name = 'parser_msg_ignore'
            self.post_sync_acl_process = None
            self.preserve_ned_path = YList()
            self.preserve_ned_path.parent = self
            self.preserve_ned_path.name = 'preserve_ned_path'
            self.preserve_paths_enabled = None
            self.process_missing_prc = None
            self.restored = None
            self.snmp_community_string = None
            self.snmp_trap_control = NetconfYang.CiscoIa.SnmpTrapControl()
            self.snmp_trap_control.parent = self


        class SnmpTrapControl(object):
            """
            This container describes the configuration parameters
            for SNMP Trap to NetConf notification processing.
            
            .. attribute:: global_forwarding
            
            	This leaf enables or disables forwarding for all SNMP traps
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: trap_list
            
            	This list describes SNMP Traps that are  supported for automatic translation to NetConf notifications
            	**type**\: list of    :py:class:`TrapList <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.SnmpTrapControl.TrapList>`
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.global_forwarding = None
                self.trap_list = YList()
                self.trap_list.parent = self
                self.trap_list.name = 'trap_list'


            class TrapList(object):
                """
                This list describes SNMP Traps that are 
                supported for automatic translation to NetConf
                notifications.
                
                .. attribute:: trap_oid  <key>
                
                	This leaf contains the OID for the  SNMP trap to be forwarded
                	**type**\:  str
                
                	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
                
                .. attribute:: description
                
                	This leaf contains the name of the SNMP trap to be  forwarded
                	**type**\:  str
                
                .. attribute:: forward
                
                	This leaf enables or disables forwarding for this SNMP trap
                	**type**\:  bool
                
                	**default value**\: true
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.trap_oid = None
                    self.description = None
                    self.forward = None

                @property
                def _common_path(self):
                    if self.trap_oid is None:
                        raise YPYModelError('Key property trap_oid is None')

                    return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:snmp-trap-control/cisco-ia:trap-list[cisco-ia:trap-oid = ' + str(self.trap_oid) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.trap_oid is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.forward is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                    return meta._meta_table['NetconfYang.CiscoIa.SnmpTrapControl.TrapList']['meta_info']

            @property
            def _common_path(self):

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:snmp-trap-control'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.global_forwarding is not None:
                    return True

                if self.trap_list is not None:
                    for child_ref in self.trap_list:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.SnmpTrapControl']['meta_info']


        class PreserveNedPath(object):
            """
            Model paths from the NED model to preserve
            upon a sync from the network element.
            These paths are not cleared from the 
            running data store prior to the sync.
            These are expressed as nodes separated by 
            slash '/', e.g.  /native/ip/access\-list
            
            .. attribute:: xpath  <key>
            
            	An XPath from the NED model
            	**type**\:  str
            
            	**length:** 1..1024
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.xpath = None

            @property
            def _common_path(self):
                if self.xpath is None:
                    raise YPYModelError('Key property xpath is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:preserve-ned-path[cisco-ia:xpath = ' + str(self.xpath) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.xpath is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.PreserveNedPath']['meta_info']


        class ParserMsgIgnore(object):
            """
            Parser output from configuration 
            change that is informational only,
            not an error. This is a read only
            list containing known informational 
            messages
            
            .. attribute:: message  <key>
            
            	A regular expression to match parser output to be ignored
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.message = None

            @property
            def _common_path(self):
                if self.message is None:
                    raise YPYModelError('Key property message is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:parser-msg-ignore[cisco-ia:message = ' + str(self.message) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.message is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.ParserMsgIgnore']['meta_info']


        class ConfParserMsgIgnore(object):
            """
            Parser output from configuration 
            change that is informational only,
            not an error
            
            .. attribute:: message  <key>
            
            	A regular expression to match parser output to be ignored
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.message = None

            @property
            def _common_path(self):
                if self.message is None:
                    raise YPYModelError('Key property message is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:conf-parser-msg-ignore[cisco-ia:message = ' + str(self.message) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.message is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.ConfParserMsgIgnore']['meta_info']


        class FullSyncCli(object):
            """
            IOS commands that result in other
            automatic configurations being applied
            for which a complete sync is required
            
            .. attribute:: command  <key>
            
            	A regular expression matching command lines which cause other automatic configuration changes
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.command = None

            @property
            def _common_path(self):
                if self.command is None:
                    raise YPYModelError('Key property command is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:full-sync-cli[cisco-ia:command = ' + str(self.command) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.command is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.FullSyncCli']['meta_info']


        class ConfFullSyncCli(object):
            """
            A user\-configurable list of IOS commands 
            that result in other automatic configurations 
            being applied for which a complete sync 
            is required
            
            .. attribute:: command  <key>
            
            	A regular expression matching command lines which cause other automatic configuration changes
            	**type**\:  str
            
            	**length:** 1..255
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.command = None

            @property
            def _common_path(self):
                if self.command is None:
                    raise YPYModelError('Key property command is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:conf-full-sync-cli[cisco-ia:command = ' + str(self.command) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.command is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.ConfFullSyncCli']['meta_info']


        class Logging(object):
            """
            Controls logging behavior of DMI applications
            
            .. attribute:: ciaauthd_log_level
            
            	Logging level for CiaAuthDaemon
            	**type**\:   :py:class:`CiaLogLevelEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevelEnum>`
            
            	**default value**\: error
            
            .. attribute:: confd_log_level
            
            	Logging level for Confd
            	**type**\:   :py:class:`SyslogSeverityEnum <ydk.models.cisco_ios_xe.cisco_ia.SyslogSeverityEnum>`
            
            	**default value**\: error
            
            .. attribute:: nes_log_level
            
            	Logging level for Network Element Synchronizer
            	**type**\:   :py:class:`CiaLogLevelEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevelEnum>`
            
            	**default value**\: error
            
            .. attribute:: odm_log_level
            
            	Logging level for  Operational Data Manager
            	**type**\:   :py:class:`CiaLogLevelEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevelEnum>`
            
            	**default value**\: error
            
            .. attribute:: onep_log_level
            
            	Logging level for ONEP
            	**type**\:   :py:class:`OnepLogLevelEnum <ydk.models.cisco_ios_xe.cisco_ia.OnepLogLevelEnum>`
            
            	**default value**\: error
            
            .. attribute:: sync_log_level
            
            	Logging level for Sync\-From Daemon
            	**type**\:   :py:class:`CiaLogLevelEnum <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevelEnum>`
            
            	**default value**\: error
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.ciaauthd_log_level = None
                self.confd_log_level = None
                self.nes_log_level = None
                self.odm_log_level = None
                self.onep_log_level = None
                self.sync_log_level = None

            @property
            def _common_path(self):

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ciaauthd_log_level is not None:
                    return True

                if self.confd_log_level is not None:
                    return True

                if self.nes_log_level is not None:
                    return True

                if self.odm_log_level is not None:
                    return True

                if self.onep_log_level is not None:
                    return True

                if self.sync_log_level is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.Logging']['meta_info']


        class Blocking(object):
            """
            Controls blocking of command lines, either 
            from the NE to Confd or disallowing
            manual input from the console/vty
            
            .. attribute:: cli_blocking_enabled
            
            	Enables blocking of designated command lines via the  network element's CLI
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: confd_cfg_blocking_enabled
            
            	Enables blocking of designated command lines via the  network element's CLI
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: confd_cfg_command
            
            	Command line pattern to omit syncing to Confd CDB
            	**type**\: list of    :py:class:`ConfdCfgCommand <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking.ConfdCfgCommand>`
            
            .. attribute:: network_element_command
            
            	Command line pattern to disallow via the network element's CLI
            	**type**\: list of    :py:class:`NetworkElementCommand <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoIa.Blocking.NetworkElementCommand>`
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                self.parent = None
                self.cli_blocking_enabled = None
                self.confd_cfg_blocking_enabled = None
                self.confd_cfg_command = YList()
                self.confd_cfg_command.parent = self
                self.confd_cfg_command.name = 'confd_cfg_command'
                self.network_element_command = YList()
                self.network_element_command.parent = self
                self.network_element_command.name = 'network_element_command'


            class NetworkElementCommand(object):
                """
                Command line pattern to disallow via the
                network element's CLI
                
                .. attribute:: command  <key>
                
                	A regular expression matching command lines which should be blocked from entry via console/vty
                	**type**\:  str
                
                	**length:** 1..255
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.command = None

                @property
                def _common_path(self):
                    if self.command is None:
                        raise YPYModelError('Key property command is None')

                    return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:blocking/cisco-ia:network-element-command[cisco-ia:command = ' + str(self.command) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.command is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                    return meta._meta_table['NetconfYang.CiscoIa.Blocking.NetworkElementCommand']['meta_info']


            class ConfdCfgCommand(object):
                """
                Command line pattern to omit syncing to Confd CDB
                
                .. attribute:: command  <key>
                
                	A regular expression matching command lines which should be blocked from being sent to Confd from the network element
                	**type**\:  str
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2017-03-02'

                def __init__(self):
                    self.parent = None
                    self.command = None

                @property
                def _common_path(self):
                    if self.command is None:
                        raise YPYModelError('Key property command is None')

                    return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:blocking/cisco-ia:confd-cfg-command[cisco-ia:command = ' + str(self.command) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.command is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                    return meta._meta_table['NetconfYang.CiscoIa.Blocking.ConfdCfgCommand']['meta_info']

            @property
            def _common_path(self):

                return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/cisco-ia:blocking'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.cli_blocking_enabled is not None:
                    return True

                if self.confd_cfg_blocking_enabled is not None:
                    return True

                if self.confd_cfg_command is not None:
                    for child_ref in self.confd_cfg_command:
                        if child_ref._has_data():
                            return True

                if self.network_element_command is not None:
                    for child_ref in self.network_element_command:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoIa.Blocking']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.auto_sync is not None:
                return True

            if self.blocking is not None and self.blocking._has_data():
                return True

            if self.conf_full_sync_cli is not None:
                for child_ref in self.conf_full_sync_cli:
                    if child_ref._has_data():
                        return True

            if self.conf_parser_msg_ignore is not None:
                for child_ref in self.conf_parser_msg_ignore:
                    if child_ref._has_data():
                        return True

            if self.config_change_delay is not None:
                return True

            if self.full_sync_cli is not None:
                for child_ref in self.full_sync_cli:
                    if child_ref._has_data():
                        return True

            if self.init_sync is not None:
                return True

            if self.intelligent_sync is not None:
                return True

            if self.logging is not None and self.logging._has_data():
                return True

            if self.max_diag_messages_saved is not None:
                return True

            if self.message_diag_level is not None:
                return True

            if self.nes_ttynum is not None:
                return True

            if self.parser_msg_ignore is not None:
                for child_ref in self.parser_msg_ignore:
                    if child_ref._has_data():
                        return True

            if self.post_sync_acl_process is not None:
                return True

            if self.preserve_ned_path is not None:
                for child_ref in self.preserve_ned_path:
                    if child_ref._has_data():
                        return True

            if self.preserve_paths_enabled is not None:
                return True

            if self.process_missing_prc is not None:
                return True

            if self.restored is not None:
                return True

            if self.snmp_community_string is not None:
                return True

            if self.snmp_trap_control is not None and self.snmp_trap_control._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
            return meta._meta_table['NetconfYang.CiscoIa']['meta_info']


    class CiscoOdm(object):
        """
        
        
        .. attribute:: actions
        
        	
        	**type**\: list of    :py:class:`Actions <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoOdm.Actions>`
        
        .. attribute:: on_demand_default_time
        
        	
        	**type**\:  int
        
        	**range:** 500..4294967295
        
        	**default value**\: 30000
        
        	**status**\: obsolete
        
        .. attribute:: on_demand_enable
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        	**status**\: obsolete
        
        .. attribute:: polling_enable
        
        	
        	**type**\:  bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'codm'
        _revision = '2017-01-25'

        def __init__(self):
            self.parent = None
            self.actions = YList()
            self.actions.parent = self
            self.actions.name = 'actions'
            self.on_demand_default_time = None
            self.on_demand_enable = None
            self.polling_enable = None


        class Actions(object):
            """
            
            
            .. attribute:: action_name  <key>
            
            	
            	**type**\:   :py:class:`ParsernameIdentity <ydk.models.cisco_ios_xe.cisco_odm.ParsernameIdentity>`
            
            .. attribute:: cdb_xpath
            
            	
            	**type**\:  str
            
            .. attribute:: mode
            
            	
            	**type**\:   :py:class:`ModeEnum <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoOdm.Actions.ModeEnum>`
            
            	**default value**\: poll
            
            .. attribute:: polling_interval
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**default value**\: 120000
            
            

            """

            _prefix = 'codm'
            _revision = '2017-01-25'

            def __init__(self):
                self.parent = None
                self.action_name = None
                self.cdb_xpath = None
                self.mode = None
                self.polling_interval = None

            class ModeEnum(Enum):
                """
                ModeEnum

                .. data:: poll = 0

                .. data:: on_demand = 1

                .. data:: none = 2

                """

                poll = 0

                on_demand = 1

                none = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                    return meta._meta_table['NetconfYang.CiscoOdm.Actions.ModeEnum']


            @property
            def _common_path(self):
                if self.action_name is None:
                    raise YPYModelError('Key property action_name is None')

                return '/cisco-self-mgmt:netconf-yang/cisco-odm:cisco-odm/cisco-odm:actions[cisco-odm:action-name = ' + str(self.action_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.action_name is not None:
                    return True

                if self.cdb_xpath is not None:
                    return True

                if self.mode is not None:
                    return True

                if self.polling_interval is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
                return meta._meta_table['NetconfYang.CiscoOdm.Actions']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-self-mgmt:netconf-yang/cisco-odm:cisco-odm'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.actions is not None:
                for child_ref in self.actions:
                    if child_ref._has_data():
                        return True

            if self.on_demand_default_time is not None:
                return True

            if self.on_demand_enable is not None:
                return True

            if self.polling_enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
            return meta._meta_table['NetconfYang.CiscoOdm']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-self-mgmt:netconf-yang'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.cisco_ia is not None and self.cisco_ia._has_data():
            return True

        if self.cisco_odm is not None and self.cisco_odm._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_self_mgmt as meta
        return meta._meta_table['NetconfYang']['meta_info']


