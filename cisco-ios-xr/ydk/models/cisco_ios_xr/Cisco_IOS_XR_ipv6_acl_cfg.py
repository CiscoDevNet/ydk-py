""" Cisco_IOS_XR_ipv6_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: IPv6 ACL configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NextHopType(Enum):
    """
    NextHopType (Enum Class)

    Next\-hop type.

    .. data:: regular_next_hop = 1

    	Regular next-hop.

    .. data:: default_next_hop = 2

    	Default next-hop.

    """

    regular_next_hop = Enum.YLeaf(1, "regular-next-hop")

    default_next_hop = Enum.YLeaf(2, "default-next-hop")



class Ipv6AclAndPrefixList(Entity):
    """
    IPv6 ACL configuration data
    
    .. attribute:: prefixes
    
    	Table of prefix lists
    	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes>`
    
    .. attribute:: log_update
    
    	Control access lists log updates
    	**type**\:  :py:class:`LogUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.LogUpdate>`
    
    .. attribute:: accesses
    
    	Table of access lists
    	**type**\:  :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses>`
    
    

    """

    _prefix = 'ipv6-acl-cfg'
    _revision = '2018-04-03'

    def __init__(self):
        super(Ipv6AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-acl-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("prefixes", ("prefixes", Ipv6AclAndPrefixList.Prefixes)), ("log-update", ("log_update", Ipv6AclAndPrefixList.LogUpdate)), ("accesses", ("accesses", Ipv6AclAndPrefixList.Accesses))])
        self._leafs = OrderedDict()

        self.prefixes = Ipv6AclAndPrefixList.Prefixes()
        self.prefixes.parent = self
        self._children_name_map["prefixes"] = "prefixes"

        self.log_update = Ipv6AclAndPrefixList.LogUpdate()
        self.log_update.parent = self
        self._children_name_map["log_update"] = "log-update"

        self.accesses = Ipv6AclAndPrefixList.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6AclAndPrefixList, [], name, value)


    class Prefixes(Entity):
        """
        Table of prefix lists
        
        .. attribute:: prefix
        
        	Name of a prefix list
        	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2018-04-03'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Prefixes, self).__init__()

            self.yang_name = "prefixes"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefix", ("prefix", Ipv6AclAndPrefixList.Prefixes.Prefix))])
            self._leafs = OrderedDict()

            self.prefix = YList(self)
            self._segment_path = lambda: "prefixes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.Prefixes, [], name, value)


        class Prefix(Entity):
            """
            Name of a prefix list
            
            .. attribute:: name  (key)
            
            	Name of a prefix list
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: prefix_list_entries
            
            	Sequence of entries forming a prefix list
            	**type**\:  :py:class:`PrefixListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries>`
            
            

            """

            _prefix = 'ipv6-acl-cfg'
            _revision = '2018-04-03'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Prefixes.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "prefixes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("prefix-list-entries", ("prefix_list_entries", Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.prefix_list_entries = Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries()
                self.prefix_list_entries.parent = self
                self._children_name_map["prefix_list_entries"] = "prefix-list-entries"
                self._segment_path = lambda: "prefix" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/prefixes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix, ['name'], name, value)


            class PrefixListEntries(Entity):
                """
                Sequence of entries forming a prefix list
                
                .. attribute:: prefix_list_entry
                
                	A prefix list entry; either a description (remark) or a prefix to match against
                	**type**\: list of  		 :py:class:`PrefixListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry>`
                
                

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2018-04-03'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__init__()

                    self.yang_name = "prefix-list-entries"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("prefix-list-entry", ("prefix_list_entry", Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry))])
                    self._leafs = OrderedDict()

                    self.prefix_list_entry = YList(self)
                    self._segment_path = lambda: "prefix-list-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, [], name, value)


                class PrefixListEntry(Entity):
                    """
                    A prefix list entry; either a description
                    (remark) or a prefix to match against
                    
                    .. attribute:: sequence_number  (key)
                    
                    	Sequence number of prefix list
                    	**type**\: int
                    
                    	**range:** 1..2147483646
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the prefix list
                    	**type**\:  :py:class:`Ipv6AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnum>`
                    
                    .. attribute:: ipv6_address_as_string
                    
                    	The IPv6 address if entered  with the ZoneMutually exclusive with Prefix and PrefixMask
                    	**type**\: str
                    
                    .. attribute:: zone
                    
                    	IPv6 Zone if entered  with the IPV6AddressMutually exclusive with Prefix and PrefixMask
                    	**type**\: str
                    
                    .. attribute:: prefix
                    
                    	IPv6 address prefix to match
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_mask
                    
                    	MaskLength of IPv6 address prefix
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: match_exact_length
                    
                    	Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items
                    	**type**\:  :py:class:`Ipv6PrefixMatchExactLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchExactLength>`
                    
                    .. attribute:: exact_prefix_length
                    
                    	If exact prefix length matching specified, set the length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: match_max_length
                    
                    	Set to perform a maximum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:  :py:class:`Ipv6PrefixMatchMaxLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMaxLength>`
                    
                    .. attribute:: max_prefix_length
                    
                    	If maximum length prefix matching specified, set the maximum length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: match_min_length
                    
                    	Set to perform a minimum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:  :py:class:`Ipv6PrefixMatchMinLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMinLength>`
                    
                    .. attribute:: min_prefix_length
                    
                    	If minimum length prefix matching specified, set the minimum length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the prefix list.  Item is mutually exclusive with all others in the object
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ipv6-acl-cfg'
                    _revision = '2018-04-03'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__init__()

                        self.yang_name = "prefix-list-entry"
                        self.yang_parent_name = "prefix-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_number']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                            ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnum', '')])),
                            ('ipv6_address_as_string', (YLeaf(YType.str, 'ipv6-address-as-string'), ['str'])),
                            ('zone', (YLeaf(YType.str, 'zone'), ['str'])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                            ('prefix_mask', (YLeaf(YType.uint8, 'prefix-mask'), ['int'])),
                            ('match_exact_length', (YLeaf(YType.enumeration, 'match-exact-length'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchExactLength', '')])),
                            ('exact_prefix_length', (YLeaf(YType.uint8, 'exact-prefix-length'), ['int'])),
                            ('match_max_length', (YLeaf(YType.enumeration, 'match-max-length'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMaxLength', '')])),
                            ('max_prefix_length', (YLeaf(YType.uint8, 'max-prefix-length'), ['int'])),
                            ('match_min_length', (YLeaf(YType.enumeration, 'match-min-length'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMinLength', '')])),
                            ('min_prefix_length', (YLeaf(YType.uint8, 'min-prefix-length'), ['int'])),
                            ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                        ])
                        self.sequence_number = None
                        self.grant = None
                        self.ipv6_address_as_string = None
                        self.zone = None
                        self.prefix = None
                        self.prefix_mask = None
                        self.match_exact_length = None
                        self.exact_prefix_length = None
                        self.match_max_length = None
                        self.max_prefix_length = None
                        self.match_min_length = None
                        self.min_prefix_length = None
                        self.remark = None
                        self._segment_path = lambda: "prefix-list-entry" + "[sequence-number='" + str(self.sequence_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, ['sequence_number', 'grant', 'ipv6_address_as_string', 'zone', 'prefix', 'prefix_mask', 'match_exact_length', 'exact_prefix_length', 'match_max_length', 'max_prefix_length', 'match_min_length', 'min_prefix_length', 'remark'], name, value)


    class LogUpdate(Entity):
        """
        Control access lists log updates
        
        .. attribute:: threshold
        
        	Log update threshold (number of hits)
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: rate
        
        	Log update rate (log messages per second)
        	**type**\: int
        
        	**range:** 1..1000
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2018-04-03'

        def __init__(self):
            super(Ipv6AclAndPrefixList.LogUpdate, self).__init__()

            self.yang_name = "log-update"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
            ])
            self.threshold = None
            self.rate = None
            self._segment_path = lambda: "log-update"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.LogUpdate, ['threshold', 'rate'], name, value)


    class Accesses(Entity):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of  		 :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2018-04-03'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("access", ("access", Ipv6AclAndPrefixList.Accesses.Access))])
            self._leafs = OrderedDict()

            self.access = YList(self)
            self._segment_path = lambda: "accesses"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.Accesses, [], name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: name  (key)
            
            	Name of the access list
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of access list entries
            	**type**\:  :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'ipv6-acl-cfg'
            _revision = '2018-04-03'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("access-list-entries", ("access_list_entries", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.access_list_entries = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self
                self._children_name_map["access_list_entries"] = "access-list-entries"
                self._segment_path = lambda: "access" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/accesses/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access, ['name'], name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of  		 :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2018-04-03'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries, self).__init__()

                    self.yang_name = "access-list-entries"
                    self.yang_parent_name = "access"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("access-list-entry", ("access_list_entry", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry))])
                    self._leafs = OrderedDict()

                    self.access_list_entry = YList(self)
                    self._segment_path = lambda: "access-list-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries, [], name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or anAccess List Entry to match against
                    
                    .. attribute:: sequence_number  (key)
                    
                    	Sequence number of access list entry
                    	**type**\: int
                    
                    	**range:** 1..2147483643
                    
                    .. attribute:: grant
                    
                    	Forwarding action for the packet. This is required for any non\-remark ACE. Leave unspecified otherwise
                    	**type**\:  :py:class:`Ipv6AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnum>`
                    
                    .. attribute:: protocol_operator
                    
                    	Protocol operator. User can specify equal or leave it unspecified for singleton protocol match, or specify range for protocol range match
                    	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                    
                    .. attribute:: protocol
                    
                    	Protocol number to match. It can be used for the lower bound (range operator) or single value (equal operator). Any value not in the permissible range will be rejected. When leave unspecified, default value is ipv6
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv6AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..255
                    
                    .. attribute:: protocol2
                    
                    	Protocol2 to match. It is used in upper bound (range operator). Any value not in the permissible range will be rejected
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv6AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..255
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:  :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:  :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: source_port
                    
                    	Source port settings
                    	**type**\:  :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort>`
                    
                    .. attribute:: destination_port
                    
                    	Destination port settings
                    	**type**\:  :py:class:`DestinationPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort>`
                    
                    .. attribute:: icmp
                    
                    	ICMP settings
                    	**type**\:  :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp>`
                    
                    .. attribute:: tcp
                    
                    	TCP settings
                    	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp>`
                    
                    .. attribute:: packet_length
                    
                    	Packet length settings
                    	**type**\:  :py:class:`PacketLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength>`
                    
                    .. attribute:: time_to_live
                    
                    	TTL settings
                    	**type**\:  :py:class:`TimeToLive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive>`
                    
                    .. attribute:: dscpvalues
                    
                    	DSCP settings
                    	**type**\:  :py:class:`DSCPValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues>`
                    
                    .. attribute:: dscp
                    
                    	DSCP value to match without using any operators.  Any value not in the permissible range will be rejected. Leave unspecified if DSCP comparion is not to be performed. For Setting dscp values, use the dscp container as this leaf will be deprecated soon
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv6AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclDscpNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..63
                    
                    .. attribute:: precedence
                    
                    	Precedence value to match (if a protocol was specified). Any value not in the permissible range will be rejected. Leave unspecified if precedence comparion is not to be performed
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv6AclPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPrecedenceNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..7
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop settings
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop>`
                    
                    .. attribute:: counter_name
                    
                    	Name of counter to aggregate hardware statistics
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: log_option
                    
                    	Log the packet on this access\-list\-entry/rule
                    	**type**\:  :py:class:`Ipv6AclLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclLoggingEnum>`
                    
                    .. attribute:: capture
                    
                    	Enable capture if set to TRUE
                    	**type**\: bool
                    
                    .. attribute:: undetermined_transport
                    
                    	Enable undetermined\-transport if set to TRUE
                    	**type**\: bool
                    
                    .. attribute:: icmp_off
                    
                    	To turn off ICMP generation for deny ACEs
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: qos_group
                    
                    	Set qos\-group number. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..512
                    
                    .. attribute:: set_ttl
                    
                    	Set TTL Value. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: header_flags
                    
                    	Match if header\-flag is present
                    	**type**\:  :py:class:`HeaderFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags>`
                    
                    .. attribute:: remark
                    
                    	Description for the access\-list\-entry/rules
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: source_prefix_group
                    
                    	IPv6 source network object group name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: destination_prefix_group
                    
                    	IPv6 destination network object group name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: source_port_group
                    
                    	Source port object group name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: destination_port_group
                    
                    	Destination port object group name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: sequence_str
                    
                    	Sequence string for the ace
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv6-acl-cfg'
                    _revision = '2018-04-03'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_number']
                        self._child_classes = OrderedDict([("source-network", ("source_network", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork)), ("destination-network", ("destination_network", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork)), ("source-port", ("source_port", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort)), ("destination-port", ("destination_port", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort)), ("icmp", ("icmp", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp)), ("tcp", ("tcp", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp)), ("packet-length", ("packet_length", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength)), ("time-to-live", ("time_to_live", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive)), ("DSCPValues", ("dscpvalues", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues)), ("next-hop", ("next_hop", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop)), ("header-flags", ("header_flags", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags))])
                        self._leafs = OrderedDict([
                            ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                            ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnum', '')])),
                            ('protocol_operator', (YLeaf(YType.enumeration, 'protocol-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                            ('protocol', (YLeaf(YType.str, 'protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumber', ''),'int'])),
                            ('protocol2', (YLeaf(YType.str, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumber', ''),'int'])),
                            ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber', ''),'int'])),
                            ('precedence', (YLeaf(YType.str, 'precedence'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPrecedenceNumber', ''),'int'])),
                            ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                            ('log_option', (YLeaf(YType.enumeration, 'log-option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclLoggingEnum', '')])),
                            ('capture', (YLeaf(YType.boolean, 'capture'), ['bool'])),
                            ('undetermined_transport', (YLeaf(YType.boolean, 'undetermined-transport'), ['bool'])),
                            ('icmp_off', (YLeaf(YType.empty, 'icmp-off'), ['Empty'])),
                            ('qos_group', (YLeaf(YType.uint32, 'qos-group'), ['int'])),
                            ('set_ttl', (YLeaf(YType.uint32, 'set-ttl'), ['int'])),
                            ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                            ('source_prefix_group', (YLeaf(YType.str, 'source-prefix-group'), ['str'])),
                            ('destination_prefix_group', (YLeaf(YType.str, 'destination-prefix-group'), ['str'])),
                            ('source_port_group', (YLeaf(YType.str, 'source-port-group'), ['str'])),
                            ('destination_port_group', (YLeaf(YType.str, 'destination-port-group'), ['str'])),
                            ('sequence_str', (YLeaf(YType.str, 'sequence-str'), ['str'])),
                        ])
                        self.sequence_number = None
                        self.grant = None
                        self.protocol_operator = None
                        self.protocol = None
                        self.protocol2 = None
                        self.dscp = None
                        self.precedence = None
                        self.counter_name = None
                        self.log_option = None
                        self.capture = None
                        self.undetermined_transport = None
                        self.icmp_off = None
                        self.qos_group = None
                        self.set_ttl = None
                        self.remark = None
                        self.source_prefix_group = None
                        self.destination_prefix_group = None
                        self.source_port_group = None
                        self.destination_port_group = None
                        self.sequence_str = None

                        self.source_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"

                        self.destination_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"

                        self.source_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                        self.source_port.parent = self
                        self._children_name_map["source_port"] = "source-port"

                        self.destination_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                        self.destination_port.parent = self
                        self._children_name_map["destination_port"] = "destination-port"

                        self.icmp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"

                        self.tcp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"

                        self.packet_length = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                        self.packet_length.parent = self
                        self._children_name_map["packet_length"] = "packet-length"

                        self.time_to_live = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                        self.time_to_live.parent = self
                        self._children_name_map["time_to_live"] = "time-to-live"

                        self.dscpvalues = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues()
                        self.dscpvalues.parent = self
                        self._children_name_map["dscpvalues"] = "DSCPValues"

                        self.next_hop = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"

                        self.header_flags = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags()
                        self.header_flags.parent = self
                        self._children_name_map["header_flags"] = "header-flags"
                        self._segment_path = lambda: "access-list-entry" + "[sequence-number='" + str(self.sequence_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, ['sequence_number', u'grant', u'protocol_operator', u'protocol', u'protocol2', u'dscp', u'precedence', u'counter_name', u'log_option', u'capture', u'undetermined_transport', u'icmp_off', u'qos_group', u'set_ttl', u'remark', u'source_prefix_group', u'destination_prefix_group', u'source_port_group', u'destination_port_group', u'sequence_str'], name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source IPv6 address, leave unspecified if inputting as IPv6 address with wildcarding
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source\-address (if specified), leave unspecified for no wildcarding
                        	**type**\: int
                        
                        	**range:** 0..128
                        
                        .. attribute:: source_mask
                        
                        	Source address mask. Either  source\-wild\-card\-bits or source\-mask is  supported, not both. Leave unspecified  for any
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('source_wild_card_bits', (YLeaf(YType.uint8, 'source-wild-card-bits'), ['int'])),
                                ('source_mask', (YLeaf(YType.str, 'source-mask'), ['str'])),
                            ])
                            self.source_address = None
                            self.source_wild_card_bits = None
                            self.source_mask = None
                            self._segment_path = lambda: "source-network"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, [u'source_address', u'source_wild_card_bits', u'source_mask'], name, value)


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination IPv6 address, leave  unspecified if inputting as IPv6 address with  wildcarding
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination  destination\-address (if specified),  leave unspecified for no wildcarding
                        	**type**\: int
                        
                        	**range:** 0..128
                        
                        .. attribute:: destination_mask
                        
                        	Destination address mask. Either  destination\-wild\-card\-bits or destination\-mask  is supported, not both. Leave unspecified for any
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ('destination_wild_card_bits', (YLeaf(YType.uint8, 'destination-wild-card-bits'), ['int'])),
                                ('destination_mask', (YLeaf(YType.str, 'destination-mask'), ['str'])),
                            ])
                            self.destination_address = None
                            self.destination_wild_card_bits = None
                            self.destination_mask = None
                            self._segment_path = lambda: "destination-network"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, [u'destination_address', u'destination_wild_card_bits', u'destination_mask'], name, value)


                    class SourcePort(Entity):
                        """
                        Source port settings.
                        
                        .. attribute:: source_operator
                        
                        	Source port comparison operator. This is a required field if any source port value is given, otherwise, config will be rejected. Leave unspecified if no source port comparison is to be done
                        	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: first_source_port
                        
                        	Lower source port for comparison. It can be used for the lower bound (range operator) or single value (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: second_source_port
                        
                        	Upper source port for comparion. It is used in the upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__init__()

                            self.yang_name = "source-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_operator', (YLeaf(YType.enumeration, 'source-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                                ('first_source_port', (YLeaf(YType.str, 'first-source-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber', ''),'int'])),
                                ('second_source_port', (YLeaf(YType.str, 'second-source-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber', ''),'int'])),
                            ])
                            self.source_operator = None
                            self.first_source_port = None
                            self.second_source_port = None
                            self._segment_path = lambda: "source-port"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, [u'source_operator', u'first_source_port', u'second_source_port'], name, value)


                    class DestinationPort(Entity):
                        """
                        Destination port settings.
                        
                        .. attribute:: destination_operator
                        
                        	Destination port comparison operator. This is a required field if any destination port value is given, otherwise, config will be rejected. Leave unspecified if no destination port comparison is to be done
                        	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: first_destination_port
                        
                        	Lower destination port for comparison. It can be used for the lower bound (range operator) or single value (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: second_destination_port
                        
                        	Upper destination port for comparison. It is used in the upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__init__()

                            self.yang_name = "destination-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_operator', (YLeaf(YType.enumeration, 'destination-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                                ('first_destination_port', (YLeaf(YType.str, 'first-destination-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber', ''),'int'])),
                                ('second_destination_port', (YLeaf(YType.str, 'second-destination-port'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumber', ''),'int'])),
                            ])
                            self.destination_operator = None
                            self.first_destination_port = None
                            self.second_destination_port = None
                            self._segment_path = lambda: "destination-port"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, [u'destination_operator', u'first_destination_port', u'second_destination_port'], name, value)


                    class Icmp(Entity):
                        """
                        ICMP settings.
                        
                        .. attribute:: icmp_type_code
                        
                        	Well known ICMP message code types to match,  leave unspecified if ICMP message code type  comparion is not to be performed
                        	**type**\:  :py:class:`Ipv6AclIcmpTypeCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclIcmpTypeCodeEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('icmp_type_code', (YLeaf(YType.enumeration, 'icmp-type-code'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclIcmpTypeCodeEnum', '')])),
                            ])
                            self.icmp_type_code = None
                            self._segment_path = lambda: "icmp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, [u'icmp_type_code'], name, value)


                    class Tcp(Entity):
                        """
                        TCP settings.
                        
                        .. attribute:: tcp_bits_match_operator
                        
                        	TCP Bits match operator. Leave unspecified if  flexible comparison of TCP bits is not  required
                        	**type**\:  :py:class:`Ipv6AclTcpMatchOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpMatchOperatorEnum>`
                        
                        .. attribute:: tcp_bits
                        
                        	TCP bits to match. Leave unspecified if  comparison of TCP bits is not required
                        	**type**\:  :py:class:`Ipv6AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumber>`
                        
                        .. attribute:: tcp_bits_mask
                        
                        	TCP bits mask to use for flexible TCP matching. Leave unspecified if it is not required
                        	**type**\:  :py:class:`Ipv6AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumber>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__init__()

                            self.yang_name = "tcp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('tcp_bits_match_operator', (YLeaf(YType.enumeration, 'tcp-bits-match-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpMatchOperatorEnum', '')])),
                                ('tcp_bits', (YLeaf(YType.bits, 'tcp-bits'), ['Bits'])),
                                ('tcp_bits_mask', (YLeaf(YType.bits, 'tcp-bits-mask'), ['Bits'])),
                            ])
                            self.tcp_bits_match_operator = None
                            self.tcp_bits = Bits()
                            self.tcp_bits_mask = Bits()
                            self._segment_path = lambda: "tcp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, [u'tcp_bits_match_operator', u'tcp_bits', u'tcp_bits_mask'], name, value)


                    class PacketLength(Entity):
                        """
                        Packet length settings.
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator applicable if packet length is to be compared. This is a required field if any packet\-length value is given, otherwise, config  will be rejected
                        	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: packet_length_min
                        
                        	Mininum packet length value for comparison. It can be used for the lower bound (range operator) or single value (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_max
                        
                        	Maximum packet length value for comparison. It is used in the upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__init__()

                            self.yang_name = "packet-length"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packet_length_operator', (YLeaf(YType.enumeration, 'packet-length-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                                ('packet_length_min', (YLeaf(YType.uint32, 'packet-length-min'), ['int'])),
                                ('packet_length_max', (YLeaf(YType.uint32, 'packet-length-max'), ['int'])),
                            ])
                            self.packet_length_operator = None
                            self.packet_length_min = None
                            self.packet_length_max = None
                            self._segment_path = lambda: "packet-length"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, [u'packet_length_operator', u'packet_length_min', u'packet_length_max'], name, value)


                    class TimeToLive(Entity):
                        """
                        TTL settings.
                        
                        .. attribute:: time_to_live_operator
                        
                        	TTL operator is applicable if TTL is to be compared. This is a required field if any TTL value is given, otherwise, config will be rejected. Leave unspecified if TTL classification is not required
                        	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: time_to_live_min
                        
                        	Mininum TTL value for comparison. It can be used for the lower bound (range operator) or single value (equal, less, greater..etc). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_max
                        
                        	Maximum TTL value for comparison. It is used in the upper bound (range operator). Any value not in the permissible range will be rejected. Leave unspecified otherwise
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__init__()

                            self.yang_name = "time-to-live"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_to_live_operator', (YLeaf(YType.enumeration, 'time-to-live-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                                ('time_to_live_min', (YLeaf(YType.uint32, 'time-to-live-min'), ['int'])),
                                ('time_to_live_max', (YLeaf(YType.uint32, 'time-to-live-max'), ['int'])),
                            ])
                            self.time_to_live_operator = None
                            self.time_to_live_min = None
                            self.time_to_live_max = None
                            self._segment_path = lambda: "time-to-live"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, [u'time_to_live_operator', u'time_to_live_min', u'time_to_live_max'], name, value)


                    class DSCPValues(Entity):
                        """
                        DSCP settings.
                        
                        .. attribute:: dscp_operator
                        
                        	Enumerated DSCP operator values. Used when operator needs to be configured. Leave unspecified if DSCP operator is not required. Note\: if the  dscp operator is not set, it logically behaves  same as equal operator
                        	**type**\:  :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: dscp_lower
                        
                        	DSCP value to match (if a value was specified). It can be used for the lower bound (range operator) or single value (equal, less, greater..etc) or without any operator. Any value not in the permissible range  will be rejected. Leave unspecified if DSCP  comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclDscpNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        .. attribute:: dscp_upper
                        
                        	DSCP2 value to match (if a value was specified), It can be used in the upper bound (range operator) Any value not in the permissible range will be rejected. leave unspecified if DSCP range comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv6AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclDscpNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues, self).__init__()

                            self.yang_name = "DSCPValues"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dscp_operator', (YLeaf(YType.enumeration, 'dscp-operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnum', '')])),
                                ('dscp_lower', (YLeaf(YType.str, 'dscp-lower'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber', ''),'int'])),
                                ('dscp_upper', (YLeaf(YType.str, 'dscp-upper'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumber', ''),'int'])),
                            ])
                            self.dscp_operator = None
                            self.dscp_lower = None
                            self.dscp_upper = None
                            self._segment_path = lambda: "DSCPValues"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DSCPValues, [u'dscp_operator', u'dscp_lower', u'dscp_upper'], name, value)


                    class NextHop(Entity):
                        """
                        Next\-hop settings.
                        
                        .. attribute:: next_hop_type
                        
                        	The nexthop type
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.NextHopType>`
                        
                        .. attribute:: next_hop_1
                        
                        	The first next\-hop settings
                        	**type**\:  :py:class:`NextHop1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1>`
                        
                        .. attribute:: next_hop_2
                        
                        	The second next\-hop settings
                        	**type**\:  :py:class:`NextHop2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2>`
                        
                        .. attribute:: next_hop_3
                        
                        	The third next\-hop settings
                        	**type**\:  :py:class:`NextHop3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("next-hop-1", ("next_hop_1", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1)), ("next-hop-2", ("next_hop_2", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2)), ("next-hop-3", ("next_hop_3", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3))])
                            self._leafs = OrderedDict([
                                ('next_hop_type', (YLeaf(YType.enumeration, 'next-hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'NextHopType', '')])),
                            ])
                            self.next_hop_type = None

                            self.next_hop_1 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1()
                            self.next_hop_1.parent = self
                            self._children_name_map["next_hop_1"] = "next-hop-1"

                            self.next_hop_2 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2()
                            self.next_hop_2.parent = self
                            self._children_name_map["next_hop_2"] = "next-hop-2"

                            self.next_hop_3 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3()
                            self.next_hop_3.parent = self
                            self._children_name_map["next_hop_3"] = "next-hop-3"
                            self._segment_path = lambda: "next-hop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, [u'next_hop_type'], name, value)


                        class NextHop1(Entity):
                            """
                            The first next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2018-04-03'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__init__()

                                self.yang_name = "next-hop-1"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-1"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, [u'next_hop', u'vrf_name', u'track_name'], name, value)


                        class NextHop2(Entity):
                            """
                            The second next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2018-04-03'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__init__()

                                self.yang_name = "next-hop-2"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-2"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, [u'next_hop', u'vrf_name', u'track_name'], name, value)


                        class NextHop3(Entity):
                            """
                            The third next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2018-04-03'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__init__()

                                self.yang_name = "next-hop-3"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-3"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, [u'next_hop', u'vrf_name', u'track_name'], name, value)


                    class HeaderFlags(Entity):
                        """
                        Match if header\-flag is present.
                        
                        .. attribute:: routing
                        
                        	Match if routing header is present
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: destopts
                        
                        	Match if destops header is present
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: hop_by_hop
                        
                        	Match if hop\-by\-hop header is present
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: fragments
                        
                        	Match if fragments header is present
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: authen
                        
                        	Match if authen header is present
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2018-04-03'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags, self).__init__()

                            self.yang_name = "header-flags"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('routing', (YLeaf(YType.empty, 'routing'), ['Empty'])),
                                ('destopts', (YLeaf(YType.empty, 'destopts'), ['Empty'])),
                                ('hop_by_hop', (YLeaf(YType.empty, 'hop-by-hop'), ['Empty'])),
                                ('fragments', (YLeaf(YType.empty, 'fragments'), ['Empty'])),
                                ('authen', (YLeaf(YType.empty, 'authen'), ['Empty'])),
                            ])
                            self.routing = None
                            self.destopts = None
                            self.hop_by_hop = None
                            self.fragments = None
                            self.authen = None
                            self._segment_path = lambda: "header-flags"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags, [u'routing', u'destopts', u'hop_by_hop', u'fragments', u'authen'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6AclAndPrefixList()
        return self._top_entity

