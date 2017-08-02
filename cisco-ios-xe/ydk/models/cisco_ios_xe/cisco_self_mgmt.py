""" cisco_self_mgmt 

Copyright (c) 2016 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NetconfYang(Entity):
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
        super(NetconfYang, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-yang"
        self.yang_parent_name = "cisco-self-mgmt"

        self.cisco_ia = NetconfYang.CiscoIa()
        self.cisco_ia.parent = self
        self._children_name_map["cisco_ia"] = "cisco-ia"
        self._children_yang_names.add("cisco-ia")

        self.cisco_odm = NetconfYang.CiscoOdm()
        self.cisco_odm.parent = self
        self._children_name_map["cisco_odm"] = "cisco-odm"
        self._children_yang_names.add("cisco-odm")


    class CiscoIa(Entity):
        """
        Customize the behavior of the DMI applications
        
        .. attribute:: auto_sync
        
        	Enables automatic synchronization of the network element's running configuration with the DMI database
        	**type**\:   :py:class:`CiaSyncType <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncType>`
        
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
        	**type**\:   :py:class:`CiaSyncType <ydk.models.cisco_ios_xe.cisco_ia.CiaSyncType>`
        
        	**default value**\: without-defaults
        
        .. attribute:: intelligent_sync
        
        	When enabled, intelligent\-sync monitors all  ttys for configuration changes and replays  these changes to the DMI database once the tty exits configuration mode.  When  disabled, the complete running\-configuration is used to synchronize the DMI database whenever a CLI configuration change is  detected
        	**type**\:  bool
        
        	**default value**\: true
        
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
            super(NetconfYang.CiscoIa, self).__init__()

            self.yang_name = "cisco-ia"
            self.yang_parent_name = "netconf-yang"

            self.auto_sync = YLeaf(YType.enumeration, "auto-sync")

            self.config_change_delay = YLeaf(YType.int16, "config-change-delay")

            self.init_sync = YLeaf(YType.enumeration, "init-sync")

            self.intelligent_sync = YLeaf(YType.boolean, "intelligent-sync")

            self.max_diag_messages_saved = YLeaf(YType.int16, "max-diag-messages-saved")

            self.message_diag_level = YLeaf(YType.int16, "message-diag-level")

            self.nes_ttynum = YLeaf(YType.int16, "nes-ttynum")

            self.post_sync_acl_process = YLeaf(YType.boolean, "post-sync-acl-process")

            self.preserve_paths_enabled = YLeaf(YType.boolean, "preserve-paths-enabled")

            self.process_missing_prc = YLeaf(YType.boolean, "process-missing-prc")

            self.restored = YLeaf(YType.boolean, "restored")

            self.snmp_community_string = YLeaf(YType.str, "snmp-community-string")

            self.blocking = NetconfYang.CiscoIa.Blocking()
            self.blocking.parent = self
            self._children_name_map["blocking"] = "blocking"
            self._children_yang_names.add("blocking")

            self.logging = NetconfYang.CiscoIa.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"
            self._children_yang_names.add("logging")

            self.snmp_trap_control = NetconfYang.CiscoIa.SnmpTrapControl()
            self.snmp_trap_control.parent = self
            self._children_name_map["snmp_trap_control"] = "snmp-trap-control"
            self._children_yang_names.add("snmp-trap-control")

            self.conf_full_sync_cli = YList(self)
            self.conf_parser_msg_ignore = YList(self)
            self.full_sync_cli = YList(self)
            self.parser_msg_ignore = YList(self)
            self.preserve_ned_path = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("auto_sync",
                            "config_change_delay",
                            "init_sync",
                            "intelligent_sync",
                            "max_diag_messages_saved",
                            "message_diag_level",
                            "nes_ttynum",
                            "post_sync_acl_process",
                            "preserve_paths_enabled",
                            "process_missing_prc",
                            "restored",
                            "snmp_community_string") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfYang.CiscoIa, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfYang.CiscoIa, self).__setattr__(name, value)


        class SnmpTrapControl(Entity):
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
                super(NetconfYang.CiscoIa.SnmpTrapControl, self).__init__()

                self.yang_name = "snmp-trap-control"
                self.yang_parent_name = "cisco-ia"

                self.global_forwarding = YLeaf(YType.boolean, "global-forwarding")

                self.trap_list = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("global_forwarding") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.SnmpTrapControl, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.SnmpTrapControl, self).__setattr__(name, value)


            class TrapList(Entity):
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
                    super(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, self).__init__()

                    self.yang_name = "trap-list"
                    self.yang_parent_name = "snmp-trap-control"

                    self.trap_oid = YLeaf(YType.str, "trap-oid")

                    self.description = YLeaf(YType.str, "description")

                    self.forward = YLeaf(YType.boolean, "forward")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("trap_oid",
                                    "description",
                                    "forward") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetconfYang.CiscoIa.SnmpTrapControl.TrapList, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.trap_oid.is_set or
                        self.description.is_set or
                        self.forward.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.trap_oid.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.forward.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "trap-list" + "[trap-oid='" + self.trap_oid.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/snmp-trap-control/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.trap_oid.is_set or self.trap_oid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.trap_oid.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.forward.is_set or self.forward.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.forward.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "trap-oid" or name == "description" or name == "forward"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "trap-oid"):
                        self.trap_oid = value
                        self.trap_oid.value_namespace = name_space
                        self.trap_oid.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "forward"):
                        self.forward = value
                        self.forward.value_namespace = name_space
                        self.forward.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.trap_list:
                    if (c.has_data()):
                        return True
                return self.global_forwarding.is_set

            def has_operation(self):
                for c in self.trap_list:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.global_forwarding.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "snmp-trap-control" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.global_forwarding.is_set or self.global_forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.global_forwarding.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "trap-list"):
                    for c in self.trap_list:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NetconfYang.CiscoIa.SnmpTrapControl.TrapList()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.trap_list.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "trap-list" or name == "global-forwarding"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "global-forwarding"):
                    self.global_forwarding = value
                    self.global_forwarding.value_namespace = name_space
                    self.global_forwarding.value_namespace_prefix = name_space_prefix


        class PreserveNedPath(Entity):
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
                super(NetconfYang.CiscoIa.PreserveNedPath, self).__init__()

                self.yang_name = "preserve-ned-path"
                self.yang_parent_name = "cisco-ia"

                self.xpath = YLeaf(YType.str, "xpath")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("xpath") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.PreserveNedPath, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.PreserveNedPath, self).__setattr__(name, value)

            def has_data(self):
                return self.xpath.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.xpath.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "preserve-ned-path" + "[xpath='" + self.xpath.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.xpath.is_set or self.xpath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.xpath.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "xpath"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "xpath"):
                    self.xpath = value
                    self.xpath.value_namespace = name_space
                    self.xpath.value_namespace_prefix = name_space_prefix


        class ParserMsgIgnore(Entity):
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
                super(NetconfYang.CiscoIa.ParserMsgIgnore, self).__init__()

                self.yang_name = "parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"

                self.message = YLeaf(YType.str, "message")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("message") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.ParserMsgIgnore, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.ParserMsgIgnore, self).__setattr__(name, value)

            def has_data(self):
                return self.message.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.message.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "parser-msg-ignore" + "[message='" + self.message.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.message.is_set or self.message.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "message"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "message"):
                    self.message = value
                    self.message.value_namespace = name_space
                    self.message.value_namespace_prefix = name_space_prefix


        class ConfParserMsgIgnore(Entity):
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
                super(NetconfYang.CiscoIa.ConfParserMsgIgnore, self).__init__()

                self.yang_name = "conf-parser-msg-ignore"
                self.yang_parent_name = "cisco-ia"

                self.message = YLeaf(YType.str, "message")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("message") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.ConfParserMsgIgnore, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.ConfParserMsgIgnore, self).__setattr__(name, value)

            def has_data(self):
                return self.message.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.message.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "conf-parser-msg-ignore" + "[message='" + self.message.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.message.is_set or self.message.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.message.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "message"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "message"):
                    self.message = value
                    self.message.value_namespace = name_space
                    self.message.value_namespace_prefix = name_space_prefix


        class FullSyncCli(Entity):
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
                super(NetconfYang.CiscoIa.FullSyncCli, self).__init__()

                self.yang_name = "full-sync-cli"
                self.yang_parent_name = "cisco-ia"

                self.command = YLeaf(YType.str, "command")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("command") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.FullSyncCli, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.FullSyncCli, self).__setattr__(name, value)

            def has_data(self):
                return self.command.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.command.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "full-sync-cli" + "[command='" + self.command.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.command.is_set or self.command.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.command.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "command"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "command"):
                    self.command = value
                    self.command.value_namespace = name_space
                    self.command.value_namespace_prefix = name_space_prefix


        class ConfFullSyncCli(Entity):
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
                super(NetconfYang.CiscoIa.ConfFullSyncCli, self).__init__()

                self.yang_name = "conf-full-sync-cli"
                self.yang_parent_name = "cisco-ia"

                self.command = YLeaf(YType.str, "command")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("command") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.ConfFullSyncCli, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.ConfFullSyncCli, self).__setattr__(name, value)

            def has_data(self):
                return self.command.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.command.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "conf-full-sync-cli" + "[command='" + self.command.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.command.is_set or self.command.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.command.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "command"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "command"):
                    self.command = value
                    self.command.value_namespace = name_space
                    self.command.value_namespace_prefix = name_space_prefix


        class Logging(Entity):
            """
            Controls logging behavior of DMI applications
            
            .. attribute:: ciaauthd_log_level
            
            	Logging level for CiaAuthDaemon
            	**type**\:   :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: confd_log_level
            
            	Logging level for Confd
            	**type**\:   :py:class:`SyslogSeverity <ydk.models.cisco_ios_xe.cisco_ia.SyslogSeverity>`
            
            	**default value**\: error
            
            .. attribute:: nes_log_level
            
            	Logging level for Network Element Synchronizer
            	**type**\:   :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: odm_log_level
            
            	Logging level for  Operational Data Manager
            	**type**\:   :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: onep_log_level
            
            	Logging level for ONEP
            	**type**\:   :py:class:`OnepLogLevel <ydk.models.cisco_ios_xe.cisco_ia.OnepLogLevel>`
            
            	**default value**\: error
            
            .. attribute:: sync_log_level
            
            	Logging level for Sync\-From Daemon
            	**type**\:   :py:class:`CiaLogLevel <ydk.models.cisco_ios_xe.cisco_ia.CiaLogLevel>`
            
            	**default value**\: error
            
            

            """

            _prefix = 'cisco-ia'
            _revision = '2017-03-02'

            def __init__(self):
                super(NetconfYang.CiscoIa.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "cisco-ia"

                self.ciaauthd_log_level = YLeaf(YType.enumeration, "ciaauthd-log-level")

                self.confd_log_level = YLeaf(YType.enumeration, "confd-log-level")

                self.nes_log_level = YLeaf(YType.enumeration, "nes-log-level")

                self.odm_log_level = YLeaf(YType.enumeration, "odm-log-level")

                self.onep_log_level = YLeaf(YType.enumeration, "onep-log-level")

                self.sync_log_level = YLeaf(YType.enumeration, "sync-log-level")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciaauthd_log_level",
                                "confd_log_level",
                                "nes_log_level",
                                "odm_log_level",
                                "onep_log_level",
                                "sync_log_level") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.Logging, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.Logging, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciaauthd_log_level.is_set or
                    self.confd_log_level.is_set or
                    self.nes_log_level.is_set or
                    self.odm_log_level.is_set or
                    self.onep_log_level.is_set or
                    self.sync_log_level.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciaauthd_log_level.yfilter != YFilter.not_set or
                    self.confd_log_level.yfilter != YFilter.not_set or
                    self.nes_log_level.yfilter != YFilter.not_set or
                    self.odm_log_level.yfilter != YFilter.not_set or
                    self.onep_log_level.yfilter != YFilter.not_set or
                    self.sync_log_level.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "logging" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciaauthd_log_level.is_set or self.ciaauthd_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciaauthd_log_level.get_name_leafdata())
                if (self.confd_log_level.is_set or self.confd_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.confd_log_level.get_name_leafdata())
                if (self.nes_log_level.is_set or self.nes_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nes_log_level.get_name_leafdata())
                if (self.odm_log_level.is_set or self.odm_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.odm_log_level.get_name_leafdata())
                if (self.onep_log_level.is_set or self.onep_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.onep_log_level.get_name_leafdata())
                if (self.sync_log_level.is_set or self.sync_log_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sync_log_level.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciaauthd-log-level" or name == "confd-log-level" or name == "nes-log-level" or name == "odm-log-level" or name == "onep-log-level" or name == "sync-log-level"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciaauthd-log-level"):
                    self.ciaauthd_log_level = value
                    self.ciaauthd_log_level.value_namespace = name_space
                    self.ciaauthd_log_level.value_namespace_prefix = name_space_prefix
                if(value_path == "confd-log-level"):
                    self.confd_log_level = value
                    self.confd_log_level.value_namespace = name_space
                    self.confd_log_level.value_namespace_prefix = name_space_prefix
                if(value_path == "nes-log-level"):
                    self.nes_log_level = value
                    self.nes_log_level.value_namespace = name_space
                    self.nes_log_level.value_namespace_prefix = name_space_prefix
                if(value_path == "odm-log-level"):
                    self.odm_log_level = value
                    self.odm_log_level.value_namespace = name_space
                    self.odm_log_level.value_namespace_prefix = name_space_prefix
                if(value_path == "onep-log-level"):
                    self.onep_log_level = value
                    self.onep_log_level.value_namespace = name_space
                    self.onep_log_level.value_namespace_prefix = name_space_prefix
                if(value_path == "sync-log-level"):
                    self.sync_log_level = value
                    self.sync_log_level.value_namespace = name_space
                    self.sync_log_level.value_namespace_prefix = name_space_prefix


        class Blocking(Entity):
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
                super(NetconfYang.CiscoIa.Blocking, self).__init__()

                self.yang_name = "blocking"
                self.yang_parent_name = "cisco-ia"

                self.cli_blocking_enabled = YLeaf(YType.boolean, "cli-blocking-enabled")

                self.confd_cfg_blocking_enabled = YLeaf(YType.boolean, "confd-cfg-blocking-enabled")

                self.confd_cfg_command = YList(self)
                self.network_element_command = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cli_blocking_enabled",
                                "confd_cfg_blocking_enabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoIa.Blocking, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoIa.Blocking, self).__setattr__(name, value)


            class NetworkElementCommand(Entity):
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
                    super(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, self).__init__()

                    self.yang_name = "network-element-command"
                    self.yang_parent_name = "blocking"

                    self.command = YLeaf(YType.str, "command")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("command") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetconfYang.CiscoIa.Blocking.NetworkElementCommand, self).__setattr__(name, value)

                def has_data(self):
                    return self.command.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.command.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "network-element-command" + "[command='" + self.command.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.command.is_set or self.command.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.command.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "command"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "command"):
                        self.command = value
                        self.command.value_namespace = name_space
                        self.command.value_namespace_prefix = name_space_prefix


            class ConfdCfgCommand(Entity):
                """
                Command line pattern to omit syncing to Confd CDB
                
                .. attribute:: command  <key>
                
                	A regular expression matching command lines which should be blocked from being sent to Confd from the network element
                	**type**\:  str
                
                

                """

                _prefix = 'cisco-ia'
                _revision = '2017-03-02'

                def __init__(self):
                    super(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, self).__init__()

                    self.yang_name = "confd-cfg-command"
                    self.yang_parent_name = "blocking"

                    self.command = YLeaf(YType.str, "command")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("command") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NetconfYang.CiscoIa.Blocking.ConfdCfgCommand, self).__setattr__(name, value)

                def has_data(self):
                    return self.command.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.command.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "confd-cfg-command" + "[command='" + self.command.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/blocking/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.command.is_set or self.command.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.command.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "command"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "command"):
                        self.command = value
                        self.command.value_namespace = name_space
                        self.command.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.confd_cfg_command:
                    if (c.has_data()):
                        return True
                for c in self.network_element_command:
                    if (c.has_data()):
                        return True
                return (
                    self.cli_blocking_enabled.is_set or
                    self.confd_cfg_blocking_enabled.is_set)

            def has_operation(self):
                for c in self.confd_cfg_command:
                    if (c.has_operation()):
                        return True
                for c in self.network_element_command:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.cli_blocking_enabled.yfilter != YFilter.not_set or
                    self.confd_cfg_blocking_enabled.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "blocking" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-ia:cisco-ia/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cli_blocking_enabled.is_set or self.cli_blocking_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cli_blocking_enabled.get_name_leafdata())
                if (self.confd_cfg_blocking_enabled.is_set or self.confd_cfg_blocking_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.confd_cfg_blocking_enabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "confd-cfg-command"):
                    for c in self.confd_cfg_command:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NetconfYang.CiscoIa.Blocking.ConfdCfgCommand()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.confd_cfg_command.append(c)
                    return c

                if (child_yang_name == "network-element-command"):
                    for c in self.network_element_command:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NetconfYang.CiscoIa.Blocking.NetworkElementCommand()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.network_element_command.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "confd-cfg-command" or name == "network-element-command" or name == "cli-blocking-enabled" or name == "confd-cfg-blocking-enabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cli-blocking-enabled"):
                    self.cli_blocking_enabled = value
                    self.cli_blocking_enabled.value_namespace = name_space
                    self.cli_blocking_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "confd-cfg-blocking-enabled"):
                    self.confd_cfg_blocking_enabled = value
                    self.confd_cfg_blocking_enabled.value_namespace = name_space
                    self.confd_cfg_blocking_enabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.conf_full_sync_cli:
                if (c.has_data()):
                    return True
            for c in self.conf_parser_msg_ignore:
                if (c.has_data()):
                    return True
            for c in self.full_sync_cli:
                if (c.has_data()):
                    return True
            for c in self.parser_msg_ignore:
                if (c.has_data()):
                    return True
            for c in self.preserve_ned_path:
                if (c.has_data()):
                    return True
            return (
                self.auto_sync.is_set or
                self.config_change_delay.is_set or
                self.init_sync.is_set or
                self.intelligent_sync.is_set or
                self.max_diag_messages_saved.is_set or
                self.message_diag_level.is_set or
                self.nes_ttynum.is_set or
                self.post_sync_acl_process.is_set or
                self.preserve_paths_enabled.is_set or
                self.process_missing_prc.is_set or
                self.restored.is_set or
                self.snmp_community_string.is_set or
                (self.blocking is not None and self.blocking.has_data()) or
                (self.logging is not None and self.logging.has_data()) or
                (self.snmp_trap_control is not None and self.snmp_trap_control.has_data()))

        def has_operation(self):
            for c in self.conf_full_sync_cli:
                if (c.has_operation()):
                    return True
            for c in self.conf_parser_msg_ignore:
                if (c.has_operation()):
                    return True
            for c in self.full_sync_cli:
                if (c.has_operation()):
                    return True
            for c in self.parser_msg_ignore:
                if (c.has_operation()):
                    return True
            for c in self.preserve_ned_path:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.auto_sync.yfilter != YFilter.not_set or
                self.config_change_delay.yfilter != YFilter.not_set or
                self.init_sync.yfilter != YFilter.not_set or
                self.intelligent_sync.yfilter != YFilter.not_set or
                self.max_diag_messages_saved.yfilter != YFilter.not_set or
                self.message_diag_level.yfilter != YFilter.not_set or
                self.nes_ttynum.yfilter != YFilter.not_set or
                self.post_sync_acl_process.yfilter != YFilter.not_set or
                self.preserve_paths_enabled.yfilter != YFilter.not_set or
                self.process_missing_prc.yfilter != YFilter.not_set or
                self.restored.yfilter != YFilter.not_set or
                self.snmp_community_string.yfilter != YFilter.not_set or
                (self.blocking is not None and self.blocking.has_operation()) or
                (self.logging is not None and self.logging.has_operation()) or
                (self.snmp_trap_control is not None and self.snmp_trap_control.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cisco-ia:cisco-ia" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-self-mgmt:netconf-yang/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.auto_sync.is_set or self.auto_sync.yfilter != YFilter.not_set):
                leaf_name_data.append(self.auto_sync.get_name_leafdata())
            if (self.config_change_delay.is_set or self.config_change_delay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.config_change_delay.get_name_leafdata())
            if (self.init_sync.is_set or self.init_sync.yfilter != YFilter.not_set):
                leaf_name_data.append(self.init_sync.get_name_leafdata())
            if (self.intelligent_sync.is_set or self.intelligent_sync.yfilter != YFilter.not_set):
                leaf_name_data.append(self.intelligent_sync.get_name_leafdata())
            if (self.max_diag_messages_saved.is_set or self.max_diag_messages_saved.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_diag_messages_saved.get_name_leafdata())
            if (self.message_diag_level.is_set or self.message_diag_level.yfilter != YFilter.not_set):
                leaf_name_data.append(self.message_diag_level.get_name_leafdata())
            if (self.nes_ttynum.is_set or self.nes_ttynum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nes_ttynum.get_name_leafdata())
            if (self.post_sync_acl_process.is_set or self.post_sync_acl_process.yfilter != YFilter.not_set):
                leaf_name_data.append(self.post_sync_acl_process.get_name_leafdata())
            if (self.preserve_paths_enabled.is_set or self.preserve_paths_enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.preserve_paths_enabled.get_name_leafdata())
            if (self.process_missing_prc.is_set or self.process_missing_prc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.process_missing_prc.get_name_leafdata())
            if (self.restored.is_set or self.restored.yfilter != YFilter.not_set):
                leaf_name_data.append(self.restored.get_name_leafdata())
            if (self.snmp_community_string.is_set or self.snmp_community_string.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmp_community_string.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "blocking"):
                if (self.blocking is None):
                    self.blocking = NetconfYang.CiscoIa.Blocking()
                    self.blocking.parent = self
                    self._children_name_map["blocking"] = "blocking"
                return self.blocking

            if (child_yang_name == "conf-full-sync-cli"):
                for c in self.conf_full_sync_cli:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoIa.ConfFullSyncCli()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.conf_full_sync_cli.append(c)
                return c

            if (child_yang_name == "conf-parser-msg-ignore"):
                for c in self.conf_parser_msg_ignore:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoIa.ConfParserMsgIgnore()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.conf_parser_msg_ignore.append(c)
                return c

            if (child_yang_name == "full-sync-cli"):
                for c in self.full_sync_cli:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoIa.FullSyncCli()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.full_sync_cli.append(c)
                return c

            if (child_yang_name == "logging"):
                if (self.logging is None):
                    self.logging = NetconfYang.CiscoIa.Logging()
                    self.logging.parent = self
                    self._children_name_map["logging"] = "logging"
                return self.logging

            if (child_yang_name == "parser-msg-ignore"):
                for c in self.parser_msg_ignore:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoIa.ParserMsgIgnore()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.parser_msg_ignore.append(c)
                return c

            if (child_yang_name == "preserve-ned-path"):
                for c in self.preserve_ned_path:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoIa.PreserveNedPath()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.preserve_ned_path.append(c)
                return c

            if (child_yang_name == "snmp-trap-control"):
                if (self.snmp_trap_control is None):
                    self.snmp_trap_control = NetconfYang.CiscoIa.SnmpTrapControl()
                    self.snmp_trap_control.parent = self
                    self._children_name_map["snmp_trap_control"] = "snmp-trap-control"
                return self.snmp_trap_control

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "blocking" or name == "conf-full-sync-cli" or name == "conf-parser-msg-ignore" or name == "full-sync-cli" or name == "logging" or name == "parser-msg-ignore" or name == "preserve-ned-path" or name == "snmp-trap-control" or name == "auto-sync" or name == "config-change-delay" or name == "init-sync" or name == "intelligent-sync" or name == "max-diag-messages-saved" or name == "message-diag-level" or name == "nes-ttynum" or name == "post-sync-acl-process" or name == "preserve-paths-enabled" or name == "process-missing-prc" or name == "restored" or name == "snmp-community-string"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "auto-sync"):
                self.auto_sync = value
                self.auto_sync.value_namespace = name_space
                self.auto_sync.value_namespace_prefix = name_space_prefix
            if(value_path == "config-change-delay"):
                self.config_change_delay = value
                self.config_change_delay.value_namespace = name_space
                self.config_change_delay.value_namespace_prefix = name_space_prefix
            if(value_path == "init-sync"):
                self.init_sync = value
                self.init_sync.value_namespace = name_space
                self.init_sync.value_namespace_prefix = name_space_prefix
            if(value_path == "intelligent-sync"):
                self.intelligent_sync = value
                self.intelligent_sync.value_namespace = name_space
                self.intelligent_sync.value_namespace_prefix = name_space_prefix
            if(value_path == "max-diag-messages-saved"):
                self.max_diag_messages_saved = value
                self.max_diag_messages_saved.value_namespace = name_space
                self.max_diag_messages_saved.value_namespace_prefix = name_space_prefix
            if(value_path == "message-diag-level"):
                self.message_diag_level = value
                self.message_diag_level.value_namespace = name_space
                self.message_diag_level.value_namespace_prefix = name_space_prefix
            if(value_path == "nes-ttynum"):
                self.nes_ttynum = value
                self.nes_ttynum.value_namespace = name_space
                self.nes_ttynum.value_namespace_prefix = name_space_prefix
            if(value_path == "post-sync-acl-process"):
                self.post_sync_acl_process = value
                self.post_sync_acl_process.value_namespace = name_space
                self.post_sync_acl_process.value_namespace_prefix = name_space_prefix
            if(value_path == "preserve-paths-enabled"):
                self.preserve_paths_enabled = value
                self.preserve_paths_enabled.value_namespace = name_space
                self.preserve_paths_enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "process-missing-prc"):
                self.process_missing_prc = value
                self.process_missing_prc.value_namespace = name_space
                self.process_missing_prc.value_namespace_prefix = name_space_prefix
            if(value_path == "restored"):
                self.restored = value
                self.restored.value_namespace = name_space
                self.restored.value_namespace_prefix = name_space_prefix
            if(value_path == "snmp-community-string"):
                self.snmp_community_string = value
                self.snmp_community_string.value_namespace = name_space
                self.snmp_community_string.value_namespace_prefix = name_space_prefix


    class CiscoOdm(Entity):
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
        _revision = '2017-04-25'

        def __init__(self):
            super(NetconfYang.CiscoOdm, self).__init__()

            self.yang_name = "cisco-odm"
            self.yang_parent_name = "netconf-yang"

            self.on_demand_default_time = YLeaf(YType.uint32, "on-demand-default-time")

            self.on_demand_enable = YLeaf(YType.boolean, "on-demand-enable")

            self.polling_enable = YLeaf(YType.boolean, "polling-enable")

            self.actions = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("on_demand_default_time",
                            "on_demand_enable",
                            "polling_enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfYang.CiscoOdm, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfYang.CiscoOdm, self).__setattr__(name, value)


        class Actions(Entity):
            """
            
            
            .. attribute:: action_name  <key>
            
            	
            	**type**\:   :py:class:`Parsername <ydk.models.cisco_ios_xe.cisco_odm.Parsername>`
            
            .. attribute:: cdb_xpath
            
            	
            	**type**\:  str
            
            .. attribute:: mode
            
            	
            	**type**\:   :py:class:`Mode <ydk.models.cisco_ios_xe.cisco_self_mgmt.NetconfYang.CiscoOdm.Actions.Mode>`
            
            	**default value**\: poll
            
            .. attribute:: polling_interval
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**default value**\: 120000
            
            

            """

            _prefix = 'codm'
            _revision = '2017-04-25'

            def __init__(self):
                super(NetconfYang.CiscoOdm.Actions, self).__init__()

                self.yang_name = "actions"
                self.yang_parent_name = "cisco-odm"

                self.action_name = YLeaf(YType.identityref, "action-name")

                self.cdb_xpath = YLeaf(YType.str, "cdb-xpath")

                self.mode = YLeaf(YType.enumeration, "mode")

                self.polling_interval = YLeaf(YType.uint32, "polling-interval")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("action_name",
                                "cdb_xpath",
                                "mode",
                                "polling_interval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.CiscoOdm.Actions, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.CiscoOdm.Actions, self).__setattr__(name, value)

            class Mode(Enum):
                """
                Mode

                .. data:: poll = 0

                .. data:: on_demand = 1

                .. data:: none = 2

                """

                poll = Enum.YLeaf(0, "poll")

                on_demand = Enum.YLeaf(1, "on-demand")

                none = Enum.YLeaf(2, "none")


            def has_data(self):
                return (
                    self.action_name.is_set or
                    self.cdb_xpath.is_set or
                    self.mode.is_set or
                    self.polling_interval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.action_name.yfilter != YFilter.not_set or
                    self.cdb_xpath.yfilter != YFilter.not_set or
                    self.mode.yfilter != YFilter.not_set or
                    self.polling_interval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "actions" + "[action-name='" + self.action_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-self-mgmt:netconf-yang/cisco-odm:cisco-odm/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.action_name.is_set or self.action_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.action_name.get_name_leafdata())
                if (self.cdb_xpath.is_set or self.cdb_xpath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cdb_xpath.get_name_leafdata())
                if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mode.get_name_leafdata())
                if (self.polling_interval.is_set or self.polling_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.polling_interval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "action-name" or name == "cdb-xpath" or name == "mode" or name == "polling-interval"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "action-name"):
                    self.action_name = value
                    self.action_name.value_namespace = name_space
                    self.action_name.value_namespace_prefix = name_space_prefix
                if(value_path == "cdb-xpath"):
                    self.cdb_xpath = value
                    self.cdb_xpath.value_namespace = name_space
                    self.cdb_xpath.value_namespace_prefix = name_space_prefix
                if(value_path == "mode"):
                    self.mode = value
                    self.mode.value_namespace = name_space
                    self.mode.value_namespace_prefix = name_space_prefix
                if(value_path == "polling-interval"):
                    self.polling_interval = value
                    self.polling_interval.value_namespace = name_space
                    self.polling_interval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.actions:
                if (c.has_data()):
                    return True
            return (
                self.on_demand_default_time.is_set or
                self.on_demand_enable.is_set or
                self.polling_enable.is_set)

        def has_operation(self):
            for c in self.actions:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.on_demand_default_time.yfilter != YFilter.not_set or
                self.on_demand_enable.yfilter != YFilter.not_set or
                self.polling_enable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cisco-odm:cisco-odm" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-self-mgmt:netconf-yang/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.on_demand_default_time.is_set or self.on_demand_default_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.on_demand_default_time.get_name_leafdata())
            if (self.on_demand_enable.is_set or self.on_demand_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.on_demand_enable.get_name_leafdata())
            if (self.polling_enable.is_set or self.polling_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.polling_enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "actions"):
                for c in self.actions:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NetconfYang.CiscoOdm.Actions()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.actions.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "actions" or name == "on-demand-default-time" or name == "on-demand-enable" or name == "polling-enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "on-demand-default-time"):
                self.on_demand_default_time = value
                self.on_demand_default_time.value_namespace = name_space
                self.on_demand_default_time.value_namespace_prefix = name_space_prefix
            if(value_path == "on-demand-enable"):
                self.on_demand_enable = value
                self.on_demand_enable.value_namespace = name_space
                self.on_demand_enable.value_namespace_prefix = name_space_prefix
            if(value_path == "polling-enable"):
                self.polling_enable = value
                self.polling_enable.value_namespace = name_space
                self.polling_enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.cisco_ia is not None and self.cisco_ia.has_data()) or
            (self.cisco_odm is not None and self.cisco_odm.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cisco_ia is not None and self.cisco_ia.has_operation()) or
            (self.cisco_odm is not None and self.cisco_odm.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-self-mgmt:netconf-yang" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cisco-ia"):
            if (self.cisco_ia is None):
                self.cisco_ia = NetconfYang.CiscoIa()
                self.cisco_ia.parent = self
                self._children_name_map["cisco_ia"] = "cisco-ia"
            return self.cisco_ia

        if (child_yang_name == "cisco-odm"):
            if (self.cisco_odm is None):
                self.cisco_odm = NetconfYang.CiscoOdm()
                self.cisco_odm.parent = self
                self._children_name_map["cisco_odm"] = "cisco-odm"
            return self.cisco_odm

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cisco-ia" or name == "cisco-odm"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NetconfYang()
        return self._top_entity

