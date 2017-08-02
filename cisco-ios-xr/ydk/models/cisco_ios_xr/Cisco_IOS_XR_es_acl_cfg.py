""" Cisco_IOS_XR_es_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package configuration.

This module contains definitions
for the following management objects\:
  es\-acl\: Layer 2 ACL configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EsAclGrantEnum(Enum):
    """
    EsAclGrantEnum

    ES acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = Enum.YLeaf(0, "deny")

    permit = Enum.YLeaf(1, "permit")



class EsAcl(Entity):
    """
    Layer 2 ACL configuration data
    
    .. attribute:: accesses
    
    	Table of access lists
    	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses>`
    
    

    """

    _prefix = 'es-acl-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(EsAcl, self).__init__()
        self._top_entity = None

        self.yang_name = "es-acl"
        self.yang_parent_name = "Cisco-IOS-XR-es-acl-cfg"

        self.accesses = EsAcl.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._children_yang_names.add("accesses")


    class Accesses(Entity):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access>`
        
        

        """

        _prefix = 'es-acl-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(EsAcl.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "es-acl"

            self.access = YList(self)

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
                        super(EsAcl.Accesses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EsAcl.Accesses, self).__setattr__(name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: name  <key>
            
            	Name of the access list
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of access list entries
            	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'es-acl-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(EsAcl.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"

                self.name = YLeaf(YType.str, "name")

                self.access_list_entries = EsAcl.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self
                self._children_name_map["access_list_entries"] = "access-list-entries"
                self._children_yang_names.add("access-list-entries")

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
                            super(EsAcl.Accesses.Access, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EsAcl.Accesses.Access, self).__setattr__(name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'es-acl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(EsAcl.Accesses.Access.AccessListEntries, self).__init__()

                    self.yang_name = "access-list-entries"
                    self.yang_parent_name = "access"

                    self.access_list_entry = YList(self)

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
                                super(EsAcl.Accesses.Access.AccessListEntries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EsAcl.Accesses.Access.AccessListEntries, self).__setattr__(name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or anAccess List Entry to match against
                    
                    .. attribute:: sequence_number  <key>
                    
                    	Sequence number of access list entry
                    	**type**\:  int
                    
                    	**range:** 1..2147483646
                    
                    .. attribute:: capture
                    
                    	Enable capture
                    	**type**\:  bool
                    
                    .. attribute:: cos
                    
                    	COS value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: dei
                    
                    	DEI bit
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:   :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: ether_type_number
                    
                    	Ethernet type Number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the ACE
                    	**type**\:   :py:class:`EsAclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAclGrantEnum>`
                    
                    .. attribute:: inner_cos
                    
                    	Inner COS value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: inner_dei
                    
                    	Inner DEI bit
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: inner_vlan1
                    
                    	Inner VLAN ID/range lower limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: inner_vlan2
                    
                    	Inner VLAN ID range higher limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: log_option
                    
                    	Whether and how to log matches against this entry
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the access list
                    	**type**\:  str
                    
                    .. attribute:: sequence_str
                    
                    	Sequence String for the ace
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:   :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: vlan1
                    
                    	VLAN ID/range lower limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vlan2
                    
                    	VLAN ID range higher limit
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'es-acl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"

                        self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                        self.capture = YLeaf(YType.boolean, "capture")

                        self.cos = YLeaf(YType.uint8, "cos")

                        self.dei = YLeaf(YType.uint8, "dei")

                        self.ether_type_number = YLeaf(YType.uint16, "ether-type-number")

                        self.grant = YLeaf(YType.enumeration, "grant")

                        self.inner_cos = YLeaf(YType.uint8, "inner-cos")

                        self.inner_dei = YLeaf(YType.uint8, "inner-dei")

                        self.inner_vlan1 = YLeaf(YType.uint16, "inner-vlan1")

                        self.inner_vlan2 = YLeaf(YType.uint16, "inner-vlan2")

                        self.log_option = YLeaf(YType.uint8, "log-option")

                        self.remark = YLeaf(YType.str, "remark")

                        self.sequence_str = YLeaf(YType.str, "sequence-str")

                        self.vlan1 = YLeaf(YType.uint16, "vlan1")

                        self.vlan2 = YLeaf(YType.uint16, "vlan2")

                        self.destination_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"
                        self._children_yang_names.add("destination-network")

                        self.source_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"
                        self._children_yang_names.add("source-network")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("sequence_number",
                                        "capture",
                                        "cos",
                                        "dei",
                                        "ether_type_number",
                                        "grant",
                                        "inner_cos",
                                        "inner_dei",
                                        "inner_vlan1",
                                        "inner_vlan2",
                                        "log_option",
                                        "remark",
                                        "sequence_str",
                                        "vlan1",
                                        "vlan2") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry, self).__setattr__(name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source address to match, leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source address (if specified), leave unspecified for no wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_wild_card_bits = YLeaf(YType.str, "source-wild-card-bits")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("source_address",
                                            "source_wild_card_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.source_address.is_set or
                                self.source_wild_card_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_wild_card_bits.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "source-network" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_address.get_name_leafdata())
                            if (self.source_wild_card_bits.is_set or self.source_wild_card_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_wild_card_bits.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "source-address" or name == "source-wild-card-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-wild-card-bits"):
                                self.source_wild_card_bits = value
                                self.source_wild_card_bits.value_namespace = name_space
                                self.source_wild_card_bits.value_namespace_prefix = name_space_prefix


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination address to match (if a protocol was specified), leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination address (if specified), leave unspecified for no wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_wild_card_bits = YLeaf(YType.str, "destination-wild-card-bits")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_address",
                                            "destination_wild_card_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.destination_address.is_set or
                                self.destination_wild_card_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.destination_wild_card_bits.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-network" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.destination_wild_card_bits.is_set or self.destination_wild_card_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_wild_card_bits.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "destination-address" or name == "destination-wild-card-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-wild-card-bits"):
                                self.destination_wild_card_bits = value
                                self.destination_wild_card_bits.value_namespace = name_space
                                self.destination_wild_card_bits.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.sequence_number.is_set or
                            self.capture.is_set or
                            self.cos.is_set or
                            self.dei.is_set or
                            self.ether_type_number.is_set or
                            self.grant.is_set or
                            self.inner_cos.is_set or
                            self.inner_dei.is_set or
                            self.inner_vlan1.is_set or
                            self.inner_vlan2.is_set or
                            self.log_option.is_set or
                            self.remark.is_set or
                            self.sequence_str.is_set or
                            self.vlan1.is_set or
                            self.vlan2.is_set or
                            (self.destination_network is not None and self.destination_network.has_data()) or
                            (self.source_network is not None and self.source_network.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sequence_number.yfilter != YFilter.not_set or
                            self.capture.yfilter != YFilter.not_set or
                            self.cos.yfilter != YFilter.not_set or
                            self.dei.yfilter != YFilter.not_set or
                            self.ether_type_number.yfilter != YFilter.not_set or
                            self.grant.yfilter != YFilter.not_set or
                            self.inner_cos.yfilter != YFilter.not_set or
                            self.inner_dei.yfilter != YFilter.not_set or
                            self.inner_vlan1.yfilter != YFilter.not_set or
                            self.inner_vlan2.yfilter != YFilter.not_set or
                            self.log_option.yfilter != YFilter.not_set or
                            self.remark.yfilter != YFilter.not_set or
                            self.sequence_str.yfilter != YFilter.not_set or
                            self.vlan1.yfilter != YFilter.not_set or
                            self.vlan2.yfilter != YFilter.not_set or
                            (self.destination_network is not None and self.destination_network.has_operation()) or
                            (self.source_network is not None and self.source_network.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-list-entry" + "[sequence-number='" + self.sequence_number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.sequence_number.is_set or self.sequence_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sequence_number.get_name_leafdata())
                        if (self.capture.is_set or self.capture.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.capture.get_name_leafdata())
                        if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos.get_name_leafdata())
                        if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dei.get_name_leafdata())
                        if (self.ether_type_number.is_set or self.ether_type_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ether_type_number.get_name_leafdata())
                        if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.grant.get_name_leafdata())
                        if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_cos.get_name_leafdata())
                        if (self.inner_dei.is_set or self.inner_dei.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_dei.get_name_leafdata())
                        if (self.inner_vlan1.is_set or self.inner_vlan1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_vlan1.get_name_leafdata())
                        if (self.inner_vlan2.is_set or self.inner_vlan2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_vlan2.get_name_leafdata())
                        if (self.log_option.is_set or self.log_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.log_option.get_name_leafdata())
                        if (self.remark.is_set or self.remark.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remark.get_name_leafdata())
                        if (self.sequence_str.is_set or self.sequence_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sequence_str.get_name_leafdata())
                        if (self.vlan1.is_set or self.vlan1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan1.get_name_leafdata())
                        if (self.vlan2.is_set or self.vlan2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vlan2.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "destination-network"):
                            if (self.destination_network is None):
                                self.destination_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                                self.destination_network.parent = self
                                self._children_name_map["destination_network"] = "destination-network"
                            return self.destination_network

                        if (child_yang_name == "source-network"):
                            if (self.source_network is None):
                                self.source_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                                self.source_network.parent = self
                                self._children_name_map["source_network"] = "source-network"
                            return self.source_network

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-network" or name == "source-network" or name == "sequence-number" or name == "capture" or name == "cos" or name == "dei" or name == "ether-type-number" or name == "grant" or name == "inner-cos" or name == "inner-dei" or name == "inner-vlan1" or name == "inner-vlan2" or name == "log-option" or name == "remark" or name == "sequence-str" or name == "vlan1" or name == "vlan2"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "sequence-number"):
                            self.sequence_number = value
                            self.sequence_number.value_namespace = name_space
                            self.sequence_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "capture"):
                            self.capture = value
                            self.capture.value_namespace = name_space
                            self.capture.value_namespace_prefix = name_space_prefix
                        if(value_path == "cos"):
                            self.cos = value
                            self.cos.value_namespace = name_space
                            self.cos.value_namespace_prefix = name_space_prefix
                        if(value_path == "dei"):
                            self.dei = value
                            self.dei.value_namespace = name_space
                            self.dei.value_namespace_prefix = name_space_prefix
                        if(value_path == "ether-type-number"):
                            self.ether_type_number = value
                            self.ether_type_number.value_namespace = name_space
                            self.ether_type_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "grant"):
                            self.grant = value
                            self.grant.value_namespace = name_space
                            self.grant.value_namespace_prefix = name_space_prefix
                        if(value_path == "inner-cos"):
                            self.inner_cos = value
                            self.inner_cos.value_namespace = name_space
                            self.inner_cos.value_namespace_prefix = name_space_prefix
                        if(value_path == "inner-dei"):
                            self.inner_dei = value
                            self.inner_dei.value_namespace = name_space
                            self.inner_dei.value_namespace_prefix = name_space_prefix
                        if(value_path == "inner-vlan1"):
                            self.inner_vlan1 = value
                            self.inner_vlan1.value_namespace = name_space
                            self.inner_vlan1.value_namespace_prefix = name_space_prefix
                        if(value_path == "inner-vlan2"):
                            self.inner_vlan2 = value
                            self.inner_vlan2.value_namespace = name_space
                            self.inner_vlan2.value_namespace_prefix = name_space_prefix
                        if(value_path == "log-option"):
                            self.log_option = value
                            self.log_option.value_namespace = name_space
                            self.log_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "remark"):
                            self.remark = value
                            self.remark.value_namespace = name_space
                            self.remark.value_namespace_prefix = name_space_prefix
                        if(value_path == "sequence-str"):
                            self.sequence_str = value
                            self.sequence_str.value_namespace = name_space
                            self.sequence_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan1"):
                            self.vlan1 = value
                            self.vlan1.value_namespace = name_space
                            self.vlan1.value_namespace_prefix = name_space_prefix
                        if(value_path == "vlan2"):
                            self.vlan2 = value
                            self.vlan2.value_namespace = name_space
                            self.vlan2.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.access_list_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.access_list_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access-list-entries" + path_buffer

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

                    if (child_yang_name == "access-list-entry"):
                        for c in self.access_list_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.access_list_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.access_list_entries is not None and self.access_list_entries.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.access_list_entries is not None and self.access_list_entries.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-es-acl-cfg:es-acl/accesses/%s" % self.get_segment_path()
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

                if (child_yang_name == "access-list-entries"):
                    if (self.access_list_entries is None):
                        self.access_list_entries = EsAcl.Accesses.Access.AccessListEntries()
                        self.access_list_entries.parent = self
                        self._children_name_map["access_list_entries"] = "access-list-entries"
                    return self.access_list_entries

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-list-entries" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.access:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.access:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "accesses" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-es-acl-cfg:es-acl/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "access"):
                for c in self.access:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EsAcl.Accesses.Access()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.access.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "access"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.accesses is not None and self.accesses.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.accesses is not None and self.accesses.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-es-acl-cfg:es-acl" + path_buffer

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

        if (child_yang_name == "accesses"):
            if (self.accesses is None):
                self.accesses = EsAcl.Accesses()
                self.accesses.parent = self
                self._children_name_map["accesses"] = "accesses"
            return self.accesses

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "accesses"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EsAcl()
        return self._top_entity

