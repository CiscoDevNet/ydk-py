""" Cisco_IOS_XR_ip_rsvp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rsvp package configuration.

This module contains definitions
for the following management objects\:
  rsvp\: Global RSVP configuration commands

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class RsvpBc0(Enum):
    """
    RsvpBc0

    Rsvp bc0

    .. data:: bc0 = 1

    	Keyword is bc0

    .. data:: global_pool = 2

    	Keyword is global-pool

    .. data:: not_specified = 3

    	Keyword is not specified

    """

    bc0 = Enum.YLeaf(1, "bc0")

    global_pool = Enum.YLeaf(2, "global-pool")

    not_specified = Enum.YLeaf(3, "not-specified")


class RsvpBc1(Enum):
    """
    RsvpBc1

    Rsvp bc1

    .. data:: bc1 = 1

    	Keyword is bc1

    .. data:: sub_pool = 2

    	Keyword is sub-pool

    """

    bc1 = Enum.YLeaf(1, "bc1")

    sub_pool = Enum.YLeaf(2, "sub-pool")


class RsvpBwCfg(Enum):
    """
    RsvpBwCfg

    Rsvp bw cfg

    .. data:: absolute = 0

    	Configuration is in absolute bandwidth values

    .. data:: percentage = 1

    	Configuration is in percentage of physical

    	bandwidth values

    """

    absolute = Enum.YLeaf(0, "absolute")

    percentage = Enum.YLeaf(1, "percentage")


class RsvpRdm(Enum):
    """
    RsvpRdm

    Rsvp rdm

    .. data:: rdm = 1

    	RDM Keyword Specified

    .. data:: not_specified = 2

    	RDM Keyword Not Specified

    .. data:: use_default_bandwidth = 3

    	Use Default Bandwidth - 75% Link Bandwidth

    """

    rdm = Enum.YLeaf(1, "rdm")

    not_specified = Enum.YLeaf(2, "not-specified")

    use_default_bandwidth = Enum.YLeaf(3, "use-default-bandwidth")



class Rsvp(Entity):
    """
    Global RSVP configuration commands
    
    .. attribute:: authentication
    
    	Configure RSVP authentication
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Authentication>`
    
    .. attribute:: controllers
    
    	Controller table
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers>`
    
    .. attribute:: global_bandwidth
    
    	Configure Global Bandwidth Parameters
    	**type**\:   :py:class:`GlobalBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth>`
    
    .. attribute:: global_logging
    
    	Global Logging
    	**type**\:   :py:class:`GlobalLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalLogging>`
    
    .. attribute:: interfaces
    
    	Interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces>`
    
    .. attribute:: neighbors
    
    	RSVP Neighbor Table
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors>`
    
    .. attribute:: signalling
    
    	Configure Global RSVP signalling parameters
    	**type**\:   :py:class:`Signalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling>`
    
    

    """

    _prefix = 'ip-rsvp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Rsvp, self).__init__()
        self._top_entity = None

        self.yang_name = "rsvp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-rsvp-cfg"

        self.authentication = Rsvp.Authentication()
        self.authentication.parent = self
        self._children_name_map["authentication"] = "authentication"
        self._children_yang_names.add("authentication")

        self.controllers = Rsvp.Controllers()
        self.controllers.parent = self
        self._children_name_map["controllers"] = "controllers"
        self._children_yang_names.add("controllers")

        self.global_bandwidth = Rsvp.GlobalBandwidth()
        self.global_bandwidth.parent = self
        self._children_name_map["global_bandwidth"] = "global-bandwidth"
        self._children_yang_names.add("global-bandwidth")

        self.global_logging = Rsvp.GlobalLogging()
        self.global_logging.parent = self
        self._children_name_map["global_logging"] = "global-logging"
        self._children_yang_names.add("global-logging")

        self.interfaces = Rsvp.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.neighbors = Rsvp.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")

        self.signalling = Rsvp.Signalling()
        self.signalling.parent = self
        self._children_name_map["signalling"] = "signalling"
        self._children_yang_names.add("signalling")


    class Neighbors(Entity):
        """
        RSVP Neighbor Table
        
        .. attribute:: neighbor
        
        	RSVP neighbor configuration
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "rsvp"

            self.neighbor = YList(self)

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
                        super(Rsvp.Neighbors, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.Neighbors, self).__setattr__(name, value)


        class Neighbor(Entity):
            """
            RSVP neighbor configuration
            
            .. attribute:: neighbor  <key>
            
            	Neighbor IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor.Authentication>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"

                self.neighbor = YLeaf(YType.str, "neighbor")

                self.authentication = Rsvp.Neighbors.Neighbor.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("neighbor") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Neighbors.Neighbor, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Neighbors.Neighbor, self).__setattr__(name, value)


            class Authentication(Entity):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Neighbors.Neighbor.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "neighbor"

                    self.enable = YLeaf(YType.boolean, "enable")

                    self.key_chain = YLeaf(YType.str, "key-chain")

                    self.life_time = YLeaf(YType.uint32, "life-time")

                    self.window_size = YLeaf(YType.uint32, "window-size")

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
                                    "key_chain",
                                    "life_time",
                                    "window_size") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.Neighbors.Neighbor.Authentication, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.Neighbors.Neighbor.Authentication, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enable.is_set or
                        self.key_chain.is_set or
                        self.life_time.is_set or
                        self.window_size.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.key_chain.yfilter != YFilter.not_set or
                        self.life_time.yfilter != YFilter.not_set or
                        self.window_size.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication" + path_buffer

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
                    if (self.key_chain.is_set or self.key_chain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_chain.get_name_leafdata())
                    if (self.life_time.is_set or self.life_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.life_time.get_name_leafdata())
                    if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.window_size.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enable" or name == "key-chain" or name == "life-time" or name == "window-size"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "key-chain"):
                        self.key_chain = value
                        self.key_chain.value_namespace = name_space
                        self.key_chain.value_namespace_prefix = name_space_prefix
                    if(value_path == "life-time"):
                        self.life_time = value
                        self.life_time.value_namespace = name_space
                        self.life_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "window-size"):
                        self.window_size = value
                        self.window_size.value_namespace = name_space
                        self.window_size.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.neighbor.is_set or
                    (self.authentication is not None and self.authentication.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.neighbor.yfilter != YFilter.not_set or
                    (self.authentication is not None and self.authentication.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbor" + "[neighbor='" + self.neighbor.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/neighbors/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.neighbor.is_set or self.neighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.neighbor.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authentication"):
                    if (self.authentication is None):
                        self.authentication = Rsvp.Neighbors.Neighbor.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                    return self.authentication

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authentication" or name == "neighbor"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "neighbor"):
                    self.neighbor = value
                    self.neighbor.value_namespace = name_space
                    self.neighbor.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.neighbor:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.neighbor:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "neighbors" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "neighbor"):
                for c in self.neighbor:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rsvp.Neighbors.Neighbor()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.neighbor.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "neighbor"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Controllers(Entity):
        """
        Controller table
        
        .. attribute:: controller
        
        	Controller configuration
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.Controllers, self).__init__()

            self.yang_name = "controllers"
            self.yang_parent_name = "rsvp"

            self.controller = YList(self)

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
                        super(Rsvp.Controllers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.Controllers, self).__setattr__(name, value)


        class Controller(Entity):
            """
            Controller configuration
            
            .. attribute:: controller_name  <key>
            
            	Name of controller
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: cntl_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`CntlSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Controllers.Controller, self).__init__()

                self.yang_name = "controller"
                self.yang_parent_name = "controllers"

                self.controller_name = YLeaf(YType.str, "controller-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.cntl_signalling = Rsvp.Controllers.Controller.CntlSignalling()
                self.cntl_signalling.parent = self
                self._children_name_map["cntl_signalling"] = "cntl-signalling"
                self._children_yang_names.add("cntl-signalling")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("controller_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Controllers.Controller, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Controllers.Controller, self).__setattr__(name, value)


            class CntlSignalling(Entity):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling.OutOfBand>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Controllers.Controller.CntlSignalling, self).__init__()

                    self.yang_name = "cntl-signalling"
                    self.yang_parent_name = "controller"

                    self.out_of_band = Rsvp.Controllers.Controller.CntlSignalling.OutOfBand()
                    self.out_of_band.parent = self
                    self._children_name_map["out_of_band"] = "out-of-band"
                    self._children_yang_names.add("out-of-band")


                class OutOfBand(Entity):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Controllers.Controller.CntlSignalling.OutOfBand, self).__init__()

                        self.yang_name = "out-of-band"
                        self.yang_parent_name = "cntl-signalling"

                        self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                        self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("missed_messages",
                                        "refresh_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Controllers.Controller.CntlSignalling.OutOfBand, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Controllers.Controller.CntlSignalling.OutOfBand, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.missed_messages.is_set or
                            self.refresh_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.missed_messages.yfilter != YFilter.not_set or
                            self.refresh_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "out-of-band" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.missed_messages.is_set or self.missed_messages.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.missed_messages.get_name_leafdata())
                        if (self.refresh_interval.is_set or self.refresh_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.refresh_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "missed-messages" or name == "refresh-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "missed-messages"):
                            self.missed_messages = value
                            self.missed_messages.value_namespace = name_space
                            self.missed_messages.value_namespace_prefix = name_space_prefix
                        if(value_path == "refresh-interval"):
                            self.refresh_interval = value
                            self.refresh_interval.value_namespace = name_space
                            self.refresh_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.out_of_band is not None and self.out_of_band.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.out_of_band is not None and self.out_of_band.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cntl-signalling" + path_buffer

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

                    if (child_yang_name == "out-of-band"):
                        if (self.out_of_band is None):
                            self.out_of_band = Rsvp.Controllers.Controller.CntlSignalling.OutOfBand()
                            self.out_of_band.parent = self
                            self._children_name_map["out_of_band"] = "out-of-band"
                        return self.out_of_band

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "out-of-band"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.controller_name.is_set or
                    self.enable.is_set or
                    (self.cntl_signalling is not None and self.cntl_signalling.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.controller_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.cntl_signalling is not None and self.cntl_signalling.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "controller" + "[controller-name='" + self.controller_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/controllers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.controller_name.is_set or self.controller_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.controller_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cntl-signalling"):
                    if (self.cntl_signalling is None):
                        self.cntl_signalling = Rsvp.Controllers.Controller.CntlSignalling()
                        self.cntl_signalling.parent = self
                        self._children_name_map["cntl_signalling"] = "cntl-signalling"
                    return self.cntl_signalling

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cntl-signalling" or name == "controller-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "controller-name"):
                    self.controller_name = value
                    self.controller_name.value_namespace = name_space
                    self.controller_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.controller:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.controller:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "controllers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "controller"):
                for c in self.controller:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Rsvp.Controllers.Controller()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.controller.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "controller"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class GlobalLogging(Entity):
        """
        Global Logging
        
        .. attribute:: log_issu_status
        
        	Enable ISSU Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_nsr_status
        
        	Enable NSR Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.GlobalLogging, self).__init__()

            self.yang_name = "global-logging"
            self.yang_parent_name = "rsvp"

            self.log_issu_status = YLeaf(YType.empty, "log-issu-status")

            self.log_nsr_status = YLeaf(YType.empty, "log-nsr-status")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("log_issu_status",
                            "log_nsr_status") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rsvp.GlobalLogging, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.GlobalLogging, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.log_issu_status.is_set or
                self.log_nsr_status.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.log_issu_status.yfilter != YFilter.not_set or
                self.log_nsr_status.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global-logging" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.log_issu_status.is_set or self.log_issu_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log_issu_status.get_name_leafdata())
            if (self.log_nsr_status.is_set or self.log_nsr_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log_nsr_status.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "log-issu-status" or name == "log-nsr-status"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "log-issu-status"):
                self.log_issu_status = value
                self.log_issu_status.value_namespace = name_space
                self.log_issu_status.value_namespace_prefix = name_space_prefix
            if(value_path == "log-nsr-status"):
                self.log_nsr_status = value
                self.log_nsr_status.value_namespace = name_space
                self.log_nsr_status.value_namespace_prefix = name_space_prefix


    class GlobalBandwidth(Entity):
        """
        Configure Global Bandwidth Parameters
        
        .. attribute:: default_interface_percent
        
        	Configure Global RSVP signalling parameters
        	**type**\:   :py:class:`DefaultInterfacePercent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.GlobalBandwidth, self).__init__()

            self.yang_name = "global-bandwidth"
            self.yang_parent_name = "rsvp"

            self.default_interface_percent = Rsvp.GlobalBandwidth.DefaultInterfacePercent()
            self.default_interface_percent.parent = self
            self._children_name_map["default_interface_percent"] = "default-interface-percent"
            self._children_yang_names.add("default-interface-percent")


        class DefaultInterfacePercent(Entity):
            """
            Configure Global RSVP signalling parameters
            
            .. attribute:: mam
            
            	Configure global default MAM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam>`
            
            .. attribute:: rdm
            
            	Configure global default RDM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.GlobalBandwidth.DefaultInterfacePercent, self).__init__()

                self.yang_name = "default-interface-percent"
                self.yang_parent_name = "global-bandwidth"

                self.mam = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam()
                self.mam.parent = self
                self._children_name_map["mam"] = "mam"
                self._children_yang_names.add("mam")

                self.rdm = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm()
                self.rdm.parent = self
                self._children_name_map["rdm"] = "rdm"
                self._children_yang_names.add("rdm")


            class Mam(Entity):
                """
                Configure global default MAM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: max_res_percent
                
                	Default maximum reservable I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam, self).__init__()

                    self.yang_name = "mam"
                    self.yang_parent_name = "default-interface-percent"

                    self.bc0_percent = YLeaf(YType.uint32, "bc0-percent")

                    self.bc1_percent = YLeaf(YType.uint32, "bc1-percent")

                    self.max_res_percent = YLeaf(YType.uint32, "max-res-percent")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bc0_percent",
                                    "bc1_percent",
                                    "max_res_percent") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bc0_percent.is_set or
                        self.bc1_percent.is_set or
                        self.max_res_percent.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bc0_percent.yfilter != YFilter.not_set or
                        self.bc1_percent.yfilter != YFilter.not_set or
                        self.max_res_percent.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mam" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/default-interface-percent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bc0_percent.is_set or self.bc0_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bc0_percent.get_name_leafdata())
                    if (self.bc1_percent.is_set or self.bc1_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bc1_percent.get_name_leafdata())
                    if (self.max_res_percent.is_set or self.max_res_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_res_percent.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bc0-percent" or name == "bc1-percent" or name == "max-res-percent"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bc0-percent"):
                        self.bc0_percent = value
                        self.bc0_percent.value_namespace = name_space
                        self.bc0_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "bc1-percent"):
                        self.bc1_percent = value
                        self.bc1_percent.value_namespace = name_space
                        self.bc1_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-res-percent"):
                        self.max_res_percent = value
                        self.max_res_percent.value_namespace = name_space
                        self.max_res_percent.value_namespace_prefix = name_space_prefix


            class Rdm(Entity):
                """
                Configure global default RDM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm, self).__init__()

                    self.yang_name = "rdm"
                    self.yang_parent_name = "default-interface-percent"

                    self.bc0_percent = YLeaf(YType.uint32, "bc0-percent")

                    self.bc1_percent = YLeaf(YType.uint32, "bc1-percent")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("bc0_percent",
                                    "bc1_percent") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.bc0_percent.is_set or
                        self.bc1_percent.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.bc0_percent.yfilter != YFilter.not_set or
                        self.bc1_percent.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rdm" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/default-interface-percent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.bc0_percent.is_set or self.bc0_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bc0_percent.get_name_leafdata())
                    if (self.bc1_percent.is_set or self.bc1_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bc1_percent.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bc0-percent" or name == "bc1-percent"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "bc0-percent"):
                        self.bc0_percent = value
                        self.bc0_percent.value_namespace = name_space
                        self.bc0_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "bc1-percent"):
                        self.bc1_percent = value
                        self.bc1_percent.value_namespace = name_space
                        self.bc1_percent.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.mam is not None and self.mam.has_data()) or
                    (self.rdm is not None and self.rdm.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.mam is not None and self.mam.has_operation()) or
                    (self.rdm is not None and self.rdm.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default-interface-percent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/global-bandwidth/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "mam"):
                    if (self.mam is None):
                        self.mam = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam()
                        self.mam.parent = self
                        self._children_name_map["mam"] = "mam"
                    return self.mam

                if (child_yang_name == "rdm"):
                    if (self.rdm is None):
                        self.rdm = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm()
                        self.rdm.parent = self
                        self._children_name_map["rdm"] = "rdm"
                    return self.rdm

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mam" or name == "rdm"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.default_interface_percent is not None and self.default_interface_percent.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.default_interface_percent is not None and self.default_interface_percent.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global-bandwidth" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default-interface-percent"):
                if (self.default_interface_percent is None):
                    self.default_interface_percent = Rsvp.GlobalBandwidth.DefaultInterfacePercent()
                    self.default_interface_percent.parent = self
                    self._children_name_map["default_interface_percent"] = "default-interface-percent"
                return self.default_interface_percent

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default-interface-percent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Interfaces(Entity):
        """
        Interface table
        
        .. attribute:: interface
        
        	Interface configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "rsvp"

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
                        super(Rsvp.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            Interface configuration
            
            .. attribute:: name  <key>
            
            	Name of interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Authentication>`
            
            .. attribute:: bandwidth
            
            	Configure Bandwidth
            	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: if_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`IfSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.name = YLeaf(YType.str, "name")

                self.enable = YLeaf(YType.empty, "enable")

                self.authentication = Rsvp.Interfaces.Interface.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
                self._children_yang_names.add("authentication")

                self.bandwidth = Rsvp.Interfaces.Interface.Bandwidth()
                self.bandwidth.parent = self
                self._children_name_map["bandwidth"] = "bandwidth"
                self._children_yang_names.add("bandwidth")

                self.if_signalling = Rsvp.Interfaces.Interface.IfSignalling()
                self.if_signalling.parent = self
                self._children_name_map["if_signalling"] = "if-signalling"
                self._children_yang_names.add("if-signalling")

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
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Interfaces.Interface, self).__setattr__(name, value)


            class IfSignalling(Entity):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: dscp
                
                	Differentiated Services Code Point (DSCP)
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: hello_graceful_restart_if_based
                
                	Enable IF\-based Hello adjacency on a RSVP interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interval_rate
                
                	Configure number of messages to be sent per interval
                	**type**\:   :py:class:`IntervalRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.IntervalRate>`
                
                .. attribute:: missed_messages
                
                	Configure max number of consecutive missed messages for state expiry
                	**type**\:  int
                
                	**range:** 1..8
                
                	**default value**\: 4
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.OutOfBand>`
                
                .. attribute:: pacing
                
                	Enable rate\-limiting on the interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: refresh_interval
                
                	Configure interval between successive refreshes
                	**type**\:  int
                
                	**range:** 10..180
                
                	**units**\: second
                
                	**default value**\: 45
                
                .. attribute:: refresh_reduction
                
                	Configure RSVP Refresh Reduction parameters
                	**type**\:   :py:class:`RefreshReduction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.IfSignalling, self).__init__()

                    self.yang_name = "if-signalling"
                    self.yang_parent_name = "interface"

                    self.dscp = YLeaf(YType.uint32, "dscp")

                    self.hello_graceful_restart_if_based = YLeaf(YType.empty, "hello-graceful-restart-if-based")

                    self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                    self.pacing = YLeaf(YType.empty, "pacing")

                    self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")

                    self.interval_rate = Rsvp.Interfaces.Interface.IfSignalling.IntervalRate()
                    self.interval_rate.parent = self
                    self._children_name_map["interval_rate"] = "interval-rate"
                    self._children_yang_names.add("interval-rate")

                    self.out_of_band = Rsvp.Interfaces.Interface.IfSignalling.OutOfBand()
                    self.out_of_band.parent = self
                    self._children_name_map["out_of_band"] = "out-of-band"
                    self._children_yang_names.add("out-of-band")

                    self.refresh_reduction = Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction()
                    self.refresh_reduction.parent = self
                    self._children_name_map["refresh_reduction"] = "refresh-reduction"
                    self._children_yang_names.add("refresh-reduction")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dscp",
                                    "hello_graceful_restart_if_based",
                                    "missed_messages",
                                    "pacing",
                                    "refresh_interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.Interfaces.Interface.IfSignalling, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.Interfaces.Interface.IfSignalling, self).__setattr__(name, value)


                class RefreshReduction(Entity):
                    """
                    Configure RSVP Refresh Reduction parameters
                    
                    .. attribute:: bundle_message_max_size
                    
                    	Configure maximum size of a single RSVP Bundle message
                    	**type**\:  int
                    
                    	**range:** 512..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: disable
                    
                    	Disable refresh reduction
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reliable_ack_hold_time
                    
                    	Configure hold time for sending RSVP ACK message(s)
                    	**type**\:  int
                    
                    	**range:** 100..5000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 400
                    
                    .. attribute:: reliable_ack_max_size
                    
                    	Configure max size of a single RSVP ACK message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: reliable_retransmit_time
                    
                    	Configure min delay to wait for an ACK before a retransmit
                    	**type**\:  int
                    
                    	**range:** 100..10000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 2100
                    
                    .. attribute:: reliable_s_refresh
                    
                    	Configure use of reliable messaging for summary refresh
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: summary_max_size
                    
                    	Configure max size of a single RSVP summary refresh message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction, self).__init__()

                        self.yang_name = "refresh-reduction"
                        self.yang_parent_name = "if-signalling"

                        self.bundle_message_max_size = YLeaf(YType.uint32, "bundle-message-max-size")

                        self.disable = YLeaf(YType.empty, "disable")

                        self.reliable_ack_hold_time = YLeaf(YType.uint32, "reliable-ack-hold-time")

                        self.reliable_ack_max_size = YLeaf(YType.uint32, "reliable-ack-max-size")

                        self.reliable_retransmit_time = YLeaf(YType.uint32, "reliable-retransmit-time")

                        self.reliable_s_refresh = YLeaf(YType.empty, "reliable-s-refresh")

                        self.summary_max_size = YLeaf(YType.uint32, "summary-max-size")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bundle_message_max_size",
                                        "disable",
                                        "reliable_ack_hold_time",
                                        "reliable_ack_max_size",
                                        "reliable_retransmit_time",
                                        "reliable_s_refresh",
                                        "summary_max_size") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bundle_message_max_size.is_set or
                            self.disable.is_set or
                            self.reliable_ack_hold_time.is_set or
                            self.reliable_ack_max_size.is_set or
                            self.reliable_retransmit_time.is_set or
                            self.reliable_s_refresh.is_set or
                            self.summary_max_size.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bundle_message_max_size.yfilter != YFilter.not_set or
                            self.disable.yfilter != YFilter.not_set or
                            self.reliable_ack_hold_time.yfilter != YFilter.not_set or
                            self.reliable_ack_max_size.yfilter != YFilter.not_set or
                            self.reliable_retransmit_time.yfilter != YFilter.not_set or
                            self.reliable_s_refresh.yfilter != YFilter.not_set or
                            self.summary_max_size.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "refresh-reduction" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bundle_message_max_size.is_set or self.bundle_message_max_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bundle_message_max_size.get_name_leafdata())
                        if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disable.get_name_leafdata())
                        if (self.reliable_ack_hold_time.is_set or self.reliable_ack_hold_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliable_ack_hold_time.get_name_leafdata())
                        if (self.reliable_ack_max_size.is_set or self.reliable_ack_max_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliable_ack_max_size.get_name_leafdata())
                        if (self.reliable_retransmit_time.is_set or self.reliable_retransmit_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliable_retransmit_time.get_name_leafdata())
                        if (self.reliable_s_refresh.is_set or self.reliable_s_refresh.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.reliable_s_refresh.get_name_leafdata())
                        if (self.summary_max_size.is_set or self.summary_max_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.summary_max_size.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bundle-message-max-size" or name == "disable" or name == "reliable-ack-hold-time" or name == "reliable-ack-max-size" or name == "reliable-retransmit-time" or name == "reliable-s-refresh" or name == "summary-max-size"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bundle-message-max-size"):
                            self.bundle_message_max_size = value
                            self.bundle_message_max_size.value_namespace = name_space
                            self.bundle_message_max_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "disable"):
                            self.disable = value
                            self.disable.value_namespace = name_space
                            self.disable.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliable-ack-hold-time"):
                            self.reliable_ack_hold_time = value
                            self.reliable_ack_hold_time.value_namespace = name_space
                            self.reliable_ack_hold_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliable-ack-max-size"):
                            self.reliable_ack_max_size = value
                            self.reliable_ack_max_size.value_namespace = name_space
                            self.reliable_ack_max_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliable-retransmit-time"):
                            self.reliable_retransmit_time = value
                            self.reliable_retransmit_time.value_namespace = name_space
                            self.reliable_retransmit_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "reliable-s-refresh"):
                            self.reliable_s_refresh = value
                            self.reliable_s_refresh.value_namespace = name_space
                            self.reliable_s_refresh.value_namespace_prefix = name_space_prefix
                        if(value_path == "summary-max-size"):
                            self.summary_max_size = value
                            self.summary_max_size.value_namespace = name_space
                            self.summary_max_size.value_namespace_prefix = name_space_prefix


                class IntervalRate(Entity):
                    """
                    Configure number of messages to be sent per
                    interval
                    
                    .. attribute:: interval_size
                    
                    	Size of an interval (milliseconds)
                    	**type**\:  int
                    
                    	**range:** 250..2000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 1000
                    
                    .. attribute:: messages_per_interval
                    
                    	Number of messages to be sent per interval
                    	**type**\:  int
                    
                    	**range:** 1..500
                    
                    	**default value**\: 100
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.IntervalRate, self).__init__()

                        self.yang_name = "interval-rate"
                        self.yang_parent_name = "if-signalling"

                        self.interval_size = YLeaf(YType.uint32, "interval-size")

                        self.messages_per_interval = YLeaf(YType.uint32, "messages-per-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interval_size",
                                        "messages_per_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Interfaces.Interface.IfSignalling.IntervalRate, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Interfaces.Interface.IfSignalling.IntervalRate, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interval_size.is_set or
                            self.messages_per_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interval_size.yfilter != YFilter.not_set or
                            self.messages_per_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interval-rate" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interval_size.is_set or self.interval_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval_size.get_name_leafdata())
                        if (self.messages_per_interval.is_set or self.messages_per_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.messages_per_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interval-size" or name == "messages-per-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interval-size"):
                            self.interval_size = value
                            self.interval_size.value_namespace = name_space
                            self.interval_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "messages-per-interval"):
                            self.messages_per_interval = value
                            self.messages_per_interval.value_namespace = name_space
                            self.messages_per_interval.value_namespace_prefix = name_space_prefix


                class OutOfBand(Entity):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.IfSignalling.OutOfBand, self).__init__()

                        self.yang_name = "out-of-band"
                        self.yang_parent_name = "if-signalling"

                        self.missed_messages = YLeaf(YType.uint32, "missed-messages")

                        self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("missed_messages",
                                        "refresh_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Interfaces.Interface.IfSignalling.OutOfBand, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Interfaces.Interface.IfSignalling.OutOfBand, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.missed_messages.is_set or
                            self.refresh_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.missed_messages.yfilter != YFilter.not_set or
                            self.refresh_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "out-of-band" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.missed_messages.is_set or self.missed_messages.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.missed_messages.get_name_leafdata())
                        if (self.refresh_interval.is_set or self.refresh_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.refresh_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "missed-messages" or name == "refresh-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "missed-messages"):
                            self.missed_messages = value
                            self.missed_messages.value_namespace = name_space
                            self.missed_messages.value_namespace_prefix = name_space_prefix
                        if(value_path == "refresh-interval"):
                            self.refresh_interval = value
                            self.refresh_interval.value_namespace = name_space
                            self.refresh_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.dscp.is_set or
                        self.hello_graceful_restart_if_based.is_set or
                        self.missed_messages.is_set or
                        self.pacing.is_set or
                        self.refresh_interval.is_set or
                        (self.interval_rate is not None and self.interval_rate.has_data()) or
                        (self.out_of_band is not None and self.out_of_band.has_data()) or
                        (self.refresh_reduction is not None and self.refresh_reduction.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.hello_graceful_restart_if_based.yfilter != YFilter.not_set or
                        self.missed_messages.yfilter != YFilter.not_set or
                        self.pacing.yfilter != YFilter.not_set or
                        self.refresh_interval.yfilter != YFilter.not_set or
                        (self.interval_rate is not None and self.interval_rate.has_operation()) or
                        (self.out_of_band is not None and self.out_of_band.has_operation()) or
                        (self.refresh_reduction is not None and self.refresh_reduction.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "if-signalling" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dscp.get_name_leafdata())
                    if (self.hello_graceful_restart_if_based.is_set or self.hello_graceful_restart_if_based.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hello_graceful_restart_if_based.get_name_leafdata())
                    if (self.missed_messages.is_set or self.missed_messages.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.missed_messages.get_name_leafdata())
                    if (self.pacing.is_set or self.pacing.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pacing.get_name_leafdata())
                    if (self.refresh_interval.is_set or self.refresh_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.refresh_interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interval-rate"):
                        if (self.interval_rate is None):
                            self.interval_rate = Rsvp.Interfaces.Interface.IfSignalling.IntervalRate()
                            self.interval_rate.parent = self
                            self._children_name_map["interval_rate"] = "interval-rate"
                        return self.interval_rate

                    if (child_yang_name == "out-of-band"):
                        if (self.out_of_band is None):
                            self.out_of_band = Rsvp.Interfaces.Interface.IfSignalling.OutOfBand()
                            self.out_of_band.parent = self
                            self._children_name_map["out_of_band"] = "out-of-band"
                        return self.out_of_band

                    if (child_yang_name == "refresh-reduction"):
                        if (self.refresh_reduction is None):
                            self.refresh_reduction = Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction()
                            self.refresh_reduction.parent = self
                            self._children_name_map["refresh_reduction"] = "refresh-reduction"
                        return self.refresh_reduction

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interval-rate" or name == "out-of-band" or name == "refresh-reduction" or name == "dscp" or name == "hello-graceful-restart-if-based" or name == "missed-messages" or name == "pacing" or name == "refresh-interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dscp"):
                        self.dscp = value
                        self.dscp.value_namespace = name_space
                        self.dscp.value_namespace_prefix = name_space_prefix
                    if(value_path == "hello-graceful-restart-if-based"):
                        self.hello_graceful_restart_if_based = value
                        self.hello_graceful_restart_if_based.value_namespace = name_space
                        self.hello_graceful_restart_if_based.value_namespace_prefix = name_space_prefix
                    if(value_path == "missed-messages"):
                        self.missed_messages = value
                        self.missed_messages.value_namespace = name_space
                        self.missed_messages.value_namespace_prefix = name_space_prefix
                    if(value_path == "pacing"):
                        self.pacing = value
                        self.pacing.value_namespace = name_space
                        self.pacing.value_namespace_prefix = name_space_prefix
                    if(value_path == "refresh-interval"):
                        self.refresh_interval = value
                        self.refresh_interval.value_namespace = name_space
                        self.refresh_interval.value_namespace_prefix = name_space_prefix


            class Bandwidth(Entity):
                """
                Configure Bandwidth
                
                .. attribute:: mam
                
                	Configure MAM bandwidth parameters
                	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Mam>`
                
                .. attribute:: rdm
                
                	Configure RDM bandwidth parameters
                	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Rdm>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.Bandwidth, self).__init__()

                    self.yang_name = "bandwidth"
                    self.yang_parent_name = "interface"

                    self.mam = Rsvp.Interfaces.Interface.Bandwidth.Mam()
                    self.mam.parent = self
                    self._children_name_map["mam"] = "mam"
                    self._children_yang_names.add("mam")

                    self.rdm = Rsvp.Interfaces.Interface.Bandwidth.Rdm()
                    self.rdm.parent = self
                    self._children_name_map["rdm"] = "rdm"
                    self._children_yang_names.add("rdm")


                class Mam(Entity):
                    """
                    Configure MAM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfg>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_bandwidth
                    
                    	Maximum reservable bandwidth (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.Bandwidth.Mam, self).__init__()

                        self.yang_name = "mam"
                        self.yang_parent_name = "bandwidth"

                        self.bandwidth_mode = YLeaf(YType.enumeration, "bandwidth-mode")

                        self.bc0_bandwidth = YLeaf(YType.uint32, "bc0-bandwidth")

                        self.bc1_bandwidth = YLeaf(YType.uint32, "bc1-bandwidth")

                        self.max_resv_bandwidth = YLeaf(YType.uint32, "max-resv-bandwidth")

                        self.max_resv_flow = YLeaf(YType.uint32, "max-resv-flow")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bandwidth_mode",
                                        "bc0_bandwidth",
                                        "bc1_bandwidth",
                                        "max_resv_bandwidth",
                                        "max_resv_flow") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Interfaces.Interface.Bandwidth.Mam, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Interfaces.Interface.Bandwidth.Mam, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bandwidth_mode.is_set or
                            self.bc0_bandwidth.is_set or
                            self.bc1_bandwidth.is_set or
                            self.max_resv_bandwidth.is_set or
                            self.max_resv_flow.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bandwidth_mode.yfilter != YFilter.not_set or
                            self.bc0_bandwidth.yfilter != YFilter.not_set or
                            self.bc1_bandwidth.yfilter != YFilter.not_set or
                            self.max_resv_bandwidth.yfilter != YFilter.not_set or
                            self.max_resv_flow.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mam" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bandwidth_mode.is_set or self.bandwidth_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bandwidth_mode.get_name_leafdata())
                        if (self.bc0_bandwidth.is_set or self.bc0_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc0_bandwidth.get_name_leafdata())
                        if (self.bc1_bandwidth.is_set or self.bc1_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc1_bandwidth.get_name_leafdata())
                        if (self.max_resv_bandwidth.is_set or self.max_resv_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_resv_bandwidth.get_name_leafdata())
                        if (self.max_resv_flow.is_set or self.max_resv_flow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_resv_flow.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bandwidth-mode" or name == "bc0-bandwidth" or name == "bc1-bandwidth" or name == "max-resv-bandwidth" or name == "max-resv-flow"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bandwidth-mode"):
                            self.bandwidth_mode = value
                            self.bandwidth_mode.value_namespace = name_space
                            self.bandwidth_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc0-bandwidth"):
                            self.bc0_bandwidth = value
                            self.bc0_bandwidth.value_namespace = name_space
                            self.bc0_bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc1-bandwidth"):
                            self.bc1_bandwidth = value
                            self.bc1_bandwidth.value_namespace = name_space
                            self.bc1_bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-resv-bandwidth"):
                            self.max_resv_bandwidth = value
                            self.max_resv_bandwidth.value_namespace = name_space
                            self.max_resv_bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-resv-flow"):
                            self.max_resv_flow = value
                            self.max_resv_flow.value_namespace = name_space
                            self.max_resv_flow.value_namespace_prefix = name_space_prefix


                class Rdm(Entity):
                    """
                    Configure RDM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfg>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc0_keyword
                    
                    	Set requests should always use BC0
                    	**type**\:   :py:class:`RsvpBc0 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc0>`
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_keyword
                    
                    	Set requests should always use BC1
                    	**type**\:   :py:class:`RsvpBc1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc1>`
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rdm_keyword
                    
                    	Set requests should always use RDM
                    	**type**\:   :py:class:`RsvpRdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpRdm>`
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Rsvp.Interfaces.Interface.Bandwidth.Rdm, self).__init__()

                        self.yang_name = "rdm"
                        self.yang_parent_name = "bandwidth"

                        self.bandwidth_mode = YLeaf(YType.enumeration, "bandwidth-mode")

                        self.bc0_bandwidth = YLeaf(YType.uint32, "bc0-bandwidth")

                        self.bc0_keyword = YLeaf(YType.enumeration, "bc0-keyword")

                        self.bc1_bandwidth = YLeaf(YType.uint32, "bc1-bandwidth")

                        self.bc1_keyword = YLeaf(YType.enumeration, "bc1-keyword")

                        self.max_resv_flow = YLeaf(YType.uint32, "max-resv-flow")

                        self.rdm_keyword = YLeaf(YType.enumeration, "rdm-keyword")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bandwidth_mode",
                                        "bc0_bandwidth",
                                        "bc0_keyword",
                                        "bc1_bandwidth",
                                        "bc1_keyword",
                                        "max_resv_flow",
                                        "rdm_keyword") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Rsvp.Interfaces.Interface.Bandwidth.Rdm, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Rsvp.Interfaces.Interface.Bandwidth.Rdm, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bandwidth_mode.is_set or
                            self.bc0_bandwidth.is_set or
                            self.bc0_keyword.is_set or
                            self.bc1_bandwidth.is_set or
                            self.bc1_keyword.is_set or
                            self.max_resv_flow.is_set or
                            self.rdm_keyword.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bandwidth_mode.yfilter != YFilter.not_set or
                            self.bc0_bandwidth.yfilter != YFilter.not_set or
                            self.bc0_keyword.yfilter != YFilter.not_set or
                            self.bc1_bandwidth.yfilter != YFilter.not_set or
                            self.bc1_keyword.yfilter != YFilter.not_set or
                            self.max_resv_flow.yfilter != YFilter.not_set or
                            self.rdm_keyword.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rdm" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bandwidth_mode.is_set or self.bandwidth_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bandwidth_mode.get_name_leafdata())
                        if (self.bc0_bandwidth.is_set or self.bc0_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc0_bandwidth.get_name_leafdata())
                        if (self.bc0_keyword.is_set or self.bc0_keyword.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc0_keyword.get_name_leafdata())
                        if (self.bc1_bandwidth.is_set or self.bc1_bandwidth.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc1_bandwidth.get_name_leafdata())
                        if (self.bc1_keyword.is_set or self.bc1_keyword.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bc1_keyword.get_name_leafdata())
                        if (self.max_resv_flow.is_set or self.max_resv_flow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_resv_flow.get_name_leafdata())
                        if (self.rdm_keyword.is_set or self.rdm_keyword.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rdm_keyword.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bandwidth-mode" or name == "bc0-bandwidth" or name == "bc0-keyword" or name == "bc1-bandwidth" or name == "bc1-keyword" or name == "max-resv-flow" or name == "rdm-keyword"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bandwidth-mode"):
                            self.bandwidth_mode = value
                            self.bandwidth_mode.value_namespace = name_space
                            self.bandwidth_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc0-bandwidth"):
                            self.bc0_bandwidth = value
                            self.bc0_bandwidth.value_namespace = name_space
                            self.bc0_bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc0-keyword"):
                            self.bc0_keyword = value
                            self.bc0_keyword.value_namespace = name_space
                            self.bc0_keyword.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc1-bandwidth"):
                            self.bc1_bandwidth = value
                            self.bc1_bandwidth.value_namespace = name_space
                            self.bc1_bandwidth.value_namespace_prefix = name_space_prefix
                        if(value_path == "bc1-keyword"):
                            self.bc1_keyword = value
                            self.bc1_keyword.value_namespace = name_space
                            self.bc1_keyword.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-resv-flow"):
                            self.max_resv_flow = value
                            self.max_resv_flow.value_namespace = name_space
                            self.max_resv_flow.value_namespace_prefix = name_space_prefix
                        if(value_path == "rdm-keyword"):
                            self.rdm_keyword = value
                            self.rdm_keyword.value_namespace = name_space
                            self.rdm_keyword.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.mam is not None and self.mam.has_data()) or
                        (self.rdm is not None and self.rdm.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.mam is not None and self.mam.has_operation()) or
                        (self.rdm is not None and self.rdm.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bandwidth" + path_buffer

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

                    if (child_yang_name == "mam"):
                        if (self.mam is None):
                            self.mam = Rsvp.Interfaces.Interface.Bandwidth.Mam()
                            self.mam.parent = self
                            self._children_name_map["mam"] = "mam"
                        return self.mam

                    if (child_yang_name == "rdm"):
                        if (self.rdm is None):
                            self.rdm = Rsvp.Interfaces.Interface.Bandwidth.Rdm()
                            self.rdm.parent = self
                            self._children_name_map["rdm"] = "rdm"
                        return self.rdm

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mam" or name == "rdm"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Authentication(Entity):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Interfaces.Interface.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "interface"

                    self.enable = YLeaf(YType.boolean, "enable")

                    self.key_chain = YLeaf(YType.str, "key-chain")

                    self.life_time = YLeaf(YType.uint32, "life-time")

                    self.window_size = YLeaf(YType.uint32, "window-size")

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
                                    "key_chain",
                                    "life_time",
                                    "window_size") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.Interfaces.Interface.Authentication, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.Interfaces.Interface.Authentication, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enable.is_set or
                        self.key_chain.is_set or
                        self.life_time.is_set or
                        self.window_size.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        self.key_chain.yfilter != YFilter.not_set or
                        self.life_time.yfilter != YFilter.not_set or
                        self.window_size.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authentication" + path_buffer

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
                    if (self.key_chain.is_set or self.key_chain.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key_chain.get_name_leafdata())
                    if (self.life_time.is_set or self.life_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.life_time.get_name_leafdata())
                    if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.window_size.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enable" or name == "key-chain" or name == "life-time" or name == "window-size"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix
                    if(value_path == "key-chain"):
                        self.key_chain = value
                        self.key_chain.value_namespace = name_space
                        self.key_chain.value_namespace_prefix = name_space_prefix
                    if(value_path == "life-time"):
                        self.life_time = value
                        self.life_time.value_namespace = name_space
                        self.life_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "window-size"):
                        self.window_size = value
                        self.window_size.value_namespace = name_space
                        self.window_size.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    self.enable.is_set or
                    (self.authentication is not None and self.authentication.has_data()) or
                    (self.bandwidth is not None and self.bandwidth.has_data()) or
                    (self.if_signalling is not None and self.if_signalling.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.authentication is not None and self.authentication.has_operation()) or
                    (self.bandwidth is not None and self.bandwidth.has_operation()) or
                    (self.if_signalling is not None and self.if_signalling.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authentication"):
                    if (self.authentication is None):
                        self.authentication = Rsvp.Interfaces.Interface.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                    return self.authentication

                if (child_yang_name == "bandwidth"):
                    if (self.bandwidth is None):
                        self.bandwidth = Rsvp.Interfaces.Interface.Bandwidth()
                        self.bandwidth.parent = self
                        self._children_name_map["bandwidth"] = "bandwidth"
                    return self.bandwidth

                if (child_yang_name == "if-signalling"):
                    if (self.if_signalling is None):
                        self.if_signalling = Rsvp.Interfaces.Interface.IfSignalling()
                        self.if_signalling.parent = self
                        self._children_name_map["if_signalling"] = "if-signalling"
                    return self.if_signalling

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authentication" or name == "bandwidth" or name == "if-signalling" or name == "name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
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
                c = Rsvp.Interfaces.Interface()
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


    class Signalling(Entity):
        """
        Configure Global RSVP signalling parameters
        
        .. attribute:: checksum
        
        	RSVP message checksum computation
        	**type**\:   :py:class:`Checksum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Checksum>`
        
        .. attribute:: global_out_of_band
        
        	Configure out\-of\-band signalling parameters
        	**type**\:   :py:class:`GlobalOutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GlobalOutOfBand>`
        
        .. attribute:: graceful_restart
        
        	Configure RSVP Graceful\-Restart parameters
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GracefulRestart>`
        
        .. attribute:: hello_graceful_restart_interval
        
        	Configure interval between successive Hello messages
        	**type**\:  int
        
        	**range:** 3000..30000
        
        	**units**\: millisecond
        
        	**default value**\: 5000
        
        .. attribute:: hello_graceful_restart_misses
        
        	Configure max number of consecutive missed Hello messages
        	**type**\:  int
        
        	**range:** 1..10
        
        	**default value**\: 3
        
        .. attribute:: pesr
        
        	Sending Path Error with State\-Removal flag
        	**type**\:   :py:class:`Pesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Pesr>`
        
        .. attribute:: prefix_filtering
        
        	Configure prefix filtering parameters
        	**type**\:   :py:class:`PrefixFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.Signalling, self).__init__()

            self.yang_name = "signalling"
            self.yang_parent_name = "rsvp"

            self.hello_graceful_restart_interval = YLeaf(YType.uint32, "hello-graceful-restart-interval")

            self.hello_graceful_restart_misses = YLeaf(YType.uint32, "hello-graceful-restart-misses")

            self.checksum = Rsvp.Signalling.Checksum()
            self.checksum.parent = self
            self._children_name_map["checksum"] = "checksum"
            self._children_yang_names.add("checksum")

            self.global_out_of_band = Rsvp.Signalling.GlobalOutOfBand()
            self.global_out_of_band.parent = self
            self._children_name_map["global_out_of_band"] = "global-out-of-band"
            self._children_yang_names.add("global-out-of-band")

            self.graceful_restart = Rsvp.Signalling.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.pesr = Rsvp.Signalling.Pesr()
            self.pesr.parent = self
            self._children_name_map["pesr"] = "pesr"
            self._children_yang_names.add("pesr")

            self.prefix_filtering = Rsvp.Signalling.PrefixFiltering()
            self.prefix_filtering.parent = self
            self._children_name_map["prefix_filtering"] = "prefix-filtering"
            self._children_yang_names.add("prefix-filtering")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("hello_graceful_restart_interval",
                            "hello_graceful_restart_misses") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rsvp.Signalling, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.Signalling, self).__setattr__(name, value)


        class GlobalOutOfBand(Entity):
            """
            Configure out\-of\-band signalling parameters
            
            .. attribute:: vrf
            
            	VRF used for out\-of\-band control signalling
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Signalling.GlobalOutOfBand, self).__init__()

                self.yang_name = "global-out-of-band"
                self.yang_parent_name = "signalling"

                self.vrf = YLeaf(YType.str, "vrf")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Signalling.GlobalOutOfBand, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Signalling.GlobalOutOfBand, self).__setattr__(name, value)

            def has_data(self):
                return self.vrf.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "global-out-of-band" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix


        class GracefulRestart(Entity):
            """
            Configure RSVP Graceful\-Restart parameters
            
            .. attribute:: enable
            
            	Enable RSVP graceful restart
            	**type**\:  bool
            
            .. attribute:: lsp_class_type
            
            	Send LSP's ctype for recovery and suggested label
            	**type**\:   :py:class:`LspClassType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GracefulRestart.LspClassType>`
            
            .. attribute:: recovery_time
            
            	Graceful restart recovery time (seconds)
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            .. attribute:: restart_time
            
            	Graceful restart time (seconds)
            	**type**\:  int
            
            	**range:** 60..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Signalling.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "signalling"

                self.enable = YLeaf(YType.boolean, "enable")

                self.recovery_time = YLeaf(YType.uint32, "recovery-time")

                self.restart_time = YLeaf(YType.uint32, "restart-time")

                self.lsp_class_type = Rsvp.Signalling.GracefulRestart.LspClassType()
                self.lsp_class_type.parent = self
                self._children_name_map["lsp_class_type"] = "lsp-class-type"
                self._children_yang_names.add("lsp-class-type")

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
                                "recovery_time",
                                "restart_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Signalling.GracefulRestart, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Signalling.GracefulRestart, self).__setattr__(name, value)


            class LspClassType(Entity):
                """
                Send LSP's ctype for recovery and suggested
                label
                
                .. attribute:: enable
                
                	Send LSP's ctype for recovery and suggested label
                	**type**\:  bool
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Signalling.GracefulRestart.LspClassType, self).__init__()

                    self.yang_name = "lsp-class-type"
                    self.yang_parent_name = "graceful-restart"

                    self.enable = YLeaf(YType.boolean, "enable")

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
                                super(Rsvp.Signalling.GracefulRestart.LspClassType, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.Signalling.GracefulRestart.LspClassType, self).__setattr__(name, value)

                def has_data(self):
                    return self.enable.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lsp-class-type" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/graceful-restart/%s" % self.get_segment_path()
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

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enable.is_set or
                    self.recovery_time.is_set or
                    self.restart_time.is_set or
                    (self.lsp_class_type is not None and self.lsp_class_type.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.recovery_time.yfilter != YFilter.not_set or
                    self.restart_time.yfilter != YFilter.not_set or
                    (self.lsp_class_type is not None and self.lsp_class_type.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "graceful-restart" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.recovery_time.is_set or self.recovery_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.recovery_time.get_name_leafdata())
                if (self.restart_time.is_set or self.restart_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.restart_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "lsp-class-type"):
                    if (self.lsp_class_type is None):
                        self.lsp_class_type = Rsvp.Signalling.GracefulRestart.LspClassType()
                        self.lsp_class_type.parent = self
                        self._children_name_map["lsp_class_type"] = "lsp-class-type"
                    return self.lsp_class_type

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lsp-class-type" or name == "enable" or name == "recovery-time" or name == "restart-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "recovery-time"):
                    self.recovery_time = value
                    self.recovery_time.value_namespace = name_space
                    self.recovery_time.value_namespace_prefix = name_space_prefix
                if(value_path == "restart-time"):
                    self.restart_time = value
                    self.restart_time.value_namespace = name_space
                    self.restart_time.value_namespace_prefix = name_space_prefix


        class PrefixFiltering(Entity):
            """
            Configure prefix filtering parameters
            
            .. attribute:: acl
            
            	Configure an ACL to perform prefix filtering of RSVP Router Alert messages
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: default_deny_action
            
            	Configure RSVP behaviour for scenarios where ACL match yields a default (implicit) deny
            	**type**\:   :py:class:`DefaultDenyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering.DefaultDenyAction>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Signalling.PrefixFiltering, self).__init__()

                self.yang_name = "prefix-filtering"
                self.yang_parent_name = "signalling"

                self.acl = YLeaf(YType.str, "acl")

                self.default_deny_action = Rsvp.Signalling.PrefixFiltering.DefaultDenyAction()
                self.default_deny_action.parent = self
                self._children_name_map["default_deny_action"] = "default-deny-action"
                self._children_yang_names.add("default-deny-action")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("acl") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Signalling.PrefixFiltering, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Signalling.PrefixFiltering, self).__setattr__(name, value)


            class DefaultDenyAction(Entity):
                """
                Configure RSVP behaviour for scenarios where
                ACL match yields a default (implicit) deny
                
                .. attribute:: drop
                
                	Configure RSVP to drop packets when ACL match yields a default (implicit) deny
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Rsvp.Signalling.PrefixFiltering.DefaultDenyAction, self).__init__()

                    self.yang_name = "default-deny-action"
                    self.yang_parent_name = "prefix-filtering"

                    self.drop = YLeaf(YType.empty, "drop")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("drop") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Rsvp.Signalling.PrefixFiltering.DefaultDenyAction, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Rsvp.Signalling.PrefixFiltering.DefaultDenyAction, self).__setattr__(name, value)

                def has_data(self):
                    return self.drop.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.drop.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "default-deny-action" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/prefix-filtering/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.drop.is_set or self.drop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.drop.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "drop"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "drop"):
                        self.drop = value
                        self.drop.value_namespace = name_space
                        self.drop.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.acl.is_set or
                    (self.default_deny_action is not None and self.default_deny_action.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.acl.yfilter != YFilter.not_set or
                    (self.default_deny_action is not None and self.default_deny_action.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prefix-filtering" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.acl.is_set or self.acl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acl.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "default-deny-action"):
                    if (self.default_deny_action is None):
                        self.default_deny_action = Rsvp.Signalling.PrefixFiltering.DefaultDenyAction()
                        self.default_deny_action.parent = self
                        self._children_name_map["default_deny_action"] = "default-deny-action"
                    return self.default_deny_action

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "default-deny-action" or name == "acl"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "acl"):
                    self.acl = value
                    self.acl.value_namespace = name_space
                    self.acl.value_namespace_prefix = name_space_prefix


        class Pesr(Entity):
            """
            Sending Path Error with State\-Removal flag
            
            .. attribute:: disable
            
            	Disable RSVP PESR
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Signalling.Pesr, self).__init__()

                self.yang_name = "pesr"
                self.yang_parent_name = "signalling"

                self.disable = YLeaf(YType.empty, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Signalling.Pesr, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Signalling.Pesr, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pesr" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix


        class Checksum(Entity):
            """
            RSVP message checksum computation
            
            .. attribute:: disable
            
            	Disable RSVP message checksum computation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Rsvp.Signalling.Checksum, self).__init__()

                self.yang_name = "checksum"
                self.yang_parent_name = "signalling"

                self.disable = YLeaf(YType.empty, "disable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Rsvp.Signalling.Checksum, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Rsvp.Signalling.Checksum, self).__setattr__(name, value)

            def has_data(self):
                return self.disable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "checksum" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/signalling/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "disable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.hello_graceful_restart_interval.is_set or
                self.hello_graceful_restart_misses.is_set or
                (self.checksum is not None and self.checksum.has_data()) or
                (self.global_out_of_band is not None and self.global_out_of_band.has_data()) or
                (self.graceful_restart is not None and self.graceful_restart.has_data()) or
                (self.pesr is not None and self.pesr.has_data()) or
                (self.prefix_filtering is not None and self.prefix_filtering.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.hello_graceful_restart_interval.yfilter != YFilter.not_set or
                self.hello_graceful_restart_misses.yfilter != YFilter.not_set or
                (self.checksum is not None and self.checksum.has_operation()) or
                (self.global_out_of_band is not None and self.global_out_of_band.has_operation()) or
                (self.graceful_restart is not None and self.graceful_restart.has_operation()) or
                (self.pesr is not None and self.pesr.has_operation()) or
                (self.prefix_filtering is not None and self.prefix_filtering.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "signalling" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.hello_graceful_restart_interval.is_set or self.hello_graceful_restart_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hello_graceful_restart_interval.get_name_leafdata())
            if (self.hello_graceful_restart_misses.is_set or self.hello_graceful_restart_misses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hello_graceful_restart_misses.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "checksum"):
                if (self.checksum is None):
                    self.checksum = Rsvp.Signalling.Checksum()
                    self.checksum.parent = self
                    self._children_name_map["checksum"] = "checksum"
                return self.checksum

            if (child_yang_name == "global-out-of-band"):
                if (self.global_out_of_band is None):
                    self.global_out_of_band = Rsvp.Signalling.GlobalOutOfBand()
                    self.global_out_of_band.parent = self
                    self._children_name_map["global_out_of_band"] = "global-out-of-band"
                return self.global_out_of_band

            if (child_yang_name == "graceful-restart"):
                if (self.graceful_restart is None):
                    self.graceful_restart = Rsvp.Signalling.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"
                return self.graceful_restart

            if (child_yang_name == "pesr"):
                if (self.pesr is None):
                    self.pesr = Rsvp.Signalling.Pesr()
                    self.pesr.parent = self
                    self._children_name_map["pesr"] = "pesr"
                return self.pesr

            if (child_yang_name == "prefix-filtering"):
                if (self.prefix_filtering is None):
                    self.prefix_filtering = Rsvp.Signalling.PrefixFiltering()
                    self.prefix_filtering.parent = self
                    self._children_name_map["prefix_filtering"] = "prefix-filtering"
                return self.prefix_filtering

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "checksum" or name == "global-out-of-band" or name == "graceful-restart" or name == "pesr" or name == "prefix-filtering" or name == "hello-graceful-restart-interval" or name == "hello-graceful-restart-misses"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "hello-graceful-restart-interval"):
                self.hello_graceful_restart_interval = value
                self.hello_graceful_restart_interval.value_namespace = name_space
                self.hello_graceful_restart_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "hello-graceful-restart-misses"):
                self.hello_graceful_restart_misses = value
                self.hello_graceful_restart_misses.value_namespace = name_space
                self.hello_graceful_restart_misses.value_namespace_prefix = name_space_prefix


    class Authentication(Entity):
        """
        Configure RSVP authentication
        
        .. attribute:: enable
        
        	Enable or disable RSVP authentication
        	**type**\:  bool
        
        .. attribute:: key_chain
        
        	Key chain to authenticate RSVP signalling messages
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: life_time
        
        	Life time (in seconds) for each security association
        	**type**\:  int
        
        	**range:** 30..86400
        
        	**units**\: second
        
        .. attribute:: window_size
        
        	Window\-size to limit number of out\-of\-order messages
        	**type**\:  int
        
        	**range:** 1..64
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Rsvp.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "rsvp"

            self.enable = YLeaf(YType.boolean, "enable")

            self.key_chain = YLeaf(YType.str, "key-chain")

            self.life_time = YLeaf(YType.uint32, "life-time")

            self.window_size = YLeaf(YType.uint32, "window-size")

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
                            "key_chain",
                            "life_time",
                            "window_size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Rsvp.Authentication, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Rsvp.Authentication, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.enable.is_set or
                self.key_chain.is_set or
                self.life_time.is_set or
                self.window_size.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.key_chain.yfilter != YFilter.not_set or
                self.life_time.yfilter != YFilter.not_set or
                self.window_size.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "authentication" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.key_chain.is_set or self.key_chain.yfilter != YFilter.not_set):
                leaf_name_data.append(self.key_chain.get_name_leafdata())
            if (self.life_time.is_set or self.life_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.life_time.get_name_leafdata())
            if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.window_size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "enable" or name == "key-chain" or name == "life-time" or name == "window-size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "key-chain"):
                self.key_chain = value
                self.key_chain.value_namespace = name_space
                self.key_chain.value_namespace_prefix = name_space_prefix
            if(value_path == "life-time"):
                self.life_time = value
                self.life_time.value_namespace = name_space
                self.life_time.value_namespace_prefix = name_space_prefix
            if(value_path == "window-size"):
                self.window_size = value
                self.window_size.value_namespace = name_space
                self.window_size.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.authentication is not None and self.authentication.has_data()) or
            (self.controllers is not None and self.controllers.has_data()) or
            (self.global_bandwidth is not None and self.global_bandwidth.has_data()) or
            (self.global_logging is not None and self.global_logging.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.neighbors is not None and self.neighbors.has_data()) or
            (self.signalling is not None and self.signalling.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.authentication is not None and self.authentication.has_operation()) or
            (self.controllers is not None and self.controllers.has_operation()) or
            (self.global_bandwidth is not None and self.global_bandwidth.has_operation()) or
            (self.global_logging is not None and self.global_logging.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.neighbors is not None and self.neighbors.has_operation()) or
            (self.signalling is not None and self.signalling.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-rsvp-cfg:rsvp" + path_buffer

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

        if (child_yang_name == "authentication"):
            if (self.authentication is None):
                self.authentication = Rsvp.Authentication()
                self.authentication.parent = self
                self._children_name_map["authentication"] = "authentication"
            return self.authentication

        if (child_yang_name == "controllers"):
            if (self.controllers is None):
                self.controllers = Rsvp.Controllers()
                self.controllers.parent = self
                self._children_name_map["controllers"] = "controllers"
            return self.controllers

        if (child_yang_name == "global-bandwidth"):
            if (self.global_bandwidth is None):
                self.global_bandwidth = Rsvp.GlobalBandwidth()
                self.global_bandwidth.parent = self
                self._children_name_map["global_bandwidth"] = "global-bandwidth"
            return self.global_bandwidth

        if (child_yang_name == "global-logging"):
            if (self.global_logging is None):
                self.global_logging = Rsvp.GlobalLogging()
                self.global_logging.parent = self
                self._children_name_map["global_logging"] = "global-logging"
            return self.global_logging

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Rsvp.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "neighbors"):
            if (self.neighbors is None):
                self.neighbors = Rsvp.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
            return self.neighbors

        if (child_yang_name == "signalling"):
            if (self.signalling is None):
                self.signalling = Rsvp.Signalling()
                self.signalling.parent = self
                self._children_name_map["signalling"] = "signalling"
            return self.signalling

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "authentication" or name == "controllers" or name == "global-bandwidth" or name == "global-logging" or name == "interfaces" or name == "neighbors" or name == "signalling"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Rsvp()
        return self._top_entity

