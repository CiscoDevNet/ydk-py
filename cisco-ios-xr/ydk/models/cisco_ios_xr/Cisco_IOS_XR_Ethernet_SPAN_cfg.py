""" Cisco_IOS_XR_Ethernet_SPAN_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package configuration.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: none

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SpanDestination(Enum):
    """
    SpanDestination

    Span destination

    .. data:: interface = 0

    	Destination Interface

    .. data:: pseudowire = 1

    	Destination Pseudowire

    .. data:: ipv4_address = 2

    	Destination next-hop IPv4 address

    .. data:: ipv6_address = 3

    	Destination next-hop IPv6 address

    """

    interface = Enum.YLeaf(0, "interface")

    pseudowire = Enum.YLeaf(1, "pseudowire")

    ipv4_address = Enum.YLeaf(2, "ipv4-address")

    ipv6_address = Enum.YLeaf(3, "ipv6-address")


class SpanMirrorInterval(Enum):
    """
    SpanMirrorInterval

    Span mirror interval

    .. data:: Y_512 = 1

    	Mirror 1 in every 512 packets

    .. data:: Y_1k = 2

    	Mirror 1 in every 1024 packets

    .. data:: Y_2k = 3

    	Mirror 1 in every 2048 packets

    .. data:: Y_4k = 4

    	Mirror 1 in every 4096 packets

    .. data:: Y_8k = 5

    	Mirror 1 in every 8192 packets

    .. data:: Y_16k = 6

    	Mirror 1 in every 16384 packets

    """

    Y_512 = Enum.YLeaf(1, "512")

    Y_1k = Enum.YLeaf(2, "1k")

    Y_2k = Enum.YLeaf(3, "2k")

    Y_4k = Enum.YLeaf(4, "4k")

    Y_8k = Enum.YLeaf(5, "8k")

    Y_16k = Enum.YLeaf(6, "16k")


class SpanTrafficDirection(Enum):
    """
    SpanTrafficDirection

    Span traffic direction

    .. data:: rx_only = 1

    	Replicate only received (ingress) traffic

    .. data:: tx_only = 2

    	Replicate only transmitted (egress) traffic

    """

    rx_only = Enum.YLeaf(1, "rx-only")

    tx_only = Enum.YLeaf(2, "tx-only")



class SpanMonitorSession(Entity):
    """
    none
    
    .. attribute:: sessions
    
    	Monitor\-session configuration commands
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions>`
    
    

    """

    _prefix = 'ethernet-span-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SpanMonitorSession, self).__init__()
        self._top_entity = None

        self.yang_name = "span-monitor-session"
        self.yang_parent_name = "Cisco-IOS-XR-Ethernet-SPAN-cfg"

        self.sessions = SpanMonitorSession.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")


    class Sessions(Entity):
        """
        Monitor\-session configuration commands
        
        .. attribute:: session
        
        	Configuration for a particular Monitor Session
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session>`
        
        

        """

        _prefix = 'ethernet-span-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "span-monitor-session"

            self.session = YList(self)

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
                        super(SpanMonitorSession.Sessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SpanMonitorSession.Sessions, self).__setattr__(name, value)


        class Session(Entity):
            """
            Configuration for a particular Monitor Session
            
            .. attribute:: session  <key>
            
            	Session Name
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: class_
            
            	Enable a Monitor Session.  Setting this item causes the Monitor Session to be created
            	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
            
            	**default value**\: ethernet
            
            .. attribute:: destination
            
            	Specify a destination
            	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanMonitorSession.Sessions.Session.Destination>`
            
            

            """

            _prefix = 'ethernet-span-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"

                self.session = YLeaf(YType.str, "session")

                self.class_ = YLeaf(YType.enumeration, "class")

                self.destination = SpanMonitorSession.Sessions.Session.Destination()
                self.destination.parent = self
                self._children_name_map["destination"] = "destination"
                self._children_yang_names.add("destination")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("session",
                                "class_") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SpanMonitorSession.Sessions.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SpanMonitorSession.Sessions.Session, self).__setattr__(name, value)


            class Destination(Entity):
                """
                Specify a destination
                
                .. attribute:: destination_interface_name
                
                	Specify the destination interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_ipv4_address
                
                	Specify the destination next\-hop IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_ipv6_address
                
                	Specify the destination next\-hop IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination_type
                
                	Specify the type of destination
                	**type**\:   :py:class:`SpanDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_cfg.SpanDestination>`
                
                

                """

                _prefix = 'ethernet-span-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Sessions.Session.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "session"

                    self.destination_interface_name = YLeaf(YType.str, "destination-interface-name")

                    self.destination_ipv4_address = YLeaf(YType.str, "destination-ipv4-address")

                    self.destination_ipv6_address = YLeaf(YType.str, "destination-ipv6-address")

                    self.destination_type = YLeaf(YType.enumeration, "destination-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination_interface_name",
                                    "destination_ipv4_address",
                                    "destination_ipv6_address",
                                    "destination_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SpanMonitorSession.Sessions.Session.Destination, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Sessions.Session.Destination, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.destination_interface_name.is_set or
                        self.destination_ipv4_address.is_set or
                        self.destination_ipv6_address.is_set or
                        self.destination_type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination_interface_name.yfilter != YFilter.not_set or
                        self.destination_ipv4_address.yfilter != YFilter.not_set or
                        self.destination_ipv6_address.yfilter != YFilter.not_set or
                        self.destination_type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination_interface_name.is_set or self.destination_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_interface_name.get_name_leafdata())
                    if (self.destination_ipv4_address.is_set or self.destination_ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ipv4_address.get_name_leafdata())
                    if (self.destination_ipv6_address.is_set or self.destination_ipv6_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_ipv6_address.get_name_leafdata())
                    if (self.destination_type.is_set or self.destination_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-interface-name" or name == "destination-ipv4-address" or name == "destination-ipv6-address" or name == "destination-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination-interface-name"):
                        self.destination_interface_name = value
                        self.destination_interface_name.value_namespace = name_space
                        self.destination_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-ipv4-address"):
                        self.destination_ipv4_address = value
                        self.destination_ipv4_address.value_namespace = name_space
                        self.destination_ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-ipv6-address"):
                        self.destination_ipv6_address = value
                        self.destination_ipv6_address.value_namespace = name_space
                        self.destination_ipv6_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-type"):
                        self.destination_type = value
                        self.destination_type.value_namespace = name_space
                        self.destination_type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.session.is_set or
                    self.class_.is_set or
                    (self.destination is not None and self.destination.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.session.yfilter != YFilter.not_set or
                    self.class_.yfilter != YFilter.not_set or
                    (self.destination is not None and self.destination.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + "[session='" + self.session.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.session.is_set or self.session.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session.get_name_leafdata())
                if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.class_.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "destination"):
                    if (self.destination is None):
                        self.destination = SpanMonitorSession.Sessions.Session.Destination()
                        self.destination.parent = self
                        self._children_name_map["destination"] = "destination"
                    return self.destination

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "session" or name == "class"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "session"):
                    self.session = value
                    self.session.value_namespace = name_space
                    self.session.value_namespace_prefix = name_space_prefix
                if(value_path == "class"):
                    self.class_ = value
                    self.class_.value_namespace = name_space
                    self.class_.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session"):
                for c in self.session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SpanMonitorSession.Sessions.Session()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.sessions is not None and self.sessions.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.sessions is not None and self.sessions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-cfg:span-monitor-session" + path_buffer

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

        if (child_yang_name == "sessions"):
            if (self.sessions is None):
                self.sessions = SpanMonitorSession.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
            return self.sessions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "sessions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SpanMonitorSession()
        return self._top_entity

