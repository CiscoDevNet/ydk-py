""" Cisco_IOS_XR_fia_hw_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-hw\-profile package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-profile\-config\: none

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class HwModuleProfileConfig(Entity):
    """
    none
    
    .. attribute:: profile
    
    	Configure profile
    	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile>`
    
    .. attribute:: fib_scale
    
    	Configure Fib for Scale for noTcam LC
    	**type**\:  :py:class:`FibScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale>`
    
    .. attribute:: orchestrated_linecard_reload
    
    	Configure OLR
    	**type**\:  :py:class:`OrchestratedLinecardReload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.OrchestratedLinecardReload>`
    
    .. attribute:: tcam
    
    	Configure Tcam
    	**type**\:  :py:class:`Tcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam>`
    
    .. attribute:: qosqppb
    
    	Configure profile
    	**type**\:  :py:class:`Qosqppb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Qosqppb>`
    
    

    """

    _prefix = 'fia-hw-profile-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        super(HwModuleProfileConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module-profile-config"
        self.yang_parent_name = "Cisco-IOS-XR-fia-hw-profile-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("profile", ("profile", HwModuleProfileConfig.Profile)), ("fib-scale", ("fib_scale", HwModuleProfileConfig.FibScale)), ("orchestrated-linecard-reload", ("orchestrated_linecard_reload", HwModuleProfileConfig.OrchestratedLinecardReload)), ("tcam", ("tcam", HwModuleProfileConfig.Tcam)), ("qosqppb", ("qosqppb", HwModuleProfileConfig.Qosqppb))])
        self._leafs = OrderedDict()

        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self
        self._children_name_map["profile"] = "profile"

        self.fib_scale = HwModuleProfileConfig.FibScale()
        self.fib_scale.parent = self
        self._children_name_map["fib_scale"] = "fib-scale"

        self.orchestrated_linecard_reload = HwModuleProfileConfig.OrchestratedLinecardReload()
        self.orchestrated_linecard_reload.parent = self
        self._children_name_map["orchestrated_linecard_reload"] = "orchestrated-linecard-reload"

        self.tcam = HwModuleProfileConfig.Tcam()
        self.tcam.parent = self
        self._children_name_map["tcam"] = "tcam"

        self.qosqppb = HwModuleProfileConfig.Qosqppb()
        self.qosqppb.parent = self
        self._children_name_map["qosqppb"] = "qosqppb"
        self._segment_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(HwModuleProfileConfig, [], name, value)


    class Profile(Entity):
        """
        Configure profile.
        
        .. attribute:: tcam_table
        
        	Configure profile for TCAM LC cards
        	**type**\:  :py:class:`TcamTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable>`
        
        .. attribute:: netflow
        
        	Configure Netflow profile
        	**type**\:  :py:class:`Netflow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflow>`
        
        .. attribute:: flowspecs
        
        	Configure Flowspec profile
        	**type**\:  :py:class:`Flowspecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Flowspecs>`
        
        .. attribute:: segment_routings
        
        	Configure Segment Routing profile
        	**type**\:  :py:class:`SegmentRoutings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.SegmentRoutings>`
        
        .. attribute:: load_balance
        
        	Configure load balance parameters
        	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.LoadBalance>`
        
        .. attribute:: stats
        
        	Configure stats
        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Stats>`
        
        .. attribute:: profile_acl
        
        	Configure acl profile
        	**type**\:  :py:class:`ProfileAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileAcl>`
        
        .. attribute:: bundle_scale
        
        	Configure Bundle profile
        	**type**\:  :py:class:`BundleScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.BundleScale>`
        
        .. attribute:: profile_tcam
        
        	Configure Tcam Profile
        	**type**\:  :py:class:`ProfileTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam>`
        
        .. attribute:: qos
        
        	Configure profile
        	**type**\:  :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Profile, self).__init__()

            self.yang_name = "profile"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tcam-table", ("tcam_table", HwModuleProfileConfig.Profile.TcamTable)), ("netflow", ("netflow", HwModuleProfileConfig.Profile.Netflow)), ("flowspecs", ("flowspecs", HwModuleProfileConfig.Profile.Flowspecs)), ("segment-routings", ("segment_routings", HwModuleProfileConfig.Profile.SegmentRoutings)), ("load-balance", ("load_balance", HwModuleProfileConfig.Profile.LoadBalance)), ("stats", ("stats", HwModuleProfileConfig.Profile.Stats)), ("profile-acl", ("profile_acl", HwModuleProfileConfig.Profile.ProfileAcl)), ("bundle-scale", ("bundle_scale", HwModuleProfileConfig.Profile.BundleScale)), ("profile-tcam", ("profile_tcam", HwModuleProfileConfig.Profile.ProfileTcam)), ("qos", ("qos", HwModuleProfileConfig.Profile.Qos))])
            self._leafs = OrderedDict()

            self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
            self.tcam_table.parent = self
            self._children_name_map["tcam_table"] = "tcam-table"

            self.netflow = HwModuleProfileConfig.Profile.Netflow()
            self.netflow.parent = self
            self._children_name_map["netflow"] = "netflow"

            self.flowspecs = HwModuleProfileConfig.Profile.Flowspecs()
            self.flowspecs.parent = self
            self._children_name_map["flowspecs"] = "flowspecs"

            self.segment_routings = HwModuleProfileConfig.Profile.SegmentRoutings()
            self.segment_routings.parent = self
            self._children_name_map["segment_routings"] = "segment-routings"

            self.load_balance = HwModuleProfileConfig.Profile.LoadBalance()
            self.load_balance.parent = self
            self._children_name_map["load_balance"] = "load-balance"

            self.stats = HwModuleProfileConfig.Profile.Stats()
            self.stats.parent = self
            self._children_name_map["stats"] = "stats"

            self.profile_acl = HwModuleProfileConfig.Profile.ProfileAcl()
            self.profile_acl.parent = self
            self._children_name_map["profile_acl"] = "profile-acl"

            self.bundle_scale = HwModuleProfileConfig.Profile.BundleScale()
            self.bundle_scale.parent = self
            self._children_name_map["bundle_scale"] = "bundle-scale"

            self.profile_tcam = HwModuleProfileConfig.Profile.ProfileTcam()
            self.profile_tcam.parent = self
            self._children_name_map["profile_tcam"] = "profile-tcam"

            self.qos = HwModuleProfileConfig.Profile.Qos()
            self.qos.parent = self
            self._children_name_map["qos"] = "qos"
            self._segment_path = lambda: "profile"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleProfileConfig.Profile, [], name, value)


        class TcamTable(Entity):
            """
            Configure profile for TCAM LC cards
            
            .. attribute:: fib_table
            
            	FIB table for TCAM LC cards
            	**type**\:  :py:class:`FibTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.TcamTable, self).__init__()

                self.yang_name = "tcam-table"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("fib-table", ("fib_table", HwModuleProfileConfig.Profile.TcamTable.FibTable))])
                self._leafs = OrderedDict()

                self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                self.fib_table.parent = self
                self._children_name_map["fib_table"] = "fib-table"
                self._segment_path = lambda: "tcam-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable, [], name, value)


            class FibTable(Entity):
                """
                FIB table for TCAM LC cards
                
                .. attribute:: ipv4_address
                
                	IPv4 table for TCAM LC cards
                	**type**\:  :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address>`
                
                .. attribute:: ipv6_address
                
                	IPv6 table for TCAM LC cards
                	**type**\:  :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable, self).__init__()

                    self.yang_name = "fib-table"
                    self.yang_parent_name = "tcam-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv4-address", ("ipv4_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address)), ("ipv6-address", ("ipv6_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address))])
                    self._leafs = OrderedDict()

                    self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                    self.ipv4_address.parent = self
                    self._children_name_map["ipv4_address"] = "ipv4-address"

                    self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                    self.ipv6_address.parent = self
                    self._children_name_map["ipv6_address"] = "ipv6-address"
                    self._segment_path = lambda: "fib-table"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable, [], name, value)


                class Ipv4Address(Entity):
                    """
                    IPv4 table for TCAM LC cards
                    
                    .. attribute:: ipv4_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:  :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address, self).__init__()

                        self.yang_name = "ipv4-address"
                        self.yang_parent_name = "fib-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-unicast", ("ipv4_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast))])
                        self._leafs = OrderedDict()

                        self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._segment_path = lambda: "ipv4-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address, [], name, value)


                    class Ipv4Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv4_unicast_prefix_lengths
                        
                        	IPv4 Unicast prefix 
                        	**type**\:  :py:class:`Ipv4UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths>`
                        
                        .. attribute:: ipv4_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, self).__init__()

                            self.yang_name = "ipv4-unicast"
                            self.yang_parent_name = "ipv4-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4-unicast-prefix-lengths", ("ipv4_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths))])
                            self._leafs = OrderedDict([
                                ('ipv4_unicast_percent', (YLeaf(YType.uint32, 'ipv4-unicast-percent'), ['int'])),
                            ])
                            self.ipv4_unicast_percent = None

                            self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                            self.ipv4_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv4_unicast_prefix_lengths"] = "ipv4-unicast-prefix-lengths"
                            self._segment_path = lambda: "ipv4-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, ['ipv4_unicast_percent'], name, value)


                        class Ipv4UnicastPrefixLengths(Entity):
                            """
                            IPv4 Unicast prefix 
                            
                            .. attribute:: ipv4_unicast_prefix_length
                            
                            	IPv4 Unicast prefix length
                            	**type**\: list of  		 :py:class:`Ipv4UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv4-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-unicast-prefix-length", ("ipv4_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength))])
                                self._leafs = OrderedDict()

                                self.ipv4_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv4-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, [], name, value)


                            class Ipv4UnicastPrefixLength(Entity):
                                """
                                IPv4 Unicast prefix length
                                
                                .. attribute:: prefix_length  (key)
                                
                                	prefix length
                                	**type**\: int
                                
                                	**range:** 0..32
                                
                                .. attribute:: ipv4_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\: str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv4-unicast-prefix-length"
                                    self.yang_parent_name = "ipv4-unicast-prefix-lengths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = ['prefix_length']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                        ('ipv4_unicast_prefix_percent', (YLeaf(YType.str, 'ipv4-unicast-prefix-percent'), ['str'])),
                                    ])
                                    self.prefix_length = None
                                    self.ipv4_unicast_prefix_percent = None
                                    self._segment_path = lambda: "ipv4-unicast-prefix-length" + "[prefix-length='" + str(self.prefix_length) + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/ipv4-unicast-prefix-lengths/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, ['prefix_length', 'ipv4_unicast_prefix_percent'], name, value)


                class Ipv6Address(Entity):
                    """
                    IPv6 table for TCAM LC cards
                    
                    .. attribute:: ipv6_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:  :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address, self).__init__()

                        self.yang_name = "ipv6-address"
                        self.yang_parent_name = "fib-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv6-unicast", ("ipv6_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast))])
                        self._leafs = OrderedDict()

                        self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._segment_path = lambda: "ipv6-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address, [], name, value)


                    class Ipv6Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv6_unicast_prefix_lengths
                        
                        	IPv6 Unicast prefix 
                        	**type**\:  :py:class:`Ipv6UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths>`
                        
                        .. attribute:: ipv6_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, self).__init__()

                            self.yang_name = "ipv6-unicast"
                            self.yang_parent_name = "ipv6-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv6-unicast-prefix-lengths", ("ipv6_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths))])
                            self._leafs = OrderedDict([
                                ('ipv6_unicast_percent', (YLeaf(YType.uint32, 'ipv6-unicast-percent'), ['int'])),
                            ])
                            self.ipv6_unicast_percent = None

                            self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                            self.ipv6_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv6_unicast_prefix_lengths"] = "ipv6-unicast-prefix-lengths"
                            self._segment_path = lambda: "ipv6-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, ['ipv6_unicast_percent'], name, value)


                        class Ipv6UnicastPrefixLengths(Entity):
                            """
                            IPv6 Unicast prefix 
                            
                            .. attribute:: ipv6_unicast_prefix_length
                            
                            	IPv6 Unicast prefix length
                            	**type**\: list of  		 :py:class:`Ipv6UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv6-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv6-unicast-prefix-length", ("ipv6_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength))])
                                self._leafs = OrderedDict()

                                self.ipv6_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv6-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, [], name, value)


                            class Ipv6UnicastPrefixLength(Entity):
                                """
                                IPv6 Unicast prefix length
                                
                                .. attribute:: prefix_length  (key)
                                
                                	prefix length
                                	**type**\: int
                                
                                	**range:** 0..128
                                
                                .. attribute:: ipv6_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\: str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv6-unicast-prefix-length"
                                    self.yang_parent_name = "ipv6-unicast-prefix-lengths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = ['prefix_length']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                        ('ipv6_unicast_prefix_percent', (YLeaf(YType.str, 'ipv6-unicast-prefix-percent'), ['str'])),
                                    ])
                                    self.prefix_length = None
                                    self.ipv6_unicast_prefix_percent = None
                                    self._segment_path = lambda: "ipv6-unicast-prefix-length" + "[prefix-length='" + str(self.prefix_length) + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/ipv6-unicast-prefix-lengths/%s" % self._segment_path()
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, ['prefix_length', 'ipv6_unicast_prefix_percent'], name, value)


        class Netflow(Entity):
            """
            Configure Netflow profile.
            
            .. attribute:: netflow_locations
            
            	none
            	**type**\:  :py:class:`NetflowLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflow.NetflowLocations>`
            
            .. attribute:: location_all
            
            	IPFIX315 Location All
            	**type**\:  :py:class:`LocationAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflow.LocationAll>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Netflow, self).__init__()

                self.yang_name = "netflow"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("netflow-locations", ("netflow_locations", HwModuleProfileConfig.Profile.Netflow.NetflowLocations)), ("location-all", ("location_all", HwModuleProfileConfig.Profile.Netflow.LocationAll))])
                self._leafs = OrderedDict()

                self.netflow_locations = HwModuleProfileConfig.Profile.Netflow.NetflowLocations()
                self.netflow_locations.parent = self
                self._children_name_map["netflow_locations"] = "netflow-locations"

                self.location_all = HwModuleProfileConfig.Profile.Netflow.LocationAll()
                self.location_all.parent = self
                self._children_name_map["location_all"] = "location-all"
                self._segment_path = lambda: "netflow"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Netflow, [], name, value)


            class NetflowLocations(Entity):
                """
                none
                
                .. attribute:: netflow_location
                
                	none
                	**type**\: list of  		 :py:class:`NetflowLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Netflow.NetflowLocations, self).__init__()

                    self.yang_name = "netflow-locations"
                    self.yang_parent_name = "netflow"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("netflow-location", ("netflow_location", HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation))])
                    self._leafs = OrderedDict()

                    self.netflow_location = YList(self)
                    self._segment_path = lambda: "netflow-locations"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/netflow/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Netflow.NetflowLocations, [], name, value)


                class NetflowLocation(Entity):
                    """
                    none
                    
                    .. attribute:: location_string  (key)
                    
                    	Location of NETFLOW config
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: netflow_location_leaf
                    
                    	none
                    	**type**\: list of  		 :py:class:`NetflowLocationLeaf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation.NetflowLocationLeaf>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation, self).__init__()

                        self.yang_name = "netflow-location"
                        self.yang_parent_name = "netflow-locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['location_string']
                        self._child_classes = OrderedDict([("netflow-location-leaf", ("netflow_location_leaf", HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation.NetflowLocationLeaf))])
                        self._leafs = OrderedDict([
                            ('location_string', (YLeaf(YType.str, 'location-string'), ['str'])),
                        ])
                        self.location_string = None

                        self.netflow_location_leaf = YList(self)
                        self._segment_path = lambda: "netflow-location" + "[location-string='" + str(self.location_string) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/netflow/netflow-locations/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation, ['location_string'], name, value)


                    class NetflowLocationLeaf(Entity):
                        """
                        none
                        
                        .. attribute:: location_id  (key)
                        
                        	Location ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: enable_val
                        
                        	If Enabled set value to 65535
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation.NetflowLocationLeaf, self).__init__()

                            self.yang_name = "netflow-location-leaf"
                            self.yang_parent_name = "netflow-location"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location_id', (YLeaf(YType.uint32, 'location-id'), ['int'])),
                                ('enable_val', (YLeaf(YType.uint32, 'enable-val'), ['int'])),
                            ])
                            self.location_id = None
                            self.enable_val = None
                            self._segment_path = lambda: "netflow-location-leaf" + "[location-id='" + str(self.location_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Netflow.NetflowLocations.NetflowLocation.NetflowLocationLeaf, ['location_id', 'enable_val'], name, value)


            class LocationAll(Entity):
                """
                IPFIX315 Location All
                
                .. attribute:: location_all_leaf
                
                	If Enabled set value to 65535
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Netflow.LocationAll, self).__init__()

                    self.yang_name = "location-all"
                    self.yang_parent_name = "netflow"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('location_all_leaf', (YLeaf(YType.uint32, 'location-all-leaf'), ['int'])),
                    ])
                    self.location_all_leaf = None
                    self._segment_path = lambda: "location-all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/netflow/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Netflow.LocationAll, ['location_all_leaf'], name, value)


        class Flowspecs(Entity):
            """
            Configure Flowspec profile.
            
            .. attribute:: flowspec
            
            	none
            	**type**\: list of  		 :py:class:`Flowspec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Flowspecs.Flowspec>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Flowspecs, self).__init__()

                self.yang_name = "flowspecs"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("flowspec", ("flowspec", HwModuleProfileConfig.Profile.Flowspecs.Flowspec))])
                self._leafs = OrderedDict()

                self.flowspec = YList(self)
                self._segment_path = lambda: "flowspecs"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Flowspecs, [], name, value)


            class Flowspec(Entity):
                """
                none
                
                .. attribute:: v6_enable  (key)
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: location_string  (key)
                
                	Location of FLOWSPEC config
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: location_id  (key)
                
                	Location ID hex to Decimal 0xffff for all
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: enable_val
                
                	If Enabled set value to 65535
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Flowspecs.Flowspec, self).__init__()

                    self.yang_name = "flowspec"
                    self.yang_parent_name = "flowspecs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['v6_enable','location_string','location_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('v6_enable', (YLeaf(YType.str, 'v6-enable'), ['str'])),
                        ('location_string', (YLeaf(YType.str, 'location-string'), ['str'])),
                        ('location_id', (YLeaf(YType.uint32, 'location-id'), ['int'])),
                        ('enable_val', (YLeaf(YType.uint32, 'enable-val'), ['int'])),
                    ])
                    self.v6_enable = None
                    self.location_string = None
                    self.location_id = None
                    self.enable_val = None
                    self._segment_path = lambda: "flowspec" + "[v6-enable='" + str(self.v6_enable) + "']" + "[location-string='" + str(self.location_string) + "']" + "[location-id='" + str(self.location_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/flowspecs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Flowspecs.Flowspec, ['v6_enable', 'location_string', 'location_id', 'enable_val'], name, value)


        class SegmentRoutings(Entity):
            """
            Configure Segment Routing profile.
            
            .. attribute:: segment_routing
            
            	none
            	**type**\: list of  		 :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.SegmentRoutings.SegmentRouting>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.SegmentRoutings, self).__init__()

                self.yang_name = "segment-routings"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("segment-routing", ("segment_routing", HwModuleProfileConfig.Profile.SegmentRoutings.SegmentRouting))])
                self._leafs = OrderedDict()

                self.segment_routing = YList(self)
                self._segment_path = lambda: "segment-routings"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.SegmentRoutings, [], name, value)


            class SegmentRouting(Entity):
                """
                none
                
                .. attribute:: srv6  (key)
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: enable_val
                
                	If Enabled set value to 1
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.SegmentRoutings.SegmentRouting, self).__init__()

                    self.yang_name = "segment-routing"
                    self.yang_parent_name = "segment-routings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['srv6']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srv6', (YLeaf(YType.str, 'srv6'), ['str'])),
                        ('enable_val', (YLeaf(YType.uint32, 'enable-val'), ['int'])),
                    ])
                    self.srv6 = None
                    self.enable_val = None
                    self._segment_path = lambda: "segment-routing" + "[srv6='" + str(self.srv6) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/segment-routings/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.SegmentRoutings.SegmentRouting, ['srv6', 'enable_val'], name, value)


        class LoadBalance(Entity):
            """
            Configure load balance parameters
            
            .. attribute:: load_balance_profile
            
            	Configure load balance parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.LoadBalance, self).__init__()

                self.yang_name = "load-balance"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('load_balance_profile', (YLeaf(YType.uint32, 'load-balance-profile'), ['int'])),
                ])
                self.load_balance_profile = None
                self._segment_path = lambda: "load-balance"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.LoadBalance, ['load_balance_profile'], name, value)


        class Stats(Entity):
            """
            Configure stats
            
            .. attribute:: stats_profile_modes
            
            	Configure stats for qos\-enhanced and acl\-permit
            	**type**\:  :py:class:`StatsProfileModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Stats.StatsProfileModes>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Stats, self).__init__()

                self.yang_name = "stats"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("stats-profile-modes", ("stats_profile_modes", HwModuleProfileConfig.Profile.Stats.StatsProfileModes))])
                self._leafs = OrderedDict()

                self.stats_profile_modes = HwModuleProfileConfig.Profile.Stats.StatsProfileModes()
                self.stats_profile_modes.parent = self
                self._children_name_map["stats_profile_modes"] = "stats-profile-modes"
                self._segment_path = lambda: "stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Stats, [], name, value)


            class StatsProfileModes(Entity):
                """
                Configure stats for qos\-enhanced and
                acl\-permit
                
                .. attribute:: stats_profile_mode
                
                	Configure stats for qos\-enhanced and acl\-permit
                	**type**\: list of  		 :py:class:`StatsProfileMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Stats.StatsProfileModes.StatsProfileMode>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Stats.StatsProfileModes, self).__init__()

                    self.yang_name = "stats-profile-modes"
                    self.yang_parent_name = "stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats-profile-mode", ("stats_profile_mode", HwModuleProfileConfig.Profile.Stats.StatsProfileModes.StatsProfileMode))])
                    self._leafs = OrderedDict()

                    self.stats_profile_mode = YList(self)
                    self._segment_path = lambda: "stats-profile-modes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/stats/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Stats.StatsProfileModes, [], name, value)


                class StatsProfileMode(Entity):
                    """
                    Configure stats for qos\-enhanced and
                    acl\-permit
                    
                    .. attribute:: stats_mode_default  (key)
                    
                    	Give Default Stats Mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mode
                    
                    	Stats Mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Stats.StatsProfileModes.StatsProfileMode, self).__init__()

                        self.yang_name = "stats-profile-mode"
                        self.yang_parent_name = "stats-profile-modes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['stats_mode_default']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('stats_mode_default', (YLeaf(YType.uint32, 'stats-mode-default'), ['int'])),
                            ('mode', (YLeaf(YType.uint32, 'mode'), ['int'])),
                        ])
                        self.stats_mode_default = None
                        self.mode = None
                        self._segment_path = lambda: "stats-profile-mode" + "[stats-mode-default='" + str(self.stats_mode_default) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/stats/stats-profile-modes/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Stats.StatsProfileModes.StatsProfileMode, ['stats_mode_default', 'mode'], name, value)


        class ProfileAcl(Entity):
            """
            Configure acl profile
            
            .. attribute:: egress
            
            	Enabled or disabled
            	**type**\: bool
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.ProfileAcl, self).__init__()

                self.yang_name = "profile-acl"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('egress', (YLeaf(YType.boolean, 'egress'), ['bool'])),
                ])
                self.egress = None
                self._segment_path = lambda: "profile-acl"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.ProfileAcl, ['egress'], name, value)


        class BundleScale(Entity):
            """
            Configure Bundle profile.
            
            .. attribute:: trunk_size
            
            	Configure Max Trunk Size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.BundleScale, self).__init__()

                self.yang_name = "bundle-scale"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('trunk_size', (YLeaf(YType.uint32, 'trunk-size'), ['int'])),
                ])
                self.trunk_size = None
                self._segment_path = lambda: "bundle-scale"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.BundleScale, ['trunk_size'], name, value)


        class ProfileTcam(Entity):
            """
            Configure Tcam Profile
            
            .. attribute:: key_format
            
            	none
            	**type**\:  :py:class:`KeyFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.ProfileTcam, self).__init__()

                self.yang_name = "profile-tcam"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("key-format", ("key_format", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat))])
                self._leafs = OrderedDict()

                self.key_format = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat()
                self.key_format.parent = self
                self._children_name_map["key_format"] = "key-format"
                self._segment_path = lambda: "profile-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam, [], name, value)


            class KeyFormat(Entity):
                """
                none
                
                .. attribute:: key_format_acl_table
                
                	Configure acl profile
                	**type**\:  :py:class:`KeyFormatAclTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat, self).__init__()

                    self.yang_name = "key-format"
                    self.yang_parent_name = "profile-tcam"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("key-format-acl-table", ("key_format_acl_table", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable))])
                    self._leafs = OrderedDict()

                    self.key_format_acl_table = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable()
                    self.key_format_acl_table.parent = self
                    self._children_name_map["key_format_acl_table"] = "key-format-acl-table"
                    self._segment_path = lambda: "key-format"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat, [], name, value)


                class KeyFormatAclTable(Entity):
                    """
                    Configure acl profile
                    
                    .. attribute:: ipv6_acl_tables
                    
                    	Configure ipv6 acl profile
                    	**type**\:  :py:class:`Ipv6AclTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables>`
                    
                    .. attribute:: ipv4_acl_tables
                    
                    	Configure ipv4 acl profile
                    	**type**\:  :py:class:`Ipv4AclTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable, self).__init__()

                        self.yang_name = "key-format-acl-table"
                        self.yang_parent_name = "key-format"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv6-acl-tables", ("ipv6_acl_tables", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables)), ("ipv4-acl-tables", ("ipv4_acl_tables", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables))])
                        self._leafs = OrderedDict()

                        self.ipv6_acl_tables = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables()
                        self.ipv6_acl_tables.parent = self
                        self._children_name_map["ipv6_acl_tables"] = "ipv6-acl-tables"

                        self.ipv4_acl_tables = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables()
                        self.ipv4_acl_tables.parent = self
                        self._children_name_map["ipv4_acl_tables"] = "ipv4-acl-tables"
                        self._segment_path = lambda: "key-format-acl-table"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable, [], name, value)


                    class Ipv6AclTables(Entity):
                        """
                        Configure ipv6 acl profile
                        
                        .. attribute:: ipv6_acl_table
                        
                        	Configure format for ipv6 acl profile
                        	**type**\: list of  		 :py:class:`Ipv6AclTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables.Ipv6AclTable>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables, self).__init__()

                            self.yang_name = "ipv6-acl-tables"
                            self.yang_parent_name = "key-format-acl-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv6-acl-table", ("ipv6_acl_table", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables.Ipv6AclTable))])
                            self._leafs = OrderedDict()

                            self.ipv6_acl_table = YList(self)
                            self._segment_path = lambda: "ipv6-acl-tables"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/key-format-acl-table/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables, [], name, value)


                        class Ipv6AclTable(Entity):
                            """
                            Configure format for ipv6 acl profile
                            
                            .. attribute:: location_string  (key)
                            
                            	Location string (all) if for all LCs
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: location_id  (key)
                            
                            	Location ID hex to Decimal 0xffff for all
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: source_addr
                            
                            	Source Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: source_port
                            
                            	Source Port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: destination_addr
                            
                            	Destination Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dest_port
                            
                            	Destination Port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prot_type
                            
                            	Next Header Type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tcp_flag
                            
                            	TCP Flags
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pack_len
                            
                            	Packet Length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: precedence
                            
                            	Precedence
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: udf1
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf2
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf3
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf4
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf5
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf6
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf7
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf8
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: en_capture
                            
                            	Enable Capture
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_ttl
                            
                            	Enable Setting TTL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_match
                            
                            	Enable Matching TTL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_share_acl
                            
                            	Enable Non Shared Interface ACL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables.Ipv6AclTable, self).__init__()

                                self.yang_name = "ipv6-acl-table"
                                self.yang_parent_name = "ipv6-acl-tables"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['location_string','location_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location_string', (YLeaf(YType.str, 'location-string'), ['str'])),
                                    ('location_id', (YLeaf(YType.uint32, 'location-id'), ['int'])),
                                    ('source_addr', (YLeaf(YType.uint32, 'source-addr'), ['int'])),
                                    ('source_port', (YLeaf(YType.uint32, 'source-port'), ['int'])),
                                    ('destination_addr', (YLeaf(YType.uint32, 'destination-addr'), ['int'])),
                                    ('dest_port', (YLeaf(YType.uint32, 'dest-port'), ['int'])),
                                    ('prot_type', (YLeaf(YType.uint32, 'prot-type'), ['int'])),
                                    ('tcp_flag', (YLeaf(YType.uint32, 'tcp-flag'), ['int'])),
                                    ('pack_len', (YLeaf(YType.uint32, 'pack-len'), ['int'])),
                                    ('precedence', (YLeaf(YType.uint32, 'precedence'), ['int'])),
                                    ('udf1', (YLeaf(YType.str, 'udf1'), ['str'])),
                                    ('udf2', (YLeaf(YType.str, 'udf2'), ['str'])),
                                    ('udf3', (YLeaf(YType.str, 'udf3'), ['str'])),
                                    ('udf4', (YLeaf(YType.str, 'udf4'), ['str'])),
                                    ('udf5', (YLeaf(YType.str, 'udf5'), ['str'])),
                                    ('udf6', (YLeaf(YType.str, 'udf6'), ['str'])),
                                    ('udf7', (YLeaf(YType.str, 'udf7'), ['str'])),
                                    ('udf8', (YLeaf(YType.str, 'udf8'), ['str'])),
                                    ('en_capture', (YLeaf(YType.uint32, 'en-capture'), ['int'])),
                                    ('en_ttl', (YLeaf(YType.uint32, 'en-ttl'), ['int'])),
                                    ('en_match', (YLeaf(YType.uint32, 'en-match'), ['int'])),
                                    ('en_share_acl', (YLeaf(YType.uint32, 'en-share-acl'), ['int'])),
                                ])
                                self.location_string = None
                                self.location_id = None
                                self.source_addr = None
                                self.source_port = None
                                self.destination_addr = None
                                self.dest_port = None
                                self.prot_type = None
                                self.tcp_flag = None
                                self.pack_len = None
                                self.precedence = None
                                self.udf1 = None
                                self.udf2 = None
                                self.udf3 = None
                                self.udf4 = None
                                self.udf5 = None
                                self.udf6 = None
                                self.udf7 = None
                                self.udf8 = None
                                self.en_capture = None
                                self.en_ttl = None
                                self.en_match = None
                                self.en_share_acl = None
                                self._segment_path = lambda: "ipv6-acl-table" + "[location-string='" + str(self.location_string) + "']" + "[location-id='" + str(self.location_id) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/key-format-acl-table/ipv6-acl-tables/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv6AclTables.Ipv6AclTable, ['location_string', 'location_id', 'source_addr', 'source_port', 'destination_addr', 'dest_port', 'prot_type', 'tcp_flag', 'pack_len', 'precedence', 'udf1', 'udf2', 'udf3', 'udf4', 'udf5', 'udf6', 'udf7', 'udf8', 'en_capture', 'en_ttl', 'en_match', 'en_share_acl'], name, value)


                    class Ipv4AclTables(Entity):
                        """
                        Configure ipv4 acl profile
                        
                        .. attribute:: ipv4_acl_table
                        
                        	Configure format for ipv4 acl profile
                        	**type**\: list of  		 :py:class:`Ipv4AclTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables.Ipv4AclTable>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables, self).__init__()

                            self.yang_name = "ipv4-acl-tables"
                            self.yang_parent_name = "key-format-acl-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4-acl-table", ("ipv4_acl_table", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables.Ipv4AclTable))])
                            self._leafs = OrderedDict()

                            self.ipv4_acl_table = YList(self)
                            self._segment_path = lambda: "ipv4-acl-tables"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/key-format-acl-table/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables, [], name, value)


                        class Ipv4AclTable(Entity):
                            """
                            Configure format for ipv4 acl profile
                            
                            .. attribute:: location_string  (key)
                            
                            	Location string (all) if for all LCs
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: location_id  (key)
                            
                            	Location ID hex to Decimal 0xffff for all
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: source_addr
                            
                            	Source Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: destination_addr
                            
                            	Destination Address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: source_port
                            
                            	Source Port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dest_port
                            
                            	Destination Port
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prot_type
                            
                            	Protocol Type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tcp_flag
                            
                            	TCP Flags
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pack_len
                            
                            	Packet Length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: frag_bit
                            
                            	Fragment Bit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: precedence
                            
                            	Precedence
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: port_range
                            
                            	PortRange
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: udf1
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf2
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf3
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf4
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf5
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf6
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf7
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: udf8
                            
                            	UDF name
                            	**type**\: str
                            
                            .. attribute:: en_capture
                            
                            	Enable Capture
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_ttl
                            
                            	Enable Setting TTL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_match
                            
                            	Enable Matching TTL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: en_share_acl
                            
                            	Enable Non Shared Interface ACL
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables.Ipv4AclTable, self).__init__()

                                self.yang_name = "ipv4-acl-table"
                                self.yang_parent_name = "ipv4-acl-tables"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = ['location_string','location_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('location_string', (YLeaf(YType.str, 'location-string'), ['str'])),
                                    ('location_id', (YLeaf(YType.uint32, 'location-id'), ['int'])),
                                    ('source_addr', (YLeaf(YType.uint32, 'source-addr'), ['int'])),
                                    ('destination_addr', (YLeaf(YType.uint32, 'destination-addr'), ['int'])),
                                    ('source_port', (YLeaf(YType.uint32, 'source-port'), ['int'])),
                                    ('dest_port', (YLeaf(YType.uint32, 'dest-port'), ['int'])),
                                    ('prot_type', (YLeaf(YType.uint32, 'prot-type'), ['int'])),
                                    ('tcp_flag', (YLeaf(YType.uint32, 'tcp-flag'), ['int'])),
                                    ('pack_len', (YLeaf(YType.uint32, 'pack-len'), ['int'])),
                                    ('frag_bit', (YLeaf(YType.uint32, 'frag-bit'), ['int'])),
                                    ('precedence', (YLeaf(YType.uint32, 'precedence'), ['int'])),
                                    ('port_range', (YLeaf(YType.uint32, 'port-range'), ['int'])),
                                    ('udf1', (YLeaf(YType.str, 'udf1'), ['str'])),
                                    ('udf2', (YLeaf(YType.str, 'udf2'), ['str'])),
                                    ('udf3', (YLeaf(YType.str, 'udf3'), ['str'])),
                                    ('udf4', (YLeaf(YType.str, 'udf4'), ['str'])),
                                    ('udf5', (YLeaf(YType.str, 'udf5'), ['str'])),
                                    ('udf6', (YLeaf(YType.str, 'udf6'), ['str'])),
                                    ('udf7', (YLeaf(YType.str, 'udf7'), ['str'])),
                                    ('udf8', (YLeaf(YType.str, 'udf8'), ['str'])),
                                    ('en_capture', (YLeaf(YType.uint32, 'en-capture'), ['int'])),
                                    ('en_ttl', (YLeaf(YType.uint32, 'en-ttl'), ['int'])),
                                    ('en_match', (YLeaf(YType.uint32, 'en-match'), ['int'])),
                                    ('en_share_acl', (YLeaf(YType.uint32, 'en-share-acl'), ['int'])),
                                ])
                                self.location_string = None
                                self.location_id = None
                                self.source_addr = None
                                self.destination_addr = None
                                self.source_port = None
                                self.dest_port = None
                                self.prot_type = None
                                self.tcp_flag = None
                                self.pack_len = None
                                self.frag_bit = None
                                self.precedence = None
                                self.port_range = None
                                self.udf1 = None
                                self.udf2 = None
                                self.udf3 = None
                                self.udf4 = None
                                self.udf5 = None
                                self.udf6 = None
                                self.udf7 = None
                                self.udf8 = None
                                self.en_capture = None
                                self.en_ttl = None
                                self.en_match = None
                                self.en_share_acl = None
                                self._segment_path = lambda: "ipv4-acl-table" + "[location-string='" + str(self.location_string) + "']" + "[location-id='" + str(self.location_id) + "']"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/key-format-acl-table/ipv4-acl-tables/%s" % self._segment_path()
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.KeyFormatAclTable.Ipv4AclTables.Ipv4AclTable, ['location_string', 'location_id', 'source_addr', 'destination_addr', 'source_port', 'dest_port', 'prot_type', 'tcp_flag', 'pack_len', 'frag_bit', 'precedence', 'port_range', 'udf1', 'udf2', 'udf3', 'udf4', 'udf5', 'udf6', 'udf7', 'udf8', 'en_capture', 'en_ttl', 'en_match', 'en_share_acl'], name, value)


        class Qos(Entity):
            """
            Configure profile.
            
            .. attribute:: hqos_enable_all
            
            	Configure Hqos profile
            	**type**\:  :py:class:`HqosEnableAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.HqosEnableAll>`
            
            .. attribute:: ingress_model_root_def
            
            	Configure Ingress Model Default
            	**type**\:  :py:class:`IngressModelRootDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModelRootDef>`
            
            .. attribute:: ingress_models
            
            	Configure Ingress Model Root
            	**type**\:  :py:class:`IngressModels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels>`
            
            .. attribute:: class_maps_root_def
            
            	Configure Class Maps Default
            	**type**\:  :py:class:`ClassMapsRootDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef>`
            
            .. attribute:: class_maps
            
            	Configure Class Map Root
            	**type**\:  :py:class:`ClassMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Qos, self).__init__()

                self.yang_name = "qos"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("hqos-enable-all", ("hqos_enable_all", HwModuleProfileConfig.Profile.Qos.HqosEnableAll)), ("ingress-model-root-def", ("ingress_model_root_def", HwModuleProfileConfig.Profile.Qos.IngressModelRootDef)), ("ingress-models", ("ingress_models", HwModuleProfileConfig.Profile.Qos.IngressModels)), ("class-maps-root-def", ("class_maps_root_def", HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef)), ("class-maps", ("class_maps", HwModuleProfileConfig.Profile.Qos.ClassMaps))])
                self._leafs = OrderedDict()

                self.hqos_enable_all = HwModuleProfileConfig.Profile.Qos.HqosEnableAll()
                self.hqos_enable_all.parent = self
                self._children_name_map["hqos_enable_all"] = "hqos-enable-all"

                self.ingress_model_root_def = HwModuleProfileConfig.Profile.Qos.IngressModelRootDef()
                self.ingress_model_root_def.parent = self
                self._children_name_map["ingress_model_root_def"] = "ingress-model-root-def"

                self.ingress_models = HwModuleProfileConfig.Profile.Qos.IngressModels()
                self.ingress_models.parent = self
                self._children_name_map["ingress_models"] = "ingress-models"

                self.class_maps_root_def = HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef()
                self.class_maps_root_def.parent = self
                self._children_name_map["class_maps_root_def"] = "class-maps-root-def"

                self.class_maps = HwModuleProfileConfig.Profile.Qos.ClassMaps()
                self.class_maps.parent = self
                self._children_name_map["class_maps"] = "class-maps"
                self._segment_path = lambda: "qos"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Qos, [], name, value)


            class HqosEnableAll(Entity):
                """
                Configure Hqos profile
                
                .. attribute:: hqos_enable
                
                	 Hqos profile value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.HqosEnableAll, self).__init__()

                    self.yang_name = "hqos-enable-all"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hqos_enable', (YLeaf(YType.uint32, 'hqos-enable'), ['int'])),
                    ])
                    self.hqos_enable = None
                    self._segment_path = lambda: "hqos-enable-all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.HqosEnableAll, ['hqos_enable'], name, value)


            class IngressModelRootDef(Entity):
                """
                Configure Ingress Model Default
                
                .. attribute:: ingress_model_leaf_def
                
                	Ingress Model Default
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.IngressModelRootDef, self).__init__()

                    self.yang_name = "ingress-model-root-def"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ingress_model_leaf_def', (YLeaf(YType.uint32, 'ingress-model-leaf-def'), ['int'])),
                    ])
                    self.ingress_model_leaf_def = None
                    self._segment_path = lambda: "ingress-model-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModelRootDef, ['ingress_model_leaf_def'], name, value)


            class IngressModels(Entity):
                """
                Configure Ingress Model Root
                
                .. attribute:: ingress_model
                
                	Configure Ingress Model
                	**type**\: list of  		 :py:class:`IngressModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.IngressModels, self).__init__()

                    self.yang_name = "ingress-models"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ingress-model", ("ingress_model", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel))])
                    self._leafs = OrderedDict()

                    self.ingress_model = YList(self)
                    self._segment_path = lambda: "ingress-models"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels, [], name, value)


                class IngressModel(Entity):
                    """
                    Configure Ingress Model
                    
                    .. attribute:: node_name  (key)
                    
                    	NodeName
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ingress_model_leaf
                    
                    	Configure Ingress Model Leaf
                    	**type**\: list of  		 :py:class:`IngressModelLeaf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel, self).__init__()

                        self.yang_name = "ingress-model"
                        self.yang_parent_name = "ingress-models"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("ingress-model-leaf", ("ingress_model_leaf", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.node_name = None

                        self.ingress_model_leaf = YList(self)
                        self._segment_path = lambda: "ingress-model" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/ingress-models/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel, ['node_name'], name, value)


                    class IngressModelLeaf(Entity):
                        """
                        Configure Ingress Model Leaf
                        
                        .. attribute:: location  (key)
                        
                        	Location
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ingress_model_leaf
                        
                        	IngressModelLeaf
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf, self).__init__()

                            self.yang_name = "ingress-model-leaf"
                            self.yang_parent_name = "ingress-model"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', (YLeaf(YType.uint32, 'location'), ['int'])),
                                ('ingress_model_leaf', (YLeaf(YType.uint32, 'ingress-model-leaf'), ['int'])),
                            ])
                            self.location = None
                            self.ingress_model_leaf = None
                            self._segment_path = lambda: "ingress-model-leaf" + "[location='" + str(self.location) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf, ['location', 'ingress_model_leaf'], name, value)


            class ClassMapsRootDef(Entity):
                """
                Configure Class Maps Default
                
                .. attribute:: class_map_size_def
                
                	Class Map Size Default
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef, self).__init__()

                    self.yang_name = "class-maps-root-def"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('class_map_size_def', (YLeaf(YType.uint32, 'class-map-size-def'), ['int'])),
                    ])
                    self.class_map_size_def = None
                    self._segment_path = lambda: "class-maps-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef, ['class_map_size_def'], name, value)


            class ClassMaps(Entity):
                """
                Configure Class Map Root
                
                .. attribute:: class_map
                
                	Configure Class Maps
                	**type**\: list of  		 :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.ClassMaps, self).__init__()

                    self.yang_name = "class-maps"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class-map", ("class_map", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap))])
                    self._leafs = OrderedDict()

                    self.class_map = YList(self)
                    self._segment_path = lambda: "class-maps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps, [], name, value)


                class ClassMap(Entity):
                    """
                    Configure Class Maps
                    
                    .. attribute:: node_name  (key)
                    
                    	NodeName
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: class_map_size
                    
                    	Class Map Size
                    	**type**\: list of  		 :py:class:`ClassMapSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap, self).__init__()

                        self.yang_name = "class-map"
                        self.yang_parent_name = "class-maps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_name']
                        self._child_classes = OrderedDict([("class-map-size", ("class_map_size", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ])
                        self.node_name = None

                        self.class_map_size = YList(self)
                        self._segment_path = lambda: "class-map" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/class-maps/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap, ['node_name'], name, value)


                    class ClassMapSize(Entity):
                        """
                        Class Map Size
                        
                        .. attribute:: location  (key)
                        
                        	Location
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: class_map_size
                        
                        	ClassMapSize
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize, self).__init__()

                            self.yang_name = "class-map-size"
                            self.yang_parent_name = "class-map"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['location']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', (YLeaf(YType.uint32, 'location'), ['int'])),
                                ('class_map_size', (YLeaf(YType.uint32, 'class-map-size'), ['int'])),
                            ])
                            self.location = None
                            self.class_map_size = None
                            self._segment_path = lambda: "class-map-size" + "[location='" + str(self.location) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize, ['location', 'class_map_size'], name, value)


    class FibScale(Entity):
        """
        Configure Fib for Scale for noTcam LC.
        
        .. attribute:: ipv6_unicast_scale_no_tcam
        
        	IPv6 table for NOTCAM LC Scale
        	**type**\:  :py:class:`Ipv6UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam>`
        
        .. attribute:: ipv4_unicast_scale_no_tcam
        
        	IPv4 table for NOTCAM LC Scale
        	**type**\:  :py:class:`Ipv4UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.FibScale, self).__init__()

            self.yang_name = "fib-scale"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6-unicast-scale-no-tcam", ("ipv6_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam)), ("ipv4-unicast-scale-no-tcam", ("ipv4_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam))])
            self._leafs = OrderedDict()

            self.ipv6_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam()
            self.ipv6_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv6_unicast_scale_no_tcam"] = "ipv6-unicast-scale-no-tcam"

            self.ipv4_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam()
            self.ipv4_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv4_unicast_scale_no_tcam"] = "ipv4-unicast-scale-no-tcam"
            self._segment_path = lambda: "fib-scale"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleProfileConfig.FibScale, [], name, value)


        class Ipv6UnicastScaleNoTcam(Entity):
            """
            IPv6 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv6_no_tcam
            
            	Scale for IPv6 table for NoTCAM LC
            	**type**\:  :py:class:`ScaleIpv6NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv6-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("scale-ipv6-no-tcam", ("scale_ipv6_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam))])
                self._leafs = OrderedDict()

                self.scale_ipv6_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam()
                self.scale_ipv6_no_tcam.parent = self
                self._children_name_map["scale_ipv6_no_tcam"] = "scale-ipv6-no-tcam"
                self._segment_path = lambda: "ipv6-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam, [], name, value)


            class ScaleIpv6NoTcam(Entity):
                """
                Scale for IPv6 table for NoTCAM LC.
                
                .. attribute:: internet_optimized_ipv6_no_tcam
                
                	Internet\-optimized Scale for IPv6 table for NoTCAM LC
                	**type**\: str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, self).__init__()

                    self.yang_name = "scale-ipv6-no-tcam"
                    self.yang_parent_name = "ipv6-unicast-scale-no-tcam"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('internet_optimized_ipv6_no_tcam', (YLeaf(YType.str, 'internet-optimized-ipv6-no-tcam'), ['str'])),
                    ])
                    self.internet_optimized_ipv6_no_tcam = None
                    self._segment_path = lambda: "scale-ipv6-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv6-unicast-scale-no-tcam/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, ['internet_optimized_ipv6_no_tcam'], name, value)


        class Ipv4UnicastScaleNoTcam(Entity):
            """
            IPv4 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv4_no_tcam
            
            	Scale for IPv4 table for NoTCAM LC
            	**type**\:  :py:class:`ScaleIpv4NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv4-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("scale-ipv4-no-tcam", ("scale_ipv4_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam))])
                self._leafs = OrderedDict()

                self.scale_ipv4_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam()
                self.scale_ipv4_no_tcam.parent = self
                self._children_name_map["scale_ipv4_no_tcam"] = "scale-ipv4-no-tcam"
                self._segment_path = lambda: "ipv4-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam, [], name, value)


            class ScaleIpv4NoTcam(Entity):
                """
                Scale for IPv4 table for NoTCAM LC.
                
                .. attribute:: optimized_ipv4_no_tcam
                
                	Optimized Scale for IPv4 table for NoTCAM LC
                	**type**\: str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, self).__init__()

                    self.yang_name = "scale-ipv4-no-tcam"
                    self.yang_parent_name = "ipv4-unicast-scale-no-tcam"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('optimized_ipv4_no_tcam', (YLeaf(YType.str, 'optimized-ipv4-no-tcam'), ['str'])),
                    ])
                    self.optimized_ipv4_no_tcam = None
                    self._segment_path = lambda: "scale-ipv4-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv4-unicast-scale-no-tcam/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, ['optimized_ipv4_no_tcam'], name, value)


    class OrchestratedLinecardReload(Entity):
        """
        Configure OLR.
        
        .. attribute:: plane_table_entries
        
        	Plane type
        	**type**\:  :py:class:`PlaneTableEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.OrchestratedLinecardReload, self).__init__()

            self.yang_name = "orchestrated-linecard-reload"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("plane-table-entries", ("plane_table_entries", HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries))])
            self._leafs = OrderedDict()

            self.plane_table_entries = HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries()
            self.plane_table_entries.parent = self
            self._children_name_map["plane_table_entries"] = "plane-table-entries"
            self._segment_path = lambda: "orchestrated-linecard-reload"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleProfileConfig.OrchestratedLinecardReload, [], name, value)


        class PlaneTableEntries(Entity):
            """
            Plane type
            
            .. attribute:: plane_table_entry
            
            	Plane \: A or B
            	**type**\: list of  		 :py:class:`PlaneTableEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries, self).__init__()

                self.yang_name = "plane-table-entries"
                self.yang_parent_name = "orchestrated-linecard-reload"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("plane-table-entry", ("plane_table_entry", HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry))])
                self._leafs = OrderedDict()

                self.plane_table_entry = YList(self)
                self._segment_path = lambda: "plane-table-entries"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/orchestrated-linecard-reload/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries, [], name, value)


            class PlaneTableEntry(Entity):
                """
                Plane \: A or B
                
                .. attribute:: plane_name  (key)
                
                	Plane Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: rack_table_entries
                
                	Rack Information
                	**type**\:  :py:class:`RackTableEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry, self).__init__()

                    self.yang_name = "plane-table-entry"
                    self.yang_parent_name = "plane-table-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['plane_name']
                    self._child_classes = OrderedDict([("rack-table-entries", ("rack_table_entries", HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries))])
                    self._leafs = OrderedDict([
                        ('plane_name', (YLeaf(YType.str, 'plane-name'), ['str'])),
                    ])
                    self.plane_name = None

                    self.rack_table_entries = HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries()
                    self.rack_table_entries.parent = self
                    self._children_name_map["rack_table_entries"] = "rack-table-entries"
                    self._segment_path = lambda: "plane-table-entry" + "[plane-name='" + str(self.plane_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/orchestrated-linecard-reload/plane-table-entries/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry, ['plane_name'], name, value)


                class RackTableEntries(Entity):
                    """
                    Rack Information
                    
                    .. attribute:: rack_table_entry
                    
                    	Rack Number
                    	**type**\: list of  		 :py:class:`RackTableEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries.RackTableEntry>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries, self).__init__()

                        self.yang_name = "rack-table-entries"
                        self.yang_parent_name = "plane-table-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rack-table-entry", ("rack_table_entry", HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries.RackTableEntry))])
                        self._leafs = OrderedDict()

                        self.rack_table_entry = YList(self)
                        self._segment_path = lambda: "rack-table-entries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries, [], name, value)


                    class RackTableEntry(Entity):
                        """
                        Rack Number
                        
                        .. attribute:: rack_num  (key)
                        
                        	Rack Number
                        	**type**\: int
                        
                        	**range:** 0..15
                        
                        .. attribute:: nodes_list
                        
                        	Please enter linecards separated via comma eg 0,3,6,11,13
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries.RackTableEntry, self).__init__()

                            self.yang_name = "rack-table-entry"
                            self.yang_parent_name = "rack-table-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rack_num']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rack_num', (YLeaf(YType.uint32, 'rack-num'), ['int'])),
                                ('nodes_list', (YLeaf(YType.str, 'nodes-list'), ['str'])),
                            ])
                            self.rack_num = None
                            self.nodes_list = None
                            self._segment_path = lambda: "rack-table-entry" + "[rack-num='" + str(self.rack_num) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.OrchestratedLinecardReload.PlaneTableEntries.PlaneTableEntry.RackTableEntries.RackTableEntry, ['rack_num', 'nodes_list'], name, value)


    class Tcam(Entity):
        """
        Configure Tcam.
        
        .. attribute:: fib_tcam_scale
        
        	Configure Fib scale for Tcam
        	**type**\:  :py:class:`FibTcamScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Tcam, self).__init__()

            self.yang_name = "tcam"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fib-tcam-scale", ("fib_tcam_scale", HwModuleProfileConfig.Tcam.FibTcamScale))])
            self._leafs = OrderedDict()

            self.fib_tcam_scale = HwModuleProfileConfig.Tcam.FibTcamScale()
            self.fib_tcam_scale.parent = self
            self._children_name_map["fib_tcam_scale"] = "fib-tcam-scale"
            self._segment_path = lambda: "tcam"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleProfileConfig.Tcam, [], name, value)


        class FibTcamScale(Entity):
            """
            Configure Fib scale for Tcam.
            
            .. attribute:: ipv4_unicast_scale
            
            	IPv4 table for TCAM LC Scale
            	**type**\:  :py:class:`Ipv4UnicastScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Tcam.FibTcamScale, self).__init__()

                self.yang_name = "fib-tcam-scale"
                self.yang_parent_name = "tcam"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4-unicast-scale", ("ipv4_unicast_scale", HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale))])
                self._leafs = OrderedDict()

                self.ipv4_unicast_scale = HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale()
                self.ipv4_unicast_scale.parent = self
                self._children_name_map["ipv4_unicast_scale"] = "ipv4-unicast-scale"
                self._segment_path = lambda: "fib-tcam-scale"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Tcam.FibTcamScale, [], name, value)


            class Ipv4UnicastScale(Entity):
                """
                IPv4 table for TCAM LC Scale.
                
                .. attribute:: ipv4_scale
                
                	Scale for IPv4 table for TCAM LC
                	**type**\: bool
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, self).__init__()

                    self.yang_name = "ipv4-unicast-scale"
                    self.yang_parent_name = "fib-tcam-scale"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ipv4_scale', (YLeaf(YType.boolean, 'ipv4-scale'), ['bool'])),
                    ])
                    self.ipv4_scale = None
                    self._segment_path = lambda: "ipv4-unicast-scale"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/fib-tcam-scale/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, ['ipv4_scale'], name, value)


    class Qosqppb(Entity):
        """
        Configure profile.
        
        .. attribute:: ipv6_scale
        
        	Configure IPv6 destination short profile
        	**type**\:  :py:class:`Ipv6Scale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Qosqppb.Ipv6Scale>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Qosqppb, self).__init__()

            self.yang_name = "qosqppb"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6-scale", ("ipv6_scale", HwModuleProfileConfig.Qosqppb.Ipv6Scale))])
            self._leafs = OrderedDict()

            self.ipv6_scale = HwModuleProfileConfig.Qosqppb.Ipv6Scale()
            self.ipv6_scale.parent = self
            self._children_name_map["ipv6_scale"] = "ipv6-scale"
            self._segment_path = lambda: "qosqppb"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(HwModuleProfileConfig.Qosqppb, [], name, value)


        class Ipv6Scale(Entity):
            """
            Configure IPv6 destination short profile
            
            .. attribute:: ipv6_short
            
            	ipv6 short profile value
            	**type**\: bool
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Qosqppb.Ipv6Scale, self).__init__()

                self.yang_name = "ipv6-scale"
                self.yang_parent_name = "qosqppb"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipv6_short', (YLeaf(YType.boolean, 'ipv6-short'), ['bool'])),
                ])
                self.ipv6_short = None
                self._segment_path = lambda: "ipv6-scale"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/qosqppb/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Qosqppb.Ipv6Scale, ['ipv6_short'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModuleProfileConfig()
        return self._top_entity

