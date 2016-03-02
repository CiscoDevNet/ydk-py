""" model_structure 

This module describes a model structure for YANG
configuration and operational state data models. Its intent is to
describe how individual device protocol and feature models fit
together and interact.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Device(object):
    """
    top\-level anchor point for models.  Device is a
    generic L2/L3 network element
    
    .. attribute:: acl
    
    	ACLs and packet forwarding rules
    	**type**\: :py:class:`Acl <ydk.models.model.model_structure.Device.Acl>`
    
    .. attribute:: hardware
    
    	This container is an anchor point for platform\-specific configuration and operational state data.  It may be further organized into chassis, linecards, ports, etc.  It is expected that vendor or platform\-specific augmentations would be used to populate this part of the device model
    	**type**\: :py:class:`Hardware <ydk.models.model.model_structure.Device.Hardware>`
    
    .. attribute:: info
    
    	This container is for base system information, including device type (e.g., physcal or virtual), model, serial no., location, etc
    	**type**\: :py:class:`Info <ydk.models.model.model_structure.Device.Info>`
    
    .. attribute:: interfaces
    
    	various interface models
    	**type**\: :py:class:`Interfaces <ydk.models.model.model_structure.Device.Interfaces>`
    
    .. attribute:: logical_routers
    
    	devices may support multiple logical router instances
    	**type**\: :py:class:`LogicalRouters <ydk.models.model.model_structure.Device.LogicalRouters>`
    
    .. attribute:: qos
    
    	QoS, including policing, shaping, etc
    	**type**\: :py:class:`Qos <ydk.models.model.model_structure.Device.Qos>`
    
    .. attribute:: system
    
    	system services
    	**type**\: :py:class:`System <ydk.models.model.model_structure.Device.System>`
    
    

    """

    _prefix = 'struct'
    _revision = '2015-03-06'

    def __init__(self):
        self.acl = Device.Acl()
        self.acl.parent = self
        self.hardware = Device.Hardware()
        self.hardware.parent = self
        self.info = Device.Info()
        self.info.parent = self
        self.interfaces = Device.Interfaces()
        self.interfaces.parent = self
        self.logical_routers = Device.LogicalRouters()
        self.logical_routers.parent = self
        self.qos = Device.Qos()
        self.qos.parent = self
        self.system = Device.System()
        self.system.parent = self


    class Acl(object):
        """
        ACLs and packet forwarding rules
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            pass

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:acl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.Acl']['meta_info']


    class Hardware(object):
        """
        This container is an anchor point for platform\-specific
        configuration and operational state data.  It may be further
        organized into chassis, linecards, ports, etc.  It is
        expected that vendor or platform\-specific augmentations
        would be used to populate this part of the device model
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            pass

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:hardware'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.Hardware']['meta_info']


    class Info(object):
        """
        This container is for base system information, including
        device type (e.g., physcal or virtual), model, serial no.,
        location, etc.
        
        .. attribute:: device_type
        
        	Type of the device, e.g., physical or virtual.  This node may be used to activate other containers in the model
        	**type**\: :py:class:`DeviceType_Enum <ydk.models.model.model_structure.Device.Info.DeviceType_Enum>`
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            self.device_type = None

        class DeviceType_Enum(Enum):
            """
            DeviceType_Enum

            Type of the device, e.g., physical or virtual.  This node
            may be used to activate other containers in the model

            """

            """

            physical or hardware device

            """
            PHYSICAL = 0

            """

            virtual or software device

            """
            VIRTUAL = 1


            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.Info.DeviceType_Enum']


        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:info'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.device_type is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.Info']['meta_info']


    class Interfaces(object):
        """
        various interface models
        
        .. attribute:: addressing
        
        	addressing and other interface\-specific data, e.g., data plane protocols
        	**type**\: :py:class:`Addressing <ydk.models.model.model_structure.Device.Interfaces.Addressing>`
        
        .. attribute:: ethernet
        
        	Ethernet interface config, e.g., 10, 40, 100GBE
        	**type**\: :py:class:`Ethernet <ydk.models.model.model_structure.Device.Interfaces.Ethernet>`
        
        .. attribute:: sonet_sdh
        
        	SONET/SDH interfaces
        	**type**\: :py:class:`SonetSdh <ydk.models.model.model_structure.Device.Interfaces.SonetSdh>`
        
        .. attribute:: tunnels
        
        	logical tunnel interfaces incl. GRE, VxLAN, L2TP etc
        	**type**\: :py:class:`Tunnels <ydk.models.model.model_structure.Device.Interfaces.Tunnels>`
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            self.addressing = Device.Interfaces.Addressing()
            self.addressing.parent = self
            self.ethernet = Device.Interfaces.Ethernet()
            self.ethernet.parent = self
            self.sonet_sdh = Device.Interfaces.SonetSdh()
            self.sonet_sdh.parent = self
            self.tunnels = Device.Interfaces.Tunnels()
            self.tunnels.parent = self


        class Addressing(object):
            """
            addressing and other interface\-specific data,
            e.g., data plane protocols
            
            .. attribute:: ipv4
            
            	IPv4 interfaces
            	**type**\: :py:class:`Ipv4 <ydk.models.model.model_structure.Device.Interfaces.Addressing.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 interfaces
            	**type**\: :py:class:`Ipv6 <ydk.models.model.model_structure.Device.Interfaces.Addressing.Ipv6>`
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                self.ipv4 = Device.Interfaces.Addressing.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Device.Interfaces.Addressing.Ipv6()
                self.ipv6.parent = self


            class Ipv4(object):
                """
                IPv4 interfaces
                
                .. attribute:: vrrp
                
                	virtual router redundancy protocol
                	**type**\: :py:class:`Vrrp <ydk.models.model.model_structure.Device.Interfaces.Addressing.Ipv4.Vrrp>`
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    self.vrrp = Device.Interfaces.Addressing.Ipv4.Vrrp()
                    self.vrrp.parent = self


                class Vrrp(object):
                    """
                    virtual router redundancy protocol
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):

                        return '/model-structure:device/model-structure:interfaces/model-structure:addressing/model-structure:ipv4/model-structure:vrrp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.Interfaces.Addressing.Ipv4.Vrrp']['meta_info']

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:interfaces/model-structure:addressing/model-structure:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.vrrp is not None and self.vrrp._has_data():
                        return True

                    if self.vrrp is not None and self.vrrp.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.Interfaces.Addressing.Ipv4']['meta_info']


            class Ipv6(object):
                """
                IPv6 interfaces
                
                .. attribute:: vrrp
                
                	virtual router redundancy protocol
                	**type**\: :py:class:`Vrrp <ydk.models.model.model_structure.Device.Interfaces.Addressing.Ipv6.Vrrp>`
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    self.vrrp = Device.Interfaces.Addressing.Ipv6.Vrrp()
                    self.vrrp.parent = self


                class Vrrp(object):
                    """
                    virtual router redundancy protocol
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):

                        return '/model-structure:device/model-structure:interfaces/model-structure:addressing/model-structure:ipv6/model-structure:vrrp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.Interfaces.Addressing.Ipv6.Vrrp']['meta_info']

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:interfaces/model-structure:addressing/model-structure:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.vrrp is not None and self.vrrp._has_data():
                        return True

                    if self.vrrp is not None and self.vrrp.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.Interfaces.Addressing.Ipv6']['meta_info']

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:interfaces/model-structure:addressing'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv4 is not None and self.ipv4.is_presence():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.Interfaces.Addressing']['meta_info']


        class Ethernet(object):
            """
            Ethernet interface config, e.g., 10, 40,
            100GBE
            
            .. attribute:: aggregates
            
            	LAGs, LACP, etc. for Ethernet interfaces
            	**type**\: :py:class:`Aggregates <ydk.models.model.model_structure.Device.Interfaces.Ethernet.Aggregates>`
            
            .. attribute:: lfm
            
            	Link\-layer fault management for Ethernet interfaces
            	**type**\: :py:class:`Lfm <ydk.models.model.model_structure.Device.Interfaces.Ethernet.Lfm>`
            
            .. attribute:: vlans
            
            	VLANs, 802.1q, q\-in\-q, etc
            	**type**\: :py:class:`Vlans <ydk.models.model.model_structure.Device.Interfaces.Ethernet.Vlans>`
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                self.aggregates = Device.Interfaces.Ethernet.Aggregates()
                self.aggregates.parent = self
                self.lfm = Device.Interfaces.Ethernet.Lfm()
                self.lfm.parent = self
                self.vlans = Device.Interfaces.Ethernet.Vlans()
                self.vlans.parent = self


            class Aggregates(object):
                """
                LAGs, LACP, etc. for Ethernet interfaces
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:interfaces/model-structure:ethernet/model-structure:aggregates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.Interfaces.Ethernet.Aggregates']['meta_info']


            class Lfm(object):
                """
                Link\-layer fault management for Ethernet interfaces
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:interfaces/model-structure:ethernet/model-structure:lfm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.Interfaces.Ethernet.Lfm']['meta_info']


            class Vlans(object):
                """
                VLANs, 802.1q, q\-in\-q, etc.
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:interfaces/model-structure:ethernet/model-structure:vlans'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.Interfaces.Ethernet.Vlans']['meta_info']

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:interfaces/model-structure:ethernet'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.aggregates is not None and self.aggregates._has_data():
                    return True

                if self.aggregates is not None and self.aggregates.is_presence():
                    return True

                if self.lfm is not None and self.lfm._has_data():
                    return True

                if self.lfm is not None and self.lfm.is_presence():
                    return True

                if self.vlans is not None and self.vlans._has_data():
                    return True

                if self.vlans is not None and self.vlans.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.Interfaces.Ethernet']['meta_info']


        class SonetSdh(object):
            """
            SONET/SDH interfaces
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:interfaces/model-structure:sonet-sdh'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.Interfaces.SonetSdh']['meta_info']


        class Tunnels(object):
            """
            logical tunnel interfaces incl. GRE, VxLAN, L2TP etc.
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:interfaces/model-structure:tunnels'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.Interfaces.Tunnels']['meta_info']

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.addressing is not None and self.addressing._has_data():
                return True

            if self.addressing is not None and self.addressing.is_presence():
                return True

            if self.ethernet is not None and self.ethernet._has_data():
                return True

            if self.ethernet is not None and self.ethernet.is_presence():
                return True

            if self.sonet_sdh is not None and self.sonet_sdh._has_data():
                return True

            if self.sonet_sdh is not None and self.sonet_sdh.is_presence():
                return True

            if self.tunnels is not None and self.tunnels._has_data():
                return True

            if self.tunnels is not None and self.tunnels.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.Interfaces']['meta_info']


    class LogicalRouters(object):
        """
        devices may support multiple logical router
        instances
        
        .. attribute:: logical_router
        
        	list of logical router instances
        	**type**\: list of :py:class:`LogicalRouter <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter>`
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            self.logical_router = YList()
            self.logical_router.parent = self
            self.logical_router.name = 'logical_router'


        class LogicalRouter(object):
            """
            list of logical router instances
            
            .. attribute:: router_id
            
            	identifier of the logical router instance
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: layer_2_protocols
            
            	layer 2 protocols and features
            	**type**\: :py:class:`Layer2Protocols <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols>`
            
            .. attribute:: layer_3_protocols
            
            	layer 3 protocols and features
            	**type**\: :py:class:`Layer3Protocols <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols>`
            
            .. attribute:: router_name
            
            	identifier of the logical router instance
            	**type**\: str
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                self.router_id = None
                self.layer_2_protocols = Device.LogicalRouters.LogicalRouter.Layer2Protocols()
                self.layer_2_protocols.parent = self
                self.layer_3_protocols = Device.LogicalRouters.LogicalRouter.Layer3Protocols()
                self.layer_3_protocols.parent = self
                self.router_name = None


            class Layer2Protocols(object):
                """
                layer 2 protocols and features
                
                .. attribute:: arp
                
                	Address resolution protocol
                	**type**\: :py:class:`Arp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp>`
                
                .. attribute:: ipv6_ndp
                
                	IPv6 neighbor discovery
                	**type**\: :py:class:`Ipv6Ndp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp>`
                
                .. attribute:: lldp
                
                	link layer discovery protocol
                	**type**\: :py:class:`Lldp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp>`
                
                .. attribute:: ptp
                
                	precision time protocol for time synchronization services. PTP also typically requires per\-interface configuration
                	**type**\: :py:class:`Ptp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp>`
                
                .. attribute:: rstp
                
                	rapid spanning tree protocol
                	**type**\: :py:class:`Rstp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp>`
                
                .. attribute:: vsi
                
                	virtual switch instance (or virtual forwarding instance) for use in PWE3 / VPLS services
                	**type**\: :py:class:`Vsi <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi>`
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    self.arp = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp()
                    self.arp.parent = self
                    self.ipv6_ndp = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp()
                    self.ipv6_ndp.parent = self
                    self.lldp = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp()
                    self.lldp.parent = self
                    self.ptp = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp()
                    self.ptp.parent = self
                    self.rstp = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp()
                    self.rstp.parent = self
                    self.vsi = Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi()
                    self.vsi.parent = self


                class Arp(object):
                    """
                    Address resolution protocol
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:arp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Arp']['meta_info']


                class Ipv6Ndp(object):
                    """
                    IPv6 neighbor discovery
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:ipv6-ndp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ipv6Ndp']['meta_info']


                class Lldp(object):
                    """
                    link layer discovery protocol
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:lldp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Lldp']['meta_info']


                class Ptp(object):
                    """
                    precision time protocol for time synchronization services.
                    PTP also typically requires per\-interface configuration
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:ptp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Ptp']['meta_info']


                class Rstp(object):
                    """
                    rapid spanning tree protocol
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:rstp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Rstp']['meta_info']


                class Vsi(object):
                    """
                    virtual switch instance (or virtual forwarding
                    instance) for use in PWE3 / VPLS services
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        pass

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:vsi'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols.Vsi']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/model-structure:layer-2-protocols'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.arp is not None and self.arp._has_data():
                        return True

                    if self.arp is not None and self.arp.is_presence():
                        return True

                    if self.ipv6_ndp is not None and self.ipv6_ndp._has_data():
                        return True

                    if self.ipv6_ndp is not None and self.ipv6_ndp.is_presence():
                        return True

                    if self.lldp is not None and self.lldp._has_data():
                        return True

                    if self.lldp is not None and self.lldp.is_presence():
                        return True

                    if self.ptp is not None and self.ptp._has_data():
                        return True

                    if self.ptp is not None and self.ptp.is_presence():
                        return True

                    if self.rstp is not None and self.rstp._has_data():
                        return True

                    if self.rstp is not None and self.rstp.is_presence():
                        return True

                    if self.vsi is not None and self.vsi._has_data():
                        return True

                    if self.vsi is not None and self.vsi.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer2Protocols']['meta_info']


            class Layer3Protocols(object):
                """
                layer 3 protocols and features
                
                .. attribute:: global_
                
                	router\-wide instance of each routing protocol
                	**type**\: :py:class:`Global <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global>`
                
                .. attribute:: routing_policy
                
                	models related to routing policy across protocols and VRFs
                	**type**\: :py:class:`RoutingPolicy <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy>`
                
                .. attribute:: vrf
                
                	list of VRF instances
                	**type**\: list of :py:class:`Vrf <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf>`
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    self.global_ = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global()
                    self.global_.parent = self
                    self.routing_policy = Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy()
                    self.routing_policy.parent = self
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Global(object):
                    """
                    router\-wide instance of each routing protocol
                    
                    .. attribute:: bfd
                    
                    	bidirectional forwarding detection
                    	**type**\: :py:class:`Bfd <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd>`
                    
                    .. attribute:: bgp
                    
                    	BGP 4
                    	**type**\: :py:class:`Bgp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp>`
                    
                    .. attribute:: igmp
                    
                    	Internet group management protocol
                    	**type**\: :py:class:`Igmp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp>`
                    
                    .. attribute:: igp
                    
                    	interior gateway protocols
                    	**type**\: :py:class:`Igp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp>`
                    
                    .. attribute:: mpls_te
                    
                    	MPLS and traffic engineering
                    	**type**\: :py:class:`MplsTe <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe>`
                    
                    .. attribute:: pim
                    
                    	protocol independent multicast
                    	**type**\: :py:class:`Pim <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim>`
                    
                    .. attribute:: static_routes
                    
                    	static route that are manually created
                    	**type**\: :py:class:`StaticRoutes <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes>`
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        self.bfd = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd()
                        self.bfd.parent = self
                        self.bgp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp()
                        self.bgp.parent = self
                        self.igmp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp()
                        self.igmp.parent = self
                        self.igp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp()
                        self.igp.parent = self
                        self.mpls_te = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe()
                        self.mpls_te.parent = self
                        self.pim = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim()
                        self.pim.parent = self
                        self.static_routes = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes()
                        self.static_routes.parent = self


                    class Bfd(object):
                        """
                        bidirectional forwarding detection
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bfd']['meta_info']


                    class Bgp(object):
                        """
                        BGP 4
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:bgp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Bgp']['meta_info']


                    class Igmp(object):
                        """
                        Internet group management protocol
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:igmp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igmp']['meta_info']


                    class Igp(object):
                        """
                        interior gateway protocols
                        
                        .. attribute:: igp_common
                        
                        	Common parameters for IGP protocols
                        	**type**\: :py:class:`IgpCommon <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon>`
                        
                        .. attribute:: is_is
                        
                        	IS\-IS IGP routing protocol
                        	**type**\: :py:class:`IsIs <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs>`
                        
                        .. attribute:: ospf
                        
                        	OSPF IGP routing protocols
                        	**type**\: :py:class:`Ospf <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            self.igp_common = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon()
                            self.igp_common.parent = self
                            self.is_is = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs()
                            self.is_is.parent = self
                            self.ospf = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf()
                            self.ospf.parent = self


                        class IgpCommon(object):
                            """
                            Common parameters for IGP protocols
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:igp-common'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IgpCommon']['meta_info']


                        class IsIs(object):
                            """
                            IS\-IS IGP routing protocol
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:is-is'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.IsIs']['meta_info']


                        class Ospf(object):
                            """
                            OSPF IGP routing protocols
                            
                            .. attribute:: ospf2
                            
                            	OSPF v2
                            	**type**\: :py:class:`Ospf2 <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2>`
                            
                            .. attribute:: ospf3
                            
                            	OSPF v3
                            	**type**\: :py:class:`Ospf3 <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3>`
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                self.ospf2 = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2()
                                self.ospf2.parent = self
                                self.ospf3 = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3()
                                self.ospf3.parent = self


                            class Ospf2(object):
                                """
                                OSPF v2
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:ospf2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf2']['meta_info']


                            class Ospf3(object):
                                """
                                OSPF v3
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:ospf3'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf.Ospf3']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.ospf2 is not None and self.ospf2._has_data():
                                    return True

                                if self.ospf2 is not None and self.ospf2.is_presence():
                                    return True

                                if self.ospf3 is not None and self.ospf3._has_data():
                                    return True

                                if self.ospf3 is not None and self.ospf3.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp.Ospf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.igp_common is not None and self.igp_common._has_data():
                                return True

                            if self.igp_common is not None and self.igp_common.is_presence():
                                return True

                            if self.is_is is not None and self.is_is._has_data():
                                return True

                            if self.is_is is not None and self.is_is.is_presence():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            if self.ospf is not None and self.ospf.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Igp']['meta_info']


                    class MplsTe(object):
                        """
                        MPLS and traffic engineering
                        
                        .. attribute:: global_
                        
                        	global MPLS configuration
                        	**type**\: :py:class:`Global <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global>`
                        
                        .. attribute:: label_switched_paths
                        
                        	models for different types of LSPs
                        	**type**\: :py:class:`LabelSwitchedPaths <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths>`
                        
                        .. attribute:: signaling
                        
                        	MPLS signaling protocols
                        	**type**\: :py:class:`Signaling <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling>`
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            self.global_ = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global()
                            self.global_.parent = self
                            self.label_switched_paths = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths()
                            self.label_switched_paths.parent = self
                            self.signaling = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling()
                            self.signaling.parent = self


                        class Global(object):
                            """
                            global MPLS configuration
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:global'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Global']['meta_info']


                        class LabelSwitchedPaths(object):
                            """
                            models for different types of LSPs
                            
                            .. attribute:: constrained_path
                            
                            	traffic\-engineered, or constrained path LSPs
                            	**type**\: :py:class:`ConstrainedPath <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath>`
                            
                            .. attribute:: igp_congruent
                            
                            	LSPs that follow the IGP\-computed path
                            	**type**\: :py:class:`IgpCongruent <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent>`
                            
                            .. attribute:: static
                            
                            	statically configured LSPs
                            	**type**\: :py:class:`Static <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static>`
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                self.constrained_path = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath()
                                self.constrained_path.parent = self
                                self.igp_congruent = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent()
                                self.igp_congruent.parent = self
                                self.static = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static()
                                self.static.parent = self


                            class ConstrainedPath(object):
                                """
                                traffic\-engineered, or constrained path LSPs
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:constrained-path'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.ConstrainedPath']['meta_info']


                            class IgpCongruent(object):
                                """
                                LSPs that follow the IGP\-computed path
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:igp-congruent'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.IgpCongruent']['meta_info']


                            class Static(object):
                                """
                                statically configured LSPs
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:static'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths.Static']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:label-switched-paths'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.constrained_path is not None and self.constrained_path._has_data():
                                    return True

                                if self.constrained_path is not None and self.constrained_path.is_presence():
                                    return True

                                if self.igp_congruent is not None and self.igp_congruent._has_data():
                                    return True

                                if self.igp_congruent is not None and self.igp_congruent.is_presence():
                                    return True

                                if self.static is not None and self.static._has_data():
                                    return True

                                if self.static is not None and self.static.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.LabelSwitchedPaths']['meta_info']


                        class Signaling(object):
                            """
                            MPLS signaling protocols
                            
                            .. attribute:: ldp
                            
                            	label distribution protocol
                            	**type**\: :py:class:`Ldp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp>`
                            
                            .. attribute:: rsvp
                            
                            	RSVP signaling
                            	**type**\: :py:class:`Rsvp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp>`
                            
                            .. attribute:: segment_routing
                            
                            	SR signaling
                            	**type**\: :py:class:`SegmentRouting <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting>`
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                self.ldp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp()
                                self.ldp.parent = self
                                self.rsvp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp()
                                self.rsvp.parent = self
                                self.segment_routing = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting()
                                self.segment_routing.parent = self


                            class Ldp(object):
                                """
                                label distribution protocol
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:ldp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Ldp']['meta_info']


                            class Rsvp(object):
                                """
                                RSVP signaling
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:rsvp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.Rsvp']['meta_info']


                            class SegmentRouting(object):
                                """
                                SR signaling
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:segment-routing'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling.SegmentRouting']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:signaling'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.ldp is not None and self.ldp._has_data():
                                    return True

                                if self.ldp is not None and self.ldp.is_presence():
                                    return True

                                if self.rsvp is not None and self.rsvp._has_data():
                                    return True

                                if self.rsvp is not None and self.rsvp.is_presence():
                                    return True

                                if self.segment_routing is not None and self.segment_routing._has_data():
                                    return True

                                if self.segment_routing is not None and self.segment_routing.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe.Signaling']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:mpls-te'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.global_ is not None and self.global_._has_data():
                                return True

                            if self.global_ is not None and self.global_.is_presence():
                                return True

                            if self.label_switched_paths is not None and self.label_switched_paths._has_data():
                                return True

                            if self.label_switched_paths is not None and self.label_switched_paths.is_presence():
                                return True

                            if self.signaling is not None and self.signaling._has_data():
                                return True

                            if self.signaling is not None and self.signaling.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.MplsTe']['meta_info']


                    class Pim(object):
                        """
                        protocol independent multicast
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:pim'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.Pim']['meta_info']


                    class StaticRoutes(object):
                        """
                        static route that are manually created
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:static-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global.StaticRoutes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:global'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.bfd is not None and self.bfd.is_presence():
                            return True

                        if self.bgp is not None and self.bgp._has_data():
                            return True

                        if self.bgp is not None and self.bgp.is_presence():
                            return True

                        if self.igmp is not None and self.igmp._has_data():
                            return True

                        if self.igmp is not None and self.igmp.is_presence():
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        if self.igp is not None and self.igp.is_presence():
                            return True

                        if self.mpls_te is not None and self.mpls_te._has_data():
                            return True

                        if self.mpls_te is not None and self.mpls_te.is_presence():
                            return True

                        if self.pim is not None and self.pim._has_data():
                            return True

                        if self.pim is not None and self.pim.is_presence():
                            return True

                        if self.static_routes is not None and self.static_routes._has_data():
                            return True

                        if self.static_routes is not None and self.static_routes.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Global']['meta_info']


                class RoutingPolicy(object):
                    """
                    models related to routing policy across
                    protocols and VRFs
                    
                    .. attribute:: bgp_policy
                    
                    	BGP\-specific routing policy parameters
                    	**type**\: :py:class:`BgpPolicy <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy>`
                    
                    .. attribute:: common
                    
                    	generic routing policy framework and configuration parameters
                    	**type**\: :py:class:`Common <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common>`
                    
                    .. attribute:: igp_policy
                    
                    	IGP routing policy knobs \-\- may include policy parameters for specific IGPs
                    	**type**\: :py:class:`IgpPolicy <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy>`
                    
                    .. attribute:: vrf_policy
                    
                    	import/export policies for VRFs
                    	**type**\: :py:class:`VrfPolicy <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy>`
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        self.bgp_policy = Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy()
                        self.bgp_policy.parent = self
                        self.common = Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common()
                        self.common.parent = self
                        self.igp_policy = Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy()
                        self.igp_policy.parent = self
                        self.vrf_policy = Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy()
                        self.vrf_policy.parent = self


                    class BgpPolicy(object):
                        """
                        BGP\-specific routing policy parameters
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:bgp-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.BgpPolicy']['meta_info']


                    class Common(object):
                        """
                        generic routing policy framework and
                        configuration parameters
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:common'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.Common']['meta_info']


                    class IgpPolicy(object):
                        """
                        IGP routing policy knobs \-\- may include
                        policy parameters for specific IGPs
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:igp-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.IgpPolicy']['meta_info']


                    class VrfPolicy(object):
                        """
                        import/export policies for VRFs
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:vrf-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy.VrfPolicy']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/model-structure:routing-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.bgp_policy is not None and self.bgp_policy._has_data():
                            return True

                        if self.bgp_policy is not None and self.bgp_policy.is_presence():
                            return True

                        if self.common is not None and self.common._has_data():
                            return True

                        if self.common is not None and self.common.is_presence():
                            return True

                        if self.igp_policy is not None and self.igp_policy._has_data():
                            return True

                        if self.igp_policy is not None and self.igp_policy.is_presence():
                            return True

                        if self.vrf_policy is not None and self.vrf_policy._has_data():
                            return True

                        if self.vrf_policy is not None and self.vrf_policy.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.RoutingPolicy']['meta_info']


                class Vrf(object):
                    """
                    list of VRF instances
                    
                    .. attribute:: vrf_name
                    
                    	name or id of the routing instance / VRF
                    	**type**\: str
                    
                    .. attribute:: bfd
                    
                    	bidirectional forwarding detection
                    	**type**\: :py:class:`Bfd <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd>`
                    
                    .. attribute:: bgp
                    
                    	BGP 4
                    	**type**\: :py:class:`Bgp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp>`
                    
                    .. attribute:: igmp
                    
                    	Internet group management protocol
                    	**type**\: :py:class:`Igmp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp>`
                    
                    .. attribute:: igp
                    
                    	interior gateway protocols
                    	**type**\: :py:class:`Igp <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp>`
                    
                    .. attribute:: pim
                    
                    	protocol independent multicast
                    	**type**\: :py:class:`Pim <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim>`
                    
                    .. attribute:: static_routes
                    
                    	static route that are manually created
                    	**type**\: :py:class:`StaticRoutes <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes>`
                    
                    

                    """

                    _prefix = 'struct'
                    _revision = '2015-03-06'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.bfd = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd()
                        self.bfd.parent = self
                        self.bgp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp()
                        self.bgp.parent = self
                        self.igmp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp()
                        self.igmp.parent = self
                        self.igp = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp()
                        self.igp.parent = self
                        self.pim = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim()
                        self.pim.parent = self
                        self.static_routes = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes()
                        self.static_routes.parent = self


                    class Bfd(object):
                        """
                        bidirectional forwarding detection
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bfd']['meta_info']


                    class Bgp(object):
                        """
                        BGP 4
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:bgp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Bgp']['meta_info']


                    class Igmp(object):
                        """
                        Internet group management protocol
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:igmp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igmp']['meta_info']


                    class Igp(object):
                        """
                        interior gateway protocols
                        
                        .. attribute:: igp_common
                        
                        	Common parameters for IGP protocols
                        	**type**\: :py:class:`IgpCommon <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon>`
                        
                        .. attribute:: is_is
                        
                        	IS\-IS IGP routing protocol
                        	**type**\: :py:class:`IsIs <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs>`
                        
                        .. attribute:: ospf
                        
                        	OSPF IGP routing protocols
                        	**type**\: :py:class:`Ospf <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            self.igp_common = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon()
                            self.igp_common.parent = self
                            self.is_is = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs()
                            self.is_is.parent = self
                            self.ospf = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf()
                            self.ospf.parent = self


                        class IgpCommon(object):
                            """
                            Common parameters for IGP protocols
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:igp-common'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IgpCommon']['meta_info']


                        class IsIs(object):
                            """
                            IS\-IS IGP routing protocol
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                pass

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:is-is'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.IsIs']['meta_info']


                        class Ospf(object):
                            """
                            OSPF IGP routing protocols
                            
                            .. attribute:: ospf2
                            
                            	OSPF v2
                            	**type**\: :py:class:`Ospf2 <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2>`
                            
                            .. attribute:: ospf3
                            
                            	OSPF v3
                            	**type**\: :py:class:`Ospf3 <ydk.models.model.model_structure.Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3>`
                            
                            

                            """

                            _prefix = 'struct'
                            _revision = '2015-03-06'

                            def __init__(self):
                                self.parent = None
                                self.ospf2 = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2()
                                self.ospf2.parent = self
                                self.ospf3 = Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3()
                                self.ospf3.parent = self


                            class Ospf2(object):
                                """
                                OSPF v2
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:ospf2'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf2']['meta_info']


                            class Ospf3(object):
                                """
                                OSPF v3
                                
                                

                                """

                                _prefix = 'struct'
                                _revision = '2015-03-06'

                                def __init__(self):
                                    self.parent = None
                                    pass

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/model-structure:ospf3'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.is_presence():
                                        return True
                                    return False

                                def is_presence(self):
                                    ''' Returns True if this instance represents presence container else returns False '''
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.model._meta import _model_structure as meta
                                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf.Ospf3']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/model-structure:ospf'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.is_presence():
                                    return True
                                if self.ospf2 is not None and self.ospf2._has_data():
                                    return True

                                if self.ospf2 is not None and self.ospf2.is_presence():
                                    return True

                                if self.ospf3 is not None and self.ospf3._has_data():
                                    return True

                                if self.ospf3 is not None and self.ospf3.is_presence():
                                    return True

                                return False

                            def is_presence(self):
                                ''' Returns True if this instance represents presence container else returns False '''
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.model._meta import _model_structure as meta
                                return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp.Ospf']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.igp_common is not None and self.igp_common._has_data():
                                return True

                            if self.igp_common is not None and self.igp_common.is_presence():
                                return True

                            if self.is_is is not None and self.is_is._has_data():
                                return True

                            if self.is_is is not None and self.is_is.is_presence():
                                return True

                            if self.ospf is not None and self.ospf._has_data():
                                return True

                            if self.ospf is not None and self.ospf.is_presence():
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Igp']['meta_info']


                    class Pim(object):
                        """
                        protocol independent multicast
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:pim'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.Pim']['meta_info']


                    class StaticRoutes(object):
                        """
                        static route that are manually created
                        
                        

                        """

                        _prefix = 'struct'
                        _revision = '2015-03-06'

                        def __init__(self):
                            self.parent = None
                            pass

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/model-structure:static-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.model._meta import _model_structure as meta
                            return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf.StaticRoutes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.vrf_name is None:
                            raise YPYDataValidationError('Key property vrf_name is None')

                        return self.parent._common_path +'/model-structure:vrf[model-structure:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.vrf_name is not None:
                            return True

                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.bfd is not None and self.bfd.is_presence():
                            return True

                        if self.bgp is not None and self.bgp._has_data():
                            return True

                        if self.bgp is not None and self.bgp.is_presence():
                            return True

                        if self.igmp is not None and self.igmp._has_data():
                            return True

                        if self.igmp is not None and self.igmp.is_presence():
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        if self.igp is not None and self.igp.is_presence():
                            return True

                        if self.pim is not None and self.pim._has_data():
                            return True

                        if self.pim is not None and self.pim.is_presence():
                            return True

                        if self.static_routes is not None and self.static_routes._has_data():
                            return True

                        if self.static_routes is not None and self.static_routes.is_presence():
                            return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.model._meta import _model_structure as meta
                        return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols.Vrf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/model-structure:layer-3-protocols'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.global_ is not None and self.global_._has_data():
                        return True

                    if self.global_ is not None and self.global_.is_presence():
                        return True

                    if self.routing_policy is not None and self.routing_policy._has_data():
                        return True

                    if self.routing_policy is not None and self.routing_policy.is_presence():
                        return True

                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.LogicalRouters.LogicalRouter.Layer3Protocols']['meta_info']

            @property
            def _common_path(self):
                if self.router_id is None:
                    raise YPYDataValidationError('Key property router_id is None')

                return '/model-structure:device/model-structure:logical-routers/model-structure:logical-router[model-structure:router-id = ' + str(self.router_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.router_id is not None:
                    return True

                if self.layer_2_protocols is not None and self.layer_2_protocols._has_data():
                    return True

                if self.layer_2_protocols is not None and self.layer_2_protocols.is_presence():
                    return True

                if self.layer_3_protocols is not None and self.layer_3_protocols._has_data():
                    return True

                if self.layer_3_protocols is not None and self.layer_3_protocols.is_presence():
                    return True

                if self.router_name is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.LogicalRouters.LogicalRouter']['meta_info']

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:logical-routers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.logical_router is not None:
                for child_ref in self.logical_router:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.LogicalRouters']['meta_info']


    class Qos(object):
        """
        QoS, including policing, shaping, etc.
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            pass

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:qos'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.Qos']['meta_info']


    class System(object):
        """
        system services
        
        .. attribute:: aaa
        
        	authentication, authorization, and accounting
        	**type**\: :py:class:`Aaa <ydk.models.model.model_structure.Device.System.Aaa>`
        
        .. attribute:: dhcp
        
        	dhcp and relay services
        	**type**\: :py:class:`Dhcp <ydk.models.model.model_structure.Device.System.Dhcp>`
        
        .. attribute:: dns
        
        	domain name service and resolver configurration
        	**type**\: :py:class:`Dns <ydk.models.model.model_structure.Device.System.Dns>`
        
        .. attribute:: ntp
        
        	network time protocol configuration
        	**type**\: :py:class:`Ntp <ydk.models.model.model_structure.Device.System.Ntp>`
        
        .. attribute:: oam
        
        	commonly use OAM functions on devices
        	**type**\: :py:class:`Oam <ydk.models.model.model_structure.Device.System.Oam>`
        
        .. attribute:: ssh
        
        	ssh server configuration
        	**type**\: :py:class:`Ssh <ydk.models.model.model_structure.Device.System.Ssh>`
        
        .. attribute:: stat_coll
        
        	mechanisms for data collection from devices, including packet and flow\-level sampling
        	**type**\: :py:class:`StatColl <ydk.models.model.model_structure.Device.System.StatColl>`
        
        .. attribute:: syslog
        
        	syslog configuration
        	**type**\: :py:class:`Syslog <ydk.models.model.model_structure.Device.System.Syslog>`
        
        .. attribute:: users
        
        	local user configuration
        	**type**\: :py:class:`Users <ydk.models.model.model_structure.Device.System.Users>`
        
        

        """

        _prefix = 'struct'
        _revision = '2015-03-06'

        def __init__(self):
            self.parent = None
            self.aaa = Device.System.Aaa()
            self.aaa.parent = self
            self.dhcp = Device.System.Dhcp()
            self.dhcp.parent = self
            self.dns = Device.System.Dns()
            self.dns.parent = self
            self.ntp = Device.System.Ntp()
            self.ntp.parent = self
            self.oam = Device.System.Oam()
            self.oam.parent = self
            self.ssh = Device.System.Ssh()
            self.ssh.parent = self
            self.stat_coll = Device.System.StatColl()
            self.stat_coll.parent = self
            self.syslog = Device.System.Syslog()
            self.syslog.parent = self
            self.users = Device.System.Users()
            self.users.parent = self


        class Aaa(object):
            """
            authentication, authorization, and accounting
            
            .. attribute:: radius
            
            	RADIUS
            	**type**\: :py:class:`Radius <ydk.models.model.model_structure.Device.System.Aaa.Radius>`
            
            .. attribute:: tacacs
            
            	TACACS+ configuration
            	**type**\: :py:class:`Tacacs <ydk.models.model.model_structure.Device.System.Aaa.Tacacs>`
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                self.radius = Device.System.Aaa.Radius()
                self.radius.parent = self
                self.tacacs = Device.System.Aaa.Tacacs()
                self.tacacs.parent = self


            class Radius(object):
                """
                RADIUS
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:system/model-structure:aaa/model-structure:radius'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.System.Aaa.Radius']['meta_info']


            class Tacacs(object):
                """
                TACACS+ configuration
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:system/model-structure:aaa/model-structure:tacacs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.System.Aaa.Tacacs']['meta_info']

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:aaa'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.radius is not None and self.radius._has_data():
                    return True

                if self.radius is not None and self.radius.is_presence():
                    return True

                if self.tacacs is not None and self.tacacs._has_data():
                    return True

                if self.tacacs is not None and self.tacacs.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Aaa']['meta_info']


        class Dhcp(object):
            """
            dhcp and relay services
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:dhcp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Dhcp']['meta_info']


        class Dns(object):
            """
            domain name service and resolver configurration
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:dns'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Dns']['meta_info']


        class Ntp(object):
            """
            network time protocol configuration
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:ntp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Ntp']['meta_info']


        class Oam(object):
            """
            commonly use OAM functions on devices
            
            .. attribute:: cfm
            
            	Ethernet connectivity fault management.  Also includes options that are associated with specific interfaces, such as maintenance endpoint domains
            	**type**\: :py:class:`Cfm <ydk.models.model.model_structure.Device.System.Oam.Cfm>`
            
            .. attribute:: snmp
            
            	SNMP server information, e.g., allowed clients
            	**type**\: :py:class:`Snmp <ydk.models.model.model_structure.Device.System.Oam.Snmp>`
            
            .. attribute:: twamp
            
            	Two\-way active measurement protocol for measuring round\-trip IP layer performance
            	**type**\: :py:class:`Twamp <ydk.models.model.model_structure.Device.System.Oam.Twamp>`
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                self.cfm = Device.System.Oam.Cfm()
                self.cfm.parent = self
                self.snmp = Device.System.Oam.Snmp()
                self.snmp.parent = self
                self.twamp = Device.System.Oam.Twamp()
                self.twamp.parent = self


            class Cfm(object):
                """
                Ethernet connectivity fault management.  Also includes
                options that are associated with specific interfaces, such
                as maintenance endpoint domains.
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:system/model-structure:oam/model-structure:cfm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.System.Oam.Cfm']['meta_info']


            class Snmp(object):
                """
                SNMP server information, e.g., allowed clients
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:system/model-structure:oam/model-structure:snmp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.System.Oam.Snmp']['meta_info']


            class Twamp(object):
                """
                Two\-way active measurement protocol for measuring
                round\-trip IP layer performance.
                
                

                """

                _prefix = 'struct'
                _revision = '2015-03-06'

                def __init__(self):
                    self.parent = None
                    pass

                @property
                def _common_path(self):

                    return '/model-structure:device/model-structure:system/model-structure:oam/model-structure:twamp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.model._meta import _model_structure as meta
                    return meta._meta_table['Device.System.Oam.Twamp']['meta_info']

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:oam'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cfm is not None and self.cfm._has_data():
                    return True

                if self.cfm is not None and self.cfm.is_presence():
                    return True

                if self.snmp is not None and self.snmp._has_data():
                    return True

                if self.snmp is not None and self.snmp.is_presence():
                    return True

                if self.twamp is not None and self.twamp._has_data():
                    return True

                if self.twamp is not None and self.twamp.is_presence():
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Oam']['meta_info']


        class Ssh(object):
            """
            ssh server configuration
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:ssh'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Ssh']['meta_info']


        class StatColl(object):
            """
            mechanisms for data collection from devices, including
            packet and flow\-level sampling
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:stat-coll'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.StatColl']['meta_info']


        class Syslog(object):
            """
            syslog configuration
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:syslog'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Syslog']['meta_info']


        class Users(object):
            """
            local user configuration
            
            

            """

            _prefix = 'struct'
            _revision = '2015-03-06'

            def __init__(self):
                self.parent = None
                pass

            @property
            def _common_path(self):

                return '/model-structure:device/model-structure:system/model-structure:users'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.model._meta import _model_structure as meta
                return meta._meta_table['Device.System.Users']['meta_info']

        @property
        def _common_path(self):

            return '/model-structure:device/model-structure:system'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.aaa is not None and self.aaa._has_data():
                return True

            if self.aaa is not None and self.aaa.is_presence():
                return True

            if self.dhcp is not None and self.dhcp._has_data():
                return True

            if self.dhcp is not None and self.dhcp.is_presence():
                return True

            if self.dns is not None and self.dns._has_data():
                return True

            if self.dns is not None and self.dns.is_presence():
                return True

            if self.ntp is not None and self.ntp._has_data():
                return True

            if self.ntp is not None and self.ntp.is_presence():
                return True

            if self.oam is not None and self.oam._has_data():
                return True

            if self.oam is not None and self.oam.is_presence():
                return True

            if self.ssh is not None and self.ssh._has_data():
                return True

            if self.ssh is not None and self.ssh.is_presence():
                return True

            if self.stat_coll is not None and self.stat_coll._has_data():
                return True

            if self.stat_coll is not None and self.stat_coll.is_presence():
                return True

            if self.syslog is not None and self.syslog._has_data():
                return True

            if self.syslog is not None and self.syslog.is_presence():
                return True

            if self.users is not None and self.users._has_data():
                return True

            if self.users is not None and self.users.is_presence():
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.model._meta import _model_structure as meta
            return meta._meta_table['Device.System']['meta_info']

    @property
    def _common_path(self):

        return '/model-structure:device'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.acl is not None and self.acl._has_data():
            return True

        if self.acl is not None and self.acl.is_presence():
            return True

        if self.hardware is not None and self.hardware._has_data():
            return True

        if self.hardware is not None and self.hardware.is_presence():
            return True

        if self.info is not None and self.info._has_data():
            return True

        if self.info is not None and self.info.is_presence():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.interfaces is not None and self.interfaces.is_presence():
            return True

        if self.logical_routers is not None and self.logical_routers._has_data():
            return True

        if self.logical_routers is not None and self.logical_routers.is_presence():
            return True

        if self.qos is not None and self.qos._has_data():
            return True

        if self.qos is not None and self.qos.is_presence():
            return True

        if self.system is not None and self.system._has_data():
            return True

        if self.system is not None and self.system.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.model._meta import _model_structure as meta
        return meta._meta_table['Device']['meta_info']


