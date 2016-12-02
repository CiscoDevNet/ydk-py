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
        
        .. attribute:: enabled
        
        	This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.    Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
        	**type**\:  bool
        
        	**default value**\: true
        
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
            self.enabled = None
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


        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.description is not None:
                return True

            if self.enabled is not None:
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
        if not self.is_config():
            return False
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
        
        .. attribute:: higher_layer_if
        
        	A list of references to interfaces layered on top of this interface
        	**type**\:  list of str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
        
        .. attribute:: if_index
        
        	The ifIndex value for the ifEntry represented by this interface
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**mandatory**\: True
        
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
            self.higher_layer_if = YLeafList()
            self.higher_layer_if.parent = self
            self.higher_layer_if.name = 'higher_layer_if'
            self.if_index = None
            self.last_change = None
            self.lower_layer_if = YLeafList()
            self.lower_layer_if.parent = self
            self.lower_layer_if.name = 'lower_layer_if'
            self.oper_status = None
            self.phys_address = None
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
                if not self.is_config():
                    return False
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
                if not self.is_config():
                    return False
                if self.units is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_interfaces as meta
                return meta._meta_table['InterfacesState.Interface.Bandwidth']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-interfaces:interfaces-state/ietf-interfaces:interface[ietf-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.admin_status is not None:
                return True

            if self.bandwidth is not None and self.bandwidth._has_data():
                return True

            if self.higher_layer_if is not None:
                for child in self.higher_layer_if:
                    if child is not None:
                        return True

            if self.if_index is not None:
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
        if not self.is_config():
            return False
        if self.interface is not None:
            for child_ref in self.interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_interfaces as meta
        return meta._meta_table['InterfacesState']['meta_info']


