""" Cisco_IOS_XR_fia_hw_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-hw\-profile package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-profile\-config\: none

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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
    
    .. attribute:: tcam
    
    	Configure Tcam
    	**type**\:  :py:class:`Tcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam>`
    
    

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
        self._child_container_classes = OrderedDict([("profile", ("profile", HwModuleProfileConfig.Profile)), ("fib-scale", ("fib_scale", HwModuleProfileConfig.FibScale)), ("tcam", ("tcam", HwModuleProfileConfig.Tcam))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self
        self._children_name_map["profile"] = "profile"
        self._children_yang_names.add("profile")

        self.fib_scale = HwModuleProfileConfig.FibScale()
        self.fib_scale.parent = self
        self._children_name_map["fib_scale"] = "fib-scale"
        self._children_yang_names.add("fib-scale")

        self.tcam = HwModuleProfileConfig.Tcam()
        self.tcam.parent = self
        self._children_name_map["tcam"] = "tcam"
        self._children_yang_names.add("tcam")
        self._segment_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config"


    class Profile(Entity):
        """
        Configure profile.
        
        .. attribute:: tcam_table
        
        	Configure profile for TCAM LC cards
        	**type**\:  :py:class:`TcamTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable>`
        
        .. attribute:: load_balance
        
        	Configure load balance parameters
        	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.LoadBalance>`
        
        .. attribute:: stats
        
        	Configure stats
        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Stats>`
        
        .. attribute:: netflows
        
        	Configure Netflow profile
        	**type**\:  :py:class:`Netflows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflows>`
        
        .. attribute:: profile_acl
        
        	Configure acl profile
        	**type**\:  :py:class:`ProfileAcl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileAcl>`
        
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
            self._child_container_classes = OrderedDict([("tcam-table", ("tcam_table", HwModuleProfileConfig.Profile.TcamTable)), ("load-balance", ("load_balance", HwModuleProfileConfig.Profile.LoadBalance)), ("stats", ("stats", HwModuleProfileConfig.Profile.Stats)), ("netflows", ("netflows", HwModuleProfileConfig.Profile.Netflows)), ("profile-acl", ("profile_acl", HwModuleProfileConfig.Profile.ProfileAcl)), ("profile-tcam", ("profile_tcam", HwModuleProfileConfig.Profile.ProfileTcam)), ("qos", ("qos", HwModuleProfileConfig.Profile.Qos))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
            self.tcam_table.parent = self
            self._children_name_map["tcam_table"] = "tcam-table"
            self._children_yang_names.add("tcam-table")

            self.load_balance = HwModuleProfileConfig.Profile.LoadBalance()
            self.load_balance.parent = self
            self._children_name_map["load_balance"] = "load-balance"
            self._children_yang_names.add("load-balance")

            self.stats = HwModuleProfileConfig.Profile.Stats()
            self.stats.parent = self
            self._children_name_map["stats"] = "stats"
            self._children_yang_names.add("stats")

            self.netflows = HwModuleProfileConfig.Profile.Netflows()
            self.netflows.parent = self
            self._children_name_map["netflows"] = "netflows"
            self._children_yang_names.add("netflows")

            self.profile_acl = HwModuleProfileConfig.Profile.ProfileAcl()
            self.profile_acl.parent = self
            self._children_name_map["profile_acl"] = "profile-acl"
            self._children_yang_names.add("profile-acl")

            self.profile_tcam = HwModuleProfileConfig.Profile.ProfileTcam()
            self.profile_tcam.parent = self
            self._children_name_map["profile_tcam"] = "profile-tcam"
            self._children_yang_names.add("profile-tcam")

            self.qos = HwModuleProfileConfig.Profile.Qos()
            self.qos.parent = self
            self._children_name_map["qos"] = "qos"
            self._children_yang_names.add("qos")
            self._segment_path = lambda: "profile"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


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
                self._child_container_classes = OrderedDict([("fib-table", ("fib_table", HwModuleProfileConfig.Profile.TcamTable.FibTable))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                self.fib_table.parent = self
                self._children_name_map["fib_table"] = "fib-table"
                self._children_yang_names.add("fib-table")
                self._segment_path = lambda: "tcam-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()


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
                    self._child_container_classes = OrderedDict([("ipv4-address", ("ipv4_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address)), ("ipv6-address", ("ipv6_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                    self.ipv4_address.parent = self
                    self._children_name_map["ipv4_address"] = "ipv4-address"
                    self._children_yang_names.add("ipv4-address")

                    self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                    self.ipv6_address.parent = self
                    self._children_name_map["ipv6_address"] = "ipv6-address"
                    self._children_yang_names.add("ipv6-address")
                    self._segment_path = lambda: "fib-table"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/%s" % self._segment_path()


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
                        self._child_container_classes = OrderedDict([("ipv4-unicast", ("ipv4_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._children_yang_names.add("ipv4-unicast")
                        self._segment_path = lambda: "ipv4-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()


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
                            self._child_container_classes = OrderedDict([("ipv4-unicast-prefix-lengths", ("ipv4_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv4_unicast_percent', YLeaf(YType.uint32, 'ipv4-unicast-percent')),
                            ])
                            self.ipv4_unicast_percent = None

                            self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                            self.ipv4_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv4_unicast_prefix_lengths"] = "ipv4-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv4-unicast-prefix-lengths")
                            self._segment_path = lambda: "ipv4-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/%s" % self._segment_path()

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
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("ipv4-unicast-prefix-length", ("ipv4_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength))])
                                self._leafs = OrderedDict()

                                self.ipv4_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv4-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/%s" % self._segment_path()

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', YLeaf(YType.uint32, 'prefix-length')),
                                        ('ipv4_unicast_prefix_percent', YLeaf(YType.str, 'ipv4-unicast-prefix-percent')),
                                    ])
                                    self.prefix_length = None
                                    self.ipv4_unicast_prefix_percent = None
                                    self._segment_path = lambda: "ipv4-unicast-prefix-length" + "[prefix-length='" + str(self.prefix_length) + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/ipv4-unicast-prefix-lengths/%s" % self._segment_path()

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
                        self._child_container_classes = OrderedDict([("ipv6-unicast", ("ipv6_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._children_yang_names.add("ipv6-unicast")
                        self._segment_path = lambda: "ipv6-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()


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
                            self._child_container_classes = OrderedDict([("ipv6-unicast-prefix-lengths", ("ipv6_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_unicast_percent', YLeaf(YType.uint32, 'ipv6-unicast-percent')),
                            ])
                            self.ipv6_unicast_percent = None

                            self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                            self.ipv6_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv6_unicast_prefix_lengths"] = "ipv6-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv6-unicast-prefix-lengths")
                            self._segment_path = lambda: "ipv6-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/%s" % self._segment_path()

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
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("ipv6-unicast-prefix-length", ("ipv6_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength))])
                                self._leafs = OrderedDict()

                                self.ipv6_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv6-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/%s" % self._segment_path()

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix_length', YLeaf(YType.uint32, 'prefix-length')),
                                        ('ipv6_unicast_prefix_percent', YLeaf(YType.str, 'ipv6-unicast-prefix-percent')),
                                    ])
                                    self.prefix_length = None
                                    self.ipv6_unicast_prefix_percent = None
                                    self._segment_path = lambda: "ipv6-unicast-prefix-length" + "[prefix-length='" + str(self.prefix_length) + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/ipv6-unicast-prefix-lengths/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, ['prefix_length', 'ipv6_unicast_prefix_percent'], name, value)


        class LoadBalance(Entity):
            """
            Configure load balance parameters
            
            .. attribute:: load_balance_profile
            
            	Configure load balance parameters
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('load_balance_profile', YLeaf(YType.int32, 'load-balance-profile')),
                ])
                self.load_balance_profile = None
                self._segment_path = lambda: "load-balance"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.LoadBalance, ['load_balance_profile'], name, value)


        class Stats(Entity):
            """
            Configure stats
            
            .. attribute:: counter_profile
            
            	Configure stats for qos\-enhanced and acl\-permit
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('counter_profile', YLeaf(YType.int32, 'counter-profile')),
                ])
                self.counter_profile = None
                self._segment_path = lambda: "stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Stats, ['counter_profile'], name, value)


        class Netflows(Entity):
            """
            Configure Netflow profile.
            
            .. attribute:: netflow
            
            	none
            	**type**\: list of  		 :py:class:`Netflow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Netflows.Netflow>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Netflows, self).__init__()

                self.yang_name = "netflows"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("netflow", ("netflow", HwModuleProfileConfig.Profile.Netflows.Netflow))])
                self._leafs = OrderedDict()

                self.netflow = YList(self)
                self._segment_path = lambda: "netflows"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Netflows, [], name, value)


            class Netflow(Entity):
                """
                none
                
                .. attribute:: ipfix315_enable  (key)
                
                	none
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: location_string  (key)
                
                	Location of NETFLOW config
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: location_id  (key)
                
                	Location ID hex to Decimal 0xffff for all
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: enable_val
                
                	If Enabled set value to 65535
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Netflows.Netflow, self).__init__()

                    self.yang_name = "netflow"
                    self.yang_parent_name = "netflows"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['ipfix315_enable','location_string','location_id']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ipfix315_enable', YLeaf(YType.str, 'ipfix315-enable')),
                        ('location_string', YLeaf(YType.str, 'location-string')),
                        ('location_id', YLeaf(YType.int32, 'location-id')),
                        ('enable_val', YLeaf(YType.int32, 'enable-val')),
                    ])
                    self.ipfix315_enable = None
                    self.location_string = None
                    self.location_id = None
                    self.enable_val = None
                    self._segment_path = lambda: "netflow" + "[ipfix315-enable='" + str(self.ipfix315_enable) + "']" + "[location-string='" + str(self.location_string) + "']" + "[location-id='" + str(self.location_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/netflows/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Netflows.Netflow, ['ipfix315_enable', 'location_string', 'location_id', 'enable_val'], name, value)


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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('egress', YLeaf(YType.boolean, 'egress')),
                ])
                self.egress = None
                self._segment_path = lambda: "profile-acl"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.ProfileAcl, ['egress'], name, value)


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
                self._child_container_classes = OrderedDict([("key-format", ("key_format", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.key_format = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat()
                self.key_format.parent = self
                self._children_name_map["key_format"] = "key-format"
                self._children_yang_names.add("key-format")
                self._segment_path = lambda: "profile-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()


            class KeyFormat(Entity):
                """
                none
                
                .. attribute:: acl_tables
                
                	Configure acl profile
                	**type**\:  :py:class:`AclTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables>`
                
                

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
                    self._child_container_classes = OrderedDict([("acl-tables", ("acl_tables", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.acl_tables = HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables()
                    self.acl_tables.parent = self
                    self._children_name_map["acl_tables"] = "acl-tables"
                    self._children_yang_names.add("acl-tables")
                    self._segment_path = lambda: "key-format"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/%s" % self._segment_path()


                class AclTables(Entity):
                    """
                    Configure acl profile
                    
                    .. attribute:: acl_table
                    
                    	Configure format for acl profile
                    	**type**\: list of  		 :py:class:`AclTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables.AclTable>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables, self).__init__()

                        self.yang_name = "acl-tables"
                        self.yang_parent_name = "key-format"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("acl-table", ("acl_table", HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables.AclTable))])
                        self._leafs = OrderedDict()

                        self.acl_table = YList(self)
                        self._segment_path = lambda: "acl-tables"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables, [], name, value)


                    class AclTable(Entity):
                        """
                        Configure format for acl profile
                        
                        .. attribute:: address_family  (key)
                        
                        	ipv4/ipv6
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: location_string  (key)
                        
                        	Location string (all) if for all LCs
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: location_id  (key)
                        
                        	Location ID hex to Decimal 0xffff for all
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: source_addr
                        
                        	Source Address 32 bit qual
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: destination_addr
                        
                        	Destination Address 32 bit qual
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: source_port
                        
                        	Source Port
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: dest_port
                        
                        	Destination Port
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: prot_type
                        
                        	Protocol Type
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: tcp_flag
                        
                        	TCP Flags
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: pack_len
                        
                        	Packet Length
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: frag_bit
                        
                        	Fragment Bit
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: precedence
                        
                        	Precedence
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: port_range
                        
                        	PortRange
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: en_ttl
                        
                        	Enable Setting TTL
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: en_match
                        
                        	Enable Matching TTL
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: en_share_acl
                        
                        	Enable Non Shared Interface ACL
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables.AclTable, self).__init__()

                            self.yang_name = "acl-table"
                            self.yang_parent_name = "acl-tables"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['address_family','location_string','location_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_family', YLeaf(YType.str, 'address-family')),
                                ('location_string', YLeaf(YType.str, 'location-string')),
                                ('location_id', YLeaf(YType.int32, 'location-id')),
                                ('source_addr', YLeaf(YType.int32, 'source-addr')),
                                ('destination_addr', YLeaf(YType.int32, 'destination-addr')),
                                ('source_port', YLeaf(YType.int32, 'source-port')),
                                ('dest_port', YLeaf(YType.int32, 'dest-port')),
                                ('prot_type', YLeaf(YType.int32, 'prot-type')),
                                ('tcp_flag', YLeaf(YType.int32, 'tcp-flag')),
                                ('pack_len', YLeaf(YType.int32, 'pack-len')),
                                ('frag_bit', YLeaf(YType.int32, 'frag-bit')),
                                ('precedence', YLeaf(YType.int32, 'precedence')),
                                ('port_range', YLeaf(YType.int32, 'port-range')),
                                ('udf1', YLeaf(YType.str, 'udf1')),
                                ('udf2', YLeaf(YType.str, 'udf2')),
                                ('udf3', YLeaf(YType.str, 'udf3')),
                                ('udf4', YLeaf(YType.str, 'udf4')),
                                ('udf5', YLeaf(YType.str, 'udf5')),
                                ('udf6', YLeaf(YType.str, 'udf6')),
                                ('udf7', YLeaf(YType.str, 'udf7')),
                                ('udf8', YLeaf(YType.str, 'udf8')),
                                ('en_capture', YLeaf(YType.int32, 'en-capture')),
                                ('en_ttl', YLeaf(YType.int32, 'en-ttl')),
                                ('en_match', YLeaf(YType.int32, 'en-match')),
                                ('en_share_acl', YLeaf(YType.int32, 'en-share-acl')),
                            ])
                            self.address_family = None
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
                            self._segment_path = lambda: "acl-table" + "[address-family='" + str(self.address_family) + "']" + "[location-string='" + str(self.location_string) + "']" + "[location-id='" + str(self.location_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/profile-tcam/key-format/acl-tables/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.ProfileTcam.KeyFormat.AclTables.AclTable, ['address_family', 'location_string', 'location_id', 'source_addr', 'destination_addr', 'source_port', 'dest_port', 'prot_type', 'tcp_flag', 'pack_len', 'frag_bit', 'precedence', 'port_range', 'udf1', 'udf2', 'udf3', 'udf4', 'udf5', 'udf6', 'udf7', 'udf8', 'en_capture', 'en_ttl', 'en_match', 'en_share_acl'], name, value)


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
            
            .. attribute:: trunks
            
            	Configure Max Trunk Size
            	**type**\:  :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.Trunks>`
            
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
                self._child_container_classes = OrderedDict([("hqos-enable-all", ("hqos_enable_all", HwModuleProfileConfig.Profile.Qos.HqosEnableAll)), ("ingress-model-root-def", ("ingress_model_root_def", HwModuleProfileConfig.Profile.Qos.IngressModelRootDef)), ("ingress-models", ("ingress_models", HwModuleProfileConfig.Profile.Qos.IngressModels)), ("trunks", ("trunks", HwModuleProfileConfig.Profile.Qos.Trunks)), ("class-maps-root-def", ("class_maps_root_def", HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef)), ("class-maps", ("class_maps", HwModuleProfileConfig.Profile.Qos.ClassMaps))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.hqos_enable_all = HwModuleProfileConfig.Profile.Qos.HqosEnableAll()
                self.hqos_enable_all.parent = self
                self._children_name_map["hqos_enable_all"] = "hqos-enable-all"
                self._children_yang_names.add("hqos-enable-all")

                self.ingress_model_root_def = HwModuleProfileConfig.Profile.Qos.IngressModelRootDef()
                self.ingress_model_root_def.parent = self
                self._children_name_map["ingress_model_root_def"] = "ingress-model-root-def"
                self._children_yang_names.add("ingress-model-root-def")

                self.ingress_models = HwModuleProfileConfig.Profile.Qos.IngressModels()
                self.ingress_models.parent = self
                self._children_name_map["ingress_models"] = "ingress-models"
                self._children_yang_names.add("ingress-models")

                self.trunks = HwModuleProfileConfig.Profile.Qos.Trunks()
                self.trunks.parent = self
                self._children_name_map["trunks"] = "trunks"
                self._children_yang_names.add("trunks")

                self.class_maps_root_def = HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef()
                self.class_maps_root_def.parent = self
                self._children_name_map["class_maps_root_def"] = "class-maps-root-def"
                self._children_yang_names.add("class-maps-root-def")

                self.class_maps = HwModuleProfileConfig.Profile.Qos.ClassMaps()
                self.class_maps.parent = self
                self._children_name_map["class_maps"] = "class-maps"
                self._children_yang_names.add("class-maps")
                self._segment_path = lambda: "qos"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()


            class HqosEnableAll(Entity):
                """
                Configure Hqos profile
                
                .. attribute:: hqos_enable
                
                	 Hqos profile value
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hqos_enable', YLeaf(YType.int32, 'hqos-enable')),
                    ])
                    self.hqos_enable = None
                    self._segment_path = lambda: "hqos-enable-all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.HqosEnableAll, ['hqos_enable'], name, value)


            class IngressModelRootDef(Entity):
                """
                Configure Ingress Model Default
                
                .. attribute:: ingress_model_leaf_def
                
                	Ingress Model Default
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ingress_model_leaf_def', YLeaf(YType.int32, 'ingress-model-leaf-def')),
                    ])
                    self.ingress_model_leaf_def = None
                    self._segment_path = lambda: "ingress-model-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ingress-model", ("ingress_model", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel))])
                    self._leafs = OrderedDict()

                    self.ingress_model = YList(self)
                    self._segment_path = lambda: "ingress-models"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

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
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ingress-model-leaf", ("ingress_model_leaf", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf))])
                        self._leafs = OrderedDict([
                            ('node_name', YLeaf(YType.str, 'node-name')),
                        ])
                        self.node_name = None

                        self.ingress_model_leaf = YList(self)
                        self._segment_path = lambda: "ingress-model" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/ingress-models/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel, ['node_name'], name, value)


                    class IngressModelLeaf(Entity):
                        """
                        Configure Ingress Model Leaf
                        
                        .. attribute:: location  (key)
                        
                        	Location
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ingress_model_leaf
                        
                        	IngressModelLeaf
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', YLeaf(YType.int32, 'location')),
                                ('ingress_model_leaf', YLeaf(YType.int32, 'ingress-model-leaf')),
                            ])
                            self.location = None
                            self.ingress_model_leaf = None
                            self._segment_path = lambda: "ingress-model-leaf" + "[location='" + str(self.location) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf, ['location', 'ingress_model_leaf'], name, value)


            class Trunks(Entity):
                """
                Configure Max Trunk Size
                
                .. attribute:: trunk_size
                
                	Max Trunk Size
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.Trunks, self).__init__()

                    self.yang_name = "trunks"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('trunk_size', YLeaf(YType.int32, 'trunk-size')),
                    ])
                    self.trunk_size = None
                    self._segment_path = lambda: "trunks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.Trunks, ['trunk_size'], name, value)


            class ClassMapsRootDef(Entity):
                """
                Configure Class Maps Default
                
                .. attribute:: class_map_size_def
                
                	Class Map Size Default
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('class_map_size_def', YLeaf(YType.int32, 'class-map-size-def')),
                    ])
                    self.class_map_size_def = None
                    self._segment_path = lambda: "class-maps-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("class-map", ("class_map", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap))])
                    self._leafs = OrderedDict()

                    self.class_map = YList(self)
                    self._segment_path = lambda: "class-maps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

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
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("class-map-size", ("class_map_size", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize))])
                        self._leafs = OrderedDict([
                            ('node_name', YLeaf(YType.str, 'node-name')),
                        ])
                        self.node_name = None

                        self.class_map_size = YList(self)
                        self._segment_path = lambda: "class-map" + "[node-name='" + str(self.node_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/class-maps/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap, ['node_name'], name, value)


                    class ClassMapSize(Entity):
                        """
                        Class Map Size
                        
                        .. attribute:: location  (key)
                        
                        	Location
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: class_map_size
                        
                        	ClassMapSize
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('location', YLeaf(YType.int32, 'location')),
                                ('class_map_size', YLeaf(YType.int32, 'class-map-size')),
                            ])
                            self.location = None
                            self.class_map_size = None
                            self._segment_path = lambda: "class-map-size" + "[location='" + str(self.location) + "']"

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
            self._child_container_classes = OrderedDict([("ipv6-unicast-scale-no-tcam", ("ipv6_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam)), ("ipv4-unicast-scale-no-tcam", ("ipv4_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.ipv6_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam()
            self.ipv6_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv6_unicast_scale_no_tcam"] = "ipv6-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv6-unicast-scale-no-tcam")

            self.ipv4_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam()
            self.ipv4_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv4_unicast_scale_no_tcam"] = "ipv4-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv4-unicast-scale-no-tcam")
            self._segment_path = lambda: "fib-scale"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


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
                self._child_container_classes = OrderedDict([("scale-ipv6-no-tcam", ("scale_ipv6_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.scale_ipv6_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam()
                self.scale_ipv6_no_tcam.parent = self
                self._children_name_map["scale_ipv6_no_tcam"] = "scale-ipv6-no-tcam"
                self._children_yang_names.add("scale-ipv6-no-tcam")
                self._segment_path = lambda: "ipv6-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()


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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('internet_optimized_ipv6_no_tcam', YLeaf(YType.str, 'internet-optimized-ipv6-no-tcam')),
                    ])
                    self.internet_optimized_ipv6_no_tcam = None
                    self._segment_path = lambda: "scale-ipv6-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv6-unicast-scale-no-tcam/%s" % self._segment_path()

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
                self._child_container_classes = OrderedDict([("scale-ipv4-no-tcam", ("scale_ipv4_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.scale_ipv4_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam()
                self.scale_ipv4_no_tcam.parent = self
                self._children_name_map["scale_ipv4_no_tcam"] = "scale-ipv4-no-tcam"
                self._children_yang_names.add("scale-ipv4-no-tcam")
                self._segment_path = lambda: "ipv4-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()


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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('optimized_ipv4_no_tcam', YLeaf(YType.str, 'optimized-ipv4-no-tcam')),
                    ])
                    self.optimized_ipv4_no_tcam = None
                    self._segment_path = lambda: "scale-ipv4-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv4-unicast-scale-no-tcam/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, ['optimized_ipv4_no_tcam'], name, value)


    class Tcam(Entity):
        """
        Configure Tcam.
        
        .. attribute:: fib_tcam_scale
        
        	Configure Fib iscale for Tcam
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
            self._child_container_classes = OrderedDict([("fib-tcam-scale", ("fib_tcam_scale", HwModuleProfileConfig.Tcam.FibTcamScale))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.fib_tcam_scale = HwModuleProfileConfig.Tcam.FibTcamScale()
            self.fib_tcam_scale.parent = self
            self._children_name_map["fib_tcam_scale"] = "fib-tcam-scale"
            self._children_yang_names.add("fib-tcam-scale")
            self._segment_path = lambda: "tcam"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


        class FibTcamScale(Entity):
            """
            Configure Fib iscale for Tcam.
            
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
                self._child_container_classes = OrderedDict([("ipv4-unicast-scale", ("ipv4_unicast_scale", HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.ipv4_unicast_scale = HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale()
                self.ipv4_unicast_scale.parent = self
                self._children_name_map["ipv4_unicast_scale"] = "ipv4-unicast-scale"
                self._children_yang_names.add("ipv4-unicast-scale")
                self._segment_path = lambda: "fib-tcam-scale"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/%s" % self._segment_path()


            class Ipv4UnicastScale(Entity):
                """
                IPv4 table for TCAM LC Scale.
                
                .. attribute:: ipv4_scale
                
                	Scale for IPv4 table for TCAM LC
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

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
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ipv4_scale', YLeaf(YType.empty, 'ipv4-scale')),
                    ])
                    self.ipv4_scale = None
                    self._segment_path = lambda: "ipv4-unicast-scale"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/fib-tcam-scale/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, ['ipv4_scale'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModuleProfileConfig()
        return self._top_entity

