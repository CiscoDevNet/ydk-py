""" Cisco_IOS_XR_ipv4_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-acl package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-acl\-and\-prefix\-list\: IPv4 ACL configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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



class Ipv4AclAndPrefixList(Entity):
    """
    IPv4 ACL configuration data
    
    .. attribute:: accesses
    
    	Table of access lists.  Entries in this table and the AccessListExistenceTable table must be kept consistent
    	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses>`
    
    .. attribute:: log_update
    
    	Control access lists log updates
    	**type**\:   :py:class:`LogUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.LogUpdate>`
    
    .. attribute:: prefixes
    
    	Table of ACL prefix lists.  Entries in this table and the PrefixListExistenceTable table must be kept consistent
    	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes>`
    
    

    """

    _prefix = 'ipv4-acl-cfg'
    _revision = '2016-11-07'

    def __init__(self):
        super(Ipv4AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-acl-cfg"

        self.accesses = Ipv4AclAndPrefixList.Accesses()
        self.accesses.parent = self
        self._children_name_map["accesses"] = "accesses"
        self._children_yang_names.add("accesses")

        self.log_update = Ipv4AclAndPrefixList.LogUpdate()
        self.log_update.parent = self
        self._children_name_map["log_update"] = "log-update"
        self._children_yang_names.add("log-update")

        self.prefixes = Ipv4AclAndPrefixList.Prefixes()
        self.prefixes.parent = self
        self._children_name_map["prefixes"] = "prefixes"
        self._children_yang_names.add("prefixes")


    class Accesses(Entity):
        """
        Table of access lists.  Entries in this table
        and the AccessListExistenceTable table must be
        kept consistent
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access>`
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2016-11-07'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Accesses, self).__init__()

            self.yang_name = "accesses"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"

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
                        super(Ipv4AclAndPrefixList.Accesses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4AclAndPrefixList.Accesses, self).__setattr__(name, value)


        class Access(Entity):
            """
            An ACL
            
            .. attribute:: access_list_name  <key>
            
            	Access list name \- 64 characters max
            	**type**\:  str
            
            .. attribute:: access_list_entries
            
            	ACL entry table; contains list of ACEs
            	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries>`
            
            

            """

            _prefix = 'ipv4-acl-cfg'
            _revision = '2016-11-07'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Accesses.Access, self).__init__()

                self.yang_name = "access"
                self.yang_parent_name = "accesses"

                self.access_list_name = YLeaf(YType.str, "access-list-name")

                self.access_list_entries = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries()
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
                    if name in ("access_list_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4AclAndPrefixList.Accesses.Access, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.Accesses.Access, self).__setattr__(name, value)


            class AccessListEntries(Entity):
                """
                ACL entry table; contains list of ACEs
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or an ACE to match against
                	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'ipv4-acl-cfg'
                _revision = '2016-11-07'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries, self).__init__()

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
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries, self).__setattr__(name, value)


                class AccessListEntry(Entity):
                    """
                    An ACL entry; either a description (remark)
                    or an ACE to match against
                    
                    .. attribute:: sequence_number  <key>
                    
                    	Sequence number for this entry
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
                    	**type**\:   :py:class:`DestinationNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork>`
                    
                    .. attribute:: destination_port
                    
                    	Destination port settings
                    	**type**\:   :py:class:`DestinationPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort>`
                    
                    .. attribute:: destination_port_group
                    
                    	Destination port object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: destination_prefix_group
                    
                    	IPv4 destination network object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: dscp
                    
                    	DSCP settings
                    	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp>`
                    
                    .. attribute:: fragment_offset
                    
                    	Fragment\-offset settings
                    	**type**\:   :py:class:`FragmentOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset>`
                    
                    .. attribute:: fragments
                    
                    	Check non\-initial fragments. Item is mutually  exclusive with TCP, SCTP, UDP, IGMP and ICMP  comparions and with logging
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the  ACE
                    	**type**\:   :py:class:`Ipv4AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclGrantEnum>`
                    
                    .. attribute:: icmp
                    
                    	ICMP settings
                    	**type**\:   :py:class:`Icmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp>`
                    
                    .. attribute:: icmp_off
                    
                    	To turn off ICMP generation for deny ACEs
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: igmp_message_type
                    
                    	IGMP message type to match. Leave unspecified if  no message type comparison is to be done
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv4AclIgmpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclIgmpNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: log_option
                    
                    	Whether and how to log matches against this  entry
                    	**type**\:   :py:class:`Ipv4AclLoggingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclLoggingEnum>`
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop settings
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop>`
                    
                    .. attribute:: packet_length
                    
                    	Packet length settings
                    	**type**\:   :py:class:`PacketLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value to match (if a protocol was  specified), leave unspecified if precedence  comparion is not to be performed
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv4AclPrecedenceNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPrecedenceNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    .. attribute:: protocol
                    
                    	Protocol to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv4AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclProtocolNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol2
                    
                    	Protocol2 to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv4AclProtocolNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclProtocolNumber>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol_operator
                    
                    	Protocol operator. Leave unspecified if no protocol comparison is to be done
                    	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                    
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
                    
                    .. attribute:: source_network
                    
                    	Source network settings
                    	**type**\:   :py:class:`SourceNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork>`
                    
                    .. attribute:: source_port
                    
                    	Source port settings
                    	**type**\:   :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort>`
                    
                    .. attribute:: source_port_group
                    
                    	Source port object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: source_prefix_group
                    
                    	IPv4 source network object group name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: tcp
                    
                    	TCP settings
                    	**type**\:   :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp>`
                    
                    .. attribute:: time_to_live
                    
                    	TTL settings
                    	**type**\:   :py:class:`TimeToLive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive>`
                    
                    

                    """

                    _prefix = 'ipv4-acl-cfg'
                    _revision = '2016-11-07'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__init__()

                        self.yang_name = "access-list-entry"
                        self.yang_parent_name = "access-list-entries"

                        self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                        self.capture = YLeaf(YType.boolean, "capture")

                        self.counter_name = YLeaf(YType.str, "counter-name")

                        self.destination_port_group = YLeaf(YType.str, "destination-port-group")

                        self.destination_prefix_group = YLeaf(YType.str, "destination-prefix-group")

                        self.fragments = YLeaf(YType.empty, "fragments")

                        self.grant = YLeaf(YType.enumeration, "grant")

                        self.icmp_off = YLeaf(YType.empty, "icmp-off")

                        self.igmp_message_type = YLeaf(YType.str, "igmp-message-type")

                        self.log_option = YLeaf(YType.enumeration, "log-option")

                        self.precedence = YLeaf(YType.str, "precedence")

                        self.protocol = YLeaf(YType.str, "protocol")

                        self.protocol2 = YLeaf(YType.str, "protocol2")

                        self.protocol_operator = YLeaf(YType.enumeration, "protocol-operator")

                        self.qos_group = YLeaf(YType.uint32, "qos-group")

                        self.remark = YLeaf(YType.str, "remark")

                        self.sequence_str = YLeaf(YType.str, "sequence-str")

                        self.source_port_group = YLeaf(YType.str, "source-port-group")

                        self.source_prefix_group = YLeaf(YType.str, "source-prefix-group")

                        self.destination_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self._children_name_map["destination_network"] = "destination-network"
                        self._children_yang_names.add("destination-network")

                        self.destination_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                        self.destination_port.parent = self
                        self._children_name_map["destination_port"] = "destination-port"
                        self._children_yang_names.add("destination-port")

                        self.dscp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp()
                        self.dscp.parent = self
                        self._children_name_map["dscp"] = "dscp"
                        self._children_yang_names.add("dscp")

                        self.fragment_offset = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset()
                        self.fragment_offset.parent = self
                        self._children_name_map["fragment_offset"] = "fragment-offset"
                        self._children_yang_names.add("fragment-offset")

                        self.icmp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                        self.icmp.parent = self
                        self._children_name_map["icmp"] = "icmp"
                        self._children_yang_names.add("icmp")

                        self.next_hop = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")

                        self.packet_length = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                        self.packet_length.parent = self
                        self._children_name_map["packet_length"] = "packet-length"
                        self._children_yang_names.add("packet-length")

                        self.source_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self._children_name_map["source_network"] = "source-network"
                        self._children_yang_names.add("source-network")

                        self.source_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                        self.source_port.parent = self
                        self._children_name_map["source_port"] = "source-port"
                        self._children_yang_names.add("source-port")

                        self.tcp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                        self.tcp.parent = self
                        self._children_name_map["tcp"] = "tcp"
                        self._children_yang_names.add("tcp")

                        self.time_to_live = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                        self.time_to_live.parent = self
                        self._children_name_map["time_to_live"] = "time-to-live"
                        self._children_yang_names.add("time-to-live")

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
                                        "counter_name",
                                        "destination_port_group",
                                        "destination_prefix_group",
                                        "fragments",
                                        "grant",
                                        "icmp_off",
                                        "igmp_message_type",
                                        "log_option",
                                        "precedence",
                                        "protocol",
                                        "protocol2",
                                        "protocol_operator",
                                        "qos_group",
                                        "remark",
                                        "sequence_str",
                                        "source_port_group",
                                        "source_prefix_group") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry, self).__setattr__(name, value)


                    class SourceNetwork(Entity):
                        """
                        Source network settings.
                        
                        .. attribute:: source_address
                        
                        	Source IPv4 address to match, leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_prefix_length
                        
                        	Prefix length to apply to source address  (if specified), leave unspecified for no  wildcarding
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: source_wild_card_bits
                        
                        	Wildcard bits to apply to source address  (if specified), leave unspecified for no  wildcarding
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__init__()

                            self.yang_name = "source-network"
                            self.yang_parent_name = "access-list-entry"

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.source_prefix_length = YLeaf(YType.uint8, "source-prefix-length")

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
                                            "source_prefix_length",
                                            "source_wild_card_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.source_address.is_set or
                                self.source_prefix_length.is_set or
                                self.source_wild_card_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.source_address.yfilter != YFilter.not_set or
                                self.source_prefix_length.yfilter != YFilter.not_set or
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
                            if (self.source_prefix_length.is_set or self.source_prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_prefix_length.get_name_leafdata())
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
                            if(name == "source-address" or name == "source-prefix-length" or name == "source-wild-card-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "source-address"):
                                self.source_address = value
                                self.source_address.value_namespace = name_space
                                self.source_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-prefix-length"):
                                self.source_prefix_length = value
                                self.source_prefix_length.value_namespace = name_space
                                self.source_prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-wild-card-bits"):
                                self.source_wild_card_bits = value
                                self.source_wild_card_bits.value_namespace = name_space
                                self.source_wild_card_bits.value_namespace_prefix = name_space_prefix


                    class DestinationNetwork(Entity):
                        """
                        Destination network settings.
                        
                        .. attribute:: destination_address
                        
                        	Destination IPv4 address to match (if a protocol was specified), leave unspecified for any
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_prefix_length
                        
                        	Prefix length to apply to destination address  (if specified), leave unspecified for no  wildcarding
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: destination_wild_card_bits
                        
                        	Wildcard bits to apply to destination address (if specified), leave unspecified for no  wildcarding
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__init__()

                            self.yang_name = "destination-network"
                            self.yang_parent_name = "access-list-entry"

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_prefix_length = YLeaf(YType.uint8, "destination-prefix-length")

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
                                            "destination_prefix_length",
                                            "destination_wild_card_bits") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.destination_address.is_set or
                                self.destination_prefix_length.is_set or
                                self.destination_wild_card_bits.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.destination_prefix_length.yfilter != YFilter.not_set or
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
                            if (self.destination_prefix_length.is_set or self.destination_prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_prefix_length.get_name_leafdata())
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
                            if(name == "destination-address" or name == "destination-prefix-length" or name == "destination-wild-card-bits"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-prefix-length"):
                                self.destination_prefix_length = value
                                self.destination_prefix_length.value_namespace = name_space
                                self.destination_prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-wild-card-bits"):
                                self.destination_wild_card_bits = value
                                self.destination_wild_card_bits.value_namespace = name_space
                                self.destination_wild_card_bits.value_namespace_prefix = name_space_prefix


                    class SourcePort(Entity):
                        """
                        Source port settings.
                        
                        .. attribute:: first_source_port
                        
                        	First source port for comparison, leave  unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_source_port
                        
                        	Second source port for comparion, leave  unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: source_operator
                        
                        	Source comparison operator . Leave unspecified  if no source port comparison is to be done
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__init__()

                            self.yang_name = "source-port"
                            self.yang_parent_name = "access-list-entry"

                            self.first_source_port = YLeaf(YType.str, "first-source-port")

                            self.second_source_port = YLeaf(YType.str, "second-source-port")

                            self.source_operator = YLeaf(YType.enumeration, "source-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("first_source_port",
                                            "second_source_port",
                                            "source_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.first_source_port.is_set or
                                self.second_source_port.is_set or
                                self.source_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.first_source_port.yfilter != YFilter.not_set or
                                self.second_source_port.yfilter != YFilter.not_set or
                                self.source_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "source-port" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.first_source_port.is_set or self.first_source_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.first_source_port.get_name_leafdata())
                            if (self.second_source_port.is_set or self.second_source_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.second_source_port.get_name_leafdata())
                            if (self.source_operator.is_set or self.source_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "first-source-port" or name == "second-source-port" or name == "source-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "first-source-port"):
                                self.first_source_port = value
                                self.first_source_port.value_namespace = name_space
                                self.first_source_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "second-source-port"):
                                self.second_source_port = value
                                self.second_source_port.value_namespace = name_space
                                self.second_source_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-operator"):
                                self.source_operator = value
                                self.source_operator.value_namespace = name_space
                                self.source_operator.value_namespace_prefix = name_space_prefix


                    class DestinationPort(Entity):
                        """
                        Destination port settings.
                        
                        .. attribute:: destination_operator
                        
                        	Destination comparison operator. Leave  unspecified if no destination port comparison is to be done
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        .. attribute:: first_destination_port
                        
                        	First destination port for comparison, leave unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_destination_port
                        
                        	Second destination port for comparion, leave unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclPortNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclPortNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__init__()

                            self.yang_name = "destination-port"
                            self.yang_parent_name = "access-list-entry"

                            self.destination_operator = YLeaf(YType.enumeration, "destination-operator")

                            self.first_destination_port = YLeaf(YType.str, "first-destination-port")

                            self.second_destination_port = YLeaf(YType.str, "second-destination-port")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_operator",
                                            "first_destination_port",
                                            "second_destination_port") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.destination_operator.is_set or
                                self.first_destination_port.is_set or
                                self.second_destination_port.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_operator.yfilter != YFilter.not_set or
                                self.first_destination_port.yfilter != YFilter.not_set or
                                self.second_destination_port.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-port" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_operator.is_set or self.destination_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_operator.get_name_leafdata())
                            if (self.first_destination_port.is_set or self.first_destination_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.first_destination_port.get_name_leafdata())
                            if (self.second_destination_port.is_set or self.second_destination_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.second_destination_port.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "destination-operator" or name == "first-destination-port" or name == "second-destination-port"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-operator"):
                                self.destination_operator = value
                                self.destination_operator.value_namespace = name_space
                                self.destination_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "first-destination-port"):
                                self.first_destination_port = value
                                self.first_destination_port.value_namespace = name_space
                                self.first_destination_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "second-destination-port"):
                                self.second_destination_port = value
                                self.second_destination_port.value_namespace = name_space
                                self.second_destination_port.value_namespace_prefix = name_space_prefix


                    class Icmp(Entity):
                        """
                        ICMP settings.
                        
                        .. attribute:: icmp_type_code
                        
                        	Well known ICMP message code types to match,  leave unspecified if ICMP message code type  comparion is not to be performed
                        	**type**\:   :py:class:`Ipv4AclIcmpTypeCodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclIcmpTypeCodeEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__init__()

                            self.yang_name = "icmp"
                            self.yang_parent_name = "access-list-entry"

                            self.icmp_type_code = YLeaf(YType.enumeration, "icmp-type-code")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("icmp_type_code") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp, self).__setattr__(name, value)

                        def has_data(self):
                            return self.icmp_type_code.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.icmp_type_code.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "icmp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.icmp_type_code.is_set or self.icmp_type_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.icmp_type_code.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "icmp-type-code"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "icmp-type-code"):
                                self.icmp_type_code = value
                                self.icmp_type_code.value_namespace = name_space
                                self.icmp_type_code.value_namespace_prefix = name_space_prefix


                    class Tcp(Entity):
                        """
                        TCP settings.
                        
                        .. attribute:: tcp_bits
                        
                        	TCP bits to match. Leave unspecified if comparison of TCP bits is not required
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpBitsNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_mask
                        
                        	TCP bits mask to use for flexible TCP matching. Leave unspecified if tcp\-bits\-match\-operator is  unspecified
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclTcpBitsNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpBitsNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_match_operator
                        
                        	TCP Bits match operator. Leave unspecified if  flexible comparison of TCP bits is not  required
                        	**type**\:   :py:class:`Ipv4AclTcpMatchOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclTcpMatchOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__init__()

                            self.yang_name = "tcp"
                            self.yang_parent_name = "access-list-entry"

                            self.tcp_bits = YLeaf(YType.str, "tcp-bits")

                            self.tcp_bits_mask = YLeaf(YType.str, "tcp-bits-mask")

                            self.tcp_bits_match_operator = YLeaf(YType.enumeration, "tcp-bits-match-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("tcp_bits",
                                            "tcp_bits_mask",
                                            "tcp_bits_match_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.tcp_bits.is_set or
                                self.tcp_bits_mask.is_set or
                                self.tcp_bits_match_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.tcp_bits.yfilter != YFilter.not_set or
                                self.tcp_bits_mask.yfilter != YFilter.not_set or
                                self.tcp_bits_match_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tcp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.tcp_bits.is_set or self.tcp_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_bits.get_name_leafdata())
                            if (self.tcp_bits_mask.is_set or self.tcp_bits_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_bits_mask.get_name_leafdata())
                            if (self.tcp_bits_match_operator.is_set or self.tcp_bits_match_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tcp_bits_match_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "tcp-bits" or name == "tcp-bits-mask" or name == "tcp-bits-match-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "tcp-bits"):
                                self.tcp_bits = value
                                self.tcp_bits.value_namespace = name_space
                                self.tcp_bits.value_namespace_prefix = name_space_prefix
                            if(value_path == "tcp-bits-mask"):
                                self.tcp_bits_mask = value
                                self.tcp_bits_mask.value_namespace = name_space
                                self.tcp_bits_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "tcp-bits-match-operator"):
                                self.tcp_bits_match_operator = value
                                self.tcp_bits_match_operator.value_namespace = name_space
                                self.tcp_bits_match_operator.value_namespace_prefix = name_space_prefix


                    class PacketLength(Entity):
                        """
                        Packet length settings.
                        
                        .. attribute:: packet_length_max
                        
                        	Maximum packet length for comparion, leave  unspecified if packet length comparison is not  to be performed or if only the minimum packet  length should be considered
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_min
                        
                        	Minimum packet length for comparison, leave  unspecified if packet length comparison is not  to be performed or if only the maximum packet  length should be considered
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: packet_length_operator
                        
                        	Packet length operator applicable if Packet  length is to be compared. Leave unspecified if  no packet length comparison is to be done
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__init__()

                            self.yang_name = "packet-length"
                            self.yang_parent_name = "access-list-entry"

                            self.packet_length_max = YLeaf(YType.uint32, "packet-length-max")

                            self.packet_length_min = YLeaf(YType.uint32, "packet-length-min")

                            self.packet_length_operator = YLeaf(YType.enumeration, "packet-length-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("packet_length_max",
                                            "packet_length_min",
                                            "packet_length_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.packet_length_max.is_set or
                                self.packet_length_min.is_set or
                                self.packet_length_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.packet_length_max.yfilter != YFilter.not_set or
                                self.packet_length_min.yfilter != YFilter.not_set or
                                self.packet_length_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "packet-length" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.packet_length_max.is_set or self.packet_length_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length_max.get_name_leafdata())
                            if (self.packet_length_min.is_set or self.packet_length_min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length_min.get_name_leafdata())
                            if (self.packet_length_operator.is_set or self.packet_length_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_length_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "packet-length-max" or name == "packet-length-min" or name == "packet-length-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "packet-length-max"):
                                self.packet_length_max = value
                                self.packet_length_max.value_namespace = name_space
                                self.packet_length_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-length-min"):
                                self.packet_length_min = value
                                self.packet_length_min.value_namespace = name_space
                                self.packet_length_min.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-length-operator"):
                                self.packet_length_operator = value
                                self.packet_length_operator.value_namespace = name_space
                                self.packet_length_operator.value_namespace_prefix = name_space_prefix


                    class TimeToLive(Entity):
                        """
                        TTL settings.
                        
                        .. attribute:: time_to_live_max
                        
                        	Maximum TTL for comparion, leave unspecified if  TTL comparison is not to be performed or if only the minimum TTL should be considered
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_min
                        
                        	TTL value for comparison OR Minimum TTL value  for TTL range comparision, leave unspecified if TTL classification is not required
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: time_to_live_operator
                        
                        	TTL operator is applicable if TTL is to be  compared. Leave unspecified if TTL  classification is not required
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__init__()

                            self.yang_name = "time-to-live"
                            self.yang_parent_name = "access-list-entry"

                            self.time_to_live_max = YLeaf(YType.uint32, "time-to-live-max")

                            self.time_to_live_min = YLeaf(YType.uint32, "time-to-live-min")

                            self.time_to_live_operator = YLeaf(YType.enumeration, "time-to-live-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("time_to_live_max",
                                            "time_to_live_min",
                                            "time_to_live_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.time_to_live_max.is_set or
                                self.time_to_live_min.is_set or
                                self.time_to_live_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.time_to_live_max.yfilter != YFilter.not_set or
                                self.time_to_live_min.yfilter != YFilter.not_set or
                                self.time_to_live_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "time-to-live" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.time_to_live_max.is_set or self.time_to_live_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_to_live_max.get_name_leafdata())
                            if (self.time_to_live_min.is_set or self.time_to_live_min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_to_live_min.get_name_leafdata())
                            if (self.time_to_live_operator.is_set or self.time_to_live_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_to_live_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "time-to-live-max" or name == "time-to-live-min" or name == "time-to-live-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "time-to-live-max"):
                                self.time_to_live_max = value
                                self.time_to_live_max.value_namespace = name_space
                                self.time_to_live_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-to-live-min"):
                                self.time_to_live_min = value
                                self.time_to_live_min.value_namespace = name_space
                                self.time_to_live_min.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-to-live-operator"):
                                self.time_to_live_operator = value
                                self.time_to_live_operator.value_namespace = name_space
                                self.time_to_live_operator.value_namespace_prefix = name_space_prefix


                    class FragmentOffset(Entity):
                        """
                        Fragment\-offset settings.
                        
                        .. attribute:: fragment_offset_1
                        
                        	Fragment\-offset value for comparison or first  fragment\-offset value for fragment\-offset range  comparision, leave unspecified if fragment\-offset classification is not required
                        	**type**\:  int
                        
                        	**range:** 0..8191
                        
                        .. attribute:: fragment_offset_2
                        
                        	Second fragment\-offset value for comparion,  leave unspecified if fragment\-offset comparison is not to be performed or if only the first fragment\-offset should be considered
                        	**type**\:  int
                        
                        	**range:** 0..8191
                        
                        .. attribute:: fragment_offset_operator
                        
                        	Fragment\-offset operator if fragment\-offset is to be compared. Leave unspecified if fragment\-offset classification is not required
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset, self).__init__()

                            self.yang_name = "fragment-offset"
                            self.yang_parent_name = "access-list-entry"

                            self.fragment_offset_1 = YLeaf(YType.uint32, "fragment-offset-1")

                            self.fragment_offset_2 = YLeaf(YType.uint32, "fragment-offset-2")

                            self.fragment_offset_operator = YLeaf(YType.enumeration, "fragment-offset-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("fragment_offset_1",
                                            "fragment_offset_2",
                                            "fragment_offset_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.fragment_offset_1.is_set or
                                self.fragment_offset_2.is_set or
                                self.fragment_offset_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.fragment_offset_1.yfilter != YFilter.not_set or
                                self.fragment_offset_2.yfilter != YFilter.not_set or
                                self.fragment_offset_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fragment-offset" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.fragment_offset_1.is_set or self.fragment_offset_1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset_1.get_name_leafdata())
                            if (self.fragment_offset_2.is_set or self.fragment_offset_2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset_2.get_name_leafdata())
                            if (self.fragment_offset_operator.is_set or self.fragment_offset_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.fragment_offset_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fragment-offset-1" or name == "fragment-offset-2" or name == "fragment-offset-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "fragment-offset-1"):
                                self.fragment_offset_1 = value
                                self.fragment_offset_1.value_namespace = name_space
                                self.fragment_offset_1.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-offset-2"):
                                self.fragment_offset_2 = value
                                self.fragment_offset_2.value_namespace = name_space
                                self.fragment_offset_2.value_namespace_prefix = name_space_prefix
                            if(value_path == "fragment-offset-operator"):
                                self.fragment_offset_operator = value
                                self.fragment_offset_operator.value_namespace = name_space
                                self.fragment_offset_operator.value_namespace_prefix = name_space_prefix


                    class NextHop(Entity):
                        """
                        Next\-hop settings.
                        
                        .. attribute:: next_hop_1
                        
                        	The first next\-hop settings
                        	**type**\:   :py:class:`NextHop1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1>`
                        
                        .. attribute:: next_hop_2
                        
                        	The second next\-hop settings
                        	**type**\:   :py:class:`NextHop2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2>`
                        
                        .. attribute:: next_hop_3
                        
                        	The third next\-hop settings
                        	**type**\:   :py:class:`NextHop3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3>`
                        
                        .. attribute:: next_hop_type
                        
                        	The nexthop type
                        	**type**\:   :py:class:`NextHopType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.NextHopType>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "access-list-entry"

                            self.next_hop_type = YLeaf(YType.enumeration, "next-hop-type")

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("next_hop_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop, self).__setattr__(name, value)


                        class NextHop1(Entity):
                            """
                            The first next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2016-11-07'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__init__()

                                self.yang_name = "next-hop-1"
                                self.yang_parent_name = "next-hop"

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("next_hop",
                                                "track_name",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_hop.is_set or
                                    self.track_name.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.track_name.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-1" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.track_name.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "next-hop" or name == "track-name" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
                                if(value_path == "track-name"):
                                    self.track_name = value
                                    self.track_name.value_namespace = name_space
                                    self.track_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class NextHop2(Entity):
                            """
                            The second next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2016-11-07'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__init__()

                                self.yang_name = "next-hop-2"
                                self.yang_parent_name = "next-hop"

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("next_hop",
                                                "track_name",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_hop.is_set or
                                    self.track_name.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.track_name.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-2" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.track_name.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "next-hop" or name == "track-name" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
                                if(value_path == "track-name"):
                                    self.track_name = value
                                    self.track_name.value_namespace = name_space
                                    self.track_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class NextHop3(Entity):
                            """
                            The third next\-hop settings.
                            
                            .. attribute:: next_hop
                            
                            	The IPv4 address of the next\-hop
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: track_name
                            
                            	The object tracking name for the next\-hop
                            	**type**\:  str
                            
                            .. attribute:: vrf_name
                            
                            	The VRF name of the next\-hop
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ipv4-acl-cfg'
                            _revision = '2016-11-07'

                            def __init__(self):
                                super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__init__()

                                self.yang_name = "next-hop-3"
                                self.yang_parent_name = "next-hop"

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.track_name = YLeaf(YType.str, "track-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("next_hop",
                                                "track_name",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_hop.is_set or
                                    self.track_name.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.track_name.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-3" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.track_name.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "next-hop" or name == "track-name" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
                                if(value_path == "track-name"):
                                    self.track_name = value
                                    self.track_name.value_namespace = name_space
                                    self.track_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.next_hop_type.is_set or
                                (self.next_hop_1 is not None and self.next_hop_1.has_data()) or
                                (self.next_hop_2 is not None and self.next_hop_2.has_data()) or
                                (self.next_hop_3 is not None and self.next_hop_3.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.next_hop_type.yfilter != YFilter.not_set or
                                (self.next_hop_1 is not None and self.next_hop_1.has_operation()) or
                                (self.next_hop_2 is not None and self.next_hop_2.has_operation()) or
                                (self.next_hop_3 is not None and self.next_hop_3.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.next_hop_type.is_set or self.next_hop_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "next-hop-1"):
                                if (self.next_hop_1 is None):
                                    self.next_hop_1 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1()
                                    self.next_hop_1.parent = self
                                    self._children_name_map["next_hop_1"] = "next-hop-1"
                                return self.next_hop_1

                            if (child_yang_name == "next-hop-2"):
                                if (self.next_hop_2 is None):
                                    self.next_hop_2 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2()
                                    self.next_hop_2.parent = self
                                    self._children_name_map["next_hop_2"] = "next-hop-2"
                                return self.next_hop_2

                            if (child_yang_name == "next-hop-3"):
                                if (self.next_hop_3 is None):
                                    self.next_hop_3 = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3()
                                    self.next_hop_3.parent = self
                                    self._children_name_map["next_hop_3"] = "next-hop-3"
                                return self.next_hop_3

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop-1" or name == "next-hop-2" or name == "next-hop-3" or name == "next-hop-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "next-hop-type"):
                                self.next_hop_type = value
                                self.next_hop_type.value_namespace = name_space
                                self.next_hop_type.value_namespace_prefix = name_space_prefix


                    class Dscp(Entity):
                        """
                        DSCP settings.
                        
                        .. attribute:: dscp_max
                        
                        	Maximum DSCP value for comparion, leave  unspecified if DSCP comparison is not to  be performed or if only the minimum DSCP should be considered
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclDscpNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: dscp_min
                        
                        	DSCP value to match or minimum DSCP value  for DSCP range comparison, leave unspecified  if DSCP comparion is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv4AclDscpNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclDscpNumber>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: dscp_operator
                        
                        	DSCP operator is applicable only when DSCP  range is configured. Leave unspecified if  DSCP range is not required
                        	**type**\:   :py:class:`Ipv4AclOperatorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclOperatorEnum>`
                        
                        

                        """

                        _prefix = 'ipv4-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp, self).__init__()

                            self.yang_name = "dscp"
                            self.yang_parent_name = "access-list-entry"

                            self.dscp_max = YLeaf(YType.str, "dscp-max")

                            self.dscp_min = YLeaf(YType.str, "dscp-min")

                            self.dscp_operator = YLeaf(YType.enumeration, "dscp-operator")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dscp_max",
                                            "dscp_min",
                                            "dscp_operator") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.dscp_max.is_set or
                                self.dscp_min.is_set or
                                self.dscp_operator.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dscp_max.yfilter != YFilter.not_set or
                                self.dscp_min.yfilter != YFilter.not_set or
                                self.dscp_operator.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dscp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dscp_max.is_set or self.dscp_max.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp_max.get_name_leafdata())
                            if (self.dscp_min.is_set or self.dscp_min.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp_min.get_name_leafdata())
                            if (self.dscp_operator.is_set or self.dscp_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp_operator.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dscp-max" or name == "dscp-min" or name == "dscp-operator"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dscp-max"):
                                self.dscp_max = value
                                self.dscp_max.value_namespace = name_space
                                self.dscp_max.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp-min"):
                                self.dscp_min = value
                                self.dscp_min.value_namespace = name_space
                                self.dscp_min.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp-operator"):
                                self.dscp_operator = value
                                self.dscp_operator.value_namespace = name_space
                                self.dscp_operator.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.sequence_number.is_set or
                            self.capture.is_set or
                            self.counter_name.is_set or
                            self.destination_port_group.is_set or
                            self.destination_prefix_group.is_set or
                            self.fragments.is_set or
                            self.grant.is_set or
                            self.icmp_off.is_set or
                            self.igmp_message_type.is_set or
                            self.log_option.is_set or
                            self.precedence.is_set or
                            self.protocol.is_set or
                            self.protocol2.is_set or
                            self.protocol_operator.is_set or
                            self.qos_group.is_set or
                            self.remark.is_set or
                            self.sequence_str.is_set or
                            self.source_port_group.is_set or
                            self.source_prefix_group.is_set or
                            (self.destination_network is not None and self.destination_network.has_data()) or
                            (self.destination_port is not None and self.destination_port.has_data()) or
                            (self.dscp is not None and self.dscp.has_data()) or
                            (self.fragment_offset is not None and self.fragment_offset.has_data()) or
                            (self.icmp is not None and self.icmp.has_data()) or
                            (self.next_hop is not None and self.next_hop.has_data()) or
                            (self.packet_length is not None and self.packet_length.has_data()) or
                            (self.source_network is not None and self.source_network.has_data()) or
                            (self.source_port is not None and self.source_port.has_data()) or
                            (self.tcp is not None and self.tcp.has_data()) or
                            (self.time_to_live is not None and self.time_to_live.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sequence_number.yfilter != YFilter.not_set or
                            self.capture.yfilter != YFilter.not_set or
                            self.counter_name.yfilter != YFilter.not_set or
                            self.destination_port_group.yfilter != YFilter.not_set or
                            self.destination_prefix_group.yfilter != YFilter.not_set or
                            self.fragments.yfilter != YFilter.not_set or
                            self.grant.yfilter != YFilter.not_set or
                            self.icmp_off.yfilter != YFilter.not_set or
                            self.igmp_message_type.yfilter != YFilter.not_set or
                            self.log_option.yfilter != YFilter.not_set or
                            self.precedence.yfilter != YFilter.not_set or
                            self.protocol.yfilter != YFilter.not_set or
                            self.protocol2.yfilter != YFilter.not_set or
                            self.protocol_operator.yfilter != YFilter.not_set or
                            self.qos_group.yfilter != YFilter.not_set or
                            self.remark.yfilter != YFilter.not_set or
                            self.sequence_str.yfilter != YFilter.not_set or
                            self.source_port_group.yfilter != YFilter.not_set or
                            self.source_prefix_group.yfilter != YFilter.not_set or
                            (self.destination_network is not None and self.destination_network.has_operation()) or
                            (self.destination_port is not None and self.destination_port.has_operation()) or
                            (self.dscp is not None and self.dscp.has_operation()) or
                            (self.fragment_offset is not None and self.fragment_offset.has_operation()) or
                            (self.icmp is not None and self.icmp.has_operation()) or
                            (self.next_hop is not None and self.next_hop.has_operation()) or
                            (self.packet_length is not None and self.packet_length.has_operation()) or
                            (self.source_network is not None and self.source_network.has_operation()) or
                            (self.source_port is not None and self.source_port.has_operation()) or
                            (self.tcp is not None and self.tcp.has_operation()) or
                            (self.time_to_live is not None and self.time_to_live.has_operation()))

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
                        if (self.counter_name.is_set or self.counter_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.counter_name.get_name_leafdata())
                        if (self.destination_port_group.is_set or self.destination_port_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_port_group.get_name_leafdata())
                        if (self.destination_prefix_group.is_set or self.destination_prefix_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_prefix_group.get_name_leafdata())
                        if (self.fragments.is_set or self.fragments.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fragments.get_name_leafdata())
                        if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.grant.get_name_leafdata())
                        if (self.icmp_off.is_set or self.icmp_off.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.icmp_off.get_name_leafdata())
                        if (self.igmp_message_type.is_set or self.igmp_message_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.igmp_message_type.get_name_leafdata())
                        if (self.log_option.is_set or self.log_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.log_option.get_name_leafdata())
                        if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.precedence.get_name_leafdata())
                        if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol.get_name_leafdata())
                        if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol2.get_name_leafdata())
                        if (self.protocol_operator.is_set or self.protocol_operator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_operator.get_name_leafdata())
                        if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_group.get_name_leafdata())
                        if (self.remark.is_set or self.remark.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remark.get_name_leafdata())
                        if (self.sequence_str.is_set or self.sequence_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sequence_str.get_name_leafdata())
                        if (self.source_port_group.is_set or self.source_port_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_port_group.get_name_leafdata())
                        if (self.source_prefix_group.is_set or self.source_prefix_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_prefix_group.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "destination-network"):
                            if (self.destination_network is None):
                                self.destination_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                                self.destination_network.parent = self
                                self._children_name_map["destination_network"] = "destination-network"
                            return self.destination_network

                        if (child_yang_name == "destination-port"):
                            if (self.destination_port is None):
                                self.destination_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                                self.destination_port.parent = self
                                self._children_name_map["destination_port"] = "destination-port"
                            return self.destination_port

                        if (child_yang_name == "dscp"):
                            if (self.dscp is None):
                                self.dscp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Dscp()
                                self.dscp.parent = self
                                self._children_name_map["dscp"] = "dscp"
                            return self.dscp

                        if (child_yang_name == "fragment-offset"):
                            if (self.fragment_offset is None):
                                self.fragment_offset = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.FragmentOffset()
                                self.fragment_offset.parent = self
                                self._children_name_map["fragment_offset"] = "fragment-offset"
                            return self.fragment_offset

                        if (child_yang_name == "icmp"):
                            if (self.icmp is None):
                                self.icmp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                                self.icmp.parent = self
                                self._children_name_map["icmp"] = "icmp"
                            return self.icmp

                        if (child_yang_name == "next-hop"):
                            if (self.next_hop is None):
                                self.next_hop = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                            return self.next_hop

                        if (child_yang_name == "packet-length"):
                            if (self.packet_length is None):
                                self.packet_length = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                                self.packet_length.parent = self
                                self._children_name_map["packet_length"] = "packet-length"
                            return self.packet_length

                        if (child_yang_name == "source-network"):
                            if (self.source_network is None):
                                self.source_network = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                                self.source_network.parent = self
                                self._children_name_map["source_network"] = "source-network"
                            return self.source_network

                        if (child_yang_name == "source-port"):
                            if (self.source_port is None):
                                self.source_port = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                                self.source_port.parent = self
                                self._children_name_map["source_port"] = "source-port"
                            return self.source_port

                        if (child_yang_name == "tcp"):
                            if (self.tcp is None):
                                self.tcp = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                                self.tcp.parent = self
                                self._children_name_map["tcp"] = "tcp"
                            return self.tcp

                        if (child_yang_name == "time-to-live"):
                            if (self.time_to_live is None):
                                self.time_to_live = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                                self.time_to_live.parent = self
                                self._children_name_map["time_to_live"] = "time-to-live"
                            return self.time_to_live

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-network" or name == "destination-port" or name == "dscp" or name == "fragment-offset" or name == "icmp" or name == "next-hop" or name == "packet-length" or name == "source-network" or name == "source-port" or name == "tcp" or name == "time-to-live" or name == "sequence-number" or name == "capture" or name == "counter-name" or name == "destination-port-group" or name == "destination-prefix-group" or name == "fragments" or name == "grant" or name == "icmp-off" or name == "igmp-message-type" or name == "log-option" or name == "precedence" or name == "protocol" or name == "protocol2" or name == "protocol-operator" or name == "qos-group" or name == "remark" or name == "sequence-str" or name == "source-port-group" or name == "source-prefix-group"):
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
                        if(value_path == "counter-name"):
                            self.counter_name = value
                            self.counter_name.value_namespace = name_space
                            self.counter_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-port-group"):
                            self.destination_port_group = value
                            self.destination_port_group.value_namespace = name_space
                            self.destination_port_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-prefix-group"):
                            self.destination_prefix_group = value
                            self.destination_prefix_group.value_namespace = name_space
                            self.destination_prefix_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "fragments"):
                            self.fragments = value
                            self.fragments.value_namespace = name_space
                            self.fragments.value_namespace_prefix = name_space_prefix
                        if(value_path == "grant"):
                            self.grant = value
                            self.grant.value_namespace = name_space
                            self.grant.value_namespace_prefix = name_space_prefix
                        if(value_path == "icmp-off"):
                            self.icmp_off = value
                            self.icmp_off.value_namespace = name_space
                            self.icmp_off.value_namespace_prefix = name_space_prefix
                        if(value_path == "igmp-message-type"):
                            self.igmp_message_type = value
                            self.igmp_message_type.value_namespace = name_space
                            self.igmp_message_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "log-option"):
                            self.log_option = value
                            self.log_option.value_namespace = name_space
                            self.log_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "precedence"):
                            self.precedence = value
                            self.precedence.value_namespace = name_space
                            self.precedence.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol"):
                            self.protocol = value
                            self.protocol.value_namespace = name_space
                            self.protocol.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol2"):
                            self.protocol2 = value
                            self.protocol2.value_namespace = name_space
                            self.protocol2.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-operator"):
                            self.protocol_operator = value
                            self.protocol_operator.value_namespace = name_space
                            self.protocol_operator.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-group"):
                            self.qos_group = value
                            self.qos_group.value_namespace = name_space
                            self.qos_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "remark"):
                            self.remark = value
                            self.remark.value_namespace = name_space
                            self.remark.value_namespace_prefix = name_space_prefix
                        if(value_path == "sequence-str"):
                            self.sequence_str = value
                            self.sequence_str.value_namespace = name_space
                            self.sequence_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-port-group"):
                            self.source_port_group = value
                            self.source_port_group.value_namespace = name_space
                            self.source_port_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-prefix-group"):
                            self.source_prefix_group = value
                            self.source_prefix_group.value_namespace = name_space
                            self.source_prefix_group.value_namespace_prefix = name_space_prefix

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
                        c = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry()
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
                    self.access_list_name.is_set or
                    (self.access_list_entries is not None and self.access_list_entries.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.access_list_name.yfilter != YFilter.not_set or
                    (self.access_list_entries is not None and self.access_list_entries.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access" + "[access-list-name='" + self.access_list_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/accesses/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.access_list_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "access-list-entries"):
                    if (self.access_list_entries is None):
                        self.access_list_entries = Ipv4AclAndPrefixList.Accesses.Access.AccessListEntries()
                        self.access_list_entries.parent = self
                        self._children_name_map["access_list_entries"] = "access-list-entries"
                    return self.access_list_entries

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "access-list-entries" or name == "access-list-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "access-list-name"):
                    self.access_list_name = value
                    self.access_list_name.value_namespace = name_space
                    self.access_list_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self.get_segment_path()
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
                c = Ipv4AclAndPrefixList.Accesses.Access()
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


    class Prefixes(Entity):
        """
        Table of ACL prefix lists.  Entries in this
        table and the PrefixListExistenceTable table
        must be kept consistent
        
        .. attribute:: prefix
        
        	Name of a prefix list
        	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix>`
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2016-11-07'

        def __init__(self):
            super(Ipv4AclAndPrefixList.Prefixes, self).__init__()

            self.yang_name = "prefixes"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"

            self.prefix = YList(self)

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
                        super(Ipv4AclAndPrefixList.Prefixes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4AclAndPrefixList.Prefixes, self).__setattr__(name, value)


        class Prefix(Entity):
            """
            Name of a prefix list
            
            .. attribute:: prefix_list_name  <key>
            
            	Prefix list name \- max 32 characters
            	**type**\:  str
            
            .. attribute:: prefix_list_entries
            
            	Sequence of entries forming a prefix list
            	**type**\:   :py:class:`PrefixListEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-acl-cfg'
            _revision = '2016-11-07'

            def __init__(self):
                super(Ipv4AclAndPrefixList.Prefixes.Prefix, self).__init__()

                self.yang_name = "prefix"
                self.yang_parent_name = "prefixes"

                self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                self.prefix_list_entries = None
                self._children_name_map["prefix_list_entries"] = "prefix-list-entries"
                self._children_yang_names.add("prefix-list-entries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("prefix_list_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4AclAndPrefixList.Prefixes.Prefix, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4AclAndPrefixList.Prefixes.Prefix, self).__setattr__(name, value)


            class PrefixListEntries(Entity):
                """
                Sequence of entries forming a prefix list
                
                .. attribute:: prefix_list_entry
                
                	A prefix list entry; either a description (remark) or a prefix to match against
                	**type**\: list of    :py:class:`PrefixListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_cfg.Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-acl-cfg'
                _revision = '2016-11-07'

                def __init__(self):
                    super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__init__()

                    self.yang_name = "prefix-list-entries"
                    self.yang_parent_name = "prefix"
                    self.is_presence_container = True

                    self.prefix_list_entry = YList(self)

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
                                super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries, self).__setattr__(name, value)


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
                    
                    	**range:** 0..32
                    
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the prefix list
                    	**type**\:   :py:class:`Ipv4AclGrantEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_acl_datatypes.Ipv4AclGrantEnum>`
                    
                    .. attribute:: match_exact_length
                    
                    	Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: match_max_length
                    
                    	Set to perform a maximum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: match_min_length
                    
                    	Set to perform a minimum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: max_prefix_length
                    
                    	If maximum length prefix matching specified, set the maximum length of prefix to be matched
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: min_prefix_length
                    
                    	If minimum length prefix matching specified, set the minimum length of prefix to be matched
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: netmask
                    
                    	Mask of IPv4 address prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix
                    
                    	IPv4 address prefix to match
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: remark
                    
                    	Comments or a description for the prefix list.  Item is mutually exclusive with all others in the object
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ipv4-acl-cfg'
                    _revision = '2016-11-07'

                    def __init__(self):
                        super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__init__()

                        self.yang_name = "prefix-list-entry"
                        self.yang_parent_name = "prefix-list-entries"

                        self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                        self.exact_prefix_length = YLeaf(YType.uint32, "exact-prefix-length")

                        self.grant = YLeaf(YType.enumeration, "grant")

                        self.match_exact_length = YLeaf(YType.empty, "match-exact-length")

                        self.match_max_length = YLeaf(YType.empty, "match-max-length")

                        self.match_min_length = YLeaf(YType.empty, "match-min-length")

                        self.max_prefix_length = YLeaf(YType.uint32, "max-prefix-length")

                        self.min_prefix_length = YLeaf(YType.uint32, "min-prefix-length")

                        self.netmask = YLeaf(YType.str, "netmask")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.remark = YLeaf(YType.str, "remark")

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
                                        "exact_prefix_length",
                                        "grant",
                                        "match_exact_length",
                                        "match_max_length",
                                        "match_min_length",
                                        "max_prefix_length",
                                        "min_prefix_length",
                                        "netmask",
                                        "prefix",
                                        "remark") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.sequence_number.is_set or
                            self.exact_prefix_length.is_set or
                            self.grant.is_set or
                            self.match_exact_length.is_set or
                            self.match_max_length.is_set or
                            self.match_min_length.is_set or
                            self.max_prefix_length.is_set or
                            self.min_prefix_length.is_set or
                            self.netmask.is_set or
                            self.prefix.is_set or
                            self.remark.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sequence_number.yfilter != YFilter.not_set or
                            self.exact_prefix_length.yfilter != YFilter.not_set or
                            self.grant.yfilter != YFilter.not_set or
                            self.match_exact_length.yfilter != YFilter.not_set or
                            self.match_max_length.yfilter != YFilter.not_set or
                            self.match_min_length.yfilter != YFilter.not_set or
                            self.max_prefix_length.yfilter != YFilter.not_set or
                            self.min_prefix_length.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.remark.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefix-list-entry" + "[sequence-number='" + self.sequence_number.get() + "']" + path_buffer

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
                        if (self.exact_prefix_length.is_set or self.exact_prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exact_prefix_length.get_name_leafdata())
                        if (self.grant.is_set or self.grant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.grant.get_name_leafdata())
                        if (self.match_exact_length.is_set or self.match_exact_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.match_exact_length.get_name_leafdata())
                        if (self.match_max_length.is_set or self.match_max_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.match_max_length.get_name_leafdata())
                        if (self.match_min_length.is_set or self.match_min_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.match_min_length.get_name_leafdata())
                        if (self.max_prefix_length.is_set or self.max_prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_prefix_length.get_name_leafdata())
                        if (self.min_prefix_length.is_set or self.min_prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_prefix_length.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.remark.is_set or self.remark.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remark.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sequence-number" or name == "exact-prefix-length" or name == "grant" or name == "match-exact-length" or name == "match-max-length" or name == "match-min-length" or name == "max-prefix-length" or name == "min-prefix-length" or name == "netmask" or name == "prefix" or name == "remark"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "sequence-number"):
                            self.sequence_number = value
                            self.sequence_number.value_namespace = name_space
                            self.sequence_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "exact-prefix-length"):
                            self.exact_prefix_length = value
                            self.exact_prefix_length.value_namespace = name_space
                            self.exact_prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "grant"):
                            self.grant = value
                            self.grant.value_namespace = name_space
                            self.grant.value_namespace_prefix = name_space_prefix
                        if(value_path == "match-exact-length"):
                            self.match_exact_length = value
                            self.match_exact_length.value_namespace = name_space
                            self.match_exact_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "match-max-length"):
                            self.match_max_length = value
                            self.match_max_length.value_namespace = name_space
                            self.match_max_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "match-min-length"):
                            self.match_min_length = value
                            self.match_min_length.value_namespace = name_space
                            self.match_min_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-prefix-length"):
                            self.max_prefix_length = value
                            self.max_prefix_length.value_namespace = name_space
                            self.max_prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-prefix-length"):
                            self.min_prefix_length = value
                            self.min_prefix_length.value_namespace = name_space
                            self.min_prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "remark"):
                            self.remark = value
                            self.remark.value_namespace = name_space
                            self.remark.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.prefix_list_entry:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.prefix_list_entry:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix-list-entries" + path_buffer

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

                    if (child_yang_name == "prefix-list-entry"):
                        for c in self.prefix_list_entry:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.prefix_list_entry.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix-list-entry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.prefix_list_name.is_set or
                    (self.prefix_list_entries is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.prefix_list_name.yfilter != YFilter.not_set or
                    (self.prefix_list_entries is not None and self.prefix_list_entries.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prefix" + "[prefix-list-name='" + self.prefix_list_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/prefixes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.prefix_list_name.is_set or self.prefix_list_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prefix_list_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "prefix-list-entries"):
                    if (self.prefix_list_entries is None):
                        self.prefix_list_entries = Ipv4AclAndPrefixList.Prefixes.Prefix.PrefixListEntries()
                        self.prefix_list_entries.parent = self
                        self._children_name_map["prefix_list_entries"] = "prefix-list-entries"
                    return self.prefix_list_entries

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "prefix-list-entries" or name == "prefix-list-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "prefix-list-name"):
                    self.prefix_list_name = value
                    self.prefix_list_name.value_namespace = name_space
                    self.prefix_list_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.prefix:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.prefix:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "prefixes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "prefix"):
                for c in self.prefix:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv4AclAndPrefixList.Prefixes.Prefix()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.prefix.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "prefix"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class LogUpdate(Entity):
        """
        Control access lists log updates
        
        .. attribute:: rate
        
        	Log update rate (log msgs per second)
        	**type**\:  int
        
        	**range:** 1..1000
        
        .. attribute:: threshold
        
        	Log update threshold (number of hits)
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        

        """

        _prefix = 'ipv4-acl-cfg'
        _revision = '2016-11-07'

        def __init__(self):
            super(Ipv4AclAndPrefixList.LogUpdate, self).__init__()

            self.yang_name = "log-update"
            self.yang_parent_name = "ipv4-acl-and-prefix-list"

            self.rate = YLeaf(YType.uint32, "rate")

            self.threshold = YLeaf(YType.uint32, "threshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("rate",
                            "threshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4AclAndPrefixList.LogUpdate, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4AclAndPrefixList.LogUpdate, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.rate.is_set or
                self.threshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.rate.yfilter != YFilter.not_set or
                self.threshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "log-update" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rate.get_name_leafdata())
            if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.threshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rate" or name == "threshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "rate"):
                self.rate = value
                self.rate.value_namespace = name_space
                self.rate.value_namespace_prefix = name_space_prefix
            if(value_path == "threshold"):
                self.threshold = value
                self.threshold.value_namespace = name_space
                self.threshold.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.accesses is not None and self.accesses.has_data()) or
            (self.log_update is not None and self.log_update.has_data()) or
            (self.prefixes is not None and self.prefixes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.accesses is not None and self.accesses.has_operation()) or
            (self.log_update is not None and self.log_update.has_operation()) or
            (self.prefixes is not None and self.prefixes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-acl-cfg:ipv4-acl-and-prefix-list" + path_buffer

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
                self.accesses = Ipv4AclAndPrefixList.Accesses()
                self.accesses.parent = self
                self._children_name_map["accesses"] = "accesses"
            return self.accesses

        if (child_yang_name == "log-update"):
            if (self.log_update is None):
                self.log_update = Ipv4AclAndPrefixList.LogUpdate()
                self.log_update.parent = self
                self._children_name_map["log_update"] = "log-update"
            return self.log_update

        if (child_yang_name == "prefixes"):
            if (self.prefixes is None):
                self.prefixes = Ipv4AclAndPrefixList.Prefixes()
                self.prefixes.parent = self
                self._children_name_map["prefixes"] = "prefixes"
            return self.prefixes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "accesses" or name == "log-update" or name == "prefixes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ipv4AclAndPrefixList()
        return self._top_entity

