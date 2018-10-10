""" Cisco_IOS_XR_ocni_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ocni package operational data.

This module contains definitions
for the following management objects\:
  ocni\-ni\-base\: An OpenConfig description of a network\-instance.
    This may be a Layer 3 forwarding construct such as a virtual
    routing and forwarding (VRF) instance, or a Layer 2 instance
    such as a virtual switch instance (VSI). Mixed Layer 2 and
    Layer 3 instances are also supaported. Copyright (c) 2017 by
    Cisco Systems, Inc.  All rights reserved.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OcniNiBase(Entity):
    """
    An OpenConfig description of a network\-instance.
    This may be a Layer 3 forwarding construct such
    as a virtual routing and forwarding (VRF)
    instance, or a Layer 2 instance such as a virtual
    switch instance (VSI). Mixed Layer 2 and Layer 3
    instances are also supaported. Copyright (c) 2017
    by Cisco Systems, Inc.  All rights reserved.
    
    .. attribute:: network_instances
    
    	Network instances configured on the local system
    	**type**\:  :py:class:`NetworkInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_oper.OcniNiBase.NetworkInstances>`
    
    

    """

    _prefix = 'ocni-oper'
    _revision = '2017-11-23'

    def __init__(self):
        super(OcniNiBase, self).__init__()
        self._top_entity = None

        self.yang_name = "ocni-ni-base"
        self.yang_parent_name = "Cisco-IOS-XR-ocni-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("network-instances", ("network_instances", OcniNiBase.NetworkInstances))])
        self._leafs = OrderedDict()

        self.network_instances = OcniNiBase.NetworkInstances()
        self.network_instances.parent = self
        self._children_name_map["network_instances"] = "network-instances"
        self._segment_path = lambda: "Cisco-IOS-XR-ocni-oper:ocni-ni-base"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OcniNiBase, [], name, value)


    class NetworkInstances(Entity):
        """
        Network instances configured on the local system
        
        .. attribute:: network_instance
        
        	Network instances configured on the local system
        	**type**\: list of  		 :py:class:`NetworkInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_oper.OcniNiBase.NetworkInstances.NetworkInstance>`
        
        

        """

        _prefix = 'ocni-oper'
        _revision = '2017-11-23'

        def __init__(self):
            super(OcniNiBase.NetworkInstances, self).__init__()

            self.yang_name = "network-instances"
            self.yang_parent_name = "ocni-ni-base"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("network-instance", ("network_instance", OcniNiBase.NetworkInstances.NetworkInstance))])
            self._leafs = OrderedDict()

            self.network_instance = YList(self)
            self._segment_path = lambda: "network-instances"
            self._absolute_path = lambda: "Cisco-IOS-XR-ocni-oper:ocni-ni-base/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OcniNiBase.NetworkInstances, [], name, value)


        class NetworkInstance(Entity):
            """
            Network instances configured on the local
            system
            
            .. attribute:: name  (key)
            
            	A unique name identifying the network instance
            	**type**\: str
            
            .. attribute:: state
            
            	Operational state parameters relating to a network instance
            	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ocni_oper.OcniNiBase.NetworkInstances.NetworkInstance.State>`
            
            

            """

            _prefix = 'ocni-oper'
            _revision = '2017-11-23'

            def __init__(self):
                super(OcniNiBase.NetworkInstances.NetworkInstance, self).__init__()

                self.yang_name = "network-instance"
                self.yang_parent_name = "network-instances"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("state", ("state", OcniNiBase.NetworkInstances.NetworkInstance.State))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.state = OcniNiBase.NetworkInstances.NetworkInstance.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "network-instance" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ocni-oper:ocni-ni-base/network-instances/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OcniNiBase.NetworkInstances.NetworkInstance, ['name'], name, value)


            class State(Entity):
                """
                Operational state parameters relating to a
                network instance
                
                .. attribute:: name
                
                	An operator\-assigned unique name for the forwarding instance
                	**type**\: str
                
                .. attribute:: type
                
                	The type of network instance. The value of this leaf indicates the type of forwarding entries that should be supported by this network instance
                	**type**\: str
                
                .. attribute:: enabled
                
                	Whether the network instance should be configured to be active on the network element
                	**type**\: bool
                
                .. attribute:: description
                
                	A free\-form string to be used by the network operator to describe the function of this network instance
                	**type**\: str
                
                .. attribute:: enabled_address_family
                
                	The address families that are to be enabled for this network instance
                	**type**\: list of str
                
                

                """

                _prefix = 'ocni-oper'
                _revision = '2017-11-23'

                def __init__(self):
                    super(OcniNiBase.NetworkInstances.NetworkInstance.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "network-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('enabled_address_family', (YLeafList(YType.str, 'enabled-address-family'), ['str'])),
                    ])
                    self.name = None
                    self.type = None
                    self.enabled = None
                    self.description = None
                    self.enabled_address_family = []
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OcniNiBase.NetworkInstances.NetworkInstance.State, [u'name', u'type', u'enabled', u'description', u'enabled_address_family'], name, value)

    def clone_ptr(self):
        self._top_entity = OcniNiBase()
        return self._top_entity

