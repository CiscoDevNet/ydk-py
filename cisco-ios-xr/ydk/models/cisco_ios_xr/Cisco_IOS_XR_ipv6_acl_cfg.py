""" Cisco_IOS_XR_ipv6_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: IPv6 ACL configuration data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NextHopType(Enum):
    """
    NextHopType

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



class Ipv6AclAndPrefixList(Entity):
    """
    IPv6 ACL configuration data
    
    .. attribute:: accesses
    
    	Table of access lists
    	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses>`
    
    .. attribute:: log_update
    
    	Control access lists log updates
    	**type**\:   :py:class:`LogUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.LogUpdate>`
    
    .. attribute:: prefixes
    
    	Table of prefix lists
    	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes>`
    
    

    """

    _prefix = 'ipv6-acl-cfg'
    _revision = '2017-05-11'

    def __init__(self):
        super(Ipv6AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-acl-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"accesses" : ("accesses", Ipv6AclAndPrefixList.Accesses), "log-update" : ("log_update", Ipv6AclAndPrefixList.LogUpdate), "prefixes" : ("prefixes", Ipv6AclAndPrefixList.Prefixes)}
        self._child_list_classes = {}

        self.accesses = Ipv6AclAndPrefixList.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._children_yang_names.add("accesses")

        self.log_update = Ipv6AclAndPrefixList.LogUpdate()
        self.log_update.parent = self
        self._children_name_map["log_update"] = "log-update"
        self._children_yang_names.add("log-update")

        self.prefixes = Ipv6AclAndPrefixList.Prefixes()
        self.prefixes.parent = self
        self._children_name_map["prefixes"] = "prefixes"
        self._children_yang_names.add("prefixes")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list"


    class Accesses(Entity):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2017-05-11'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"access" : ("access", Ipv6AclAndPrefixList.Accesses.Access)}

            self.access = YList(self)
            self._segment_path = lambda: "accesses"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.Accesses, [], name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: name  <key>
            
            	Name of the access list
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of access list entries
            	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'ipv6-acl-cfg'
            _revision = '2017-05-11'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"access-list-entries" : ("access_list_entries", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.access_list_entries = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self
                self._children_name_map["access_list_entries"] = "access-list-entries"
                self._children_yang_names.add("access-list-entries")
                self._segment_path = lambda: "access" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/accesses/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access, ['name'], name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2017-05-11'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries, self).__init__()

                    self.yang_name = "access-list-entries"
                    self.yang_parent_name = "access"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"access-list-entry" : ("access_list_entry", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry)}

                    self.access_list_entry = YList(self)
                    self._segment_path = lambda: "access-list-entries"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries, [], name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or anAccess List Entry to match against
                    
                    .. attribute:: sequence_number  <key>
                    
                    	Sequence number of access list entry
                    	**type**\:  int
                    
                    	**range:** 1..2147483643
                    
                    .. attribute:: capture
                    
                    	Enable capture
                    	**type**\:  bool
                    
                    .. attribute:: counter_name
                    
                    	Counter name
                    	**type**\:  str
                    
                    .. attribute:: destination_network
                    
                    	Destination network settings
                    	**type**\:   :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: destination_port
                    
                    	Destination port settings
                    	**type**\:   :py:class:`DestinationPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort>`
                    
                    .. attribute:: destination_port_group
                    
                    	Destination port object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: destination_prefix_group
                    
                    	IPv6 destination network object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: dscp
                    
                    	DSCP value to match (if a protocol was specified), leave unspecified if DSCP comparion is not to be performed
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclDscpNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..64
                    
                    
                    ----
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the  ACE
                    	**type**\:   :py:class:`Ipv6AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnum>`
                    
                    .. attribute:: header_flags
                    
                    	Match if header\-flag is present
                    	**type**\:   :py:class:`HeaderFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags>`
                    
                    .. attribute:: icmp
                    
                    	ICMP settings
                    	**type**\:   :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp>`
                    
                    .. attribute:: icmp_off
                    
                    	To turn off ICMP generation for deny ACEs
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: log_option
                    
                    	Whether and how to log matches against this  entry
                    	**type**\:   :py:class:`Ipv6AclLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclLoggingEnum>`
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop settings
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop>`
                    
                    .. attribute:: packet_length
                    
                    	Packet length settings
                    	**type**\:   :py:class:`PacketLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value to match (if a protocol was  specified), leave unspecified if precedence  comparion is not to be performed
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPrecedenceNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    .. attribute:: protocol
                    
                    	Protocol to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol2
                    
                    	Protocol2 to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol_operator
                    
                    	Protocol operator. Leave unspecified if no protocol comparison is to be done
                    	**type**\:   :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                    
                    .. attribute:: qos_group
                    
                    	Set qos\-group number
                    	**type**\:  int
                    
                    	**range:** 0..512
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the access list
                    	**type**\:  str
                    
                    .. attribute:: sequence_str
                    
                    	Sequence String for the ace
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: set_ttl
                    
                    	Set TTL Value. Ranges from 0\-255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:   :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: source_port
                    
                    	Source port settings
                    	**type**\:   :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort>`
                    
                    .. attribute:: source_port_group
                    
                    	Source port object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: source_prefix_group
                    
                    	IPv6 source network object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: tcp
                    
                    	TCP settings
                    	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp>`
                    
                    .. attribute:: time_to_live
                    
                    	TTL settings
                    	**type**\:   :py:class:`TimeToLive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive>`
                    
                    .. attribute:: undetermined_transport
                    
                    	Enable undetermined\-transport
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv6-acl-cfg'
                    _revision = '2017-05-11'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"destination-network" : ("destination_network", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork), "destination-port" : ("destination_port", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort), "header-flags" : ("header_flags", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags), "icmp" : ("icmp", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp), "next-hop" : ("next_hop", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop), "packet-length" : ("packet_length", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength), "source-network" : ("source_network", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork), "source-port" : ("source_port", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort), "tcp" : ("tcp", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp), "time-to-live" : ("time_to_live", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive)}
                        self._child_list_classes = {}

                        self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                        self.capture = YLeaf(YType.boolean, "capture")

                        self.counter_name = YLeaf(YType.str, "counter-name")

                        self.destination_port_group = YLeaf(YType.str, "destination-port-group")

                        self.destination_prefix_group = YLeaf(YType.str, "destination-prefix-group")

                        self.dscp = YLeaf(YType.str, "dscp")

                        self.grant = YLeaf(YType.enumeration, "grant")

                        self.icmp_off = YLeaf(YType.empty, "icmp-off")

                        self.log_option = YLeaf(YType.enumeration, "log-option")

                        self.precedence = YLeaf(YType.str, "precedence")

                        self.protocol = YLeaf(YType.str, "protocol")

                        self.protocol2 = YLeaf(YType.str, "protocol2")

                        self.protocol_operator = YLeaf(YType.enumeration, "protocol-operator")

                        self.qos_group = YLeaf(YType.uint32, "qos-group")

                        self.remark = YLeaf(YType.str, "remark")

                        self.sequence_str = YLeaf(YType.str, "sequence-str")

                        self.set_ttl = YLeaf(YType.uint32, "set-ttl")

                        self.source_port_group = YLeaf(YType.str, "source-port-group")

                        self.source_prefix_group = YLeaf(YType.str, "source-prefix-group")

                        self.undetermined_transport = YLeaf(YType.boolean, "undetermined-transport")

                        self.destination_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"
                        self._children_yang_names.add("destination-network")

                        self.destination_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                        self.destination_port.parent = self
                        self._children_name_map["destination_port"] = "destination-port"
                        self._children_yang_names.add("destination-port")

                        self.header_flags = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags()
                        self.header_flags.parent = self
                        self._children_name_map["header_flags"] = "header-flags"
                        self._children_yang_names.add("header-flags")

                        self.icmp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"
                        self._children_yang_names.add("icmp")

                        self.next_hop = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")

                        self.packet_length = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                        self.packet_length.parent = self
                        self._children_name_map["packet_length"] = "packet-length"
                        self._children_yang_names.add("packet-length")

                        self.source_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"
                        self._children_yang_names.add("source-network")

                        self.source_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                        self.source_port.parent = self
                        self._children_name_map["source_port"] = "source-port"
                        self._children_yang_names.add("source-port")

                        self.tcp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                        self._children_yang_names.add("tcp")

                        self.time_to_live = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                        self.time_to_live.parent = self
                        self._children_name_map["time_to_live"] = "time-to-live"
                        self._children_yang_names.add("time-to-live")
                        self._segment_path = lambda: "access-list-entry" + "[sequence-number='" + self.sequence_number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, ['sequence_number', 'capture', 'counter_name', 'destination_port_group', 'destination_prefix_group', 'dscp', 'grant', 'icmp_off', 'log_option', 'precedence', 'protocol', 'protocol2', 'protocol_operator', 'qos_group', 'remark', 'sequence_str', 'set_ttl', 'source_port_group', 'source_prefix_group', 'undetermined_transport'], name, value)


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination IPv6 address, leave unspecified if inputting as IPv6 address with  wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_mask
                        
                        	Destination address mask. Either destination\-wild\-card\-bits or destination\-mask. is supported, not both. Leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination  destination\-address (if specified),  leave unspecified for no wildcarding
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_mask = YLeaf(YType.str, "destination-mask")

                            self.destination_wild_card_bits = YLeaf(YType.uint8, "destination-wild-card-bits")
                            self._segment_path = lambda: "destination-network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, ['destination_address', 'destination_mask', 'destination_wild_card_bits'], name, value)


                    class DestinationPort(Entity):
                        """
                        Destination port settings.
                        
                        .. attribute:: destination_operator
                        
                        	Destination comparison operator. Leave  unspecified if no destination port comparison  is to be done
                        	**type**\:   :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        .. attribute:: first_destination_port
                        
                        	First destination port for comparison, leave  unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_destination_port
                        
                        	Second destination port for comparion, leave  unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__init__()

                            self.yang_name = "destination-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.destination_operator = YLeaf(YType.enumeration, "destination-operator")

                            self.first_destination_port = YLeaf(YType.str, "first-destination-port")

                            self.second_destination_port = YLeaf(YType.str, "second-destination-port")
                            self._segment_path = lambda: "destination-port"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, ['destination_operator', 'first_destination_port', 'second_destination_port'], name, value)


                    class HeaderFlags(Entity):
                        """
                        Match if header\-flag is present.
                        
                        .. attribute:: authen
                        
                        	Match if authen header is present
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: destopts
                        
                        	Match if destops header is present
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: fragments
                        
                        	Match if fragments header is present
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: hop_by_hop
                        
                        	Match if hop\-by\-hop header is present
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: routing
                        
                        	Match if routing header is present
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags, self).__init__()

                            self.yang_name = "header-flags"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.authen = YLeaf(YType.empty, "authen")

                            self.destopts = YLeaf(YType.empty, "destopts")

                            self.fragments = YLeaf(YType.empty, "fragments")

                            self.hop_by_hop = YLeaf(YType.empty, "hop-by-hop")

                            self.routing = YLeaf(YType.empty, "routing")
                            self._segment_path = lambda: "header-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags, ['authen', 'destopts', 'fragments', 'hop_by_hop', 'routing'], name, value)


                    class Icmp(Entity):
                        """
                        ICMP settings.
                        
                        .. attribute:: icmp_type_code
                        
                        	Well known ICMP message code types to match,  leave unspecified if ICMP message code type  comparion is not to be performed
                        	**type**\:   :py:class:`Ipv6AclIcmpTypeCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclIcmpTypeCodeEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.icmp_type_code = YLeaf(YType.enumeration, "icmp-type-code")
                            self._segment_path = lambda: "icmp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, ['icmp_type_code'], name, value)


                    class NextHop(Entity):
                        """
                        Next\-hop settings.
                        
                        .. attribute:: next_hop_1
                        
                        	The first next\-hop settings
                        	**type**\:   :py:class:`NextHop1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1>`
                        
                        .. attribute:: next_hop_2
                        
                        	The second next\-hop settings
                        	**type**\:   :py:class:`NextHop2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2>`
                        
                        .. attribute:: next_hop_3
                        
                        	The third next\-hop settings
                        	**type**\:   :py:class:`NextHop3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3>`
                        
                        .. attribute:: next_hop_type
                        
                        	The nexthop type
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.NextHopType>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"next-hop-1" : ("next_hop_1", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1), "next-hop-2" : ("next_hop_2", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2), "next-hop-3" : ("next_hop_3", Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3)}
                            self._child_list_classes = {}

                            self.next_hop_type = YLeaf(YType.enumeration, "next-hop-type")

                            self.next_hop_1 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1()
                            self.next_hop_1.parent = self
                            self._children_name_map["next_hop_1"] = "next-hop-1"
                            self._children_yang_names.add("next-hop-1")

                            self.next_hop_2 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2()
                            self.next_hop_2.parent = self
                            self._children_name_map["next_hop_2"] = "next-hop-2"
                            self._children_yang_names.add("next-hop-2")

                            self.next_hop_3 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3()
                            self.next_hop_3.parent = self
                            self._children_name_map["next_hop_3"] = "next-hop-3"
                            self._children_yang_names.add("next-hop-3")
                            self._segment_path = lambda: "next-hop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, ['next_hop_type'], name, value)


                        class NextHop1(Entity):
                            """
                            The first next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2017-05-11'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__init__()

                                self.yang_name = "next-hop-1"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "next-hop-1"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, ['next_hop', 'track_name', 'vrf_name'], name, value)


                        class NextHop2(Entity):
                            """
                            The second next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2017-05-11'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__init__()

                                self.yang_name = "next-hop-2"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "next-hop-2"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, ['next_hop', 'track_name', 'vrf_name'], name, value)


                        class NextHop3(Entity):
                            """
                            The third next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv6 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv6-acl-cfg'
                            _revision = '2017-05-11'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__init__()

                                self.yang_name = "next-hop-3"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "next-hop-3"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, ['next_hop', 'track_name', 'vrf_name'], name, value)


                    class PacketLength(Entity):
                        """
                        Packet length settings.
                        
                        .. attribute:: packet_length_max
                        
                        	Maximum packet length for comparion, leave  unspecified if packet length comparison is not to be performed or if only the minimum packet  length should be considered
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_min
                        
                        	Minimum packet length for comparison, leave  unspecified if packet length comparison is not to be performed or if only the maximum packet length should be considered
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator applicable if packet  length is to be compared. Leave unspecified if no Packet length comparison is to be done
                        	**type**\:   :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__init__()

                            self.yang_name = "packet-length"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.packet_length_max = YLeaf(YType.uint32, "packet-length-max")

                            self.packet_length_min = YLeaf(YType.uint32, "packet-length-min")

                            self.packet_length_operator = YLeaf(YType.enumeration, "packet-length-operator")
                            self._segment_path = lambda: "packet-length"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, ['packet_length_max', 'packet_length_min', 'packet_length_operator'], name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source IPv6 address, leave unspecified if inputting as IPv6 address with wildcarding
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_mask
                        
                        	Source address mask. Either source\-wild\-card\-bits or source\-mask is. supported, not both. Leave unspecified. for any
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source\-address (if specified), leave unspecified for no wildcarding
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_mask = YLeaf(YType.str, "source-mask")

                            self.source_wild_card_bits = YLeaf(YType.uint8, "source-wild-card-bits")
                            self._segment_path = lambda: "source-network"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, ['source_address', 'source_mask', 'source_wild_card_bits'], name, value)


                    class SourcePort(Entity):
                        """
                        Source port settings.
                        
                        .. attribute:: first_source_port
                        
                        	First source port for comparison,  leave unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_source_port
                        
                        	Second source port for comparion,  leave unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: source_operator
                        
                        	Source comparison operator. Leave unspecified if no source port comparison is to be done
                        	**type**\:   :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__init__()

                            self.yang_name = "source-port"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.first_source_port = YLeaf(YType.str, "first-source-port")

                            self.second_source_port = YLeaf(YType.str, "second-source-port")

                            self.source_operator = YLeaf(YType.enumeration, "source-operator")
                            self._segment_path = lambda: "source-port"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, ['first_source_port', 'second_source_port', 'source_operator'], name, value)


                    class Tcp(Entity):
                        """
                        TCP settings.
                        
                        .. attribute:: tcp_bits
                        
                        	TCP bits to match. Leave unspecified if  comparison of TCP bits is not required
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_mask
                        
                        	TCP bits mask to use for flexible TCP matching. Leave unspecified if it is not required
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_match_operator
                        
                        	TCP Bits match operator. Leave unspecified if  flexible comparison of TCP bits is not  required
                        	**type**\:   :py:class:`Ipv6AclTcpMatchOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpMatchOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__init__()

                            self.yang_name = "tcp"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.tcp_bits = YLeaf(YType.str, "tcp-bits")

                            self.tcp_bits_mask = YLeaf(YType.str, "tcp-bits-mask")

                            self.tcp_bits_match_operator = YLeaf(YType.enumeration, "tcp-bits-match-operator")
                            self._segment_path = lambda: "tcp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, ['tcp_bits', 'tcp_bits_mask', 'tcp_bits_match_operator'], name, value)


                    class TimeToLive(Entity):
                        """
                        TTL settings.
                        
                        .. attribute:: time_to_live_max
                        
                        	Maximum TTL for comparion, leave unspecified if TTL comparison is not to be performed or if only the minimum TTL should be considered
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_min
                        
                        	TTL value for comparison OR Minimum TTL value  for TTL range comparision, leave unspecified if TTL classification is not required
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_operator
                        
                        	TTL operator is applicable if TTL is to be  compared. Leave unspecified if TTL  classification is not required
                        	**type**\:   :py:class:`Ipv6AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2017-05-11'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__init__()

                            self.yang_name = "time-to-live"
                            self.yang_parent_name = "access-list-entry"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.time_to_live_max = YLeaf(YType.uint32, "time-to-live-max")

                            self.time_to_live_min = YLeaf(YType.uint32, "time-to-live-min")

                            self.time_to_live_operator = YLeaf(YType.enumeration, "time-to-live-operator")
                            self._segment_path = lambda: "time-to-live"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, ['time_to_live_max', 'time_to_live_min', 'time_to_live_operator'], name, value)


    class LogUpdate(Entity):
        """
        Control access lists log updates
        
        .. attribute:: rate
        
        	Log update rate (log messages per second)
        	**type**\:  int
        
        	**range:** 1..1000
        
        .. attribute:: threshold
        
        	Log update threshold (number of hits)
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2017-05-11'

        def __init__(self):
            super(Ipv6AclAndPrefixList.LogUpdate, self).__init__()

            self.yang_name = "log-update"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.rate = YLeaf(YType.uint32, "rate")

            self.threshold = YLeaf(YType.uint32, "threshold")
            self._segment_path = lambda: "log-update"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.LogUpdate, ['rate', 'threshold'], name, value)


    class Prefixes(Entity):
        """
        Table of prefix lists
        
        .. attribute:: prefix
        
        	Name of a prefix list
        	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2017-05-11'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Prefixes, self).__init__()

            self.yang_name = "prefixes"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"prefix" : ("prefix", Ipv6AclAndPrefixList.Prefixes.Prefix)}

            self.prefix = YList(self)
            self._segment_path = lambda: "prefixes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6AclAndPrefixList.Prefixes, [], name, value)


        class Prefix(Entity):
            """
            Name of a prefix list
            
            .. attribute:: name  <key>
            
            	Name of a prefix list
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: prefix_list_entries
            
            	Sequence of entries forming a prefix list
            	**type**\:   :py:class:`PrefixListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv6-acl-cfg'
            _revision = '2017-05-11'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Prefixes.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "prefixes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"prefix-list-entries" : ("prefix_list_entries", Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.prefix_list_entries = None
                self._children_name_map["prefix_list_entries"] = "prefix-list-entries"
                self._children_yang_names.add("prefix-list-entries")
                self._segment_path = lambda: "prefix" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/prefixes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix, ['name'], name, value)


            class PrefixListEntries(Entity):
                """
                Sequence of entries forming a prefix list
                
                .. attribute:: prefix_list_entry
                
                	A prefix list entry; either a description (remark) or a prefix to match against
                	**type**\: list of    :py:class:`PrefixListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2017-05-11'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__init__()

                    self.yang_name = "prefix-list-entries"
                    self.yang_parent_name = "prefix"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"prefix-list-entry" : ("prefix_list_entry", Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry)}
                    self.is_presence_container = True

                    self.prefix_list_entry = YList(self)
                    self._segment_path = lambda: "prefix-list-entries"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, [], name, value)


                class PrefixListEntry(Entity):
                    """
                    A prefix list entry; either a description
                    (remark) or a prefix to match against
                    
                    .. attribute:: sequence_number  <key>
                    
                    	Sequence number of prefix list
                    	**type**\:  int
                    
                    	**range:** 1..2147483646
                    
                    .. attribute:: exact_prefix_length
                    
                    	If exact prefix length matching specified, set the length of prefix to be matched
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the prefix list
                    	**type**\:   :py:class:`Ipv6AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnum>`
                    
                    .. attribute:: ipv6_address_as_string
                    
                    	The IPv6 address if entered  with the ZoneMutually exclusive with Prefix and PrefixMask
                    	**type**\:  str
                    
                    .. attribute:: match_exact_length
                    
                    	Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items
                    	**type**\:   :py:class:`Ipv6PrefixMatchExactLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchExactLength>`
                    
                    .. attribute:: match_max_length
                    
                    	Set to perform a maximum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:   :py:class:`Ipv6PrefixMatchMaxLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMaxLength>`
                    
                    .. attribute:: match_min_length
                    
                    	Set to perform a minimum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:   :py:class:`Ipv6PrefixMatchMinLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMinLength>`
                    
                    .. attribute:: max_prefix_length
                    
                    	If maximum length prefix matching specified, set the maximum length of prefix to be matched
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: min_prefix_length
                    
                    	If minimum length prefix matching specified, set the minimum length of prefix to be matched
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: prefix
                    
                    	IPv6 address prefix to match
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_mask
                    
                    	MaskLength of IPv6 address prefix
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the prefix list.  Item is mutually exclusive with all others in the object
                    	**type**\:  str
                    
                    .. attribute:: zone
                    
                    	IPv6 Zone if entered  with the IPV6AddressMutually exclusive with Prefix and PrefixMask
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ipv6-acl-cfg'
                    _revision = '2017-05-11'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__init__()

                        self.yang_name = "prefix-list-entry"
                        self.yang_parent_name = "prefix-list-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                        self.exact_prefix_length = YLeaf(YType.uint8, "exact-prefix-length")

                        self.grant = YLeaf(YType.enumeration, "grant")

                        self.ipv6_address_as_string = YLeaf(YType.str, "ipv6-address-as-string")

                        self.match_exact_length = YLeaf(YType.enumeration, "match-exact-length")

                        self.match_max_length = YLeaf(YType.enumeration, "match-max-length")

                        self.match_min_length = YLeaf(YType.enumeration, "match-min-length")

                        self.max_prefix_length = YLeaf(YType.uint8, "max-prefix-length")

                        self.min_prefix_length = YLeaf(YType.uint8, "min-prefix-length")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_mask = YLeaf(YType.uint8, "prefix-mask")

                        self.remark = YLeaf(YType.str, "remark")

                        self.zone = YLeaf(YType.str, "zone")
                        self._segment_path = lambda: "prefix-list-entry" + "[sequence-number='" + self.sequence_number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, ['sequence_number', 'exact_prefix_length', 'grant', 'ipv6_address_as_string', 'match_exact_length', 'match_max_length', 'match_min_length', 'max_prefix_length', 'min_prefix_length', 'prefix', 'prefix_mask', 'remark', 'zone'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv6AclAndPrefixList()
        return self._top_entity

