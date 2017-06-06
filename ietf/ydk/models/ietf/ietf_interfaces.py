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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class InterfaceTypeIdentity(object):
    """
    Base identity from which specific interface types are
    derived.
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['InterfaceTypeIdentity']['meta_info']


class Interfaces(object):
    """
    Interface configuration parameters.
    
    .. attribute:: interface
    
    	The list of configured interfaces on the device.  The operational state of an interface is available in the /interfaces\-state/interface list.  If the configuration of a system\-controlled interface cannot be used by the system (e.g., the interface hardware present does not match the interface type), then the configuration is not applied to the system\-controlled interface shown in the /interfaces\-state/interface list.  If the configuration of a user\-controlled interface cannot be used by the system, the configured interface is not instantiated in the /interfaces\-state/interface list
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        self.interface = YList()
        self.interface.parent = self
        self.interface.name = 'interface'


    class Interface(object):
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
        	**type**\:   :py:class:`LinkUpDownTrapEnableEnum <ydk.models.ietf.ietf_interfaces.Interfaces.Interface.LinkUpDownTrapEnableEnum>`
        
        .. attribute:: type
        
        	The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
        	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            self.parent = None
            self.name = None
            self.description = None
            self.diffserv_target_entry = YList()
            self.diffserv_target_entry.parent = self
            self.diffserv_target_entry.name = 'diffserv_target_entry'
            self.enabled = None
            self.ipv4 = None
            self.ipv6 = None
            self.link_up_down_trap_enable = None
            self.type = None

        class LinkUpDownTrapEnableEnum(Enum):
            """
            LinkUpDownTrapEnableEnum

            Controls whether linkUp/linkDown SNMP notifications

            should be generated for this interface.

            If this node is not configured, the value 'enabled' is

            operationally used by the server for interfaces that do

            not operate on top of any other interface (i.e., there are

            no 'lower\-layer\-if' entries), and 'disabled' otherwise.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.LinkUpDownTrapEnableEnum']



        class DiffservTargetEntry(object):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`DirectionIdentity <ydk.models.ietf.ietf_diffserv_target.DirectionIdentity>`
            
            .. attribute:: policy_name  <key>
            
            	Policy entry name
            	**type**\:  str
            
            

            """

            _prefix = 'target'
            _revision = '2015-04-07'

            def __init__(self):
                self.parent = None
                self.direction = None
                self.policy_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.direction is None:
                    raise YPYModelError('Key property direction is None')
                if self.policy_name is None:
                    raise YPYModelError('Key property policy_name is None')

                return self.parent._common_path +'/ietf-diffserv-target:diffserv-target-entry[ietf-diffserv-target:direction = ' + str(self.direction) + '][ietf-diffserv-target:policy-name = ' + str(self.policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.direction is not None:
                    return True

                if self.policy_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.DiffservTargetEntry']['meta_info']


        class Ipv4(object):
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
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.enabled = None
                self.forwarding = None
                self.mtu = None
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'


            class Address(object):
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
                    self.parent = None
                    self.ip = None
                    self.netmask = None
                    self.prefix_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:address[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.netmask is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv4.Address']['meta_info']


            class Neighbor(object):
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
                    self.parent = None
                    self.ip = None
                    self.link_layer_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:neighbor[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.link_layer_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv4.Neighbor']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ip:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.enabled is not None:
                    return True

                if self.forwarding is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Ipv4']['meta_info']


        class Ipv6(object):
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
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.autoconf = Interfaces.Interface.Ipv6.Autoconf()
                self.autoconf.parent = self
                self.dup_addr_detect_transmits = None
                self.enabled = None
                self.forwarding = None
                self.ipv6_router_advertisements = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements()
                self.ipv6_router_advertisements.parent = self
                self.mtu = None
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'


            class Address(object):
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
                    self.parent = None
                    self.ip = None
                    self.prefix_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:address[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv6.Address']['meta_info']


            class Neighbor(object):
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
                    self.parent = None
                    self.ip = None
                    self.link_layer_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:neighbor[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.link_layer_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv6.Neighbor']['meta_info']


            class Autoconf(object):
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
                    self.parent = None
                    self.create_global_addresses = None
                    self.create_temporary_addresses = None
                    self.temporary_preferred_lifetime = None
                    self.temporary_valid_lifetime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ip:autoconf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.create_global_addresses is not None:
                        return True

                    if self.create_temporary_addresses is not None:
                        return True

                    if self.temporary_preferred_lifetime is not None:
                        return True

                    if self.temporary_valid_lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv6.Autoconf']['meta_info']


            class Ipv6RouterAdvertisements(object):
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
                    self.parent = None
                    self.cur_hop_limit = None
                    self.default_lifetime = None
                    self.link_mtu = None
                    self.managed_flag = None
                    self.max_rtr_adv_interval = None
                    self.min_rtr_adv_interval = None
                    self.other_config_flag = None
                    self.prefix_list = Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList()
                    self.prefix_list.parent = self
                    self.reachable_time = None
                    self.retrans_timer = None
                    self.send_advertisements = None


                class PrefixList(object):
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
                        self.parent = None
                        self.prefix = YList()
                        self.prefix.parent = self
                        self.prefix.name = 'prefix'


                    class Prefix(object):
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
                            self.parent = None
                            self.prefix_spec = None
                            self.autonomous_flag = None
                            self.no_advertise = None
                            self.on_link_flag = None
                            self.preferred_lifetime = None
                            self.valid_lifetime = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.prefix_spec is None:
                                raise YPYModelError('Key property prefix_spec is None')

                            return self.parent._common_path +'/ietf-ipv6-unicast-routing:prefix[ietf-ipv6-unicast-routing:prefix-spec = ' + str(self.prefix_spec) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.prefix_spec is not None:
                                return True

                            if self.autonomous_flag is not None:
                                return True

                            if self.no_advertise is not None:
                                return True

                            if self.on_link_flag is not None:
                                return True

                            if self.preferred_lifetime is not None:
                                return True

                            if self.valid_lifetime is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList.Prefix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-ipv6-unicast-routing:prefix-list'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.prefix is not None:
                            for child_ref in self.prefix:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements.PrefixList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-ipv6-unicast-routing:ipv6-router-advertisements'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cur_hop_limit is not None:
                        return True

                    if self.default_lifetime is not None:
                        return True

                    if self.link_mtu is not None:
                        return True

                    if self.managed_flag is not None:
                        return True

                    if self.max_rtr_adv_interval is not None:
                        return True

                    if self.min_rtr_adv_interval is not None:
                        return True

                    if self.other_config_flag is not None:
                        return True

                    if self.prefix_list is not None and self.prefix_list._has_data():
                        return True

                    if self.reachable_time is not None:
                        return True

                    if self.retrans_timer is not None:
                        return True

                    if self.send_advertisements is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ipv6.Ipv6RouterAdvertisements']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ip:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.autoconf is not None and self.autoconf._has_data():
                    return True

                if self.dup_addr_detect_transmits is not None:
                    return True

                if self.enabled is not None:
                    return True

                if self.forwarding is not None:
                    return True

                if self.ipv6_router_advertisements is not None and self.ipv6_router_advertisements._has_data():
                    return True

                if self.mtu is not None:
                    return True

                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Ipv6']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.description is not None:
                return True

            if self.diffserv_target_entry is not None:
                for child_ref in self.diffserv_target_entry:
                    if child_ref._has_data():
                        return True

            if self.enabled is not None:
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            if self.link_up_down_trap_enable is not None:
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_interfaces as meta
            return meta._meta_table['Interfaces.Interface']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-interfaces:interfaces'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.interface is not None:
            for child_ref in self.interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['Interfaces']['meta_info']


class InterfacesState(object):
    """
    Data nodes for the operational state of interfaces.
    
    .. attribute:: interface
    
    	The list of interfaces on the device.  System\-controlled interfaces created by the system are always present in this list, whether they are configured or not
    	**type**\: list of    :py:class:`Interface <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
    
    

    """

    _prefix = 'if'
    _revision = '2014-05-08'

    def __init__(self):
        self.interface = YList()
        self.interface.parent = self
        self.interface.name = 'interface'


    class Interface(object):
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
        	**type**\:   :py:class:`AdminStatusEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.AdminStatusEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: bandwidth
        
        	Bandwidth data for an interface
        	**type**\:   :py:class:`Bandwidth <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Bandwidth>`
        
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
        	**type**\:   :py:class:`OperStatusEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.OperStatusEnum>`
        
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
        	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'if'
        _revision = '2014-05-08'

        def __init__(self):
            self.parent = None
            self.name = None
            self.admin_status = None
            self.bandwidth = InterfacesState.Interface.Bandwidth()
            self.bandwidth.parent = self
            self.diffserv_target_entry = YList()
            self.diffserv_target_entry.parent = self
            self.diffserv_target_entry.name = 'diffserv_target_entry'
            self.higher_layer_if = YLeafList()
            self.higher_layer_if.parent = self
            self.higher_layer_if.name = 'higher_layer_if'
            self.if_index = None
            self.ipv4 = None
            self.ipv6 = None
            self.last_change = None
            self.lower_layer_if = YLeafList()
            self.lower_layer_if.parent = self
            self.lower_layer_if.name = 'lower_layer_if'
            self.oper_status = None
            self.phys_address = None
            self.routing_instance = None
            self.speed = None
            self.statistics = InterfacesState.Interface.Statistics()
            self.statistics.parent = self
            self.type = None

        class AdminStatusEnum(Enum):
            """
            AdminStatusEnum

            The desired state of the interface.

            This leaf has the same read semantics as ifAdminStatus.

            .. data:: up = 1

            	Ready to pass packets.

            .. data:: down = 2

            	Not ready to pass packets and not in some test mode.

            .. data:: testing = 3

            	In some test mode.

            """

            up = 1

            down = 2

            testing = 3


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.AdminStatusEnum']


        class OperStatusEnum(Enum):
            """
            OperStatusEnum

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

            up = 1

            down = 2

            testing = 3

            unknown = 4

            dormant = 5

            not_present = 6

            lower_layer_down = 7


            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.OperStatusEnum']



        class Statistics(object):
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
                self.parent = None
                self.discontinuity_time = None
                self.in_broadcast_pkts = None
                self.in_discards = None
                self.in_errors = None
                self.in_multicast_pkts = None
                self.in_octets = None
                self.in_pkts = None
                self.in_unicast_pkts = None
                self.in_unknown_protos = None
                self.out_broadcast_pkts = None
                self.out_discards = None
                self.out_errors = None
                self.out_multicast_pkts = None
                self.out_octets = None
                self.out_pkts = None
                self.out_unicast_pkts = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-interfaces:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.discontinuity_time is not None:
                    return True

                if self.in_broadcast_pkts is not None:
                    return True

                if self.in_discards is not None:
                    return True

                if self.in_errors is not None:
                    return True

                if self.in_multicast_pkts is not None:
                    return True

                if self.in_octets is not None:
                    return True

                if self.in_pkts is not None:
                    return True

                if self.in_unicast_pkts is not None:
                    return True

                if self.in_unknown_protos is not None:
                    return True

                if self.out_broadcast_pkts is not None:
                    return True

                if self.out_discards is not None:
                    return True

                if self.out_errors is not None:
                    return True

                if self.out_multicast_pkts is not None:
                    return True

                if self.out_octets is not None:
                    return True

                if self.out_pkts is not None:
                    return True

                if self.out_unicast_pkts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Statistics']['meta_info']


        class DiffservTargetEntry(object):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`DirectionIdentity <ydk.models.ietf.ietf_diffserv_target.DirectionIdentity>`
            
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
                self.parent = None
                self.direction = None
                self.policy_name = None
                self.diffserv_target_classifier_statistics = YList()
                self.diffserv_target_classifier_statistics.parent = self
                self.diffserv_target_classifier_statistics.name = 'diffserv_target_classifier_statistics'


            class DiffservTargetClassifierStatistics(object):
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
                    self.parent = None
                    self.classifier_entry_name = None
                    self.parent_path = None
                    self.classifier_entry_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self.meter_statistics = YList()
                    self.meter_statistics.parent = self
                    self.meter_statistics.name = 'meter_statistics'
                    self.queuing_statistics = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                    self.queuing_statistics.parent = self


                class ClassifierEntryStatistics(object):
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
                        self.parent = None
                        self.classified_bytes = None
                        self.classified_pkts = None
                        self.classified_rate = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-diffserv-target:classifier-entry-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.classified_bytes is not None:
                            return True

                        if self.classified_pkts is not None:
                            return True

                        if self.classified_rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info']


                class MeterStatistics(object):
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
                        self.parent = None
                        self.meter_id = None
                        self.meter_failed_bytes = None
                        self.meter_failed_pkts = None
                        self.meter_succeed_bytes = None
                        self.meter_succeed_pkts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_id is None:
                            raise YPYModelError('Key property meter_id is None')

                        return self.parent._common_path +'/ietf-diffserv-target:meter-statistics[ietf-diffserv-target:meter-id = ' + str(self.meter_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.meter_id is not None:
                            return True

                        if self.meter_failed_bytes is not None:
                            return True

                        if self.meter_failed_pkts is not None:
                            return True

                        if self.meter_succeed_bytes is not None:
                            return True

                        if self.meter_succeed_pkts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics']['meta_info']


                class QueuingStatistics(object):
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
                        self.parent = None
                        self.drop_bytes = None
                        self.drop_pkts = None
                        self.output_bytes = None
                        self.output_pkts = None
                        self.queue_size_bytes = None
                        self.queue_size_pkts = None
                        self.wred_stats = InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                        self.wred_stats.parent = self


                    class WredStats(object):
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
                            self.parent = None
                            self.early_drop_bytes = None
                            self.early_drop_pkts = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-diffserv-target:wred-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.early_drop_bytes is not None:
                                return True

                            if self.early_drop_pkts is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_interfaces as meta
                            return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-diffserv-target:queuing-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.drop_bytes is not None:
                            return True

                        if self.drop_pkts is not None:
                            return True

                        if self.output_bytes is not None:
                            return True

                        if self.output_pkts is not None:
                            return True

                        if self.queue_size_bytes is not None:
                            return True

                        if self.queue_size_pkts is not None:
                            return True

                        if self.wred_stats is not None and self.wred_stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.classifier_entry_name is None:
                        raise YPYModelError('Key property classifier_entry_name is None')
                    if self.parent_path is None:
                        raise YPYModelError('Key property parent_path is None')

                    return self.parent._common_path +'/ietf-diffserv-target:diffserv-target-classifier-statistics[ietf-diffserv-target:classifier-entry-name = ' + str(self.classifier_entry_name) + '][ietf-diffserv-target:parent-path = ' + str(self.parent_path) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.classifier_entry_name is not None:
                        return True

                    if self.parent_path is not None:
                        return True

                    if self.classifier_entry_statistics is not None and self.classifier_entry_statistics._has_data():
                        return True

                    if self.meter_statistics is not None:
                        for child_ref in self.meter_statistics:
                            if child_ref._has_data():
                                return True

                    if self.queuing_statistics is not None and self.queuing_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.direction is None:
                    raise YPYModelError('Key property direction is None')
                if self.policy_name is None:
                    raise YPYModelError('Key property policy_name is None')

                return self.parent._common_path +'/ietf-diffserv-target:diffserv-target-entry[ietf-diffserv-target:direction = ' + str(self.direction) + '][ietf-diffserv-target:policy-name = ' + str(self.policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.direction is not None:
                    return True

                if self.policy_name is not None:
                    return True

                if self.diffserv_target_classifier_statistics is not None:
                    for child_ref in self.diffserv_target_classifier_statistics:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.DiffservTargetEntry']['meta_info']


        class Bandwidth(object):
            """
            Bandwidth data for an interface.
            
            .. attribute:: units
            
            	Units of the bandwidth
            	**type**\:  str
            
            .. attribute:: value
            
            	Raw value for the bandwidth
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'if-ext'

            def __init__(self):
                self.parent = None
                self.units = None
                self.value = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-interfaces-ext:bandwidth'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.units is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Bandwidth']['meta_info']


        class Ipv4(object):
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
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.forwarding = None
                self.mtu = None
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'


            class Address(object):
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
                	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.ietf.ietf_ip.IpAddressOriginEnum>`
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..32
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.netmask = None
                    self.origin = None
                    self.prefix_length = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:address[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.netmask is not None:
                        return True

                    if self.origin is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['InterfacesState.Interface.Ipv4.Address']['meta_info']


            class Neighbor(object):
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
                	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.ietf.ietf_ip.NeighborOriginEnum>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.link_layer_address = None
                    self.origin = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:neighbor[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.link_layer_address is not None:
                        return True

                    if self.origin is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['InterfacesState.Interface.Ipv4.Neighbor']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ip:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.forwarding is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Ipv4']['meta_info']


        class Ipv6(object):
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
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ip'
            _revision = '2014-06-16'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.address = YList()
                self.address.parent = self
                self.address.name = 'address'
                self.forwarding = None
                self.mtu = None
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'


            class Address(object):
                """
                The list of IPv6 addresses on the interface.
                
                .. attribute:: ip  <key>
                
                	The IPv6 address on the interface
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: origin
                
                	The origin of this address
                	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.ietf.ietf_ip.IpAddressOriginEnum>`
                
                .. attribute:: prefix_length
                
                	The length of the subnet prefix
                	**type**\:  int
                
                	**range:** 0..128
                
                	**mandatory**\: True
                
                .. attribute:: status
                
                	The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Address.StatusEnum>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.origin = None
                    self.prefix_length = None
                    self.status = None

                class StatusEnum(Enum):
                    """
                    StatusEnum

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

                    preferred = 0

                    deprecated = 1

                    invalid = 2

                    inaccessible = 3

                    unknown = 4

                    tentative = 5

                    duplicate = 6

                    optimistic = 7


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['InterfacesState.Interface.Ipv6.Address.StatusEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:address[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.origin is not None:
                        return True

                    if self.prefix_length is not None:
                        return True

                    if self.status is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['InterfacesState.Interface.Ipv6.Address']['meta_info']


            class Neighbor(object):
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
                	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.ietf.ietf_ip.NeighborOriginEnum>`
                
                .. attribute:: state
                
                	The Neighbor Unreachability Detection state of this entry
                	**type**\:   :py:class:`StateEnum <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface.Ipv6.Neighbor.StateEnum>`
                
                

                """

                _prefix = 'ip'
                _revision = '2014-06-16'

                def __init__(self):
                    self.parent = None
                    self.ip = None
                    self.is_router = None
                    self.link_layer_address = None
                    self.origin = None
                    self.state = None

                class StateEnum(Enum):
                    """
                    StateEnum

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

                    incomplete = 0

                    reachable = 1

                    stale = 2

                    delay = 3

                    probe = 4


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_interfaces as meta
                        return meta._meta_table['InterfacesState.Interface.Ipv6.Neighbor.StateEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.ip is None:
                        raise YPYModelError('Key property ip is None')

                    return self.parent._common_path +'/ietf-ip:neighbor[ietf-ip:ip = ' + str(self.ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ip is not None:
                        return True

                    if self.is_router is not None:
                        return True

                    if self.link_layer_address is not None:
                        return True

                    if self.origin is not None:
                        return True

                    if self.state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_interfaces as meta
                    return meta._meta_table['InterfacesState.Interface.Ipv6.Neighbor']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-ip:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.address is not None:
                    for child_ref in self.address:
                        if child_ref._has_data():
                            return True

                if self.forwarding is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Ipv6']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces-state/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.admin_status is not None:
                return True

            if self.bandwidth is not None and self.bandwidth._has_data():
                return True

            if self.diffserv_target_entry is not None:
                for child_ref in self.diffserv_target_entry:
                    if child_ref._has_data():
                        return True

            if self.higher_layer_if is not None:
                for child in self.higher_layer_if:
                    if child is not None:
                        return True

            if self.if_index is not None:
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            if self.last_change is not None:
                return True

            if self.lower_layer_if is not None:
                for child in self.lower_layer_if:
                    if child is not None:
                        return True

            if self.oper_status is not None:
                return True

            if self.phys_address is not None:
                return True

            if self.routing_instance is not None:
                return True

            if self.speed is not None:
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_interfaces as meta
            return meta._meta_table['InterfacesState.Interface']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-interfaces:interfaces-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interface is not None:
            for child_ref in self.interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['InterfacesState']['meta_info']


