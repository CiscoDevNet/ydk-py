""" Cisco_IOS_XR_tunnel_l2tun_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package configuration.

This module contains definitions
for the following management objects\:
  l2tp\: L2TPv3 class used for L2VPNs

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class L2TpDigestHashMethod(Enum):
    """
    L2TpDigestHashMethod

    L2tp digest hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    """

    md5 = Enum.YLeaf(1, "md5")

    sha1 = Enum.YLeaf(2, "sha1")


class L2TpHashMethod(Enum):
    """
    L2TpHashMethod

    L2tp hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    .. data:: none = 3

    	None

    """

    md5 = Enum.YLeaf(1, "md5")

    sha1 = Enum.YLeaf(2, "sha1")

    none = Enum.YLeaf(3, "none")



class L2Tp(Entity):
    """
    L2TPv3 class used for L2VPNs
    
    .. attribute:: classes
    
    	List of classes
    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes>`
    
    

    """

    _prefix = 'tunnel-l2tun-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(L2Tp, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tp"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-cfg"

        self.classes = L2Tp.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"
        self._children_yang_names.add("classes")


    class Classes(Entity):
        """
        List of classes
        
        .. attribute:: class_
        
        	Configuration for a specific class
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tp"

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
                        super(L2Tp.Classes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(L2Tp.Classes, self).__setattr__(name, value)


        class Class_(Entity):
            """
            Configuration for a specific class
            
            .. attribute:: class_name  <key>
            
            	Specify the class name. Regexp\: ^[a\-z0\-9A\-Z][\-\_.a\-z0\-9A\-Z]\*$
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: authentication
            
            	Authenticate the L2TP control connection
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: congestion_control
            
            	Congestion control enabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: digest
            
            	Message digest authentication for the L2TP control connection
            	**type**\:   :py:class:`Digest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest>`
            
            .. attribute:: enable
            
            	Enable L2TPv3 class used for L2VPNs
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hello_interval
            
            	Specify interval (in seconds)
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**units**\: second
            
            .. attribute:: hidden
            
            	Specify to hide AVPs in outgoing control messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: host_name
            
            	Local hostname for control connection authentication
            	**type**\:  str
            
            .. attribute:: ip
            
            	IP TOS value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Ip>`
            
            .. attribute:: password
            
            	Specify the password for control channel authentication
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: receive_window
            
            	Receive window size for the control connection
            	**type**\:  int
            
            	**range:** 1..16384
            
            	**units**\: byte
            
            .. attribute:: retransmit
            
            	Control message retransmission parameters
            	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit>`
            
            .. attribute:: security
            
            	Security check
            	**type**\:   :py:class:`Security <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Security>`
            
            .. attribute:: timeout_no_user
            
            	Timeout value for no\-user in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_setup
            
            	Time permitted to set up a control connection
            	**type**\:  int
            
            	**range:** 60..6000
            
            	**units**\: second
            
            .. attribute:: tunnel
            
            	l2TP tunnel
            	**type**\:   :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Tunnel>`
            
            

            """

            _prefix = 'tunnel-l2tun-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Classes.Class_, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"

                self.class_name = YLeaf(YType.str, "class-name")

                self.authentication = YLeaf(YType.int32, "authentication")

                self.congestion_control = YLeaf(YType.empty, "congestion-control")

                self.enable = YLeaf(YType.empty, "enable")

                self.hello_interval = YLeaf(YType.uint32, "hello-interval")

                self.hidden = YLeaf(YType.empty, "hidden")

                self.host_name = YLeaf(YType.str, "host-name")

                self.password = YLeaf(YType.str, "password")

                self.receive_window = YLeaf(YType.uint32, "receive-window")

                self.timeout_no_user = YLeaf(YType.uint32, "timeout-no-user")

                self.timeout_setup = YLeaf(YType.uint32, "timeout-setup")

                self.digest = L2Tp.Classes.Class_.Digest()
                self.digest.parent = self
                self._children_name_map["digest"] = "digest"
                self._children_yang_names.add("digest")

                self.ip = L2Tp.Classes.Class_.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
                self._children_yang_names.add("ip")

                self.retransmit = L2Tp.Classes.Class_.Retransmit()
                self.retransmit.parent = self
                self._children_name_map["retransmit"] = "retransmit"
                self._children_yang_names.add("retransmit")

                self.security = L2Tp.Classes.Class_.Security()
                self.security.parent = self
                self._children_name_map["security"] = "security"
                self._children_yang_names.add("security")

                self.tunnel = L2Tp.Classes.Class_.Tunnel()
                self.tunnel.parent = self
                self._children_name_map["tunnel"] = "tunnel"
                self._children_yang_names.add("tunnel")

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
                                "authentication",
                                "congestion_control",
                                "enable",
                                "hello_interval",
                                "hidden",
                                "host_name",
                                "password",
                                "receive_window",
                                "timeout_no_user",
                                "timeout_setup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(L2Tp.Classes.Class_, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(L2Tp.Classes.Class_, self).__setattr__(name, value)


            class Security(Entity):
                """
                Security check
                
                .. attribute:: ip
                
                	Security check for IP
                	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Security.Ip>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class_.Security, self).__init__()

                    self.yang_name = "security"
                    self.yang_parent_name = "class"

                    self.ip = L2Tp.Classes.Class_.Security.Ip()
                    self.ip.parent = self
                    self._children_name_map["ip"] = "ip"
                    self._children_yang_names.add("ip")


                class Ip(Entity):
                    """
                    Security check for IP
                    
                    .. attribute:: address_check
                    
                    	Enable IP address check for L2TP packets
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class_.Security.Ip, self).__init__()

                        self.yang_name = "ip"
                        self.yang_parent_name = "security"

                        self.address_check = YLeaf(YType.empty, "address-check")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address_check") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(L2Tp.Classes.Class_.Security.Ip, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L2Tp.Classes.Class_.Security.Ip, self).__setattr__(name, value)

                    def has_data(self):
                        return self.address_check.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address_check.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ip" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address_check.is_set or self.address_check.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_check.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address-check"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address-check"):
                            self.address_check = value
                            self.address_check.value_namespace = name_space
                            self.address_check.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.ip is not None and self.ip.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ip is not None and self.ip.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "security" + path_buffer

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

                    if (child_yang_name == "ip"):
                        if (self.ip is None):
                            self.ip = L2Tp.Classes.Class_.Security.Ip()
                            self.ip.parent = self
                            self._children_name_map["ip"] = "ip"
                        return self.ip

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Retransmit(Entity):
                """
                Control message retransmission parameters
                
                .. attribute:: initial
                
                	Set retries and timeouts for initial
                	**type**\:   :py:class:`Initial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Initial>`
                
                .. attribute:: retry
                
                	Specify retransmit retry count
                	**type**\:  int
                
                	**range:** 5..1000
                
                .. attribute:: timeout
                
                	Set timeout value range
                	**type**\:   :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Timeout>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class_.Retransmit, self).__init__()

                    self.yang_name = "retransmit"
                    self.yang_parent_name = "class"

                    self.retry = YLeaf(YType.uint32, "retry")

                    self.initial = L2Tp.Classes.Class_.Retransmit.Initial()
                    self.initial.parent = self
                    self._children_name_map["initial"] = "initial"
                    self._children_yang_names.add("initial")

                    self.timeout = L2Tp.Classes.Class_.Retransmit.Timeout()
                    self.timeout.parent = self
                    self._children_name_map["timeout"] = "timeout"
                    self._children_yang_names.add("timeout")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("retry") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L2Tp.Classes.Class_.Retransmit, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L2Tp.Classes.Class_.Retransmit, self).__setattr__(name, value)


                class Initial(Entity):
                    """
                    Set retries and timeouts for initial
                    
                    .. attribute:: retry
                    
                    	Specify the retry number
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    .. attribute:: timeout
                    
                    	Set timeout value range
                    	**type**\:   :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Initial.Timeout>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class_.Retransmit.Initial, self).__init__()

                        self.yang_name = "initial"
                        self.yang_parent_name = "retransmit"

                        self.retry = YLeaf(YType.uint32, "retry")

                        self.timeout = L2Tp.Classes.Class_.Retransmit.Initial.Timeout()
                        self.timeout.parent = self
                        self._children_name_map["timeout"] = "timeout"
                        self._children_yang_names.add("timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("retry") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(L2Tp.Classes.Class_.Retransmit.Initial, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L2Tp.Classes.Class_.Retransmit.Initial, self).__setattr__(name, value)


                    class Timeout(Entity):
                        """
                        Set timeout value range
                        
                        .. attribute:: maximum
                        
                        	Specify maximum timeout
                        	**type**\:  int
                        
                        	**range:** 1..8
                        
                        .. attribute:: minimum
                        
                        	Specify minimum timeout
                        	**type**\:  int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Classes.Class_.Retransmit.Initial.Timeout, self).__init__()

                            self.yang_name = "timeout"
                            self.yang_parent_name = "initial"

                            self.maximum = YLeaf(YType.uint32, "maximum")

                            self.minimum = YLeaf(YType.uint32, "minimum")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("maximum",
                                            "minimum") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(L2Tp.Classes.Class_.Retransmit.Initial.Timeout, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(L2Tp.Classes.Class_.Retransmit.Initial.Timeout, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.maximum.is_set or
                                self.minimum.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.maximum.yfilter != YFilter.not_set or
                                self.minimum.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "timeout" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maximum.get_name_leafdata())
                            if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minimum.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "maximum" or name == "minimum"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "maximum"):
                                self.maximum = value
                                self.maximum.value_namespace = name_space
                                self.maximum.value_namespace_prefix = name_space_prefix
                            if(value_path == "minimum"):
                                self.minimum = value
                                self.minimum.value_namespace = name_space
                                self.minimum.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.retry.is_set or
                            (self.timeout is not None and self.timeout.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.retry.yfilter != YFilter.not_set or
                            (self.timeout is not None and self.timeout.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "initial" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.retry.is_set or self.retry.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.retry.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "timeout"):
                            if (self.timeout is None):
                                self.timeout = L2Tp.Classes.Class_.Retransmit.Initial.Timeout()
                                self.timeout.parent = self
                                self._children_name_map["timeout"] = "timeout"
                            return self.timeout

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "timeout" or name == "retry"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "retry"):
                            self.retry = value
                            self.retry.value_namespace = name_space
                            self.retry.value_namespace_prefix = name_space_prefix


                class Timeout(Entity):
                    """
                    Set timeout value range
                    
                    .. attribute:: maximum
                    
                    	Specify maximum timeout
                    	**type**\:  int
                    
                    	**range:** 1..8
                    
                    .. attribute:: minimum
                    
                    	Specify minimum timeout
                    	**type**\:  int
                    
                    	**range:** 1..8
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class_.Retransmit.Timeout, self).__init__()

                        self.yang_name = "timeout"
                        self.yang_parent_name = "retransmit"

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.minimum = YLeaf(YType.uint32, "minimum")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("maximum",
                                        "minimum") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(L2Tp.Classes.Class_.Retransmit.Timeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L2Tp.Classes.Class_.Retransmit.Timeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.maximum.is_set or
                            self.minimum.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.maximum.yfilter != YFilter.not_set or
                            self.minimum.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum.get_name_leafdata())
                        if (self.minimum.is_set or self.minimum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minimum.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "maximum" or name == "minimum"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "maximum"):
                            self.maximum = value
                            self.maximum.value_namespace = name_space
                            self.maximum.value_namespace_prefix = name_space_prefix
                        if(value_path == "minimum"):
                            self.minimum = value
                            self.minimum.value_namespace = name_space
                            self.minimum.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.retry.is_set or
                        (self.initial is not None and self.initial.has_data()) or
                        (self.timeout is not None and self.timeout.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.retry.yfilter != YFilter.not_set or
                        (self.initial is not None and self.initial.has_operation()) or
                        (self.timeout is not None and self.timeout.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "retransmit" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.retry.is_set or self.retry.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "initial"):
                        if (self.initial is None):
                            self.initial = L2Tp.Classes.Class_.Retransmit.Initial()
                            self.initial.parent = self
                            self._children_name_map["initial"] = "initial"
                        return self.initial

                    if (child_yang_name == "timeout"):
                        if (self.timeout is None):
                            self.timeout = L2Tp.Classes.Class_.Retransmit.Timeout()
                            self.timeout.parent = self
                            self._children_name_map["timeout"] = "timeout"
                        return self.timeout

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "initial" or name == "timeout" or name == "retry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "retry"):
                        self.retry = value
                        self.retry.value_namespace = name_space
                        self.retry.value_namespace_prefix = name_space_prefix


            class Tunnel(Entity):
                """
                l2TP tunnel
                
                .. attribute:: accounting
                
                	Tunnel accounting
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class_.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "class"

                    self.accounting = YLeaf(YType.str, "accounting")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("accounting") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L2Tp.Classes.Class_.Tunnel, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L2Tp.Classes.Class_.Tunnel, self).__setattr__(name, value)

                def has_data(self):
                    return self.accounting.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.accounting.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tunnel" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.accounting.is_set or self.accounting.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "accounting"):
                        self.accounting = value
                        self.accounting.value_namespace = name_space
                        self.accounting.value_namespace_prefix = name_space_prefix


            class Digest(Entity):
                """
                Message digest authentication for the L2TP
                control connection
                
                .. attribute:: check_disable
                
                	Disable digest checking
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: hash
                
                	Specify hash method
                	**type**\:   :py:class:`L2TpDigestHashMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2TpDigestHashMethod>`
                
                .. attribute:: secrets
                
                	Set shared secret for message digest
                	**type**\:   :py:class:`Secrets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest.Secrets>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class_.Digest, self).__init__()

                    self.yang_name = "digest"
                    self.yang_parent_name = "class"

                    self.check_disable = YLeaf(YType.empty, "check-disable")

                    self.hash = YLeaf(YType.enumeration, "hash")

                    self.secrets = L2Tp.Classes.Class_.Digest.Secrets()
                    self.secrets.parent = self
                    self._children_name_map["secrets"] = "secrets"
                    self._children_yang_names.add("secrets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("check_disable",
                                    "hash") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L2Tp.Classes.Class_.Digest, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L2Tp.Classes.Class_.Digest, self).__setattr__(name, value)


                class Secrets(Entity):
                    """
                    Set shared secret for message digest
                    
                    .. attribute:: secret
                    
                    	The encrypted user secret and hash method
                    	**type**\: list of    :py:class:`Secret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest.Secrets.Secret>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class_.Digest.Secrets, self).__init__()

                        self.yang_name = "secrets"
                        self.yang_parent_name = "digest"

                        self.secret = YList(self)

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
                                    super(L2Tp.Classes.Class_.Digest.Secrets, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(L2Tp.Classes.Class_.Digest.Secrets, self).__setattr__(name, value)


                    class Secret(Entity):
                        """
                        The encrypted user secret and hash method
                        
                        .. attribute:: secret_name  <key>
                        
                        	Specify the encrypted user secret
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: hash
                        
                        	Specify hash method
                        	**type**\:   :py:class:`L2TpHashMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2TpHashMethod>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Classes.Class_.Digest.Secrets.Secret, self).__init__()

                            self.yang_name = "secret"
                            self.yang_parent_name = "secrets"

                            self.secret_name = YLeaf(YType.str, "secret-name")

                            self.hash = YLeaf(YType.enumeration, "hash")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("secret_name",
                                            "hash") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(L2Tp.Classes.Class_.Digest.Secrets.Secret, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(L2Tp.Classes.Class_.Digest.Secrets.Secret, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.secret_name.is_set or
                                self.hash.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.secret_name.yfilter != YFilter.not_set or
                                self.hash.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "secret" + "[secret-name='" + self.secret_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.secret_name.is_set or self.secret_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.secret_name.get_name_leafdata())
                            if (self.hash.is_set or self.hash.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hash.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "secret-name" or name == "hash"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "secret-name"):
                                self.secret_name = value
                                self.secret_name.value_namespace = name_space
                                self.secret_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "hash"):
                                self.hash = value
                                self.hash.value_namespace = name_space
                                self.hash.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.secret:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.secret:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "secrets" + path_buffer

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

                        if (child_yang_name == "secret"):
                            for c in self.secret:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = L2Tp.Classes.Class_.Digest.Secrets.Secret()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.secret.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "secret"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.check_disable.is_set or
                        self.hash.is_set or
                        (self.secrets is not None and self.secrets.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.check_disable.yfilter != YFilter.not_set or
                        self.hash.yfilter != YFilter.not_set or
                        (self.secrets is not None and self.secrets.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "digest" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.check_disable.is_set or self.check_disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.check_disable.get_name_leafdata())
                    if (self.hash.is_set or self.hash.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hash.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "secrets"):
                        if (self.secrets is None):
                            self.secrets = L2Tp.Classes.Class_.Digest.Secrets()
                            self.secrets.parent = self
                            self._children_name_map["secrets"] = "secrets"
                        return self.secrets

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "secrets" or name == "check-disable" or name == "hash"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "check-disable"):
                        self.check_disable = value
                        self.check_disable.value_namespace = name_space
                        self.check_disable.value_namespace_prefix = name_space_prefix
                    if(value_path == "hash"):
                        self.hash = value
                        self.hash.value_namespace = name_space
                        self.hash.value_namespace_prefix = name_space_prefix


            class Ip(Entity):
                """
                IP TOS value
                
                .. attribute:: tos
                
                	IP TOS value (decimal)
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class_.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "class"

                    self.tos = YLeaf(YType.uint32, "tos")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("tos") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(L2Tp.Classes.Class_.Ip, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(L2Tp.Classes.Class_.Ip, self).__setattr__(name, value)

                def has_data(self):
                    return self.tos.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.tos.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.tos.is_set or self.tos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tos.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tos"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "tos"):
                        self.tos = value
                        self.tos.value_namespace = name_space
                        self.tos.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.class_name.is_set or
                    self.authentication.is_set or
                    self.congestion_control.is_set or
                    self.enable.is_set or
                    self.hello_interval.is_set or
                    self.hidden.is_set or
                    self.host_name.is_set or
                    self.password.is_set or
                    self.receive_window.is_set or
                    self.timeout_no_user.is_set or
                    self.timeout_setup.is_set or
                    (self.digest is not None and self.digest.has_data()) or
                    (self.ip is not None and self.ip.has_data()) or
                    (self.retransmit is not None and self.retransmit.has_data()) or
                    (self.security is not None and self.security.has_data()) or
                    (self.tunnel is not None and self.tunnel.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.class_name.yfilter != YFilter.not_set or
                    self.authentication.yfilter != YFilter.not_set or
                    self.congestion_control.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.hello_interval.yfilter != YFilter.not_set or
                    self.hidden.yfilter != YFilter.not_set or
                    self.host_name.yfilter != YFilter.not_set or
                    self.password.yfilter != YFilter.not_set or
                    self.receive_window.yfilter != YFilter.not_set or
                    self.timeout_no_user.yfilter != YFilter.not_set or
                    self.timeout_setup.yfilter != YFilter.not_set or
                    (self.digest is not None and self.digest.has_operation()) or
                    (self.ip is not None and self.ip.has_operation()) or
                    (self.retransmit is not None and self.retransmit.has_operation()) or
                    (self.security is not None and self.security.has_operation()) or
                    (self.tunnel is not None and self.tunnel.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/classes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.class_name.get_name_leafdata())
                if (self.authentication.is_set or self.authentication.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authentication.get_name_leafdata())
                if (self.congestion_control.is_set or self.congestion_control.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.congestion_control.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.hello_interval.is_set or self.hello_interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hello_interval.get_name_leafdata())
                if (self.hidden.is_set or self.hidden.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hidden.get_name_leafdata())
                if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_name.get_name_leafdata())
                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password.get_name_leafdata())
                if (self.receive_window.is_set or self.receive_window.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.receive_window.get_name_leafdata())
                if (self.timeout_no_user.is_set or self.timeout_no_user.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout_no_user.get_name_leafdata())
                if (self.timeout_setup.is_set or self.timeout_setup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout_setup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "digest"):
                    if (self.digest is None):
                        self.digest = L2Tp.Classes.Class_.Digest()
                        self.digest.parent = self
                        self._children_name_map["digest"] = "digest"
                    return self.digest

                if (child_yang_name == "ip"):
                    if (self.ip is None):
                        self.ip = L2Tp.Classes.Class_.Ip()
                        self.ip.parent = self
                        self._children_name_map["ip"] = "ip"
                    return self.ip

                if (child_yang_name == "retransmit"):
                    if (self.retransmit is None):
                        self.retransmit = L2Tp.Classes.Class_.Retransmit()
                        self.retransmit.parent = self
                        self._children_name_map["retransmit"] = "retransmit"
                    return self.retransmit

                if (child_yang_name == "security"):
                    if (self.security is None):
                        self.security = L2Tp.Classes.Class_.Security()
                        self.security.parent = self
                        self._children_name_map["security"] = "security"
                    return self.security

                if (child_yang_name == "tunnel"):
                    if (self.tunnel is None):
                        self.tunnel = L2Tp.Classes.Class_.Tunnel()
                        self.tunnel.parent = self
                        self._children_name_map["tunnel"] = "tunnel"
                    return self.tunnel

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "digest" or name == "ip" or name == "retransmit" or name == "security" or name == "tunnel" or name == "class-name" or name == "authentication" or name == "congestion-control" or name == "enable" or name == "hello-interval" or name == "hidden" or name == "host-name" or name == "password" or name == "receive-window" or name == "timeout-no-user" or name == "timeout-setup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "class-name"):
                    self.class_name = value
                    self.class_name.value_namespace = name_space
                    self.class_name.value_namespace_prefix = name_space_prefix
                if(value_path == "authentication"):
                    self.authentication = value
                    self.authentication.value_namespace = name_space
                    self.authentication.value_namespace_prefix = name_space_prefix
                if(value_path == "congestion-control"):
                    self.congestion_control = value
                    self.congestion_control.value_namespace = name_space
                    self.congestion_control.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "hello-interval"):
                    self.hello_interval = value
                    self.hello_interval.value_namespace = name_space
                    self.hello_interval.value_namespace_prefix = name_space_prefix
                if(value_path == "hidden"):
                    self.hidden = value
                    self.hidden.value_namespace = name_space
                    self.hidden.value_namespace_prefix = name_space_prefix
                if(value_path == "host-name"):
                    self.host_name = value
                    self.host_name.value_namespace = name_space
                    self.host_name.value_namespace_prefix = name_space_prefix
                if(value_path == "password"):
                    self.password = value
                    self.password.value_namespace = name_space
                    self.password.value_namespace_prefix = name_space_prefix
                if(value_path == "receive-window"):
                    self.receive_window = value
                    self.receive_window.value_namespace = name_space
                    self.receive_window.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout-no-user"):
                    self.timeout_no_user = value
                    self.timeout_no_user.value_namespace = name_space
                    self.timeout_no_user.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout-setup"):
                    self.timeout_setup = value
                    self.timeout_setup.value_namespace = name_space
                    self.timeout_setup.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/%s" % self.get_segment_path()
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
                c = L2Tp.Classes.Class_()
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

    def has_data(self):
        return (self.classes is not None and self.classes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.classes is not None and self.classes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp" + path_buffer

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

        if (child_yang_name == "classes"):
            if (self.classes is None):
                self.classes = L2Tp.Classes()
                self.classes.parent = self
                self._children_name_map["classes"] = "classes"
            return self.classes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "classes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = L2Tp()
        return self._top_entity

