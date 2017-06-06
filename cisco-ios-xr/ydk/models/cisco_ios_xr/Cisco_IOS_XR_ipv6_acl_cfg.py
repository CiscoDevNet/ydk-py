""" Cisco_IOS_XR_ipv6_acl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: IPv6 ACL configuration data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NextHopTypeEnum(Enum):
    """
    NextHopTypeEnum

    Next\-hop type.

    .. data:: none_next_hop = 0

    	None next-hop.

    .. data:: regular_next_hop = 1

    	Regular next-hop.

    .. data:: default_next_hop = 2

    	Default next-hop.

    """

    none_next_hop = 0

    regular_next_hop = 1

    default_next_hop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
        return meta._meta_table['NextHopTypeEnum']



class Ipv6AclAndPrefixList(object):
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
    _revision = '2016-11-07'

    def __init__(self):
        self.accesses = Ipv6AclAndPrefixList.Accesses()
        self.accesses.parent = self
        self.log_update = Ipv6AclAndPrefixList.LogUpdate()
        self.log_update.parent = self
        self.prefixes = Ipv6AclAndPrefixList.Prefixes()
        self.prefixes.parent = self


    class Prefixes(object):
        """
        Table of prefix lists
        
        .. attribute:: prefix
        
        	Name of a prefix list
        	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2016-11-07'

        def __init__(self):
            self.parent = None
            self.prefix = YList()
            self.prefix.parent = self
            self.prefix.name = 'prefix'


        class Prefix(object):
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
            _revision = '2016-11-07'

            def __init__(self):
                self.parent = None
                self.name = None
                self.prefix_list_entries = None


            class PrefixListEntries(object):
                """
                Sequence of entries forming a prefix list
                
                .. attribute:: prefix_list_entry
                
                	A prefix list entry; either a description (remark) or a prefix to match against
                	**type**\: list of    :py:class:`PrefixListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2016-11-07'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.prefix_list_entry = YList()
                    self.prefix_list_entry.parent = self
                    self.prefix_list_entry.name = 'prefix_list_entry'


                class PrefixListEntry(object):
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
                    	**type**\:   :py:class:`Ipv6AclGrantEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnumEnum>`
                    
                    .. attribute:: ipv6_address_as_string
                    
                    	The IPv6 address if entered  with the ZoneMutually exclusive with Prefix and PrefixMask
                    	**type**\:  str
                    
                    .. attribute:: match_exact_length
                    
                    	Set to perform an exact prefix length match. Item is mutually exclusive with minimum and maximum length match items
                    	**type**\:   :py:class:`Ipv6PrefixMatchExactLengthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchExactLengthEnum>`
                    
                    .. attribute:: match_max_length
                    
                    	Set to perform a maximum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:   :py:class:`Ipv6PrefixMatchMaxLengthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMaxLengthEnum>`
                    
                    .. attribute:: match_min_length
                    
                    	Set to perform a minimum length prefix match .  Item is mutually exclusive with exact length match item
                    	**type**\:   :py:class:`Ipv6PrefixMatchMinLengthEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6PrefixMatchMinLengthEnum>`
                    
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
                    _revision = '2016-11-07'

                    def __init__(self):
                        self.parent = None
                        self.sequence_number = None
                        self.exact_prefix_length = None
                        self.grant = None
                        self.ipv6_address_as_string = None
                        self.match_exact_length = None
                        self.match_max_length = None
                        self.match_min_length = None
                        self.max_prefix_length = None
                        self.min_prefix_length = None
                        self.prefix = None
                        self.prefix_mask = None
                        self.remark = None
                        self.zone = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.sequence_number is None:
                            raise YPYModelError('Key property sequence_number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:prefix-list-entry[Cisco-IOS-XR-ipv6-acl-cfg:sequence-number = ' + str(self.sequence_number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sequence_number is not None:
                            return True

                        if self.exact_prefix_length is not None:
                            return True

                        if self.grant is not None:
                            return True

                        if self.ipv6_address_as_string is not None:
                            return True

                        if self.match_exact_length is not None:
                            return True

                        if self.match_max_length is not None:
                            return True

                        if self.match_min_length is not None:
                            return True

                        if self.max_prefix_length is not None:
                            return True

                        if self.min_prefix_length is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_mask is not None:
                            return True

                        if self.remark is not None:
                            return True

                        if self.zone is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                        return meta._meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:prefix-list-entries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.prefix_list_entry is not None:
                        for child_ref in self.prefix_list_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-cfg:prefixes/Cisco-IOS-XR-ipv6-acl-cfg:prefix[Cisco-IOS-XR-ipv6-acl-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.prefix_list_entries is not None and self.prefix_list_entries._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-cfg:prefixes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.prefix is not None:
                for child_ref in self.prefix:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
            return meta._meta_table['Ipv6AclAndPrefixList.Prefixes']['meta_info']


    class LogUpdate(object):
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
        _revision = '2016-11-07'

        def __init__(self):
            self.parent = None
            self.rate = None
            self.threshold = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-cfg:log-update'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.rate is not None:
                return True

            if self.threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
            return meta._meta_table['Ipv6AclAndPrefixList.LogUpdate']['meta_info']


    class Accesses(object):
        """
        Table of access lists
        
        .. attribute:: access
        
        	An ACL
        	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access>`
        
        

        """

        _prefix = 'ipv6-acl-cfg'
        _revision = '2016-11-07'

        def __init__(self):
            self.parent = None
            self.access = YList()
            self.access.parent = self
            self.access.name = 'access'


        class Access(object):
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
            _revision = '2016-11-07'

            def __init__(self):
                self.parent = None
                self.name = None
                self.access_list_entries = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries()
                self.access_list_entries.parent = self


            class AccessListEntries(object):
                """
                ACL entry table; contains list of access list
                entries
                
                .. attribute:: access_list_entry
                
                	An ACL entry; either a description (remark) or anAccess List Entry to match against
                	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry>`
                
                

                """

                _prefix = 'ipv6-acl-cfg'
                _revision = '2016-11-07'

                def __init__(self):
                    self.parent = None
                    self.access_list_entry = YList()
                    self.access_list_entry.parent = self
                    self.access_list_entry.name = 'access_list_entry'


                class AccessListEntry(object):
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
                    
                    	**type**\:   :py:class:`Ipv6AclDscpNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclDscpNumberEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..64
                    
                    
                    ----
                    .. attribute:: grant
                    
                    	Whether to forward or drop packets matching the  ACE
                    	**type**\:   :py:class:`Ipv6AclGrantEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclGrantEnumEnum>`
                    
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
                    	**type**\:   :py:class:`Ipv6AclLoggingEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclLoggingEnumEnum>`
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop settings
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop>`
                    
                    .. attribute:: packet_length
                    
                    	Packet length settings
                    	**type**\:   :py:class:`PacketLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength>`
                    
                    .. attribute:: precedence
                    
                    	Precedence value to match (if a protocol was  specified), leave unspecified if precedence  comparion is not to be performed
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclPrecedenceNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPrecedenceNumberEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    .. attribute:: protocol
                    
                    	Protocol to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclProtocolNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumberEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol2
                    
                    	Protocol2 to match
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`Ipv6AclProtocolNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclProtocolNumberEnum>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    
                    ----
                    .. attribute:: protocol_operator
                    
                    	Protocol operator. Leave unspecified if no protocol comparison is to be done
                    	**type**\:   :py:class:`Ipv6AclOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnumEnum>`
                    
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
                    _revision = '2016-11-07'

                    def __init__(self):
                        self.parent = None
                        self.sequence_number = None
                        self.capture = None
                        self.counter_name = None
                        self.destination_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork()
                        self.destination_network.parent = self
                        self.destination_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort()
                        self.destination_port.parent = self
                        self.destination_port_group = None
                        self.destination_prefix_group = None
                        self.dscp = None
                        self.grant = None
                        self.header_flags = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags()
                        self.header_flags.parent = self
                        self.icmp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp()
                        self.icmp.parent = self
                        self.icmp_off = None
                        self.log_option = None
                        self.next_hop = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop()
                        self.next_hop.parent = self
                        self.packet_length = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength()
                        self.packet_length.parent = self
                        self.precedence = None
                        self.protocol = None
                        self.protocol2 = None
                        self.protocol_operator = None
                        self.qos_group = None
                        self.remark = None
                        self.sequence_str = None
                        self.source_network = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork()
                        self.source_network.parent = self
                        self.source_port = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort()
                        self.source_port.parent = self
                        self.source_port_group = None
                        self.source_prefix_group = None
                        self.tcp = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp()
                        self.tcp.parent = self
                        self.time_to_live = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive()
                        self.time_to_live.parent = self
                        self.undetermined_transport = None


                    class SourceNetwork(object):
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
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.source_address = None
                            self.source_mask = None
                            self.source_wild_card_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:source-network'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source_address is not None:
                                return True

                            if self.source_mask is not None:
                                return True

                            if self.source_wild_card_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info']


                    class DestinationNetwork(object):
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
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.destination_address = None
                            self.destination_mask = None
                            self.destination_wild_card_bits = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:destination-network'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.destination_address is not None:
                                return True

                            if self.destination_mask is not None:
                                return True

                            if self.destination_wild_card_bits is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info']


                    class SourcePort(object):
                        """
                        Source port settings.
                        
                        .. attribute:: first_source_port
                        
                        	First source port for comparison,  leave unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_source_port
                        
                        	Second source port for comparion,  leave unspecified if source port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: source_operator
                        
                        	Source comparison operator. Leave unspecified if no source port comparison is to be done
                        	**type**\:   :py:class:`Ipv6AclOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnumEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.first_source_port = None
                            self.second_source_port = None
                            self.source_operator = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:source-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.first_source_port is not None:
                                return True

                            if self.second_source_port is not None:
                                return True

                            if self.source_operator is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort']['meta_info']


                    class DestinationPort(object):
                        """
                        Destination port settings.
                        
                        .. attribute:: destination_operator
                        
                        	Destination comparison operator. Leave  unspecified if no destination port comparison  is to be done
                        	**type**\:   :py:class:`Ipv6AclOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnumEnum>`
                        
                        .. attribute:: first_destination_port
                        
                        	First destination port for comparison, leave  unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        .. attribute:: second_destination_port
                        
                        	Second destination port for comparion, leave  unspecified if destination port comparison is not to be performed
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclPortNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclPortNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.destination_operator = None
                            self.first_destination_port = None
                            self.second_destination_port = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:destination-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.destination_operator is not None:
                                return True

                            if self.first_destination_port is not None:
                                return True

                            if self.second_destination_port is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort']['meta_info']


                    class Icmp(object):
                        """
                        ICMP settings.
                        
                        .. attribute:: icmp_type_code
                        
                        	Well known ICMP message code types to match,  leave unspecified if ICMP message code type  comparion is not to be performed
                        	**type**\:   :py:class:`Ipv6AclIcmpTypeCodeEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclIcmpTypeCodeEnumEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.icmp_type_code = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:icmp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.icmp_type_code is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp']['meta_info']


                    class Tcp(object):
                        """
                        TCP settings.
                        
                        .. attribute:: tcp_bits
                        
                        	TCP bits to match. Leave unspecified if  comparison of TCP bits is not required
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclTcpBitsNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_mask
                        
                        	TCP bits mask to use for flexible TCP matching. Leave unspecified if it is not required
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`Ipv6AclTcpBitsNumberEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpBitsNumberEnum>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 0..63
                        
                        
                        ----
                        .. attribute:: tcp_bits_match_operator
                        
                        	TCP Bits match operator. Leave unspecified if  flexible comparison of TCP bits is not  required
                        	**type**\:   :py:class:`Ipv6AclTcpMatchOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclTcpMatchOperatorEnumEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.tcp_bits = None
                            self.tcp_bits_mask = None
                            self.tcp_bits_match_operator = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:tcp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.tcp_bits is not None:
                                return True

                            if self.tcp_bits_mask is not None:
                                return True

                            if self.tcp_bits_match_operator is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp']['meta_info']


                    class PacketLength(object):
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
                        	**type**\:   :py:class:`Ipv6AclOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnumEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.packet_length_max = None
                            self.packet_length_min = None
                            self.packet_length_operator = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:packet-length'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.packet_length_max is not None:
                                return True

                            if self.packet_length_min is not None:
                                return True

                            if self.packet_length_operator is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength']['meta_info']


                    class TimeToLive(object):
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
                        	**type**\:   :py:class:`Ipv6AclOperatorEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes.Ipv6AclOperatorEnumEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.time_to_live_max = None
                            self.time_to_live_min = None
                            self.time_to_live_operator = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:time-to-live'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.time_to_live_max is not None:
                                return True

                            if self.time_to_live_min is not None:
                                return True

                            if self.time_to_live_operator is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive']['meta_info']


                    class NextHop(object):
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
                        	**type**\:   :py:class:`NextHopTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg.NextHopTypeEnum>`
                        
                        

                        """

                        _prefix = 'ipv6-acl-cfg'
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.next_hop_1 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1()
                            self.next_hop_1.parent = self
                            self.next_hop_2 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2()
                            self.next_hop_2.parent = self
                            self.next_hop_3 = Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3()
                            self.next_hop_3.parent = self
                            self.next_hop_type = None


                        class NextHop1(object):
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
                            _revision = '2016-11-07'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.track_name = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:next-hop-1'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.track_name is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1']['meta_info']


                        class NextHop2(object):
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
                            _revision = '2016-11-07'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.track_name = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:next-hop-2'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.track_name is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2']['meta_info']


                        class NextHop3(object):
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
                            _revision = '2016-11-07'

                            def __init__(self):
                                self.parent = None
                                self.next_hop = None
                                self.track_name = None
                                self.vrf_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:next-hop-3'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.next_hop is not None:
                                    return True

                                if self.track_name is not None:
                                    return True

                                if self.vrf_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                                return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:next-hop'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.next_hop_1 is not None and self.next_hop_1._has_data():
                                return True

                            if self.next_hop_2 is not None and self.next_hop_2._has_data():
                                return True

                            if self.next_hop_3 is not None and self.next_hop_3._has_data():
                                return True

                            if self.next_hop_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']


                    class HeaderFlags(object):
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
                        _revision = '2016-11-07'

                        def __init__(self):
                            self.parent = None
                            self.authen = None
                            self.destopts = None
                            self.fragments = None
                            self.hop_by_hop = None
                            self.routing = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:header-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.authen is not None:
                                return True

                            if self.destopts is not None:
                                return True

                            if self.fragments is not None:
                                return True

                            if self.hop_by_hop is not None:
                                return True

                            if self.routing is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                            return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.sequence_number is None:
                            raise YPYModelError('Key property sequence_number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:access-list-entry[Cisco-IOS-XR-ipv6-acl-cfg:sequence-number = ' + str(self.sequence_number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sequence_number is not None:
                            return True

                        if self.capture is not None:
                            return True

                        if self.counter_name is not None:
                            return True

                        if self.destination_network is not None and self.destination_network._has_data():
                            return True

                        if self.destination_port is not None and self.destination_port._has_data():
                            return True

                        if self.destination_port_group is not None:
                            return True

                        if self.destination_prefix_group is not None:
                            return True

                        if self.dscp is not None:
                            return True

                        if self.grant is not None:
                            return True

                        if self.header_flags is not None and self.header_flags._has_data():
                            return True

                        if self.icmp is not None and self.icmp._has_data():
                            return True

                        if self.icmp_off is not None:
                            return True

                        if self.log_option is not None:
                            return True

                        if self.next_hop is not None and self.next_hop._has_data():
                            return True

                        if self.packet_length is not None and self.packet_length._has_data():
                            return True

                        if self.precedence is not None:
                            return True

                        if self.protocol is not None:
                            return True

                        if self.protocol2 is not None:
                            return True

                        if self.protocol_operator is not None:
                            return True

                        if self.qos_group is not None:
                            return True

                        if self.remark is not None:
                            return True

                        if self.sequence_str is not None:
                            return True

                        if self.source_network is not None and self.source_network._has_data():
                            return True

                        if self.source_port is not None and self.source_port._has_data():
                            return True

                        if self.source_port_group is not None:
                            return True

                        if self.source_prefix_group is not None:
                            return True

                        if self.tcp is not None and self.tcp._has_data():
                            return True

                        if self.time_to_live is not None and self.time_to_live._has_data():
                            return True

                        if self.undetermined_transport is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                        return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-acl-cfg:access-list-entries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_list_entry is not None:
                        for child_ref in self.access_list_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                    return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-cfg:accesses/Cisco-IOS-XR-ipv6-acl-cfg:access[Cisco-IOS-XR-ipv6-acl-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.access_list_entries is not None and self.access_list_entries._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
                return meta._meta_table['Ipv6AclAndPrefixList.Accesses.Access']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list/Cisco-IOS-XR-ipv6-acl-cfg:accesses'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.access is not None:
                for child_ref in self.access:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
            return meta._meta_table['Ipv6AclAndPrefixList.Accesses']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-acl-cfg:ipv6-acl-and-prefix-list'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.accesses is not None and self.accesses._has_data():
            return True

        if self.log_update is not None and self.log_update._has_data():
            return True

        if self.prefixes is not None and self.prefixes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_cfg as meta
        return meta._meta_table['Ipv6AclAndPrefixList']['meta_info']


