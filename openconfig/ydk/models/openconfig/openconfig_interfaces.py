""" openconfig_interfaces 

Model for managing network interfaces.

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7223 with an alternate structure
(particularly for operational state data) and with additional
configuration items.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Interfaces(object):
    """
    Top level container for interfaces, including configuration
    and state data.
    
    .. attribute:: interface
    
    	The list of named interfaces on the device
    	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
    
    

    """

    _prefix = 'ocif'
    _revision = '2015-11-20'

    def __init__(self):
        self.interface = YList()
        self.interface.parent = self
        self.interface.name = 'interface'


    class Interface(object):
        """
        The list of named interfaces on the device.
        
        .. attribute:: name  <key>
        
        	References the configured name of the interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
        
        .. attribute:: aggregation
        
        	Options for logical interfaces representing aggregates
        	**type**\:   :py:class:`Aggregation <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation>`
        
        	**presence node**\: True
        
        .. attribute:: config
        
        	Configurable items at the global, physical interface level
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
        
        .. attribute:: ethernet
        
        	Top\-level container for ethernet configuration and state
        	**type**\:   :py:class:`Ethernet <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet>`
        
        .. attribute:: hold_time
        
        	Top\-level container for hold\-time settings to enable dampening advertisements of interface transitions
        	**type**\:   :py:class:`HoldTime <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime>`
        
        .. attribute:: routed_vlan
        
        	Top\-level container for routed vlan interfaces.  These logical interfaces are also known as SVI (switched virtual interface), IRB (integrated routing and bridging), RVI (routed VLAN interface)
        	**type**\:   :py:class:`RoutedVlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan>`
        
        .. attribute:: state
        
        	Operational state data at the global interface level
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State>`
        
        .. attribute:: subinterfaces
        
        	Enclosing container for the list of subinterfaces associated with a physical interface
        	**type**\:   :py:class:`Subinterfaces <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces>`
        
        

        """

        _prefix = 'ocif'
        _revision = '2015-11-20'

        def __init__(self):
            self.parent = None
            self.name = None
            self.aggregation = None
            self.config = Interfaces.Interface.Config()
            self.config.parent = self
            self.ethernet = Interfaces.Interface.Ethernet()
            self.ethernet.parent = self
            self.hold_time = Interfaces.Interface.HoldTime()
            self.hold_time.parent = self
            self.routed_vlan = Interfaces.Interface.RoutedVlan()
            self.routed_vlan.parent = self
            self.state = Interfaces.Interface.State()
            self.state.parent = self
            self.subinterfaces = Interfaces.Interface.Subinterfaces()
            self.subinterfaces.parent = self


        class Config(object):
            """
            Configurable items at the global, physical interface
            level
            
            .. attribute:: description
            
            	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
            	**type**\:  str
            
            .. attribute:: enabled
            
            	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: mtu
            
            	Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default \-\- e.g., 1514 bytes on an Ethernet interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
            	**type**\:  str
            
            .. attribute:: type
            
            	[adapted from IETF interfaces model (RFC 7223)]  The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
            	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ocif'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self.description = None
                self.enabled = None
                self.mtu = None
                self.name = None
                self.type = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-interfaces:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.description is not None:
                    return True

                if self.enabled is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.name is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Config']['meta_info']


        class State(object):
            """
            Operational state data at the global interface level
            
            .. attribute:: admin_status
            
            	[adapted from IETF interfaces model (RFC 7223)]  The desired state of the interface.  In RFC 7223 this leaf has the same read semantics as ifAdminStatus.  Here, it reflects the administrative state as set by enabling or disabling the interface
            	**type**\:   :py:class:`AdminStatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.AdminStatusEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: counters
            
            	A collection of interface\-related statistics objects
            	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.Counters>`
            
            .. attribute:: description
            
            	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
            	**type**\:  str
            
            .. attribute:: enabled
            
            	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: hardware_port
            
            	References the hardware port in the device inventory
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            .. attribute:: ifindex
            
            	System assigned number for each interface.  Corresponds to ifIndex object in SNMP Interface MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_change
            
            	Date and time of the last state change of the interface (e.g., up\-to\-down transition).   This corresponds to the ifLastChange object in the standard interface MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mtu
            
            	Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default \-\- e.g., 1514 bytes on an Ethernet interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
            	**type**\:  str
            
            .. attribute:: oper_status
            
            	[adapted from IETF interfaces model (RFC 7223)]  The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
            	**type**\:   :py:class:`OperStatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.OperStatusEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: type
            
            	[adapted from IETF interfaces model (RFC 7223)]  The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
            	**type**\:   :py:class:`InterfaceTypeIdentity <ydk.models.ietf.ietf_interfaces.InterfaceTypeIdentity>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ocif'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self.admin_status = None
                self.counters = Interfaces.Interface.State.Counters()
                self.counters.parent = self
                self.description = None
                self.enabled = None
                self.hardware_port = None
                self.ifindex = None
                self.last_change = None
                self.mtu = None
                self.name = None
                self.oper_status = None
                self.type = None

            class AdminStatusEnum(Enum):
                """
                AdminStatusEnum

                [adapted from IETF interfaces model (RFC 7223)]

                The desired state of the interface.  In RFC 7223 this leaf

                has the same read semantics as ifAdminStatus.  Here, it

                reflects the administrative state as set by enabling or

                disabling the interface.

                .. data:: UP = 0

                	Ready to pass packets.

                .. data:: DOWN = 1

                	Not ready to pass packets and not in some test mode.

                .. data:: TESTING = 2

                	In some test mode.

                """

                UP = 0

                DOWN = 1

                TESTING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.State.AdminStatusEnum']


            class OperStatusEnum(Enum):
                """
                OperStatusEnum

                [adapted from IETF interfaces model (RFC 7223)]

                The current operational state of the interface.

                This leaf has the same semantics as ifOperStatus.

                .. data:: UP = 1

                	Ready to pass packets.

                .. data:: DOWN = 2

                	The interface does not pass any packets.

                .. data:: TESTING = 3

                	In some test mode.  No operational packets can

                	be passed.

                .. data:: UNKNOWN = 4

                	Status cannot be determined for some reason.

                .. data:: DORMANT = 5

                	Waiting for some external event.

                .. data:: NOT_PRESENT = 6

                	Some component (typically hardware) is missing.

                .. data:: LOWER_LAYER_DOWN = 7

                	Down due to state of lower-layer interface(s).

                """

                UP = 1

                DOWN = 2

                TESTING = 3

                UNKNOWN = 4

                DORMANT = 5

                NOT_PRESENT = 6

                LOWER_LAYER_DOWN = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.State.OperStatusEnum']



            class Counters(object):
                """
                A collection of interface\-related statistics objects.
                
                .. attribute:: in_broadcast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_discards
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_errors
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_multicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]   The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_octets
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_unicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_unknown_protos
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_clear
                
                	Indicates the last time the interface counters were cleared
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: out_broadcast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_discards
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_errors
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_multicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_octets
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_unicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ocif'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.in_broadcast_pkts = None
                    self.in_discards = None
                    self.in_errors = None
                    self.in_multicast_pkts = None
                    self.in_octets = None
                    self.in_unicast_pkts = None
                    self.in_unknown_protos = None
                    self.last_clear = None
                    self.out_broadcast_pkts = None
                    self.out_discards = None
                    self.out_errors = None
                    self.out_multicast_pkts = None
                    self.out_octets = None
                    self.out_unicast_pkts = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-interfaces:counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
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

                    if self.in_unicast_pkts is not None:
                        return True

                    if self.in_unknown_protos is not None:
                        return True

                    if self.last_clear is not None:
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

                    if self.out_unicast_pkts is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.State.Counters']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-interfaces:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.admin_status is not None:
                    return True

                if self.counters is not None and self.counters._has_data():
                    return True

                if self.description is not None:
                    return True

                if self.enabled is not None:
                    return True

                if self.hardware_port is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.last_change is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.name is not None:
                    return True

                if self.oper_status is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.State']['meta_info']


        class HoldTime(object):
            """
            Top\-level container for hold\-time settings to enable
            dampening advertisements of interface transitions.
            
            .. attribute:: config
            
            	Configuration data for interface hold\-time settings
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime.Config>`
            
            .. attribute:: state
            
            	Operational state data for interface hold\-time
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime.State>`
            
            

            """

            _prefix = 'ocif'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self.config = Interfaces.Interface.HoldTime.Config()
                self.config.parent = self
                self.state = Interfaces.Interface.HoldTime.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for interface hold\-time settings.
                
                .. attribute:: down
                
                	Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: up
                
                	Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                

                """

                _prefix = 'ocif'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.down = None
                    self.up = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-interfaces:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.down is not None:
                        return True

                    if self.up is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.HoldTime.Config']['meta_info']


            class State(object):
                """
                Operational state data for interface hold\-time.
                
                .. attribute:: down
                
                	Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: up
                
                	Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                

                """

                _prefix = 'ocif'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.down = None
                    self.up = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-interfaces:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.down is not None:
                        return True

                    if self.up is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.HoldTime.State']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-interfaces:hold-time'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.HoldTime']['meta_info']


        class Subinterfaces(object):
            """
            Enclosing container for the list of subinterfaces associated
            with a physical interface
            
            .. attribute:: subinterface
            
            	The list of subinterfaces (logical interfaces) associated with a physical interface
            	**type**\: list of    :py:class:`Subinterface <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
            
            

            """

            _prefix = 'ocif'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self.subinterface = YList()
                self.subinterface.parent = self
                self.subinterface.name = 'subinterface'


            class Subinterface(object):
                """
                The list of subinterfaces (logical interfaces) associated
                with a physical interface
                
                .. attribute:: index  <key>
                
                	The index number of the subinterface \-\- used to address the logical interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Config>`
                
                .. attribute:: config
                
                	Configurable items at the subinterface level
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Config>`
                
                .. attribute:: ipv4
                
                	Parameters for the IPv4 address family
                	**type**\:   :py:class:`Ipv4 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4>`
                
                	**presence node**\: True
                
                .. attribute:: ipv6
                
                	Parameters for the IPv6 address family
                	**type**\:   :py:class:`Ipv6 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6>`
                
                	**presence node**\: True
                
                .. attribute:: state
                
                	Operational state data for logical interfaces
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State>`
                
                .. attribute:: vlan
                
                	Enclosing container for VLAN interface\-specific data on subinterfaces
                	**type**\:   :py:class:`Vlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan>`
                
                

                """

                _prefix = 'ocif'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.index = None
                    self.config = Interfaces.Interface.Subinterfaces.Subinterface.Config()
                    self.config.parent = self
                    self.ipv4 = None
                    self.ipv6 = None
                    self.state = Interfaces.Interface.Subinterfaces.Subinterface.State()
                    self.state.parent = self
                    self.vlan = Interfaces.Interface.Subinterfaces.Subinterface.Vlan()
                    self.vlan.parent = self


                class Config(object):
                    """
                    Configurable items at the subinterface level
                    
                    .. attribute:: description
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
                    	**type**\:  str
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: index
                    
                    	The index of the subinterface, or logical interface number. On systems with no support for subinterfaces, or not using subinterfaces, this value should default to 0, i.e., the default subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: name
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
                    	**type**\:  str
                    
                    .. attribute:: unnumbered
                    
                    	Indicates that the subinterface is unnumbered, and provides a reference to the subinterface that provides the IP address information (v4, v6 or both) for the current subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'ocif'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.description = None
                        self.enabled = None
                        self.index = None
                        self.name = None
                        self.unnumbered = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-interfaces:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.description is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.index is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.unnumbered is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for logical interfaces
                    
                    .. attribute:: admin_status
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The desired state of the interface.  In RFC 7223 this leaf has the same read semantics as ifAdminStatus.  Here, it reflects the administrative state as set by enabling or disabling the interface
                    	**type**\:   :py:class:`AdminStatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.AdminStatusEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: counters
                    
                    	A collection of interface\-related statistics objects
                    	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.Counters>`
                    
                    .. attribute:: description
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
                    	**type**\:  str
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: ifindex
                    
                    	System assigned number for each interface.  Corresponds to ifIndex object in SNMP Interface MIB
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: index
                    
                    	The index of the subinterface, or logical interface number. On systems with no support for subinterfaces, or not using subinterfaces, this value should default to 0, i.e., the default subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: last_change
                    
                    	Date and time of the last state change of the interface (e.g., up\-to\-down transition).   This corresponds to the ifLastChange object in the standard interface MIB
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
                    	**type**\:  str
                    
                    .. attribute:: oper_status
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
                    	**type**\:   :py:class:`OperStatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.OperStatusEnum>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: unnumbered
                    
                    	Indicates that the subinterface is unnumbered, and provides a reference to the subinterface that provides the IP address information (v4, v6 or both) for the current subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'ocif'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.admin_status = None
                        self.counters = Interfaces.Interface.Subinterfaces.Subinterface.State.Counters()
                        self.counters.parent = self
                        self.description = None
                        self.enabled = None
                        self.ifindex = None
                        self.index = None
                        self.last_change = None
                        self.name = None
                        self.oper_status = None
                        self.unnumbered = None

                    class AdminStatusEnum(Enum):
                        """
                        AdminStatusEnum

                        [adapted from IETF interfaces model (RFC 7223)]

                        The desired state of the interface.  In RFC 7223 this leaf

                        has the same read semantics as ifAdminStatus.  Here, it

                        reflects the administrative state as set by enabling or

                        disabling the interface.

                        .. data:: UP = 0

                        	Ready to pass packets.

                        .. data:: DOWN = 1

                        	Not ready to pass packets and not in some test mode.

                        .. data:: TESTING = 2

                        	In some test mode.

                        """

                        UP = 0

                        DOWN = 1

                        TESTING = 2


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State.AdminStatusEnum']


                    class OperStatusEnum(Enum):
                        """
                        OperStatusEnum

                        [adapted from IETF interfaces model (RFC 7223)]

                        The current operational state of the interface.

                        This leaf has the same semantics as ifOperStatus.

                        .. data:: UP = 1

                        	Ready to pass packets.

                        .. data:: DOWN = 2

                        	The interface does not pass any packets.

                        .. data:: TESTING = 3

                        	In some test mode.  No operational packets can

                        	be passed.

                        .. data:: UNKNOWN = 4

                        	Status cannot be determined for some reason.

                        .. data:: DORMANT = 5

                        	Waiting for some external event.

                        .. data:: NOT_PRESENT = 6

                        	Some component (typically hardware) is missing.

                        .. data:: LOWER_LAYER_DOWN = 7

                        	Down due to state of lower-layer interface(s).

                        """

                        UP = 1

                        DOWN = 2

                        TESTING = 3

                        UNKNOWN = 4

                        DORMANT = 5

                        NOT_PRESENT = 6

                        LOWER_LAYER_DOWN = 7


                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State.OperStatusEnum']



                    class Counters(object):
                        """
                        A collection of interface\-related statistics objects.
                        
                        .. attribute:: in_broadcast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_discards
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_errors
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_multicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]   The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_unicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_unknown_protos
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_clear
                        
                        	Indicates the last time the interface counters were cleared
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: out_broadcast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_discards
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_errors
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_multicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_unicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ocif'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.in_broadcast_pkts = None
                            self.in_discards = None
                            self.in_errors = None
                            self.in_multicast_pkts = None
                            self.in_octets = None
                            self.in_unicast_pkts = None
                            self.in_unknown_protos = None
                            self.last_clear = None
                            self.out_broadcast_pkts = None
                            self.out_discards = None
                            self.out_errors = None
                            self.out_multicast_pkts = None
                            self.out_octets = None
                            self.out_unicast_pkts = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-interfaces:counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
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

                            if self.in_unicast_pkts is not None:
                                return True

                            if self.in_unknown_protos is not None:
                                return True

                            if self.last_clear is not None:
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

                            if self.out_unicast_pkts is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State.Counters']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-interfaces:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.admin_status is not None:
                            return True

                        if self.counters is not None and self.counters._has_data():
                            return True

                        if self.description is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.ifindex is not None:
                            return True

                        if self.index is not None:
                            return True

                        if self.last_change is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.oper_status is not None:
                            return True

                        if self.unnumbered is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.State']['meta_info']


                class Vlan(object):
                    """
                    Enclosing container for VLAN interface\-specific
                    data on subinterfaces
                    
                    .. attribute:: config
                    
                    	Configuration parameters for VLANs
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config>`
                    
                    .. attribute:: state
                    
                    	State variables for VLANs
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State>`
                    
                    

                    """

                    _prefix = 'vlan'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration parameters for VLANs
                        
                        .. attribute:: global_vlan_id
                        
                        	VLAN id for the subinterface \-\- references a global VLAN by name or id
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        
                        ----
                        .. attribute:: vlan_id
                        
                        	VLAN id for the subinterface \-\- specified inline for the case of a local VLAN
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                        
                        
                        ----
                        

                        """

                        _prefix = 'vlan'
                        _revision = '2015-10-09'

                        def __init__(self):
                            self.parent = None
                            self.global_vlan_id = None
                            self.vlan_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-vlan:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.global_vlan_id is not None:
                                return True

                            if self.vlan_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config']['meta_info']


                    class State(object):
                        """
                        State variables for VLANs
                        
                        .. attribute:: global_vlan_id
                        
                        	VLAN id for the subinterface \-\- references a global VLAN by name or id
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        
                        ----
                        .. attribute:: vlan_id
                        
                        	VLAN id for the subinterface \-\- specified inline for the case of a local VLAN
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                        
                        
                        ----
                        

                        """

                        _prefix = 'vlan'
                        _revision = '2015-10-09'

                        def __init__(self):
                            self.parent = None
                            self.global_vlan_id = None
                            self.vlan_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-vlan:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.global_vlan_id is not None:
                                return True

                            if self.vlan_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-vlan:vlan'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Vlan']['meta_info']


                class Ipv4(object):
                    """
                    Parameters for the IPv4 address family.
                    
                    .. attribute:: address
                    
                    	The list of configured IPv4 addresses on the interface
                    	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address>`
                    
                    .. attribute:: config
                    
                    	Top\-level IPv4 configuration data for the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config>`
                    
                    .. attribute:: neighbor
                    
                    	A list of mappings from IPv4 addresses to link\-layer addresses. Entries in this list are used as static entries in the ARP Cache
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor>`
                    
                    .. attribute:: state
                    
                    	Top level IPv4 operational state data
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.address = YList()
                        self.address.parent = self
                        self.address.name = 'address'
                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config()
                        self.config.parent = self
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'
                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State()
                        self.state.parent = self


                    class Address(object):
                        """
                        The list of configured IPv4 addresses on the interface.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each configured IPv4 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for each IPv4 address configured on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State>`
                        
                        .. attribute:: vrrp
                        
                        	Enclosing container for VRRP groups handled by this IP interface
                        	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config()
                            self.config.parent = self
                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State()
                            self.state.parent = self
                            self.vrrp = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp()
                            self.vrrp.parent = self


                        class Config(object):
                            """
                            Configuration data for each configured IPv4
                            address on the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv4 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:config'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Config']['meta_info']


                        class State(object):
                            """
                            Operational state data for each IPv4 address
                            configured on the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv4 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: origin
                            
                            	The origin of this address, e.g., statically configured, assigned by DHCP, etc.
                            	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.openconfig.openconfig_if_ip.IpAddressOriginEnum>`
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.origin = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:state'

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

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.State']['meta_info']


                        class Vrrp(object):
                            """
                            Enclosing container for VRRP groups handled by this
                            IP interface
                            
                            .. attribute:: vrrp_group
                            
                            	List of VRRP groups, keyed by virtual router id
                            	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.vrrp_group = YList()
                                self.vrrp_group.parent = self
                                self.vrrp_group.name = 'vrrp_group'


                            class VrrpGroup(object):
                                """
                                List of VRRP groups, keyed by virtual router id
                                
                                .. attribute:: virtual_router_id  <key>
                                
                                	References the configured virtual router id for this VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration data for the VRRP group
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: interface_tracking
                                
                                	Top\-level container for VRRP interface tracking
                                	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the VRRP group
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State>`
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.virtual_router_id = None
                                    self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config()
                                    self.config.parent = self
                                    self.interface_tracking = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                    self.interface_tracking.parent = self
                                    self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.accept_mode = None
                                        self.advertisement_interval = None
                                        self.preempt = None
                                        self.preempt_delay = None
                                        self.priority = None
                                        self.virtual_address = YLeafList()
                                        self.virtual_address.parent = self
                                        self.virtual_address.name = 'virtual_address'
                                        self.virtual_router_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.accept_mode is not None:
                                            return True

                                        if self.advertisement_interval is not None:
                                            return True

                                        if self.preempt is not None:
                                            return True

                                        if self.preempt_delay is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        if self.virtual_address is not None:
                                            for child in self.virtual_address:
                                                if child is not None:
                                                    return True

                                        if self.virtual_router_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.Config']['meta_info']


                                class State(object):
                                    """
                                    Operational state data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: current_priority
                                    
                                    	Operational value of the priority for the interface in the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.accept_mode = None
                                        self.advertisement_interval = None
                                        self.current_priority = None
                                        self.preempt = None
                                        self.preempt_delay = None
                                        self.priority = None
                                        self.virtual_address = YLeafList()
                                        self.virtual_address.parent = self
                                        self.virtual_address.name = 'virtual_address'
                                        self.virtual_router_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.accept_mode is not None:
                                            return True

                                        if self.advertisement_interval is not None:
                                            return True

                                        if self.current_priority is not None:
                                            return True

                                        if self.preempt is not None:
                                            return True

                                        if self.preempt_delay is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        if self.virtual_address is not None:
                                            for child in self.virtual_address:
                                                if child is not None:
                                                    return True

                                        if self.virtual_router_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.State']['meta_info']


                                class InterfaceTracking(object):
                                    """
                                    Top\-level container for VRRP interface tracking
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for VRRP interface tracking
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for VRRP interface tracking
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                        self.config.parent = self
                                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                        self.state.parent = self


                                    class Config(object):
                                        """
                                        Configuration data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'ocip'
                                        _revision = '2015-11-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.priority_decrement = None
                                            self.track_interface = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-if-ip:config'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.priority_decrement is not None:
                                                return True

                                            if self.track_interface is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info']


                                    class State(object):
                                        """
                                        Operational state data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'ocip'
                                        _revision = '2015-11-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.priority_decrement = None
                                            self.track_interface = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-if-ip:state'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.priority_decrement is not None:
                                                return True

                                            if self.track_interface is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:interface-tracking'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.config is not None and self.config._has_data():
                                            return True

                                        if self.state is not None and self.state._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.virtual_router_id is None:
                                        raise YPYModelError('Key property virtual_router_id is None')

                                    return self.parent._common_path +'/openconfig-if-ip:vrrp-group[openconfig-if-ip:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.virtual_router_id is not None:
                                        return True

                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.interface_tracking is not None and self.interface_tracking._has_data():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:vrrp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vrrp_group is not None:
                                    for child_ref in self.vrrp_group:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address.Vrrp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip is None:
                                raise YPYModelError('Key property ip is None')

                            return self.parent._common_path +'/openconfig-if-ip:address[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ip is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.vrrp is not None and self.vrrp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Address']['meta_info']


                    class Neighbor(object):
                        """
                        A list of mappings from IPv4 addresses to
                        link\-layer addresses.
                        Entries in this list are used as static entries in the
                        ARP Cache.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each configured IPv4 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for each IPv4 address configured on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config()
                            self.config.parent = self
                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration data for each configured IPv4
                            address on the interface
                            
                            .. attribute:: ip
                            
                            	The IPv4 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.link_layer_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:config'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.Config']['meta_info']


                        class State(object):
                            """
                            Operational state data for each IPv4 address
                            configured on the interface
                            
                            .. attribute:: ip
                            
                            	The IPv4 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: origin
                            
                            	The origin of this neighbor entry, static or dynamic
                            	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.openconfig.openconfig_if_ip.NeighborOriginEnum>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.link_layer_address = None
                                self.origin = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:state'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip is None:
                                raise YPYModelError('Key property ip is None')

                            return self.parent._common_path +'/openconfig-if-ip:neighbor[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ip is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbor']['meta_info']


                    class Config(object):
                        """
                        Top\-level IPv4 configuration data for the interface
                        
                        .. attribute:: enabled
                        
                        	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	The size, in octets, of the largest IPv4 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 68..65535
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None
                            self.mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.enabled is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config']['meta_info']


                    class State(object):
                        """
                        Top level IPv4 operational state data
                        
                        .. attribute:: enabled
                        
                        	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	The size, in octets, of the largest IPv4 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 68..65535
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.enabled = None
                            self.mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.enabled is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:ipv4'

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

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv4']['meta_info']


                class Ipv6(object):
                    """
                    Parameters for the IPv6 address family.
                    
                    .. attribute:: address
                    
                    	The list of configured IPv6 addresses on the interface
                    	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address>`
                    
                    .. attribute:: autoconf
                    
                    	Top\-level container for IPv6 autoconf
                    	**type**\:   :py:class:`Autoconf <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf>`
                    
                    .. attribute:: config
                    
                    	Top\-level config data for the IPv6 interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config>`
                    
                    .. attribute:: neighbor
                    
                    	A list of mappings from IPv6 addresses to link\-layer addresses. Entries in this list are used as static entries in the Neighbor Cache
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor>`
                    
                    .. attribute:: state
                    
                    	Top\-level operational state data for the IPv6 interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State>`
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.address = YList()
                        self.address.parent = self
                        self.address.name = 'address'
                        self.autoconf = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf()
                        self.autoconf.parent = self
                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config()
                        self.config.parent = self
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'
                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State()
                        self.state.parent = self


                    class Address(object):
                        """
                        The list of configured IPv6 addresses on the interface.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each IPv6 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config>`
                        
                        .. attribute:: state
                        
                        	State data for each IPv6 address on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State>`
                        
                        .. attribute:: vrrp
                        
                        	Enclosing container for VRRP groups handled by this IP interface
                        	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config()
                            self.config.parent = self
                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State()
                            self.state.parent = self
                            self.vrrp = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp()
                            self.vrrp.parent = self


                        class Config(object):
                            """
                            Configuration data for each IPv6 address on
                            the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv6 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..128
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:config'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Config']['meta_info']


                        class State(object):
                            """
                            State data for each IPv6 address on the
                            interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv6 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: origin
                            
                            	[adapted from IETF IP model RFC 7277] The origin of this address, e.g., static, dhcp, etc
                            	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.openconfig.openconfig_if_ip.IpAddressOriginEnum>`
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..128
                            
                            	**mandatory**\: True
                            
                            .. attribute:: status
                            
                            	[adapted from IETF IP model RFC 7277] The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                            	**type**\:   :py:class:`StatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State.StatusEnum>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.origin = None
                                self.prefix_length = None
                                self.status = None

                            class StatusEnum(Enum):
                                """
                                StatusEnum

                                [adapted from IETF IP model RFC 7277]

                                The status of an address.  Most of the states correspond

                                to states from the IPv6 Stateless Address

                                Autoconfiguration protocol.

                                .. data:: PREFERRED = 0

                                	This is a valid address that can appear as the

                                	destination or source address of a packet.

                                .. data:: DEPRECATED = 1

                                	This is a valid but deprecated address that should

                                	no longer be used as a source address in new

                                	communications, but packets addressed to such an

                                	address are processed as expected.

                                .. data:: INVALID = 2

                                	This isn't a valid address, and it shouldn't appear

                                	as the destination or source address of a packet.

                                .. data:: INACCESSIBLE = 3

                                	The address is not accessible because the interface

                                	to which this address is assigned is not

                                	operational.

                                .. data:: UNKNOWN = 4

                                	The status cannot be determined for some reason.

                                .. data:: TENTATIVE = 5

                                	The uniqueness of the address on the link is being

                                	verified.  Addresses in this state should not be

                                	used for general communication and should only be

                                	used to determine the uniqueness of the address.

                                .. data:: DUPLICATE = 6

                                	The address has been determined to be non-unique on

                                	the link and so must not be used.

                                .. data:: OPTIMISTIC = 7

                                	The address is available for use, subject to

                                	restrictions, while its uniqueness on a link is

                                	being verified.

                                """

                                PREFERRED = 0

                                DEPRECATED = 1

                                INVALID = 2

                                INACCESSIBLE = 3

                                UNKNOWN = 4

                                TENTATIVE = 5

                                DUPLICATE = 6

                                OPTIMISTIC = 7


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State.StatusEnum']


                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:state'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.State']['meta_info']


                        class Vrrp(object):
                            """
                            Enclosing container for VRRP groups handled by this
                            IP interface
                            
                            .. attribute:: vrrp_group
                            
                            	List of VRRP groups, keyed by virtual router id
                            	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.vrrp_group = YList()
                                self.vrrp_group.parent = self
                                self.vrrp_group.name = 'vrrp_group'


                            class VrrpGroup(object):
                                """
                                List of VRRP groups, keyed by virtual router id
                                
                                .. attribute:: virtual_router_id  <key>
                                
                                	References the configured virtual router id for this VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration data for the VRRP group
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: interface_tracking
                                
                                	Top\-level container for VRRP interface tracking
                                	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the VRRP group
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State>`
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.virtual_router_id = None
                                    self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config()
                                    self.config.parent = self
                                    self.interface_tracking = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                    self.interface_tracking.parent = self
                                    self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_link_local
                                    
                                    	For VRRP on IPv6 interfaces, sets the virtual link local address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.accept_mode = None
                                        self.advertisement_interval = None
                                        self.preempt = None
                                        self.preempt_delay = None
                                        self.priority = None
                                        self.virtual_address = YLeafList()
                                        self.virtual_address.parent = self
                                        self.virtual_address.name = 'virtual_address'
                                        self.virtual_link_local = None
                                        self.virtual_router_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.accept_mode is not None:
                                            return True

                                        if self.advertisement_interval is not None:
                                            return True

                                        if self.preempt is not None:
                                            return True

                                        if self.preempt_delay is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        if self.virtual_address is not None:
                                            for child in self.virtual_address:
                                                if child is not None:
                                                    return True

                                        if self.virtual_link_local is not None:
                                            return True

                                        if self.virtual_router_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.Config']['meta_info']


                                class State(object):
                                    """
                                    Operational state data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: current_priority
                                    
                                    	Operational value of the priority for the interface in the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_link_local
                                    
                                    	For VRRP on IPv6 interfaces, sets the virtual link local address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.accept_mode = None
                                        self.advertisement_interval = None
                                        self.current_priority = None
                                        self.preempt = None
                                        self.preempt_delay = None
                                        self.priority = None
                                        self.virtual_address = YLeafList()
                                        self.virtual_address.parent = self
                                        self.virtual_address.name = 'virtual_address'
                                        self.virtual_link_local = None
                                        self.virtual_router_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.accept_mode is not None:
                                            return True

                                        if self.advertisement_interval is not None:
                                            return True

                                        if self.current_priority is not None:
                                            return True

                                        if self.preempt is not None:
                                            return True

                                        if self.preempt_delay is not None:
                                            return True

                                        if self.priority is not None:
                                            return True

                                        if self.virtual_address is not None:
                                            for child in self.virtual_address:
                                                if child is not None:
                                                    return True

                                        if self.virtual_link_local is not None:
                                            return True

                                        if self.virtual_router_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.State']['meta_info']


                                class InterfaceTracking(object):
                                    """
                                    Top\-level container for VRRP interface tracking
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for VRRP interface tracking
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for VRRP interface tracking
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                        self.config.parent = self
                                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                        self.state.parent = self


                                    class Config(object):
                                        """
                                        Configuration data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'ocip'
                                        _revision = '2015-11-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.priority_decrement = None
                                            self.track_interface = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-if-ip:config'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.priority_decrement is not None:
                                                return True

                                            if self.track_interface is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info']


                                    class State(object):
                                        """
                                        Operational state data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'ocip'
                                        _revision = '2015-11-20'

                                        def __init__(self):
                                            self.parent = None
                                            self.priority_decrement = None
                                            self.track_interface = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/openconfig-if-ip:state'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.priority_decrement is not None:
                                                return True

                                            if self.track_interface is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:interface-tracking'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.config is not None and self.config._has_data():
                                            return True

                                        if self.state is not None and self.state._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.virtual_router_id is None:
                                        raise YPYModelError('Key property virtual_router_id is None')

                                    return self.parent._common_path +'/openconfig-if-ip:vrrp-group[openconfig-if-ip:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.virtual_router_id is not None:
                                        return True

                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.interface_tracking is not None and self.interface_tracking._has_data():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:vrrp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.vrrp_group is not None:
                                    for child_ref in self.vrrp_group:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address.Vrrp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip is None:
                                raise YPYModelError('Key property ip is None')

                            return self.parent._common_path +'/openconfig-if-ip:address[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ip is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            if self.vrrp is not None and self.vrrp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Address']['meta_info']


                    class Neighbor(object):
                        """
                        A list of mappings from IPv6 addresses to
                        link\-layer addresses.
                        Entries in this list are used as static entries in the
                        Neighbor Cache.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP neighbor address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each IPv6 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config>`
                        
                        .. attribute:: state
                        
                        	State data for each IPv6 address on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config()
                            self.config.parent = self
                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            Configuration data for each IPv6 address on
                            the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv6 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	[adapted from IETF IP model RFC 7277] The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.link_layer_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:config'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.Config']['meta_info']


                        class State(object):
                            """
                            State data for each IPv6 address on the
                            interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277] The IPv6 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_router
                            
                            	[adapted from IETF IP model RFC 7277] Indicates that the neighbor node acts as a router
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: link_layer_address
                            
                            	[adapted from IETF IP model RFC 7277] The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: neighbor_state
                            
                            	[adapted from IETF IP model RFC 7277] The Neighbor Unreachability Detection state of this entry
                            	**type**\:   :py:class:`NeighborStateEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State.NeighborStateEnum>`
                            
                            .. attribute:: origin
                            
                            	[adapted from IETF IP model RFC 7277] The origin of this neighbor entry
                            	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.openconfig.openconfig_if_ip.NeighborOriginEnum>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.ip = None
                                self.is_router = None
                                self.link_layer_address = None
                                self.neighbor_state = None
                                self.origin = None

                            class NeighborStateEnum(Enum):
                                """
                                NeighborStateEnum

                                [adapted from IETF IP model RFC 7277]

                                The Neighbor Unreachability Detection state of this

                                entry.

                                .. data:: INCOMPLETE = 0

                                	Address resolution is in progress, and the link-layer

                                	     address of the neighbor has not yet been

                                	     determined.

                                .. data:: REACHABLE = 1

                                	Roughly speaking, the neighbor is known to have been

                                	     reachable recently (within tens of seconds ago).

                                .. data:: STALE = 2

                                	The neighbor is no longer known to be reachable, but

                                	     until traffic is sent to the neighbor no attempt

                                	     should be made to verify its reachability.

                                .. data:: DELAY = 3

                                	The neighbor is no longer known to be reachable, and

                                	     traffic has recently been sent to the neighbor.

                                	     Rather than probe the neighbor immediately, however,

                                	     delay sending probes for a short while in order to

                                	     give upper-layer protocols a chance to provide

                                	     reachability confirmation.

                                .. data:: PROBE = 4

                                	The neighbor is no longer known to be reachable, and

                                	     unicast Neighbor Solicitation probes are being sent

                                	     to verify reachability.

                                """

                                INCOMPLETE = 0

                                REACHABLE = 1

                                STALE = 2

                                DELAY = 3

                                PROBE = 4


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State.NeighborStateEnum']


                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-ip:state'

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

                                if self.neighbor_state is not None:
                                    return True

                                if self.origin is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip is None:
                                raise YPYModelError('Key property ip is None')

                            return self.parent._common_path +'/openconfig-if-ip:neighbor[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ip is not None:
                                return True

                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbor']['meta_info']


                    class Config(object):
                        """
                        Top\-level config data for the IPv6 interface
                        
                        .. attribute:: dup_addr_detect_transmits
                        
                        	[adapted from IETF IP model RFC 7277] The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        .. attribute:: enabled
                        
                        	[adapted from IETF IP model RFC 7277] Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	[adapted from IETF IP model RFC 7277] The size, in octets, of the largest IPv6 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 1280..4294967295
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.dup_addr_detect_transmits = None
                            self.enabled = None
                            self.mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.dup_addr_detect_transmits is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config']['meta_info']


                    class State(object):
                        """
                        Top\-level operational state data for the IPv6 interface
                        
                        .. attribute:: dup_addr_detect_transmits
                        
                        	[adapted from IETF IP model RFC 7277] The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        .. attribute:: enabled
                        
                        	[adapted from IETF IP model RFC 7277] Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	[adapted from IETF IP model RFC 7277] The size, in octets, of the largest IPv6 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 1280..4294967295
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.dup_addr_detect_transmits = None
                            self.enabled = None
                            self.mtu = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dup_addr_detect_transmits is not None:
                                return True

                            if self.enabled is not None:
                                return True

                            if self.mtu is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State']['meta_info']


                    class Autoconf(object):
                        """
                        Top\-level container for IPv6 autoconf
                        
                        .. attribute:: config
                        
                        	[adapted from IETF IP model RFC 7277] Parameters to control the autoconfiguration of IPv6 addresses, as described in RFC 4862
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data 
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config()
                            self.config.parent = self
                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State()
                            self.state.parent = self


                        class Config(object):
                            """
                            [adapted from IETF IP model RFC 7277]
                            Parameters to control the autoconfiguration of IPv6
                            addresses, as described in RFC 4862.
                            
                            .. attribute:: create_global_addresses
                            
                            	[adapted from IETF IP model RFC 7277] If enabled, the host creates global addresses as described in RFC 4862
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            .. attribute:: create_temporary_addresses
                            
                            	[adapted from IETF IP model RFC 7277] If enabled, the host creates temporary addresses as described in RFC 4941
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: temporary_preferred_lifetime
                            
                            	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is preferred
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 86400
                            
                            .. attribute:: temporary_valid_lifetime
                            
                            	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is valid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 604800
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

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

                                return self.parent._common_path +'/openconfig-if-ip:config'

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.Config']['meta_info']


                        class State(object):
                            """
                            Operational state data 
                            
                            .. attribute:: create_global_addresses
                            
                            	[adapted from IETF IP model RFC 7277] If enabled, the host creates global addresses as described in RFC 4862
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            .. attribute:: create_temporary_addresses
                            
                            	[adapted from IETF IP model RFC 7277] If enabled, the host creates temporary addresses as described in RFC 4941
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: temporary_preferred_lifetime
                            
                            	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is preferred
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 86400
                            
                            .. attribute:: temporary_valid_lifetime
                            
                            	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is valid
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 604800
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

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

                                return self.parent._common_path +'/openconfig-if-ip:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

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
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:autoconf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.config is not None and self.config._has_data():
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Autoconf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:ipv6'

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

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface.Ipv6']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.index is None:
                        raise YPYModelError('Key property index is None')

                    return self.parent._common_path +'/openconfig-interfaces:subinterface[openconfig-interfaces:index = ' + str(self.index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.index is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.ipv4 is not None and self.ipv4._has_data():
                        return True

                    if self.ipv6 is not None and self.ipv6._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    if self.vlan is not None and self.vlan._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Subinterfaces.Subinterface']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-interfaces:subinterfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subinterface is not None:
                    for child_ref in self.subinterface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Subinterfaces']['meta_info']


        class Ethernet(object):
            """
            Top\-level container for ethernet configuration
            and state
            
            .. attribute:: config
            
            	Configuration data for ethernet interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Config>`
            
            .. attribute:: state
            
            	State variables for Ethernet interfaces
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State>`
            
            .. attribute:: vlan
            
            	Enclosing container for VLAN interface\-specific data on Ethernet interfaces
            	**type**\:   :py:class:`Vlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Vlan>`
            
            

            """

            _prefix = 'eth'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self.config = Interfaces.Interface.Ethernet.Config()
                self.config.parent = self
                self.state = Interfaces.Interface.Ethernet.State()
                self.state.parent = self
                self.vlan = Interfaces.Interface.Ethernet.Vlan()
                self.vlan.parent = self


            class Config(object):
                """
                Configuration data for ethernet interfaces
                
                .. attribute:: aggregate_id
                
                	Specify the logical aggregate interface to which this interface belongs
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: auto_negotiate
                
                	Set to TRUE to request the interface to auto\-negotiate transmission parameters with its peer interface.  When set to FALSE, the transmission parameters are specified manually
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: duplex_mode
                
                	When auto\-negotiate is TRUE, this optionally sets the duplex mode that will be advertised to the peer.  If unspecified, the interface should negotiate the duplex mode directly (typically full\-duplex).  When auto\-negotiate is FALSE, this sets the duplex mode on the interface directly
                	**type**\:   :py:class:`DuplexModeEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Config.DuplexModeEnum>`
                
                .. attribute:: enable_flow_control
                
                	Enable or disable flow control for this interface. Ethernet flow control is a mechanism by which a receiver may send PAUSE frames to a sender to stop transmission for a specified time.  This setting should override auto\-negotiated flow control settings.  If left unspecified, and auto\-negotiate is TRUE, flow control mode is negotiated with the peer interface
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: mac_address
                
                	Assigns a MAC address to the Ethernet interface.  If not specified, the corresponding operational state leaf is expected to show the system\-assigned MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: port_speed
                
                	When auto\-negotiate is TRUE, this optionally sets the port\-speed mode that will be advertised to the peer for negotiation.  If unspecified, it is expected that the interface will select the highest speed available based on negotiation.  When auto\-negotiate is set to FALSE, sets the link speed to a fixed value \-\- supported values are defined by ethernet\-speed identities
                	**type**\:   :py:class:`EthernetSpeedIdentity <ydk.models.openconfig.openconfig_if_ethernet.EthernetSpeedIdentity>`
                
                

                """

                _prefix = 'eth'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.aggregate_id = None
                    self.auto_negotiate = None
                    self.duplex_mode = None
                    self.enable_flow_control = None
                    self.mac_address = None
                    self.port_speed = None

                class DuplexModeEnum(Enum):
                    """
                    DuplexModeEnum

                    When auto\-negotiate is TRUE, this optionally sets the

                    duplex mode that will be advertised to the peer.  If

                    unspecified, the interface should negotiate the duplex mode

                    directly (typically full\-duplex).  When auto\-negotiate is

                    FALSE, this sets the duplex mode on the interface directly.

                    .. data:: FULL = 0

                    	Full duplex mode

                    .. data:: HALF = 1

                    	Half duplex mode

                    """

                    FULL = 0

                    HALF = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ethernet.Config.DuplexModeEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-ethernet:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.aggregate_id is not None:
                        return True

                    if self.auto_negotiate is not None:
                        return True

                    if self.duplex_mode is not None:
                        return True

                    if self.enable_flow_control is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.port_speed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ethernet.Config']['meta_info']


            class State(object):
                """
                State variables for Ethernet interfaces
                
                .. attribute:: aggregate_id
                
                	Specify the logical aggregate interface to which this interface belongs
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: auto_negotiate
                
                	Set to TRUE to request the interface to auto\-negotiate transmission parameters with its peer interface.  When set to FALSE, the transmission parameters are specified manually
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: counters
                
                	Ethernet interface counters
                	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State.Counters>`
                
                .. attribute:: duplex_mode
                
                	When auto\-negotiate is TRUE, this optionally sets the duplex mode that will be advertised to the peer.  If unspecified, the interface should negotiate the duplex mode directly (typically full\-duplex).  When auto\-negotiate is FALSE, this sets the duplex mode on the interface directly
                	**type**\:   :py:class:`DuplexModeEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State.DuplexModeEnum>`
                
                .. attribute:: enable_flow_control
                
                	Enable or disable flow control for this interface. Ethernet flow control is a mechanism by which a receiver may send PAUSE frames to a sender to stop transmission for a specified time.  This setting should override auto\-negotiated flow control settings.  If left unspecified, and auto\-negotiate is TRUE, flow control mode is negotiated with the peer interface
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: hw_mac_address
                
                	Represenets the 'burned\-in',  or system\-assigned, MAC address for the Ethernet interface
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mac_address
                
                	Assigns a MAC address to the Ethernet interface.  If not specified, the corresponding operational state leaf is expected to show the system\-assigned MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: port_speed
                
                	When auto\-negotiate is TRUE, this optionally sets the port\-speed mode that will be advertised to the peer for negotiation.  If unspecified, it is expected that the interface will select the highest speed available based on negotiation.  When auto\-negotiate is set to FALSE, sets the link speed to a fixed value \-\- supported values are defined by ethernet\-speed identities
                	**type**\:   :py:class:`EthernetSpeedIdentity <ydk.models.openconfig.openconfig_if_ethernet.EthernetSpeedIdentity>`
                
                

                """

                _prefix = 'eth'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.aggregate_id = None
                    self.auto_negotiate = None
                    self.counters = Interfaces.Interface.Ethernet.State.Counters()
                    self.counters.parent = self
                    self.duplex_mode = None
                    self.enable_flow_control = None
                    self.hw_mac_address = None
                    self.mac_address = None
                    self.port_speed = None

                class DuplexModeEnum(Enum):
                    """
                    DuplexModeEnum

                    When auto\-negotiate is TRUE, this optionally sets the

                    duplex mode that will be advertised to the peer.  If

                    unspecified, the interface should negotiate the duplex mode

                    directly (typically full\-duplex).  When auto\-negotiate is

                    FALSE, this sets the duplex mode on the interface directly.

                    .. data:: FULL = 0

                    	Full duplex mode

                    .. data:: HALF = 1

                    	Half duplex mode

                    """

                    FULL = 0

                    HALF = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ethernet.State.DuplexModeEnum']



                class Counters(object):
                    """
                    Ethernet interface counters
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_control_frames
                    
                    	MAC layer control frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_pause_frames
                    
                    	MAC layer PAUSE frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_oversize_frames
                    
                    	Number of oversize frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_control_frames
                    
                    	MAC layer control frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_pause_frames
                    
                    	MAC layer PAUSE frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'eth'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.in_8021q_frames = None
                        self.in_crc_errors = None
                        self.in_fragment_frames = None
                        self.in_jabber_frames = None
                        self.in_mac_control_frames = None
                        self.in_mac_pause_frames = None
                        self.in_oversize_frames = None
                        self.out_8021q_frames = None
                        self.out_mac_control_frames = None
                        self.out_mac_pause_frames = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ethernet:counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.in_8021q_frames is not None:
                            return True

                        if self.in_crc_errors is not None:
                            return True

                        if self.in_fragment_frames is not None:
                            return True

                        if self.in_jabber_frames is not None:
                            return True

                        if self.in_mac_control_frames is not None:
                            return True

                        if self.in_mac_pause_frames is not None:
                            return True

                        if self.in_oversize_frames is not None:
                            return True

                        if self.out_8021q_frames is not None:
                            return True

                        if self.out_mac_control_frames is not None:
                            return True

                        if self.out_mac_pause_frames is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ethernet.State.Counters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-ethernet:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aggregate_id is not None:
                        return True

                    if self.auto_negotiate is not None:
                        return True

                    if self.counters is not None and self.counters._has_data():
                        return True

                    if self.duplex_mode is not None:
                        return True

                    if self.enable_flow_control is not None:
                        return True

                    if self.hw_mac_address is not None:
                        return True

                    if self.mac_address is not None:
                        return True

                    if self.port_speed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ethernet.State']['meta_info']


            class Vlan(object):
                """
                Enclosing container for VLAN interface\-specific
                data on Ethernet interfaces
                
                .. attribute:: config
                
                	Configuration parameters for VLANs
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Vlan.Config>`
                
                .. attribute:: state
                
                	State variables for VLANs
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Vlan.State>`
                
                

                """

                _prefix = 'vlan'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.config = Interfaces.Interface.Ethernet.Vlan.Config()
                    self.config.parent = self
                    self.state = Interfaces.Interface.Ethernet.Vlan.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeTypeEnum <ydk.models.openconfig.openconfig_vlan.VlanModeTypeEnum>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'vlan'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.access_vlan = None
                        self.interface_mode = None
                        self.native_vlan = None
                        self.trunk_vlans = YLeafList()
                        self.trunk_vlans.parent = self
                        self.trunk_vlans.name = 'trunk_vlans'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-vlan:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_vlan is not None:
                            return True

                        if self.interface_mode is not None:
                            return True

                        if self.native_vlan is not None:
                            return True

                        if self.trunk_vlans is not None:
                            for child in self.trunk_vlans:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ethernet.Vlan.Config']['meta_info']


                class State(object):
                    """
                    State variables for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeTypeEnum <ydk.models.openconfig.openconfig_vlan.VlanModeTypeEnum>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'vlan'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.access_vlan = None
                        self.interface_mode = None
                        self.native_vlan = None
                        self.trunk_vlans = YLeafList()
                        self.trunk_vlans.parent = self
                        self.trunk_vlans.name = 'trunk_vlans'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-vlan:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.access_vlan is not None:
                            return True

                        if self.interface_mode is not None:
                            return True

                        if self.native_vlan is not None:
                            return True

                        if self.trunk_vlans is not None:
                            for child in self.trunk_vlans:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Ethernet.Vlan.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-vlan:vlan'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Ethernet.Vlan']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-if-ethernet:ethernet'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.vlan is not None and self.vlan._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Ethernet']['meta_info']


        class Aggregation(object):
            """
            Options for logical interfaces representing
            aggregates
            
            .. attribute:: config
            
            	Configuration variables for logical aggregate / LAG interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Config>`
            
            .. attribute:: lacp
            
            	Configuration for LACP protocol operation on the aggregate interface
            	**type**\:   :py:class:`Lacp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp>`
            
            	**presence node**\: True
            
            .. attribute:: state
            
            	Operational state variables for logical aggregate / LAG interfaces
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.State>`
            
            .. attribute:: vlan
            
            	Enclosing container for VLAN interface\-specific data on Ethernet interfaces
            	**type**\:   :py:class:`Vlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Vlan>`
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'lag'
            _revision = '2015-11-20'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.config = Interfaces.Interface.Aggregation.Config()
                self.config.parent = self
                self.lacp = None
                self.state = Interfaces.Interface.Aggregation.State()
                self.state.parent = self
                self.vlan = Interfaces.Interface.Aggregation.Vlan()
                self.vlan.parent = self


            class Config(object):
                """
                Configuration variables for logical aggregate /
                LAG interfaces
                
                .. attribute:: lag_type
                
                	Sets the type of LAG, i.e., how it is configured / maintained
                	**type**\:   :py:class:`AggregationTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.AggregationTypeEnum>`
                
                .. attribute:: min_links
                
                	Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'lag'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.lag_type = None
                    self.min_links = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-aggregate:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lag_type is not None:
                        return True

                    if self.min_links is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Aggregation.Config']['meta_info']


            class State(object):
                """
                Operational state variables for logical
                aggregate / LAG interfaces
                
                .. attribute:: lag_type
                
                	Sets the type of LAG, i.e., how it is configured / maintained
                	**type**\:   :py:class:`AggregationTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.AggregationTypeEnum>`
                
                .. attribute:: members
                
                	List of current member interfaces for the aggregate, expressed as references to existing interfaces
                	**type**\:  list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: min_links
                
                	Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'lag'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self.lag_type = None
                    self.members = YLeafList()
                    self.members.parent = self
                    self.members.name = 'members'
                    self.min_links = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-aggregate:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.lag_type is not None:
                        return True

                    if self.members is not None:
                        for child in self.members:
                            if child is not None:
                                return True

                    if self.min_links is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Aggregation.State']['meta_info']


            class Lacp(object):
                """
                Configuration for LACP protocol operation on the
                aggregate interface
                
                .. attribute:: config
                
                	Configuration data for LACP
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Config>`
                
                .. attribute:: members
                
                	Enclosing container for the list of members interfaces of the aggregate. This list is considered operational state only so is labeled config false and has no config container
                	**type**\:   :py:class:`Members <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Members>`
                
                .. attribute:: state
                
                	Operational state data for LACP
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.State>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'lag'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.config = Interfaces.Interface.Aggregation.Lacp.Config()
                    self.config.parent = self
                    self.members = Interfaces.Interface.Aggregation.Lacp.Members()
                    self.members.parent = self
                    self.state = Interfaces.Interface.Aggregation.Lacp.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for LACP
                    
                    .. attribute:: interval
                    
                    	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                    	**type**\:   :py:class:`LacpPeriodTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpPeriodTypeEnum>`
                    
                    	**default value**\: SLOW
                    
                    .. attribute:: lacp_mode
                    
                    	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                    	**type**\:   :py:class:`LacpActivityTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpActivityTypeEnum>`
                    
                    	**default value**\: ACTIVE
                    
                    .. attribute:: system_id_mac
                    
                    	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: system_priority
                    
                    	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'lag'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.interval = None
                        self.lacp_mode = None
                        self.system_id_mac = None
                        self.system_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-aggregate:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interval is not None:
                            return True

                        if self.lacp_mode is not None:
                            return True

                        if self.system_id_mac is not None:
                            return True

                        if self.system_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for LACP
                    
                    .. attribute:: interval
                    
                    	Set the period between LACP messages \-\- uses the lacp\-period\-type enumeration
                    	**type**\:   :py:class:`LacpPeriodTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpPeriodTypeEnum>`
                    
                    	**default value**\: SLOW
                    
                    .. attribute:: lacp_mode
                    
                    	ACTIVE is to initiate the transmission of LACP packets. PASSIVE is to wait for peer to initiate the transmission of LACP packets
                    	**type**\:   :py:class:`LacpActivityTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpActivityTypeEnum>`
                    
                    	**default value**\: ACTIVE
                    
                    .. attribute:: system_id_mac
                    
                    	The MAC address portion of the node's System ID. This is combined with the system priority to construct the 8\-octet system\-id
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: system_priority
                    
                    	Sytem priority used by the node on this LAG interface. Lower value is higher priority for determining which node is the controlling system
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'lag'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.interval = None
                        self.lacp_mode = None
                        self.system_id_mac = None
                        self.system_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-aggregate:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interval is not None:
                            return True

                        if self.lacp_mode is not None:
                            return True

                        if self.system_id_mac is not None:
                            return True

                        if self.system_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.State']['meta_info']


                class Members(object):
                    """
                    Enclosing container for the list of members interfaces of
                    the aggregate. This list is considered operational state
                    only so is labeled config false and has no config container
                    
                    .. attribute:: member
                    
                    	List of member interfaces and their associated status for a LACP\-controlled aggregate interface.  Member list is not configurable here \-\- each interface indicates items its participation in the LAG
                    	**type**\: list of    :py:class:`Member <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Members.Member>`
                    
                    

                    """

                    _prefix = 'lag'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.member = YList()
                        self.member.parent = self
                        self.member.name = 'member'


                    class Member(object):
                        """
                        List of member interfaces and their associated status for
                        a LACP\-controlled aggregate interface.  Member list is not
                        configurable here \-\- each interface indicates items
                        its participation in the LAG.
                        
                        .. attribute:: interface  <key>
                        
                        	Reference to aggregate member interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`interface <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Members.Member.State>`
                        
                        .. attribute:: state
                        
                        	Operational state data for aggregate members
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Members.Member.State>`
                        
                        

                        """

                        _prefix = 'lag'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.interface = None
                            self.state = Interfaces.Interface.Aggregation.Lacp.Members.Member.State()
                            self.state.parent = self


                        class State(object):
                            """
                            Operational state data for aggregate members
                            
                            .. attribute:: activity
                            
                            	Indicates participant is active or passive
                            	**type**\:   :py:class:`LacpActivityTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpActivityTypeEnum>`
                            
                            .. attribute:: aggregatable
                            
                            	A true value indicates that the participant will allow the link to be used as part of the aggregate. A false value indicates the link should be used as an individual link
                            	**type**\:  bool
                            
                            .. attribute:: collecting
                            
                            	If true, the participant is collecting incoming frames on the link, otherwise false
                            	**type**\:  bool
                            
                            .. attribute:: counters
                            
                            	LACP protocol counters
                            	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters>`
                            
                            .. attribute:: distributing
                            
                            	When true, the participant is distributing outgoing frames; when false, distribution is disabled
                            	**type**\:  bool
                            
                            .. attribute:: interface
                            
                            	Interface member of the LACP aggregate
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: oper_key
                            
                            	Current operational value of the key for the aggregate interface
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: partner_id
                            
                            	MAC address representing the protocol partner's interface system ID
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: partner_key
                            
                            	Operational value of the protocol partner's key
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: synchronization
                            
                            	Indicates whether the participant is in\-sync or out\-of\-sync
                            	**type**\:   :py:class:`LacpSynchronizationTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpSynchronizationTypeEnum>`
                            
                            .. attribute:: system_id
                            
                            	MAC address that defines the local system ID for the aggregate interface
                            	**type**\:  str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: timeout
                            
                            	The timeout type (short or long) used by the participant
                            	**type**\:   :py:class:`LacpTimeoutTypeEnum <ydk.models.openconfig.openconfig_if_aggregate.LacpTimeoutTypeEnum>`
                            
                            

                            """

                            _prefix = 'lag'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.activity = None
                                self.aggregatable = None
                                self.collecting = None
                                self.counters = Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters()
                                self.counters.parent = self
                                self.distributing = None
                                self.interface = None
                                self.oper_key = None
                                self.partner_id = None
                                self.partner_key = None
                                self.synchronization = None
                                self.system_id = None
                                self.timeout = None


                            class Counters(object):
                                """
                                LACP protocol counters
                                
                                .. attribute:: lacp_errors
                                
                                	Number of LACPDU illegal packet errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: lacp_in_pkts
                                
                                	Number of LACPDUs received
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: lacp_out_pkts
                                
                                	Number of LACPDUs transmitted
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: lacp_rx_errors
                                
                                	Number of LACPDU receive packet errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: lacp_tx_errors
                                
                                	Number of LACPDU transmit packet errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: lacp_unknown_errors
                                
                                	Number of LACPDU unknown packet errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'lag'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.lacp_errors = None
                                    self.lacp_in_pkts = None
                                    self.lacp_out_pkts = None
                                    self.lacp_rx_errors = None
                                    self.lacp_tx_errors = None
                                    self.lacp_unknown_errors = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-aggregate:counters'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.lacp_errors is not None:
                                        return True

                                    if self.lacp_in_pkts is not None:
                                        return True

                                    if self.lacp_out_pkts is not None:
                                        return True

                                    if self.lacp_rx_errors is not None:
                                        return True

                                    if self.lacp_tx_errors is not None:
                                        return True

                                    if self.lacp_unknown_errors is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member.State.Counters']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-if-aggregate:state'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.activity is not None:
                                    return True

                                if self.aggregatable is not None:
                                    return True

                                if self.collecting is not None:
                                    return True

                                if self.counters is not None and self.counters._has_data():
                                    return True

                                if self.distributing is not None:
                                    return True

                                if self.interface is not None:
                                    return True

                                if self.oper_key is not None:
                                    return True

                                if self.partner_id is not None:
                                    return True

                                if self.partner_key is not None:
                                    return True

                                if self.synchronization is not None:
                                    return True

                                if self.system_id is not None:
                                    return True

                                if self.timeout is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member.State']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface is None:
                                raise YPYModelError('Key property interface is None')

                            return self.parent._common_path +'/openconfig-if-aggregate:member[openconfig-if-aggregate:interface = ' + str(self.interface) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface is not None:
                                return True

                            if self.state is not None and self.state._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.Members.Member']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-aggregate:members'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.member is not None:
                            for child_ref in self.member:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Aggregation.Lacp.Members']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-aggregate:lacp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.members is not None and self.members._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Aggregation.Lacp']['meta_info']


            class Vlan(object):
                """
                Enclosing container for VLAN interface\-specific
                data on Ethernet interfaces
                
                .. attribute:: config
                
                	Configuration parameters for VLANs
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Vlan.Config>`
                
                .. attribute:: state
                
                	State variables for VLANs
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Vlan.State>`
                
                

                """

                _prefix = 'vlan'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.config = Interfaces.Interface.Aggregation.Vlan.Config()
                    self.config.parent = self
                    self.state = Interfaces.Interface.Aggregation.Vlan.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration parameters for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeTypeEnum <ydk.models.openconfig.openconfig_vlan.VlanModeTypeEnum>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'vlan'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.access_vlan = None
                        self.interface_mode = None
                        self.native_vlan = None
                        self.trunk_vlans = YLeafList()
                        self.trunk_vlans.parent = self
                        self.trunk_vlans.name = 'trunk_vlans'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-vlan:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_vlan is not None:
                            return True

                        if self.interface_mode is not None:
                            return True

                        if self.native_vlan is not None:
                            return True

                        if self.trunk_vlans is not None:
                            for child in self.trunk_vlans:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Aggregation.Vlan.Config']['meta_info']


                class State(object):
                    """
                    State variables for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeTypeEnum <ydk.models.openconfig.openconfig_vlan.VlanModeTypeEnum>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'vlan'
                    _revision = '2015-10-09'

                    def __init__(self):
                        self.parent = None
                        self.access_vlan = None
                        self.interface_mode = None
                        self.native_vlan = None
                        self.trunk_vlans = YLeafList()
                        self.trunk_vlans.parent = self
                        self.trunk_vlans.name = 'trunk_vlans'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-vlan:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.access_vlan is not None:
                            return True

                        if self.interface_mode is not None:
                            return True

                        if self.native_vlan is not None:
                            return True

                        if self.trunk_vlans is not None:
                            for child in self.trunk_vlans:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.Aggregation.Vlan.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-vlan:vlan'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.Aggregation.Vlan']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-if-aggregate:aggregation'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.config is not None and self.config._has_data():
                    return True

                if self.lacp is not None and self.lacp._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                if self.vlan is not None and self.vlan._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.Aggregation']['meta_info']


        class RoutedVlan(object):
            """
            Top\-level container for routed vlan interfaces.  These
            logical interfaces are also known as SVI (switched virtual
            interface), IRB (integrated routing and bridging), RVI
            (routed VLAN interface)
            
            .. attribute:: config
            
            	Configuration data for routed vlan interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Config>`
            
            .. attribute:: ipv4
            
            	Parameters for the IPv4 address family
            	**type**\:   :py:class:`Ipv4 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4>`
            
            	**presence node**\: True
            
            .. attribute:: ipv6
            
            	Parameters for the IPv6 address family
            	**type**\:   :py:class:`Ipv6 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6>`
            
            	**presence node**\: True
            
            .. attribute:: state
            
            	Operational state data 
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.State>`
            
            

            """

            _prefix = 'vlan'
            _revision = '2015-10-09'

            def __init__(self):
                self.parent = None
                self.config = Interfaces.Interface.RoutedVlan.Config()
                self.config.parent = self
                self.ipv4 = None
                self.ipv6 = None
                self.state = Interfaces.Interface.RoutedVlan.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for routed vlan interfaces
                
                .. attribute:: vlan
                
                	References the VLAN for which this IP interface provides routing services \-\- similar to a switch virtual interface (SVI), or integrated routing and bridging interface (IRB) in some implementations
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..65535
                
                
                ----
                	**type**\:  str
                
                
                ----
                

                """

                _prefix = 'vlan'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.vlan = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-vlan:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vlan is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Config']['meta_info']


            class State(object):
                """
                Operational state data 
                
                .. attribute:: vlan
                
                	References the VLAN for which this IP interface provides routing services \-\- similar to a switch virtual interface (SVI), or integrated routing and bridging interface (IRB) in some implementations
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..65535
                
                
                ----
                	**type**\:  str
                
                
                ----
                

                """

                _prefix = 'vlan'
                _revision = '2015-10-09'

                def __init__(self):
                    self.parent = None
                    self.vlan = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-vlan:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vlan is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.RoutedVlan.State']['meta_info']


            class Ipv4(object):
                """
                Parameters for the IPv4 address family.
                
                .. attribute:: address
                
                	The list of configured IPv4 addresses on the interface
                	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address>`
                
                .. attribute:: config
                
                	Top\-level IPv4 configuration data for the interface
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Config>`
                
                .. attribute:: neighbor
                
                	A list of mappings from IPv4 addresses to link\-layer addresses. Entries in this list are used as static entries in the ARP Cache
                	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbor>`
                
                .. attribute:: state
                
                	Top level IPv4 operational state data
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.State>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ocip'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.address = YList()
                    self.address.parent = self
                    self.address.name = 'address'
                    self.config = Interfaces.Interface.RoutedVlan.Ipv4.Config()
                    self.config.parent = self
                    self.neighbor = YList()
                    self.neighbor.parent = self
                    self.neighbor.name = 'neighbor'
                    self.state = Interfaces.Interface.RoutedVlan.Ipv4.State()
                    self.state.parent = self


                class Address(object):
                    """
                    The list of configured IPv4 addresses on the interface.
                    
                    .. attribute:: ip  <key>
                    
                    	References the configured IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for each configured IPv4 address on the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for each IPv4 address configured on the interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.State>`
                    
                    .. attribute:: vrrp
                    
                    	Enclosing container for VRRP groups handled by this IP interface
                    	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp>`
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.config = Interfaces.Interface.RoutedVlan.Ipv4.Address.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.RoutedVlan.Ipv4.Address.State()
                        self.state.parent = self
                        self.vrrp = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp()
                        self.vrrp.parent = self


                    class Config(object):
                        """
                        Configuration data for each configured IPv4
                        address on the interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv4 address on the interface
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data for each IPv4 address
                        configured on the interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv4 address on the interface
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: origin
                        
                        	The origin of this address, e.g., statically configured, assigned by DHCP, etc.
                        	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.openconfig.openconfig_if_ip.IpAddressOriginEnum>`
                        
                        .. attribute:: prefix_length
                        
                        	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.origin = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

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

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.State']['meta_info']


                    class Vrrp(object):
                        """
                        Enclosing container for VRRP groups handled by this
                        IP interface
                        
                        .. attribute:: vrrp_group
                        
                        	List of VRRP groups, keyed by virtual router id
                        	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.vrrp_group = YList()
                            self.vrrp_group.parent = self
                            self.vrrp_group.name = 'vrrp_group'


                        class VrrpGroup(object):
                            """
                            List of VRRP groups, keyed by virtual router id
                            
                            .. attribute:: virtual_router_id  <key>
                            
                            	References the configured virtual router id for this VRRP group
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for the VRRP group
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config>`
                            
                            .. attribute:: interface_tracking
                            
                            	Top\-level container for VRRP interface tracking
                            	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                            
                            .. attribute:: state
                            
                            	Operational state data for the VRRP group
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.virtual_router_id = None
                                self.config = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config()
                                self.config.parent = self
                                self.interface_tracking = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                self.interface_tracking.parent = self
                                self.state = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration data for the VRRP group
                                
                                .. attribute:: accept_mode
                                
                                	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: advertisement_interval
                                
                                	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                	**type**\:  int
                                
                                	**range:** 1..4095
                                
                                	**units**\: centiseconds
                                
                                	**default value**\: 100
                                
                                .. attribute:: preempt
                                
                                	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: preempt_delay
                                
                                	Set the delay the higher priority router waits before preempting
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**default value**\: 0
                                
                                .. attribute:: priority
                                
                                	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                	**type**\:  int
                                
                                	**range:** 1..254
                                
                                	**default value**\: 100
                                
                                .. attribute:: virtual_address
                                
                                	Configure one or more virtual addresses for the VRRP group
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_router_id
                                
                                	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.accept_mode = None
                                    self.advertisement_interval = None
                                    self.preempt = None
                                    self.preempt_delay = None
                                    self.priority = None
                                    self.virtual_address = YLeafList()
                                    self.virtual_address.parent = self
                                    self.virtual_address.name = 'virtual_address'
                                    self.virtual_router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.accept_mode is not None:
                                        return True

                                    if self.advertisement_interval is not None:
                                        return True

                                    if self.preempt is not None:
                                        return True

                                    if self.preempt_delay is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.virtual_address is not None:
                                        for child in self.virtual_address:
                                            if child is not None:
                                                return True

                                    if self.virtual_router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.Config']['meta_info']


                            class State(object):
                                """
                                Operational state data for the VRRP group
                                
                                .. attribute:: accept_mode
                                
                                	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: advertisement_interval
                                
                                	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                	**type**\:  int
                                
                                	**range:** 1..4095
                                
                                	**units**\: centiseconds
                                
                                	**default value**\: 100
                                
                                .. attribute:: current_priority
                                
                                	Operational value of the priority for the interface in the VRRP group
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: preempt
                                
                                	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: preempt_delay
                                
                                	Set the delay the higher priority router waits before preempting
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**default value**\: 0
                                
                                .. attribute:: priority
                                
                                	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                	**type**\:  int
                                
                                	**range:** 1..254
                                
                                	**default value**\: 100
                                
                                .. attribute:: virtual_address
                                
                                	Configure one or more virtual addresses for the VRRP group
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_router_id
                                
                                	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.accept_mode = None
                                    self.advertisement_interval = None
                                    self.current_priority = None
                                    self.preempt = None
                                    self.preempt_delay = None
                                    self.priority = None
                                    self.virtual_address = YLeafList()
                                    self.virtual_address.parent = self
                                    self.virtual_address.name = 'virtual_address'
                                    self.virtual_router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.accept_mode is not None:
                                        return True

                                    if self.advertisement_interval is not None:
                                        return True

                                    if self.current_priority is not None:
                                        return True

                                    if self.preempt is not None:
                                        return True

                                    if self.preempt_delay is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.virtual_address is not None:
                                        for child in self.virtual_address:
                                            if child is not None:
                                                return True

                                    if self.virtual_router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.State']['meta_info']


                            class InterfaceTracking(object):
                                """
                                Top\-level container for VRRP interface tracking
                                
                                .. attribute:: config
                                
                                	Configuration data for VRRP interface tracking
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for VRRP interface tracking
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.config = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                    self.config.parent = self
                                    self.state = Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration data for VRRP interface tracking
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Set the value to subtract from priority when the tracked interface goes down
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: track_interface
                                    
                                    	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.priority_decrement = None
                                        self.track_interface = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.priority_decrement is not None:
                                            return True

                                        if self.track_interface is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info']


                                class State(object):
                                    """
                                    Operational state data for VRRP interface tracking
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Set the value to subtract from priority when the tracked interface goes down
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: track_interface
                                    
                                    	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.priority_decrement = None
                                        self.track_interface = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.priority_decrement is not None:
                                            return True

                                        if self.track_interface is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:interface-tracking'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.virtual_router_id is None:
                                    raise YPYModelError('Key property virtual_router_id is None')

                                return self.parent._common_path +'/openconfig-if-ip:vrrp-group[openconfig-if-ip:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.virtual_router_id is not None:
                                    return True

                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.interface_tracking is not None and self.interface_tracking._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp.VrrpGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:vrrp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vrrp_group is not None:
                                for child_ref in self.vrrp_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address.Vrrp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')

                        return self.parent._common_path +'/openconfig-if-ip:address[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.vrrp is not None and self.vrrp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Address']['meta_info']


                class Neighbor(object):
                    """
                    A list of mappings from IPv4 addresses to
                    link\-layer addresses.
                    Entries in this list are used as static entries in the
                    ARP Cache.
                    
                    .. attribute:: ip  <key>
                    
                    	References the configured IP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for each configured IPv4 address on the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for each IPv4 address configured on the interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State>`
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.config = Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration data for each configured IPv4
                        address on the interface
                        
                        .. attribute:: ip
                        
                        	The IPv4 address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: link_layer_address
                        
                        	The link\-layer address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.link_layer_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data for each IPv4 address
                        configured on the interface
                        
                        .. attribute:: ip
                        
                        	The IPv4 address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: link_layer_address
                        
                        	The link\-layer address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: origin
                        
                        	The origin of this neighbor entry, static or dynamic
                        	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.openconfig.openconfig_if_ip.NeighborOriginEnum>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.link_layer_address = None
                            self.origin = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')

                        return self.parent._common_path +'/openconfig-if-ip:neighbor[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Neighbor']['meta_info']


                class Config(object):
                    """
                    Top\-level IPv4 configuration data for the interface
                    
                    .. attribute:: enabled
                    
                    	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	The size, in octets, of the largest IPv4 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 68..65535
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enabled is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.Config']['meta_info']


                class State(object):
                    """
                    Top level IPv4 operational state data
                    
                    .. attribute:: enabled
                    
                    	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	The size, in octets, of the largest IPv4 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 68..65535
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.enabled = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.enabled is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-ip:ipv4'

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

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.neighbor is not None:
                        for child_ref in self.neighbor:
                            if child_ref._has_data():
                                return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv4']['meta_info']


            class Ipv6(object):
                """
                Parameters for the IPv6 address family.
                
                .. attribute:: address
                
                	The list of configured IPv6 addresses on the interface
                	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address>`
                
                .. attribute:: autoconf
                
                	Top\-level container for IPv6 autoconf
                	**type**\:   :py:class:`Autoconf <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Autoconf>`
                
                .. attribute:: config
                
                	Top\-level config data for the IPv6 interface
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Config>`
                
                .. attribute:: neighbor
                
                	A list of mappings from IPv6 addresses to link\-layer addresses. Entries in this list are used as static entries in the Neighbor Cache
                	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbor>`
                
                .. attribute:: state
                
                	Top\-level operational state data for the IPv6 interface
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.State>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ocip'
                _revision = '2015-11-20'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.address = YList()
                    self.address.parent = self
                    self.address.name = 'address'
                    self.autoconf = Interfaces.Interface.RoutedVlan.Ipv6.Autoconf()
                    self.autoconf.parent = self
                    self.config = Interfaces.Interface.RoutedVlan.Ipv6.Config()
                    self.config.parent = self
                    self.neighbor = YList()
                    self.neighbor.parent = self
                    self.neighbor.name = 'neighbor'
                    self.state = Interfaces.Interface.RoutedVlan.Ipv6.State()
                    self.state.parent = self


                class Address(object):
                    """
                    The list of configured IPv6 addresses on the interface.
                    
                    .. attribute:: ip  <key>
                    
                    	References the configured IP address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for each IPv6 address on the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Config>`
                    
                    .. attribute:: state
                    
                    	State data for each IPv6 address on the interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.State>`
                    
                    .. attribute:: vrrp
                    
                    	Enclosing container for VRRP groups handled by this IP interface
                    	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp>`
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.config = Interfaces.Interface.RoutedVlan.Ipv6.Address.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.RoutedVlan.Ipv6.Address.State()
                        self.state.parent = self
                        self.vrrp = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp()
                        self.vrrp.parent = self


                    class Config(object):
                        """
                        Configuration data for each IPv6 address on
                        the interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv6 address on the interface
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Config']['meta_info']


                    class State(object):
                        """
                        State data for each IPv6 address on the
                        interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv6 address on the interface
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: origin
                        
                        	[adapted from IETF IP model RFC 7277] The origin of this address, e.g., static, dhcp, etc
                        	**type**\:   :py:class:`IpAddressOriginEnum <ydk.models.openconfig.openconfig_if_ip.IpAddressOriginEnum>`
                        
                        .. attribute:: prefix_length
                        
                        	[adapted from IETF IP model RFC 7277] The length of the subnet prefix
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        	**mandatory**\: True
                        
                        .. attribute:: status
                        
                        	[adapted from IETF IP model RFC 7277] The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                        	**type**\:   :py:class:`StatusEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.State.StatusEnum>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.origin = None
                            self.prefix_length = None
                            self.status = None

                        class StatusEnum(Enum):
                            """
                            StatusEnum

                            [adapted from IETF IP model RFC 7277]

                            The status of an address.  Most of the states correspond

                            to states from the IPv6 Stateless Address

                            Autoconfiguration protocol.

                            .. data:: PREFERRED = 0

                            	This is a valid address that can appear as the

                            	destination or source address of a packet.

                            .. data:: DEPRECATED = 1

                            	This is a valid but deprecated address that should

                            	no longer be used as a source address in new

                            	communications, but packets addressed to such an

                            	address are processed as expected.

                            .. data:: INVALID = 2

                            	This isn't a valid address, and it shouldn't appear

                            	as the destination or source address of a packet.

                            .. data:: INACCESSIBLE = 3

                            	The address is not accessible because the interface

                            	to which this address is assigned is not

                            	operational.

                            .. data:: UNKNOWN = 4

                            	The status cannot be determined for some reason.

                            .. data:: TENTATIVE = 5

                            	The uniqueness of the address on the link is being

                            	verified.  Addresses in this state should not be

                            	used for general communication and should only be

                            	used to determine the uniqueness of the address.

                            .. data:: DUPLICATE = 6

                            	The address has been determined to be non-unique on

                            	the link and so must not be used.

                            .. data:: OPTIMISTIC = 7

                            	The address is available for use, subject to

                            	restrictions, while its uniqueness on a link is

                            	being verified.

                            """

                            PREFERRED = 0

                            DEPRECATED = 1

                            INVALID = 2

                            INACCESSIBLE = 3

                            UNKNOWN = 4

                            TENTATIVE = 5

                            DUPLICATE = 6

                            OPTIMISTIC = 7


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.State.StatusEnum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.State']['meta_info']


                    class Vrrp(object):
                        """
                        Enclosing container for VRRP groups handled by this
                        IP interface
                        
                        .. attribute:: vrrp_group
                        
                        	List of VRRP groups, keyed by virtual router id
                        	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.vrrp_group = YList()
                            self.vrrp_group.parent = self
                            self.vrrp_group.name = 'vrrp_group'


                        class VrrpGroup(object):
                            """
                            List of VRRP groups, keyed by virtual router id
                            
                            .. attribute:: virtual_router_id  <key>
                            
                            	References the configured virtual router id for this VRRP group
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for the VRRP group
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config>`
                            
                            .. attribute:: interface_tracking
                            
                            	Top\-level container for VRRP interface tracking
                            	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                            
                            .. attribute:: state
                            
                            	Operational state data for the VRRP group
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State>`
                            
                            

                            """

                            _prefix = 'ocip'
                            _revision = '2015-11-20'

                            def __init__(self):
                                self.parent = None
                                self.virtual_router_id = None
                                self.config = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config()
                                self.config.parent = self
                                self.interface_tracking = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                self.interface_tracking.parent = self
                                self.state = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State()
                                self.state.parent = self


                            class Config(object):
                                """
                                Configuration data for the VRRP group
                                
                                .. attribute:: accept_mode
                                
                                	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: advertisement_interval
                                
                                	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                	**type**\:  int
                                
                                	**range:** 1..4095
                                
                                	**units**\: centiseconds
                                
                                	**default value**\: 100
                                
                                .. attribute:: preempt
                                
                                	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: preempt_delay
                                
                                	Set the delay the higher priority router waits before preempting
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**default value**\: 0
                                
                                .. attribute:: priority
                                
                                	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                	**type**\:  int
                                
                                	**range:** 1..254
                                
                                	**default value**\: 100
                                
                                .. attribute:: virtual_address
                                
                                	Configure one or more virtual addresses for the VRRP group
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_link_local
                                
                                	For VRRP on IPv6 interfaces, sets the virtual link local address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_router_id
                                
                                	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.accept_mode = None
                                    self.advertisement_interval = None
                                    self.preempt = None
                                    self.preempt_delay = None
                                    self.priority = None
                                    self.virtual_address = YLeafList()
                                    self.virtual_address.parent = self
                                    self.virtual_address.name = 'virtual_address'
                                    self.virtual_link_local = None
                                    self.virtual_router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:config'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.accept_mode is not None:
                                        return True

                                    if self.advertisement_interval is not None:
                                        return True

                                    if self.preempt is not None:
                                        return True

                                    if self.preempt_delay is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.virtual_address is not None:
                                        for child in self.virtual_address:
                                            if child is not None:
                                                return True

                                    if self.virtual_link_local is not None:
                                        return True

                                    if self.virtual_router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.Config']['meta_info']


                            class State(object):
                                """
                                Operational state data for the VRRP group
                                
                                .. attribute:: accept_mode
                                
                                	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: advertisement_interval
                                
                                	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                	**type**\:  int
                                
                                	**range:** 1..4095
                                
                                	**units**\: centiseconds
                                
                                	**default value**\: 100
                                
                                .. attribute:: current_priority
                                
                                	Operational value of the priority for the interface in the VRRP group
                                	**type**\:  int
                                
                                	**range:** 0..255
                                
                                .. attribute:: preempt
                                
                                	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                .. attribute:: preempt_delay
                                
                                	Set the delay the higher priority router waits before preempting
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**default value**\: 0
                                
                                .. attribute:: priority
                                
                                	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                	**type**\:  int
                                
                                	**range:** 1..254
                                
                                	**default value**\: 100
                                
                                .. attribute:: virtual_address
                                
                                	Configure one or more virtual addresses for the VRRP group
                                	**type**\: one of the below types:
                                
                                	**type**\:  list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  list of str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_link_local
                                
                                	For VRRP on IPv6 interfaces, sets the virtual link local address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: virtual_router_id
                                
                                	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.accept_mode = None
                                    self.advertisement_interval = None
                                    self.current_priority = None
                                    self.preempt = None
                                    self.preempt_delay = None
                                    self.priority = None
                                    self.virtual_address = YLeafList()
                                    self.virtual_address.parent = self
                                    self.virtual_address.name = 'virtual_address'
                                    self.virtual_link_local = None
                                    self.virtual_router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:state'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.accept_mode is not None:
                                        return True

                                    if self.advertisement_interval is not None:
                                        return True

                                    if self.current_priority is not None:
                                        return True

                                    if self.preempt is not None:
                                        return True

                                    if self.preempt_delay is not None:
                                        return True

                                    if self.priority is not None:
                                        return True

                                    if self.virtual_address is not None:
                                        for child in self.virtual_address:
                                            if child is not None:
                                                return True

                                    if self.virtual_link_local is not None:
                                        return True

                                    if self.virtual_router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.State']['meta_info']


                            class InterfaceTracking(object):
                                """
                                Top\-level container for VRRP interface tracking
                                
                                .. attribute:: config
                                
                                	Configuration data for VRRP interface tracking
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state data for VRRP interface tracking
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                
                                

                                """

                                _prefix = 'ocip'
                                _revision = '2015-11-20'

                                def __init__(self):
                                    self.parent = None
                                    self.config = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                    self.config.parent = self
                                    self.state = Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                    self.state.parent = self


                                class Config(object):
                                    """
                                    Configuration data for VRRP interface tracking
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Set the value to subtract from priority when the tracked interface goes down
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: track_interface
                                    
                                    	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.priority_decrement = None
                                        self.track_interface = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:config'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.priority_decrement is not None:
                                            return True

                                        if self.track_interface is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.Config']['meta_info']


                                class State(object):
                                    """
                                    Operational state data for VRRP interface tracking
                                    
                                    .. attribute:: priority_decrement
                                    
                                    	Set the value to subtract from priority when the tracked interface goes down
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: track_interface
                                    
                                    	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'ocip'
                                    _revision = '2015-11-20'

                                    def __init__(self):
                                        self.parent = None
                                        self.priority_decrement = None
                                        self.track_interface = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/openconfig-if-ip:state'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.priority_decrement is not None:
                                            return True

                                        if self.track_interface is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking.State']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/openconfig-if-ip:interface-tracking'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.config is not None and self.config._has_data():
                                        return True

                                    if self.state is not None and self.state._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup.InterfaceTracking']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.virtual_router_id is None:
                                    raise YPYModelError('Key property virtual_router_id is None')

                                return self.parent._common_path +'/openconfig-if-ip:vrrp-group[openconfig-if-ip:virtual-router-id = ' + str(self.virtual_router_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.virtual_router_id is not None:
                                    return True

                                if self.config is not None and self.config._has_data():
                                    return True

                                if self.interface_tracking is not None and self.interface_tracking._has_data():
                                    return True

                                if self.state is not None and self.state._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp.VrrpGroup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:vrrp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vrrp_group is not None:
                                for child_ref in self.vrrp_group:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address.Vrrp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')

                        return self.parent._common_path +'/openconfig-if-ip:address[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        if self.vrrp is not None and self.vrrp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Address']['meta_info']


                class Neighbor(object):
                    """
                    A list of mappings from IPv6 addresses to
                    link\-layer addresses.
                    Entries in this list are used as static entries in the
                    Neighbor Cache.
                    
                    .. attribute:: ip  <key>
                    
                    	References the configured IP neighbor address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for each IPv6 address on the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config>`
                    
                    .. attribute:: state
                    
                    	State data for each IPv6 address on the interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State>`
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.ip = None
                        self.config = Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        Configuration data for each IPv6 address on
                        the interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv6 address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: link_layer_address
                        
                        	[adapted from IETF IP model RFC 7277] The link\-layer address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.link_layer_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:config'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.Config']['meta_info']


                    class State(object):
                        """
                        State data for each IPv6 address on the
                        interface
                        
                        .. attribute:: ip
                        
                        	[adapted from IETF IP model RFC 7277] The IPv6 address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_router
                        
                        	[adapted from IETF IP model RFC 7277] Indicates that the neighbor node acts as a router
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: link_layer_address
                        
                        	[adapted from IETF IP model RFC 7277] The link\-layer address of the neighbor node
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: neighbor_state
                        
                        	[adapted from IETF IP model RFC 7277] The Neighbor Unreachability Detection state of this entry
                        	**type**\:   :py:class:`NeighborStateEnum <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State.NeighborStateEnum>`
                        
                        .. attribute:: origin
                        
                        	[adapted from IETF IP model RFC 7277] The origin of this neighbor entry
                        	**type**\:   :py:class:`NeighborOriginEnum <ydk.models.openconfig.openconfig_if_ip.NeighborOriginEnum>`
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

                        def __init__(self):
                            self.parent = None
                            self.ip = None
                            self.is_router = None
                            self.link_layer_address = None
                            self.neighbor_state = None
                            self.origin = None

                        class NeighborStateEnum(Enum):
                            """
                            NeighborStateEnum

                            [adapted from IETF IP model RFC 7277]

                            The Neighbor Unreachability Detection state of this

                            entry.

                            .. data:: INCOMPLETE = 0

                            	Address resolution is in progress, and the link-layer

                            	     address of the neighbor has not yet been

                            	     determined.

                            .. data:: REACHABLE = 1

                            	Roughly speaking, the neighbor is known to have been

                            	     reachable recently (within tens of seconds ago).

                            .. data:: STALE = 2

                            	The neighbor is no longer known to be reachable, but

                            	     until traffic is sent to the neighbor no attempt

                            	     should be made to verify its reachability.

                            .. data:: DELAY = 3

                            	The neighbor is no longer known to be reachable, and

                            	     traffic has recently been sent to the neighbor.

                            	     Rather than probe the neighbor immediately, however,

                            	     delay sending probes for a short while in order to

                            	     give upper-layer protocols a chance to provide

                            	     reachability confirmation.

                            .. data:: PROBE = 4

                            	The neighbor is no longer known to be reachable, and

                            	     unicast Neighbor Solicitation probes are being sent

                            	     to verify reachability.

                            """

                            INCOMPLETE = 0

                            REACHABLE = 1

                            STALE = 2

                            DELAY = 3

                            PROBE = 4


                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                                return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State.NeighborStateEnum']


                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-if-ip:state'

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

                            if self.neighbor_state is not None:
                                return True

                            if self.origin is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ip is None:
                            raise YPYModelError('Key property ip is None')

                        return self.parent._common_path +'/openconfig-if-ip:neighbor[openconfig-if-ip:ip = ' + str(self.ip) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Neighbor']['meta_info']


                class Config(object):
                    """
                    Top\-level config data for the IPv6 interface
                    
                    .. attribute:: dup_addr_detect_transmits
                    
                    	[adapted from IETF IP model RFC 7277] The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF IP model RFC 7277] Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	[adapted from IETF IP model RFC 7277] The size, in octets, of the largest IPv6 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 1280..4294967295
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.dup_addr_detect_transmits = None
                        self.enabled = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.dup_addr_detect_transmits is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Config']['meta_info']


                class State(object):
                    """
                    Top\-level operational state data for the IPv6 interface
                    
                    .. attribute:: dup_addr_detect_transmits
                    
                    	[adapted from IETF IP model RFC 7277] The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF IP model RFC 7277] Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	[adapted from IETF IP model RFC 7277] The size, in octets, of the largest IPv6 packet that the interface will send and receive. The server may restrict the allowed values for this leaf, depending on the interface's type. If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 1280..4294967295
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.dup_addr_detect_transmits = None
                        self.enabled = None
                        self.mtu = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dup_addr_detect_transmits is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.State']['meta_info']


                class Autoconf(object):
                    """
                    Top\-level container for IPv6 autoconf
                    
                    .. attribute:: config
                    
                    	[adapted from IETF IP model RFC 7277] Parameters to control the autoconfiguration of IPv6 addresses, as described in RFC 4862
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data 
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State>`
                    
                    

                    """

                    _prefix = 'ocip'
                    _revision = '2015-11-20'

                    def __init__(self):
                        self.parent = None
                        self.config = Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config()
                        self.config.parent = self
                        self.state = Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State()
                        self.state.parent = self


                    class Config(object):
                        """
                        [adapted from IETF IP model RFC 7277]
                        Parameters to control the autoconfiguration of IPv6
                        addresses, as described in RFC 4862.
                        
                        .. attribute:: create_global_addresses
                        
                        	[adapted from IETF IP model RFC 7277] If enabled, the host creates global addresses as described in RFC 4862
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: create_temporary_addresses
                        
                        	[adapted from IETF IP model RFC 7277] If enabled, the host creates temporary addresses as described in RFC 4941
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: temporary_preferred_lifetime
                        
                        	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is preferred
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 86400
                        
                        .. attribute:: temporary_valid_lifetime
                        
                        	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 604800
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

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

                            return self.parent._common_path +'/openconfig-if-ip:config'

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.Config']['meta_info']


                    class State(object):
                        """
                        Operational state data 
                        
                        .. attribute:: create_global_addresses
                        
                        	[adapted from IETF IP model RFC 7277] If enabled, the host creates global addresses as described in RFC 4862
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: create_temporary_addresses
                        
                        	[adapted from IETF IP model RFC 7277] If enabled, the host creates temporary addresses as described in RFC 4941
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: temporary_preferred_lifetime
                        
                        	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is preferred
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 86400
                        
                        .. attribute:: temporary_valid_lifetime
                        
                        	[adapted from IETF IP model RFC 7277] The time period during which the temporary address is valid
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: seconds
                        
                        	**default value**\: 604800
                        
                        

                        """

                        _prefix = 'ocip'
                        _revision = '2015-11-20'

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

                            return self.parent._common_path +'/openconfig-if-ip:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

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
                            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                            return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-if-ip:autoconf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                        return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6.Autoconf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-if-ip:ipv6'

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

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.neighbor is not None:
                        for child_ref in self.neighbor:
                            if child_ref._has_data():
                                return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                    return meta._meta_table['Interfaces.Interface.RoutedVlan.Ipv6']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-vlan:routed-vlan'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.config is not None and self.config._has_data():
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_interfaces as meta
                return meta._meta_table['Interfaces.Interface.RoutedVlan']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/openconfig-interfaces:interfaces/openconfig-interfaces:interface[openconfig-interfaces:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.aggregation is not None and self.aggregation._has_data():
                return True

            if self.config is not None and self.config._has_data():
                return True

            if self.ethernet is not None and self.ethernet._has_data():
                return True

            if self.hold_time is not None and self.hold_time._has_data():
                return True

            if self.routed_vlan is not None and self.routed_vlan._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            if self.subinterfaces is not None and self.subinterfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_interfaces as meta
            return meta._meta_table['Interfaces.Interface']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-interfaces:interfaces'

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
        from ydk.models.openconfig._meta import _openconfig_interfaces as meta
        return meta._meta_table['Interfaces']['meta_info']


