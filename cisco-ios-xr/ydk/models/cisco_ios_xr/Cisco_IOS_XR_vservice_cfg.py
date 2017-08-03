""" Cisco_IOS_XR_vservice_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR vservice package configuration.

This module contains definitions
for the following management objects\:
  vservice\: configure vservice node

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.names = Vservice.ServiceFunctionLocator.Names()
            self.names.parent = self
            self._children_name_map["names"] = "names"
            self._children_yang_names.add("names")


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

                self.name = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vservice.ServiceFunctionLocator.Names, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vservice.ServiceFunctionLocator.Names, self).__setattr__(name, value)


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

                    self.function_name = YLeaf(YType.str, "function-name")

                    self.locator_id = YLeaf(YType.uint32, "locator-id")

                    self.node = Vservice.ServiceFunctionLocator.Names.Name.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("function_name",
                                    "locator_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vservice.ServiceFunctionLocator.Names.Name, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vservice.ServiceFunctionLocator.Names.Name, self).__setattr__(name, value)


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

                        self.ipv4_destination_address = YLeaf(YType.str, "ipv4-destination-address")

                        self.ipv4_source_address = YLeaf(YType.str, "ipv4-source-address")

                        self.transport = YLeaf(YType.enumeration, "transport")

                        self.vni = YLeaf(YType.int32, "vni")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv4_destination_address",
                                        "ipv4_source_address",
                                        "transport",
                                        "vni") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vservice.ServiceFunctionLocator.Names.Name.Node, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vservice.ServiceFunctionLocator.Names.Name.Node, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipv4_destination_address.is_set or
                            self.ipv4_source_address.is_set or
                            self.transport.is_set or
                            self.vni.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv4_destination_address.yfilter != YFilter.not_set or
                            self.ipv4_source_address.yfilter != YFilter.not_set or
                            self.transport.yfilter != YFilter.not_set or
                            self.vni.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv4_destination_address.is_set or self.ipv4_destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_destination_address.get_name_leafdata())
                        if (self.ipv4_source_address.is_set or self.ipv4_source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_source_address.get_name_leafdata())
                        if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transport.get_name_leafdata())
                        if (self.vni.is_set or self.vni.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vni.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4-destination-address" or name == "ipv4-source-address" or name == "transport" or name == "vni"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv4-destination-address"):
                            self.ipv4_destination_address = value
                            self.ipv4_destination_address.value_namespace = name_space
                            self.ipv4_destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-source-address"):
                            self.ipv4_source_address = value
                            self.ipv4_source_address.value_namespace = name_space
                            self.ipv4_source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "transport"):
                            self.transport = value
                            self.transport.value_namespace = name_space
                            self.transport.value_namespace_prefix = name_space_prefix
                        if(value_path == "vni"):
                            self.vni = value
                            self.vni.value_namespace = name_space
                            self.vni.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.function_name.is_set or
                        self.locator_id.is_set or
                        (self.node is not None and self.node.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.function_name.yfilter != YFilter.not_set or
                        self.locator_id.yfilter != YFilter.not_set or
                        (self.node is not None and self.node.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "name" + "[function-name='" + self.function_name.get() + "']" + "[locator-id='" + self.locator_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-locator/names/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.function_name.is_set or self.function_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.function_name.get_name_leafdata())
                    if (self.locator_id.is_set or self.locator_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.locator_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "node"):
                        if (self.node is None):
                            self.node = Vservice.ServiceFunctionLocator.Names.Name.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                        return self.node

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node" or name == "function-name" or name == "locator-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "function-name"):
                        self.function_name = value
                        self.function_name.value_namespace = name_space
                        self.function_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "locator-id"):
                        self.locator_id = value
                        self.locator_id.value_namespace = name_space
                        self.locator_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.name:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.name:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "names" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-locator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "name"):
                    for c in self.name:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vservice.ServiceFunctionLocator.Names.Name()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.name.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.names is not None and self.names.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.names is not None and self.names.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "service-function-locator" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "names"):
                if (self.names is None):
                    self.names = Vservice.ServiceFunctionLocator.Names()
                    self.names.parent = self
                    self._children_name_map["names"] = "names"
                return self.names

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "names"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.metadata_disposition = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vservice.MetadataDispositions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vservice.MetadataDispositions, self).__setattr__(name, value)


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

                self.disposition_name = YLeaf(YType.str, "disposition-name")

                self.format = YLeaf(YType.enumeration, "format")

                self.match_entry = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disposition_name",
                                "format") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vservice.MetadataDispositions.MetadataDisposition, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vservice.MetadataDispositions.MetadataDisposition, self).__setattr__(name, value)


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

                    self.match_entry_name = YLeaf(YType.str, "match-entry-name")

                    self.node = Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("match_entry_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry, self).__setattr__(name, value)


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

                        self.action_type = YLeaf(YType.enumeration, "action-type")

                        self.match_type = YLeaf(YType.enumeration, "match-type")

                        self.nexthop_ipv4_address = YLeaf(YType.str, "nexthop-ipv4-address")

                        self.tenant_id = YLeafList(YType.int32, "tenant-id")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("action_type",
                                        "match_type",
                                        "nexthop_ipv4_address",
                                        "tenant_id",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.tenant_id.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.action_type.is_set or
                            self.match_type.is_set or
                            self.nexthop_ipv4_address.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        for leaf in self.tenant_id.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.action_type.yfilter != YFilter.not_set or
                            self.match_type.yfilter != YFilter.not_set or
                            self.nexthop_ipv4_address.yfilter != YFilter.not_set or
                            self.tenant_id.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.action_type.is_set or self.action_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.action_type.get_name_leafdata())
                        if (self.match_type.is_set or self.match_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.match_type.get_name_leafdata())
                        if (self.nexthop_ipv4_address.is_set or self.nexthop_ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nexthop_ipv4_address.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        leaf_name_data.extend(self.tenant_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "action-type" or name == "match-type" or name == "nexthop-ipv4-address" or name == "tenant-id" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "action-type"):
                            self.action_type = value
                            self.action_type.value_namespace = name_space
                            self.action_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "match-type"):
                            self.match_type = value
                            self.match_type.value_namespace = name_space
                            self.match_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "nexthop-ipv4-address"):
                            self.nexthop_ipv4_address = value
                            self.nexthop_ipv4_address.value_namespace = name_space
                            self.nexthop_ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "tenant-id"):
                            self.tenant_id.append(value)
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.match_entry_name.is_set or
                        (self.node is not None and self.node.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.match_entry_name.yfilter != YFilter.not_set or
                        (self.node is not None and self.node.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "match-entry" + "[match-entry-name='" + self.match_entry_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.match_entry_name.is_set or self.match_entry_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.match_entry_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "node"):
                        if (self.node is None):
                            self.node = Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                        return self.node

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node" or name == "match-entry-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "match-entry-name"):
                        self.match_entry_name = value
                        self.match_entry_name.value_namespace = name_space
                        self.match_entry_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.match_entry:
                    if (c.has_data()):
                        return True
                return (
                    self.disposition_name.is_set or
                    self.format.is_set)

            def has_operation(self):
                for c in self.match_entry:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.disposition_name.yfilter != YFilter.not_set or
                    self.format.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "metadata-disposition" + "[disposition-name='" + self.disposition_name.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/metadata-dispositions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disposition_name.is_set or self.disposition_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disposition_name.get_name_leafdata())
                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.format.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "match-entry"):
                    for c in self.match_entry:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vservice.MetadataDispositions.MetadataDisposition.MatchEntry()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.match_entry.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "match-entry" or name == "disposition-name" or name == "format"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disposition-name"):
                    self.disposition_name = value
                    self.disposition_name.value_namespace = name_space
                    self.disposition_name.value_namespace_prefix = name_space_prefix
                if(value_path == "format"):
                    self.format = value
                    self.format.value_namespace = name_space
                    self.format.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.metadata_disposition:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.metadata_disposition:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "metadata-dispositions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "metadata-disposition"):
                for c in self.metadata_disposition:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vservice.MetadataDispositions.MetadataDisposition()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.metadata_disposition.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "metadata-disposition"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.names = Vservice.ServiceFunctionForwardLocator.Names()
            self.names.parent = self
            self._children_name_map["names"] = "names"
            self._children_yang_names.add("names")


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

                self.name = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vservice.ServiceFunctionForwardLocator.Names, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vservice.ServiceFunctionForwardLocator.Names, self).__setattr__(name, value)


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

                    self.function_name = YLeaf(YType.str, "function-name")

                    self.locator_id = YLeaf(YType.uint32, "locator-id")

                    self.node = Vservice.ServiceFunctionForwardLocator.Names.Name.Node()
                    self.node.parent = self
                    self._children_name_map["node"] = "node"
                    self._children_yang_names.add("node")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("function_name",
                                    "locator_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vservice.ServiceFunctionForwardLocator.Names.Name, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vservice.ServiceFunctionForwardLocator.Names.Name, self).__setattr__(name, value)


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

                        self.ipv4_destination_address = YLeaf(YType.str, "ipv4-destination-address")

                        self.ipv4_source_address = YLeaf(YType.str, "ipv4-source-address")

                        self.transport = YLeaf(YType.enumeration, "transport")

                        self.vni = YLeaf(YType.int32, "vni")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv4_destination_address",
                                        "ipv4_source_address",
                                        "transport",
                                        "vni") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vservice.ServiceFunctionForwardLocator.Names.Name.Node, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vservice.ServiceFunctionForwardLocator.Names.Name.Node, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipv4_destination_address.is_set or
                            self.ipv4_source_address.is_set or
                            self.transport.is_set or
                            self.vni.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv4_destination_address.yfilter != YFilter.not_set or
                            self.ipv4_source_address.yfilter != YFilter.not_set or
                            self.transport.yfilter != YFilter.not_set or
                            self.vni.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "node" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv4_destination_address.is_set or self.ipv4_destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_destination_address.get_name_leafdata())
                        if (self.ipv4_source_address.is_set or self.ipv4_source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_source_address.get_name_leafdata())
                        if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transport.get_name_leafdata())
                        if (self.vni.is_set or self.vni.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vni.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4-destination-address" or name == "ipv4-source-address" or name == "transport" or name == "vni"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv4-destination-address"):
                            self.ipv4_destination_address = value
                            self.ipv4_destination_address.value_namespace = name_space
                            self.ipv4_destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-source-address"):
                            self.ipv4_source_address = value
                            self.ipv4_source_address.value_namespace = name_space
                            self.ipv4_source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "transport"):
                            self.transport = value
                            self.transport.value_namespace = name_space
                            self.transport.value_namespace_prefix = name_space_prefix
                        if(value_path == "vni"):
                            self.vni = value
                            self.vni.value_namespace = name_space
                            self.vni.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.function_name.is_set or
                        self.locator_id.is_set or
                        (self.node is not None and self.node.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.function_name.yfilter != YFilter.not_set or
                        self.locator_id.yfilter != YFilter.not_set or
                        (self.node is not None and self.node.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "name" + "[function-name='" + self.function_name.get() + "']" + "[locator-id='" + self.locator_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-forward-locator/names/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.function_name.is_set or self.function_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.function_name.get_name_leafdata())
                    if (self.locator_id.is_set or self.locator_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.locator_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "node"):
                        if (self.node is None):
                            self.node = Vservice.ServiceFunctionForwardLocator.Names.Name.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                        return self.node

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "node" or name == "function-name" or name == "locator-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "function-name"):
                        self.function_name = value
                        self.function_name.value_namespace = name_space
                        self.function_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "locator-id"):
                        self.locator_id = value
                        self.locator_id.value_namespace = name_space
                        self.locator_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.name:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.name:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "names" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-forward-locator/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "name"):
                    for c in self.name:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vservice.ServiceFunctionForwardLocator.Names.Name()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.name.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.names is not None and self.names.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.names is not None and self.names.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "service-function-forward-locator" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "names"):
                if (self.names is None):
                    self.names = Vservice.ServiceFunctionForwardLocator.Names()
                    self.names.parent = self
                    self._children_name_map["names"] = "names"
                return self.names

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "names"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.metadata_template = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vservice.MetadataTemplates, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vservice.MetadataTemplates, self).__setattr__(name, value)


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

                self.metadata_name = YLeaf(YType.str, "metadata-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.format = YLeaf(YType.enumeration, "format")

                self.tenant_id = YLeaf(YType.uint32, "tenant-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("metadata_name",
                                "type",
                                "format",
                                "tenant_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vservice.MetadataTemplates.MetadataTemplate, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vservice.MetadataTemplates.MetadataTemplate, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.metadata_name.is_set or
                    self.type.is_set or
                    self.format.is_set or
                    self.tenant_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.metadata_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.format.yfilter != YFilter.not_set or
                    self.tenant_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "metadata-template" + "[metadata-name='" + self.metadata_name.get() + "']" + "[type='" + self.type.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/metadata-templates/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.metadata_name.is_set or self.metadata_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.metadata_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.format.get_name_leafdata())
                if (self.tenant_id.is_set or self.tenant_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tenant_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "metadata-name" or name == "type" or name == "format" or name == "tenant-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "metadata-name"):
                    self.metadata_name = value
                    self.metadata_name.value_namespace = name_space
                    self.metadata_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "format"):
                    self.format = value
                    self.format.value_namespace = name_space
                    self.format.value_namespace_prefix = name_space_prefix
                if(value_path == "tenant-id"):
                    self.tenant_id = value
                    self.tenant_id.value_namespace = name_space
                    self.tenant_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.metadata_template:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.metadata_template:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "metadata-templates" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "metadata-template"):
                for c in self.metadata_template:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vservice.MetadataTemplates.MetadataTemplate()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.metadata_template.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "metadata-template"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.paths = Vservice.ServiceFunctionPath.Paths()
            self.paths.parent = self
            self._children_name_map["paths"] = "paths"
            self._children_yang_names.add("paths")


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

                self.path = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vservice.ServiceFunctionPath.Paths, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vservice.ServiceFunctionPath.Paths, self).__setattr__(name, value)


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

                    self.path_id = YLeaf(YType.uint32, "path-id")

                    self.service_index = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("path_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vservice.ServiceFunctionPath.Paths.Path, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vservice.ServiceFunctionPath.Paths.Path, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex, self).__setattr__(name, value)


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

                            self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node()
                            self.node.parent = self
                            self._children_name_map["node"] = "node"
                            self._children_yang_names.add("node")


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

                                self.action = YLeaf(YType.enumeration, "action")

                                self.metatdata_disposition = YLeaf(YType.str, "metatdata-disposition")

                                self.nexthop_ipv4_address = YLeaf(YType.str, "nexthop-ipv4-address")

                                self.vrf = YLeaf(YType.str, "vrf")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("action",
                                                "metatdata_disposition",
                                                "nexthop_ipv4_address",
                                                "vrf") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.action.is_set or
                                    self.metatdata_disposition.is_set or
                                    self.nexthop_ipv4_address.is_set or
                                    self.vrf.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.action.yfilter != YFilter.not_set or
                                    self.metatdata_disposition.yfilter != YFilter.not_set or
                                    self.nexthop_ipv4_address.yfilter != YFilter.not_set or
                                    self.vrf.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "node" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.action.get_name_leafdata())
                                if (self.metatdata_disposition.is_set or self.metatdata_disposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metatdata_disposition.get_name_leafdata())
                                if (self.nexthop_ipv4_address.is_set or self.nexthop_ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nexthop_ipv4_address.get_name_leafdata())
                                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "action" or name == "metatdata-disposition" or name == "nexthop-ipv4-address" or name == "vrf"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "action"):
                                    self.action = value
                                    self.action.value_namespace = name_space
                                    self.action.value_namespace_prefix = name_space_prefix
                                if(value_path == "metatdata-disposition"):
                                    self.metatdata_disposition = value
                                    self.metatdata_disposition.value_namespace = name_space
                                    self.metatdata_disposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "nexthop-ipv4-address"):
                                    self.nexthop_ipv4_address = value
                                    self.nexthop_ipv4_address.value_namespace = name_space
                                    self.nexthop_ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf"):
                                    self.vrf = value
                                    self.vrf.value_namespace = name_space
                                    self.vrf.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.node is not None and self.node.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.node is not None and self.node.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "terminate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "node"):
                                if (self.node is None):
                                    self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node()
                                    self.node.parent = self
                                    self._children_name_map["node"] = "node"
                                return self.node

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "node"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.sff_name = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames, self).__setattr__(name, value)


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

                                self.name = YLeaf(YType.str, "name")

                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node()
                                self.node.parent = self
                                self._children_name_map["node"] = "node"
                                self._children_yang_names.add("node")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName, self).__setattr__(name, value)


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

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.reserved = YLeaf(YType.empty, "reserved")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable",
                                                    "reserved") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.enable.is_set or
                                        self.reserved.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.reserved.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "node" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.reserved.is_set or self.reserved.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.reserved.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable" or name == "reserved"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "reserved"):
                                        self.reserved = value
                                        self.reserved.value_namespace = name_space
                                        self.reserved.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.name.is_set or
                                    (self.node is not None and self.node.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    (self.node is not None and self.node.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sff-name" + "[name='" + self.name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "node"):
                                    if (self.node is None):
                                        self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node()
                                        self.node.parent = self
                                        self._children_name_map["node"] = "node"
                                    return self.node

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "node" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sff_name:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sff_name:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sff-names" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sff-name"):
                                for c in self.sff_name:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sff_name.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sff-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.sf_name = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames, self).__setattr__(name, value)


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

                                self.name = YLeaf(YType.str, "name")

                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node()
                                self.node.parent = self
                                self._children_name_map["node"] = "node"
                                self._children_yang_names.add("node")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName, self).__setattr__(name, value)


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

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.reserved = YLeaf(YType.empty, "reserved")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable",
                                                    "reserved") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.enable.is_set or
                                        self.reserved.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.reserved.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "node" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.reserved.is_set or self.reserved.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.reserved.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable" or name == "reserved"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "reserved"):
                                        self.reserved = value
                                        self.reserved.value_namespace = name_space
                                        self.reserved.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.name.is_set or
                                    (self.node is not None and self.node.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    (self.node is not None and self.node.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sf-name" + "[name='" + self.name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "node"):
                                    if (self.node is None):
                                        self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node()
                                        self.node.parent = self
                                        self._children_name_map["node"] = "node"
                                    return self.node

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "node" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sf_name:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sf_name:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sf-names" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sf-name"):
                                for c in self.sf_name:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sf_name.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.index.is_set or
                            (self.sf_names is not None and self.sf_names.has_data()) or
                            (self.sff_names is not None and self.sff_names.has_data()) or
                            (self.terminate is not None and self.terminate.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            (self.sf_names is not None and self.sf_names.has_operation()) or
                            (self.sff_names is not None and self.sff_names.has_operation()) or
                            (self.terminate is not None and self.terminate.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-index" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sf-names"):
                            if (self.sf_names is None):
                                self.sf_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames()
                                self.sf_names.parent = self
                                self._children_name_map["sf_names"] = "sf-names"
                            return self.sf_names

                        if (child_yang_name == "sff-names"):
                            if (self.sff_names is None):
                                self.sff_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames()
                                self.sff_names.parent = self
                                self._children_name_map["sff_names"] = "sff-names"
                            return self.sff_names

                        if (child_yang_name == "terminate"):
                            if (self.terminate is None):
                                self.terminate = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate()
                                self.terminate.parent = self
                                self._children_name_map["terminate"] = "terminate"
                            return self.terminate

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sf-names" or name == "sff-names" or name == "terminate" or name == "index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.service_index:
                        if (c.has_data()):
                            return True
                    return self.path_id.is_set

                def has_operation(self):
                    for c in self.service_index:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.path_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-path/paths/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "service-index"):
                        for c in self.service_index:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.service_index.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service-index" or name == "path-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "path-id"):
                        self.path_id = value
                        self.path_id.value_namespace = name_space
                        self.path_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.path:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.path:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "paths" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/service-function-path/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "path"):
                    for c in self.path:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Vservice.ServiceFunctionPath.Paths.Path()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.path.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.paths is not None and self.paths.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.paths is not None and self.paths.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "service-function-path" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "paths"):
                if (self.paths is None):
                    self.paths = Vservice.ServiceFunctionPath.Paths()
                    self.paths.parent = self
                    self._children_name_map["paths"] = "paths"
                return self.paths

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "paths"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.metadata_dispositions is not None and self.metadata_dispositions.has_data()) or
            (self.metadata_templates is not None and self.metadata_templates.has_data()) or
            (self.service_function_forward_locator is not None and self.service_function_forward_locator.has_data()) or
            (self.service_function_locator is not None and self.service_function_locator.has_data()) or
            (self.service_function_path is not None and self.service_function_path.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.metadata_dispositions is not None and self.metadata_dispositions.has_operation()) or
            (self.metadata_templates is not None and self.metadata_templates.has_operation()) or
            (self.service_function_forward_locator is not None and self.service_function_forward_locator.has_operation()) or
            (self.service_function_locator is not None and self.service_function_locator.has_operation()) or
            (self.service_function_path is not None and self.service_function_path.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-vservice-cfg:vservice" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "metadata-dispositions"):
            if (self.metadata_dispositions is None):
                self.metadata_dispositions = Vservice.MetadataDispositions()
                self.metadata_dispositions.parent = self
                self._children_name_map["metadata_dispositions"] = "metadata-dispositions"
            return self.metadata_dispositions

        if (child_yang_name == "metadata-templates"):
            if (self.metadata_templates is None):
                self.metadata_templates = Vservice.MetadataTemplates()
                self.metadata_templates.parent = self
                self._children_name_map["metadata_templates"] = "metadata-templates"
            return self.metadata_templates

        if (child_yang_name == "service-function-forward-locator"):
            if (self.service_function_forward_locator is None):
                self.service_function_forward_locator = Vservice.ServiceFunctionForwardLocator()
                self.service_function_forward_locator.parent = self
                self._children_name_map["service_function_forward_locator"] = "service-function-forward-locator"
            return self.service_function_forward_locator

        if (child_yang_name == "service-function-locator"):
            if (self.service_function_locator is None):
                self.service_function_locator = Vservice.ServiceFunctionLocator()
                self.service_function_locator.parent = self
                self._children_name_map["service_function_locator"] = "service-function-locator"
            return self.service_function_locator

        if (child_yang_name == "service-function-path"):
            if (self.service_function_path is None):
                self.service_function_path = Vservice.ServiceFunctionPath()
                self.service_function_path.parent = self
                self._children_name_map["service_function_path"] = "service-function-path"
            return self.service_function_path

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "metadata-dispositions" or name == "metadata-templates" or name == "service-function-forward-locator" or name == "service-function-locator" or name == "service-function-path"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vservice()
        return self._top_entity

