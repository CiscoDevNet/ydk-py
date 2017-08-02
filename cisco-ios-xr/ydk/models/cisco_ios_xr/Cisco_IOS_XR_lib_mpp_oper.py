""" Cisco_IOS_XR_lib_mpp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-mpp package operational data.

This module contains definitions
for the following management objects\:
  management\-plane\-protection\: Management Plane Protection (MPP)
    operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MppAllow(Enum):
    """
    MppAllow

    MPP protocol types

    .. data:: ssh = 0

    	SSH protocol

    .. data:: telnet = 1

    	TELNET protocol

    .. data:: snmp = 2

    	SNMP protocol

    .. data:: tftp = 3

    	TFTP protocol

    .. data:: http = 4

    	HTTP protocol

    .. data:: xr_xml = 5

    	XML

    .. data:: netconf = 6

    	NETCONF protocol

    .. data:: all = 7

    	All

    """

    ssh = Enum.YLeaf(0, "ssh")

    telnet = Enum.YLeaf(1, "telnet")

    snmp = Enum.YLeaf(2, "snmp")

    tftp = Enum.YLeaf(3, "tftp")

    http = Enum.YLeaf(4, "http")

    xr_xml = Enum.YLeaf(5, "xr-xml")

    netconf = Enum.YLeaf(6, "netconf")

    all = Enum.YLeaf(7, "all")



class MppAfIdBase(Identity):
    """
    Base identity for Mpp\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(MppAfIdBase, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:Mpp-af-id-base")


class ManagementPlaneProtection(Entity):
    """
    Management Plane Protection (MPP) operational
    data
    
    .. attribute:: inband
    
    	Management Plane Protection (MPP) inband interface data
    	**type**\:   :py:class:`Inband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband>`
    
    .. attribute:: outband
    
    	Management Plane Protection (MPP) outband interface data
    	**type**\:   :py:class:`Outband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband>`
    
    

    """

    _prefix = 'lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(ManagementPlaneProtection, self).__init__()
        self._top_entity = None

        self.yang_name = "management-plane-protection"
        self.yang_parent_name = "Cisco-IOS-XR-lib-mpp-oper"

        self.inband = ManagementPlaneProtection.Inband()
        self.inband.parent = self
        self._children_name_map["inband"] = "inband"
        self._children_yang_names.add("inband")

        self.outband = ManagementPlaneProtection.Outband()
        self.outband.parent = self
        self._children_name_map["outband"] = "outband"
        self._children_yang_names.add("outband")


    class Outband(Entity):
        """
        Management Plane Protection (MPP) outband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces>`
        
        .. attribute:: vrf
        
        	Outband VRF information
        	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Vrf>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(ManagementPlaneProtection.Outband, self).__init__()

            self.yang_name = "outband"
            self.yang_parent_name = "management-plane-protection"

            self.interfaces = ManagementPlaneProtection.Outband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.vrf = ManagementPlaneProtection.Outband.Vrf()
            self.vrf.parent = self
            self._children_name_map["vrf"] = "vrf"
            self._children_yang_names.add("vrf")


        class Vrf(Entity):
            """
            Outband VRF information
            
            .. attribute:: vrf_name
            
            	Outband VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "outband"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                            super(ManagementPlaneProtection.Outband.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ManagementPlaneProtection.Outband.Vrf, self).__setattr__(name, value)

            def has_data(self):
                return self.vrf_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self.get_segment_path()
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

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "outband"

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
                            super(ManagementPlaneProtection.Outband.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ManagementPlaneProtection.Outband.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(ManagementPlaneProtection.Outband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.protocol = YList(self)

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
                                super(ManagementPlaneProtection.Outband.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ManagementPlaneProtection.Outband.Interfaces.Interface, self).__setattr__(name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"

                        self.allow = YLeaf(YType.enumeration, "allow")

                        self.is_all_peers_allowed = YLeaf(YType.boolean, "is-all-peers-allowed")

                        self.peer_address = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("allow",
                                        "is_all_peers_allowed") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, self).__setattr__(name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "protocol"

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.peer_address:
                            if (c.has_data()):
                                return True
                        return (
                            self.allow.is_set or
                            self.is_all_peers_allowed.is_set)

                    def has_operation(self):
                        for c in self.peer_address:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.allow.yfilter != YFilter.not_set or
                            self.is_all_peers_allowed.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocol" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.allow.is_set or self.allow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.allow.get_name_leafdata())
                        if (self.is_all_peers_allowed.is_set or self.is_all_peers_allowed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_all_peers_allowed.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "peer-address"):
                            for c in self.peer_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.peer_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-address" or name == "allow" or name == "is-all-peers-allowed"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "allow"):
                            self.allow = value
                            self.allow.value_namespace = name_space
                            self.allow.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-all-peers-allowed"):
                            self.is_all_peers_allowed = value
                            self.is_all_peers_allowed.value_namespace = name_space
                            self.is_all_peers_allowed.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.protocol:
                        if (c.has_data()):
                            return True
                    return self.interface_name.is_set

                def has_operation(self):
                    for c in self.protocol:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/interfaces/%s" % self.get_segment_path()
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

                    if (child_yang_name == "protocol"):
                        for c in self.protocol:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.protocol.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol" or name == "interface-name"):
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
                    path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self.get_segment_path()
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
                    c = ManagementPlaneProtection.Outband.Interfaces.Interface()
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
                (self.interfaces is not None and self.interfaces.has_data()) or
                (self.vrf is not None and self.vrf.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()) or
                (self.vrf is not None and self.vrf.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "outband" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = ManagementPlaneProtection.Outband.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            if (child_yang_name == "vrf"):
                if (self.vrf is None):
                    self.vrf = ManagementPlaneProtection.Outband.Vrf()
                    self.vrf.parent = self
                    self._children_name_map["vrf"] = "vrf"
                return self.vrf

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces" or name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Inband(Entity):
        """
        Management Plane Protection (MPP) inband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(ManagementPlaneProtection.Inband, self).__init__()

            self.yang_name = "inband"
            self.yang_parent_name = "management-plane-protection"

            self.interfaces = ManagementPlaneProtection.Inband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(ManagementPlaneProtection.Inband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "inband"

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
                            super(ManagementPlaneProtection.Inband.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ManagementPlaneProtection.Inband.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    super(ManagementPlaneProtection.Inband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.protocol = YList(self)

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
                                super(ManagementPlaneProtection.Inband.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ManagementPlaneProtection.Inband.Interfaces.Interface, self).__setattr__(name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"

                        self.allow = YLeaf(YType.enumeration, "allow")

                        self.is_all_peers_allowed = YLeaf(YType.boolean, "is-all-peers-allowed")

                        self.peer_address = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("allow",
                                        "is_all_peers_allowed") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, self).__setattr__(name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "protocol"

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.peer_address:
                            if (c.has_data()):
                                return True
                        return (
                            self.allow.is_set or
                            self.is_all_peers_allowed.is_set)

                    def has_operation(self):
                        for c in self.peer_address:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.allow.yfilter != YFilter.not_set or
                            self.is_all_peers_allowed.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protocol" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.allow.is_set or self.allow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.allow.get_name_leafdata())
                        if (self.is_all_peers_allowed.is_set or self.is_all_peers_allowed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_all_peers_allowed.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "peer-address"):
                            for c in self.peer_address:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.peer_address.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-address" or name == "allow" or name == "is-all-peers-allowed"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "allow"):
                            self.allow = value
                            self.allow.value_namespace = name_space
                            self.allow.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-all-peers-allowed"):
                            self.is_all_peers_allowed = value
                            self.is_all_peers_allowed.value_namespace = name_space
                            self.is_all_peers_allowed.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.protocol:
                        if (c.has_data()):
                            return True
                    return self.interface_name.is_set

                def has_operation(self):
                    for c in self.protocol:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/interfaces/%s" % self.get_segment_path()
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

                    if (child_yang_name == "protocol"):
                        for c in self.protocol:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.protocol.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "protocol" or name == "interface-name"):
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
                    path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/%s" % self.get_segment_path()
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
                    c = ManagementPlaneProtection.Inband.Interfaces.Interface()
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
            return (self.interfaces is not None and self.interfaces.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.interfaces is not None and self.interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "inband" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = ManagementPlaneProtection.Inband.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.inband is not None and self.inband.has_data()) or
            (self.outband is not None and self.outband.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.inband is not None and self.inband.has_operation()) or
            (self.outband is not None and self.outband.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection" + path_buffer

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

        if (child_yang_name == "inband"):
            if (self.inband is None):
                self.inband = ManagementPlaneProtection.Inband()
                self.inband.parent = self
                self._children_name_map["inband"] = "inband"
            return self.inband

        if (child_yang_name == "outband"):
            if (self.outband is None):
                self.outband = ManagementPlaneProtection.Outband()
                self.outband.parent = self
                self._children_name_map["outband"] = "outband"
            return self.outband

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "inband" or name == "outband"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ManagementPlaneProtection()
        return self._top_entity

class Ipv4(Identity):
    """
    IPv4 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Ipv4, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:ipv4")


class Ipv6(Identity):
    """
    IPv6 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(Ipv6, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:ipv6")


