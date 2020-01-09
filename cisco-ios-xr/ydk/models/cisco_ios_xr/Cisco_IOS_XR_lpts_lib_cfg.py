""" Cisco_IOS_XR_lpts_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-lib package configuration.

This module contains definitions
for the following management objects\:
  lpts\: lpts configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Lpts(_Entity_):
    """
    lpts configuration commands
    
    .. attribute:: ipolicer
    
    	Pre IFiB Policer Configuration 
    	**type**\:  :py:class:`Ipolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer>`
    
    	**presence node**\: True
    
    .. attribute:: domain_names
    
    	Pre IFiB Domains Configuration 
    	**type**\:  :py:class:`DomainNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.DomainNames>`
    
    .. attribute:: ipunt_policer
    
    	Pre IFiB Punt Policer Configuration 
    	**type**\:  :py:class:`IpuntPolicer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer>`
    
    	**presence node**\: True
    
    .. attribute:: punt
    
    	Configure penalty timeout value
    	**type**\:  :py:class:`Punt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt>`
    
    

    """

    _prefix = 'lpts-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Lpts, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-lib-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer", ("ipolicer", Lpts.Ipolicer)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:domain-names", ("domain_names", Lpts.DomainNames)), ("Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer", ("ipunt_policer", Lpts.IpuntPolicer)), ("Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt", ("punt", Lpts.Punt))])
        self._leafs = OrderedDict()

        self.ipolicer = None
        self._children_name_map["ipolicer"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer"

        self.domain_names = Lpts.DomainNames()
        self.domain_names.parent = self
        self._children_name_map["domain_names"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:domain-names"

        self.ipunt_policer = None
        self._children_name_map["ipunt_policer"] = "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer"

        self.punt = Lpts.Punt()
        self.punt.parent = self
        self._children_name_map["punt"] = "Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt"
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lpts, [], name, value)


    class Ipolicer(_Entity_):
        """
        Pre IFiB Policer Configuration 
        
        .. attribute:: acls
        
        	Table for ACLs
        	**type**\:  :py:class:`Acls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls>`
        
        .. attribute:: enable
        
        	Enabled
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: policer_domains
        
        	Policer Domain Table
        	**type**\:  :py:class:`PolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.PolicerDomains>`
        
        .. attribute:: flows
        
        	Table for Flows
        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2019-10-23'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Lpts.Ipolicer, self).__init__()

            self.yang_name = "ipolicer"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("acls", ("acls", Lpts.Ipolicer.Acls)), ("policer-domains", ("policer_domains", Lpts.Ipolicer.PolicerDomains)), ("flows", ("flows", Lpts.Ipolicer.Flows))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.acls = Lpts.Ipolicer.Acls()
            self.acls.parent = self
            self._children_name_map["acls"] = "acls"

            self.policer_domains = Lpts.Ipolicer.PolicerDomains()
            self.policer_domains.parent = self
            self._children_name_map["policer_domains"] = "policer-domains"

            self.flows = Lpts.Ipolicer.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.Ipolicer, ['enable'], name, value)


        class Acls(_Entity_):
            """
            Table for ACLs
            
            .. attribute:: acl
            
            	ACL name
            	**type**\: list of  		 :py:class:`Acl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.Ipolicer.Acls, self).__init__()

                self.yang_name = "acls"
                self.yang_parent_name = "ipolicer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("acl", ("acl", Lpts.Ipolicer.Acls.Acl))])
                self._leafs = OrderedDict()

                self.acl = YList(self)
                self._segment_path = lambda: "acls"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Ipolicer.Acls, [], name, value)


            class Acl(_Entity_):
                """
                ACL name
                
                .. attribute:: acl_name  (key)
                
                	ACL name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: afi_types
                
                	AFI Family
                	**type**\:  :py:class:`AfiTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Ipolicer.Acls.Acl, self).__init__()

                    self.yang_name = "acl"
                    self.yang_parent_name = "acls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['acl_name']
                    self._child_classes = OrderedDict([("afi-types", ("afi_types", Lpts.Ipolicer.Acls.Acl.AfiTypes))])
                    self._leafs = OrderedDict([
                        ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                    ])
                    self.acl_name = None

                    self.afi_types = Lpts.Ipolicer.Acls.Acl.AfiTypes()
                    self.afi_types.parent = self
                    self._children_name_map["afi_types"] = "afi-types"
                    self._segment_path = lambda: "acl" + "[acl-name='" + str(self.acl_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/acls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Ipolicer.Acls.Acl, ['acl_name'], name, value)


                class AfiTypes(_Entity_):
                    """
                    AFI Family
                    
                    .. attribute:: afi_type
                    
                    	AFI Family type
                    	**type**\: list of  		 :py:class:`AfiType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Ipolicer.Acls.Acl.AfiTypes, self).__init__()

                        self.yang_name = "afi-types"
                        self.yang_parent_name = "acl"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("afi-type", ("afi_type", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType))])
                        self._leafs = OrderedDict()

                        self.afi_type = YList(self)
                        self._segment_path = lambda: "afi-types"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes, [], name, value)


                    class AfiType(_Entity_):
                        """
                        AFI Family type
                        
                        .. attribute:: afi_family_type  (key)
                        
                        	AFI Family Type
                        	**type**\:  :py:class:`Lptsafi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.Lptsafi>`
                        
                        .. attribute:: vrf_names
                        
                        	VRF list
                        	**type**\:  :py:class:`VrfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames>`
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType, self).__init__()

                            self.yang_name = "afi-type"
                            self.yang_parent_name = "afi-types"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['afi_family_type']
                            self._child_classes = OrderedDict([("vrf-names", ("vrf_names", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames))])
                            self._leafs = OrderedDict([
                                ('afi_family_type', (YLeaf(YType.enumeration, 'afi-family-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'Lptsafi', '')])),
                            ])
                            self.afi_family_type = None

                            self.vrf_names = Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames()
                            self.vrf_names.parent = self
                            self._children_name_map["vrf_names"] = "vrf-names"
                            self._segment_path = lambda: "afi-type" + "[afi-family-type='" + str(self.afi_family_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType, ['afi_family_type'], name, value)


                        class VrfNames(_Entity_):
                            """
                            VRF list
                            
                            .. attribute:: vrf_name
                            
                            	VRF name
                            	**type**\: list of  		 :py:class:`VrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName>`
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames, self).__init__()

                                self.yang_name = "vrf-names"
                                self.yang_parent_name = "afi-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("vrf-name", ("vrf_name", Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName))])
                                self._leafs = OrderedDict()

                                self.vrf_name = YList(self)
                                self._segment_path = lambda: "vrf-names"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames, [], name, value)


                            class VrfName(_Entity_):
                                """
                                VRF name
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: acl_rate
                                
                                	pre\-ifib policer rate config commands
                                	**type**\: int
                                
                                	**range:** 0..100000
                                
                                

                                """

                                _prefix = 'lpts-pre-ifib-cfg'
                                _revision = '2019-10-23'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName, self).__init__()

                                    self.yang_name = "vrf-name"
                                    self.yang_parent_name = "vrf-names"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                        ('acl_rate', (YLeaf(YType.uint32, 'acl-rate'), ['int'])),
                                    ])
                                    self.vrf_name = None
                                    self.acl_rate = None
                                    self._segment_path = lambda: "vrf-name" + "[vrf-name='" + str(self.vrf_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName, ['vrf_name', 'acl_rate'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                                    return meta._meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames.VrfName']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                                return meta._meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType.VrfNames']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes.AfiType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.Acls.Acl.AfiTypes']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Acls.Acl']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Acls']['meta_info']


        class PolicerDomains(_Entity_):
            """
            Policer Domain Table
            
            .. attribute:: policer_domain
            
            	Domain name
            	**type**\: list of  		 :py:class:`PolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.PolicerDomains.PolicerDomain>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.Ipolicer.PolicerDomains, self).__init__()

                self.yang_name = "policer-domains"
                self.yang_parent_name = "ipolicer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policer-domain", ("policer_domain", Lpts.Ipolicer.PolicerDomains.PolicerDomain))])
                self._leafs = OrderedDict()

                self.policer_domain = YList(self)
                self._segment_path = lambda: "policer-domains"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Ipolicer.PolicerDomains, [], name, value)


            class PolicerDomain(_Entity_):
                """
                Domain name
                
                .. attribute:: domain_name  (key)
                
                	Domain name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: flows
                
                	Table for Flows
                	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Ipolicer.PolicerDomains.PolicerDomain, self).__init__()

                    self.yang_name = "policer-domain"
                    self.yang_parent_name = "policer-domains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain_name']
                    self._child_classes = OrderedDict([("flows", ("flows", Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows))])
                    self._leafs = OrderedDict([
                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                    ])
                    self.domain_name = None

                    self.flows = Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                    self._segment_path = lambda: "policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/policer-domains/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Ipolicer.PolicerDomains.PolicerDomain, ['domain_name'], name, value)


                class Flows(_Entity_):
                    """
                    Table for Flows
                    
                    .. attribute:: flow
                    
                    	selected flow type
                    	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows, self).__init__()

                        self.yang_name = "flows"
                        self.yang_parent_name = "policer-domain"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow", ("flow", Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow))])
                        self._leafs = OrderedDict()

                        self.flow = YList(self)
                        self._segment_path = lambda: "flows"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows, [], name, value)


                    class Flow(_Entity_):
                        """
                        selected flow type
                        
                        .. attribute:: flow_type  (key)
                        
                        	LPTS Flow Type
                        	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                        
                        .. attribute:: precedences
                        
                        	TOS Precedence value(s)
                        	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences>`
                        
                        .. attribute:: rate
                        
                        	Configured rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow, self).__init__()

                            self.yang_name = "flow"
                            self.yang_parent_name = "flows"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['flow_type']
                            self._child_classes = OrderedDict([("precedences", ("precedences", Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences))])
                            self._leafs = OrderedDict([
                                ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ])
                            self.flow_type = None
                            self.rate = None

                            self.precedences = Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences()
                            self.precedences.parent = self
                            self._children_name_map["precedences"] = "precedences"
                            self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow, ['flow_type', 'rate'], name, value)


                        class Precedences(_Entity_):
                            """
                            TOS Precedence value(s)
                            
                            .. attribute:: precedence
                            
                            	Precedence values
                            	**type**\: union of the below types:
                            
                            		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                            
                            		**type**\: list of int
                            
                            			**range:** 0..7
                            
                            

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, self).__init__()

                                self.yang_name = "precedences"
                                self.yang_parent_name = "flow"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                                ])
                                self.precedence = []
                                self._segment_path = lambda: "precedences"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences, ['precedence'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                                return meta._meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow.Precedences']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows.Flow']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain.Flows']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.PolicerDomains.PolicerDomain']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.PolicerDomains']['meta_info']


        class Flows(_Entity_):
            """
            Table for Flows
            
            .. attribute:: flow
            
            	selected flow type
            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.Ipolicer.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "ipolicer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("flow", ("flow", Lpts.Ipolicer.Flows.Flow))])
                self._leafs = OrderedDict()

                self.flow = YList(self)
                self._segment_path = lambda: "flows"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Ipolicer.Flows, [], name, value)


            class Flow(_Entity_):
                """
                selected flow type
                
                .. attribute:: flow_type  (key)
                
                	LPTS Flow Type
                	**type**\:  :py:class:`LptsFlow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsFlow>`
                
                .. attribute:: precedences
                
                	TOS Precedence value(s)
                	**type**\:  :py:class:`Precedences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Ipolicer.Flows.Flow.Precedences>`
                
                .. attribute:: rate
                
                	Configured rate value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Ipolicer.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['flow_type']
                    self._child_classes = OrderedDict([("precedences", ("precedences", Lpts.Ipolicer.Flows.Flow.Precedences))])
                    self._leafs = OrderedDict([
                        ('flow_type', (YLeaf(YType.enumeration, 'flow-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow', '')])),
                        ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                    ])
                    self.flow_type = None
                    self.rate = None

                    self.precedences = Lpts.Ipolicer.Flows.Flow.Precedences()
                    self.precedences.parent = self
                    self._children_name_map["precedences"] = "precedences"
                    self._segment_path = lambda: "flow" + "[flow-type='" + str(self.flow_type) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipolicer/flows/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Ipolicer.Flows.Flow, ['flow_type', 'rate'], name, value)


                class Precedences(_Entity_):
                    """
                    TOS Precedence value(s)
                    
                    .. attribute:: precedence
                    
                    	Precedence values
                    	**type**\: union of the below types:
                    
                    		**type**\: list of   :py:class:`LptsPreIFibPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPreIFibPrecedenceNumber>`
                    
                    		**type**\: list of int
                    
                    			**range:** 0..7
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Ipolicer.Flows.Flow.Precedences, self).__init__()

                        self.yang_name = "precedences"
                        self.yang_parent_name = "flow"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('precedence', (YLeafList(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber', ''),'int'])),
                        ])
                        self.precedence = []
                        self._segment_path = lambda: "precedences"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Ipolicer.Flows.Flow.Precedences, ['precedence'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Ipolicer.Flows']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.Ipolicer']['meta_info']


    class DomainNames(_Entity_):
        """
        Pre IFiB Domains Configuration 
        
        .. attribute:: domain_name
        
        	Domain name
        	**type**\: list of  		 :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.DomainNames.DomainName>`
        
        

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2019-10-23'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Lpts.DomainNames, self).__init__()

            self.yang_name = "domain-names"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("domain-name", ("domain_name", Lpts.DomainNames.DomainName))])
            self._leafs = OrderedDict()

            self.domain_name = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:domain-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.DomainNames, [], name, value)


        class DomainName(_Entity_):
            """
            Domain name
            
            .. attribute:: domain_name  (key)
            
            	Domain name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: interface_names
            
            	Domain Interface
            	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.DomainNames.DomainName.InterfaceNames>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.DomainNames.DomainName, self).__init__()

                self.yang_name = "domain-name"
                self.yang_parent_name = "domain-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['domain_name']
                self._child_classes = OrderedDict([("interface-names", ("interface_names", Lpts.DomainNames.DomainName.InterfaceNames))])
                self._leafs = OrderedDict([
                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                ])
                self.domain_name = None

                self.interface_names = Lpts.DomainNames.DomainName.InterfaceNames()
                self.interface_names.parent = self
                self._children_name_map["interface_names"] = "interface-names"
                self._segment_path = lambda: "domain-name" + "[domain-name='" + str(self.domain_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:domain-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.DomainNames.DomainName, ['domain_name'], name, value)


            class InterfaceNames(_Entity_):
                """
                Domain Interface
                
                .. attribute:: interface_name
                
                	pre\-ifib Domain Single interface configuration
                	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.DomainNames.DomainName.InterfaceNames, self).__init__()

                    self.yang_name = "interface-names"
                    self.yang_parent_name = "domain-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-name", ("interface_name", Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName))])
                    self._leafs = OrderedDict()

                    self.interface_name = YList(self)
                    self._segment_path = lambda: "interface-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.DomainNames.DomainName.InterfaceNames, [], name, value)


                class InterfaceName(_Entity_):
                    """
                    pre\-ifib Domain Single interface
                    configuration
                    
                    .. attribute:: domain_interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: domain_interface_name_xr
                    
                    	Enabled or disabled
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName, self).__init__()

                        self.yang_name = "interface-name"
                        self.yang_parent_name = "interface-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['domain_interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('domain_interface_name', (YLeaf(YType.str, 'domain-interface-name'), ['str'])),
                            ('domain_interface_name_xr', (YLeaf(YType.boolean, 'domain-interface-name-xr'), ['bool'])),
                        ])
                        self.domain_interface_name = None
                        self.domain_interface_name_xr = None
                        self._segment_path = lambda: "interface-name" + "[domain-interface-name='" + str(self.domain_interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName, ['domain_interface_name', 'domain_interface_name_xr'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.DomainNames.DomainName.InterfaceNames.InterfaceName']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.DomainNames.DomainName.InterfaceNames']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.DomainNames.DomainName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.DomainNames']['meta_info']


    class IpuntPolicer(_Entity_):
        """
        Pre IFiB Punt Policer Configuration 
        
        .. attribute:: punt_type_table
        
        	Punt Policer Table
        	**type**\:  :py:class:`PuntTypeTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntTypeTable>`
        
        .. attribute:: enable
        
        	Enabled
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: punt_policer_domains
        
        	Punt Policer Domain Table
        	**type**\:  :py:class:`PuntPolicerDomains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerDomains>`
        
        .. attribute:: punt_policer_interface_names
        
        	Punt Policer Interface
        	**type**\:  :py:class:`PuntPolicerInterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerInterfaceNames>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'lpts-pre-ifib-cfg'
        _revision = '2019-10-23'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Lpts.IpuntPolicer, self).__init__()

            self.yang_name = "ipunt-policer"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("punt-type-table", ("punt_type_table", Lpts.IpuntPolicer.PuntTypeTable)), ("punt-policer-domains", ("punt_policer_domains", Lpts.IpuntPolicer.PuntPolicerDomains)), ("punt-policer-interface-names", ("punt_policer_interface_names", Lpts.IpuntPolicer.PuntPolicerInterfaceNames))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.punt_type_table = Lpts.IpuntPolicer.PuntTypeTable()
            self.punt_type_table.parent = self
            self._children_name_map["punt_type_table"] = "punt-type-table"

            self.punt_policer_domains = Lpts.IpuntPolicer.PuntPolicerDomains()
            self.punt_policer_domains.parent = self
            self._children_name_map["punt_policer_domains"] = "punt-policer-domains"

            self.punt_policer_interface_names = Lpts.IpuntPolicer.PuntPolicerInterfaceNames()
            self.punt_policer_interface_names.parent = self
            self._children_name_map["punt_policer_interface_names"] = "punt-policer-interface-names"
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.IpuntPolicer, ['enable'], name, value)


        class PuntTypeTable(_Entity_):
            """
            Punt Policer Table
            
            .. attribute:: punt_type
            
            	Punt Protocol Type
            	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntTypeTable.PuntType>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.IpuntPolicer.PuntTypeTable, self).__init__()

                self.yang_name = "punt-type-table"
                self.yang_parent_name = "ipunt-policer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("punt-type", ("punt_type", Lpts.IpuntPolicer.PuntTypeTable.PuntType))])
                self._leafs = OrderedDict()

                self.punt_type = YList(self)
                self._segment_path = lambda: "punt-type-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.IpuntPolicer.PuntTypeTable, [], name, value)


            class PuntType(_Entity_):
                """
                Punt Protocol Type
                
                .. attribute:: punt_id  (key)
                
                	Punt Type
                	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                
                .. attribute:: rate
                
                	Enable or Disable Punt Police and corresponding Rate in PPS
                	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.IpuntPolicer.PuntTypeTable.PuntType, self).__init__()

                    self.yang_name = "punt-type"
                    self.yang_parent_name = "punt-type-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['punt_id']
                    self._child_classes = OrderedDict([("rate", ("rate", Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate))])
                    self._leafs = OrderedDict([
                        ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                    ])
                    self.punt_id = None

                    self.rate = None
                    self._children_name_map["rate"] = "rate"
                    self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/punt-type-table/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.IpuntPolicer.PuntTypeTable.PuntType, ['punt_id'], name, value)


                class Rate(_Entity_):
                    """
                    Enable or Disable Punt Police and corresponding
                    Rate in PPS
                    
                    .. attribute:: is_enabled
                    
                    	Is Punt Policer enabled
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: rate
                    
                    	Configured rate value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate, self).__init__()

                        self.yang_name = "rate"
                        self.yang_parent_name = "punt-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ])
                        self.is_enabled = None
                        self.rate = None
                        self._segment_path = lambda: "rate"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.IpuntPolicer.PuntTypeTable.PuntType.Rate']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.IpuntPolicer.PuntTypeTable.PuntType']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.IpuntPolicer.PuntTypeTable']['meta_info']


        class PuntPolicerDomains(_Entity_):
            """
            Punt Policer Domain Table
            
            .. attribute:: punt_policer_domain
            
            	Domain name
            	**type**\: list of  		 :py:class:`PuntPolicerDomain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.IpuntPolicer.PuntPolicerDomains, self).__init__()

                self.yang_name = "punt-policer-domains"
                self.yang_parent_name = "ipunt-policer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("punt-policer-domain", ("punt_policer_domain", Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain))])
                self._leafs = OrderedDict()

                self.punt_policer_domain = YList(self)
                self._segment_path = lambda: "punt-policer-domains"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerDomains, [], name, value)


            class PuntPolicerDomain(_Entity_):
                """
                Domain name
                
                .. attribute:: domain_name  (key)
                
                	Domain name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: punt_type_domain_table
                
                	Punt Policer Table
                	**type**\:  :py:class:`PuntTypeDomainTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain, self).__init__()

                    self.yang_name = "punt-policer-domain"
                    self.yang_parent_name = "punt-policer-domains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain_name']
                    self._child_classes = OrderedDict([("punt-type-domain-table", ("punt_type_domain_table", Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable))])
                    self._leafs = OrderedDict([
                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                    ])
                    self.domain_name = None

                    self.punt_type_domain_table = Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable()
                    self.punt_type_domain_table.parent = self
                    self._children_name_map["punt_type_domain_table"] = "punt-type-domain-table"
                    self._segment_path = lambda: "punt-policer-domain" + "[domain-name='" + str(self.domain_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/punt-policer-domains/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain, ['domain_name'], name, value)


                class PuntTypeDomainTable(_Entity_):
                    """
                    Punt Policer Table
                    
                    .. attribute:: punt_type
                    
                    	Punt Protocol Type
                    	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, self).__init__()

                        self.yang_name = "punt-type-domain-table"
                        self.yang_parent_name = "punt-policer-domain"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-type", ("punt_type", Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType))])
                        self._leafs = OrderedDict()

                        self.punt_type = YList(self)
                        self._segment_path = lambda: "punt-type-domain-table"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable, [], name, value)


                    class PuntType(_Entity_):
                        """
                        Punt Protocol Type
                        
                        .. attribute:: punt_id  (key)
                        
                        	Punt Type
                        	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                        
                        .. attribute:: rate
                        
                        	Enable or Disable Punt Police and corresponding Rate in PPS
                        	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, self).__init__()

                            self.yang_name = "punt-type"
                            self.yang_parent_name = "punt-type-domain-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_id']
                            self._child_classes = OrderedDict([("rate", ("rate", Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate))])
                            self._leafs = OrderedDict([
                                ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                            ])
                            self.punt_id = None

                            self.rate = None
                            self._children_name_map["rate"] = "rate"
                            self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType, ['punt_id'], name, value)


                        class Rate(_Entity_):
                            """
                            Enable or Disable Punt Police and corresponding
                            Rate in PPS
                            
                            .. attribute:: is_enabled
                            
                            	Is Punt Policer enabled
                            	**type**\: bool
                            
                            	**mandatory**\: True
                            
                            .. attribute:: rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, self).__init__()

                                self.yang_name = "rate"
                                self.yang_parent_name = "punt-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                    ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ])
                                self.is_enabled = None
                                self.rate = None
                                self._segment_path = lambda: "rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                                return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType.Rate']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable.PuntType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain.PuntTypeDomainTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerDomains.PuntPolicerDomain']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerDomains']['meta_info']


        class PuntPolicerInterfaceNames(_Entity_):
            """
            Punt Policer Interface
            
            .. attribute:: punt_policer_interface_name
            
            	Pre\-ifib Punt Policer Interface Configuration
            	**type**\: list of  		 :py:class:`PuntPolicerInterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName>`
            
            

            """

            _prefix = 'lpts-pre-ifib-cfg'
            _revision = '2019-10-23'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.IpuntPolicer.PuntPolicerInterfaceNames, self).__init__()

                self.yang_name = "punt-policer-interface-names"
                self.yang_parent_name = "ipunt-policer"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("punt-policer-interface-name", ("punt_policer_interface_name", Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName))])
                self._leafs = OrderedDict()

                self.punt_policer_interface_name = YList(self)
                self._segment_path = lambda: "punt-policer-interface-names"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerInterfaceNames, [], name, value)


            class PuntPolicerInterfaceName(_Entity_):
                """
                Pre\-ifib Punt Policer Interface Configuration
                
                .. attribute:: punt_interface_name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: punt_type_interface_table
                
                	Punt Policer Table
                	**type**\:  :py:class:`PuntTypeInterfaceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable>`
                
                

                """

                _prefix = 'lpts-pre-ifib-cfg'
                _revision = '2019-10-23'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, self).__init__()

                    self.yang_name = "punt-policer-interface-name"
                    self.yang_parent_name = "punt-policer-interface-names"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['punt_interface_name']
                    self._child_classes = OrderedDict([("punt-type-interface-table", ("punt_type_interface_table", Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable))])
                    self._leafs = OrderedDict([
                        ('punt_interface_name', (YLeaf(YType.str, 'punt-interface-name'), ['str'])),
                    ])
                    self.punt_interface_name = None

                    self.punt_type_interface_table = Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable()
                    self.punt_type_interface_table.parent = self
                    self._children_name_map["punt_type_interface_table"] = "punt-type-interface-table"
                    self._segment_path = lambda: "punt-policer-interface-name" + "[punt-interface-name='" + str(self.punt_interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-pre-ifib-cfg:ipunt-policer/punt-policer-interface-names/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName, ['punt_interface_name'], name, value)


                class PuntTypeInterfaceTable(_Entity_):
                    """
                    Punt Policer Table
                    
                    .. attribute:: punt_type
                    
                    	Punt Protocol Type
                    	**type**\: list of  		 :py:class:`PuntType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-cfg'
                    _revision = '2019-10-23'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, self).__init__()

                        self.yang_name = "punt-type-interface-table"
                        self.yang_parent_name = "punt-policer-interface-name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("punt-type", ("punt_type", Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType))])
                        self._leafs = OrderedDict()

                        self.punt_type = YList(self)
                        self._segment_path = lambda: "punt-type-interface-table"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable, [], name, value)


                    class PuntType(_Entity_):
                        """
                        Punt Protocol Type
                        
                        .. attribute:: punt_id  (key)
                        
                        	Punt Type
                        	**type**\:  :py:class:`LptsPunt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg.LptsPunt>`
                        
                        .. attribute:: rate
                        
                        	Enable or Disable Punt Police and corresponding Rate in PPS
                        	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate>`
                        
                        	**presence node**\: True
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-cfg'
                        _revision = '2019-10-23'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, self).__init__()

                            self.yang_name = "punt-type"
                            self.yang_parent_name = "punt-type-interface-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['punt_id']
                            self._child_classes = OrderedDict([("rate", ("rate", Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate))])
                            self._leafs = OrderedDict([
                                ('punt_id', (YLeaf(YType.enumeration, 'punt-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPunt', '')])),
                            ])
                            self.punt_id = None

                            self.rate = None
                            self._children_name_map["rate"] = "rate"
                            self._segment_path = lambda: "punt-type" + "[punt-id='" + str(self.punt_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType, ['punt_id'], name, value)


                        class Rate(_Entity_):
                            """
                            Enable or Disable Punt Police and corresponding
                            Rate in PPS
                            
                            .. attribute:: is_enabled
                            
                            	Is Punt Policer enabled
                            	**type**\: bool
                            
                            	**mandatory**\: True
                            
                            .. attribute:: rate
                            
                            	Configured rate value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'lpts-pre-ifib-cfg'
                            _revision = '2019-10-23'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, self).__init__()

                                self.yang_name = "rate"
                                self.yang_parent_name = "punt-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                                    ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ])
                                self.is_enabled = None
                                self.rate = None
                                self._segment_path = lambda: "rate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate, ['is_enabled', 'rate'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                                return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType.Rate']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable.PuntType']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName.PuntTypeInterfaceTable']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames.PuntPolicerInterfaceName']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.IpuntPolicer.PuntPolicerInterfaceNames']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.IpuntPolicer']['meta_info']


    class Punt(_Entity_):
        """
        Configure penalty timeout value
        
        .. attribute:: flowtrap
        
        	excessive punt flow trap configuration commands
        	**type**\:  :py:class:`Flowtrap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap>`
        
        

        """

        _prefix = 'lpts-punt-flowtrap-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Lpts.Punt, self).__init__()

            self.yang_name = "punt"
            self.yang_parent_name = "lpts"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("flowtrap", ("flowtrap", Lpts.Punt.Flowtrap))])
            self._leafs = OrderedDict()

            self.flowtrap = Lpts.Punt.Flowtrap()
            self.flowtrap.parent = self
            self._children_name_map["flowtrap"] = "flowtrap"
            self._segment_path = lambda: "Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lpts.Punt, [], name, value)


        class Flowtrap(_Entity_):
            """
            excessive punt flow trap configuration commands
            
            .. attribute:: penalty_rates
            
            	Configure penalty policing rate
            	**type**\:  :py:class:`PenaltyRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates>`
            
            .. attribute:: penalty_timeouts
            
            	Configure penalty timeout value
            	**type**\:  :py:class:`PenaltyTimeouts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts>`
            
            .. attribute:: exclude
            
            	Exclude an item from all traps
            	**type**\:  :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude>`
            
            .. attribute:: max_flow_gap
            
            	Maximum flow gap in milliseconds
            	**type**\: int
            
            	**range:** 1..60000
            
            .. attribute:: et_size
            
            	Should be power of 2. Any one of 1,2,4,8,16,32 ,64,128
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: eviction_threshold
            
            	Eviction threshold, should be less than report\-threshold
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: report_threshold
            
            	Threshold to cross for a flow to be considered as bad actor flow
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: non_subscriber_interfaces
            
            	Enable trap based on source mac on non\-subscriber interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sample_prob
            
            	Probability of packets to be sampled
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: eviction_search_limit
            
            	Eviction search limit, should be less than trap\-size
            	**type**\: int
            
            	**range:** 1..128
            
            .. attribute:: routing_protocols_enable
            
            	Allow routing protocols to pass through copp sampler
            	**type**\: bool
            
            .. attribute:: subscriber_interfaces
            
            	Enable the trap on subscriber interfaces
            	**type**\: bool
            
            .. attribute:: interface_based_flow
            
            	Identify flow based on interface and flowtype
            	**type**\: bool
            
            .. attribute:: dampening
            
            	Dampening period for a bad actor flow in milliseconds
            	**type**\: int
            
            	**range:** 5000..60000
            
            

            """

            _prefix = 'lpts-punt-flowtrap-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Lpts.Punt.Flowtrap, self).__init__()

                self.yang_name = "flowtrap"
                self.yang_parent_name = "punt"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("penalty-rates", ("penalty_rates", Lpts.Punt.Flowtrap.PenaltyRates)), ("penalty-timeouts", ("penalty_timeouts", Lpts.Punt.Flowtrap.PenaltyTimeouts)), ("exclude", ("exclude", Lpts.Punt.Flowtrap.Exclude))])
                self._leafs = OrderedDict([
                    ('max_flow_gap', (YLeaf(YType.uint32, 'max-flow-gap'), ['int'])),
                    ('et_size', (YLeaf(YType.uint32, 'et-size'), ['int'])),
                    ('eviction_threshold', (YLeaf(YType.uint32, 'eviction-threshold'), ['int'])),
                    ('report_threshold', (YLeaf(YType.uint16, 'report-threshold'), ['int'])),
                    ('non_subscriber_interfaces', (YLeaf(YType.uint32, 'non-subscriber-interfaces'), ['int'])),
                    ('sample_prob', (YLeaf(YType.str, 'sample-prob'), ['str'])),
                    ('eviction_search_limit', (YLeaf(YType.uint32, 'eviction-search-limit'), ['int'])),
                    ('routing_protocols_enable', (YLeaf(YType.boolean, 'routing-protocols-enable'), ['bool'])),
                    ('subscriber_interfaces', (YLeaf(YType.boolean, 'subscriber-interfaces'), ['bool'])),
                    ('interface_based_flow', (YLeaf(YType.boolean, 'interface-based-flow'), ['bool'])),
                    ('dampening', (YLeaf(YType.uint32, 'dampening'), ['int'])),
                ])
                self.max_flow_gap = None
                self.et_size = None
                self.eviction_threshold = None
                self.report_threshold = None
                self.non_subscriber_interfaces = None
                self.sample_prob = None
                self.eviction_search_limit = None
                self.routing_protocols_enable = None
                self.subscriber_interfaces = None
                self.interface_based_flow = None
                self.dampening = None

                self.penalty_rates = Lpts.Punt.Flowtrap.PenaltyRates()
                self.penalty_rates.parent = self
                self._children_name_map["penalty_rates"] = "penalty-rates"

                self.penalty_timeouts = Lpts.Punt.Flowtrap.PenaltyTimeouts()
                self.penalty_timeouts.parent = self
                self._children_name_map["penalty_timeouts"] = "penalty-timeouts"

                self.exclude = Lpts.Punt.Flowtrap.Exclude()
                self.exclude.parent = self
                self._children_name_map["exclude"] = "exclude"
                self._segment_path = lambda: "flowtrap"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lpts.Punt.Flowtrap, ['max_flow_gap', 'et_size', 'eviction_threshold', 'report_threshold', 'non_subscriber_interfaces', 'sample_prob', 'eviction_search_limit', 'routing_protocols_enable', 'subscriber_interfaces', 'interface_based_flow', 'dampening'], name, value)


            class PenaltyRates(_Entity_):
                """
                Configure penalty policing rate
                
                .. attribute:: penalty_rate
                
                	none
                	**type**\: list of  		 :py:class:`PenaltyRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Punt.Flowtrap.PenaltyRates, self).__init__()

                    self.yang_name = "penalty-rates"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("penalty-rate", ("penalty_rate", Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate))])
                    self._leafs = OrderedDict()

                    self.penalty_rate = YList(self)
                    self._segment_path = lambda: "penalty-rates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyRates, [], name, value)


                class PenaltyRate(_Entity_):
                    """
                    none
                    
                    .. attribute:: protocol_name  (key)
                    
                    	none
                    	**type**\:  :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: rate
                    
                    	Penalty policer rate in packets\-per\-second
                    	**type**\: int
                    
                    	**range:** 2..100
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, self).__init__()

                        self.yang_name = "penalty-rate"
                        self.yang_parent_name = "penalty-rates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['protocol_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId', '')])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                        ])
                        self.protocol_name = None
                        self.rate = None
                        self._segment_path = lambda: "penalty-rate" + "[protocol-name='" + str(self.protocol_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-rates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate, ['protocol_name', 'rate'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyRates.PenaltyRate']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyRates']['meta_info']


            class PenaltyTimeouts(_Entity_):
                """
                Configure penalty timeout value
                
                .. attribute:: penalty_timeout
                
                	none
                	**type**\: list of  		 :py:class:`PenaltyTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Punt.Flowtrap.PenaltyTimeouts, self).__init__()

                    self.yang_name = "penalty-timeouts"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("penalty-timeout", ("penalty_timeout", Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout))])
                    self._leafs = OrderedDict()

                    self.penalty_timeout = YList(self)
                    self._segment_path = lambda: "penalty-timeouts"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyTimeouts, [], name, value)


                class PenaltyTimeout(_Entity_):
                    """
                    none
                    
                    .. attribute:: protocol_name  (key)
                    
                    	none
                    	**type**\:  :py:class:`LptsPuntFlowtrapProtoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg.LptsPuntFlowtrapProtoId>`
                    
                    .. attribute:: timeout
                    
                    	Timeout value in minutes
                    	**type**\: int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, self).__init__()

                        self.yang_name = "penalty-timeout"
                        self.yang_parent_name = "penalty-timeouts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['protocol_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_punt_flowtrap_cfg', 'LptsPuntFlowtrapProtoId', '')])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ])
                        self.protocol_name = None
                        self.timeout = None
                        self._segment_path = lambda: "penalty-timeout" + "[protocol-name='" + str(self.protocol_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/penalty-timeouts/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout, ['protocol_name', 'timeout'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts.PenaltyTimeout']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.PenaltyTimeouts']['meta_info']


            class Exclude(_Entity_):
                """
                Exclude an item from all traps
                
                .. attribute:: interface_names
                
                	none
                	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames>`
                
                

                """

                _prefix = 'lpts-punt-flowtrap-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Lpts.Punt.Flowtrap.Exclude, self).__init__()

                    self.yang_name = "exclude"
                    self.yang_parent_name = "flowtrap"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-names", ("interface_names", Lpts.Punt.Flowtrap.Exclude.InterfaceNames))])
                    self._leafs = OrderedDict()

                    self.interface_names = Lpts.Punt.Flowtrap.Exclude.InterfaceNames()
                    self.interface_names.parent = self
                    self._children_name_map["interface_names"] = "interface-names"
                    self._segment_path = lambda: "exclude"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lpts.Punt.Flowtrap.Exclude, [], name, value)


                class InterfaceNames(_Entity_):
                    """
                    none
                    
                    .. attribute:: interface_name
                    
                    	Name of interface to exclude from all traps
                    	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg.Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName>`
                    
                    

                    """

                    _prefix = 'lpts-punt-flowtrap-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, self).__init__()

                        self.yang_name = "interface-names"
                        self.yang_parent_name = "exclude"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-name", ("interface_name", Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName))])
                        self._leafs = OrderedDict()

                        self.interface_name = YList(self)
                        self._segment_path = lambda: "interface-names"
                        self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lpts.Punt.Flowtrap.Exclude.InterfaceNames, [], name, value)


                    class InterfaceName(_Entity_):
                        """
                        Name of interface to exclude from all traps
                        
                        .. attribute:: ifname  (key)
                        
                        	Name of interface to exclude from all traps
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: id1
                        
                        	Enabled or disabled
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'lpts-punt-flowtrap-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, self).__init__()

                            self.yang_name = "interface-name"
                            self.yang_parent_name = "interface-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['ifname']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ifname', (YLeaf(YType.str, 'ifname'), ['str'])),
                                ('id1', (YLeaf(YType.boolean, 'id1'), ['bool'])),
                            ])
                            self.ifname = None
                            self.id1 = None
                            self._segment_path = lambda: "interface-name" + "[ifname='" + str(self.ifname) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-lib-cfg:lpts/Cisco-IOS-XR-lpts-punt-flowtrap-cfg:punt/flowtrap/exclude/interface-names/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName, ['ifname', 'id1'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                            return meta._meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames.InterfaceName']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                        return meta._meta_table['Lpts.Punt.Flowtrap.Exclude.InterfaceNames']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                    return meta._meta_table['Lpts.Punt.Flowtrap.Exclude']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
                return meta._meta_table['Lpts.Punt.Flowtrap']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
            return meta._meta_table['Lpts.Punt']['meta_info']

    def clone_ptr(self):
        self._top_entity = Lpts()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_lib_cfg as meta
        return meta._meta_table['Lpts']['meta_info']


