""" Cisco_IOS_XR_ip_sbfd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-sbfd package configuration.

This module contains definitions
for the following management objects\:
  sbfd\: SBFD Configuration ,Seamless\-BFD is method for detecting
    faultsbetween two different nodes in a network

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Sbfd(Entity):
    """
    SBFD Configuration ,Seamless\-BFD is method for
    detecting faultsbetween two different nodes in a
    network
    
    .. attribute:: remote_target
    
    	configure remote target
    	**type**\:  :py:class:`RemoteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget>`
    
    .. attribute:: local_discriminator
    
    	Configure local discriminator
    	**type**\:  :py:class:`LocalDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator>`
    
    

    """

    _prefix = 'ip-sbfd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sbfd, self).__init__()
        self._top_entity = None

        self.yang_name = "sbfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-sbfd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("remote-target", ("remote_target", Sbfd.RemoteTarget)), ("local-discriminator", ("local_discriminator", Sbfd.LocalDiscriminator))])
        self._leafs = OrderedDict()

        self.remote_target = Sbfd.RemoteTarget()
        self.remote_target.parent = self
        self._children_name_map["remote_target"] = "remote-target"

        self.local_discriminator = Sbfd.LocalDiscriminator()
        self.local_discriminator.parent = self
        self._children_name_map["local_discriminator"] = "local-discriminator"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sbfd, [], name, value)


    class RemoteTarget(Entity):
        """
        configure remote target
        
        .. attribute:: ipv4_addresses
        
        	ipv4 address as target
        	**type**\:  :py:class:`Ipv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses>`
        
        .. attribute:: ipv6_addresses
        
        	ipv6 address as target
        	**type**\:  :py:class:`Ipv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses>`
        
        

        """

        _prefix = 'ip-sbfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sbfd.RemoteTarget, self).__init__()

            self.yang_name = "remote-target"
            self.yang_parent_name = "sbfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv4-addresses", ("ipv4_addresses", Sbfd.RemoteTarget.Ipv4Addresses)), ("ipv6-addresses", ("ipv6_addresses", Sbfd.RemoteTarget.Ipv6Addresses))])
            self._leafs = OrderedDict()

            self.ipv4_addresses = Sbfd.RemoteTarget.Ipv4Addresses()
            self.ipv4_addresses.parent = self
            self._children_name_map["ipv4_addresses"] = "ipv4-addresses"

            self.ipv6_addresses = Sbfd.RemoteTarget.Ipv6Addresses()
            self.ipv6_addresses.parent = self
            self._children_name_map["ipv6_addresses"] = "ipv6-addresses"
            self._segment_path = lambda: "remote-target"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sbfd.RemoteTarget, [], name, value)


        class Ipv4Addresses(Entity):
            """
            ipv4 address as target
            
            .. attribute:: ipv4_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of  		 :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.RemoteTarget.Ipv4Addresses, self).__init__()

                self.yang_name = "ipv4-addresses"
                self.yang_parent_name = "remote-target"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4-address", ("ipv4_address", Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address))])
                self._leafs = OrderedDict()

                self.ipv4_address = YList(self)
                self._segment_path = lambda: "ipv4-addresses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.RemoteTarget.Ipv4Addresses, [], name, value)


            class Ipv4Address(Entity):
                """
                IP Address Value for RemoteDiscriminatorTable
                
                .. attribute:: address  (key)
                
                	 IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_discriminator
                
                	Remote Discriminator value
                	**type**\: list of  		 :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address, self).__init__()

                    self.yang_name = "ipv4-address"
                    self.yang_parent_name = "ipv4-addresses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([("remote-discriminator", ("remote_discriminator", Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator))])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None

                    self.remote_discriminator = YList(self)
                    self._segment_path = lambda: "ipv4-address" + "[address='" + str(self.address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/ipv4-addresses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address, ['address'], name, value)


                class RemoteDiscriminator(Entity):
                    """
                    Remote Discriminator value
                    
                    .. attribute:: remote_discriminator  (key)
                    
                    	Remote Discriminator Value
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'ip-sbfd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "ipv4-address"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['remote_discriminator']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('remote_discriminator', (YLeaf(YType.uint32, 'remote-discriminator'), ['int'])),
                        ])
                        self.remote_discriminator = None
                        self._segment_path = lambda: "remote-discriminator" + "[remote-discriminator='" + str(self.remote_discriminator) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator, ['remote_discriminator'], name, value)


        class Ipv6Addresses(Entity):
            """
            ipv6 address as target
            
            .. attribute:: ipv6_address
            
            	IP Address Value for RemoteDiscriminatorTable
            	**type**\: list of  		 :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.RemoteTarget.Ipv6Addresses, self).__init__()

                self.yang_name = "ipv6-addresses"
                self.yang_parent_name = "remote-target"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv6-address", ("ipv6_address", Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address))])
                self._leafs = OrderedDict()

                self.ipv6_address = YList(self)
                self._segment_path = lambda: "ipv6-addresses"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.RemoteTarget.Ipv6Addresses, [], name, value)


            class Ipv6Address(Entity):
                """
                IP Address Value for RemoteDiscriminatorTable
                
                .. attribute:: address  (key)
                
                	 IPv6 adddress
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_discriminator
                
                	Remote Discriminator value
                	**type**\: list of  		 :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address, self).__init__()

                    self.yang_name = "ipv6-address"
                    self.yang_parent_name = "ipv6-addresses"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([("remote-discriminator", ("remote_discriminator", Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator))])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ])
                    self.address = None

                    self.remote_discriminator = YList(self)
                    self._segment_path = lambda: "ipv6-address" + "[address='" + str(self.address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/remote-target/ipv6-addresses/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address, ['address'], name, value)


                class RemoteDiscriminator(Entity):
                    """
                    Remote Discriminator value
                    
                    .. attribute:: remote_discriminator  (key)
                    
                    	Remote Discriminator Value
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'ip-sbfd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "ipv6-address"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['remote_discriminator']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('remote_discriminator', (YLeaf(YType.uint32, 'remote-discriminator'), ['int'])),
                        ])
                        self.remote_discriminator = None
                        self._segment_path = lambda: "remote-discriminator" + "[remote-discriminator='" + str(self.remote_discriminator) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator, ['remote_discriminator'], name, value)


    class LocalDiscriminator(Entity):
        """
        Configure local discriminator
        
        .. attribute:: intf_discriminators
        
        	Configure local discriminator from interface address
        	**type**\:  :py:class:`IntfDiscriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.IntfDiscriminators>`
        
        .. attribute:: dynamic_discriminators
        
        	Configure local discriminator dynamically
        	**type**\:  :py:class:`DynamicDiscriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.DynamicDiscriminators>`
        
        .. attribute:: ipv4_discriminators
        
        	Configure local discriminator as an ipv4 address
        	**type**\:  :py:class:`Ipv4Discriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Ipv4Discriminators>`
        
        .. attribute:: val32_discriminators
        
        	Configure local discriminator as an integer
        	**type**\:  :py:class:`Val32Discriminators <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Val32Discriminators>`
        
        

        """

        _prefix = 'ip-sbfd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sbfd.LocalDiscriminator, self).__init__()

            self.yang_name = "local-discriminator"
            self.yang_parent_name = "sbfd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("intf-discriminators", ("intf_discriminators", Sbfd.LocalDiscriminator.IntfDiscriminators)), ("dynamic-discriminators", ("dynamic_discriminators", Sbfd.LocalDiscriminator.DynamicDiscriminators)), ("ipv4-discriminators", ("ipv4_discriminators", Sbfd.LocalDiscriminator.Ipv4Discriminators)), ("val32-discriminators", ("val32_discriminators", Sbfd.LocalDiscriminator.Val32Discriminators))])
            self._leafs = OrderedDict()

            self.intf_discriminators = Sbfd.LocalDiscriminator.IntfDiscriminators()
            self.intf_discriminators.parent = self
            self._children_name_map["intf_discriminators"] = "intf-discriminators"

            self.dynamic_discriminators = Sbfd.LocalDiscriminator.DynamicDiscriminators()
            self.dynamic_discriminators.parent = self
            self._children_name_map["dynamic_discriminators"] = "dynamic-discriminators"

            self.ipv4_discriminators = Sbfd.LocalDiscriminator.Ipv4Discriminators()
            self.ipv4_discriminators.parent = self
            self._children_name_map["ipv4_discriminators"] = "ipv4-discriminators"

            self.val32_discriminators = Sbfd.LocalDiscriminator.Val32Discriminators()
            self.val32_discriminators.parent = self
            self._children_name_map["val32_discriminators"] = "val32-discriminators"
            self._segment_path = lambda: "local-discriminator"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Sbfd.LocalDiscriminator, [], name, value)


        class IntfDiscriminators(Entity):
            """
            Configure local discriminator from interface
            address
            
            .. attribute:: intf_discriminator
            
            	interface address as discriminator
            	**type**\: list of  		 :py:class:`IntfDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.IntfDiscriminators, self).__init__()

                self.yang_name = "intf-discriminators"
                self.yang_parent_name = "local-discriminator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("intf-discriminator", ("intf_discriminator", Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator))])
                self._leafs = OrderedDict()

                self.intf_discriminator = YList(self)
                self._segment_path = lambda: "intf-discriminators"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.LocalDiscriminator.IntfDiscriminators, [], name, value)


            class IntfDiscriminator(Entity):
                """
                interface address as discriminator
                
                .. attribute:: interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator, self).__init__()

                    self.yang_name = "intf-discriminator"
                    self.yang_parent_name = "intf-discriminators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ])
                    self.interface_name = None
                    self._segment_path = lambda: "intf-discriminator" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/intf-discriminators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator, ['interface_name'], name, value)


        class DynamicDiscriminators(Entity):
            """
            Configure local discriminator dynamically
            
            .. attribute:: dynamic_discriminator
            
            	Local discriminator value
            	**type**\: list of  		 :py:class:`DynamicDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.DynamicDiscriminators, self).__init__()

                self.yang_name = "dynamic-discriminators"
                self.yang_parent_name = "local-discriminator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("dynamic-discriminator", ("dynamic_discriminator", Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator))])
                self._leafs = OrderedDict()

                self.dynamic_discriminator = YList(self)
                self._segment_path = lambda: "dynamic-discriminators"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.LocalDiscriminator.DynamicDiscriminators, [], name, value)


            class DynamicDiscriminator(Entity):
                """
                Local discriminator value
                
                .. attribute:: discriminator  (key)
                
                	Dynamic discriminator value
                	**type**\: int
                
                	**range:** 0..1
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator, self).__init__()

                    self.yang_name = "dynamic-discriminator"
                    self.yang_parent_name = "dynamic-discriminators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['discriminator']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('discriminator', (YLeaf(YType.uint32, 'discriminator'), ['int'])),
                    ])
                    self.discriminator = None
                    self._segment_path = lambda: "dynamic-discriminator" + "[discriminator='" + str(self.discriminator) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/dynamic-discriminators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator, ['discriminator'], name, value)


        class Ipv4Discriminators(Entity):
            """
            Configure local discriminator as an ipv4
            address
            
            .. attribute:: ipv4_discriminator
            
            	ipv4 address as discriminator
            	**type**\: list of  		 :py:class:`Ipv4Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.Ipv4Discriminators, self).__init__()

                self.yang_name = "ipv4-discriminators"
                self.yang_parent_name = "local-discriminator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4-discriminator", ("ipv4_discriminator", Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator))])
                self._leafs = OrderedDict()

                self.ipv4_discriminator = YList(self)
                self._segment_path = lambda: "ipv4-discriminators"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.LocalDiscriminator.Ipv4Discriminators, [], name, value)


            class Ipv4Discriminator(Entity):
                """
                ipv4 address as discriminator
                
                .. attribute:: address  (key)
                
                	 IPv4 address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator, self).__init__()

                    self.yang_name = "ipv4-discriminator"
                    self.yang_parent_name = "ipv4-discriminators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                    ])
                    self.address = None
                    self._segment_path = lambda: "ipv4-discriminator" + "[address='" + str(self.address) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/ipv4-discriminators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator, ['address'], name, value)


        class Val32Discriminators(Entity):
            """
            Configure local discriminator as an integer
            
            .. attribute:: val32_discriminator
            
            	Local discriminator value
            	**type**\: list of  		 :py:class:`Val32Discriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg.Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator>`
            
            

            """

            _prefix = 'ip-sbfd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.LocalDiscriminator.Val32Discriminators, self).__init__()

                self.yang_name = "val32-discriminators"
                self.yang_parent_name = "local-discriminator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("val32-discriminator", ("val32_discriminator", Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator))])
                self._leafs = OrderedDict()

                self.val32_discriminator = YList(self)
                self._segment_path = lambda: "val32-discriminators"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Sbfd.LocalDiscriminator.Val32Discriminators, [], name, value)


            class Val32Discriminator(Entity):
                """
                Local discriminator value
                
                .. attribute:: discriminator  (key)
                
                	Local discriminator value
                	**type**\: int
                
                	**range:** 1..4294967295
                
                

                """

                _prefix = 'ip-sbfd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator, self).__init__()

                    self.yang_name = "val32-discriminator"
                    self.yang_parent_name = "val32-discriminators"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['discriminator']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('discriminator', (YLeaf(YType.uint32, 'discriminator'), ['int'])),
                    ])
                    self.discriminator = None
                    self._segment_path = lambda: "val32-discriminator" + "[discriminator='" + str(self.discriminator) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-sbfd-cfg:sbfd/local-discriminator/val32-discriminators/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator, ['discriminator'], name, value)

    def clone_ptr(self):
        self._top_entity = Sbfd()
        return self._top_entity

