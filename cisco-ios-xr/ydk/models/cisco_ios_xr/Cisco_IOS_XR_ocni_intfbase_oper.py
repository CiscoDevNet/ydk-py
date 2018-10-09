""" Cisco_IOS_XR_ocni_intfbase_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ocni\-intfbase package operational data.

This module contains definitions
for the following management objects\:
  ocni\-ni\-intfbase\: An OpenConfig description of a
    network\-instance. This may be a Layer 3 forwarding construct
    such as a virtual routing and forwarding (VRF) instance, or
    a Layer 2 instance such as a virtual switch instance (VSI).
    Mixed Layer 2 and Layer 3 instances are also supported.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OcniNiIntfbase(Entity):
    """
    An OpenConfig description of a network\-instance.
    This may be a Layer 3 forwarding construct such
    as a virtual routing and forwarding (VRF)
    instance, or a Layer 2 instance such as a virtual
    switch instance (VSI). Mixed Layer 2 and Layer 3
    instances are also supported.
    
    .. attribute:: network_instances
    
    	Network instances configured on the local system
    	**type**\:  :py:class:`NetworkInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_intfbase_oper.OcniNiIntfbase.NetworkInstances>`
    
    

    """

    _prefix = 'ocni-intfbase-oper'
    _revision = '2017-11-23'

    def __init__(self):
        super(OcniNiIntfbase, self).__init__()
        self._top_entity = None

        self.yang_name = "ocni-ni-intfbase"
        self.yang_parent_name = "Cisco-IOS-XR-ocni-intfbase-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("network-instances", ("network_instances", OcniNiIntfbase.NetworkInstances))])
        self._leafs = OrderedDict()

        self.network_instances = OcniNiIntfbase.NetworkInstances()
        self.network_instances.parent = self
        self._children_name_map["network_instances"] = "network-instances"
        self._segment_path = lambda: "Cisco-IOS-XR-ocni-intfbase-oper:ocni-ni-intfbase"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OcniNiIntfbase, [], name, value)


    class NetworkInstances(Entity):
        """
        Network instances configured on the local system
        
        .. attribute:: network_instance
        
        	Network instances configured on the local system
        	**type**\: list of  		 :py:class:`NetworkInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_intfbase_oper.OcniNiIntfbase.NetworkInstances.NetworkInstance>`
        
        

        """

        _prefix = 'ocni-intfbase-oper'
        _revision = '2017-11-23'

        def __init__(self):
            super(OcniNiIntfbase.NetworkInstances, self).__init__()

            self.yang_name = "network-instances"
            self.yang_parent_name = "ocni-ni-intfbase"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("network-instance", ("network_instance", OcniNiIntfbase.NetworkInstances.NetworkInstance))])
            self._leafs = OrderedDict()

            self.network_instance = YList(self)
            self._segment_path = lambda: "network-instances"
            self._absolute_path = lambda: "Cisco-IOS-XR-ocni-intfbase-oper:ocni-ni-intfbase/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OcniNiIntfbase.NetworkInstances, [], name, value)


        class NetworkInstance(Entity):
            """
            Network instances configured on the local
            system
            
            .. attribute:: name  (key)
            
            	A unique name identifying the network instance
            	**type**\: str
            
            .. attribute:: interfaces
            
            	An interface associated with the network instance
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_intfbase_oper.OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces>`
            
            

            """

            _prefix = 'ocni-intfbase-oper'
            _revision = '2017-11-23'

            def __init__(self):
                super(OcniNiIntfbase.NetworkInstances.NetworkInstance, self).__init__()

                self.yang_name = "network-instance"
                self.yang_parent_name = "network-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("interfaces", ("interfaces", OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.interfaces = OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "network-instance" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ocni-intfbase-oper:ocni-ni-intfbase/network-instances/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OcniNiIntfbase.NetworkInstances.NetworkInstance, ['name'], name, value)


            class Interfaces(Entity):
                """
                An interface associated with the network
                instance
                
                .. attribute:: interface
                
                	An interface associated with the network instance
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_intfbase_oper.OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface>`
                
                

                """

                _prefix = 'ocni-intfbase-oper'
                _revision = '2017-11-23'

                def __init__(self):
                    super(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "network-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    An interface associated with the network
                    instance
                    
                    .. attribute:: id  (key)
                    
                    	A reference to an identifier for this interface which acts as a key for this list
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the associated interface
                    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_intfbase_oper.OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface.State>`
                    
                    

                    """

                    _prefix = 'ocni-intfbase-oper'
                    _revision = '2017-11-23'

                    def __init__(self):
                        super(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id']
                        self._child_classes = OrderedDict([("state", ("state", OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface.State))])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.str, 'id'), ['str'])),
                        ])
                        self.id = None

                        self.state = OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "interface" + "[id='" + str(self.id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface, ['id'], name, value)


                    class State(Entity):
                        """
                        Operational state parameters relating to the
                        associated interface
                        
                        .. attribute:: id
                        
                        	A unique identifier for this interface \- this is expressed as a free\-text string
                        	**type**\: str
                        
                        .. attribute:: interface
                        
                        	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                        	**type**\: str
                        
                        .. attribute:: subinterface
                        
                        	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: associated_address_family
                        
                        	The address families on the subinterface which are to be associated with this network instance. When this leaf\-list is empty and the network instance requires Layer 3 information the address families for which the network instance is enabled should be imported. If the value of this leaf\-list is specified then the association MUST only be made for those address families that are included in the list
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'ocni-intfbase-oper'
                        _revision = '2017-11-23'

                        def __init__(self):
                            super(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', (YLeaf(YType.str, 'id'), ['str'])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('subinterface', (YLeaf(YType.uint32, 'subinterface'), ['int'])),
                                ('associated_address_family', (YLeafList(YType.str, 'associated-address-family'), ['str'])),
                            ])
                            self.id = None
                            self.interface = None
                            self.subinterface = None
                            self.associated_address_family = []
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OcniNiIntfbase.NetworkInstances.NetworkInstance.Interfaces.Interface.State, [u'id', u'interface', u'subinterface', u'associated_address_family'], name, value)

    def clone_ptr(self):
        self._top_entity = OcniNiIntfbase()
        return self._top_entity

