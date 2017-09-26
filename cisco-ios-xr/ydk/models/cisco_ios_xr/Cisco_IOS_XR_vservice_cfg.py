""" Cisco_IOS_XR_vservice_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR vservice package configuration.

This module contains definitions
for the following management objects\:
  vservice\: configure vservice node

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SfcMetadataAlloc(Enum):
    """
    SfcMetadataAlloc

    Sfc metadata alloc

    .. data:: type1 = 1

    	type 1 allocation

    """

    type1 = Enum.YLeaf(1, "type1")


class SfcMetadataDispositionAction(Enum):
    """
    SfcMetadataDispositionAction

    Sfc metadata disposition action

    .. data:: redirect_nexthop = 1

    	redirect nexthop action

    """

    redirect_nexthop = Enum.YLeaf(1, "redirect-nexthop")


class SfcMetadataDispositionMatch(Enum):
    """
    SfcMetadataDispositionMatch

    Sfc metadata disposition match

    .. data:: type1_dcalloc_tenant_id = 1

    	match type 1

    """

    type1_dcalloc_tenant_id = Enum.YLeaf(1, "type1-dcalloc-tenant-id")


class SfcMetadataType1AllocFormat(Enum):
    """
    SfcMetadataType1AllocFormat

    Sfc metadata type1 alloc format

    .. data:: dc_allocation = 1

    	data center allocation

    """

    dc_allocation = Enum.YLeaf(1, "dc-allocation")


class SfcSfTransport(Enum):
    """
    SfcSfTransport

    Sfc sf transport

    .. data:: vxlan_gpe = 1

    	vxlan-gpe transport type

    """

    vxlan_gpe = Enum.YLeaf(1, "vxlan-gpe")



class Vservice(Entity):
    """
    configure vservice node
    
    .. attribute:: metadata_dispositions
    
    	Configure metadata disposition
    	**type**\:   :py:class:`MetadataDispositions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions>`
    
    .. attribute:: metadata_templates
    
    	configure metadata imposition
    	**type**\:   :py:class:`MetadataTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataTemplates>`
    
    .. attribute:: service_function_forward_locator
    
    	configure service function forward locator
    	**type**\:   :py:class:`ServiceFunctionForwardLocator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator>`
    
    .. attribute:: service_function_locator
    
    	configure service function locator
    	**type**\:   :py:class:`ServiceFunctionLocator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator>`
    
    .. attribute:: service_function_path
    
    	service function path
    	**type**\:   :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath>`
    
    

    """

    _prefix = 'vservice-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vservice, self).__init__()
        self._top_entity = None

        self.yang_name = "vservice"
        self.yang_parent_name = "Cisco-IOS-XR-vservice-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"metadata-dispositions" : ("metadata_dispositions", Vservice.MetadataDispositions), "metadata-templates" : ("metadata_templates", Vservice.MetadataTemplates), "service-function-forward-locator" : ("service_function_forward_locator", Vservice.ServiceFunctionForwardLocator), "service-function-locator" : ("service_function_locator", Vservice.ServiceFunctionLocator), "service-function-path" : ("service_function_path", Vservice.ServiceFunctionPath)}
        self._child_list_classes = {}

        self.metadata_dispositions = Vservice.MetadataDispositions()
        self.metadata_dispositions.parent = self
        self._children_name_map["metadata_dispositions"] = "metadata-dispositions"
        self._children_yang_names.add("metadata-dispositions")

        self.metadata_templates = Vservice.MetadataTemplates()
        self.metadata_templates.parent = self
        self._children_name_map["metadata_templates"] = "metadata-templates"
        self._children_yang_names.add("metadata-templates")

        self.service_function_forward_locator = Vservice.ServiceFunctionForwardLocator()
        self.service_function_forward_locator.parent = self
        self._children_name_map["service_function_forward_locator"] = "service-function-forward-locator"
        self._children_yang_names.add("service-function-forward-locator")

        self.service_function_locator = Vservice.ServiceFunctionLocator()
        self.service_function_locator.parent = self
        self._children_name_map["service_function_locator"] = "service-function-locator"
        self._children_yang_names.add("service-function-locator")

        self.service_function_path = Vservice.ServiceFunctionPath()
        self.service_function_path.parent = self
        self._children_name_map["service_function_path"] = "service-function-path"
        self._children_yang_names.add("service-function-path")
        self._segment_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice"


    class MetadataDispositions(Entity):
        """
        Configure metadata disposition
        
        .. attribute:: metadata_disposition
        
        	metadata disposition name
        	**type**\: list of    :py:class:`MetadataDisposition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vservice.MetadataDispositions, self).__init__()

            self.yang_name = "metadata-dispositions"
            self.yang_parent_name = "vservice"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"metadata-disposition" : ("metadata_disposition", Vservice.MetadataDispositions.MetadataDisposition)}

            self.metadata_disposition = YList(self)
            self._segment_path = lambda: "metadata-dispositions"
            self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vservice.MetadataDispositions, [], name, value)


        class MetadataDisposition(Entity):
            """
            metadata disposition name
            
            .. attribute:: disposition_name  <key>
            
            	disposition name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: format  <key>
            
            	Specify Format
            	**type**\:   :py:class:`SfcMetadataType1AllocFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataType1AllocFormat>`
            
            .. attribute:: match_entry
            
            	match entry name
            	**type**\: list of    :py:class:`MatchEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition.MatchEntry>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vservice.MetadataDispositions.MetadataDisposition, self).__init__()

                self.yang_name = "metadata-disposition"
                self.yang_parent_name = "metadata-dispositions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"match-entry" : ("match_entry", Vservice.MetadataDispositions.MetadataDisposition.MatchEntry)}

                self.disposition_name = YLeaf(YType.str, "disposition-name")

                self.format = YLeaf(YType.enumeration, "format")

                self.match_entry = YList(self)
                self._segment_path = lambda: "metadata-disposition" + "[disposition-name='" + self.disposition_name.get() + "']" + "[format='" + self.format.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/metadata-dispositions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vservice.MetadataDispositions.MetadataDisposition, ['disposition_name', 'format'], name, value)


            class MatchEntry(Entity):
                """
                match entry name
                
                .. attribute:: match_entry_name  <key>
                
                	match entry name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: node
                
                	configure disposition data
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry, self).__init__()

                    self.yang_name = "match-entry"
                    self.yang_parent_name = "metadata-disposition"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"node" : ("node", Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node)}
                    self._child_list_classes = {}

                    self.match_entry_name = YLeaf(YType.str, "match-entry-name")

                    self.node = Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")
                    self._segment_path = lambda: "match-entry" + "[match-entry-name='" + self.match_entry_name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry, ['match_entry_name'], name, value)


                class Node(Entity):
                    """
                    configure disposition data
                    
                    .. attribute:: action_type
                    
                    	action type
                    	**type**\:   :py:class:`SfcMetadataDispositionAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionAction>`
                    
                    .. attribute:: match_type
                    
                    	match type
                    	**type**\:   :py:class:`SfcMetadataDispositionMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionMatch>`
                    
                    .. attribute:: nexthop_ipv4_address
                    
                    	IPv4 nexthop address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tenant_id
                    
                    	24\-bit tenant id
                    	**type**\:  list of int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vrf
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "match-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.action_type = YLeaf(YType.enumeration, "action-type")

                        self.match_type = YLeaf(YType.enumeration, "match-type")

                        self.nexthop_ipv4_address = YLeaf(YType.str, "nexthop-ipv4-address")

                        self.tenant_id = YLeafList(YType.int32, "tenant-id")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "node"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node, ['action_type', 'match_type', 'nexthop_ipv4_address', 'tenant_id', 'vrf'], name, value)


    class MetadataTemplates(Entity):
        """
        configure metadata imposition
        
        .. attribute:: metadata_template
        
        	metadata name, type and format
        	**type**\: list of    :py:class:`MetadataTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataTemplates.MetadataTemplate>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vservice.MetadataTemplates, self).__init__()

            self.yang_name = "metadata-templates"
            self.yang_parent_name = "vservice"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"metadata-template" : ("metadata_template", Vservice.MetadataTemplates.MetadataTemplate)}

            self.metadata_template = YList(self)
            self._segment_path = lambda: "metadata-templates"
            self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vservice.MetadataTemplates, [], name, value)


        class MetadataTemplate(Entity):
            """
            metadata name, type and format
            
            .. attribute:: metadata_name  <key>
            
            	metadata name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: type  <key>
            
            	Specify Type 
            	**type**\:   :py:class:`SfcMetadataAlloc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataAlloc>`
            
            .. attribute:: format  <key>
            
            	Specify Format
            	**type**\:   :py:class:`SfcMetadataType1AllocFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataType1AllocFormat>`
            
            .. attribute:: tenant_id
            
            	Enter 24\-bit tenant id
            	**type**\:  int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vservice.MetadataTemplates.MetadataTemplate, self).__init__()

                self.yang_name = "metadata-template"
                self.yang_parent_name = "metadata-templates"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.metadata_name = YLeaf(YType.str, "metadata-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.format = YLeaf(YType.enumeration, "format")

                self.tenant_id = YLeaf(YType.uint32, "tenant-id")
                self._segment_path = lambda: "metadata-template" + "[metadata-name='" + self.metadata_name.get() + "']" + "[type='" + self.type.get() + "']" + "[format='" + self.format.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/metadata-templates/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vservice.MetadataTemplates.MetadataTemplate, ['metadata_name', 'type', 'format', 'tenant_id'], name, value)


    class ServiceFunctionForwardLocator(Entity):
        """
        configure service function forward locator
        
        .. attribute:: names
        
        	Mention the sf/sff name
        	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vservice.ServiceFunctionForwardLocator, self).__init__()

            self.yang_name = "service-function-forward-locator"
            self.yang_parent_name = "vservice"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"names" : ("names", Vservice.ServiceFunctionForwardLocator.Names)}
            self._child_list_classes = {}

            self.names = Vservice.ServiceFunctionForwardLocator.Names()
            self.names.parent = self
            self._children_name_map["names"] = "names"
            self._children_yang_names.add("names")
            self._segment_path = lambda: "service-function-forward-locator"
            self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self._segment_path()


        class Names(Entity):
            """
            Mention the sf/sff name
            
            .. attribute:: name
            
            	service function name
            	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names.Name>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vservice.ServiceFunctionForwardLocator.Names, self).__init__()

                self.yang_name = "names"
                self.yang_parent_name = "service-function-forward-locator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"name" : ("name", Vservice.ServiceFunctionForwardLocator.Names.Name)}

                self.name = YList(self)
                self._segment_path = lambda: "names"
                self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-forward-locator/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vservice.ServiceFunctionForwardLocator.Names, [], name, value)


            class Name(Entity):
                """
                service function name
                
                .. attribute:: function_name  <key>
                
                	Service function/forwarder name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: locator_id  <key>
                
                	Specify locator id
                	**type**\:  int
                
                	**range:** 1..255
                
                .. attribute:: node
                
                	configure sff/sffl
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names.Name.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vservice.ServiceFunctionForwardLocator.Names.Name, self).__init__()

                    self.yang_name = "name"
                    self.yang_parent_name = "names"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"node" : ("node", Vservice.ServiceFunctionForwardLocator.Names.Name.Node)}
                    self._child_list_classes = {}

                    self.function_name = YLeaf(YType.str, "function-name")

                    self.locator_id = YLeaf(YType.uint32, "locator-id")

                    self.node = Vservice.ServiceFunctionForwardLocator.Names.Name.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")
                    self._segment_path = lambda: "name" + "[function-name='" + self.function_name.get() + "']" + "[locator-id='" + self.locator_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-forward-locator/names/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Vservice.ServiceFunctionForwardLocator.Names.Name, ['function_name', 'locator_id'], name, value)


                class Node(Entity):
                    """
                    configure sff/sffl
                    
                    .. attribute:: ipv4_destination_address
                    
                    	IPv4 destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_source_address
                    
                    	IPv4 source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport
                    
                    	Transport type
                    	**type**\:   :py:class:`SfcSfTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcSfTransport>`
                    
                    .. attribute:: vni
                    
                    	VNI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vservice.ServiceFunctionForwardLocator.Names.Name.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipv4_destination_address = YLeaf(YType.str, "ipv4-destination-address")

                        self.ipv4_source_address = YLeaf(YType.str, "ipv4-source-address")

                        self.transport = YLeaf(YType.enumeration, "transport")

                        self.vni = YLeaf(YType.int32, "vni")
                        self._segment_path = lambda: "node"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vservice.ServiceFunctionForwardLocator.Names.Name.Node, ['ipv4_destination_address', 'ipv4_source_address', 'transport', 'vni'], name, value)


    class ServiceFunctionLocator(Entity):
        """
        configure service function locator
        
        .. attribute:: names
        
        	Mention the sf/sff name
        	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vservice.ServiceFunctionLocator, self).__init__()

            self.yang_name = "service-function-locator"
            self.yang_parent_name = "vservice"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"names" : ("names", Vservice.ServiceFunctionLocator.Names)}
            self._child_list_classes = {}

            self.names = Vservice.ServiceFunctionLocator.Names()
            self.names.parent = self
            self._children_name_map["names"] = "names"
            self._children_yang_names.add("names")
            self._segment_path = lambda: "service-function-locator"
            self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self._segment_path()


        class Names(Entity):
            """
            Mention the sf/sff name
            
            .. attribute:: name
            
            	service function name
            	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names.Name>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vservice.ServiceFunctionLocator.Names, self).__init__()

                self.yang_name = "names"
                self.yang_parent_name = "service-function-locator"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"name" : ("name", Vservice.ServiceFunctionLocator.Names.Name)}

                self.name = YList(self)
                self._segment_path = lambda: "names"
                self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-locator/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vservice.ServiceFunctionLocator.Names, [], name, value)


            class Name(Entity):
                """
                service function name
                
                .. attribute:: function_name  <key>
                
                	Service function/forwarder name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: locator_id  <key>
                
                	Specify locator id
                	**type**\:  int
                
                	**range:** 1..255
                
                .. attribute:: node
                
                	configure sff/sffl
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names.Name.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vservice.ServiceFunctionLocator.Names.Name, self).__init__()

                    self.yang_name = "name"
                    self.yang_parent_name = "names"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"node" : ("node", Vservice.ServiceFunctionLocator.Names.Name.Node)}
                    self._child_list_classes = {}

                    self.function_name = YLeaf(YType.str, "function-name")

                    self.locator_id = YLeaf(YType.uint32, "locator-id")

                    self.node = Vservice.ServiceFunctionLocator.Names.Name.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")
                    self._segment_path = lambda: "name" + "[function-name='" + self.function_name.get() + "']" + "[locator-id='" + self.locator_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-locator/names/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Vservice.ServiceFunctionLocator.Names.Name, ['function_name', 'locator_id'], name, value)


                class Node(Entity):
                    """
                    configure sff/sffl
                    
                    .. attribute:: ipv4_destination_address
                    
                    	IPv4 destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_source_address
                    
                    	IPv4 source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport
                    
                    	Transport type
                    	**type**\:   :py:class:`SfcSfTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcSfTransport>`
                    
                    .. attribute:: vni
                    
                    	VNI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vservice.ServiceFunctionLocator.Names.Name.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipv4_destination_address = YLeaf(YType.str, "ipv4-destination-address")

                        self.ipv4_source_address = YLeaf(YType.str, "ipv4-source-address")

                        self.transport = YLeaf(YType.enumeration, "transport")

                        self.vni = YLeaf(YType.int32, "vni")
                        self._segment_path = lambda: "node"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vservice.ServiceFunctionLocator.Names.Name.Node, ['ipv4_destination_address', 'ipv4_source_address', 'transport', 'vni'], name, value)


    class ServiceFunctionPath(Entity):
        """
        service function path
        
        .. attribute:: paths
        
        	service function path id
        	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vservice.ServiceFunctionPath, self).__init__()

            self.yang_name = "service-function-path"
            self.yang_parent_name = "vservice"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"paths" : ("paths", Vservice.ServiceFunctionPath.Paths)}
            self._child_list_classes = {}

            self.paths = Vservice.ServiceFunctionPath.Paths()
            self.paths.parent = self
            self._children_name_map["paths"] = "paths"
            self._children_yang_names.add("paths")
            self._segment_path = lambda: "service-function-path"
            self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self._segment_path()


        class Paths(Entity):
            """
            service function path id
            
            .. attribute:: path
            
            	specify the service function path id
            	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vservice.ServiceFunctionPath.Paths, self).__init__()

                self.yang_name = "paths"
                self.yang_parent_name = "service-function-path"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"path" : ("path", Vservice.ServiceFunctionPath.Paths.Path)}

                self.path = YList(self)
                self._segment_path = lambda: "paths"
                self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-path/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vservice.ServiceFunctionPath.Paths, [], name, value)


            class Path(Entity):
                """
                specify the service function path id
                
                .. attribute:: path_id  <key>
                
                	Specify the service function path id
                	**type**\:  int
                
                	**range:** 1..16777215
                
                .. attribute:: service_index
                
                	specify the service index
                	**type**\: list of    :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vservice.ServiceFunctionPath.Paths.Path, self).__init__()

                    self.yang_name = "path"
                    self.yang_parent_name = "paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"service-index" : ("service_index", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex)}

                    self.path_id = YLeaf(YType.uint32, "path-id")

                    self.service_index = YList(self)
                    self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-vservice-cfg:vservice/service-function-path/paths/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path, ['path_id'], name, value)


                class ServiceIndex(Entity):
                    """
                    specify the service index
                    
                    .. attribute:: index  <key>
                    
                    	Specify the id of service function
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: sf_names
                    
                    	service function 
                    	**type**\:   :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames>`
                    
                    .. attribute:: sff_names
                    
                    	service function forwarder 
                    	**type**\:   :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames>`
                    
                    .. attribute:: terminate
                    
                    	configure terminate
                    	**type**\:   :py:class:`Terminate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate>`
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex, self).__init__()

                        self.yang_name = "service-index"
                        self.yang_parent_name = "path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sf-names" : ("sf_names", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames), "sff-names" : ("sff_names", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames), "terminate" : ("terminate", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate)}
                        self._child_list_classes = {}

                        self.index = YLeaf(YType.uint32, "index")

                        self.sf_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames()
                        self.sf_names.parent = self
                        self._children_name_map["sf_names"] = "sf-names"
                        self._children_yang_names.add("sf-names")

                        self.sff_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames()
                        self.sff_names.parent = self
                        self._children_name_map["sff_names"] = "sff-names"
                        self._children_yang_names.add("sff-names")

                        self.terminate = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate()
                        self.terminate.parent = self
                        self._children_name_map["terminate"] = "terminate"
                        self._children_yang_names.add("terminate")
                        self._segment_path = lambda: "service-index" + "[index='" + self.index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex, ['index'], name, value)


                    class SfNames(Entity):
                        """
                        service function 
                        
                        .. attribute:: sf_name
                        
                        	service function name
                        	**type**\: list of    :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames, self).__init__()

                            self.yang_name = "sf-names"
                            self.yang_parent_name = "service-index"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sf-name" : ("sf_name", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName)}

                            self.sf_name = YList(self)
                            self._segment_path = lambda: "sf-names"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames, [], name, value)


                        class SfName(Entity):
                            """
                            service function name
                            
                            .. attribute:: name  <key>
                            
                            	SF Name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: node
                            
                            	configure SFP
                            	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node>`
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName, self).__init__()

                                self.yang_name = "sf-name"
                                self.yang_parent_name = "sf-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"node" : ("node", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node)}
                                self._child_list_classes = {}

                                self.name = YLeaf(YType.str, "name")

                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node()
                                self.node.parent = self
                                self._children_name_map["node"] = "node"
                                self._children_yang_names.add("node")
                                self._segment_path = lambda: "sf-name" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName, ['name'], name, value)


                            class Node(Entity):
                                """
                                configure SFP
                                
                                .. attribute:: enable
                                
                                	Enable Service function path
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: reserved
                                
                                	Dummy
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'vservice-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node, self).__init__()

                                    self.yang_name = "node"
                                    self.yang_parent_name = "sf-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.reserved = YLeaf(YType.empty, "reserved")
                                    self._segment_path = lambda: "node"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node, ['enable', 'reserved'], name, value)


                    class SffNames(Entity):
                        """
                        service function forwarder 
                        
                        .. attribute:: sff_name
                        
                        	service function forwarder name
                        	**type**\: list of    :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames, self).__init__()

                            self.yang_name = "sff-names"
                            self.yang_parent_name = "service-index"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sff-name" : ("sff_name", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName)}

                            self.sff_name = YList(self)
                            self._segment_path = lambda: "sff-names"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames, [], name, value)


                        class SffName(Entity):
                            """
                            service function forwarder name
                            
                            .. attribute:: name  <key>
                            
                            	SFF Name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: node
                            
                            	configure SFP
                            	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node>`
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName, self).__init__()

                                self.yang_name = "sff-name"
                                self.yang_parent_name = "sff-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"node" : ("node", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node)}
                                self._child_list_classes = {}

                                self.name = YLeaf(YType.str, "name")

                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node()
                                self.node.parent = self
                                self._children_name_map["node"] = "node"
                                self._children_yang_names.add("node")
                                self._segment_path = lambda: "sff-name" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName, ['name'], name, value)


                            class Node(Entity):
                                """
                                configure SFP
                                
                                .. attribute:: enable
                                
                                	Enable Service function path
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: reserved
                                
                                	Dummy
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'vservice-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node, self).__init__()

                                    self.yang_name = "node"
                                    self.yang_parent_name = "sff-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.reserved = YLeaf(YType.empty, "reserved")
                                    self._segment_path = lambda: "node"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node, ['enable', 'reserved'], name, value)


                    class Terminate(Entity):
                        """
                        configure terminate
                        
                        .. attribute:: node
                        
                        	configure default terminate action
                        	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate, self).__init__()

                            self.yang_name = "terminate"
                            self.yang_parent_name = "service-index"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"node" : ("node", Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node)}
                            self._child_list_classes = {}

                            self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                            self._children_yang_names.add("node")
                            self._segment_path = lambda: "terminate"


                        class Node(Entity):
                            """
                            configure default terminate action
                            
                            .. attribute:: action
                            
                            	default action enum
                            	**type**\:   :py:class:`SfcMetadataDispositionAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionAction>`
                            
                            .. attribute:: metatdata_disposition
                            
                            	metadata\-disposition name
                            	**type**\:  str
                            
                            .. attribute:: nexthop_ipv4_address
                            
                            	IPv4 nexthop address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf
                            
                            	nexthop vrf name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node, self).__init__()

                                self.yang_name = "node"
                                self.yang_parent_name = "terminate"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.action = YLeaf(YType.enumeration, "action")

                                self.metatdata_disposition = YLeaf(YType.str, "metatdata-disposition")

                                self.nexthop_ipv4_address = YLeaf(YType.str, "nexthop-ipv4-address")

                                self.vrf = YLeaf(YType.str, "vrf")
                                self._segment_path = lambda: "node"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node, ['action', 'metatdata_disposition', 'nexthop_ipv4_address', 'vrf'], name, value)

    def clone_ptr(self):
        self._top_entity = Vservice()
        return self._top_entity

