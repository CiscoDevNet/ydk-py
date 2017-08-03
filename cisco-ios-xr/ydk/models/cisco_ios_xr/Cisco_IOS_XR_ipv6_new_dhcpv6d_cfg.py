""" Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package configuration.

This module contains definitions
for the following management objects\:
  dhcpv6\: None

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Insert(Enum):
    """
    Insert

    Insert

    .. data:: local = 0

    	Insert locally generated/configured Interface

    	ID value

    .. data:: received = 1

    	Insert received Interface ID value

    .. data:: pppoe = 2

    	Insert received Interface ID value from SADB

    """

    local = Enum.YLeaf(0, "local")

    received = Enum.YLeaf(1, "received")

    pppoe = Enum.YLeaf(2, "pppoe")


class LinkLayerAddr(Enum):
    """
    LinkLayerAddr

    Link layer addr

    .. data:: set = 4

    	Insert Received LinkLayerAddr Value from SADB

    """

    set = Enum.YLeaf(4, "set")


class SubscriberId(Enum):
    """
    SubscriberId

    Subscriber id

    .. data:: pppoe = 3

    	Insert Received Subscriber-ID Value from SADB

    """

    pppoe = Enum.YLeaf(3, "pppoe")



class Dhcpv6(Entity):
    """
    None
    
    .. attribute:: allow_duid_change
    
    	For BNG session, allow duid change for a client MAC
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:   :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Database>`
    
    .. attribute:: enable
    
    	Enable None. Deletion of this object also causes deletion of all associated objects under DHCPv6
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: interfaces
    
    	Table of Interface
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces>`
    
    .. attribute:: profiles
    
    	Table of Profile
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv6-new-dhcpv6d-cfg'
    _revision = '2016-10-10'

    def __init__(self):
        super(Dhcpv6, self).__init__()
        self._top_entity = None

        self.yang_name = "dhcpv6"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg"
        self.is_presence_container = True

        self.allow_duid_change = YLeaf(YType.empty, "allow-duid-change")

        self.enable = YLeaf(YType.empty, "enable")

        self.database = Dhcpv6.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"
        self._children_yang_names.add("database")

        self.interfaces = Dhcpv6.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.profiles = Dhcpv6.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("allow_duid_change",
                        "enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Dhcpv6, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Dhcpv6, self).__setattr__(name, value)


    class Database(Entity):
        """
        Enable DHCP binding database storage to file
        system
        
        .. attribute:: full_write_interval
        
        	Full file write interval (default 10 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**default value**\: 10
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**default value**\: 1
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: relay
        
        	Enable DHCP relay binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Dhcpv6.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "dhcpv6"

            self.full_write_interval = YLeaf(YType.uint32, "full-write-interval")

            self.incremental_write_interval = YLeaf(YType.uint32, "incremental-write-interval")

            self.proxy = YLeaf(YType.empty, "proxy")

            self.relay = YLeaf(YType.empty, "relay")

            self.server = YLeaf(YType.empty, "server")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("full_write_interval",
                            "incremental_write_interval",
                            "proxy",
                            "relay",
                            "server") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Dhcpv6.Database, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Dhcpv6.Database, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.full_write_interval.is_set or
                self.incremental_write_interval.is_set or
                self.proxy.is_set or
                self.relay.is_set or
                self.server.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.full_write_interval.yfilter != YFilter.not_set or
                self.incremental_write_interval.yfilter != YFilter.not_set or
                self.proxy.yfilter != YFilter.not_set or
                self.relay.yfilter != YFilter.not_set or
                self.server.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "database" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.full_write_interval.is_set or self.full_write_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.full_write_interval.get_name_leafdata())
            if (self.incremental_write_interval.is_set or self.incremental_write_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.incremental_write_interval.get_name_leafdata())
            if (self.proxy.is_set or self.proxy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.proxy.get_name_leafdata())
            if (self.relay.is_set or self.relay.yfilter != YFilter.not_set):
                leaf_name_data.append(self.relay.get_name_leafdata())
            if (self.server.is_set or self.server.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "full-write-interval" or name == "incremental-write-interval" or name == "proxy" or name == "relay" or name == "server"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "full-write-interval"):
                self.full_write_interval = value
                self.full_write_interval.value_namespace = name_space
                self.full_write_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "incremental-write-interval"):
                self.incremental_write_interval = value
                self.incremental_write_interval.value_namespace = name_space
                self.incremental_write_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "proxy"):
                self.proxy = value
                self.proxy.value_namespace = name_space
                self.proxy.value_namespace_prefix = name_space_prefix
            if(value_path == "relay"):
                self.relay = value
                self.relay.value_namespace = name_space
                self.relay.value_namespace_prefix = name_space_prefix
            if(value_path == "server"):
                self.server = value
                self.server.value_namespace = name_space
                self.server.value_namespace_prefix = name_space_prefix


    class Profiles(Entity):
        """
        Table of Profile
        
        .. attribute:: profile
        
        	None
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Dhcpv6.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "dhcpv6"

            self.profile = YList(self)

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
                        super(Dhcpv6.Profiles, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Dhcpv6.Profiles, self).__setattr__(name, value)


        class Profile(Entity):
            """
            None
            
            .. attribute:: profile_name  <key>
            
            	Profile name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: base
            
            	None
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base>`
            
            	**presence node**\: True
            
            .. attribute:: proxy
            
            	None
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy>`
            
            	**presence node**\: True
            
            .. attribute:: relay
            
            	None
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay>`
            
            	**presence node**\: True
            
            .. attribute:: server
            
            	None
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Dhcpv6.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"

                self.profile_name = YLeaf(YType.str, "profile-name")

                self.base = None
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.proxy = None
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.relay = None
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")

                self.server = None
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("profile_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Dhcpv6.Profiles.Profile, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Dhcpv6.Profiles.Profile, self).__setattr__(name, value)


            class Relay(Entity):
                """
                None
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Relay
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: helper_addresses
                
                	Table of HelperAddress
                	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses>`
                
                .. attribute:: iana_route_add
                
                	Enable route addition for IANA
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "profile"
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.iana_route_add = YLeaf(YType.empty, "iana-route-add")

                    self.helper_addresses = Dhcpv6.Profiles.Profile.Relay.HelperAddresses()
                    self.helper_addresses.parent = self
                    self._children_name_map["helper_addresses"] = "helper-addresses"
                    self._children_yang_names.add("helper-addresses")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable",
                                    "iana_route_add") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Profiles.Profile.Relay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Profiles.Profile.Relay, self).__setattr__(name, value)


                class HelperAddresses(Entity):
                    """
                    Table of HelperAddress
                    
                    .. attribute:: helper_address
                    
                    	Specify the server helper address
                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__init__()

                        self.yang_name = "helper-addresses"
                        self.yang_parent_name = "relay"

                        self.helper_address = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses, self).__setattr__(name, value)


                    class HelperAddress(Entity):
                        """
                        Specify the server helper address
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: helper_address  <key>
                        
                        	Server Global unicast address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, self).__init__()

                            self.yang_name = "helper-address"
                            self.yang_parent_name = "helper-addresses"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.helper_address = YLeaf(YType.str, "helper-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("vrf_name",
                                            "helper_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.vrf_name.is_set or
                                self.helper_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                self.helper_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "helper-address" + "[vrf-name='" + self.vrf_name.get() + "']" + "[helper-address='" + self.helper_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())
                            if (self.helper_address.is_set or self.helper_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.helper_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "vrf-name" or name == "helper-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "helper-address"):
                                self.helper_address = value
                                self.helper_address.value_namespace = name_space
                                self.helper_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.helper_address:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.helper_address:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "helper-addresses" + path_buffer

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

                        if (child_yang_name == "helper-address"):
                            for c in self.helper_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.helper_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "helper-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        self.iana_route_add.is_set or
                        (self.helper_addresses is not None and self.helper_addresses.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.iana_route_add.yfilter != YFilter.not_set or
                        (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "relay" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.iana_route_add.is_set or self.iana_route_add.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.iana_route_add.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "helper-addresses"):
                        if (self.helper_addresses is None):
                            self.helper_addresses = Dhcpv6.Profiles.Profile.Relay.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                        return self.helper_addresses

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "helper-addresses" or name == "enable" or name == "iana-route-add"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "iana-route-add"):
                        self.iana_route_add = value
                        self.iana_route_add.value_namespace = name_space
                        self.iana_route_add.value_namespace_prefix = name_space_prefix


            class Base(Entity):
                """
                None
                
                .. attribute:: default
                
                	Default match option
                	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Base
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: match
                
                	Enter match option
                	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "profile"
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.default = Dhcpv6.Profiles.Profile.Base.Default()
                    self.default.parent = self
                    self._children_name_map["default"] = "default"
                    self._children_yang_names.add("default")

                    self.match = Dhcpv6.Profiles.Profile.Base.Match()
                    self.match.parent = self
                    self._children_name_map["match"] = "match"
                    self._children_yang_names.add("match")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Profiles.Profile.Base, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Profiles.Profile.Base, self).__setattr__(name, value)


                class Default(Entity):
                    """
                    Default match option
                    
                    .. attribute:: profile
                    
                    	Enter proxy or server profile
                    	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Default.Profile>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Default, self).__init__()

                        self.yang_name = "default"
                        self.yang_parent_name = "base"

                        self.profile = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Base.Default, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Base.Default, self).__setattr__(name, value)


                    class Profile(Entity):
                        """
                        Enter proxy or server profile
                        
                        .. attribute:: profile_name  <key>
                        
                        	Profile name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: proxy_mode
                        
                        	Specify mode\-class based Proxy Option
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: server_mode
                        
                        	Specify mode\-class based Server option
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Default.Profile, self).__init__()

                            self.yang_name = "profile"
                            self.yang_parent_name = "default"

                            self.profile_name = YLeaf(YType.str, "profile-name")

                            self.proxy_mode = YLeaf(YType.empty, "proxy-mode")

                            self.server_mode = YLeaf(YType.empty, "server-mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("profile_name",
                                            "proxy_mode",
                                            "server_mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Base.Default.Profile, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Base.Default.Profile, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.profile_name.is_set or
                                self.proxy_mode.is_set or
                                self.server_mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.profile_name.yfilter != YFilter.not_set or
                                self.proxy_mode.yfilter != YFilter.not_set or
                                self.server_mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "profile" + "[profile-name='" + self.profile_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.profile_name.get_name_leafdata())
                            if (self.proxy_mode.is_set or self.proxy_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.proxy_mode.get_name_leafdata())
                            if (self.server_mode.is_set or self.server_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.server_mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "profile-name" or name == "proxy-mode" or name == "server-mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "profile-name"):
                                self.profile_name = value
                                self.profile_name.value_namespace = name_space
                                self.profile_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "proxy-mode"):
                                self.proxy_mode = value
                                self.proxy_mode.value_namespace = name_space
                                self.proxy_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "server-mode"):
                                self.server_mode = value
                                self.server_mode.value_namespace = name_space
                                self.server_mode.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.profile:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.profile:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "default" + path_buffer

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

                        if (child_yang_name == "profile"):
                            for c in self.profile:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Base.Default.Profile()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.profile.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "profile"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Match(Entity):
                    """
                    Enter match option
                    
                    .. attribute:: mode_classes
                    
                    	Table of ModeClass
                    	**type**\:   :py:class:`ModeClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Base.Match, self).__init__()

                        self.yang_name = "match"
                        self.yang_parent_name = "base"

                        self.mode_classes = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses()
                        self.mode_classes.parent = self
                        self._children_name_map["mode_classes"] = "mode-classes"
                        self._children_yang_names.add("mode-classes")


                    class ModeClasses(Entity):
                        """
                        Table of ModeClass
                        
                        .. attribute:: mode_class
                        
                        	Specify PPP/IPoE class option
                        	**type**\: list of    :py:class:`ModeClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__init__()

                            self.yang_name = "mode-classes"
                            self.yang_parent_name = "match"

                            self.mode_class = YList(self)

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
                                        super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses, self).__setattr__(name, value)


                        class ModeClass(Entity):
                            """
                            Specify PPP/IPoE class option
                            
                            .. attribute:: class_name  <key>
                            
                            	Class name
                            	**type**\:  str
                            
                            	**length:** 1..128
                            
                            .. attribute:: profile
                            
                            	Enter proxy or server profile
                            	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__init__()

                                self.yang_name = "mode-class"
                                self.yang_parent_name = "mode-classes"

                                self.class_name = YLeaf(YType.str, "class-name")

                                self.profile = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("class_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass, self).__setattr__(name, value)


                            class Profile(Entity):
                                """
                                Enter proxy or server profile
                                
                                .. attribute:: profile_name  <key>
                                
                                	Profile name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: proxy_mode
                                
                                	Specify mode\-class based Proxy Option
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: server_mode
                                
                                	Specify mode\-class based Server option
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2016-10-10'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile, self).__init__()

                                    self.yang_name = "profile"
                                    self.yang_parent_name = "mode-class"

                                    self.profile_name = YLeaf(YType.str, "profile-name")

                                    self.proxy_mode = YLeaf(YType.empty, "proxy-mode")

                                    self.server_mode = YLeaf(YType.empty, "server-mode")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("profile_name",
                                                    "proxy_mode",
                                                    "server_mode") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.profile_name.is_set or
                                        self.proxy_mode.is_set or
                                        self.server_mode.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.profile_name.yfilter != YFilter.not_set or
                                        self.proxy_mode.yfilter != YFilter.not_set or
                                        self.server_mode.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "profile" + "[profile-name='" + self.profile_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.profile_name.get_name_leafdata())
                                    if (self.proxy_mode.is_set or self.proxy_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.proxy_mode.get_name_leafdata())
                                    if (self.server_mode.is_set or self.server_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.server_mode.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "profile-name" or name == "proxy-mode" or name == "server-mode"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "profile-name"):
                                        self.profile_name = value
                                        self.profile_name.value_namespace = name_space
                                        self.profile_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "proxy-mode"):
                                        self.proxy_mode = value
                                        self.proxy_mode.value_namespace = name_space
                                        self.proxy_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "server-mode"):
                                        self.server_mode = value
                                        self.server_mode.value_namespace = name_space
                                        self.server_mode.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.profile:
                                    if (c.has_data()):
                                        return True
                                return self.class_name.is_set

                            def has_operation(self):
                                for c in self.profile:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.class_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mode-class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.class_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "profile"):
                                    for c in self.profile:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass.Profile()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.profile.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile" or name == "class-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "class-name"):
                                    self.class_name = value
                                    self.class_name.value_namespace = name_space
                                    self.class_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.mode_class:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.mode_class:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mode-classes" + path_buffer

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

                            if (child_yang_name == "mode-class"):
                                for c in self.mode_class:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses.ModeClass()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.mode_class.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mode-class"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.mode_classes is not None and self.mode_classes.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.mode_classes is not None and self.mode_classes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "match" + path_buffer

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

                        if (child_yang_name == "mode-classes"):
                            if (self.mode_classes is None):
                                self.mode_classes = Dhcpv6.Profiles.Profile.Base.Match.ModeClasses()
                                self.mode_classes.parent = self
                                self._children_name_map["mode_classes"] = "mode-classes"
                            return self.mode_classes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mode-classes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        (self.default is not None and self.default.has_data()) or
                        (self.match is not None and self.match.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.default is not None and self.default.has_operation()) or
                        (self.match is not None and self.match.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "base" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "default"):
                        if (self.default is None):
                            self.default = Dhcpv6.Profiles.Profile.Base.Default()
                            self.default.parent = self
                            self._children_name_map["default"] = "default"
                        return self.default

                    if (child_yang_name == "match"):
                        if (self.match is None):
                            self.match = Dhcpv6.Profiles.Profile.Base.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"
                        return self.match

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "default" or name == "match" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix


            class Proxy(Entity):
                """
                None
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes>`
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Proxy
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces>`
                
                .. attribute:: link_address
                
                	IPv6 address to be filled in link\-address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: relay
                
                	Specify relay configuration
                	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay>`
                
                .. attribute:: route_add_disable
                
                	RouteDisable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions>`
                
                .. attribute:: src_intf_name
                
                	Create or enter proxy profile Source Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: vrfs
                
                	VRF related configuration
                	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "profile"
                    self.is_presence_container = True

                    self.enable = YLeaf(YType.empty, "enable")

                    self.link_address = YLeaf(YType.str, "link-address")

                    self.route_add_disable = YLeaf(YType.empty, "route-add-disable")

                    self.src_intf_name = YLeaf(YType.str, "src-intf-name")

                    self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._children_yang_names.add("interfaces")

                    self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                    self.relay.parent = self
                    self._children_name_map["relay"] = "relay"
                    self._children_yang_names.add("relay")

                    self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")

                    self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                    self.vrfs.parent = self
                    self._children_name_map["vrfs"] = "vrfs"
                    self._children_yang_names.add("vrfs")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enable",
                                    "link_address",
                                    "route_add_disable",
                                    "src_intf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Profiles.Profile.Proxy, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Profiles.Profile.Proxy, self).__setattr__(name, value)


                class Interfaces(Entity):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	None
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "proxy"

                        self.interface = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Proxy.Interfaces, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        None
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface to configure
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_id
                        
                        	Physical interface ID
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_id = YLeaf(YType.str, "interface-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name",
                                            "interface_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.interface_id.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.interface_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.interface_id.is_set or self.interface_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "interface-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-id"):
                                self.interface_id = value
                                self.interface_id.value_namespace = name_space
                                self.interface_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.interface:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interfaces" + path_buffer

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

                        if (child_yang_name == "interface"):
                            for c in self.interface:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Relay(Entity):
                    """
                    Specify relay configuration
                    
                    .. attribute:: option
                    
                    	Specify relay option configuration
                    	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Relay, self).__init__()

                        self.yang_name = "relay"
                        self.yang_parent_name = "proxy"

                        self.option = Dhcpv6.Profiles.Profile.Proxy.Relay.Option()
                        self.option.parent = self
                        self._children_name_map["option"] = "option"
                        self._children_yang_names.add("option")


                    class Option(Entity):
                        """
                        Specify relay option configuration
                        
                        .. attribute:: interface_id
                        
                        	Interface Id option
                        	**type**\:   :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId>`
                        
                        .. attribute:: link_layer_addr
                        
                        	Configure Received link\-layer\-Addr
                        	**type**\:   :py:class:`LinkLayerAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.LinkLayerAddr>`
                        
                        .. attribute:: remote_i_dreceived
                        
                        	Set remote\-id value from SADB
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: remote_id
                        
                        	Enter remote\-id value
                        	**type**\:  str
                        
                        	**length:** 1..256
                        
                        .. attribute:: subscriber_id
                        
                        	Configure Received SubscriberID
                        	**type**\:   :py:class:`SubscriberId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.SubscriberId>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__init__()

                            self.yang_name = "option"
                            self.yang_parent_name = "relay"

                            self.link_layer_addr = YLeaf(YType.enumeration, "link-layer-addr")

                            self.remote_i_dreceived = YLeaf(YType.int32, "remote-i-dreceived")

                            self.remote_id = YLeaf(YType.str, "remote-id")

                            self.subscriber_id = YLeaf(YType.enumeration, "subscriber-id")

                            self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                            self.interface_id.parent = self
                            self._children_name_map["interface_id"] = "interface-id"
                            self._children_yang_names.add("interface-id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("link_layer_addr",
                                            "remote_i_dreceived",
                                            "remote_id",
                                            "subscriber_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option, self).__setattr__(name, value)


                        class InterfaceId(Entity):
                            """
                            Interface Id option
                            
                            .. attribute:: insert
                            
                            	Configure InterfaceID insert type
                            	**type**\:   :py:class:`Insert <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Insert>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__init__()

                                self.yang_name = "interface-id"
                                self.yang_parent_name = "option"

                                self.insert = YLeaf(YType.enumeration, "insert")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("insert") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId, self).__setattr__(name, value)

                            def has_data(self):
                                return self.insert.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.insert.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.insert.is_set or self.insert.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.insert.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "insert"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "insert"):
                                    self.insert = value
                                    self.insert.value_namespace = name_space
                                    self.insert.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.link_layer_addr.is_set or
                                self.remote_i_dreceived.is_set or
                                self.remote_id.is_set or
                                self.subscriber_id.is_set or
                                (self.interface_id is not None and self.interface_id.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.link_layer_addr.yfilter != YFilter.not_set or
                                self.remote_i_dreceived.yfilter != YFilter.not_set or
                                self.remote_id.yfilter != YFilter.not_set or
                                self.subscriber_id.yfilter != YFilter.not_set or
                                (self.interface_id is not None and self.interface_id.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "option" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.link_layer_addr.is_set or self.link_layer_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.link_layer_addr.get_name_leafdata())
                            if (self.remote_i_dreceived.is_set or self.remote_i_dreceived.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_i_dreceived.get_name_leafdata())
                            if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.remote_id.get_name_leafdata())
                            if (self.subscriber_id.is_set or self.subscriber_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.subscriber_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "interface-id"):
                                if (self.interface_id is None):
                                    self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                                    self.interface_id.parent = self
                                    self._children_name_map["interface_id"] = "interface-id"
                                return self.interface_id

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-id" or name == "link-layer-addr" or name == "remote-i-dreceived" or name == "remote-id" or name == "subscriber-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "link-layer-addr"):
                                self.link_layer_addr = value
                                self.link_layer_addr.value_namespace = name_space
                                self.link_layer_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-i-dreceived"):
                                self.remote_i_dreceived = value
                                self.remote_i_dreceived.value_namespace = name_space
                                self.remote_i_dreceived.value_namespace_prefix = name_space_prefix
                            if(value_path == "remote-id"):
                                self.remote_id = value
                                self.remote_id.value_namespace = name_space
                                self.remote_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "subscriber-id"):
                                self.subscriber_id = value
                                self.subscriber_id.value_namespace = name_space
                                self.subscriber_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.option is not None and self.option.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.option is not None and self.option.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "relay" + path_buffer

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

                        if (child_yang_name == "option"):
                            if (self.option is None):
                                self.option = Dhcpv6.Profiles.Profile.Proxy.Relay.Option()
                                self.option.parent = self
                                self._children_name_map["option"] = "option"
                            return self.option

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "option"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Vrfs(Entity):
                    """
                    VRF related configuration
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__init__()

                        self.yang_name = "vrfs"
                        self.yang_parent_name = "proxy"

                        self.vrf = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs, self).__setattr__(name, value)


                    class Vrf(Entity):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "vrfs"

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf, self).__setattr__(name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	DHCPv6 Helper Address
                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "vrf"

                                self.helper_address = YList(self)

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
                                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)


                            class HelperAddress(Entity):
                                """
                                DHCPv6 Helper Address
                                
                                .. attribute:: helper_address  <key>
                                
                                	DHCPv6 Helper Address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: any_out_interface
                                
                                	DHCPv6 HelperAddress Output Interface
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: out_interface
                                
                                	DHCPv6 HelperAddress Specific Output Interface
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2016-10-10'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"

                                    self.helper_address = YLeaf(YType.str, "helper-address")

                                    self.any_out_interface = YLeaf(YType.empty, "any-out-interface")

                                    self.out_interface = YLeaf(YType.str, "out-interface")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("helper_address",
                                                    "any_out_interface",
                                                    "out_interface") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.helper_address.is_set or
                                        self.any_out_interface.is_set or
                                        self.out_interface.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.helper_address.yfilter != YFilter.not_set or
                                        self.any_out_interface.yfilter != YFilter.not_set or
                                        self.out_interface.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "helper-address" + "[helper-address='" + self.helper_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.helper_address.is_set or self.helper_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.helper_address.get_name_leafdata())
                                    if (self.any_out_interface.is_set or self.any_out_interface.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.any_out_interface.get_name_leafdata())
                                    if (self.out_interface.is_set or self.out_interface.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.out_interface.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "helper-address" or name == "any-out-interface" or name == "out-interface"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "helper-address"):
                                        self.helper_address = value
                                        self.helper_address.value_namespace = name_space
                                        self.helper_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "any-out-interface"):
                                        self.any_out_interface = value
                                        self.any_out_interface.value_namespace = name_space
                                        self.any_out_interface.value_namespace_prefix = name_space_prefix
                                    if(value_path == "out-interface"):
                                        self.out_interface = value
                                        self.out_interface.value_namespace = name_space
                                        self.out_interface.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.helper_address:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.helper_address:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "helper-addresses" + path_buffer

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

                                if (child_yang_name == "helper-address"):
                                    for c in self.helper_address:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.helper_address.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "helper-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.vrf_name.is_set or
                                (self.helper_addresses is not None and self.helper_addresses.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "helper-addresses"):
                                if (self.helper_addresses is None):
                                    self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                return self.helper_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "helper-addresses" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.vrf:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.vrf:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrfs" + path_buffer

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

                        if (child_yang_name == "vrf"):
                            for c in self.vrf:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.vrf.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "proxy"

                        self.class_ = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Proxy.Classes, self).__setattr__(name, value)


                    class Class_(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  <key>
                        
                        	Class name
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\:   :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses>`
                        
                        .. attribute:: link_address
                        
                        	IPv6 address to be filled in link\-address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.link_address = YLeaf(YType.str, "link-address")

                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses()
                            self.helper_addresses.parent = self
                            self._children_name_map["helper_addresses"] = "helper-addresses"
                            self._children_yang_names.add("helper-addresses")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("class_name",
                                            "link_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_, self).__setattr__(name, value)


                        class HelperAddresses(Entity):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	Specify the server helper address
                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses, self).__init__()

                                self.yang_name = "helper-addresses"
                                self.yang_parent_name = "class"

                                self.helper_address = YList(self)

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
                                            super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses, self).__setattr__(name, value)


                            class HelperAddress(Entity):
                                """
                                Specify the server helper address
                                
                                .. attribute:: vrf_name  <key>
                                
                                	VRF name
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: helper_address  <key>
                                
                                	Server address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2016-10-10'

                                def __init__(self):
                                    super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress, self).__init__()

                                    self.yang_name = "helper-address"
                                    self.yang_parent_name = "helper-addresses"

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_address = YLeaf(YType.str, "helper-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("vrf_name",
                                                    "helper_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.vrf_name.is_set or
                                        self.helper_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        self.helper_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "helper-address" + "[vrf-name='" + self.vrf_name.get() + "']" + "[helper-address='" + self.helper_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                                    if (self.helper_address.is_set or self.helper_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.helper_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "vrf-name" or name == "helper-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "helper-address"):
                                        self.helper_address = value
                                        self.helper_address.value_namespace = name_space
                                        self.helper_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.helper_address:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.helper_address:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "helper-addresses" + path_buffer

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

                                if (child_yang_name == "helper-address"):
                                    for c in self.helper_address:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses.HelperAddress()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.helper_address.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "helper-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.class_name.is_set or
                                self.link_address.is_set or
                                (self.helper_addresses is not None and self.helper_addresses.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.class_name.yfilter != YFilter.not_set or
                                self.link_address.yfilter != YFilter.not_set or
                                (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.class_name.get_name_leafdata())
                            if (self.link_address.is_set or self.link_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.link_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "helper-addresses"):
                                if (self.helper_addresses is None):
                                    self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class_.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                return self.helper_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "helper-addresses" or name == "class-name" or name == "link-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "class-name"):
                                self.class_name = value
                                self.class_name.value_namespace = name_space
                                self.class_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "link-address"):
                                self.link_address = value
                                self.link_address.value_namespace = name_space
                                self.link_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.class_:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.class_:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "classes" + path_buffer

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

                        if (child_yang_name == "class"):
                            for c in self.class_:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Proxy.Classes.Class_()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.class_.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "class"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Proxy.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "proxy"

                        self.mac = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")


                    class Mac(Entity):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"

                            self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"

                                self.block = YLeaf(YType.uint32, "block")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request = YLeaf(YType.uint32, "request")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("block",
                                                "limit",
                                                "request") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.block.is_set or
                                    self.limit.is_set or
                                    self.request.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.block.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "throttle" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.block.is_set or self.block.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.block.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request.is_set or self.request.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "block" or name == "limit" or name == "request"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "block"):
                                    self.block = value
                                    self.block.value_namespace = name_space
                                    self.block.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request"):
                                    self.request = value
                                    self.request.value_namespace = name_space
                                    self.request.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.throttle is not None and self.throttle.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.throttle is not None and self.throttle.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mac" + path_buffer

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

                            if (child_yang_name == "throttle"):
                                if (self.throttle is None):
                                    self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                                    self.throttle.parent = self
                                    self._children_name_map["throttle"] = "throttle"
                                return self.throttle

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "throttle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.mac is not None and self.mac.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.mac is not None and self.mac.has_operation()))

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

                        if (child_yang_name == "mac"):
                            if (self.mac is None):
                                self.mac = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac()
                                self.mac.parent = self
                                self._children_name_map["mac"] = "mac"
                            return self.mac

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mac"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.enable.is_set or
                        self.link_address.is_set or
                        self.route_add_disable.is_set or
                        self.src_intf_name.is_set or
                        (self.classes is not None and self.classes.has_data()) or
                        (self.interfaces is not None and self.interfaces.has_data()) or
                        (self.relay is not None and self.relay.has_data()) or
                        (self.sessions is not None and self.sessions.has_data()) or
                        (self.vrfs is not None and self.vrfs.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.link_address.yfilter != YFilter.not_set or
                        self.route_add_disable.yfilter != YFilter.not_set or
                        self.src_intf_name.yfilter != YFilter.not_set or
                        (self.classes is not None and self.classes.has_operation()) or
                        (self.interfaces is not None and self.interfaces.has_operation()) or
                        (self.relay is not None and self.relay.has_operation()) or
                        (self.sessions is not None and self.sessions.has_operation()) or
                        (self.vrfs is not None and self.vrfs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "proxy" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.link_address.is_set or self.link_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_address.get_name_leafdata())
                    if (self.route_add_disable.is_set or self.route_add_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route_add_disable.get_name_leafdata())
                    if (self.src_intf_name.is_set or self.src_intf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.src_intf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "classes"):
                        if (self.classes is None):
                            self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"
                        return self.classes

                    if (child_yang_name == "interfaces"):
                        if (self.interfaces is None):
                            self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"
                        return self.interfaces

                    if (child_yang_name == "relay"):
                        if (self.relay is None):
                            self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                            self.relay.parent = self
                            self._children_name_map["relay"] = "relay"
                        return self.relay

                    if (child_yang_name == "sessions"):
                        if (self.sessions is None):
                            self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                            self.sessions.parent = self
                            self._children_name_map["sessions"] = "sessions"
                        return self.sessions

                    if (child_yang_name == "vrfs"):
                        if (self.vrfs is None):
                            self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"
                        return self.vrfs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "classes" or name == "interfaces" or name == "relay" or name == "sessions" or name == "vrfs" or name == "enable" or name == "link-address" or name == "route-add-disable" or name == "src-intf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-address"):
                        self.link_address = value
                        self.link_address.value_namespace = name_space
                        self.link_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "route-add-disable"):
                        self.route_add_disable = value
                        self.route_add_disable.value_namespace = name_space
                        self.route_add_disable.value_namespace_prefix = name_space_prefix
                    if(value_path == "src-intf-name"):
                        self.src_intf_name = value
                        self.src_intf_name.value_namespace = name_space
                        self.src_intf_name.value_namespace_prefix = name_space_prefix


            class Server(Entity):
                """
                None
                
                .. attribute:: address_pool
                
                	Address pool name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: aftr_name
                
                	AFTR name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes>`
                
                .. attribute:: dhcpv6_options
                
                	DHCPv6 options
                	**type**\:   :py:class:`Dhcpv6Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options>`
                
                .. attribute:: dns_servers
                
                	DNS servers
                	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.DnsServers>`
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Server
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: lease
                
                	lease
                	**type**\:   :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Lease>`
                
                .. attribute:: preference
                
                	DHCP Server Preference
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: prefix_pool
                
                	Prefix pool name
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rapid_commit
                
                	Allow RAPID Commit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Profiles.Profile.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "profile"
                    self.is_presence_container = True

                    self.address_pool = YLeaf(YType.str, "address-pool")

                    self.aftr_name = YLeaf(YType.str, "aftr-name")

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.preference = YLeaf(YType.uint32, "preference")

                    self.prefix_pool = YLeaf(YType.str, "prefix-pool")

                    self.rapid_commit = YLeaf(YType.empty, "rapid-commit")

                    self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                    self.classes.parent = self
                    self._children_name_map["classes"] = "classes"
                    self._children_yang_names.add("classes")

                    self.dhcpv6_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options()
                    self.dhcpv6_options.parent = self
                    self._children_name_map["dhcpv6_options"] = "dhcpv6-options"
                    self._children_yang_names.add("dhcpv6-options")

                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                    self.dns_servers.parent = self
                    self._children_name_map["dns_servers"] = "dns-servers"
                    self._children_yang_names.add("dns-servers")

                    self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                    self.lease.parent = self
                    self._children_name_map["lease"] = "lease"
                    self._children_yang_names.add("lease")

                    self.sessions = Dhcpv6.Profiles.Profile.Server.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address_pool",
                                    "aftr_name",
                                    "domain_name",
                                    "enable",
                                    "preference",
                                    "prefix_pool",
                                    "rapid_commit") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Profiles.Profile.Server, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Profiles.Profile.Server, self).__setattr__(name, value)


                class Sessions(Entity):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "server"

                        self.mac = Dhcpv6.Profiles.Profile.Server.Sessions.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")


                    class Mac(Entity):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "sessions"

                            self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                            self.throttle.parent = self
                            self._children_name_map["throttle"] = "throttle"
                            self._children_yang_names.add("throttle")


                        class Throttle(Entity):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, self).__init__()

                                self.yang_name = "throttle"
                                self.yang_parent_name = "mac"

                                self.block = YLeaf(YType.uint32, "block")

                                self.limit = YLeaf(YType.uint32, "limit")

                                self.request = YLeaf(YType.uint32, "request")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("block",
                                                "limit",
                                                "request") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.block.is_set or
                                    self.limit.is_set or
                                    self.request.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.block.yfilter != YFilter.not_set or
                                    self.limit.yfilter != YFilter.not_set or
                                    self.request.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "throttle" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.block.is_set or self.block.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.block.get_name_leafdata())
                                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit.get_name_leafdata())
                                if (self.request.is_set or self.request.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.request.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "block" or name == "limit" or name == "request"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "block"):
                                    self.block = value
                                    self.block.value_namespace = name_space
                                    self.block.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit"):
                                    self.limit = value
                                    self.limit.value_namespace = name_space
                                    self.limit.value_namespace_prefix = name_space_prefix
                                if(value_path == "request"):
                                    self.request = value
                                    self.request.value_namespace = name_space
                                    self.request.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.throttle is not None and self.throttle.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.throttle is not None and self.throttle.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mac" + path_buffer

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

                            if (child_yang_name == "throttle"):
                                if (self.throttle is None):
                                    self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                                    self.throttle.parent = self
                                    self._children_name_map["throttle"] = "throttle"
                                return self.throttle

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "throttle"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.mac is not None and self.mac.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.mac is not None and self.mac.has_operation()))

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

                        if (child_yang_name == "mac"):
                            if (self.mac is None):
                                self.mac = Dhcpv6.Profiles.Profile.Server.Sessions.Mac()
                                self.mac.parent = self
                                self._children_name_map["mac"] = "mac"
                            return self.mac

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mac"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class DnsServers(Entity):
                    """
                    DNS servers
                    
                    .. attribute:: dns_server
                    
                    	Server's IPv6 address
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__init__()

                        self.yang_name = "dns-servers"
                        self.yang_parent_name = "server"

                        self.dns_server = YLeafList(YType.str, "dns-server")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dns_server") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Server.DnsServers, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.dns_server.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return False

                    def has_operation(self):
                        for leaf in self.dns_server.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dns_server.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dns-servers" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.dns_server.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dns-server"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dns-server"):
                            self.dns_server.append(value)


                class Classes(Entity):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class_>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Classes, self).__init__()

                        self.yang_name = "classes"
                        self.yang_parent_name = "server"

                        self.class_ = YList(self)

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
                                    super(Dhcpv6.Profiles.Profile.Server.Classes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Server.Classes, self).__setattr__(name, value)


                    class Class_(Entity):
                        """
                        None
                        
                        .. attribute:: class_name  <key>
                        
                        	class name
                        	**type**\:  str
                        
                        	**length:** 1..128
                        
                        .. attribute:: address_pool
                        
                        	Address pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:   :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers>`
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: preference
                        
                        	DHCP Server Preference
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: prefix_pool
                        
                        	Prefix pool name
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Classes.Class_, self).__init__()

                            self.yang_name = "class"
                            self.yang_parent_name = "classes"

                            self.class_name = YLeaf(YType.str, "class-name")

                            self.address_pool = YLeaf(YType.str, "address-pool")

                            self.domain_name = YLeaf(YType.str, "domain-name")

                            self.preference = YLeaf(YType.uint32, "preference")

                            self.prefix_pool = YLeaf(YType.str, "prefix-pool")

                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"
                            self._children_yang_names.add("dns-servers")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("class_name",
                                            "address_pool",
                                            "domain_name",
                                            "preference",
                                            "prefix_pool") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Server.Classes.Class_, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Server.Classes.Class_, self).__setattr__(name, value)


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	Server's IPv6 address
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2016-10-10'

                            def __init__(self):
                                super(Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "class"

                                self.dns_server = YLeafList(YType.str, "dns-server")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dns_server") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.dns_server.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.dns_server.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dns_server.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dns-servers" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.dns_server.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dns-server"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dns-server"):
                                    self.dns_server.append(value)

                        def has_data(self):
                            return (
                                self.class_name.is_set or
                                self.address_pool.is_set or
                                self.domain_name.is_set or
                                self.preference.is_set or
                                self.prefix_pool.is_set or
                                (self.dns_servers is not None and self.dns_servers.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.class_name.yfilter != YFilter.not_set or
                                self.address_pool.yfilter != YFilter.not_set or
                                self.domain_name.yfilter != YFilter.not_set or
                                self.preference.yfilter != YFilter.not_set or
                                self.prefix_pool.yfilter != YFilter.not_set or
                                (self.dns_servers is not None and self.dns_servers.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.class_name.get_name_leafdata())
                            if (self.address_pool.is_set or self.address_pool.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_pool.get_name_leafdata())
                            if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.domain_name.get_name_leafdata())
                            if (self.preference.is_set or self.preference.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preference.get_name_leafdata())
                            if (self.prefix_pool.is_set or self.prefix_pool.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_pool.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dns-servers"):
                                if (self.dns_servers is None):
                                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class_.DnsServers()
                                    self.dns_servers.parent = self
                                    self._children_name_map["dns_servers"] = "dns-servers"
                                return self.dns_servers

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dns-servers" or name == "class-name" or name == "address-pool" or name == "domain-name" or name == "preference" or name == "prefix-pool"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "class-name"):
                                self.class_name = value
                                self.class_name.value_namespace = name_space
                                self.class_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "address-pool"):
                                self.address_pool = value
                                self.address_pool.value_namespace = name_space
                                self.address_pool.value_namespace_prefix = name_space_prefix
                            if(value_path == "domain-name"):
                                self.domain_name = value
                                self.domain_name.value_namespace = name_space
                                self.domain_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "preference"):
                                self.preference = value
                                self.preference.value_namespace = name_space
                                self.preference.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-pool"):
                                self.prefix_pool = value
                                self.prefix_pool.value_namespace = name_space
                                self.prefix_pool.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.class_:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.class_:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "classes" + path_buffer

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

                        if (child_yang_name == "class"):
                            for c in self.class_:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Dhcpv6.Profiles.Profile.Server.Classes.Class_()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.class_.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "class"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Lease(Entity):
                    """
                    lease
                    
                    .. attribute:: days
                    
                    	Days
                    	**type**\:  int
                    
                    	**range:** 0..365
                    
                    	**units**\: day
                    
                    .. attribute:: hours
                    
                    	Hours
                    	**type**\:  int
                    
                    	**range:** 0..23
                    
                    	**units**\: hour
                    
                    .. attribute:: infinite
                    
                    	Set string
                    	**type**\:  str
                    
                    .. attribute:: minutes
                    
                    	Minutes
                    	**type**\:  int
                    
                    	**range:** 1..59
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Lease, self).__init__()

                        self.yang_name = "lease"
                        self.yang_parent_name = "server"

                        self.days = YLeaf(YType.uint32, "days")

                        self.hours = YLeaf(YType.uint32, "hours")

                        self.infinite = YLeaf(YType.str, "infinite")

                        self.minutes = YLeaf(YType.uint32, "minutes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("days",
                                        "hours",
                                        "infinite",
                                        "minutes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Dhcpv6.Profiles.Profile.Server.Lease, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Dhcpv6.Profiles.Profile.Server.Lease, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.days.is_set or
                            self.hours.is_set or
                            self.infinite.is_set or
                            self.minutes.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.days.yfilter != YFilter.not_set or
                            self.hours.yfilter != YFilter.not_set or
                            self.infinite.yfilter != YFilter.not_set or
                            self.minutes.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lease" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.days.is_set or self.days.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.days.get_name_leafdata())
                        if (self.hours.is_set or self.hours.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hours.get_name_leafdata())
                        if (self.infinite.is_set or self.infinite.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.infinite.get_name_leafdata())
                        if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minutes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "days" or name == "hours" or name == "infinite" or name == "minutes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "days"):
                            self.days = value
                            self.days.value_namespace = name_space
                            self.days.value_namespace_prefix = name_space_prefix
                        if(value_path == "hours"):
                            self.hours = value
                            self.hours.value_namespace = name_space
                            self.hours.value_namespace_prefix = name_space_prefix
                        if(value_path == "infinite"):
                            self.infinite = value
                            self.infinite.value_namespace = name_space
                            self.infinite.value_namespace_prefix = name_space_prefix
                        if(value_path == "minutes"):
                            self.minutes = value
                            self.minutes.value_namespace = name_space
                            self.minutes.value_namespace_prefix = name_space_prefix


                class Dhcpv6Options(Entity):
                    """
                    DHCPv6 options
                    
                    .. attribute:: vendor_options
                    
                    	Vendor options
                    	**type**\:   :py:class:`VendorOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2016-10-10'

                    def __init__(self):
                        super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options, self).__init__()

                        self.yang_name = "dhcpv6-options"
                        self.yang_parent_name = "server"

                        self.vendor_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions()
                        self.vendor_options.parent = self
                        self._children_name_map["vendor_options"] = "vendor-options"
                        self._children_yang_names.add("vendor-options")


                    class VendorOptions(Entity):
                        """
                        Vendor options
                        
                        .. attribute:: type
                        
                        	Set string
                        	**type**\:  str
                        
                        .. attribute:: vendor_options
                        
                        	Vendor options
                        	**type**\:  str
                        
                        	**length:** 1..512
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2016-10-10'

                        def __init__(self):
                            super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, self).__init__()

                            self.yang_name = "vendor-options"
                            self.yang_parent_name = "dhcpv6-options"

                            self.type = YLeaf(YType.str, "type")

                            self.vendor_options = YLeaf(YType.str, "vendor-options")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("type",
                                            "vendor_options") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.type.is_set or
                                self.vendor_options.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                self.vendor_options.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vendor-options" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())
                            if (self.vendor_options.is_set or self.vendor_options.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vendor_options.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "type" or name == "vendor-options"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix
                            if(value_path == "vendor-options"):
                                self.vendor_options = value
                                self.vendor_options.value_namespace = name_space
                                self.vendor_options.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.vendor_options is not None and self.vendor_options.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.vendor_options is not None and self.vendor_options.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dhcpv6-options" + path_buffer

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

                        if (child_yang_name == "vendor-options"):
                            if (self.vendor_options is None):
                                self.vendor_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options.VendorOptions()
                                self.vendor_options.parent = self
                                self._children_name_map["vendor_options"] = "vendor-options"
                            return self.vendor_options

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vendor-options"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.address_pool.is_set or
                        self.aftr_name.is_set or
                        self.domain_name.is_set or
                        self.enable.is_set or
                        self.preference.is_set or
                        self.prefix_pool.is_set or
                        self.rapid_commit.is_set or
                        (self.classes is not None and self.classes.has_data()) or
                        (self.dhcpv6_options is not None and self.dhcpv6_options.has_data()) or
                        (self.dns_servers is not None and self.dns_servers.has_data()) or
                        (self.lease is not None and self.lease.has_data()) or
                        (self.sessions is not None and self.sessions.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address_pool.yfilter != YFilter.not_set or
                        self.aftr_name.yfilter != YFilter.not_set or
                        self.domain_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.preference.yfilter != YFilter.not_set or
                        self.prefix_pool.yfilter != YFilter.not_set or
                        self.rapid_commit.yfilter != YFilter.not_set or
                        (self.classes is not None and self.classes.has_operation()) or
                        (self.dhcpv6_options is not None and self.dhcpv6_options.has_operation()) or
                        (self.dns_servers is not None and self.dns_servers.has_operation()) or
                        (self.lease is not None and self.lease.has_operation()) or
                        (self.sessions is not None and self.sessions.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address_pool.is_set or self.address_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_pool.get_name_leafdata())
                    if (self.aftr_name.is_set or self.aftr_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aftr_name.get_name_leafdata())
                    if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())
                    if (self.preference.is_set or self.preference.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.preference.get_name_leafdata())
                    if (self.prefix_pool.is_set or self.prefix_pool.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_pool.get_name_leafdata())
                    if (self.rapid_commit.is_set or self.rapid_commit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rapid_commit.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "classes"):
                        if (self.classes is None):
                            self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"
                        return self.classes

                    if (child_yang_name == "dhcpv6-options"):
                        if (self.dhcpv6_options is None):
                            self.dhcpv6_options = Dhcpv6.Profiles.Profile.Server.Dhcpv6Options()
                            self.dhcpv6_options.parent = self
                            self._children_name_map["dhcpv6_options"] = "dhcpv6-options"
                        return self.dhcpv6_options

                    if (child_yang_name == "dns-servers"):
                        if (self.dns_servers is None):
                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"
                        return self.dns_servers

                    if (child_yang_name == "lease"):
                        if (self.lease is None):
                            self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                            self.lease.parent = self
                            self._children_name_map["lease"] = "lease"
                        return self.lease

                    if (child_yang_name == "sessions"):
                        if (self.sessions is None):
                            self.sessions = Dhcpv6.Profiles.Profile.Server.Sessions()
                            self.sessions.parent = self
                            self._children_name_map["sessions"] = "sessions"
                        return self.sessions

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "classes" or name == "dhcpv6-options" or name == "dns-servers" or name == "lease" or name == "sessions" or name == "address-pool" or name == "aftr-name" or name == "domain-name" or name == "enable" or name == "preference" or name == "prefix-pool" or name == "rapid-commit"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address-pool"):
                        self.address_pool = value
                        self.address_pool.value_namespace = name_space
                        self.address_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "aftr-name"):
                        self.aftr_name = value
                        self.aftr_name.value_namespace = name_space
                        self.aftr_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "domain-name"):
                        self.domain_name = value
                        self.domain_name.value_namespace = name_space
                        self.domain_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "preference"):
                        self.preference = value
                        self.preference.value_namespace = name_space
                        self.preference.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-pool"):
                        self.prefix_pool = value
                        self.prefix_pool.value_namespace = name_space
                        self.prefix_pool.value_namespace_prefix = name_space_prefix
                    if(value_path == "rapid-commit"):
                        self.rapid_commit = value
                        self.rapid_commit.value_namespace = name_space
                        self.rapid_commit.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.profile_name.is_set or
                    (self.base is not None) or
                    (self.proxy is not None) or
                    (self.relay is not None) or
                    (self.server is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.profile_name.yfilter != YFilter.not_set or
                    (self.base is not None and self.base.has_operation()) or
                    (self.proxy is not None and self.proxy.has_operation()) or
                    (self.relay is not None and self.relay.has_operation()) or
                    (self.server is not None and self.server.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "profile" + "[profile-name='" + self.profile_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/profiles/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "base"):
                    if (self.base is None):
                        self.base = Dhcpv6.Profiles.Profile.Base()
                        self.base.parent = self
                        self._children_name_map["base"] = "base"
                    return self.base

                if (child_yang_name == "proxy"):
                    if (self.proxy is None):
                        self.proxy = Dhcpv6.Profiles.Profile.Proxy()
                        self.proxy.parent = self
                        self._children_name_map["proxy"] = "proxy"
                    return self.proxy

                if (child_yang_name == "relay"):
                    if (self.relay is None):
                        self.relay = Dhcpv6.Profiles.Profile.Relay()
                        self.relay.parent = self
                        self._children_name_map["relay"] = "relay"
                    return self.relay

                if (child_yang_name == "server"):
                    if (self.server is None):
                        self.server = Dhcpv6.Profiles.Profile.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                    return self.server

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "base" or name == "proxy" or name == "relay" or name == "server" or name == "profile-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "profile-name"):
                    self.profile_name = value
                    self.profile_name.value_namespace = name_space
                    self.profile_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.profile:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.profile:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "profiles" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "profile"):
                for c in self.profile:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Dhcpv6.Profiles.Profile()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.profile.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "profile"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        Table of Interface
        
        .. attribute:: interface
        
        	None
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2016-10-10'

        def __init__(self):
            super(Dhcpv6.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "dhcpv6"

            self.interface = YList(self)

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
                        super(Dhcpv6.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Dhcpv6.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            None
            
            .. attribute:: interface_name  <key>
            
            	Interface to configure
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: base
            
            	Assign a base profile to interface
            	**type**\:   :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Base>`
            
            .. attribute:: pppoe
            
            	PPPoE subscriber interface
            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Pppoe>`
            
            .. attribute:: proxy
            
            	Assign a proxy profile to interface
            	**type**\:   :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Proxy>`
            
            .. attribute:: relay
            
            	Assign a relay profile to interface
            	**type**\:   :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Relay>`
            
            .. attribute:: server
            
            	Assign a server profile to interface
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Server>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2016-10-10'

            def __init__(self):
                super(Dhcpv6.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.base = Dhcpv6.Interfaces.Interface.Base()
                self.base.parent = self
                self._children_name_map["base"] = "base"
                self._children_yang_names.add("base")

                self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                self.pppoe.parent = self
                self._children_name_map["pppoe"] = "pppoe"
                self._children_yang_names.add("pppoe")

                self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                self.proxy.parent = self
                self._children_name_map["proxy"] = "proxy"
                self._children_yang_names.add("proxy")

                self.relay = Dhcpv6.Interfaces.Interface.Relay()
                self.relay.parent = self
                self._children_name_map["relay"] = "relay"
                self._children_yang_names.add("relay")

                self.server = Dhcpv6.Interfaces.Interface.Server()
                self.server.parent = self
                self._children_name_map["server"] = "server"
                self._children_yang_names.add("server")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Dhcpv6.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Dhcpv6.Interfaces.Interface, self).__setattr__(name, value)


            class Pppoe(Entity):
                """
                PPPoE subscriber interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Pppoe, self).__init__()

                    self.yang_name = "pppoe"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Interfaces.Interface.Pppoe, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Interfaces.Interface.Pppoe, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pppoe" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class Proxy(Entity):
                """
                Assign a proxy profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Proxy, self).__init__()

                    self.yang_name = "proxy"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Interfaces.Interface.Proxy, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Interfaces.Interface.Proxy, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "proxy" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class Base(Entity):
                """
                Assign a base profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Base, self).__init__()

                    self.yang_name = "base"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Interfaces.Interface.Base, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Interfaces.Interface.Base, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "base" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class Server(Entity):
                """
                Assign a server profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Interfaces.Interface.Server, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Interfaces.Interface.Server, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class Relay(Entity):
                """
                Assign a relay profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2016-10-10'

                def __init__(self):
                    super(Dhcpv6.Interfaces.Interface.Relay, self).__init__()

                    self.yang_name = "relay"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Dhcpv6.Interfaces.Interface.Relay, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Dhcpv6.Interfaces.Interface.Relay, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "relay" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.base is not None and self.base.has_data()) or
                    (self.pppoe is not None and self.pppoe.has_data()) or
                    (self.proxy is not None and self.proxy.has_data()) or
                    (self.relay is not None and self.relay.has_data()) or
                    (self.server is not None and self.server.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.base is not None and self.base.has_operation()) or
                    (self.pppoe is not None and self.pppoe.has_operation()) or
                    (self.proxy is not None and self.proxy.has_operation()) or
                    (self.relay is not None and self.relay.has_operation()) or
                    (self.server is not None and self.server.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "base"):
                    if (self.base is None):
                        self.base = Dhcpv6.Interfaces.Interface.Base()
                        self.base.parent = self
                        self._children_name_map["base"] = "base"
                    return self.base

                if (child_yang_name == "pppoe"):
                    if (self.pppoe is None):
                        self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                        self.pppoe.parent = self
                        self._children_name_map["pppoe"] = "pppoe"
                    return self.pppoe

                if (child_yang_name == "proxy"):
                    if (self.proxy is None):
                        self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                        self.proxy.parent = self
                        self._children_name_map["proxy"] = "proxy"
                    return self.proxy

                if (child_yang_name == "relay"):
                    if (self.relay is None):
                        self.relay = Dhcpv6.Interfaces.Interface.Relay()
                        self.relay.parent = self
                        self._children_name_map["relay"] = "relay"
                    return self.relay

                if (child_yang_name == "server"):
                    if (self.server is None):
                        self.server = Dhcpv6.Interfaces.Interface.Server()
                        self.server.parent = self
                        self._children_name_map["server"] = "server"
                    return self.server

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "base" or name == "pppoe" or name == "proxy" or name == "relay" or name == "server" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Dhcpv6.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.allow_duid_change.is_set or
            self.enable.is_set or
            (self.database is not None and self.database.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.profiles is not None and self.profiles.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.allow_duid_change.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.database is not None and self.database.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.profiles is not None and self.profiles.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.allow_duid_change.is_set or self.allow_duid_change.yfilter != YFilter.not_set):
            leaf_name_data.append(self.allow_duid_change.get_name_leafdata())
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "database"):
            if (self.database is None):
                self.database = Dhcpv6.Database()
                self.database.parent = self
                self._children_name_map["database"] = "database"
            return self.database

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Dhcpv6.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "profiles"):
            if (self.profiles is None):
                self.profiles = Dhcpv6.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
            return self.profiles

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "database" or name == "interfaces" or name == "profiles" or name == "allow-duid-change" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "allow-duid-change"):
            self.allow_duid_change = value
            self.allow_duid_change.value_namespace = name_space
            self.allow_duid_change.value_namespace_prefix = name_space_prefix
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Dhcpv6()
        return self._top_entity

