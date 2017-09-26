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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"interface" : ("interface", Interfaces.Interface)}

        self.interface = YList(self)
        self._segment_path = lambda: "ietf-interfaces:interfaces"

    def __setattr__(self, name, value):
        self._perform_setattr(Interfaces, [], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ipv4" : ("ipv4", Interfaces.Interface.Ipv4), "ipv6" : ("ipv6", Interfaces.Interface.Ipv6)}
            self._child_list_classes = {"diffserv-target-entry" : ("diffserv_target_entry", Interfaces.Interface.DiffservTargetEntry)}

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
            self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "ietf-interfaces:interfaces/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.Interface, ['name', 'description', 'enabled', 'link_up_down_trap_enable', 'type'], name, value)

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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.direction = YLeaf(YType.identityref, "direction")

                self.policy_name = YLeaf(YType.str, "policy-name")
                self._segment_path = lambda: "ietf-diffserv-target:diffserv-target-entry" + "[direction='" + self.direction.get() + "']" + "[policy-name='" + self.policy_name.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.DiffservTargetEntry, ['direction', 'policy_name'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"address" : ("address", Interfaces.Interface.Ipv4.Address), "neighbor" : ("neighbor", Interfaces.Interface.Ipv4.Neighbor)}
                self.is_presence_container = True

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.address = YList(self)
                self.neighbor = YList(self)
                self._segment_path = lambda: "ietf-ip:ipv4"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.Ipv4, ['enabled', 'forwarding', 'mtu'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                    self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv4.Address, ['ip', 'netmask', 'prefix_length'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                    self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv4.Neighbor, ['ip', 'link_layer_address'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"autoconf" : ("autoconf", Interfaces.Interface.Ipv6.Autoconf), "ipv6-router-advertisements" : ("ipv6_router_advertisements", Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements)}
                self._child_list_classes = {"address" : ("address", Interfaces.Interface.Ipv6.Address), "neighbor" : ("neighbor", Interfaces.Interface.Ipv6.Neighbor)}
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
                self._segment_path = lambda: "ietf-ip:ipv6"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.Ipv6, ['dup_addr_detect_transmits', 'enabled', 'forwarding', 'mtu'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                    self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv6.Address, ['ip', 'prefix_length'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.create_global_addresses = YLeaf(YType.boolean, "create-global-addresses")

                    self.create_temporary_addresses = YLeaf(YType.boolean, "create-temporary-addresses")

                    self.temporary_preferred_lifetime = YLeaf(YType.uint32, "temporary-preferred-lifetime")

                    self.temporary_valid_lifetime = YLeaf(YType.uint32, "temporary-valid-lifetime")
                    self._segment_path = lambda: "autoconf"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv6.Autoconf, ['create_global_addresses', 'create_temporary_addresses', 'temporary_preferred_lifetime', 'temporary_valid_lifetime'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"prefix-list" : ("prefix_list", Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "ietf-ipv6-unicast-routing:ipv6-router-advertisements"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements, ['cur_hop_limit', 'default_lifetime', 'link_mtu', 'managed_flag', 'max_rtr_adv_interval', 'min_rtr_adv_interval', 'other_config_flag', 'reachable_time', 'retrans_timer', 'send_advertisements'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"prefix" : ("prefix", Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix)}

                        self.prefix = YList(self)
                        self._segment_path = lambda: "prefix-list"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList, [], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.prefix_spec = YLeaf(YType.str, "prefix-spec")

                            self.autonomous_flag = YLeaf(YType.boolean, "autonomous-flag")

                            self.no_advertise = YLeaf(YType.empty, "no-advertise")

                            self.on_link_flag = YLeaf(YType.boolean, "on-link-flag")

                            self.preferred_lifetime = YLeaf(YType.uint32, "preferred-lifetime")

                            self.valid_lifetime = YLeaf(YType.uint32, "valid-lifetime")
                            self._segment_path = lambda: "prefix" + "[prefix-spec='" + self.prefix_spec.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix, ['prefix_spec', 'autonomous_flag', 'no_advertise', 'on_link_flag', 'preferred_lifetime', 'valid_lifetime'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                    self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ipv6.Neighbor, ['ip', 'link_layer_address'], name, value)

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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"interface" : ("interface", InterfacesState.Interface)}

        self.interface = YList(self)
        self._segment_path = lambda: "ietf-interfaces:interfaces-state"

    def __setattr__(self, name, value):
        self._perform_setattr(InterfacesState, [], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ipv4" : ("ipv4", InterfacesState.Interface.Ipv4), "ipv6" : ("ipv6", InterfacesState.Interface.Ipv6), "statistics" : ("statistics", InterfacesState.Interface.Statistics)}
            self._child_list_classes = {"diffserv-target-entry" : ("diffserv_target_entry", InterfacesState.Interface.DiffservTargetEntry)}

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
            self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "ietf-interfaces:interfaces-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(InterfacesState.Interface, ['name', 'admin_status', 'higher_layer_if', 'if_index', 'last_change', 'lower_layer_if', 'oper_status', 'phys_address', 'routing_instance', 'speed', 'type'], name, value)

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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"diffserv-target-classifier-statistics" : ("diffserv_target_classifier_statistics", InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics)}

                self.direction = YLeaf(YType.identityref, "direction")

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.diffserv_target_classifier_statistics = YList(self)
                self._segment_path = lambda: "ietf-diffserv-target:diffserv-target-entry" + "[direction='" + self.direction.get() + "']" + "[policy-name='" + self.policy_name.get() + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry, ['direction', 'policy_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"classifier-entry-statistics" : ("classifier_entry_statistics", InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics), "queuing-statistics" : ("queuing_statistics", InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics)}
                    self._child_list_classes = {"meter-statistics" : ("meter_statistics", InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics)}

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
                    self._segment_path = lambda: "diffserv-target-classifier-statistics" + "[classifier-entry-name='" + self.classifier_entry_name.get() + "']" + "[parent-path='" + self.parent_path.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics, ['classifier_entry_name', 'parent_path'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.classified_bytes = YLeaf(YType.uint64, "classified-bytes")

                        self.classified_pkts = YLeaf(YType.uint64, "classified-pkts")

                        self.classified_rate = YLeaf(YType.uint64, "classified-rate")
                        self._segment_path = lambda: "classifier-entry-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, ['classified_bytes', 'classified_pkts', 'classified_rate'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.meter_id = YLeaf(YType.uint16, "meter-id")

                        self.meter_failed_bytes = YLeaf(YType.uint64, "meter-failed-bytes")

                        self.meter_failed_pkts = YLeaf(YType.uint64, "meter-failed-pkts")

                        self.meter_succeed_bytes = YLeaf(YType.uint64, "meter-succeed-bytes")

                        self.meter_succeed_pkts = YLeaf(YType.uint64, "meter-succeed-pkts")
                        self._segment_path = lambda: "meter-statistics" + "[meter-id='" + self.meter_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, ['meter_id', 'meter_failed_bytes', 'meter_failed_pkts', 'meter_succeed_bytes', 'meter_succeed_pkts'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"wred-stats" : ("wred_stats", InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "queuing-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, ['drop_bytes', 'drop_pkts', 'output_bytes', 'output_pkts', 'queue_size_bytes', 'queue_size_pkts'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.early_drop_bytes = YLeaf(YType.uint64, "early-drop-bytes")

                            self.early_drop_pkts = YLeaf(YType.uint64, "early-drop-pkts")
                            self._segment_path = lambda: "wred-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, ['early_drop_bytes', 'early_drop_pkts'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"address" : ("address", InterfacesState.Interface.Ipv4.Address), "neighbor" : ("neighbor", InterfacesState.Interface.Ipv4.Neighbor)}
                self.is_presence_container = True

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.address = YList(self)
                self.neighbor = YList(self)
                self._segment_path = lambda: "ietf-ip:ipv4"

            def __setattr__(self, name, value):
                self._perform_setattr(InterfacesState.Interface.Ipv4, ['forwarding', 'mtu'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.netmask = YLeaf(YType.str, "netmask")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                    self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfacesState.Interface.Ipv4.Address, ['ip', 'netmask', 'origin', 'prefix_length'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                    self.origin = YLeaf(YType.enumeration, "origin")
                    self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfacesState.Interface.Ipv4.Neighbor, ['ip', 'link_layer_address', 'origin'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"address" : ("address", InterfacesState.Interface.Ipv6.Address), "neighbor" : ("neighbor", InterfacesState.Interface.Ipv6.Neighbor)}
                self.is_presence_container = True

                self.forwarding = YLeaf(YType.boolean, "forwarding")

                self.mtu = YLeaf(YType.uint32, "mtu")

                self.address = YList(self)
                self.neighbor = YList(self)
                self._segment_path = lambda: "ietf-ip:ipv6"

            def __setattr__(self, name, value):
                self._perform_setattr(InterfacesState.Interface.Ipv6, ['forwarding', 'mtu'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    self.status = YLeaf(YType.enumeration, "status")
                    self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfacesState.Interface.Ipv6.Address, ['ip', 'origin', 'prefix_length', 'status'], name, value)

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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip = YLeaf(YType.str, "ip")

                    self.is_router = YLeaf(YType.empty, "is-router")

                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                    self.origin = YLeaf(YType.enumeration, "origin")

                    self.state = YLeaf(YType.enumeration, "state")
                    self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(InterfacesState.Interface.Ipv6.Neighbor, ['ip', 'is_router', 'link_layer_address', 'origin', 'state'], name, value)

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
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "statistics"

            def __setattr__(self, name, value):
                self._perform_setattr(InterfacesState.Interface.Statistics, ['discontinuity_time', 'in_broadcast_pkts', 'in_discards', 'in_errors', 'in_multicast_pkts', 'in_octets', 'in_pkts', 'in_unicast_pkts', 'in_unknown_protos', 'out_broadcast_pkts', 'out_discards', 'out_errors', 'out_multicast_pkts', 'out_octets', 'out_pkts', 'out_unicast_pkts'], name, value)

    def clone_ptr(self):
        self._top_entity = InterfacesState()
        return self._top_entity

