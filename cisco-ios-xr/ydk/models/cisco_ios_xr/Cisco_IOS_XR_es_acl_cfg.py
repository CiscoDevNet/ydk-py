""" Cisco_IOS_XR_es_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR es\-acl package configuration.

This module contains definitions
for the following management objects\:
  es\-acl\: Layer 2 ACL configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EsAclGrantEnum(Enum):
    """
    EsAclGrantEnum (Enum Class)

    ES ACL forwarding action.

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
    	**type**\:  :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses>`
    
    

    """

    _prefix = 'es-acl-cfg'
    _revision = '2018-02-26'

    def __init__(self):
        super(EsAcl, self).__init__()
        self._top_entity = None

        self.yang_name = "es-acl"
        self.yang_parent_name = "Cisco-IOS-XR-es-acl-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("accesses", ("accesses", EsAcl.Accesses))])
        self._leafs = OrderedDict()

        self.accesses = EsAcl.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._segment_path = lambda: "Cisco-IOS-XR-es-acl-cfg:es-acl"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EsAcl, [], name, value)


    class Accesses(Entity):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of  		 :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access>`
        
        

        """

        _prefix = 'es-acl-cfg'
        _revision = '2018-02-26'

        def __init__(self):
            super(EsAcl.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "es-acl"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("access", ("access", EsAcl.Accesses.Access))])
            self._leafs = OrderedDict()

            self.access = YList(self)
            self._segment_path = lambda: "accesses"
            self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-cfg:es-acl/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EsAcl.Accesses, [], name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: name  (key)
            
            	Name of the access list
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of access list entries
            	**type**\:  :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'es-acl-cfg'
            _revision = '2018-02-26'

            def __init__(self):
                super(EsAcl.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("access-list-entries", ("access_list_entries", EsAcl.Accesses.Access.AccessListEntries))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.access_list_entries = EsAcl.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self
                self._children_name_map["access_list_entries"] = "access-list-entries"
                self._segment_path = lambda: "access" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-es-acl-cfg:es-acl/accesses/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EsAcl.Accesses.Access, ['name'], name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of  		 :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'es-acl-cfg'
                _revision = '2018-02-26'

                def __init__(self):
                    super(EsAcl.Accesses.Access.AccessListEntries, self).__init__()

                    self.yang_name = "access-list-entries"
                    self.yang_parent_name = "access"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("access-list-entry", ("access_list_entry", EsAcl.Accesses.Access.AccessListEntries.AccessListEntry))])
                    self._leafs = OrderedDict()

                    self.access_list_entry = YList(self)
                    self._segment_path = lambda: "access-list-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EsAcl.Accesses.Access.AccessListEntries, [], name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or anAccess List Entry to match against
                    
                    .. attribute:: sequence_number  (key)
                    
                    	Sequence number of access list entry
                    	**type**\: int
                    
                    	**range:** 1..2147483646
                    
                    .. attribute:: grant
                    
                    	Forwarding action for the packet. This is required for any non\-remark ACE. Leave unspecified otherwise
                    	**type**\:  :py:class:`EsAclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAclGrantEnum>`
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:  :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:  :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg.EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: vlan1
                    
                    	This 12\-bit VLAN\-ID in the VLAN Tag header uniquely identifies the VLAN. It can be used for the lower bound (in range) or single value. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..4095
                    
                    .. attribute:: vlan2
                    
                    	This 12 bit VLAN\-ID in the VLAN Tag header uniquely identifies the VLAN. It is used in the upper bound (in range). Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..4095
                    
                    .. attribute:: cos
                    
                    	Class of Service value. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: dei
                    
                    	Discard Eligibility Indication bit. User can specify 1 to indicate the bit is set. Leave unspecified otherwise
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: inner_vlan1
                    
                    	This represents the QinQ vlan identifier. It can be used for the lower bound (in range) or single value. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..4095
                    
                    .. attribute:: inner_vlan2
                    
                    	This represents the QinQ vlan identifier. It is used in the upper bound (in range). Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..4095
                    
                    .. attribute:: inner_cos
                    
                    	Class of Service of Inner Header. Range from 0 to 7. Any value beyond this range will be rejected by ACL verifier
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: inner_dei
                    
                    	Class of Service of Inner Header. Any value not in the permissible range will be rejected
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: remark
                    
                    	Description for the access\-list\-entry/rule
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: ether_type_number
                    
                    	Ethernet type Number in Hex. Any value not in the permissible range will be rejected
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,4}
                    
                    .. attribute:: capture
                    
                    	Enable capture if set to TRUE
                    	**type**\: bool
                    
                    .. attribute:: log_option
                    
                    	Log the packet on this access\-list\-entry/rule. User can specify 1 to enable logging the match, leave unspecified otherwise
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: sequence_str
                    
                    	Sequence String for the ace
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'es-acl-cfg'
                    _revision = '2018-02-26'

                    def __init__(self):
                        super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_number']
                        self._child_classes = OrderedDict([("source-network", ("source_network", EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork)), ("destination-network", ("destination_network", EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork))])
                        self._leafs = OrderedDict([
                            ('sequence_number', (YLeaf(YType.uint32, 'sequence-number'), ['int'])),
                            ('grant', (YLeaf(YType.enumeration, 'grant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_es_acl_cfg', 'EsAclGrantEnum', '')])),
                            ('vlan1', (YLeaf(YType.uint32, 'vlan1'), ['int'])),
                            ('vlan2', (YLeaf(YType.uint32, 'vlan2'), ['int'])),
                            ('cos', (YLeaf(YType.uint32, 'cos'), ['int'])),
                            ('dei', (YLeaf(YType.uint32, 'dei'), ['int'])),
                            ('inner_vlan1', (YLeaf(YType.uint32, 'inner-vlan1'), ['int'])),
                            ('inner_vlan2', (YLeaf(YType.uint32, 'inner-vlan2'), ['int'])),
                            ('inner_cos', (YLeaf(YType.uint32, 'inner-cos'), ['int'])),
                            ('inner_dei', (YLeaf(YType.uint32, 'inner-dei'), ['int'])),
                            ('remark', (YLeaf(YType.str, 'remark'), ['str'])),
                            ('ether_type_number', (YLeaf(YType.str, 'ether-type-number'), ['str'])),
                            ('capture', (YLeaf(YType.boolean, 'capture'), ['bool'])),
                            ('log_option', (YLeaf(YType.uint32, 'log-option'), ['int'])),
                            ('sequence_str', (YLeaf(YType.str, 'sequence-str'), ['str'])),
                        ])
                        self.sequence_number = None
                        self.grant = None
                        self.vlan1 = None
                        self.vlan2 = None
                        self.cos = None
                        self.dei = None
                        self.inner_vlan1 = None
                        self.inner_vlan2 = None
                        self.inner_cos = None
                        self.inner_dei = None
                        self.remark = None
                        self.ether_type_number = None
                        self.capture = None
                        self.log_option = None
                        self.sequence_str = None

                        self.source_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"

                        self.destination_network = EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"
                        self._segment_path = lambda: "access-list-entry" + "[sequence-number='" + str(self.sequence_number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry, ['sequence_number', 'grant', 'vlan1', 'vlan2', 'cos', 'dei', 'inner_vlan1', 'inner_vlan2', 'inner_cos', 'inner_dei', 'remark', 'ether_type_number', 'capture', 'log_option', 'sequence_str'], name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source address to match, leave unspecified for any
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source address (if specified), leave unspecified for no wildcarding
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2018-02-26'

                        def __init__(self):
                            super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('source_wild_card_bits', (YLeaf(YType.str, 'source-wild-card-bits'), ['str'])),
                            ])
                            self.source_address = None
                            self.source_wild_card_bits = None
                            self._segment_path = lambda: "source-network"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, ['source_address', 'source_wild_card_bits'], name, value)


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination address to match (if a protocol was specified), leave unspecified for any
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination address (if specified), leave unspecified for no wildcarding
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{1,4}(\\.[0\-9a\-fA\-F]{1,4}){2})
                        
                        

                        """

                        _prefix = 'es-acl-cfg'
                        _revision = '2018-02-26'

                        def __init__(self):
                            super(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ('destination_wild_card_bits', (YLeaf(YType.str, 'destination-wild-card-bits'), ['str'])),
                            ])
                            self.destination_address = None
                            self.destination_wild_card_bits = None
                            self._segment_path = lambda: "destination-network"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EsAcl.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, ['destination_address', 'destination_wild_card_bits'], name, value)

    def clone_ptr(self):
        self._top_entity = EsAcl()
        return self._top_entity

