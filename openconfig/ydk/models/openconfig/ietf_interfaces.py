""" ietf_interfaces 

This module contains a collection of YANG definitions for
managing network interfaces.

Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 7223; see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InterfaceType(Identity):
    """
    Base identity from which specific interface types are
    derived.
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        super(InterfaceType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-interfaces", "ietf-interfaces", "ietf-interfaces:interface-type")


class Interfaces(Entity):
    """
    Interface configuration parameters.
    
    .. attribute:: interface
    
    	The list of configured interfaces on the device.  The operational state of an interface is available in the /interfaces\-state/interface list.  If the configuration of a system\-controlled interface cannot be used by the system (e.g., the interface hardware present does not match the interface type), then the configuration is not applied to the system\-controlled interface shown in the /interfaces\-state/interface list.  If the configuration of a user\-controlled interface cannot be used by the system, the configured interface is not instantiated in the /interfaces\-state/interface list
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        super(Interfaces, self).__init__()
        self._top_entity = None

        self.yang_name = "interfaces"
        self.yang_parent_name = "ietf-interfaces"

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
                    super(Interfaces, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Interfaces, self).__setattr__(name, value)


    class Interface(Entity):
        """
        The list of configured interfaces on the device.
        
        The operational state of an interface is available in the
        /interfaces\-state/interface list.  If the configuration of a
        system\-controlled interface cannot be used by the system
        (e.g., the interface hardware present does not match the
        interface type), then the configuration is not applied to
        the system\-controlled interface shown in the
        /interfaces\-state/interface list.  If the configuration
        of a user\-controlled interface cannot be used by the system,
        the configured interface is not instantiated in the
        /interfaces\-state/interface list.
        
        .. attribute:: name  <key>
        
        	The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list /interfaces\-state/interface contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the /interfaces\-state/interface list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  If the device supports pre\-provisioning of interface configuration, the 'pre\-provisioning' feature is advertised.  If the device allows arbitrarily named user\-controlled interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interface\-state/interface list
        	**type**\:  str
        
        .. attribute:: description
        
        	A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
        	**type**\:  str
        
        .. attribute:: diffserv_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of    :py:class:`DiffservTargetEntry <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.DiffservTargetEntry>`
        
        .. attribute:: enabled
        
        	This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.    Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
        	**type**\:  bool
        
        	**default value**\: true
        
        .. attribute:: ipv4
        
        	Parameters for the IPv4 address family
        	**type**\:   :py:class:`Ipv4 <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv4>`
        
        	**presence node**\: True
        
        .. attribute:: ipv6
        
        	Parameters for the IPv6 address family
        	**type**\:   :py:class:`Ipv6 <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6>`
        
        	**presence node**\: True
        
        .. attribute:: link_up_down_trap_enable
        
        	Controls whether linkUp/linkDown SNMP notifications should be generated for this interface.  If this node is not configured, the value 'enabled' is operationally used by the server for interfaces that do not operate on top of any other interface (i.e., there are no 'lower\-layer\-if' entries), and 'disabled' otherwise
        	**type**\:   :py:class:`LinkUpDownTrapEnable <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.LinkUpDownTrapEnable>`
        
        .. attribute:: type
        
        	The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
        	**type**\:   :py:class:`InterfaceType <ydk.models.ietf.ietf_interfaces.InterfaceType>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            super(Interfaces.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "interfaces"

            self.name = YLeaf(YType.str, "name")

            self.description = YLeaf(YType.str, "description")

            self.enabled = YLeaf(YType.boolean, "enabled")

            self.link_up_down_trap_enable = YLeaf(YType.enumeration, "link-up-down-trap-enable")

            self.type = YLeaf(YType.identityref, "type")

            self.ipv4 = None
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = None
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.diffserv_target_entry = YList(self)

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
                            "description",
                            "enabled",
                            "link_up_down_trap_enable",
                            "type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Interfaces.Interface, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Interfaces.Interface, self).__setattr__(name, value)

        class LinkUpDownTrapEnable(Enum):
            """
            LinkUpDownTrapEnable

            Controls whether linkUp/linkDown SNMP notifications

            should be generated for this interface.

            If this node is not configured, the value 'enabled' is

            operationally used by the server for interfaces that do

            not operate on top of any other interface (i.e., there are

            no 'lower\-layer\-if' entries), and 'disabled' otherwise.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")



        class DiffservTargetEntry(Entity):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`Direction <ydk.models.ietf.ietf_diffserv_target.Direction>`
            
            .. attribute:: policy_name  <key>
            
            	Policy entry name
            	**type**\:  str
            
            

            """

            _prefix = 'target'
            _revision = '2015-04-07'

            def __init__(self):
                super(Interfaces.Interface.DiffservTargetEntry, self).__init__()

                self.yang_name = "diffserv-target-entry"
                self.yang_parent_name = "interface"

                self.direction = YLeaf(YType.identityref, "direction")

                self.policy_name = YLeaf(YType.str, "policy-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("direction",
                                "policy_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Interfaces.Interface.DiffservTargetEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Interfaces.Interface.DiffservTargetEntry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.direction.is_set or
                    self.policy_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.direction.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-diffserv-target:diffserv-target-entry" + "[direction='" + self.direction.get() + "']" + "[policy-name='" + self.policy_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.direction.get_name_leafdata())
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "direction" or name == "policy-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "direction"):
                    self.direction = value
                    self.direction.value_namespace = name_space
                    self.direction.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix


        class Ipv4(Entity):
            """
            Parameters for the IPv4 address family.
            
            .. attribute:: address
            
            	The list of configured IPv4 addresses on the interface
            	**type**\: list of    :py:class:`Address <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv4.Address>`
            
            .. attribute:: enabled
            
            	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: forwarding
            
            	Controls IPv4 packet forwarding of datagrams received by, but not addressed to, this interface.  IPv4 routers forward datagrams.  IPv4 hosts do not (except those source\-routed via the host)
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: mtu
            
            	The size, in octets, of the largest IPv4 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
            	**type**\:  int
            
            	**range:** 68..65535
            
            	**units**\: octets
            
            .. attribute:: neighbor
            
            	A list of mappings from IPv4 addresses to link\-layer addresses. Entries in this list are used as static entries in the ARP Cache
            	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv4.Neighbor>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                super(Interfaces.Interface.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "interface"
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.address = YList(self)
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
                    if name in ("enabled",
                                "forwarding",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Interfaces.Interface.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Interfaces.Interface.Ipv4, self).__setattr__(name, value)


            class Address(Entity):
                """
                The list of configured IPv4 addresses on the interface.
                
                .. attribute:: ip  <key>
                
                	The IPv4 address on the interface
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask
                
                	The subnet specified as a netmask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..32
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(Interfaces.Interface.Ipv4.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "ipv4"

                    self.ip = YLeaf(YType.str, "ip")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "netmask",
                                    "prefix_length") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv4.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv4.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.netmask.is_set or
                        self.prefix_length.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.netmask.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.netmask.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "netmask" or name == "prefix-length"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "netmask"):
                        self.netmask = value
                        self.netmask.value_namespace = name_space
                        self.netmask.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix


            class Neighbor(Entity):
                """
                A list of mappings from IPv4 addresses to
                link\-layer addresses.
                Entries in this list are used as static entries in the
                ARP Cache.
                
                .. attribute:: ip  <key>
                
                	The IPv4 address of the neighbor node
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: link_layer_address
                
                	The link\-layer address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(Interfaces.Interface.Ipv4.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "ipv4"

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "link_layer_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv4.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv4.Neighbor, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.link_layer_address.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.link_layer_address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_layer_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "link-layer-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-layer-address"):
                        self.link_layer_address = value
                        self.link_layer_address.value_namespace = name_space
                        self.link_layer_address.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                for c in self.neighbor:
                    if (c.has_data()):
                        return True
                return (
                    self.enabled.is_set or
                    self.forwarding.is_set or
                    self.mtu.is_set)

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                for c in self.neighbor:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.forwarding.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-ip:ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.forwarding.is_set or self.forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Interfaces.Interface.Ipv4.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                if (child_yang_name == "neighbor"):
                    for c in self.neighbor:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Interfaces.Interface.Ipv4.Neighbor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "neighbor" or name == "enabled" or name == "forwarding" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "forwarding"):
                    self.forwarding = value
                    self.forwarding.value_namespace = name_space
                    self.forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix


        class Ipv6(Entity):
            """
            Parameters for the IPv6 address family.
            
            .. attribute:: address
            
            	The list of configured IPv6 addresses on the interface
            	**type**\: list of    :py:class:`Address <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Address>`
            
            .. attribute:: autoconf
            
            	Parameters to control the autoconfiguration of IPv6 addresses, as described in RFC 4862
            	**type**\:   :py:class:`Autoconf <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Autoconf>`
            
            .. attribute:: dup_addr_detect_transmits
            
            	The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 1
            
            .. attribute:: enabled
            
            	Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: forwarding
            
            	Controls IPv6 packet forwarding of datagrams received by, but not addressed to, this interface.  IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host)
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: ipv6_router_advertisements
            
            	Configuration of IPv6 Router Advertisements
            	**type**\:   :py:class:`Ipv6RouterAdvertisements <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements>`
            
            .. attribute:: mtu
            
            	The size, in octets, of the largest IPv6 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
            	**type**\:  int
            
            	**range:** 1280..4294967295
            
            	**units**\: octets
            
            .. attribute:: neighbor
            
            	A list of mappings from IPv6 addresses to link\-layer addresses. Entries in this list are used as static entries in the Neighbor Cache
            	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Neighbor>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                super(Interfaces.Interface.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "interface"
                self.is_presence_container = True

                self.dup_addr_detect_transmits = YLeaf(YType.uint32, "dup-addr-detect-transmits")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint32, "mtu")

                self.autoconf = Interfaces.Interface.Ipv6.Autoconf()
                self.autoconf.parent = self
                self._children_name_map["autoconf"] = "autoconf"
                self._children_yang_names.add("autoconf")

                self.ipv6_router_advertisements = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements()
                self.ipv6_router_advertisements.parent = self
                self._children_name_map["ipv6_router_advertisements"] = "ipv6-router-advertisements"
                self._children_yang_names.add("ipv6-router-advertisements")

                self.address = YList(self)
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
                    if name in ("dup_addr_detect_transmits",
                                "enabled",
                                "forwarding",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Interfaces.Interface.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Interfaces.Interface.Ipv6, self).__setattr__(name, value)


            class Address(Entity):
                """
                The list of configured IPv6 addresses on the interface.
                
                .. attribute:: ip  <key>
                
                	The IPv6 address on the interface
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..128
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(Interfaces.Interface.Ipv6.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "ipv6"

                    self.ip = YLeaf(YType.str, "ip")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "prefix_length") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv6.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv6.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.prefix_length.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "prefix-length"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix


            class Neighbor(Entity):
                """
                A list of mappings from IPv6 addresses to
                link\-layer addresses.
                Entries in this list are used as static entries in the
                Neighbor Cache.
                
                .. attribute:: ip  <key>
                
                	The IPv6 address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: link_layer_address
                
                	The link\-layer address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(Interfaces.Interface.Ipv6.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "ipv6"

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "link_layer_address") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv6.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv6.Neighbor, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.link_layer_address.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.link_layer_address.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_layer_address.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "link-layer-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-layer-address"):
                        self.link_layer_address = value
                        self.link_layer_address.value_namespace = name_space
                        self.link_layer_address.value_namespace_prefix = name_space_prefix


            class Autoconf(Entity):
                """
                Parameters to control the autoconfiguration of IPv6
                addresses, as described in RFC 4862.
                
                .. attribute:: create_global_addresses
                
                	If enabled, the host creates global addresses as described in RFC 4862
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: create_temporary_addresses
                
                	If enabled, the host creates temporary addresses as described in RFC 4941
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: temporary_preferred_lifetime
                
                	The time period during which the temporary address is preferred
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 86400
                
                .. attribute:: temporary_valid_lifetime
                
                	The time period during which the temporary address is valid
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 604800
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(Interfaces.Interface.Ipv6.Autoconf, self).__init__()

                    self.yang_name = "autoconf"
                    self.yang_parent_name = "ipv6"

                    self.create_global_addresses = YLeaf(YType.boolean, "create-global-addresses")

                    self.create_temporary_addresses = YLeaf(YType.boolean, "create-temporary-addresses")

                    self.temporary_preferred_lifetime = YLeaf(YType.uint32, "temporary-preferred-lifetime")

                    self.temporary_valid_lifetime = YLeaf(YType.uint32, "temporary-valid-lifetime")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("create_global_addresses",
                                    "create_temporary_addresses",
                                    "temporary_preferred_lifetime",
                                    "temporary_valid_lifetime") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv6.Autoconf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv6.Autoconf, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.create_global_addresses.is_set or
                        self.create_temporary_addresses.is_set or
                        self.temporary_preferred_lifetime.is_set or
                        self.temporary_valid_lifetime.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.create_global_addresses.yfilter != YFilter.not_set or
                        self.create_temporary_addresses.yfilter != YFilter.not_set or
                        self.temporary_preferred_lifetime.yfilter != YFilter.not_set or
                        self.temporary_valid_lifetime.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "autoconf" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.create_global_addresses.is_set or self.create_global_addresses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.create_global_addresses.get_name_leafdata())
                    if (self.create_temporary_addresses.is_set or self.create_temporary_addresses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.create_temporary_addresses.get_name_leafdata())
                    if (self.temporary_preferred_lifetime.is_set or self.temporary_preferred_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temporary_preferred_lifetime.get_name_leafdata())
                    if (self.temporary_valid_lifetime.is_set or self.temporary_valid_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temporary_valid_lifetime.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "create-global-addresses" or name == "create-temporary-addresses" or name == "temporary-preferred-lifetime" or name == "temporary-valid-lifetime"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "create-global-addresses"):
                        self.create_global_addresses = value
                        self.create_global_addresses.value_namespace = name_space
                        self.create_global_addresses.value_namespace_prefix = name_space_prefix
                    if(value_path == "create-temporary-addresses"):
                        self.create_temporary_addresses = value
                        self.create_temporary_addresses.value_namespace = name_space
                        self.create_temporary_addresses.value_namespace_prefix = name_space_prefix
                    if(value_path == "temporary-preferred-lifetime"):
                        self.temporary_preferred_lifetime = value
                        self.temporary_preferred_lifetime.value_namespace = name_space
                        self.temporary_preferred_lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "temporary-valid-lifetime"):
                        self.temporary_valid_lifetime = value
                        self.temporary_valid_lifetime.value_namespace = name_space
                        self.temporary_valid_lifetime.value_namespace_prefix = name_space_prefix


            class Ipv6RouterAdvertisements(Entity):
                """
                Configuration of IPv6 Router Advertisements.
                
                .. attribute:: cur_hop_limit
                
                	The value to be placed in the Cur Hop Limit field in the Router Advertisement messages sent by the router. A value of zero means unspecified (by this router).  If this parameter is not configured, the device SHOULD use the value specified in IANA Assigned Numbers that was in effect at the time of implementation
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: default_lifetime
                
                	The value to be placed in the Router Lifetime field of Router Advertisements sent from the interface, in seconds. It MUST be either zero or between max\-rtr\-adv\-interval and 9000 seconds. A value of zero indicates that the router is not to be used as a default router. These limits may be overridden by specific documents that describe how IPv6 operates over different link layers.  If this parameter is not configured, the device SHOULD use a value of 3 \* max\-rtr\-adv\-interval
                	**type**\:  int
                
                	**range:** 0..9000
                
                	**units**\: seconds
                
                .. attribute:: link_mtu
                
                	The value to be placed in MTU options sent by the router. A value of zero indicates that no MTU options are sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 0
                
                .. attribute:: managed_flag
                
                	The value to be placed in the 'Managed address configuration' flag field in the Router Advertisement
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: max_rtr_adv_interval
                
                	The maximum time allowed between sending unsolicited multicast Router Advertisements from the interface
                	**type**\:  int
                
                	**range:** 4..1800
                
                	**units**\: seconds
                
                	**default value**\: 600
                
                .. attribute:: min_rtr_adv_interval
                
                	The minimum time allowed between sending unsolicited multicast Router Advertisements from the interface.  The default value to be used operationally if this leaf is not configured is determined as follows\:  \- if max\-rtr\-adv\-interval >= 9 seconds, the default value   is 0.33 \* max\-rtr\-adv\-interval;  \- otherwise it is 0.75 \* max\-rtr\-adv\-interval
                	**type**\:  int
                
                	**range:** 3..1350
                
                	**units**\: seconds
                
                .. attribute:: other_config_flag
                
                	The value to be placed in the 'Other configuration' flag field in the Router Advertisement
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: prefix_list
                
                	Configuration of prefixes to be placed in Prefix Information options in Router Advertisement messages sent from the interface.  Prefixes that are advertised by default but do not have their entries in the child 'prefix' list are advertised with the default values of all parameters.  The link\-local prefix SHOULD NOT be included in the list of advertised prefixes
                	**type**\:   :py:class:`PrefixList <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList>`
                
                .. attribute:: reachable_time
                
                	The value to be placed in the Reachable Time field in the Router Advertisement messages sent by the router. A value of zero means unspecified (by this router)
                	**type**\:  int
                
                	**range:** 0..3600000
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: retrans_timer
                
                	The value to be placed in the Retrans Timer field in the Router Advertisement messages sent by the router. A value of zero means unspecified (by this router)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: send_advertisements
                
                	A flag indicating whether or not the router sends periodic Router Advertisements and responds to Router Solicitations
                	**type**\:  bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'v6ur'
                _revision = '2015-05-25'

                def __init__(self):
                    super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements, self).__init__()

                    self.yang_name = "ipv6-router-advertisements"
                    self.yang_parent_name = "ipv6"

                    self.cur_hop_limit = YLeaf(YType.uint8, "cur-hop-limit")

                    self.default_lifetime = YLeaf(YType.uint16, "default-lifetime")

                    self.link_mtu = YLeaf(YType.uint32, "link-mtu")

                    self.managed_flag = YLeaf(YType.boolean, "managed-flag")

                    self.max_rtr_adv_interval = YLeaf(YType.uint16, "max-rtr-adv-interval")

                    self.min_rtr_adv_interval = YLeaf(YType.uint16, "min-rtr-adv-interval")

                    self.other_config_flag = YLeaf(YType.boolean, "other-config-flag")

                    self.reachable_time = YLeaf(YType.uint32, "reachable-time")

                    self.retrans_timer = YLeaf(YType.uint32, "retrans-timer")

                    self.send_advertisements = YLeaf(YType.boolean, "send-advertisements")

                    self.prefix_list = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList()
                    self.prefix_list.parent = self
                    self._children_name_map["prefix_list"] = "prefix-list"
                    self._children_yang_names.add("prefix-list")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cur_hop_limit",
                                    "default_lifetime",
                                    "link_mtu",
                                    "managed_flag",
                                    "max_rtr_adv_interval",
                                    "min_rtr_adv_interval",
                                    "other_config_flag",
                                    "reachable_time",
                                    "retrans_timer",
                                    "send_advertisements") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements, self).__setattr__(name, value)


                class PrefixList(Entity):
                    """
                    Configuration of prefixes to be placed in Prefix
                    Information options in Router Advertisement messages sent
                    from the interface.
                    
                    Prefixes that are advertised by default but do not have
                    their entries in the child 'prefix' list are advertised
                    with the default values of all parameters.
                    
                    The link\-local prefix SHOULD NOT be included in the list
                    of advertised prefixes.
                    
                    .. attribute:: prefix
                    
                    	Configuration of an advertised prefix entry
                    	**type**\: list of    :py:class:`Prefix <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix>`
                    
                    

                    """

                    _prefix = 'v6ur'
                    _revision = '2015-05-25'

                    def __init__(self):
                        super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList, self).__init__()

                        self.yang_name = "prefix-list"
                        self.yang_parent_name = "ipv6-router-advertisements"

                        self.prefix = YList(self)

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
                                    super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList, self).__setattr__(name, value)


                    class Prefix(Entity):
                        """
                        Configuration of an advertised prefix entry.
                        
                        .. attribute:: prefix_spec  <key>
                        
                        	IPv6 address prefix
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        .. attribute:: autonomous_flag
                        
                        	The value to be placed in the Autonomous Flag field in the Prefix Information option
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: no_advertise
                        
                        	The prefix will not be advertised.  This can be used for removing the prefix from the default set of advertised prefixes
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: on_link_flag
                        
                        	The value to be placed in the on\-link flag ('L\-bit') field in the Prefix Information option
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: preferred_lifetime
                        
                        	The value to be placed in the Preferred Lifetime in the Prefix Information option. The designated value of all 1's (0xffffffff) represents infinity
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 604800
                        
                        .. attribute:: valid_lifetime
                        
                        	The value to be placed in the Valid Lifetime in the Prefix Information option. The designated value of all 1's (0xffffffff) represents infinity
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 2592000
                        
                        

                        """

                        _prefix = 'v6ur'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefix-list"

                            self.prefix_spec = YLeaf(YType.str, "prefix-spec")

                            self.autonomous_flag = YLeaf(YType.boolean, "autonomous-flag")

                            self.no_advertise = YLeaf(YType.empty, "no-advertise")

                            self.on_link_flag = YLeaf(YType.boolean, "on-link-flag")

                            self.preferred_lifetime = YLeaf(YType.uint32, "preferred-lifetime")

                            self.valid_lifetime = YLeaf(YType.uint32, "valid-lifetime")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prefix_spec",
                                            "autonomous_flag",
                                            "no_advertise",
                                            "on_link_flag",
                                            "preferred_lifetime",
                                            "valid_lifetime") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.prefix_spec.is_set or
                                self.autonomous_flag.is_set or
                                self.no_advertise.is_set or
                                self.on_link_flag.is_set or
                                self.preferred_lifetime.is_set or
                                self.valid_lifetime.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prefix_spec.yfilter != YFilter.not_set or
                                self.autonomous_flag.yfilter != YFilter.not_set or
                                self.no_advertise.yfilter != YFilter.not_set or
                                self.on_link_flag.yfilter != YFilter.not_set or
                                self.preferred_lifetime.yfilter != YFilter.not_set or
                                self.valid_lifetime.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prefix" + "[prefix-spec='" + self.prefix_spec.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.prefix_spec.is_set or self.prefix_spec.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_spec.get_name_leafdata())
                            if (self.autonomous_flag.is_set or self.autonomous_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.autonomous_flag.get_name_leafdata())
                            if (self.no_advertise.is_set or self.no_advertise.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_advertise.get_name_leafdata())
                            if (self.on_link_flag.is_set or self.on_link_flag.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.on_link_flag.get_name_leafdata())
                            if (self.preferred_lifetime.is_set or self.preferred_lifetime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.preferred_lifetime.get_name_leafdata())
                            if (self.valid_lifetime.is_set or self.valid_lifetime.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.valid_lifetime.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prefix-spec" or name == "autonomous-flag" or name == "no-advertise" or name == "on-link-flag" or name == "preferred-lifetime" or name == "valid-lifetime"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prefix-spec"):
                                self.prefix_spec = value
                                self.prefix_spec.value_namespace = name_space
                                self.prefix_spec.value_namespace_prefix = name_space_prefix
                            if(value_path == "autonomous-flag"):
                                self.autonomous_flag = value
                                self.autonomous_flag.value_namespace = name_space
                                self.autonomous_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-advertise"):
                                self.no_advertise = value
                                self.no_advertise.value_namespace = name_space
                                self.no_advertise.value_namespace_prefix = name_space_prefix
                            if(value_path == "on-link-flag"):
                                self.on_link_flag = value
                                self.on_link_flag.value_namespace = name_space
                                self.on_link_flag.value_namespace_prefix = name_space_prefix
                            if(value_path == "preferred-lifetime"):
                                self.preferred_lifetime = value
                                self.preferred_lifetime.value_namespace = name_space
                                self.preferred_lifetime.value_namespace_prefix = name_space_prefix
                            if(value_path == "valid-lifetime"):
                                self.valid_lifetime = value
                                self.valid_lifetime.value_namespace = name_space
                                self.valid_lifetime.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prefix:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prefix:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefix-list" + path_buffer

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

                        if (child_yang_name == "prefix"):
                            for c in self.prefix:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prefix.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.cur_hop_limit.is_set or
                        self.default_lifetime.is_set or
                        self.link_mtu.is_set or
                        self.managed_flag.is_set or
                        self.max_rtr_adv_interval.is_set or
                        self.min_rtr_adv_interval.is_set or
                        self.other_config_flag.is_set or
                        self.reachable_time.is_set or
                        self.retrans_timer.is_set or
                        self.send_advertisements.is_set or
                        (self.prefix_list is not None and self.prefix_list.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cur_hop_limit.yfilter != YFilter.not_set or
                        self.default_lifetime.yfilter != YFilter.not_set or
                        self.link_mtu.yfilter != YFilter.not_set or
                        self.managed_flag.yfilter != YFilter.not_set or
                        self.max_rtr_adv_interval.yfilter != YFilter.not_set or
                        self.min_rtr_adv_interval.yfilter != YFilter.not_set or
                        self.other_config_flag.yfilter != YFilter.not_set or
                        self.reachable_time.yfilter != YFilter.not_set or
                        self.retrans_timer.yfilter != YFilter.not_set or
                        self.send_advertisements.yfilter != YFilter.not_set or
                        (self.prefix_list is not None and self.prefix_list.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ietf-ipv6-unicast-routing:ipv6-router-advertisements" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cur_hop_limit.is_set or self.cur_hop_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cur_hop_limit.get_name_leafdata())
                    if (self.default_lifetime.is_set or self.default_lifetime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_lifetime.get_name_leafdata())
                    if (self.link_mtu.is_set or self.link_mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_mtu.get_name_leafdata())
                    if (self.managed_flag.is_set or self.managed_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.managed_flag.get_name_leafdata())
                    if (self.max_rtr_adv_interval.is_set or self.max_rtr_adv_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_rtr_adv_interval.get_name_leafdata())
                    if (self.min_rtr_adv_interval.is_set or self.min_rtr_adv_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_rtr_adv_interval.get_name_leafdata())
                    if (self.other_config_flag.is_set or self.other_config_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.other_config_flag.get_name_leafdata())
                    if (self.reachable_time.is_set or self.reachable_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reachable_time.get_name_leafdata())
                    if (self.retrans_timer.is_set or self.retrans_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retrans_timer.get_name_leafdata())
                    if (self.send_advertisements.is_set or self.send_advertisements.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.send_advertisements.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "prefix-list"):
                        if (self.prefix_list is None):
                            self.prefix_list = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList()
                            self.prefix_list.parent = self
                            self._children_name_map["prefix_list"] = "prefix-list"
                        return self.prefix_list

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix-list" or name == "cur-hop-limit" or name == "default-lifetime" or name == "link-mtu" or name == "managed-flag" or name == "max-rtr-adv-interval" or name == "min-rtr-adv-interval" or name == "other-config-flag" or name == "reachable-time" or name == "retrans-timer" or name == "send-advertisements"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cur-hop-limit"):
                        self.cur_hop_limit = value
                        self.cur_hop_limit.value_namespace = name_space
                        self.cur_hop_limit.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-lifetime"):
                        self.default_lifetime = value
                        self.default_lifetime.value_namespace = name_space
                        self.default_lifetime.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-mtu"):
                        self.link_mtu = value
                        self.link_mtu.value_namespace = name_space
                        self.link_mtu.value_namespace_prefix = name_space_prefix
                    if(value_path == "managed-flag"):
                        self.managed_flag = value
                        self.managed_flag.value_namespace = name_space
                        self.managed_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-rtr-adv-interval"):
                        self.max_rtr_adv_interval = value
                        self.max_rtr_adv_interval.value_namespace = name_space
                        self.max_rtr_adv_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-rtr-adv-interval"):
                        self.min_rtr_adv_interval = value
                        self.min_rtr_adv_interval.value_namespace = name_space
                        self.min_rtr_adv_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "other-config-flag"):
                        self.other_config_flag = value
                        self.other_config_flag.value_namespace = name_space
                        self.other_config_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "reachable-time"):
                        self.reachable_time = value
                        self.reachable_time.value_namespace = name_space
                        self.reachable_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "retrans-timer"):
                        self.retrans_timer = value
                        self.retrans_timer.value_namespace = name_space
                        self.retrans_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "send-advertisements"):
                        self.send_advertisements = value
                        self.send_advertisements.value_namespace = name_space
                        self.send_advertisements.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                for c in self.neighbor:
                    if (c.has_data()):
                        return True
                return (
                    self.dup_addr_detect_transmits.is_set or
                    self.enabled.is_set or
                    self.forwarding.is_set or
                    self.mtu.is_set or
                    (self.autoconf is not None and self.autoconf.has_data()) or
                    (self.ipv6_router_advertisements is not None and self.ipv6_router_advertisements.has_data()))

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                for c in self.neighbor:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.dup_addr_detect_transmits.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.forwarding.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set or
                    (self.autoconf is not None and self.autoconf.has_operation()) or
                    (self.ipv6_router_advertisements is not None and self.ipv6_router_advertisements.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-ip:ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dup_addr_detect_transmits.is_set or self.dup_addr_detect_transmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dup_addr_detect_transmits.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.forwarding.is_set or self.forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Interfaces.Interface.Ipv6.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                if (child_yang_name == "autoconf"):
                    if (self.autoconf is None):
                        self.autoconf = Interfaces.Interface.Ipv6.Autoconf()
                        self.autoconf.parent = self
                        self._children_name_map["autoconf"] = "autoconf"
                    return self.autoconf

                if (child_yang_name == "ipv6-router-advertisements"):
                    if (self.ipv6_router_advertisements is None):
                        self.ipv6_router_advertisements = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements()
                        self.ipv6_router_advertisements.parent = self
                        self._children_name_map["ipv6_router_advertisements"] = "ipv6-router-advertisements"
                    return self.ipv6_router_advertisements

                if (child_yang_name == "neighbor"):
                    for c in self.neighbor:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Interfaces.Interface.Ipv6.Neighbor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "autoconf" or name == "ipv6-router-advertisements" or name == "neighbor" or name == "dup-addr-detect-transmits" or name == "enabled" or name == "forwarding" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dup-addr-detect-transmits"):
                    self.dup_addr_detect_transmits = value
                    self.dup_addr_detect_transmits.value_namespace = name_space
                    self.dup_addr_detect_transmits.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "forwarding"):
                    self.forwarding = value
                    self.forwarding.value_namespace = name_space
                    self.forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffserv_target_entry:
                if (c.has_data()):
                    return True
            return (
                self.name.is_set or
                self.description.is_set or
                self.enabled.is_set or
                self.link_up_down_trap_enable.is_set or
                self.type.is_set or
                (self.ipv4 is not None) or
                (self.ipv6 is not None))

        def has_operation(self):
            for c in self.diffserv_target_entry:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.description.yfilter != YFilter.not_set or
                self.enabled.yfilter != YFilter.not_set or
                self.link_up_down_trap_enable.yfilter != YFilter.not_set or
                self.type.yfilter != YFilter.not_set or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-interfaces:interfaces/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                leaf_name_data.append(self.description.get_name_leafdata())
            if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enabled.get_name_leafdata())
            if (self.link_up_down_trap_enable.is_set or self.link_up_down_trap_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.link_up_down_trap_enable.get_name_leafdata())
            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffserv-target-entry"):
                for c in self.diffserv_target_entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Interfaces.Interface.DiffservTargetEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffserv_target_entry.append(c)
                return c

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = Interfaces.Interface.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Interfaces.Interface.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffserv-target-entry" or name == "ipv4" or name == "ipv6" or name == "name" or name == "description" or name == "enabled" or name == "link-up-down-trap-enable" or name == "type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "description"):
                self.description = value
                self.description.value_namespace = name_space
                self.description.value_namespace_prefix = name_space_prefix
            if(value_path == "enabled"):
                self.enabled = value
                self.enabled.value_namespace = name_space
                self.enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "link-up-down-trap-enable"):
                self.link_up_down_trap_enable = value
                self.link_up_down_trap_enable.value_namespace = name_space
                self.link_up_down_trap_enable.value_namespace_prefix = name_space_prefix
            if(value_path == "type"):
                self.type = value
                self.type.value_namespace = name_space
                self.type.value_namespace_prefix = name_space_prefix

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
        path_buffer = "ietf-interfaces:interfaces" + path_buffer

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

        if (child_yang_name == "interface"):
            for c in self.interface:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Interfaces.Interface()
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

    def clone_ptr(self):
        self._top_entity = Interfaces()
        return self._top_entity

class InterfacesState(Entity):
    """
    Data nodes for the operational state of interfaces.
    
    .. attribute:: interface
    
    	The list of interfaces on the device.  System\-controlled interfaces created by the system are always present in this list, whether they are configured or not
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        super(InterfacesState, self).__init__()
        self._top_entity = None

        self.yang_name = "interfaces-state"
        self.yang_parent_name = "ietf-interfaces"

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
                    super(InterfacesState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(InterfacesState, self).__setattr__(name, value)


    class Interface(Entity):
        """
        The list of interfaces on the device.
        
        System\-controlled interfaces created by the system are
        always present in this list, whether they are configured or
        not.
        
        .. attribute:: name  <key>
        
        	The name of the interface.  A server implementation MAY map this leaf to the ifName MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifName.  The definition of such a mechanism is outside the scope of this document
        	**type**\:  str
        
        .. attribute:: admin_status
        
        	The desired state of the interface.  This leaf has the same read semantics as ifAdminStatus
        	**type**\:   :py:class:`AdminStatus <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.AdminStatus>`
        
        	**mandatory**\: True
        
        .. attribute:: diffserv_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of    :py:class:`DiffservTargetEntry <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry>`
        
        .. attribute:: higher_layer_if
        
        	A list of references to interfaces layered on top of this interface
        	**type**\:  list of str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
        
        .. attribute:: if_index
        
        	The ifIndex value for the ifEntry represented by this interface
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**mandatory**\: True
        
        .. attribute:: ipv4
        
        	Interface\-specific parameters for the IPv4 address family
        	**type**\:   :py:class:`Ipv4 <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv4>`
        
        	**presence node**\: True
        
        .. attribute:: ipv6
        
        	Parameters for the IPv6 address family
        	**type**\:   :py:class:`Ipv6 <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6>`
        
        	**presence node**\: True
        
        .. attribute:: last_change
        
        	The time the interface entered its current operational state.  If the current state was entered prior to the last re\-initialization of the local network management subsystem, then this node is not present
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: lower_layer_if
        
        	A list of references to interfaces layered underneath this interface
        	**type**\:  list of str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
        
        .. attribute:: oper_status
        
        	The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
        	**type**\:   :py:class:`OperStatus <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.OperStatus>`
        
        	**mandatory**\: True
        
        .. attribute:: phys_address
        
        	The interface's address at its protocol sub\-layer.  For example, for an 802.x interface, this object normally contains a Media Access Control (MAC) address.  The interface's media\-specific modules must define the bit   and byte ordering and the format of the value of this object.  For interfaces that do not have such an address (e.g., a serial line), this node is not present
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
        
        .. attribute:: routing_instance
        
        	The name of the routing instance to which the interface is assigned
        	**type**\:  str
        
        .. attribute:: speed
        
        	An estimate of the interface's current bandwidth in bits per second.  For interfaces that do not vary in bandwidth or for those where no accurate estimation can be made, this node should contain the nominal bandwidth. For interfaces that have no concept of bandwidth, this node is not present
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bits/second
        
        .. attribute:: statistics
        
        	A collection of interface\-related statistics objects
        	**type**\:   :py:class:`Statistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Statistics>`
        
        .. attribute:: type
        
        	The type of the interface
        	**type**\:   :py:class:`InterfaceType <ydk.models.ietf.ietf_interfaces.InterfaceType>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            super(InterfacesState.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "interfaces-state"

            self.name = YLeaf(YType.str, "name")

            self.admin_status = YLeaf(YType.enumeration, "admin-status")

            self.higher_layer_if = YLeafList(YType.str, "higher-layer-if")

            self.if_index = YLeaf(YType.int32, "if-index")

            self.last_change = YLeaf(YType.str, "last-change")

            self.lower_layer_if = YLeafList(YType.str, "lower-layer-if")

            self.oper_status = YLeaf(YType.enumeration, "oper-status")

            self.phys_address = YLeaf(YType.str, "phys-address")

            self.routing_instance = YLeaf(YType.str, "ietf-routing:routing-instance")

            self.speed = YLeaf(YType.uint64, "speed")

            self.type = YLeaf(YType.identityref, "type")

            self.ipv4 = None
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = None
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.statistics = InterfacesState.Interface.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")

            self.diffserv_target_entry = YList(self)

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
                            "admin_status",
                            "higher_layer_if",
                            "if_index",
                            "last_change",
                            "lower_layer_if",
                            "oper_status",
                            "phys_address",
                            "routing_instance",
                            "speed",
                            "type") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(InterfacesState.Interface, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InterfacesState.Interface, self).__setattr__(name, value)

        class AdminStatus(Enum):
            """
            AdminStatus

            The desired state of the interface.

            This leaf has the same read semantics as ifAdminStatus.

            .. data:: up = 1

            	Ready to pass packets.

            .. data:: down = 2

            	Not ready to pass packets and not in some test mode.

            .. data:: testing = 3

            	In some test mode.

            """

            up = Enum.YLeaf(1, "up")

            down = Enum.YLeaf(2, "down")

            testing = Enum.YLeaf(3, "testing")


        class OperStatus(Enum):
            """
            OperStatus

            The current operational state of the interface.

            This leaf has the same semantics as ifOperStatus.

            .. data:: up = 1

            	Ready to pass packets.

            .. data:: down = 2

            	The interface does not pass any packets.

            .. data:: testing = 3

            	In some test mode.  No operational packets can

            	be passed.

            .. data:: unknown = 4

            	Status cannot be determined for some reason.

            .. data:: dormant = 5

            	Waiting for some external event.

            .. data:: not_present = 6

            	Some component (typically hardware) is missing.

            .. data:: lower_layer_down = 7

            	Down due to state of lower-layer interface(s).

            """

            up = Enum.YLeaf(1, "up")

            down = Enum.YLeaf(2, "down")

            testing = Enum.YLeaf(3, "testing")

            unknown = Enum.YLeaf(4, "unknown")

            dormant = Enum.YLeaf(5, "dormant")

            not_present = Enum.YLeaf(6, "not-present")

            lower_layer_down = Enum.YLeaf(7, "lower-layer-down")



        class Statistics(Entity):
            """
            A collection of interface\-related statistics objects.
            
            .. attribute:: discontinuity_time
            
            	The time on the most recent occasion at which any one or more of this interface's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this node contains the time the local management subsystem re\-initialized itself
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            	**mandatory**\: True
            
            .. attribute:: in_broadcast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_discards
            
            	The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_errors
            
            	For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_multicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_octets
            
            	The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_pkts
            
            	total packets input
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_unicast_pkts
            
            	The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: in_unknown_protos
            
            	For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_broadcast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_discards
            
            	The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_errors
            
            	For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_multicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_octets
            
            	The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_pkts
            
            	total packets output
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: out_unicast_pkts
            
            	The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'if'
            _revision = '2014-05-08'

            def __init__(self):
                super(InterfacesState.Interface.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "interface"

                self.discontinuity_time = YLeaf(YType.str, "discontinuity-time")

                self.in_broadcast_pkts = YLeaf(YType.uint64, "in-broadcast-pkts")

                self.in_discards = YLeaf(YType.uint32, "in-discards")

                self.in_errors = YLeaf(YType.uint32, "in-errors")

                self.in_multicast_pkts = YLeaf(YType.uint64, "in-multicast-pkts")

                self.in_octets = YLeaf(YType.uint64, "in-octets")

                self.in_pkts = YLeaf(YType.uint64, "ietf-interfaces-ext:in-pkts")

                self.in_unicast_pkts = YLeaf(YType.uint64, "in-unicast-pkts")

                self.in_unknown_protos = YLeaf(YType.uint32, "in-unknown-protos")

                self.out_broadcast_pkts = YLeaf(YType.uint64, "out-broadcast-pkts")

                self.out_discards = YLeaf(YType.uint32, "out-discards")

                self.out_errors = YLeaf(YType.uint32, "out-errors")

                self.out_multicast_pkts = YLeaf(YType.uint64, "out-multicast-pkts")

                self.out_octets = YLeaf(YType.uint64, "out-octets")

                self.out_pkts = YLeaf(YType.uint64, "ietf-interfaces-ext:out-pkts")

                self.out_unicast_pkts = YLeaf(YType.uint64, "out-unicast-pkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("discontinuity_time",
                                "in_broadcast_pkts",
                                "in_discards",
                                "in_errors",
                                "in_multicast_pkts",
                                "in_octets",
                                "in_pkts",
                                "in_unicast_pkts",
                                "in_unknown_protos",
                                "out_broadcast_pkts",
                                "out_discards",
                                "out_errors",
                                "out_multicast_pkts",
                                "out_octets",
                                "out_pkts",
                                "out_unicast_pkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InterfacesState.Interface.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfacesState.Interface.Statistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.discontinuity_time.is_set or
                    self.in_broadcast_pkts.is_set or
                    self.in_discards.is_set or
                    self.in_errors.is_set or
                    self.in_multicast_pkts.is_set or
                    self.in_octets.is_set or
                    self.in_pkts.is_set or
                    self.in_unicast_pkts.is_set or
                    self.in_unknown_protos.is_set or
                    self.out_broadcast_pkts.is_set or
                    self.out_discards.is_set or
                    self.out_errors.is_set or
                    self.out_multicast_pkts.is_set or
                    self.out_octets.is_set or
                    self.out_pkts.is_set or
                    self.out_unicast_pkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.discontinuity_time.yfilter != YFilter.not_set or
                    self.in_broadcast_pkts.yfilter != YFilter.not_set or
                    self.in_discards.yfilter != YFilter.not_set or
                    self.in_errors.yfilter != YFilter.not_set or
                    self.in_multicast_pkts.yfilter != YFilter.not_set or
                    self.in_octets.yfilter != YFilter.not_set or
                    self.in_pkts.yfilter != YFilter.not_set or
                    self.in_unicast_pkts.yfilter != YFilter.not_set or
                    self.in_unknown_protos.yfilter != YFilter.not_set or
                    self.out_broadcast_pkts.yfilter != YFilter.not_set or
                    self.out_discards.yfilter != YFilter.not_set or
                    self.out_errors.yfilter != YFilter.not_set or
                    self.out_multicast_pkts.yfilter != YFilter.not_set or
                    self.out_octets.yfilter != YFilter.not_set or
                    self.out_pkts.yfilter != YFilter.not_set or
                    self.out_unicast_pkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.discontinuity_time.is_set or self.discontinuity_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.discontinuity_time.get_name_leafdata())
                if (self.in_broadcast_pkts.is_set or self.in_broadcast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_broadcast_pkts.get_name_leafdata())
                if (self.in_discards.is_set or self.in_discards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_discards.get_name_leafdata())
                if (self.in_errors.is_set or self.in_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_errors.get_name_leafdata())
                if (self.in_multicast_pkts.is_set or self.in_multicast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_multicast_pkts.get_name_leafdata())
                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                if (self.in_pkts.is_set or self.in_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_pkts.get_name_leafdata())
                if (self.in_unicast_pkts.is_set or self.in_unicast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_unicast_pkts.get_name_leafdata())
                if (self.in_unknown_protos.is_set or self.in_unknown_protos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.in_unknown_protos.get_name_leafdata())
                if (self.out_broadcast_pkts.is_set or self.out_broadcast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_broadcast_pkts.get_name_leafdata())
                if (self.out_discards.is_set or self.out_discards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_discards.get_name_leafdata())
                if (self.out_errors.is_set or self.out_errors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_errors.get_name_leafdata())
                if (self.out_multicast_pkts.is_set or self.out_multicast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_multicast_pkts.get_name_leafdata())
                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                if (self.out_pkts.is_set or self.out_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_pkts.get_name_leafdata())
                if (self.out_unicast_pkts.is_set or self.out_unicast_pkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.out_unicast_pkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "discontinuity-time" or name == "in-broadcast-pkts" or name == "in-discards" or name == "in-errors" or name == "in-multicast-pkts" or name == "in-octets" or name == "in-pkts" or name == "in-unicast-pkts" or name == "in-unknown-protos" or name == "out-broadcast-pkts" or name == "out-discards" or name == "out-errors" or name == "out-multicast-pkts" or name == "out-octets" or name == "out-pkts" or name == "out-unicast-pkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "discontinuity-time"):
                    self.discontinuity_time = value
                    self.discontinuity_time.value_namespace = name_space
                    self.discontinuity_time.value_namespace_prefix = name_space_prefix
                if(value_path == "in-broadcast-pkts"):
                    self.in_broadcast_pkts = value
                    self.in_broadcast_pkts.value_namespace = name_space
                    self.in_broadcast_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "in-discards"):
                    self.in_discards = value
                    self.in_discards.value_namespace = name_space
                    self.in_discards.value_namespace_prefix = name_space_prefix
                if(value_path == "in-errors"):
                    self.in_errors = value
                    self.in_errors.value_namespace = name_space
                    self.in_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "in-multicast-pkts"):
                    self.in_multicast_pkts = value
                    self.in_multicast_pkts.value_namespace = name_space
                    self.in_multicast_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "in-octets"):
                    self.in_octets = value
                    self.in_octets.value_namespace = name_space
                    self.in_octets.value_namespace_prefix = name_space_prefix
                if(value_path == "in-pkts"):
                    self.in_pkts = value
                    self.in_pkts.value_namespace = name_space
                    self.in_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "in-unicast-pkts"):
                    self.in_unicast_pkts = value
                    self.in_unicast_pkts.value_namespace = name_space
                    self.in_unicast_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "in-unknown-protos"):
                    self.in_unknown_protos = value
                    self.in_unknown_protos.value_namespace = name_space
                    self.in_unknown_protos.value_namespace_prefix = name_space_prefix
                if(value_path == "out-broadcast-pkts"):
                    self.out_broadcast_pkts = value
                    self.out_broadcast_pkts.value_namespace = name_space
                    self.out_broadcast_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "out-discards"):
                    self.out_discards = value
                    self.out_discards.value_namespace = name_space
                    self.out_discards.value_namespace_prefix = name_space_prefix
                if(value_path == "out-errors"):
                    self.out_errors = value
                    self.out_errors.value_namespace = name_space
                    self.out_errors.value_namespace_prefix = name_space_prefix
                if(value_path == "out-multicast-pkts"):
                    self.out_multicast_pkts = value
                    self.out_multicast_pkts.value_namespace = name_space
                    self.out_multicast_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "out-octets"):
                    self.out_octets = value
                    self.out_octets.value_namespace = name_space
                    self.out_octets.value_namespace_prefix = name_space_prefix
                if(value_path == "out-pkts"):
                    self.out_pkts = value
                    self.out_pkts.value_namespace = name_space
                    self.out_pkts.value_namespace_prefix = name_space_prefix
                if(value_path == "out-unicast-pkts"):
                    self.out_unicast_pkts = value
                    self.out_unicast_pkts.value_namespace = name_space
                    self.out_unicast_pkts.value_namespace_prefix = name_space_prefix


        class DiffservTargetEntry(Entity):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`Direction <ydk.models.ietf.ietf_diffserv_target.Direction>`
            
            .. attribute:: policy_name  <key>
            
            	Policy entry name
            	**type**\:  str
            
            .. attribute:: diffserv_target_classifier_statistics
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of    :py:class:`DiffservTargetClassifierStatistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics>`
            
            

            """

            _prefix = 'target'
            _revision = '2015-04-07'

            def __init__(self):
                super(InterfacesState.Interface.DiffservTargetEntry, self).__init__()

                self.yang_name = "diffserv-target-entry"
                self.yang_parent_name = "interface"

                self.direction = YLeaf(YType.identityref, "direction")

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.diffserv_target_classifier_statistics = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("direction",
                                "policy_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InterfacesState.Interface.DiffservTargetEntry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfacesState.Interface.DiffservTargetEntry, self).__setattr__(name, value)


            class DiffservTargetClassifierStatistics(Entity):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name  <key>
                
                	Classifier Entry Name
                	**type**\:  str
                
                .. attribute:: parent_path  <key>
                
                	Path of the Classifier Entry in a hierarchial policy 
                	**type**\:  str
                
                .. attribute:: classifier_entry_statistics
                
                	 This group defines the classifier filter statistics of  each classifier entry         
                	**type**\:   :py:class:`ClassifierEntryStatistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics>`
                
                .. attribute:: meter_statistics
                
                	Meter statistics
                	**type**\: list of    :py:class:`MeterStatistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics>`
                
                .. attribute:: queuing_statistics
                
                	queue related statistics 
                	**type**\:   :py:class:`QueuingStatistics <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics>`
                
                

                """

                _prefix = 'target'
                _revision = '2015-04-07'

                def __init__(self):
                    super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__init__()

                    self.yang_name = "diffserv-target-classifier-statistics"
                    self.yang_parent_name = "diffserv-target-entry"

                    self.classifier_entry_name = YLeaf(YType.str, "classifier-entry-name")

                    self.parent_path = YLeaf(YType.str, "parent-path")

                    self.classifier_entry_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self._children_name_map["classifier_entry_statistics"] = "classifier-entry-statistics"
                    self._children_yang_names.add("classifier-entry-statistics")

                    self.queuing_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                    self.queuing_statistics.parent = self
                    self._children_name_map["queuing_statistics"] = "queuing-statistics"
                    self._children_yang_names.add("queuing-statistics")

                    self.meter_statistics = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("classifier_entry_name",
                                    "parent_path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__setattr__(name, value)


                class ClassifierEntryStatistics(Entity):
                    """
                    
                    This group defines the classifier filter statistics of 
                    each classifier entry
                           
                    
                    
                    .. attribute:: classified_bytes
                    
                    	 Number of total bytes which filtered   to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_pkts
                    
                    	 Number of total packets which filtered  to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	 Rate of average data flow through the   classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    

                    """

                    _prefix = 'target'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__init__()

                        self.yang_name = "classifier-entry-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.classified_bytes = YLeaf(YType.uint64, "classified-bytes")

                        self.classified_pkts = YLeaf(YType.uint64, "classified-pkts")

                        self.classified_rate = YLeaf(YType.uint64, "classified-rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("classified_bytes",
                                        "classified_pkts",
                                        "classified_rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.classified_bytes.is_set or
                            self.classified_pkts.is_set or
                            self.classified_rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.classified_bytes.yfilter != YFilter.not_set or
                            self.classified_pkts.yfilter != YFilter.not_set or
                            self.classified_rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "classifier-entry-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.classified_bytes.is_set or self.classified_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_bytes.get_name_leafdata())
                        if (self.classified_pkts.is_set or self.classified_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_pkts.get_name_leafdata())
                        if (self.classified_rate.is_set or self.classified_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.classified_rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "classified-bytes" or name == "classified-pkts" or name == "classified-rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "classified-bytes"):
                            self.classified_bytes = value
                            self.classified_bytes.value_namespace = name_space
                            self.classified_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "classified-pkts"):
                            self.classified_pkts = value
                            self.classified_pkts.value_namespace = name_space
                            self.classified_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "classified-rate"):
                            self.classified_rate = value
                            self.classified_rate.value_namespace = name_space
                            self.classified_rate.value_namespace_prefix = name_space_prefix


                class MeterStatistics(Entity):
                    """
                    Meter statistics
                    
                    .. attribute:: meter_id  <key>
                    
                    	Meter Identifier
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: meter_failed_bytes
                    
                    	Bytes of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_pkts
                    
                    	Number of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_bytes
                    
                    	Bytes of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_pkts
                    
                    	Number of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'target'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__init__()

                        self.yang_name = "meter-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.meter_id = YLeaf(YType.uint16, "meter-id")

                        self.meter_failed_bytes = YLeaf(YType.uint64, "meter-failed-bytes")

                        self.meter_failed_pkts = YLeaf(YType.uint64, "meter-failed-pkts")

                        self.meter_succeed_bytes = YLeaf(YType.uint64, "meter-succeed-bytes")

                        self.meter_succeed_pkts = YLeaf(YType.uint64, "meter-succeed-pkts")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("meter_id",
                                        "meter_failed_bytes",
                                        "meter_failed_pkts",
                                        "meter_succeed_bytes",
                                        "meter_succeed_pkts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.meter_id.is_set or
                            self.meter_failed_bytes.is_set or
                            self.meter_failed_pkts.is_set or
                            self.meter_succeed_bytes.is_set or
                            self.meter_succeed_pkts.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.meter_id.yfilter != YFilter.not_set or
                            self.meter_failed_bytes.yfilter != YFilter.not_set or
                            self.meter_failed_pkts.yfilter != YFilter.not_set or
                            self.meter_succeed_bytes.yfilter != YFilter.not_set or
                            self.meter_succeed_pkts.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "meter-statistics" + "[meter-id='" + self.meter_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.meter_id.is_set or self.meter_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_id.get_name_leafdata())
                        if (self.meter_failed_bytes.is_set or self.meter_failed_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_failed_bytes.get_name_leafdata())
                        if (self.meter_failed_pkts.is_set or self.meter_failed_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_failed_pkts.get_name_leafdata())
                        if (self.meter_succeed_bytes.is_set or self.meter_succeed_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_succeed_bytes.get_name_leafdata())
                        if (self.meter_succeed_pkts.is_set or self.meter_succeed_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.meter_succeed_pkts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "meter-id" or name == "meter-failed-bytes" or name == "meter-failed-pkts" or name == "meter-succeed-bytes" or name == "meter-succeed-pkts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "meter-id"):
                            self.meter_id = value
                            self.meter_id.value_namespace = name_space
                            self.meter_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-failed-bytes"):
                            self.meter_failed_bytes = value
                            self.meter_failed_bytes.value_namespace = name_space
                            self.meter_failed_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-failed-pkts"):
                            self.meter_failed_pkts = value
                            self.meter_failed_pkts.value_namespace = name_space
                            self.meter_failed_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-succeed-bytes"):
                            self.meter_succeed_bytes = value
                            self.meter_succeed_bytes.value_namespace = name_space
                            self.meter_succeed_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "meter-succeed-pkts"):
                            self.meter_succeed_pkts = value
                            self.meter_succeed_pkts.value_namespace = name_space
                            self.meter_succeed_pkts.value_namespace_prefix = name_space_prefix


                class QueuingStatistics(Entity):
                    """
                    queue related statistics 
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: wred_stats
                    
                    	Container for WRED statistics
                    	**type**\:   :py:class:`WredStats <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats>`
                    
                    

                    """

                    _prefix = 'target'
                    _revision = '2015-04-07'

                    def __init__(self):
                        super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__init__()

                        self.yang_name = "queuing-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"

                        self.drop_bytes = YLeaf(YType.uint64, "drop-bytes")

                        self.drop_pkts = YLeaf(YType.uint64, "drop-pkts")

                        self.output_bytes = YLeaf(YType.uint64, "output-bytes")

                        self.output_pkts = YLeaf(YType.uint64, "output-pkts")

                        self.queue_size_bytes = YLeaf(YType.uint64, "queue-size-bytes")

                        self.queue_size_pkts = YLeaf(YType.uint64, "queue-size-pkts")

                        self.wred_stats = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                        self.wred_stats.parent = self
                        self._children_name_map["wred_stats"] = "wred-stats"
                        self._children_yang_names.add("wred-stats")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("drop_bytes",
                                        "drop_pkts",
                                        "output_bytes",
                                        "output_pkts",
                                        "queue_size_bytes",
                                        "queue_size_pkts") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__setattr__(name, value)


                    class WredStats(Entity):
                        """
                        Container for WRED statistics
                        
                        .. attribute:: early_drop_bytes
                        
                        	Early drop bytes 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: early_drop_pkts
                        
                        	Early drop packets 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'target'
                        _revision = '2015-04-07'

                        def __init__(self):
                            super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__init__()

                            self.yang_name = "wred-stats"
                            self.yang_parent_name = "queuing-statistics"

                            self.early_drop_bytes = YLeaf(YType.uint64, "early-drop-bytes")

                            self.early_drop_pkts = YLeaf(YType.uint64, "early-drop-pkts")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("early_drop_bytes",
                                            "early_drop_pkts") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.early_drop_bytes.is_set or
                                self.early_drop_pkts.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.early_drop_bytes.yfilter != YFilter.not_set or
                                self.early_drop_pkts.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "wred-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.early_drop_bytes.is_set or self.early_drop_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.early_drop_bytes.get_name_leafdata())
                            if (self.early_drop_pkts.is_set or self.early_drop_pkts.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.early_drop_pkts.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "early-drop-bytes" or name == "early-drop-pkts"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "early-drop-bytes"):
                                self.early_drop_bytes = value
                                self.early_drop_bytes.value_namespace = name_space
                                self.early_drop_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "early-drop-pkts"):
                                self.early_drop_pkts = value
                                self.early_drop_pkts.value_namespace = name_space
                                self.early_drop_pkts.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.drop_bytes.is_set or
                            self.drop_pkts.is_set or
                            self.output_bytes.is_set or
                            self.output_pkts.is_set or
                            self.queue_size_bytes.is_set or
                            self.queue_size_pkts.is_set or
                            (self.wred_stats is not None and self.wred_stats.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.drop_bytes.yfilter != YFilter.not_set or
                            self.drop_pkts.yfilter != YFilter.not_set or
                            self.output_bytes.yfilter != YFilter.not_set or
                            self.output_pkts.yfilter != YFilter.not_set or
                            self.queue_size_bytes.yfilter != YFilter.not_set or
                            self.queue_size_pkts.yfilter != YFilter.not_set or
                            (self.wred_stats is not None and self.wred_stats.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "queuing-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.drop_bytes.is_set or self.drop_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_bytes.get_name_leafdata())
                        if (self.drop_pkts.is_set or self.drop_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.drop_pkts.get_name_leafdata())
                        if (self.output_bytes.is_set or self.output_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_bytes.get_name_leafdata())
                        if (self.output_pkts.is_set or self.output_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_pkts.get_name_leafdata())
                        if (self.queue_size_bytes.is_set or self.queue_size_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.queue_size_bytes.get_name_leafdata())
                        if (self.queue_size_pkts.is_set or self.queue_size_pkts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.queue_size_pkts.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "wred-stats"):
                            if (self.wred_stats is None):
                                self.wred_stats = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                                self.wred_stats.parent = self
                                self._children_name_map["wred_stats"] = "wred-stats"
                            return self.wred_stats

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "wred-stats" or name == "drop-bytes" or name == "drop-pkts" or name == "output-bytes" or name == "output-pkts" or name == "queue-size-bytes" or name == "queue-size-pkts"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "drop-bytes"):
                            self.drop_bytes = value
                            self.drop_bytes.value_namespace = name_space
                            self.drop_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "drop-pkts"):
                            self.drop_pkts = value
                            self.drop_pkts.value_namespace = name_space
                            self.drop_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-bytes"):
                            self.output_bytes = value
                            self.output_bytes.value_namespace = name_space
                            self.output_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-pkts"):
                            self.output_pkts = value
                            self.output_pkts.value_namespace = name_space
                            self.output_pkts.value_namespace_prefix = name_space_prefix
                        if(value_path == "queue-size-bytes"):
                            self.queue_size_bytes = value
                            self.queue_size_bytes.value_namespace = name_space
                            self.queue_size_bytes.value_namespace_prefix = name_space_prefix
                        if(value_path == "queue-size-pkts"):
                            self.queue_size_pkts = value
                            self.queue_size_pkts.value_namespace = name_space
                            self.queue_size_pkts.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.meter_statistics:
                        if (c.has_data()):
                            return True
                    return (
                        self.classifier_entry_name.is_set or
                        self.parent_path.is_set or
                        (self.classifier_entry_statistics is not None and self.classifier_entry_statistics.has_data()) or
                        (self.queuing_statistics is not None and self.queuing_statistics.has_data()))

                def has_operation(self):
                    for c in self.meter_statistics:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.classifier_entry_name.yfilter != YFilter.not_set or
                        self.parent_path.yfilter != YFilter.not_set or
                        (self.classifier_entry_statistics is not None and self.classifier_entry_statistics.has_operation()) or
                        (self.queuing_statistics is not None and self.queuing_statistics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "diffserv-target-classifier-statistics" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + "[parent-path='" + self.parent_path.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.classifier_entry_name.is_set or self.classifier_entry_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.classifier_entry_name.get_name_leafdata())
                    if (self.parent_path.is_set or self.parent_path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parent_path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "classifier-entry-statistics"):
                        if (self.classifier_entry_statistics is None):
                            self.classifier_entry_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                            self.classifier_entry_statistics.parent = self
                            self._children_name_map["classifier_entry_statistics"] = "classifier-entry-statistics"
                        return self.classifier_entry_statistics

                    if (child_yang_name == "meter-statistics"):
                        for c in self.meter_statistics:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.meter_statistics.append(c)
                        return c

                    if (child_yang_name == "queuing-statistics"):
                        if (self.queuing_statistics is None):
                            self.queuing_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                            self.queuing_statistics.parent = self
                            self._children_name_map["queuing_statistics"] = "queuing-statistics"
                        return self.queuing_statistics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "classifier-entry-statistics" or name == "meter-statistics" or name == "queuing-statistics" or name == "classifier-entry-name" or name == "parent-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "classifier-entry-name"):
                        self.classifier_entry_name = value
                        self.classifier_entry_name.value_namespace = name_space
                        self.classifier_entry_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "parent-path"):
                        self.parent_path = value
                        self.parent_path.value_namespace = name_space
                        self.parent_path.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.diffserv_target_classifier_statistics:
                    if (c.has_data()):
                        return True
                return (
                    self.direction.is_set or
                    self.policy_name.is_set)

            def has_operation(self):
                for c in self.diffserv_target_classifier_statistics:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.direction.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-diffserv-target:diffserv-target-entry" + "[direction='" + self.direction.get() + "']" + "[policy-name='" + self.policy_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.direction.get_name_leafdata())
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "diffserv-target-classifier-statistics"):
                    for c in self.diffserv_target_classifier_statistics:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.diffserv_target_classifier_statistics.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "diffserv-target-classifier-statistics" or name == "direction" or name == "policy-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "direction"):
                    self.direction = value
                    self.direction.value_namespace = name_space
                    self.direction.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix


        class Ipv4(Entity):
            """
            Interface\-specific parameters for the IPv4 address family.
            
            .. attribute:: address
            
            	The list of IPv4 addresses on the interface
            	**type**\: list of    :py:class:`Address <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv4.Address>`
            
            .. attribute:: forwarding
            
            	Indicates whether IPv4 packet forwarding is enabled or disabled on this interface
            	**type**\:  bool
            
            .. attribute:: mtu
            
            	The size, in octets, of the largest IPv4 packet that the interface will send and receive
            	**type**\:  int
            
            	**range:** 68..65535
            
            	**units**\: octets
            
            .. attribute:: neighbor
            
            	A list of mappings from IPv4 addresses to link\-layer addresses. This list represents the ARP Cache
            	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv4.Neighbor>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                super(InterfacesState.Interface.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "interface"
                self.is_presence_container = True

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.address = YList(self)
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
                    if name in ("forwarding",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InterfacesState.Interface.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfacesState.Interface.Ipv4, self).__setattr__(name, value)


            class Address(Entity):
                """
                The list of IPv4 addresses on the interface.
                
                .. attribute:: ip  <key>
                
                	The IPv4 address on the interface
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: netmask
                
                	The subnet specified as a netmask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                
                .. attribute:: origin
                
                	The origin of this address
                	**type**\:   :py:class:`IpAddressOrigin <ydk.models.ietf.ietf_ip.IpAddressOrigin>`
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..32
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(InterfacesState.Interface.Ipv4.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "ipv4"

                    self.ip = YLeaf(YType.str, "ip")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "netmask",
                                    "origin",
                                    "prefix_length") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfacesState.Interface.Ipv4.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfacesState.Interface.Ipv4.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.netmask.is_set or
                        self.origin.is_set or
                        self.prefix_length.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.netmask.yfilter != YFilter.not_set or
                        self.origin.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.netmask.get_name_leafdata())
                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.origin.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "netmask" or name == "origin" or name == "prefix-length"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "netmask"):
                        self.netmask = value
                        self.netmask.value_namespace = name_space
                        self.netmask.value_namespace_prefix = name_space_prefix
                    if(value_path == "origin"):
                        self.origin = value
                        self.origin.value_namespace = name_space
                        self.origin.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix


            class Neighbor(Entity):
                """
                A list of mappings from IPv4 addresses to
                link\-layer addresses.
                This list represents the ARP Cache.
                
                .. attribute:: ip  <key>
                
                	The IPv4 address of the neighbor node
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: link_layer_address
                
                	The link\-layer address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: origin
                
                	The origin of this neighbor entry
                	**type**\:   :py:class:`NeighborOrigin <ydk.models.ietf.ietf_ip.NeighborOrigin>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(InterfacesState.Interface.Ipv4.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "ipv4"

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                    self.origin = YLeaf(YType.enumeration, "origin")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "link_layer_address",
                                    "origin") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfacesState.Interface.Ipv4.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfacesState.Interface.Ipv4.Neighbor, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.link_layer_address.is_set or
                        self.origin.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.link_layer_address.yfilter != YFilter.not_set or
                        self.origin.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_layer_address.get_name_leafdata())
                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.origin.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "link-layer-address" or name == "origin"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-layer-address"):
                        self.link_layer_address = value
                        self.link_layer_address.value_namespace = name_space
                        self.link_layer_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "origin"):
                        self.origin = value
                        self.origin.value_namespace = name_space
                        self.origin.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                for c in self.neighbor:
                    if (c.has_data()):
                        return True
                return (
                    self.forwarding.is_set or
                    self.mtu.is_set)

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                for c in self.neighbor:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.forwarding.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-ip:ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.forwarding.is_set or self.forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = InterfacesState.Interface.Ipv4.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                if (child_yang_name == "neighbor"):
                    for c in self.neighbor:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = InterfacesState.Interface.Ipv4.Neighbor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "neighbor" or name == "forwarding" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "forwarding"):
                    self.forwarding = value
                    self.forwarding.value_namespace = name_space
                    self.forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix


        class Ipv6(Entity):
            """
            Parameters for the IPv6 address family.
            
            .. attribute:: address
            
            	The list of IPv6 addresses on the interface
            	**type**\: list of    :py:class:`Address <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Address>`
            
            .. attribute:: forwarding
            
            	Indicates whether IPv6 packet forwarding is enabled or disabled on this interface
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: mtu
            
            	The size, in octets, of the largest IPv6 packet that the interface will send and receive
            	**type**\:  int
            
            	**range:** 1280..4294967295
            
            	**units**\: octets
            
            .. attribute:: neighbor
            
            	A list of mappings from IPv6 addresses to link\-layer addresses. This list represents the Neighbor Cache
            	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Neighbor>`
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                super(InterfacesState.Interface.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "interface"
                self.is_presence_container = True

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint32, "mtu")

                self.address = YList(self)
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
                    if name in ("forwarding",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(InterfacesState.Interface.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(InterfacesState.Interface.Ipv6, self).__setattr__(name, value)


            class Address(Entity):
                """
                The list of IPv6 addresses on the interface.
                
                .. attribute:: ip  <key>
                
                	The IPv6 address on the interface
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: origin
                
                	The origin of this address
                	**type**\:   :py:class:`IpAddressOrigin <ydk.models.ietf.ietf_ip.IpAddressOrigin>`
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..128
                
                	**mandatory**\: True
                
                .. attribute:: status
                
                	The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                	**type**\:   :py:class:`Status <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Address.Status>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(InterfacesState.Interface.Ipv6.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "ipv6"

                    self.ip = YLeaf(YType.str, "ip")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    self.status = YLeaf(YType.enumeration, "status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "origin",
                                    "prefix_length",
                                    "status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfacesState.Interface.Ipv6.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfacesState.Interface.Ipv6.Address, self).__setattr__(name, value)

                class Status(Enum):
                    """
                    Status

                    The status of an address.  Most of the states correspond

                    to states from the IPv6 Stateless Address

                    Autoconfiguration protocol.

                    .. data:: preferred = 0

                    	This is a valid address that can appear as the

                    	destination or source address of a packet.

                    .. data:: deprecated = 1

                    	This is a valid but deprecated address that should

                    	no longer be used as a source address in new

                    	communications, but packets addressed to such an

                    	address are processed as expected.

                    .. data:: invalid = 2

                    	This isn't a valid address, and it shouldn't appear

                    	as the destination or source address of a packet.

                    .. data:: inaccessible = 3

                    	The address is not accessible because the interface

                    	to which this address is assigned is not

                    	operational.

                    .. data:: unknown = 4

                    	The status cannot be determined for some reason.

                    .. data:: tentative = 5

                    	The uniqueness of the address on the link is being

                    	verified.  Addresses in this state should not be

                    	used for general communication and should only be

                    	used to determine the uniqueness of the address.

                    .. data:: duplicate = 6

                    	The address has been determined to be non-unique on

                    	the link and so must not be used.

                    .. data:: optimistic = 7

                    	The address is available for use, subject to

                    	restrictions, while its uniqueness on a link is

                    	being verified.

                    """

                    preferred = Enum.YLeaf(0, "preferred")

                    deprecated = Enum.YLeaf(1, "deprecated")

                    invalid = Enum.YLeaf(2, "invalid")

                    inaccessible = Enum.YLeaf(3, "inaccessible")

                    unknown = Enum.YLeaf(4, "unknown")

                    tentative = Enum.YLeaf(5, "tentative")

                    duplicate = Enum.YLeaf(6, "duplicate")

                    optimistic = Enum.YLeaf(7, "optimistic")


                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.origin.is_set or
                        self.prefix_length.is_set or
                        self.status.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.origin.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        self.status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "address" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.origin.get_name_leafdata())
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())
                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "origin" or name == "prefix-length" or name == "status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "origin"):
                        self.origin = value
                        self.origin.value_namespace = name_space
                        self.origin.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "status"):
                        self.status = value
                        self.status.value_namespace = name_space
                        self.status.value_namespace_prefix = name_space_prefix


            class Neighbor(Entity):
                """
                A list of mappings from IPv6 addresses to
                link\-layer addresses.
                This list represents the Neighbor Cache.
                
                .. attribute:: ip  <key>
                
                	The IPv6 address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: is_router
                
                	Indicates that the neighbor node acts as a router
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: link_layer_address
                
                	The link\-layer address of the neighbor node
                	**type**\:  str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: origin
                
                	The origin of this neighbor entry
                	**type**\:   :py:class:`NeighborOrigin <ydk.models.ietf.ietf_ip.NeighborOrigin>`
                
                .. attribute:: state
                
                	The Neighbor Unreachability Detection state of this entry
                	**type**\:   :py:class:`State <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Neighbor.State>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    super(InterfacesState.Interface.Ipv6.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "ipv6"

                    self.ip = YLeaf(YType.str, "ip")

                    self.is_router = YLeaf(YType.empty, "is-router")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.state = YLeaf(YType.enumeration, "state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ip",
                                    "is_router",
                                    "link_layer_address",
                                    "origin",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(InterfacesState.Interface.Ipv6.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(InterfacesState.Interface.Ipv6.Neighbor, self).__setattr__(name, value)

                class State(Enum):
                    """
                    State

                    The Neighbor Unreachability Detection state of this

                    entry.

                    .. data:: incomplete = 0

                    	Address resolution is in progress, and the link-layer

                    	address of the neighbor has not yet been

                    	determined.

                    .. data:: reachable = 1

                    	Roughly speaking, the neighbor is known to have been

                    	reachable recently (within tens of seconds ago).

                    .. data:: stale = 2

                    	The neighbor is no longer known to be reachable, but

                    	until traffic is sent to the neighbor no attempt

                    	should be made to verify its reachability.

                    .. data:: delay = 3

                    	The neighbor is no longer known to be reachable, and

                    	traffic has recently been sent to the neighbor.

                    	Rather than probe the neighbor immediately, however,

                    	delay sending probes for a short while in order to

                    	give upper-layer protocols a chance to provide

                    	reachability confirmation.

                    .. data:: probe = 4

                    	The neighbor is no longer known to be reachable, and

                    	unicast Neighbor Solicitation probes are being sent

                    	to verify reachability.

                    """

                    incomplete = Enum.YLeaf(0, "incomplete")

                    reachable = Enum.YLeaf(1, "reachable")

                    stale = Enum.YLeaf(2, "stale")

                    delay = Enum.YLeaf(3, "delay")

                    probe = Enum.YLeaf(4, "probe")


                def has_data(self):
                    return (
                        self.ip.is_set or
                        self.is_router.is_set or
                        self.link_layer_address.is_set or
                        self.origin.is_set or
                        self.state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ip.yfilter != YFilter.not_set or
                        self.is_router.yfilter != YFilter.not_set or
                        self.link_layer_address.yfilter != YFilter.not_set or
                        self.origin.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + "[ip='" + self.ip.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ip.is_set or self.ip.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip.get_name_leafdata())
                    if (self.is_router.is_set or self.is_router.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_router.get_name_leafdata())
                    if (self.link_layer_address.is_set or self.link_layer_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.link_layer_address.get_name_leafdata())
                    if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.origin.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ip" or name == "is-router" or name == "link-layer-address" or name == "origin" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ip"):
                        self.ip = value
                        self.ip.value_namespace = name_space
                        self.ip.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-router"):
                        self.is_router = value
                        self.is_router.value_namespace = name_space
                        self.is_router.value_namespace_prefix = name_space_prefix
                    if(value_path == "link-layer-address"):
                        self.link_layer_address = value
                        self.link_layer_address.value_namespace = name_space
                        self.link_layer_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "origin"):
                        self.origin = value
                        self.origin.value_namespace = name_space
                        self.origin.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                for c in self.neighbor:
                    if (c.has_data()):
                        return True
                return (
                    self.forwarding.is_set or
                    self.mtu.is_set)

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                for c in self.neighbor:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.forwarding.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ietf-ip:ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.forwarding.is_set or self.forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = InterfacesState.Interface.Ipv6.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                if (child_yang_name == "neighbor"):
                    for c in self.neighbor:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = InterfacesState.Interface.Ipv6.Neighbor()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.neighbor.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "neighbor" or name == "forwarding" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "forwarding"):
                    self.forwarding = value
                    self.forwarding.value_namespace = name_space
                    self.forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.diffserv_target_entry:
                if (c.has_data()):
                    return True
            for leaf in self.higher_layer_if.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.lower_layer_if.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.name.is_set or
                self.admin_status.is_set or
                self.if_index.is_set or
                self.last_change.is_set or
                self.oper_status.is_set or
                self.phys_address.is_set or
                self.routing_instance.is_set or
                self.speed.is_set or
                self.type.is_set or
                (self.statistics is not None and self.statistics.has_data()) or
                (self.ipv4 is not None) or
                (self.ipv6 is not None))

        def has_operation(self):
            for c in self.diffserv_target_entry:
                if (c.has_operation()):
                    return True
            for leaf in self.higher_layer_if.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.lower_layer_if.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.admin_status.yfilter != YFilter.not_set or
                self.higher_layer_if.yfilter != YFilter.not_set or
                self.if_index.yfilter != YFilter.not_set or
                self.last_change.yfilter != YFilter.not_set or
                self.lower_layer_if.yfilter != YFilter.not_set or
                self.oper_status.yfilter != YFilter.not_set or
                self.phys_address.yfilter != YFilter.not_set or
                self.routing_instance.yfilter != YFilter.not_set or
                self.speed.yfilter != YFilter.not_set or
                self.type.yfilter != YFilter.not_set or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interface" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ietf-interfaces:interfaces-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.admin_status.is_set or self.admin_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.admin_status.get_name_leafdata())
            if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                leaf_name_data.append(self.if_index.get_name_leafdata())
            if (self.last_change.is_set or self.last_change.yfilter != YFilter.not_set):
                leaf_name_data.append(self.last_change.get_name_leafdata())
            if (self.oper_status.is_set or self.oper_status.yfilter != YFilter.not_set):
                leaf_name_data.append(self.oper_status.get_name_leafdata())
            if (self.phys_address.is_set or self.phys_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.phys_address.get_name_leafdata())
            if (self.routing_instance.is_set or self.routing_instance.yfilter != YFilter.not_set):
                leaf_name_data.append(self.routing_instance.get_name_leafdata())
            if (self.speed.is_set or self.speed.yfilter != YFilter.not_set):
                leaf_name_data.append(self.speed.get_name_leafdata())
            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type.get_name_leafdata())

            leaf_name_data.extend(self.higher_layer_if.get_name_leafdata())

            leaf_name_data.extend(self.lower_layer_if.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "diffserv-target-entry"):
                for c in self.diffserv_target_entry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = InterfacesState.Interface.DiffservTargetEntry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.diffserv_target_entry.append(c)
                return c

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = InterfacesState.Interface.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = InterfacesState.Interface.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = InterfacesState.Interface.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diffserv-target-entry" or name == "ipv4" or name == "ipv6" or name == "statistics" or name == "name" or name == "admin-status" or name == "higher-layer-if" or name == "if-index" or name == "last-change" or name == "lower-layer-if" or name == "oper-status" or name == "phys-address" or name == "routing-instance" or name == "speed" or name == "type"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "admin-status"):
                self.admin_status = value
                self.admin_status.value_namespace = name_space
                self.admin_status.value_namespace_prefix = name_space_prefix
            if(value_path == "higher-layer-if"):
                self.higher_layer_if.append(value)
            if(value_path == "if-index"):
                self.if_index = value
                self.if_index.value_namespace = name_space
                self.if_index.value_namespace_prefix = name_space_prefix
            if(value_path == "last-change"):
                self.last_change = value
                self.last_change.value_namespace = name_space
                self.last_change.value_namespace_prefix = name_space_prefix
            if(value_path == "lower-layer-if"):
                self.lower_layer_if.append(value)
            if(value_path == "oper-status"):
                self.oper_status = value
                self.oper_status.value_namespace = name_space
                self.oper_status.value_namespace_prefix = name_space_prefix
            if(value_path == "phys-address"):
                self.phys_address = value
                self.phys_address.value_namespace = name_space
                self.phys_address.value_namespace_prefix = name_space_prefix
            if(value_path == "routing-instance"):
                self.routing_instance = value
                self.routing_instance.value_namespace = name_space
                self.routing_instance.value_namespace_prefix = name_space_prefix
            if(value_path == "speed"):
                self.speed = value
                self.speed.value_namespace = name_space
                self.speed.value_namespace_prefix = name_space_prefix
            if(value_path == "type"):
                self.type = value
                self.type.value_namespace = name_space
                self.type.value_namespace_prefix = name_space_prefix

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
        path_buffer = "ietf-interfaces:interfaces-state" + path_buffer

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

        if (child_yang_name == "interface"):
            for c in self.interface:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = InterfacesState.Interface()
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

    def clone_ptr(self):
        self._top_entity = InterfacesState()
        return self._top_entity

