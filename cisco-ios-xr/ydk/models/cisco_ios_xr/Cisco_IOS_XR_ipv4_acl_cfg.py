""" Cisco_IOS_XR_ipv4_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-acl package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-acl\-and\-prefix\-list\: IPv4 ACL configuration data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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

    .. data:: none_next_hop = 0

    	None next-hop.

    .. data:: regular_next_hop = 1

    	Regular next-hop.

    .. data:: default_next_hop = 2

    	Default next-hop.

    """

    none_next_hop = Enum.YLeaf(0, "none-next-hop")

    regular_next_hop = Enum.YLeaf(1, "regular-next-hop")

    default_next_hop = Enum.YLeaf(2, "default-next-hop")



class Ipv4AclAndPrefixList(Entity):
    """
    IPv4 ACL configuration data
    
    .. attribute:: accesses
    
    	Table of access lists.  Entries in this table and the AccessListExistenceTable table must be kept consistent
    	**type**\:  :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses>`
    
    .. attribute:: prefixes
    
    	Table of ACL prefix lists.  Entries in this table and the PrefixListExistenceTable table must be kept consistent
    	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes>`
    
    .. attribute:: log_update
    
    	Control access lists log updates
    	**type**\:  :py:class:`LogUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.LogUpdate>`
    
    

    """

    _prefix = 'ipv4-acl-cfg'
    _revision = '2017-06-08'

    def __init__(self):
        super(Ipv4AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-acl-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("accesses", ("accesses", Ipv4AclAndPrefixList.Accesses)), ("prefixes", ("prefixes", Ipv4AclAndPrefixList.Prefixes)), ("log-update", ("log_update", Ipv4AclAndPrefixList.LogUpdate))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.accesses = Ipv4AclAndPrefixList.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._children_yang_names.add("accesses")

        self.prefixes = Ipv4AclAndPrefixList.Prefixes()
        self.prefixes.parent = self
        self._children_name_map["prefixes"] = "prefixes"
        self._children_yang_names.add("prefixes")

        self.log_update = Ipv4AclAndPrefixList.LogUpdate()
        self.log_update.parent = self
        self._children_name_map["log_update"] = "log-update"
        self._children_yang_names.add("log-update")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list"


    class Accesses(Entity):
        """
        Table of access lists.  Entries in this table
        and the AccessListExistenceTable table must be
        kept consistent
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of  		 :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access>`
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2017-06-08'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("access", ("access", Ipv4AclAndPrefixList.Accesses.Access))])
            self._leafs = OrderedDict()

            self.access = YList(self)
            self._segment_path = lambda: "accesses"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4AclAndPrefixList.Accesses, [], name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: access_list_name  (key)
            
            	Access list name \- 64 characters max
            	**type**\: str
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of ACEs
            	**type**\:  :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'ipv4-acl-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['access_list_name']
                self._child_container_classes = OrderedDict([("access-list-entries", ("access_list_entries", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('access_list_name', YLeaf(YType.str, 'access-list-name')),
                ])
                self.access_list_name = None

                self.access_list_entries = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self
                self._children_name_map["access_list_entries"] = "access-list-entries"
                self._children_yang_names.add("access-list-entries")
                self._segment_path = lambda: "access" + "[access-list-name='" + str(self.access_list_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/accesses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access, ['access_list_name'], name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of ACEs
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or an ACE to match against
                	**type**\: list of  		 :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'ipv4-acl-cfg'
                _revision = '2017-06-08'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries, self).__init__()

                    self.yang_name = "access-list-entries"
                    self.yang_parent_name = "access"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("access-list-entry", ("access_list_entry", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry))])
                    self._leafs = OrderedDict()

                    self.access_list_entry = YList(self)
                    self._segment_path = lambda: "access-list-entries"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries, [], name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or an ACE to match against
                    
                    .. attribute:: sequence_number  (key)
                    
                    	Sequence number for this entry
                    	**type**\: int
                    
                    	**range:** 1..2147483643
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the  ACE
                    	**type**\:  :py:class:`Ipv4AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclGrantEnum>`
                    
                    .. attribute:: protocol_operator
                    
                    	Protocol operator. Leave unspecified if no protocol comparison is to be done
                    	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                    
                    .. attribute:: protocol
                    
                    	Protocol to match
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv4AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclProtocolNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..255
                    
                    .. attribute:: protocol2
                    
                    	Protocol2 to match
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv4AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclProtocolNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..255
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:  :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:  :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: source_port
                    
                    	Source port settings
                    	**type**\:  :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort>`
                    
                    .. attribute:: destination_port
                    
                    	Destination port settings
                    	**type**\:  :py:class:`DestinationPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort>`
                    
                    .. attribute:: icmp
                    
                    	ICMP settings
                    	**type**\:  :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp>`
                    
                    .. attribute:: tcp
                    
                    	TCP settings
                    	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp>`
                    
                    .. attribute:: packet_length
                    
                    	Packet length settings
                    	**type**\:  :py:class:`PacketLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength>`
                    
                    .. attribute:: time_to_live
                    
                    	TTL settings
                    	**type**\:  :py:class:`TimeToLive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive>`
                    
                    .. attribute:: fragment_offset
                    
                    	Fragment\-offset settings
                    	**type**\:  :py:class:`FragmentOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset>`
                    
                    .. attribute:: fragment_type
                    
                    	Fragment flags, such as dont\-fragment, is\-fragment, first\-fragment, and last\-fragment
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv4AclFragFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclFragFlags>`
                    
                    		**type**\: int
                    
                    			**range:** 1..9
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop settings
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop>`
                    
                    .. attribute:: counter_name
                    
                    	Counter name
                    	**type**\: str
                    
                    .. attribute:: igmp_message_type
                    
                    	IGMP message type to match. Leave unspecified if  no message type comparison is to be done
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv4AclIgmpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclIgmpNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..255
                    
                    .. attribute:: dscp
                    
                    	DSCP settings
                    	**type**\:  :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value to match (if a protocol was  specified), leave unspecified if precedence  comparion is not to be performed
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`Ipv4AclPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPrecedenceNumber>`
                    
                    		**type**\: int
                    
                    			**range:** 0..7
                    
                    .. attribute:: log_option
                    
                    	Whether and how to log matches against this  entry
                    	**type**\:  :py:class:`Ipv4AclLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclLoggingEnum>`
                    
                    .. attribute:: capture
                    
                    	Enable capture
                    	**type**\: bool
                    
                    .. attribute:: icmp_off
                    
                    	To turn off ICMP generation for deny ACEs
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: qos_group
                    
                    	Set qos\-group number
                    	**type**\: int
                    
                    	**range:** 0..512
                    
                    .. attribute:: set_ttl
                    
                    	Set TTL Value. Ranges from 0\-255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: fragments
                    
                    	Check non\-initial fragments. Item is mutually  exclusive with TCP, SCTP, UDP, IGMP and ICMP  comparions and with logging
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the access list
                    	**type**\: str
                    
                    .. attribute:: source_prefix_group
                    
                    	IPv4 source network object group name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: destination_prefix_group
                    
                    	IPv4 destination network object group name
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
                    
                    	Sequence String for the ace
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-acl-cfg'
                    _revision = '2017-06-08'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_number']
                        self._child_container_classes = OrderedDict([("source-network", ("source_network", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork)), ("destination-network", ("destination_network", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork)), ("source-port", ("source_port", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort)), ("destination-port", ("destination_port", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort)), ("icmp", ("icmp", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp)), ("tcp", ("tcp", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp)), ("packet-length", ("packet_length", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength)), ("time-to-live", ("time_to_live", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive)), ("fragment-offset", ("fragment_offset", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset)), ("next-hop", ("next_hop", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop)), ("dscp", ("dscp", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sequence_number', YLeaf(YType.uint32, 'sequence-number')),
                            ('grant', YLeaf(YType.enumeration, 'grant')),
                            ('protocol_operator', YLeaf(YType.enumeration, 'protocol-operator')),
                            ('protocol', YLeaf(YType.str, 'protocol')),
                            ('protocol2', YLeaf(YType.str, 'protocol2')),
                            ('fragment_type', YLeaf(YType.str, 'fragment-type')),
                            ('counter_name', YLeaf(YType.str, 'counter-name')),
                            ('igmp_message_type', YLeaf(YType.str, 'igmp-message-type')),
                            ('precedence', YLeaf(YType.str, 'precedence')),
                            ('log_option', YLeaf(YType.enumeration, 'log-option')),
                            ('capture', YLeaf(YType.boolean, 'capture')),
                            ('icmp_off', YLeaf(YType.empty, 'icmp-off')),
                            ('qos_group', YLeaf(YType.uint32, 'qos-group')),
                            ('set_ttl', YLeaf(YType.uint32, 'set-ttl')),
                            ('fragments', YLeaf(YType.empty, 'fragments')),
                            ('remark', YLeaf(YType.str, 'remark')),
                            ('source_prefix_group', YLeaf(YType.str, 'source-prefix-group')),
                            ('destination_prefix_group', YLeaf(YType.str, 'destination-prefix-group')),
                            ('source_port_group', YLeaf(YType.str, 'source-port-group')),
                            ('destination_port_group', YLeaf(YType.str, 'destination-port-group')),
                            ('sequence_str', YLeaf(YType.str, 'sequence-str')),
                        ])
                        self.sequence_number = None
                        self.grant = None
                        self.protocol_operator = None
                        self.protocol = None
                        self.protocol2 = None
                        self.fragment_type = None
                        self.counter_name = None
                        self.igmp_message_type = None
                        self.precedence = None
                        self.log_option = None
                        self.capture = None
                        self.icmp_off = None
                        self.qos_group = None
                        self.set_ttl = None
                        self.fragments = None
                        self.remark = None
                        self.source_prefix_group = None
                        self.destination_prefix_group = None
                        self.source_port_group = None
                        self.destination_port_group = None
                        self.sequence_str = None

                        self.source_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"
                        self._children_yang_names.add("source-network")

                        self.destination_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"
                        self._children_yang_names.add("destination-network")

                        self.source_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                        self.source_port.parent = self
                        self._children_name_map["source_port"] = "source-port"
                        self._children_yang_names.add("source-port")

                        self.destination_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                        self.destination_port.parent = self
                        self._children_name_map["destination_port"] = "destination-port"
                        self._children_yang_names.add("destination-port")

                        self.icmp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"
                        self._children_yang_names.add("icmp")

                        self.tcp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                        self._children_yang_names.add("tcp")

                        self.packet_length = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                        self.packet_length.parent = self
                        self._children_name_map["packet_length"] = "packet-length"
                        self._children_yang_names.add("packet-length")

                        self.time_to_live = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                        self.time_to_live.parent = self
                        self._children_name_map["time_to_live"] = "time-to-live"
                        self._children_yang_names.add("time-to-live")

                        self.fragment_offset = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset()
                        self.fragment_offset.parent = self
                        self._children_name_map["fragment_offset"] = "fragment-offset"
                        self._children_yang_names.add("fragment-offset")

                        self.next_hop = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")

                        self.dscp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp()
                        self.dscp.parent = self
                        self._children_name_map["dscp"] = "dscp"
                        self._children_yang_names.add("dscp")
                        self._segment_path = lambda: "access-list-entry" + "[sequence-number='" + str(self.sequence_number) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, ['sequence_number', 'grant', 'protocol_operator', 'protocol', 'protocol2', 'fragment_type', 'counter_name', 'igmp_message_type', 'precedence', 'log_option', 'capture', 'icmp_off', 'qos_group', 'set_ttl', 'fragments', 'remark', 'source_prefix_group', 'destination_prefix_group', 'source_port_group', 'destination_port_group', 'sequence_str'], name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source IPv4 address to match, leave unspecified for any
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source address  (if specified), leave unspecified for no  wildcarding
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_prefix_length
                        
                        	Prefix length to apply to source address  (if specified), leave unspecified for no  wildcarding
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', YLeaf(YType.str, 'source-address')),
                                ('source_wild_card_bits', YLeaf(YType.str, 'source-wild-card-bits')),
                                ('source_prefix_length', YLeaf(YType.uint8, 'source-prefix-length')),
                            ])
                            self.source_address = None
                            self.source_wild_card_bits = None
                            self.source_prefix_length = None
                            self._segment_path = lambda: "source-network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, ['source_address', 'source_wild_card_bits', 'source_prefix_length'], name, value)


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination IPv4 address to match (if a protocol was specified), leave unspecified for any
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination address (if specified), leave unspecified for no  wildcarding
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_prefix_length
                        
                        	Prefix length to apply to destination address  (if specified), leave unspecified for no  wildcarding
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_address', YLeaf(YType.str, 'destination-address')),
                                ('destination_wild_card_bits', YLeaf(YType.str, 'destination-wild-card-bits')),
                                ('destination_prefix_length', YLeaf(YType.uint8, 'destination-prefix-length')),
                            ])
                            self.destination_address = None
                            self.destination_wild_card_bits = None
                            self.destination_prefix_length = None
                            self._segment_path = lambda: "destination-network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, ['destination_address', 'destination_wild_card_bits', 'destination_prefix_length'], name, value)


                    class SourcePort(Entity):
                        """
                        Source port settings.
                        
                        .. attribute:: source_operator
                        
                        	Source comparison operator . Leave unspecified  if no source port comparison is to be done
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: first_source_port
                        
                        	First source port for comparison, leave  unspecified if source port comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: second_source_port
                        
                        	Second source port for comparion, leave  unspecified if source port comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__init__()

                            self.yang_name = "source-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_operator', YLeaf(YType.enumeration, 'source-operator')),
                                ('first_source_port', YLeaf(YType.str, 'first-source-port')),
                                ('second_source_port', YLeaf(YType.str, 'second-source-port')),
                            ])
                            self.source_operator = None
                            self.first_source_port = None
                            self.second_source_port = None
                            self._segment_path = lambda: "source-port"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, ['source_operator', 'first_source_port', 'second_source_port'], name, value)


                    class DestinationPort(Entity):
                        """
                        Destination port settings.
                        
                        .. attribute:: destination_operator
                        
                        	Destination comparison operator. Leave  unspecified if no destination port comparison is to be done
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: first_destination_port
                        
                        	First destination port for comparison, leave unspecified if destination port comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        .. attribute:: second_destination_port
                        
                        	Second destination port for comparion, leave unspecified if destination port comparison is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__init__()

                            self.yang_name = "destination-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_operator', YLeaf(YType.enumeration, 'destination-operator')),
                                ('first_destination_port', YLeaf(YType.str, 'first-destination-port')),
                                ('second_destination_port', YLeaf(YType.str, 'second-destination-port')),
                            ])
                            self.destination_operator = None
                            self.first_destination_port = None
                            self.second_destination_port = None
                            self._segment_path = lambda: "destination-port"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, ['destination_operator', 'first_destination_port', 'second_destination_port'], name, value)


                    class Icmp(Entity):
                        """
                        ICMP settings.
                        
                        .. attribute:: icmp_type_code
                        
                        	Well known ICMP message code types to match,  leave unspecified if ICMP message code type  comparion is not to be performed
                        	**type**\:  :py:class:`Ipv4AclIcmpTypeCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclIcmpTypeCodeEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('icmp_type_code', YLeaf(YType.enumeration, 'icmp-type-code')),
                            ])
                            self.icmp_type_code = None
                            self._segment_path = lambda: "icmp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, ['icmp_type_code'], name, value)


                    class Tcp(Entity):
                        """
                        TCP settings.
                        
                        .. attribute:: tcp_bits_match_operator
                        
                        	TCP Bits match operator. Leave unspecified if  flexible comparison of TCP bits is not  required
                        	**type**\:  :py:class:`Ipv4AclTcpMatchOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpMatchOperatorEnum>`
                        
                        .. attribute:: tcp_bits
                        
                        	TCP bits to match. Leave unspecified if comparison of TCP bits is not required
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpBitsNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        .. attribute:: tcp_bits_mask
                        
                        	TCP bits mask to use for flexible TCP matching. Leave unspecified if tcp\-bits\-match\-operator is  unspecified
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpBitsNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__init__()

                            self.yang_name = "tcp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('tcp_bits_match_operator', YLeaf(YType.enumeration, 'tcp-bits-match-operator')),
                                ('tcp_bits', YLeaf(YType.str, 'tcp-bits')),
                                ('tcp_bits_mask', YLeaf(YType.str, 'tcp-bits-mask')),
                            ])
                            self.tcp_bits_match_operator = None
                            self.tcp_bits = None
                            self.tcp_bits_mask = None
                            self._segment_path = lambda: "tcp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, ['tcp_bits_match_operator', 'tcp_bits', 'tcp_bits_mask'], name, value)


                    class PacketLength(Entity):
                        """
                        Packet length settings.
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator applicable if Packet  length is to be compared. Leave unspecified if  no packet length comparison is to be done
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: packet_length_min
                        
                        	Minimum packet length for comparison, leave  unspecified if packet length comparison is not  to be performed or if only the maximum packet  length should be considered
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_max
                        
                        	Maximum packet length for comparion, leave  unspecified if packet length comparison is not  to be performed or if only the minimum packet  length should be considered
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__init__()

                            self.yang_name = "packet-length"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packet_length_operator', YLeaf(YType.enumeration, 'packet-length-operator')),
                                ('packet_length_min', YLeaf(YType.uint32, 'packet-length-min')),
                                ('packet_length_max', YLeaf(YType.uint32, 'packet-length-max')),
                            ])
                            self.packet_length_operator = None
                            self.packet_length_min = None
                            self.packet_length_max = None
                            self._segment_path = lambda: "packet-length"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, ['packet_length_operator', 'packet_length_min', 'packet_length_max'], name, value)


                    class TimeToLive(Entity):
                        """
                        TTL settings.
                        
                        .. attribute:: time_to_live_operator
                        
                        	TTL operator is applicable if TTL is to be  compared. Leave unspecified if TTL  classification is not required
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: time_to_live_min
                        
                        	TTL value for comparison OR Minimum TTL value  for TTL range comparision, leave unspecified if  TTL classification is not required
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_max
                        
                        	Maximum TTL for comparion, leave unspecified if  TTL comparison is not to be performed or if only the minimum TTL should be considered
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__init__()

                            self.yang_name = "time-to-live"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('time_to_live_operator', YLeaf(YType.enumeration, 'time-to-live-operator')),
                                ('time_to_live_min', YLeaf(YType.uint32, 'time-to-live-min')),
                                ('time_to_live_max', YLeaf(YType.uint32, 'time-to-live-max')),
                            ])
                            self.time_to_live_operator = None
                            self.time_to_live_min = None
                            self.time_to_live_max = None
                            self._segment_path = lambda: "time-to-live"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, ['time_to_live_operator', 'time_to_live_min', 'time_to_live_max'], name, value)


                    class FragmentOffset(Entity):
                        """
                        Fragment\-offset settings.
                        
                        .. attribute:: fragment_offset_operator
                        
                        	Fragment\-offset operator is applicable if fragment\-offset is to be compared. Leave unspecified if fragment\-offset classification is not required
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: fragment_offset_1
                        
                        	Fragment\-offset value for comparison OR first fragment\-offset value for fragment\-offset range comparision, leave unspecified if fragment\-offset classification is not required
                        	**type**\: int
                        
                        	**range:** 0..8191
                        
                        .. attribute:: fragment_offset_2
                        
                        	Second fragment\-offset value for comparion, leave unspecified if fragment\-offset comparison is not to be performed or if only the first fragment\-offset value should be considered
                        	**type**\: int
                        
                        	**range:** 0..8191
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset, self).__init__()

                            self.yang_name = "fragment-offset"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('fragment_offset_operator', YLeaf(YType.enumeration, 'fragment-offset-operator')),
                                ('fragment_offset_1', YLeaf(YType.uint32, 'fragment-offset-1')),
                                ('fragment_offset_2', YLeaf(YType.uint32, 'fragment-offset-2')),
                            ])
                            self.fragment_offset_operator = None
                            self.fragment_offset_1 = None
                            self.fragment_offset_2 = None
                            self._segment_path = lambda: "fragment-offset"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset, ['fragment_offset_operator', 'fragment_offset_1', 'fragment_offset_2'], name, value)


                    class NextHop(Entity):
                        """
                        Next\-hop settings.
                        
                        .. attribute:: next_hop_type
                        
                        	The nexthop type
                        	**type**\:  :py:class:`NextHopType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.NextHopType>`
                        
                        .. attribute:: next_hop_1
                        
                        	The first next\-hop settings
                        	**type**\:  :py:class:`NextHop1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1>`
                        
                        .. attribute:: next_hop_2
                        
                        	The second next\-hop settings
                        	**type**\:  :py:class:`NextHop2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2>`
                        
                        .. attribute:: next_hop_3
                        
                        	The third next\-hop settings
                        	**type**\:  :py:class:`NextHop3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("next-hop-1", ("next_hop_1", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1)), ("next-hop-2", ("next_hop_2", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2)), ("next-hop-3", ("next_hop_3", Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop_type', YLeaf(YType.enumeration, 'next-hop-type')),
                            ])
                            self.next_hop_type = None

                            self.next_hop_1 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1()
                            self.next_hop_1.parent = self
                            self._children_name_map["next_hop_1"] = "next-hop-1"
                            self._children_yang_names.add("next-hop-1")

                            self.next_hop_2 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2()
                            self.next_hop_2.parent = self
                            self._children_name_map["next_hop_2"] = "next-hop-2"
                            self._children_yang_names.add("next-hop-2")

                            self.next_hop_3 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3()
                            self.next_hop_3.parent = self
                            self._children_name_map["next_hop_3"] = "next-hop-3"
                            self._children_yang_names.add("next-hop-3")
                            self._segment_path = lambda: "next-hop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, ['next_hop_type'], name, value)


                        class NextHop1(Entity):
                            """
                            The first next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2017-06-08'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__init__()

                                self.yang_name = "next-hop-1"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('track_name', YLeaf(YType.str, 'track-name')),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-1"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, ['next_hop', 'vrf_name', 'track_name'], name, value)


                        class NextHop2(Entity):
                            """
                            The second next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2017-06-08'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__init__()

                                self.yang_name = "next-hop-2"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('track_name', YLeaf(YType.str, 'track-name')),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-2"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, ['next_hop', 'vrf_name', 'track_name'], name, value)


                        class NextHop3(Entity):
                            """
                            The third next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\: str
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2017-06-08'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__init__()

                                self.yang_name = "next-hop-3"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                                    ('track_name', YLeaf(YType.str, 'track-name')),
                                ])
                                self.next_hop = None
                                self.vrf_name = None
                                self.track_name = None
                                self._segment_path = lambda: "next-hop-3"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, ['next_hop', 'vrf_name', 'track_name'], name, value)


                    class Dscp(Entity):
                        """
                        DSCP settings.
                        
                        .. attribute:: dscp_operator
                        
                        	DSCP operator is applicable only when DSCP  range is configured. Leave unspecified if  DSCP range is not required
                        	**type**\:  :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: dscp_min
                        
                        	DSCP value to match or minimum DSCP value  for DSCP range comparison, leave unspecified  if DSCP comparion is not to be performed
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclDscpNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        .. attribute:: dscp_max
                        
                        	Maximum DSCP value for comparion, leave  unspecified if DSCP comparison is not to  be performed or if only the minimum DSCP should be considered
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`Ipv4AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclDscpNumber>`
                        
                        		**type**\: int
                        
                        			**range:** 0..63
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2017-06-08'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp, self).__init__()

                            self.yang_name = "dscp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('dscp_operator', YLeaf(YType.enumeration, 'dscp-operator')),
                                ('dscp_min', YLeaf(YType.str, 'dscp-min')),
                                ('dscp_max', YLeaf(YType.str, 'dscp-max')),
                            ])
                            self.dscp_operator = None
                            self.dscp_min = None
                            self.dscp_max = None
                            self._segment_path = lambda: "dscp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp, ['dscp_operator', 'dscp_min', 'dscp_max'], name, value)


    class Prefixes(Entity):
        """
        Table of ACL prefix lists.  Entries in this
        table and the PrefixListExistenceTable table
        must be kept consistent
        
        .. attribute:: prefix
        
        	Name of a prefix list
        	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix>`
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2017-06-08'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Prefixes, self).__init__()

            self.yang_name = "prefixes"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("prefix", ("prefix", Ipv4AclAndPrefixList.Prefixes.Prefix))])
            self._leafs = OrderedDict()

            self.prefix = YList(self)
            self._segment_path = lambda: "prefixes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4AclAndPrefixList.Prefixes, [], name, value)


        class Prefix(Entity):
            """
            Name of a prefix list
            
            .. attribute:: prefix_list_name  (key)
            
            	Prefix list name \- max 32 characters
            	**type**\: str
            
            .. attribute:: prefix_list_entries
            
            	Sequence of entries forming a prefix list
            	**type**\:  :py:class:`PrefixListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-acl-cfg'
            _revision = '2017-06-08'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Prefixes.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "prefixes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['prefix_list_name']
                self._child_container_classes = OrderedDict([("prefix-list-entries", ("prefix_list_entries", Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('prefix_list_name', YLeaf(YType.str, 'prefix-list-name')),
                ])
                self.prefix_list_name = None

                self.prefix_list_entries = None
                self._children_name_map["prefix_list_entries"] = "prefix-list-entries"
                self._children_yang_names.add("prefix-list-entries")
                self._segment_path = lambda: "prefix" + "[prefix-list-name='" + str(self.prefix_list_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/prefixes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4AclAndPrefixList.Prefixes.Prefix, ['prefix_list_name'], name, value)


            class PrefixListEntries(Entity):
                """
                Sequence of entries forming a prefix list
                
                .. attribute:: prefix_list_entry
                
                	A prefix list entry; either a description (remark) or a prefix to match against
                	**type**\: list of  		 :py:class:`PrefixListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-acl-cfg'
                _revision = '2017-06-08'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__init__()

                    self.yang_name = "prefix-list-entries"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("prefix-list-entry", ("prefix_list_entry", Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict()

                    self.prefix_list_entry = YList(self)
                    self._segment_path = lambda: "prefix-list-entries"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, [], name, value)


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
                    	**type**\:  :py:class:`Ipv4AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclGrantEnum>`
                    
                    .. attribute:: prefix
                    
                    	IPv4 address prefix to match
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask
                    
                    	Mask of IPv4 address prefix
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: match_exact_length
                    
                    	Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: exact_prefix_length
                    
                    	If exact prefix length matching specified, set the length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: match_max_length
                    
                    	Set to perform a maximum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: max_prefix_length
                    
                    	If maximum length prefix matching specified, set the maximum length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: match_min_length
                    
                    	Set to perform a minimum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: min_prefix_length
                    
                    	If minimum length prefix matching specified, set the minimum length of prefix to be matched
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the prefix list.  Item is mutually exclusive with all others in the object
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ipv4-acl-cfg'
                    _revision = '2017-06-08'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__init__()

                        self.yang_name = "prefix-list-entry"
                        self.yang_parent_name = "prefix-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sequence_number']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sequence_number', YLeaf(YType.uint32, 'sequence-number')),
                            ('grant', YLeaf(YType.enumeration, 'grant')),
                            ('prefix', YLeaf(YType.str, 'prefix')),
                            ('netmask', YLeaf(YType.str, 'netmask')),
                            ('match_exact_length', YLeaf(YType.empty, 'match-exact-length')),
                            ('exact_prefix_length', YLeaf(YType.uint32, 'exact-prefix-length')),
                            ('match_max_length', YLeaf(YType.empty, 'match-max-length')),
                            ('max_prefix_length', YLeaf(YType.uint32, 'max-prefix-length')),
                            ('match_min_length', YLeaf(YType.empty, 'match-min-length')),
                            ('min_prefix_length', YLeaf(YType.uint32, 'min-prefix-length')),
                            ('remark', YLeaf(YType.str, 'remark')),
                        ])
                        self.sequence_number = None
                        self.grant = None
                        self.prefix = None
                        self.netmask = None
                        self.match_exact_length = None
                        self.exact_prefix_length = None
                        self.match_max_length = None
                        self.max_prefix_length = None
                        self.match_min_length = None
                        self.min_prefix_length = None
                        self.remark = None
                        self._segment_path = lambda: "prefix-list-entry" + "[sequence-number='" + str(self.sequence_number) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, ['sequence_number', 'grant', 'prefix', 'netmask', 'match_exact_length', 'exact_prefix_length', 'match_max_length', 'max_prefix_length', 'match_min_length', 'min_prefix_length', 'remark'], name, value)


    class LogUpdate(Entity):
        """
        Control access lists log updates
        
        .. attribute:: threshold
        
        	Log update threshold (number of hits)
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: rate
        
        	Log update rate (log msgs per second)
        	**type**\: int
        
        	**range:** 1..1000
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2017-06-08'

        def __init__(self):
            super(Ipv4AclAndPrefixList.LogUpdate, self).__init__()

            self.yang_name = "log-update"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('threshold', YLeaf(YType.uint32, 'threshold')),
                ('rate', YLeaf(YType.uint32, 'rate')),
            ])
            self.threshold = None
            self.rate = None
            self._segment_path = lambda: "log-update"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4AclAndPrefixList.LogUpdate, ['threshold', 'rate'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4AclAndPrefixList()
        return self._top_entity

