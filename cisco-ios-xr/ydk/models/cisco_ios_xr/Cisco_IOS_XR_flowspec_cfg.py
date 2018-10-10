""" Cisco_IOS_XR_flowspec_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR flowspec package configuration.

This module contains definitions
for the following management objects\:
  flow\-spec\: FlowSpec configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FsAddf(Enum):
    """
    FsAddf (Enum Class)

    Fs addf

    .. data:: ipv4 = 1

    	IPv4 FlowSpec

    .. data:: ipv6 = 2

    	IPv6 FlowSpec

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class FsAfP(Enum):
    """
    FsAfP (Enum Class)

    Fs af p

    .. data:: pbr = 2

    	PBR policy type

    """

    pbr = Enum.YLeaf(2, "pbr")


class FsVrfAf(Enum):
    """
    FsVrfAf (Enum Class)

    Fs vrf af

    .. data:: ipv4 = 1

    	IPv4 FlowSpec

    .. data:: ipv6 = 2

    	IPv6 FlowSpec

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class FsVrfAfP(Enum):
    """
    FsVrfAfP (Enum Class)

    Fs vrf af p

    .. data:: pbr = 2

    	PBR policy type

    """

    pbr = Enum.YLeaf(2, "pbr")



class FlowSpec(Entity):
    """
    FlowSpec configuration
    
    .. attribute:: afs
    
    	Table of AF
    	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Afs>`
    
    .. attribute:: vrfs
    
    	Table of VRF
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs>`
    
    .. attribute:: enable
    
    	Enable FlowSpec configuration. Deletion of this object also causes deletion of all associated objects under FlowSpec
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: interface_all
    
    	Install FlowSpec policy on all interfaces
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'flowspec-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(FlowSpec, self).__init__()
        self._top_entity = None

        self.yang_name = "flow-spec"
        self.yang_parent_name = "Cisco-IOS-XR-flowspec-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("afs", ("afs", FlowSpec.Afs)), ("vrfs", ("vrfs", FlowSpec.Vrfs))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('interface_all', (YLeaf(YType.empty, 'interface-all'), ['Empty'])),
        ])
        self.enable = None
        self.interface_all = None

        self.afs = FlowSpec.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"

        self.vrfs = FlowSpec.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-flowspec-cfg:flow-spec"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FlowSpec, ['enable', 'interface_all'], name, value)


    class Afs(Entity):
        """
        Table of AF
        
        .. attribute:: af
        
        	Address Family Identifier Type (IPv4/IPv6)
        	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Afs.Af>`
        
        

        """

        _prefix = 'flowspec-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(FlowSpec.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "flow-spec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("af", ("af", FlowSpec.Afs.Af))])
            self._leafs = OrderedDict()

            self.af = YList(self)
            self._segment_path = lambda: "afs"
            self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-cfg:flow-spec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FlowSpec.Afs, [], name, value)


        class Af(Entity):
            """
            Address Family Identifier Type (IPv4/IPv6)
            
            .. attribute:: af_name  (key)
            
            	AFI type
            	**type**\:  :py:class:`FsAddf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FsAddf>`
            
            .. attribute:: service_policies
            
            	Table of ServicePolicy
            	**type**\:  :py:class:`ServicePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Afs.Af.ServicePolicies>`
            
            .. attribute:: interface_all
            
            	Install FlowSpec policy on all interfaces
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'flowspec-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(FlowSpec.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af_name']
                self._child_classes = OrderedDict([("service-policies", ("service_policies", FlowSpec.Afs.Af.ServicePolicies))])
                self._leafs = OrderedDict([
                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAddf', '')])),
                    ('interface_all', (YLeaf(YType.empty, 'interface-all'), ['Empty'])),
                ])
                self.af_name = None
                self.interface_all = None

                self.service_policies = FlowSpec.Afs.Af.ServicePolicies()
                self.service_policies.parent = self
                self._children_name_map["service_policies"] = "service-policies"
                self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-cfg:flow-spec/afs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FlowSpec.Afs.Af, ['af_name', 'interface_all'], name, value)


            class ServicePolicies(Entity):
                """
                Table of ServicePolicy
                
                .. attribute:: service_policy
                
                	Service Policy configuration
                	**type**\: list of  		 :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Afs.Af.ServicePolicies.ServicePolicy>`
                
                

                """

                _prefix = 'flowspec-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FlowSpec.Afs.Af.ServicePolicies, self).__init__()

                    self.yang_name = "service-policies"
                    self.yang_parent_name = "af"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("service-policy", ("service_policy", FlowSpec.Afs.Af.ServicePolicies.ServicePolicy))])
                    self._leafs = OrderedDict()

                    self.service_policy = YList(self)
                    self._segment_path = lambda: "service-policies"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowSpec.Afs.Af.ServicePolicies, [], name, value)


                class ServicePolicy(Entity):
                    """
                    Service Policy configuration
                    
                    .. attribute:: policy_name  (key)
                    
                    	Policy map name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: policy_type
                    
                    	keys\: policy\-type
                    	**type**\: list of  		 :py:class:`PolicyType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Afs.Af.ServicePolicies.ServicePolicy.PolicyType>`
                    
                    

                    """

                    _prefix = 'flowspec-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FlowSpec.Afs.Af.ServicePolicies.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "service-policies"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['policy_name']
                        self._child_classes = OrderedDict([("policy-type", ("policy_type", FlowSpec.Afs.Af.ServicePolicies.ServicePolicy.PolicyType))])
                        self._leafs = OrderedDict([
                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                        ])
                        self.policy_name = None

                        self.policy_type = YList(self)
                        self._segment_path = lambda: "service-policy" + "[policy-name='" + str(self.policy_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FlowSpec.Afs.Af.ServicePolicies.ServicePolicy, ['policy_name'], name, value)


                    class PolicyType(Entity):
                        """
                        keys\: policy\-type
                        
                        .. attribute:: policy_type  (key)
                        
                        	Choose the Policy type
                        	**type**\:  :py:class:`FsAfP <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FsAfP>`
                        
                        .. attribute:: local
                        
                        	Set constant integer
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'flowspec-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FlowSpec.Afs.Af.ServicePolicies.ServicePolicy.PolicyType, self).__init__()

                            self.yang_name = "policy-type"
                            self.yang_parent_name = "service-policy"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['policy_type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('policy_type', (YLeaf(YType.enumeration, 'policy-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsAfP', '')])),
                                ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                            ])
                            self.policy_type = None
                            self.local = None
                            self._segment_path = lambda: "policy-type" + "[policy-type='" + str(self.policy_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FlowSpec.Afs.Af.ServicePolicies.ServicePolicy.PolicyType, ['policy_type', 'local'], name, value)


    class Vrfs(Entity):
        """
        Table of VRF
        
        .. attribute:: vrf
        
        	VRF configuration
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf>`
        
        

        """

        _prefix = 'flowspec-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(FlowSpec.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "flow-spec"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", FlowSpec.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-cfg:flow-spec/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FlowSpec.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF configuration
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: afs
            
            	Table of AF
            	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf.Afs>`
            
            

            """

            _prefix = 'flowspec-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(FlowSpec.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("afs", ("afs", FlowSpec.Vrfs.Vrf.Afs))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.afs = FlowSpec.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-flowspec-cfg:flow-spec/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FlowSpec.Vrfs.Vrf, ['vrf_name'], name, value)


            class Afs(Entity):
                """
                Table of AF
                
                .. attribute:: af
                
                	Address Family Identifier Type (IPv4/IPv6)
                	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'flowspec-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FlowSpec.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("af", ("af", FlowSpec.Vrfs.Vrf.Afs.Af))])
                    self._leafs = OrderedDict()

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Address Family Identifier Type (IPv4/IPv6)
                    
                    .. attribute:: af_name  (key)
                    
                    	AFI type
                    	**type**\:  :py:class:`FsVrfAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FsVrfAf>`
                    
                    .. attribute:: service_policies
                    
                    	Table of ServicePolicy
                    	**type**\:  :py:class:`ServicePolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies>`
                    
                    .. attribute:: interface_all
                    
                    	Install FlowSpec policy on all interfaces
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'flowspec-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FlowSpec.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['af_name']
                        self._child_classes = OrderedDict([("service-policies", ("service_policies", FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies))])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsVrfAf', '')])),
                            ('interface_all', (YLeaf(YType.empty, 'interface-all'), ['Empty'])),
                        ])
                        self.af_name = None
                        self.interface_all = None

                        self.service_policies = FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies()
                        self.service_policies.parent = self
                        self._children_name_map["service_policies"] = "service-policies"
                        self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af, ['af_name', 'interface_all'], name, value)


                    class ServicePolicies(Entity):
                        """
                        Table of ServicePolicy
                        
                        .. attribute:: service_policy
                        
                        	Service Policy configuration
                        	**type**\: list of  		 :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy>`
                        
                        

                        """

                        _prefix = 'flowspec-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies, self).__init__()

                            self.yang_name = "service-policies"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("service-policy", ("service_policy", FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy))])
                            self._leafs = OrderedDict()

                            self.service_policy = YList(self)
                            self._segment_path = lambda: "service-policies"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies, [], name, value)


                        class ServicePolicy(Entity):
                            """
                            Service Policy configuration
                            
                            .. attribute:: policy_name  (key)
                            
                            	Policy map name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: policy_type
                            
                            	keys\: policy\-type
                            	**type**\: list of  		 :py:class:`PolicyType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy.PolicyType>`
                            
                            

                            """

                            _prefix = 'flowspec-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy, self).__init__()

                                self.yang_name = "service-policy"
                                self.yang_parent_name = "service-policies"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['policy_name']
                                self._child_classes = OrderedDict([("policy-type", ("policy_type", FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy.PolicyType))])
                                self._leafs = OrderedDict([
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                ])
                                self.policy_name = None

                                self.policy_type = YList(self)
                                self._segment_path = lambda: "service-policy" + "[policy-name='" + str(self.policy_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy, ['policy_name'], name, value)


                            class PolicyType(Entity):
                                """
                                keys\: policy\-type
                                
                                .. attribute:: policy_type  (key)
                                
                                	Choose the Policy type
                                	**type**\:  :py:class:`FsVrfAfP <ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg.FsVrfAfP>`
                                
                                .. attribute:: local
                                
                                	Set constant integer
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'flowspec-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy.PolicyType, self).__init__()

                                    self.yang_name = "policy-type"
                                    self.yang_parent_name = "service-policy"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['policy_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('policy_type', (YLeaf(YType.enumeration, 'policy-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_flowspec_cfg', 'FsVrfAfP', '')])),
                                        ('local', (YLeaf(YType.boolean, 'local'), ['bool'])),
                                    ])
                                    self.policy_type = None
                                    self.local = None
                                    self._segment_path = lambda: "policy-type" + "[policy-type='" + str(self.policy_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FlowSpec.Vrfs.Vrf.Afs.Af.ServicePolicies.ServicePolicy.PolicyType, ['policy_type', 'local'], name, value)

    def clone_ptr(self):
        self._top_entity = FlowSpec()
        return self._top_entity

