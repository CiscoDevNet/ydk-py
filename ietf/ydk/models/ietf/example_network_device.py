""" example_network_device 

This module describes a model structure for YANG
configuration and operational state data models. Its intent is
to describe how individual device protocol and feature models
fit together and interact.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ControlPlaneProtocolTypeIdentity(object):
    """
    Base identity for derivation of control\-plane protocols
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['ControlPlaneProtocolTypeIdentity']['meta_info']


class OamServiceTypeIdentity(object):
    """
    Base identity for derivation of Operations,
    Administration, and Maintenance (OAM) services.
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['OamServiceTypeIdentity']['meta_info']


class NetworkServiceTypeIdentity(object):
    """
    Base identity for derivation of network services
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['NetworkServiceTypeIdentity']['meta_info']


class MplsLspTypeIdentity(object):
    """
    Base identity for derivation of MPLS LSP typs
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['MplsLspTypeIdentity']['meta_info']


class SystemManagementProtocolTypeIdentity(object):
    """
    Base identity for derivation of system management
    protocols
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['SystemManagementProtocolTypeIdentity']['meta_info']


class OamProtocolTypeIdentity(object):
    """
    Base identity for derivation of OAM protocols
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['OamProtocolTypeIdentity']['meta_info']


class IetfYangLibrary(object):
    """
    YANG Module Library as defined in
    draft\-ietf\-netconf\-yang\-library
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:ietf-yang-library'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['IetfYangLibrary']['meta_info']


class Interfaces(object):
    """
    Interface list as defined by RFC7223/RFC7224
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:interfaces'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['Interfaces']['meta_info']


class Hardware(object):
    """
    Hardware / vendor\-specific data relevant to the platform.
    This container is an anchor point for platform\-specific
    configuration and operational state data.  It may be further
    organized into chassis, line cards, ports, etc.  It is
    expected that vendor or platform\-specific augmentations
    would be used to populate this part of the device model
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:hardware'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['Hardware']['meta_info']


class Qos(object):
    """
    QoS features, for example policing, shaping, etc.
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['Qos']['meta_info']


class SystemManagement(object):
    """
    System management for physical or virtual device.
    
    .. attribute:: system_management_global
    
    	System management \- with reuse of RFC 7317
    	**type**\:   :py:class:`SystemManagementGlobal <ydk.models.ietf.example_network_device.SystemManagement.SystemManagementGlobal>`
    
    .. attribute:: system_management_protocol
    
    	List of system management protocol configured for a logical network element
    	**type**\: list of    :py:class:`SystemManagementProtocol <ydk.models.ietf.example_network_device.SystemManagement.SystemManagementProtocol>`
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        self.system_management_global = SystemManagement.SystemManagementGlobal()
        self.system_management_global.parent = self
        self.system_management_protocol = YList()
        self.system_management_protocol.parent = self
        self.system_management_protocol.name = 'system_management_protocol'


    class SystemManagementGlobal(object):
        """
        System management \- with reuse of RFC 7317
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/example-network-device:system-management/example-network-device:system-management-global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['SystemManagement.SystemManagementGlobal']['meta_info']


    class SystemManagementProtocol(object):
        """
        List of system management protocol
        configured for a logical network
        element.
        
        .. attribute:: type  <key>
        
        	Syslog, ssh, TACAC+, SNMP, NETCONF, etc
        	**type**\:   :py:class:`SystemManagementProtocolTypeIdentity <ydk.models.ietf.example_network_device.SystemManagementProtocolTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.type = None

        @property
        def _common_path(self):
            if self.type is None:
                raise YPYModelError('Key property type is None')

            return '/example-network-device:system-management/example-network-device:system-management-protocol[example-network-device:type = ' + str(self.type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['SystemManagement.SystemManagementProtocol']['meta_info']

    @property
    def _common_path(self):

        return '/example-network-device:system-management'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.system_management_global is not None and self.system_management_global._has_data():
            return True

        if self.system_management_protocol is not None:
            for child_ref in self.system_management_protocol:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['SystemManagement']['meta_info']


class NetworkServices(object):
    """
    Container for list of configured network
    services.
    
    .. attribute:: network_service
    
    	List of network services configured for a network instance
    	**type**\: list of    :py:class:`NetworkService <ydk.models.ietf.example_network_device.NetworkServices.NetworkService>`
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        self.network_service = YList()
        self.network_service.parent = self
        self.network_service.name = 'network_service'


    class NetworkService(object):
        """
        List of network services configured for a
        network instance.
        
        .. attribute:: type  <key>
        
        	The network service type supported within a network instance, e.g., NTP server, DNS server, DHCP server, etc
        	**type**\:   :py:class:`NetworkServiceTypeIdentity <ydk.models.ietf.example_network_device.NetworkServiceTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.type = None

        @property
        def _common_path(self):
            if self.type is None:
                raise YPYModelError('Key property type is None')

            return '/example-network-device:network-services/example-network-device:network-service[example-network-device:type = ' + str(self.type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['NetworkServices.NetworkService']['meta_info']

    @property
    def _common_path(self):

        return '/example-network-device:network-services'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.network_service is not None:
            for child_ref in self.network_service:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['NetworkServices']['meta_info']


class OamProtocols(object):
    """
    Container for configured OAM protocols.
    
    .. attribute:: oam_protocol
    
    	List of configured OAM protocols
    	**type**\: list of    :py:class:`OamProtocol <ydk.models.ietf.example_network_device.OamProtocols.OamProtocol>`
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        self.oam_protocol = YList()
        self.oam_protocol.parent = self
        self.oam_protocol.name = 'oam_protocol'


    class OamProtocol(object):
        """
        List of configured OAM protocols.
        
        .. attribute:: type  <key>
        
        	The Operations, Administration, and Maintenance (OAM) protocol type, e.g., BFD, TWAMP, CFM, etc
        	**type**\:   :py:class:`OamProtocolTypeIdentity <ydk.models.ietf.example_network_device.OamProtocolTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.type = None

        @property
        def _common_path(self):
            if self.type is None:
                raise YPYModelError('Key property type is None')

            return '/example-network-device:oam-protocols/example-network-device:oam-protocol[example-network-device:type = ' + str(self.type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['OamProtocols.OamProtocol']['meta_info']

    @property
    def _common_path(self):

        return '/example-network-device:oam-protocols'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.oam_protocol is not None:
            for child_ref in self.oam_protocol:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['OamProtocols']['meta_info']


class Routing(object):
    """
    The YANG Data Model for Routing Management revised to be
    Network Instance / VRF independent. 
    
    .. attribute:: control_plane_protocol
    
    	List of control plane protocols configured for a network instance
    	**type**\: list of    :py:class:`ControlPlaneProtocol <ydk.models.ietf.example_network_device.Routing.ControlPlaneProtocol>`
    
    .. attribute:: rib
    
    	Each entry represents a RIB identified by the 'name' key. All routes in a RIB must belong to the same address family.  For each routing instance, an implementation should provide one system\-controlled default RIB for each supported address family
    	**type**\: list of    :py:class:`Rib <ydk.models.ietf.example_network_device.Routing.Rib>`
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        self.control_plane_protocol = YList()
        self.control_plane_protocol.parent = self
        self.control_plane_protocol.name = 'control_plane_protocol'
        self.rib = YList()
        self.rib.parent = self
        self.rib.name = 'rib'


    class ControlPlaneProtocol(object):
        """
        List of control plane protocols configured for
        a network instance.
        
        .. attribute:: type  <key>
        
        	The control plane protocol type, e.g., BGP, OSPF IS\-IS, etc
        	**type**\:   :py:class:`ControlPlaneProtocolTypeIdentity <ydk.models.ietf.example_network_device.ControlPlaneProtocolTypeIdentity>`
        
        	**mandatory**\: True
        
        .. attribute:: policy
        
        	Protocol specific policy, reusing [RTG\-POLICY]
        	**type**\:   :py:class:`Policy <ydk.models.ietf.example_network_device.Routing.ControlPlaneProtocol.Policy>`
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.type = None
            self.policy = Routing.ControlPlaneProtocol.Policy()
            self.policy.parent = self


        class Policy(object):
            """
            Protocol specific policy,
            reusing [RTG\-POLICY]
            
            

            """

            _prefix = 'nd'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/example-network-device:policy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _example_network_device as meta
                return meta._meta_table['Routing.ControlPlaneProtocol.Policy']['meta_info']

        @property
        def _common_path(self):
            if self.type is None:
                raise YPYModelError('Key property type is None')

            return '/example-network-device:routing/example-network-device:control-plane-protocol[example-network-device:type = ' + str(self.type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.type is not None:
                return True

            if self.policy is not None and self.policy._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['Routing.ControlPlaneProtocol']['meta_info']


    class Rib(object):
        """
        Each entry represents a RIB identified by the
        'name' key. All routes in a RIB must belong to the
        same address family.
        
        For each routing instance, an implementation should
        provide one system\-controlled default RIB for each
        supported address family.
        
        .. attribute:: name  <key>
        
        	The name of the RIB
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: description
        
        	Description of the RIB
        	**type**\:  str
        
        .. attribute:: policy
        
        	Policy specific to RIB
        	**type**\:   :py:class:`Policy <ydk.models.ietf.example_network_device.Routing.Rib.Policy>`
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.name = None
            self.description = None
            self.policy = Routing.Rib.Policy()
            self.policy.parent = self


        class Policy(object):
            """
            Policy specific to RIB
            
            

            """

            _prefix = 'nd'
            _revision = '2017-03-13'

            def __init__(self):
                self.parent = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/example-network-device:policy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _example_network_device as meta
                return meta._meta_table['Routing.Rib.Policy']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/example-network-device:routing/example-network-device:rib[example-network-device:name = ' + str(self.name) + ']'

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

            if self.policy is not None and self.policy._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['Routing.Rib']['meta_info']

    @property
    def _common_path(self):

        return '/example-network-device:routing'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.control_plane_protocol is not None:
            for child_ref in self.control_plane_protocol:
                if child_ref._has_data():
                    return True

        if self.rib is not None:
            for child_ref in self.rib:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['Routing']['meta_info']


class Mpls(object):
    """
    MPLS and TE configuration
    
    .. attribute:: global_
    
    	Global MPLS configuration
    	**type**\:   :py:class:`Global_ <ydk.models.ietf.example_network_device.Mpls.Global_>`
    
    .. attribute:: lsps
    
    	List of LSP types
    	**type**\: list of    :py:class:`Lsps <ydk.models.ietf.example_network_device.Mpls.Lsps>`
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        self.global_ = Mpls.Global_()
        self.global_.parent = self
        self.lsps = YList()
        self.lsps.parent = self
        self.lsps.name = 'lsps'


    class Global_(object):
        """
        Global MPLS configuration
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None

        @property
        def _common_path(self):

            return '/example-network-device:mpls/example-network-device:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['Mpls.Global_']['meta_info']


    class Lsps(object):
        """
        List of LSP types.
        
        .. attribute:: type  <key>
        
        	MPLS and Traffic Engineering protocol LSP types, static, LDP/SR (igp\-congruent), RSVP TE (constrained\-paths) , etc
        	**type**\:   :py:class:`MplsLspTypeIdentity <ydk.models.ietf.example_network_device.MplsLspTypeIdentity>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'nd'
        _revision = '2017-03-13'

        def __init__(self):
            self.parent = None
            self.type = None

        @property
        def _common_path(self):
            if self.type is None:
                raise YPYModelError('Key property type is None')

            return '/example-network-device:mpls/example-network-device:lsps[example-network-device:type = ' + str(self.type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _example_network_device as meta
            return meta._meta_table['Mpls.Lsps']['meta_info']

    @property
    def _common_path(self):

        return '/example-network-device:mpls'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.global_ is not None and self.global_._has_data():
            return True

        if self.lsps is not None:
            for child_ref in self.lsps:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['Mpls']['meta_info']


class IeeeDot1Q(object):
    """
    The YANG Data Model for VLAN bridges as defined by the IEEE
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:ieee-dot1Q'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['IeeeDot1Q']['meta_info']


class IetfAcl(object):
    """
    Packet Access Control Lists (ACLs) as specified
      in draft\-ietf\-netmod\-acl\-model
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:ietf-acl'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['IetfAcl']['meta_info']


class IetfKeyChain(object):
    """
    Key chains as specified in
    draft\-ietf\-rtgwg\-yang\-key\-chain;
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:ietf-key-chain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['IetfKeyChain']['meta_info']


class LogicalNetworkElement(object):
    """
    This module is used to support multiple logical network
    elements on a single physical or virtual system.
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:logical-network-element'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['LogicalNetworkElement']['meta_info']


class NetworkInstance(object):
    """
    This module is used to support multiple network instances
    within a single physical or virtual device.  Network
    instances are commonly know as VRFs (virtual routing
    and forwarding) and VSIs (virtual switching instances).
    
    

    """

    _prefix = 'nd'
    _revision = '2017-03-13'

    def __init__(self):
        pass

    @property
    def _common_path(self):

        return '/example-network-device:network-instance'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _example_network_device as meta
        return meta._meta_table['NetworkInstance']['meta_info']


