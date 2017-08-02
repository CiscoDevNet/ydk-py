""" Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma\-gbl package configuration.

This module contains definitions
for the following management objects\:
  pppoe\-cfg\: PPPOE configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PppoeInvalidSessionIdBehavior(Enum):
    """
    PppoeInvalidSessionIdBehavior

    Pppoe invalid session id behavior

    .. data:: drop = 0

    	Drop packets with an invalid session ID

    .. data:: log = 1

    	Log packets with an invalid session ID

    """

    drop = Enum.YLeaf(0, "drop")

    log = Enum.YLeaf(1, "log")



class PppoeCfg(Entity):
    """
    PPPOE configuration data
    
    .. attribute:: in_flight_window
    
    	Set the PPPoE in\-flight window size
    	**type**\:  int
    
    	**range:** 1..20000
    
    .. attribute:: pppoe_bba_groups
    
    	PPPoE BBA\-Group configuration data
    	**type**\:   :py:class:`PppoeBbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups>`
    
    .. attribute:: session_id_space_flat
    
    	Disable per\-parent session ID spaces
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(PppoeCfg, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe-cfg"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg"

        self.in_flight_window = YLeaf(YType.uint32, "in-flight-window")

        self.session_id_space_flat = YLeaf(YType.empty, "session-id-space-flat")

        self.pppoe_bba_groups = PppoeCfg.PppoeBbaGroups()
        self.pppoe_bba_groups.parent = self
        self._children_name_map["pppoe_bba_groups"] = "pppoe-bba-groups"
        self._children_yang_names.add("pppoe-bba-groups")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("in_flight_window",
                        "session_id_space_flat") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(PppoeCfg, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(PppoeCfg, self).__setattr__(name, value)


    class PppoeBbaGroups(Entity):
        """
        PPPoE BBA\-Group configuration data
        
        .. attribute:: pppoe_bba_group
        
        	PPPoE BBA\-Group configuration data
        	**type**\: list of    :py:class:`PppoeBbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(PppoeCfg.PppoeBbaGroups, self).__init__()

            self.yang_name = "pppoe-bba-groups"
            self.yang_parent_name = "pppoe-cfg"

            self.pppoe_bba_group = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PppoeCfg.PppoeBbaGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PppoeCfg.PppoeBbaGroups, self).__setattr__(name, value)


        class PppoeBbaGroup(Entity):
            """
            PPPoE BBA\-Group configuration data
            
            .. attribute:: bba_group  <key>
            
            	BBA\-Group name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: completion_timeout
            
            	PPPoE session completion timeout
            	**type**\:  int
            
            	**range:** 30..600
            
            .. attribute:: control_packets
            
            	PPPoE control\-packet configuration data
            	**type**\:   :py:class:`ControlPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets>`
            
            .. attribute:: enable_padt_after_shut_down
            
            	Enable padt after shutdown
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: invalid_session_id
            
            	Invalid session\-ID behavior
            	**type**\:   :py:class:`PppoeInvalidSessionIdBehavior <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeInvalidSessionIdBehavior>`
            
            .. attribute:: mtu
            
            	PPPoE default MTU
            	**type**\:  int
            
            	**range:** 500..2000
            
            .. attribute:: pa_do_delay
            
            	PPPoE PADO delay configuration data
            	**type**\:   :py:class:`PaDoDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay>`
            
            .. attribute:: sessions
            
            	PPPoE session configuration data
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions>`
            
            .. attribute:: tag
            
            	PPPoE tag configuration data
            	**type**\:   :py:class:`Tag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-gbl-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup, self).__init__()

                self.yang_name = "pppoe-bba-group"
                self.yang_parent_name = "pppoe-bba-groups"

                self.bba_group = YLeaf(YType.str, "bba-group")

                self.completion_timeout = YLeaf(YType.uint32, "completion-timeout")

                self.enable_padt_after_shut_down = YLeaf(YType.empty, "enable-padt-after-shut-down")

                self.invalid_session_id = YLeaf(YType.enumeration, "invalid-session-id")

                self.mtu = YLeaf(YType.uint32, "mtu")

                self.control_packets = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets()
                self.control_packets.parent = self
                self._children_name_map["control_packets"] = "control-packets"
                self._children_yang_names.add("control-packets")

                self.pa_do_delay = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay()
                self.pa_do_delay.parent = self
                self._children_name_map["pa_do_delay"] = "pa-do-delay"
                self._children_yang_names.add("pa-do-delay")

                self.sessions = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")

                self.tag = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag()
                self.tag.parent = self
                self._children_name_map["tag"] = "tag"
                self._children_yang_names.add("tag")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bba_group",
                                "completion_timeout",
                                "enable_padt_after_shut_down",
                                "invalid_session_id",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup, self).__setattr__(name, value)


            class Tag(Entity):
                """
                PPPoE tag configuration data
                
                .. attribute:: ac_name
                
                	The name to include in the AC tag
                	**type**\:  str
                
                .. attribute:: padr
                
                	PADR packets
                	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr>`
                
                .. attribute:: ppp_max_payload
                
                	Minimum and maximum payloads
                	**type**\:   :py:class:`PppMaxPayload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload>`
                
                .. attribute:: ppp_max_payload_deny
                
                	Ignore the ppp\-max\-payload tag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: service_name_configureds
                
                	Service name
                	**type**\:   :py:class:`ServiceNameConfigureds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds>`
                
                .. attribute:: service_selection_disable
                
                	Disable advertising of unrequested service names
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag, self).__init__()

                    self.yang_name = "tag"
                    self.yang_parent_name = "pppoe-bba-group"

                    self.ac_name = YLeaf(YType.str, "ac-name")

                    self.ppp_max_payload_deny = YLeaf(YType.empty, "ppp-max-payload-deny")

                    self.service_selection_disable = YLeaf(YType.empty, "service-selection-disable")

                    self.padr = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr()
                    self.padr.parent = self
                    self._children_name_map["padr"] = "padr"
                    self._children_yang_names.add("padr")

                    self.ppp_max_payload = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload()
                    self.ppp_max_payload.parent = self
                    self._children_name_map["ppp_max_payload"] = "ppp-max-payload"
                    self._children_yang_names.add("ppp-max-payload")

                    self.service_name_configureds = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds()
                    self.service_name_configureds.parent = self
                    self._children_name_map["service_name_configureds"] = "service-name-configureds"
                    self._children_yang_names.add("service-name-configureds")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ac_name",
                                    "ppp_max_payload_deny",
                                    "service_selection_disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag, self).__setattr__(name, value)


                class Padr(Entity):
                    """
                    PADR packets
                    
                    .. attribute:: invalid_payload_allow
                    
                    	Allow sessions to come up with invalid\-payload
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: session_unique_relay_session_id
                    
                    	Allow sessions to come up with unique relay\-session\-id in padr
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr, self).__init__()

                        self.yang_name = "padr"
                        self.yang_parent_name = "tag"

                        self.invalid_payload_allow = YLeaf(YType.empty, "invalid-payload-allow")

                        self.session_unique_relay_session_id = YLeaf(YType.empty, "session-unique-relay-session-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("invalid_payload_allow",
                                        "session_unique_relay_session_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.invalid_payload_allow.is_set or
                            self.session_unique_relay_session_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.invalid_payload_allow.yfilter != YFilter.not_set or
                            self.session_unique_relay_session_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "padr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.invalid_payload_allow.is_set or self.invalid_payload_allow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_payload_allow.get_name_leafdata())
                        if (self.session_unique_relay_session_id.is_set or self.session_unique_relay_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_unique_relay_session_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "invalid-payload-allow" or name == "session-unique-relay-session-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "invalid-payload-allow"):
                            self.invalid_payload_allow = value
                            self.invalid_payload_allow.value_namespace = name_space
                            self.invalid_payload_allow.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-unique-relay-session-id"):
                            self.session_unique_relay_session_id = value
                            self.session_unique_relay_session_id.value_namespace = name_space
                            self.session_unique_relay_session_id.value_namespace_prefix = name_space_prefix


                class ServiceNameConfigureds(Entity):
                    """
                    Service name
                    
                    .. attribute:: service_name_configured
                    
                    	Service name supported on this group
                    	**type**\: list of    :py:class:`ServiceNameConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds, self).__init__()

                        self.yang_name = "service-name-configureds"
                        self.yang_parent_name = "tag"

                        self.service_name_configured = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds, self).__setattr__(name, value)


                    class ServiceNameConfigured(Entity):
                        """
                        Service name supported on this group
                        
                        .. attribute:: name  <key>
                        
                        	Service name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured, self).__init__()

                            self.yang_name = "service-name-configured"
                            self.yang_parent_name = "service-name-configureds"

                            self.name = YLeaf(YType.str, "name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured, self).__setattr__(name, value)

                        def has_data(self):
                            return self.name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "service-name-configured" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.service_name_configured:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.service_name_configured:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-name-configureds" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "service-name-configured"):
                            for c in self.service_name_configured:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.service_name_configured.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "service-name-configured"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class PppMaxPayload(Entity):
                    """
                    Minimum and maximum payloads
                    
                    .. attribute:: max
                    
                    	Maximum payload
                    	**type**\:  int
                    
                    	**range:** 500..2000
                    
                    .. attribute:: min
                    
                    	Minimum payload
                    	**type**\:  int
                    
                    	**range:** 500..2000
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload, self).__init__()

                        self.yang_name = "ppp-max-payload"
                        self.yang_parent_name = "tag"

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ppp-max-payload" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.ac_name.is_set or
                        self.ppp_max_payload_deny.is_set or
                        self.service_selection_disable.is_set or
                        (self.padr is not None and self.padr.has_data()) or
                        (self.ppp_max_payload is not None and self.ppp_max_payload.has_data()) or
                        (self.service_name_configureds is not None and self.service_name_configureds.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ac_name.yfilter != YFilter.not_set or
                        self.ppp_max_payload_deny.yfilter != YFilter.not_set or
                        self.service_selection_disable.yfilter != YFilter.not_set or
                        (self.padr is not None and self.padr.has_operation()) or
                        (self.ppp_max_payload is not None and self.ppp_max_payload.has_operation()) or
                        (self.service_name_configureds is not None and self.service_name_configureds.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tag" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ac_name.is_set or self.ac_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ac_name.get_name_leafdata())
                    if (self.ppp_max_payload_deny.is_set or self.ppp_max_payload_deny.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ppp_max_payload_deny.get_name_leafdata())
                    if (self.service_selection_disable.is_set or self.service_selection_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service_selection_disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "padr"):
                        if (self.padr is None):
                            self.padr = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr()
                            self.padr.parent = self
                            self._children_name_map["padr"] = "padr"
                        return self.padr

                    if (child_yang_name == "ppp-max-payload"):
                        if (self.ppp_max_payload is None):
                            self.ppp_max_payload = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload()
                            self.ppp_max_payload.parent = self
                            self._children_name_map["ppp_max_payload"] = "ppp-max-payload"
                        return self.ppp_max_payload

                    if (child_yang_name == "service-name-configureds"):
                        if (self.service_name_configureds is None):
                            self.service_name_configureds = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds()
                            self.service_name_configureds.parent = self
                            self._children_name_map["service_name_configureds"] = "service-name-configureds"
                        return self.service_name_configureds

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "padr" or name == "ppp-max-payload" or name == "service-name-configureds" or name == "ac-name" or name == "ppp-max-payload-deny" or name == "service-selection-disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ac-name"):
                        self.ac_name = value
                        self.ac_name.value_namespace = name_space
                        self.ac_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ppp-max-payload-deny"):
                        self.ppp_max_payload_deny = value
                        self.ppp_max_payload_deny.value_namespace = name_space
                        self.ppp_max_payload_deny.value_namespace_prefix = name_space_prefix
                    if(value_path == "service-selection-disable"):
                        self.service_selection_disable = value
                        self.service_selection_disable.value_namespace = name_space
                        self.service_selection_disable.value_namespace_prefix = name_space_prefix


            class Sessions(Entity):
                """
                PPPoE session configuration data
                
                .. attribute:: access_interface_limit
                
                	Set per\-access interface limit
                	**type**\:   :py:class:`AccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_limit
                
                	Set Circuit ID and Remote ID session limit/threshold
                	**type**\:   :py:class:`CircuitIdAndRemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_throttle
                
                	Set Circuit ID and Remote ID session throttle
                	**type**\:   :py:class:`CircuitIdAndRemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_limit
                
                	Set Circuit ID session limit and threshold
                	**type**\:   :py:class:`CircuitIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_throttle
                
                	Set Circuit ID session throttle
                	**type**\:   :py:class:`CircuitIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_limit
                
                	Set Inner VLAN session limit and threshold
                	**type**\:   :py:class:`InnerVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_throttle
                
                	Set Inner VLAN session throttle
                	**type**\:   :py:class:`InnerVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold
                	**type**\:   :py:class:`MacAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_throttle
                
                	Set per\-MAC/Access Interface throttle
                	**type**\:   :py:class:`MacAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold for IWF sessions
                	**type**\:   :py:class:`MacIwfAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_throttle
                
                	Set per\-MAC/Access interface throttle for IWF sessions
                	**type**\:   :py:class:`MacIwfAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_limit
                
                	Set per\-MAC session limit and threshold for IWF sessions
                	**type**\:   :py:class:`MacIwfLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_limit
                
                	Set per\-MAC address session limit and threshold
                	**type**\:   :py:class:`MacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_throttle
                
                	Set per\-MAC throttle
                	**type**\:   :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: max_limit
                
                	Set per\-card session limit and threshold
                	**type**\:   :py:class:`MaxLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_limit
                
                	Set Outer VLAN session limit and threshold
                	**type**\:   :py:class:`OuterVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_throttle
                
                	Set Outer VLAN session throttle
                	**type**\:   :py:class:`OuterVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_limit
                
                	Set Remote ID session limit and threshold
                	**type**\:   :py:class:`RemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_throttle
                
                	Set Remote ID session throttle
                	**type**\:   :py:class:`RemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: vlan_limit
                
                	Set VLAN (inner + outer tags) session limit and threshold
                	**type**\:   :py:class:`VlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: vlan_throttle
                
                	Set VLAN (inner + outer tags) session throttle
                	**type**\:   :py:class:`VlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "pppoe-bba-group"

                    self.access_interface_limit = None
                    self._children_name_map["access_interface_limit"] = "access-interface-limit"
                    self._children_yang_names.add("access-interface-limit")

                    self.circuit_id_and_remote_id_limit = None
                    self._children_name_map["circuit_id_and_remote_id_limit"] = "circuit-id-and-remote-id-limit"
                    self._children_yang_names.add("circuit-id-and-remote-id-limit")

                    self.circuit_id_and_remote_id_throttle = None
                    self._children_name_map["circuit_id_and_remote_id_throttle"] = "circuit-id-and-remote-id-throttle"
                    self._children_yang_names.add("circuit-id-and-remote-id-throttle")

                    self.circuit_id_limit = None
                    self._children_name_map["circuit_id_limit"] = "circuit-id-limit"
                    self._children_yang_names.add("circuit-id-limit")

                    self.circuit_id_throttle = None
                    self._children_name_map["circuit_id_throttle"] = "circuit-id-throttle"
                    self._children_yang_names.add("circuit-id-throttle")

                    self.inner_vlan_limit = None
                    self._children_name_map["inner_vlan_limit"] = "inner-vlan-limit"
                    self._children_yang_names.add("inner-vlan-limit")

                    self.inner_vlan_throttle = None
                    self._children_name_map["inner_vlan_throttle"] = "inner-vlan-throttle"
                    self._children_yang_names.add("inner-vlan-throttle")

                    self.mac_access_interface_limit = None
                    self._children_name_map["mac_access_interface_limit"] = "mac-access-interface-limit"
                    self._children_yang_names.add("mac-access-interface-limit")

                    self.mac_access_interface_throttle = None
                    self._children_name_map["mac_access_interface_throttle"] = "mac-access-interface-throttle"
                    self._children_yang_names.add("mac-access-interface-throttle")

                    self.mac_iwf_access_interface_limit = None
                    self._children_name_map["mac_iwf_access_interface_limit"] = "mac-iwf-access-interface-limit"
                    self._children_yang_names.add("mac-iwf-access-interface-limit")

                    self.mac_iwf_access_interface_throttle = None
                    self._children_name_map["mac_iwf_access_interface_throttle"] = "mac-iwf-access-interface-throttle"
                    self._children_yang_names.add("mac-iwf-access-interface-throttle")

                    self.mac_iwf_limit = None
                    self._children_name_map["mac_iwf_limit"] = "mac-iwf-limit"
                    self._children_yang_names.add("mac-iwf-limit")

                    self.mac_limit = None
                    self._children_name_map["mac_limit"] = "mac-limit"
                    self._children_yang_names.add("mac-limit")

                    self.mac_throttle = None
                    self._children_name_map["mac_throttle"] = "mac-throttle"
                    self._children_yang_names.add("mac-throttle")

                    self.max_limit = None
                    self._children_name_map["max_limit"] = "max-limit"
                    self._children_yang_names.add("max-limit")

                    self.outer_vlan_limit = None
                    self._children_name_map["outer_vlan_limit"] = "outer-vlan-limit"
                    self._children_yang_names.add("outer-vlan-limit")

                    self.outer_vlan_throttle = None
                    self._children_name_map["outer_vlan_throttle"] = "outer-vlan-throttle"
                    self._children_yang_names.add("outer-vlan-throttle")

                    self.remote_id_limit = None
                    self._children_name_map["remote_id_limit"] = "remote-id-limit"
                    self._children_yang_names.add("remote-id-limit")

                    self.remote_id_throttle = None
                    self._children_name_map["remote_id_throttle"] = "remote-id-throttle"
                    self._children_yang_names.add("remote-id-throttle")

                    self.vlan_limit = None
                    self._children_name_map["vlan_limit"] = "vlan-limit"
                    self._children_yang_names.add("vlan-limit")

                    self.vlan_throttle = None
                    self._children_name_map["vlan_throttle"] = "vlan-throttle"
                    self._children_yang_names.add("vlan-throttle")


                class VlanThrottle(Entity):
                    """
                    Set VLAN (inner + outer tags) session
                    throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle, self).__init__()

                        self.yang_name = "vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vlan-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class InnerVlanThrottle(Entity):
                    """
                    Set Inner VLAN session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle, self).__init__()

                        self.yang_name = "inner-vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inner-vlan-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class RemoteIdLimit(Entity):
                    """
                    Set Remote ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Remote ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Remote ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit, self).__init__()

                        self.yang_name = "remote-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-id-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class MacIwfAccessInterfaceThrottle(Entity):
                    """
                    Set per\-MAC/Access interface throttle for IWF
                    sessions
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle, self).__init__()

                        self.yang_name = "mac-iwf-access-interface-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-iwf-access-interface-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class AccessInterfaceLimit(Entity):
                    """
                    Set per\-access interface limit
                    
                    .. attribute:: limit
                    
                    	Per\-access interface session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-access interface session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit, self).__init__()

                        self.yang_name = "access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-interface-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class MacAccessInterfaceThrottle(Entity):
                    """
                    Set per\-MAC/Access Interface throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle, self).__init__()

                        self.yang_name = "mac-access-interface-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-access-interface-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class OuterVlanLimit(Entity):
                    """
                    Set Outer VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Outer VLAN limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Outer VLAN threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit, self).__init__()

                        self.yang_name = "outer-vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outer-vlan-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class CircuitIdThrottle(Entity):
                    """
                    Set Circuit ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle, self).__init__()

                        self.yang_name = "circuit-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class MacLimit(Entity):
                    """
                    Set per\-MAC address session limit and
                    threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit, self).__init__()

                        self.yang_name = "mac-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class CircuitIdLimit(Entity):
                    """
                    Set Circuit ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit, self).__init__()

                        self.yang_name = "circuit-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class MacIwfLimit(Entity):
                    """
                    Set per\-MAC session limit and threshold for
                    IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit, self).__init__()

                        self.yang_name = "mac-iwf-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-iwf-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class MacIwfAccessInterfaceLimit(Entity):
                    """
                    Set per\-MAC access interface session limit
                    and threshold for IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit, self).__init__()

                        self.yang_name = "mac-iwf-access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-iwf-access-interface-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class InnerVlanLimit(Entity):
                    """
                    Set Inner VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Inner VLAN limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Inner VLAN threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit, self).__init__()

                        self.yang_name = "inner-vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "inner-vlan-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class OuterVlanThrottle(Entity):
                    """
                    Set Outer VLAN session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle, self).__init__()

                        self.yang_name = "outer-vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "outer-vlan-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class MacThrottle(Entity):
                    """
                    Set per\-MAC throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle, self).__init__()

                        self.yang_name = "mac-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class CircuitIdAndRemoteIdLimit(Entity):
                    """
                    Set Circuit ID and Remote ID session
                    limit/threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit, self).__init__()

                        self.yang_name = "circuit-id-and-remote-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-and-remote-id-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class VlanLimit(Entity):
                    """
                    Set VLAN (inner + outer tags) session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-VLAN (inner + outer tags) limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-VLAN (inner + outer tags) threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit, self).__init__()

                        self.yang_name = "vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vlan-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class MacAccessInterfaceLimit(Entity):
                    """
                    Set per\-MAC access interface session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit, self).__init__()

                        self.yang_name = "mac-access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mac-access-interface-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class RemoteIdThrottle(Entity):
                    """
                    Set Remote ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle, self).__init__()

                        self.yang_name = "remote-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-id-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix


                class MaxLimit(Entity):
                    """
                    Set per\-card session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-card session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-card session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit, self).__init__()

                        self.yang_name = "max-limit"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.limit = YLeaf(YType.uint32, "limit")

                        self.threshold = YLeaf(YType.uint32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("limit",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.limit.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.limit.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "max-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.limit.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "limit" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "limit"):
                            self.limit = value
                            self.limit.value_namespace = name_space
                            self.limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix


                class CircuitIdAndRemoteIdThrottle(Entity):
                    """
                    Set Circuit ID and Remote ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle, self).__init__()

                        self.yang_name = "circuit-id-and-remote-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_presence_container = True

                        self.blocking_period = YLeaf(YType.uint32, "blocking-period")

                        self.request_period = YLeaf(YType.uint32, "request-period")

                        self.throttle = YLeaf(YType.uint32, "throttle")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("blocking_period",
                                        "request_period",
                                        "throttle") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.blocking_period.is_set or
                            self.request_period.is_set or
                            self.throttle.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.blocking_period.yfilter != YFilter.not_set or
                            self.request_period.yfilter != YFilter.not_set or
                            self.throttle.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-and-remote-id-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.blocking_period.is_set or self.blocking_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.blocking_period.get_name_leafdata())
                        if (self.request_period.is_set or self.request_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.request_period.get_name_leafdata())
                        if (self.throttle.is_set or self.throttle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "blocking-period" or name == "request-period" or name == "throttle"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "blocking-period"):
                            self.blocking_period = value
                            self.blocking_period.value_namespace = name_space
                            self.blocking_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "request-period"):
                            self.request_period = value
                            self.request_period.value_namespace = name_space
                            self.request_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle"):
                            self.throttle = value
                            self.throttle.value_namespace = name_space
                            self.throttle.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.access_interface_limit is not None) or
                        (self.circuit_id_and_remote_id_limit is not None) or
                        (self.circuit_id_and_remote_id_throttle is not None) or
                        (self.circuit_id_limit is not None) or
                        (self.circuit_id_throttle is not None) or
                        (self.inner_vlan_limit is not None) or
                        (self.inner_vlan_throttle is not None) or
                        (self.mac_access_interface_limit is not None) or
                        (self.mac_access_interface_throttle is not None) or
                        (self.mac_iwf_access_interface_limit is not None) or
                        (self.mac_iwf_access_interface_throttle is not None) or
                        (self.mac_iwf_limit is not None) or
                        (self.mac_limit is not None) or
                        (self.mac_throttle is not None) or
                        (self.max_limit is not None) or
                        (self.outer_vlan_limit is not None) or
                        (self.outer_vlan_throttle is not None) or
                        (self.remote_id_limit is not None) or
                        (self.remote_id_throttle is not None) or
                        (self.vlan_limit is not None) or
                        (self.vlan_throttle is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.access_interface_limit is not None and self.access_interface_limit.has_operation()) or
                        (self.circuit_id_and_remote_id_limit is not None and self.circuit_id_and_remote_id_limit.has_operation()) or
                        (self.circuit_id_and_remote_id_throttle is not None and self.circuit_id_and_remote_id_throttle.has_operation()) or
                        (self.circuit_id_limit is not None and self.circuit_id_limit.has_operation()) or
                        (self.circuit_id_throttle is not None and self.circuit_id_throttle.has_operation()) or
                        (self.inner_vlan_limit is not None and self.inner_vlan_limit.has_operation()) or
                        (self.inner_vlan_throttle is not None and self.inner_vlan_throttle.has_operation()) or
                        (self.mac_access_interface_limit is not None and self.mac_access_interface_limit.has_operation()) or
                        (self.mac_access_interface_throttle is not None and self.mac_access_interface_throttle.has_operation()) or
                        (self.mac_iwf_access_interface_limit is not None and self.mac_iwf_access_interface_limit.has_operation()) or
                        (self.mac_iwf_access_interface_throttle is not None and self.mac_iwf_access_interface_throttle.has_operation()) or
                        (self.mac_iwf_limit is not None and self.mac_iwf_limit.has_operation()) or
                        (self.mac_limit is not None and self.mac_limit.has_operation()) or
                        (self.mac_throttle is not None and self.mac_throttle.has_operation()) or
                        (self.max_limit is not None and self.max_limit.has_operation()) or
                        (self.outer_vlan_limit is not None and self.outer_vlan_limit.has_operation()) or
                        (self.outer_vlan_throttle is not None and self.outer_vlan_throttle.has_operation()) or
                        (self.remote_id_limit is not None and self.remote_id_limit.has_operation()) or
                        (self.remote_id_throttle is not None and self.remote_id_throttle.has_operation()) or
                        (self.vlan_limit is not None and self.vlan_limit.has_operation()) or
                        (self.vlan_throttle is not None and self.vlan_throttle.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sessions" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "access-interface-limit"):
                        if (self.access_interface_limit is None):
                            self.access_interface_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit()
                            self.access_interface_limit.parent = self
                            self._children_name_map["access_interface_limit"] = "access-interface-limit"
                        return self.access_interface_limit

                    if (child_yang_name == "circuit-id-and-remote-id-limit"):
                        if (self.circuit_id_and_remote_id_limit is None):
                            self.circuit_id_and_remote_id_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit()
                            self.circuit_id_and_remote_id_limit.parent = self
                            self._children_name_map["circuit_id_and_remote_id_limit"] = "circuit-id-and-remote-id-limit"
                        return self.circuit_id_and_remote_id_limit

                    if (child_yang_name == "circuit-id-and-remote-id-throttle"):
                        if (self.circuit_id_and_remote_id_throttle is None):
                            self.circuit_id_and_remote_id_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle()
                            self.circuit_id_and_remote_id_throttle.parent = self
                            self._children_name_map["circuit_id_and_remote_id_throttle"] = "circuit-id-and-remote-id-throttle"
                        return self.circuit_id_and_remote_id_throttle

                    if (child_yang_name == "circuit-id-limit"):
                        if (self.circuit_id_limit is None):
                            self.circuit_id_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit()
                            self.circuit_id_limit.parent = self
                            self._children_name_map["circuit_id_limit"] = "circuit-id-limit"
                        return self.circuit_id_limit

                    if (child_yang_name == "circuit-id-throttle"):
                        if (self.circuit_id_throttle is None):
                            self.circuit_id_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle()
                            self.circuit_id_throttle.parent = self
                            self._children_name_map["circuit_id_throttle"] = "circuit-id-throttle"
                        return self.circuit_id_throttle

                    if (child_yang_name == "inner-vlan-limit"):
                        if (self.inner_vlan_limit is None):
                            self.inner_vlan_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit()
                            self.inner_vlan_limit.parent = self
                            self._children_name_map["inner_vlan_limit"] = "inner-vlan-limit"
                        return self.inner_vlan_limit

                    if (child_yang_name == "inner-vlan-throttle"):
                        if (self.inner_vlan_throttle is None):
                            self.inner_vlan_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle()
                            self.inner_vlan_throttle.parent = self
                            self._children_name_map["inner_vlan_throttle"] = "inner-vlan-throttle"
                        return self.inner_vlan_throttle

                    if (child_yang_name == "mac-access-interface-limit"):
                        if (self.mac_access_interface_limit is None):
                            self.mac_access_interface_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit()
                            self.mac_access_interface_limit.parent = self
                            self._children_name_map["mac_access_interface_limit"] = "mac-access-interface-limit"
                        return self.mac_access_interface_limit

                    if (child_yang_name == "mac-access-interface-throttle"):
                        if (self.mac_access_interface_throttle is None):
                            self.mac_access_interface_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle()
                            self.mac_access_interface_throttle.parent = self
                            self._children_name_map["mac_access_interface_throttle"] = "mac-access-interface-throttle"
                        return self.mac_access_interface_throttle

                    if (child_yang_name == "mac-iwf-access-interface-limit"):
                        if (self.mac_iwf_access_interface_limit is None):
                            self.mac_iwf_access_interface_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit()
                            self.mac_iwf_access_interface_limit.parent = self
                            self._children_name_map["mac_iwf_access_interface_limit"] = "mac-iwf-access-interface-limit"
                        return self.mac_iwf_access_interface_limit

                    if (child_yang_name == "mac-iwf-access-interface-throttle"):
                        if (self.mac_iwf_access_interface_throttle is None):
                            self.mac_iwf_access_interface_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle()
                            self.mac_iwf_access_interface_throttle.parent = self
                            self._children_name_map["mac_iwf_access_interface_throttle"] = "mac-iwf-access-interface-throttle"
                        return self.mac_iwf_access_interface_throttle

                    if (child_yang_name == "mac-iwf-limit"):
                        if (self.mac_iwf_limit is None):
                            self.mac_iwf_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit()
                            self.mac_iwf_limit.parent = self
                            self._children_name_map["mac_iwf_limit"] = "mac-iwf-limit"
                        return self.mac_iwf_limit

                    if (child_yang_name == "mac-limit"):
                        if (self.mac_limit is None):
                            self.mac_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit()
                            self.mac_limit.parent = self
                            self._children_name_map["mac_limit"] = "mac-limit"
                        return self.mac_limit

                    if (child_yang_name == "mac-throttle"):
                        if (self.mac_throttle is None):
                            self.mac_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle()
                            self.mac_throttle.parent = self
                            self._children_name_map["mac_throttle"] = "mac-throttle"
                        return self.mac_throttle

                    if (child_yang_name == "max-limit"):
                        if (self.max_limit is None):
                            self.max_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit()
                            self.max_limit.parent = self
                            self._children_name_map["max_limit"] = "max-limit"
                        return self.max_limit

                    if (child_yang_name == "outer-vlan-limit"):
                        if (self.outer_vlan_limit is None):
                            self.outer_vlan_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit()
                            self.outer_vlan_limit.parent = self
                            self._children_name_map["outer_vlan_limit"] = "outer-vlan-limit"
                        return self.outer_vlan_limit

                    if (child_yang_name == "outer-vlan-throttle"):
                        if (self.outer_vlan_throttle is None):
                            self.outer_vlan_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle()
                            self.outer_vlan_throttle.parent = self
                            self._children_name_map["outer_vlan_throttle"] = "outer-vlan-throttle"
                        return self.outer_vlan_throttle

                    if (child_yang_name == "remote-id-limit"):
                        if (self.remote_id_limit is None):
                            self.remote_id_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit()
                            self.remote_id_limit.parent = self
                            self._children_name_map["remote_id_limit"] = "remote-id-limit"
                        return self.remote_id_limit

                    if (child_yang_name == "remote-id-throttle"):
                        if (self.remote_id_throttle is None):
                            self.remote_id_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle()
                            self.remote_id_throttle.parent = self
                            self._children_name_map["remote_id_throttle"] = "remote-id-throttle"
                        return self.remote_id_throttle

                    if (child_yang_name == "vlan-limit"):
                        if (self.vlan_limit is None):
                            self.vlan_limit = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit()
                            self.vlan_limit.parent = self
                            self._children_name_map["vlan_limit"] = "vlan-limit"
                        return self.vlan_limit

                    if (child_yang_name == "vlan-throttle"):
                        if (self.vlan_throttle is None):
                            self.vlan_throttle = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle()
                            self.vlan_throttle.parent = self
                            self._children_name_map["vlan_throttle"] = "vlan-throttle"
                        return self.vlan_throttle

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-interface-limit" or name == "circuit-id-and-remote-id-limit" or name == "circuit-id-and-remote-id-throttle" or name == "circuit-id-limit" or name == "circuit-id-throttle" or name == "inner-vlan-limit" or name == "inner-vlan-throttle" or name == "mac-access-interface-limit" or name == "mac-access-interface-throttle" or name == "mac-iwf-access-interface-limit" or name == "mac-iwf-access-interface-throttle" or name == "mac-iwf-limit" or name == "mac-limit" or name == "mac-throttle" or name == "max-limit" or name == "outer-vlan-limit" or name == "outer-vlan-throttle" or name == "remote-id-limit" or name == "remote-id-throttle" or name == "vlan-limit" or name == "vlan-throttle"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ControlPackets(Entity):
                """
                PPPoE control\-packet configuration data
                
                .. attribute:: priority
                
                	Set the Priority to use for PPP and PPPoE control packets
                	**type**\:  int
                
                	**range:** 0..7
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets, self).__init__()

                    self.yang_name = "control-packets"
                    self.yang_parent_name = "pppoe-bba-group"

                    self.priority = YLeaf(YType.uint32, "priority")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("priority") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets, self).__setattr__(name, value)

                def has_data(self):
                    return self.priority.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "control-packets" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "priority"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix


            class PaDoDelay(Entity):
                """
                PPPoE PADO delay configuration data
                
                .. attribute:: circuit_id
                
                	Configure PADO delay dependent on the received Circuit ID
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: circuit_id_strings
                
                	Delay the PADO response when there is an exact match on the received Circuit ID
                	**type**\:   :py:class:`CircuitIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings>`
                
                .. attribute:: circuit_id_substrings
                
                	Delay the PADO response when the received Circuit ID contains the given string
                	**type**\:   :py:class:`CircuitIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings>`
                
                .. attribute:: default
                
                	PADO delay (in milliseconds)
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: remote_id
                
                	Configure PADO delay dependent on the received Remote ID
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: remote_id_strings
                
                	Delay the PADO response when there is an exact match on the received Remote ID
                	**type**\:   :py:class:`RemoteIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings>`
                
                .. attribute:: remote_id_substrings
                
                	Delay the PADO response when the received Remote ID contains the given string
                	**type**\:   :py:class:`RemoteIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings>`
                
                .. attribute:: service_name_strings
                
                	Delay the PADO response when there is an exact match on the received Service Name
                	**type**\:   :py:class:`ServiceNameStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings>`
                
                .. attribute:: service_name_substrings
                
                	Delay the PADO response when the received Service Name contains the given string
                	**type**\:   :py:class:`ServiceNameSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay, self).__init__()

                    self.yang_name = "pa-do-delay"
                    self.yang_parent_name = "pppoe-bba-group"

                    self.circuit_id = YLeaf(YType.uint32, "circuit-id")

                    self.default = YLeaf(YType.uint32, "default")

                    self.remote_id = YLeaf(YType.uint32, "remote-id")

                    self.circuit_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings()
                    self.circuit_id_strings.parent = self
                    self._children_name_map["circuit_id_strings"] = "circuit-id-strings"
                    self._children_yang_names.add("circuit-id-strings")

                    self.circuit_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings()
                    self.circuit_id_substrings.parent = self
                    self._children_name_map["circuit_id_substrings"] = "circuit-id-substrings"
                    self._children_yang_names.add("circuit-id-substrings")

                    self.remote_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings()
                    self.remote_id_strings.parent = self
                    self._children_name_map["remote_id_strings"] = "remote-id-strings"
                    self._children_yang_names.add("remote-id-strings")

                    self.remote_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings()
                    self.remote_id_substrings.parent = self
                    self._children_name_map["remote_id_substrings"] = "remote-id-substrings"
                    self._children_yang_names.add("remote-id-substrings")

                    self.service_name_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings()
                    self.service_name_strings.parent = self
                    self._children_name_map["service_name_strings"] = "service-name-strings"
                    self._children_yang_names.add("service-name-strings")

                    self.service_name_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings()
                    self.service_name_substrings.parent = self
                    self._children_name_map["service_name_substrings"] = "service-name-substrings"
                    self._children_yang_names.add("service-name-substrings")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("circuit_id",
                                    "default",
                                    "remote_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay, self).__setattr__(name, value)


                class RemoteIdSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Remote ID contains the given string
                    
                    .. attribute:: remote_id_substring
                    
                    	Delay the PADO response when the received Remote ID contains the given string
                    	**type**\: list of    :py:class:`RemoteIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings, self).__init__()

                        self.yang_name = "remote-id-substrings"
                        self.yang_parent_name = "pa-do-delay"

                        self.remote_id_substring = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings, self).__setattr__(name, value)


                    class RemoteIdSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Remote ID contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Remote ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring, self).__init__()

                            self.yang_name = "remote-id-substring"
                            self.yang_parent_name = "remote-id-substrings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote-id-substring" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.remote_id_substring:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.remote_id_substring:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-id-substrings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "remote-id-substring"):
                            for c in self.remote_id_substring:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.remote_id_substring.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-id-substring"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class RemoteIdStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Remote ID
                    
                    .. attribute:: remote_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Remote ID
                    	**type**\: list of    :py:class:`RemoteIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings, self).__init__()

                        self.yang_name = "remote-id-strings"
                        self.yang_parent_name = "pa-do-delay"

                        self.remote_id_string = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings, self).__setattr__(name, value)


                    class RemoteIdString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Remote ID
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Remote ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString, self).__init__()

                            self.yang_name = "remote-id-string"
                            self.yang_parent_name = "remote-id-strings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote-id-string" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.remote_id_string:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.remote_id_string:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-id-strings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "remote-id-string"):
                            for c in self.remote_id_string:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.remote_id_string.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "remote-id-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ServiceNameStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Service Name
                    
                    .. attribute:: service_name_string
                    
                    	Delay the PADO response when there is an exact match on the received Service Name
                    	**type**\: list of    :py:class:`ServiceNameString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings, self).__init__()

                        self.yang_name = "service-name-strings"
                        self.yang_parent_name = "pa-do-delay"

                        self.service_name_string = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings, self).__setattr__(name, value)


                    class ServiceNameString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Service Name
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Service Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString, self).__init__()

                            self.yang_name = "service-name-string"
                            self.yang_parent_name = "service-name-strings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "service-name-string" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.service_name_string:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.service_name_string:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-name-strings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "service-name-string"):
                            for c in self.service_name_string:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.service_name_string.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "service-name-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class CircuitIdSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Circuit ID contains the given string
                    
                    .. attribute:: circuit_id_substring
                    
                    	Delay the PADO response when the received Circuit ID contains the given string
                    	**type**\: list of    :py:class:`CircuitIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings, self).__init__()

                        self.yang_name = "circuit-id-substrings"
                        self.yang_parent_name = "pa-do-delay"

                        self.circuit_id_substring = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings, self).__setattr__(name, value)


                    class CircuitIdSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Circuit ID contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Circuit ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring, self).__init__()

                            self.yang_name = "circuit-id-substring"
                            self.yang_parent_name = "circuit-id-substrings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "circuit-id-substring" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.circuit_id_substring:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.circuit_id_substring:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-substrings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "circuit-id-substring"):
                            for c in self.circuit_id_substring:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.circuit_id_substring.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "circuit-id-substring"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class ServiceNameSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Service Name contains the given string
                    
                    .. attribute:: service_name_substring
                    
                    	Delay the PADO response when the received Service Name contains the given string
                    	**type**\: list of    :py:class:`ServiceNameSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings, self).__init__()

                        self.yang_name = "service-name-substrings"
                        self.yang_parent_name = "pa-do-delay"

                        self.service_name_substring = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings, self).__setattr__(name, value)


                    class ServiceNameSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Service Name contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Service Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring, self).__init__()

                            self.yang_name = "service-name-substring"
                            self.yang_parent_name = "service-name-substrings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "service-name-substring" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.service_name_substring:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.service_name_substring:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-name-substrings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "service-name-substring"):
                            for c in self.service_name_substring:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.service_name_substring.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "service-name-substring"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class CircuitIdStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Circuit ID
                    
                    .. attribute:: circuit_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Circuit ID
                    	**type**\: list of    :py:class:`CircuitIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings, self).__init__()

                        self.yang_name = "circuit-id-strings"
                        self.yang_parent_name = "pa-do-delay"

                        self.circuit_id_string = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings, self).__setattr__(name, value)


                    class CircuitIdString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Circuit ID
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Circuit ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString, self).__init__()

                            self.yang_name = "circuit-id-string"
                            self.yang_parent_name = "circuit-id-strings"

                            self.name = YLeaf(YType.str, "name")

                            self.delay = YLeaf(YType.uint32, "delay")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "delay") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.delay.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "circuit-id-string" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "delay"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.circuit_id_string:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.circuit_id_string:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "circuit-id-strings" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "circuit-id-string"):
                            for c in self.circuit_id_string:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.circuit_id_string.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "circuit-id-string"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.circuit_id.is_set or
                        self.default.is_set or
                        self.remote_id.is_set or
                        (self.circuit_id_strings is not None and self.circuit_id_strings.has_data()) or
                        (self.circuit_id_substrings is not None and self.circuit_id_substrings.has_data()) or
                        (self.remote_id_strings is not None and self.remote_id_strings.has_data()) or
                        (self.remote_id_substrings is not None and self.remote_id_substrings.has_data()) or
                        (self.service_name_strings is not None and self.service_name_strings.has_data()) or
                        (self.service_name_substrings is not None and self.service_name_substrings.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.circuit_id.yfilter != YFilter.not_set or
                        self.default.yfilter != YFilter.not_set or
                        self.remote_id.yfilter != YFilter.not_set or
                        (self.circuit_id_strings is not None and self.circuit_id_strings.has_operation()) or
                        (self.circuit_id_substrings is not None and self.circuit_id_substrings.has_operation()) or
                        (self.remote_id_strings is not None and self.remote_id_strings.has_operation()) or
                        (self.remote_id_substrings is not None and self.remote_id_substrings.has_operation()) or
                        (self.service_name_strings is not None and self.service_name_strings.has_operation()) or
                        (self.service_name_substrings is not None and self.service_name_substrings.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pa-do-delay" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.circuit_id.get_name_leafdata())
                    if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default.get_name_leafdata())
                    if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "circuit-id-strings"):
                        if (self.circuit_id_strings is None):
                            self.circuit_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings()
                            self.circuit_id_strings.parent = self
                            self._children_name_map["circuit_id_strings"] = "circuit-id-strings"
                        return self.circuit_id_strings

                    if (child_yang_name == "circuit-id-substrings"):
                        if (self.circuit_id_substrings is None):
                            self.circuit_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings()
                            self.circuit_id_substrings.parent = self
                            self._children_name_map["circuit_id_substrings"] = "circuit-id-substrings"
                        return self.circuit_id_substrings

                    if (child_yang_name == "remote-id-strings"):
                        if (self.remote_id_strings is None):
                            self.remote_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings()
                            self.remote_id_strings.parent = self
                            self._children_name_map["remote_id_strings"] = "remote-id-strings"
                        return self.remote_id_strings

                    if (child_yang_name == "remote-id-substrings"):
                        if (self.remote_id_substrings is None):
                            self.remote_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings()
                            self.remote_id_substrings.parent = self
                            self._children_name_map["remote_id_substrings"] = "remote-id-substrings"
                        return self.remote_id_substrings

                    if (child_yang_name == "service-name-strings"):
                        if (self.service_name_strings is None):
                            self.service_name_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings()
                            self.service_name_strings.parent = self
                            self._children_name_map["service_name_strings"] = "service-name-strings"
                        return self.service_name_strings

                    if (child_yang_name == "service-name-substrings"):
                        if (self.service_name_substrings is None):
                            self.service_name_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings()
                            self.service_name_substrings.parent = self
                            self._children_name_map["service_name_substrings"] = "service-name-substrings"
                        return self.service_name_substrings

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "circuit-id-strings" or name == "circuit-id-substrings" or name == "remote-id-strings" or name == "remote-id-substrings" or name == "service-name-strings" or name == "service-name-substrings" or name == "circuit-id" or name == "default" or name == "remote-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "circuit-id"):
                        self.circuit_id = value
                        self.circuit_id.value_namespace = name_space
                        self.circuit_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "default"):
                        self.default = value
                        self.default.value_namespace = name_space
                        self.default.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-id"):
                        self.remote_id = value
                        self.remote_id.value_namespace = name_space
                        self.remote_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.bba_group.is_set or
                    self.completion_timeout.is_set or
                    self.enable_padt_after_shut_down.is_set or
                    self.invalid_session_id.is_set or
                    self.mtu.is_set or
                    (self.control_packets is not None and self.control_packets.has_data()) or
                    (self.pa_do_delay is not None and self.pa_do_delay.has_data()) or
                    (self.sessions is not None and self.sessions.has_data()) or
                    (self.tag is not None and self.tag.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bba_group.yfilter != YFilter.not_set or
                    self.completion_timeout.yfilter != YFilter.not_set or
                    self.enable_padt_after_shut_down.yfilter != YFilter.not_set or
                    self.invalid_session_id.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set or
                    (self.control_packets is not None and self.control_packets.has_operation()) or
                    (self.pa_do_delay is not None and self.pa_do_delay.has_operation()) or
                    (self.sessions is not None and self.sessions.has_operation()) or
                    (self.tag is not None and self.tag.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pppoe-bba-group" + "[bba-group='" + self.bba_group.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/pppoe-bba-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bba_group.is_set or self.bba_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bba_group.get_name_leafdata())
                if (self.completion_timeout.is_set or self.completion_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.completion_timeout.get_name_leafdata())
                if (self.enable_padt_after_shut_down.is_set or self.enable_padt_after_shut_down.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable_padt_after_shut_down.get_name_leafdata())
                if (self.invalid_session_id.is_set or self.invalid_session_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.invalid_session_id.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "control-packets"):
                    if (self.control_packets is None):
                        self.control_packets = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets()
                        self.control_packets.parent = self
                        self._children_name_map["control_packets"] = "control-packets"
                    return self.control_packets

                if (child_yang_name == "pa-do-delay"):
                    if (self.pa_do_delay is None):
                        self.pa_do_delay = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay()
                        self.pa_do_delay.parent = self
                        self._children_name_map["pa_do_delay"] = "pa-do-delay"
                    return self.pa_do_delay

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                if (child_yang_name == "tag"):
                    if (self.tag is None):
                        self.tag = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag()
                        self.tag.parent = self
                        self._children_name_map["tag"] = "tag"
                    return self.tag

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "control-packets" or name == "pa-do-delay" or name == "sessions" or name == "tag" or name == "bba-group" or name == "completion-timeout" or name == "enable-padt-after-shut-down" or name == "invalid-session-id" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bba-group"):
                    self.bba_group = value
                    self.bba_group.value_namespace = name_space
                    self.bba_group.value_namespace_prefix = name_space_prefix
                if(value_path == "completion-timeout"):
                    self.completion_timeout = value
                    self.completion_timeout.value_namespace = name_space
                    self.completion_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "enable-padt-after-shut-down"):
                    self.enable_padt_after_shut_down = value
                    self.enable_padt_after_shut_down.value_namespace = name_space
                    self.enable_padt_after_shut_down.value_namespace_prefix = name_space_prefix
                if(value_path == "invalid-session-id"):
                    self.invalid_session_id = value
                    self.invalid_session_id.value_namespace = name_space
                    self.invalid_session_id.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pppoe_bba_group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pppoe_bba_group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pppoe-bba-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pppoe-bba-group"):
                for c in self.pppoe_bba_group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pppoe_bba_group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pppoe-bba-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.in_flight_window.is_set or
            self.session_id_space_flat.is_set or
            (self.pppoe_bba_groups is not None and self.pppoe_bba_groups.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.in_flight_window.yfilter != YFilter.not_set or
            self.session_id_space_flat.yfilter != YFilter.not_set or
            (self.pppoe_bba_groups is not None and self.pppoe_bba_groups.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.in_flight_window.is_set or self.in_flight_window.yfilter != YFilter.not_set):
            leaf_name_data.append(self.in_flight_window.get_name_leafdata())
        if (self.session_id_space_flat.is_set or self.session_id_space_flat.yfilter != YFilter.not_set):
            leaf_name_data.append(self.session_id_space_flat.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "pppoe-bba-groups"):
            if (self.pppoe_bba_groups is None):
                self.pppoe_bba_groups = PppoeCfg.PppoeBbaGroups()
                self.pppoe_bba_groups.parent = self
                self._children_name_map["pppoe_bba_groups"] = "pppoe-bba-groups"
            return self.pppoe_bba_groups

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "pppoe-bba-groups" or name == "in-flight-window" or name == "session-id-space-flat"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "in-flight-window"):
            self.in_flight_window = value
            self.in_flight_window.value_namespace = name_space
            self.in_flight_window.value_namespace_prefix = name_space_prefix
        if(value_path == "session-id-space-flat"):
            self.session_id_space_flat = value
            self.session_id_space_flat.value_namespace = name_space
            self.session_id_space_flat.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = PppoeCfg()
        return self._top_entity

