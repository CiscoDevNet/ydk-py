""" ietf_access_control_list 

This YANG module defines a component that describing the
configuration of Access Control Lists (ACLs).
Copyright (c) 2016 IETF Trust and the persons identified as
the document authors.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD
License set forth in Section 4.c of the IETF Trust's Legal
Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).
This version of this YANG module is part of RFC XXXX; see
the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AclBaseIdentity(object):
    """
    Base Access Control List type for all Access Control List type
    identifiers.
    
    

    """

    _prefix = 'acl'
    _revision = '2016-10-12'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_access_control_list as meta
        return meta._meta_table['AclBaseIdentity']['meta_info']


class AccessLists(object):
    """
    This is a top level container for Access Control Lists.
    It can have one or more Access Control Lists.
    
    .. attribute:: acl
    
    	An Access Control List(ACL) is an ordered list of Access List Entries (ACE). Each Access Control Entry has a list of match criteria and a list of actions. Since there are several kinds of Access Control Lists implemented with different attributes for different vendors, this model accommodates customizing Access Control Lists for each kind and for each vendor
    	**type**\: list of    :py:class:`Acl <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl>`
    
    

    """

    _prefix = 'acl'
    _revision = '2016-10-12'

    def __init__(self):
        self.acl = YList()
        self.acl.parent = self
        self.acl.name = 'acl'


    class Acl(object):
        """
        An Access Control List(ACL) is an ordered list of
        Access List Entries (ACE). Each Access Control Entry has a
        list of match criteria and a list of actions.
        Since there are several kinds of Access Control Lists
        implemented with different attributes for
        different vendors, this
        model accommodates customizing Access Control Lists for
        each kind and for each vendor.
        
        .. attribute:: acl_name  <key>
        
        	The name of access\-list. A device MAY restrict the length and value of this name, possibly space and special characters are not allowed
        	**type**\:  str
        
        .. attribute:: acl_type  <key>
        
        	Type of access control list. Indicates the primary intended type of match criteria (e.g. ethernet, IPv4, IPv6, mixed, etc) used in the list instance
        	**type**\:   :py:class:`AclBaseIdentity <ydk.models.ietf.ietf_access_control_list.AclBaseIdentity>`
        
        .. attribute:: access_list_entries
        
        	The access\-list\-entries container contains a list of access\-list\-entries(ACE)
        	**type**\:   :py:class:`AccessListEntries <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries>`
        
        .. attribute:: acl_oper_data
        
        	Overall Access Control List operational data
        	**type**\:   :py:class:`AclOperData <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AclOperData>`
        
        

        """

        _prefix = 'acl'
        _revision = '2016-10-12'

        def __init__(self):
            self.parent = None
            self.acl_name = None
            self.acl_type = None
            self.access_list_entries = AccessLists.Acl.AccessListEntries()
            self.access_list_entries.parent = self
            self.acl_oper_data = AccessLists.Acl.AclOperData()
            self.acl_oper_data.parent = self


        class AclOperData(object):
            """
            Overall Access Control List operational data
            
            

            """

            _prefix = 'acl'
            _revision = '2016-10-12'

            def __init__(self):
                self.parent = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-access-control-list:acl-oper-data'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_access_control_list as meta
                return meta._meta_table['AccessLists.Acl.AclOperData']['meta_info']


        class AccessListEntries(object):
            """
            The access\-list\-entries container contains
            a list of access\-list\-entries(ACE).
            
            .. attribute:: ace
            
            	List of access list entries(ACE)
            	**type**\: list of    :py:class:`Ace <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace>`
            
            

            """

            _prefix = 'acl'
            _revision = '2016-10-12'

            def __init__(self):
                self.parent = None
                self.ace = YList()
                self.ace.parent = self
                self.ace.name = 'ace'


            class Ace(object):
                """
                List of access list entries(ACE)
                
                .. attribute:: rule_name  <key>
                
                	A unique name identifying this Access List Entry(ACE)
                	**type**\:  str
                
                .. attribute:: ace_oper_data
                
                	Operational data for this Access List Entry
                	**type**\:   :py:class:`AceOperData <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace.AceOperData>`
                
                .. attribute:: actions
                
                	Definitions of action criteria for this Access List Entry
                	**type**\:   :py:class:`Actions <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace.Actions>`
                
                .. attribute:: matches
                
                	Definitions for match criteria for this Access List Entry
                	**type**\:   :py:class:`Matches <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace.Matches>`
                
                

                """

                _prefix = 'acl'
                _revision = '2016-10-12'

                def __init__(self):
                    self.parent = None
                    self.rule_name = None
                    self.ace_oper_data = AccessLists.Acl.AccessListEntries.Ace.AceOperData()
                    self.ace_oper_data.parent = self
                    self.actions = AccessLists.Acl.AccessListEntries.Ace.Actions()
                    self.actions.parent = self
                    self.matches = AccessLists.Acl.AccessListEntries.Ace.Matches()
                    self.matches.parent = self


                class Matches(object):
                    """
                    Definitions for match criteria for this Access List
                    Entry.
                    
                    .. attribute:: destination_ipv4_network
                    
                    	Destination IPv4 address prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    .. attribute:: destination_ipv6_network
                    
                    	Destination IPv6 address prefix
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: destination_mac_address
                    
                    	Destination IEEE 802 MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: destination_mac_address_mask
                    
                    	Destination IEEE 802 MAC address mask
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: destination_port_range
                    
                    	Inclusive range representing destination ports to be used. When        only lower\-port is present, it represents a single port
                    	**type**\:   :py:class:`DestinationPortRange <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: dscp
                    
                    	Value of dscp
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: flow_label
                    
                    	IPv6 Flow label
                    	**type**\:  int
                    
                    	**range:** 0..1048575
                    
                    .. attribute:: protocol
                    
                    	Internet Protocol number
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: source_ipv4_network
                    
                    	Source IPv4 address prefix
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    .. attribute:: source_ipv6_network
                    
                    	Source IPv6 address prefix
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: source_mac_address
                    
                    	Source IEEE 802 MAC address
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mac_address_mask
                    
                    	Source IEEE 802 MAC address mask
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_port_range
                    
                    	Inclusive range representing source ports to be used. When only lower\-port is present, it represents a single port
                    	**type**\:   :py:class:`SourcePortRange <ydk.models.ietf.ietf_access_control_list.AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'acl'
                    _revision = '2016-10-12'

                    def __init__(self):
                        self.parent = None
                        self.destination_ipv4_network = None
                        self.destination_ipv6_network = None
                        self.destination_mac_address = None
                        self.destination_mac_address_mask = None
                        self.destination_port_range = None
                        self.dscp = None
                        self.flow_label = None
                        self.protocol = None
                        self.source_ipv4_network = None
                        self.source_ipv6_network = None
                        self.source_mac_address = None
                        self.source_mac_address_mask = None
                        self.source_port_range = None


                    class SourcePortRange(object):
                        """
                        Inclusive range representing source ports to be used.
                        When only lower\-port is present, it represents a single port.
                        
                        .. attribute:: lower_port
                        
                        	Lower boundary for port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**mandatory**\: True
                        
                        .. attribute:: upper_port
                        
                        	Upper boundary for port . If existing, the upper port must be greater or equal to lower\-port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'acl'
                        _revision = '2016-10-12'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.lower_port = None
                            self.upper_port = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-access-control-list:source-port-range'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.lower_port is not None:
                                return True

                            if self.upper_port is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_access_control_list as meta
                            return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange']['meta_info']


                    class DestinationPortRange(object):
                        """
                        Inclusive range representing destination ports to be used. When
                               only lower\-port is present, it represents a single port.
                        
                        .. attribute:: lower_port
                        
                        	Lower boundary for port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**mandatory**\: True
                        
                        .. attribute:: upper_port
                        
                        	Upper boundary for port. If existing, the upper port must be greater or equal to lower\-port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'acl'
                        _revision = '2016-10-12'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.lower_port = None
                            self.upper_port = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-access-control-list:destination-port-range'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self._is_presence:
                                return True
                            if self.lower_port is not None:
                                return True

                            if self.upper_port is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_access_control_list as meta
                            return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-access-control-list:matches'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.destination_ipv4_network is not None:
                            return True

                        if self.destination_ipv6_network is not None:
                            return True

                        if self.destination_mac_address is not None:
                            return True

                        if self.destination_mac_address_mask is not None:
                            return True

                        if self.destination_port_range is not None and self.destination_port_range._has_data():
                            return True

                        if self.dscp is not None:
                            return True

                        if self.flow_label is not None:
                            return True

                        if self.protocol is not None:
                            return True

                        if self.source_ipv4_network is not None:
                            return True

                        if self.source_ipv6_network is not None:
                            return True

                        if self.source_mac_address is not None:
                            return True

                        if self.source_mac_address_mask is not None:
                            return True

                        if self.source_port_range is not None and self.source_port_range._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_access_control_list as meta
                        return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches']['meta_info']


                class Actions(object):
                    """
                    Definitions of action criteria for this Access List
                    Entry.
                    
                    .. attribute:: deny
                    
                    	Deny action
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: permit
                    
                    	Permit action
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'acl'
                    _revision = '2016-10-12'

                    def __init__(self):
                        self.parent = None
                        self.deny = None
                        self.permit = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-access-control-list:actions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.deny is not None:
                            return True

                        if self.permit is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_access_control_list as meta
                        return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace.Actions']['meta_info']


                class AceOperData(object):
                    """
                    Operational data for this Access List Entry.
                    
                    .. attribute:: match_counter
                    
                    	Number of matches for this Access List Entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'acl'
                    _revision = '2016-10-12'

                    def __init__(self):
                        self.parent = None
                        self.match_counter = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-access-control-list:ace-oper-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.match_counter is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_access_control_list as meta
                        return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace.AceOperData']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.rule_name is None:
                        raise YPYModelError('Key property rule_name is None')

                    return self.parent._common_path +'/ietf-access-control-list:ace[ietf-access-control-list:rule-name = ' + str(self.rule_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.rule_name is not None:
                        return True

                    if self.ace_oper_data is not None and self.ace_oper_data._has_data():
                        return True

                    if self.actions is not None and self.actions._has_data():
                        return True

                    if self.matches is not None and self.matches._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_access_control_list as meta
                    return meta._meta_table['AccessLists.Acl.AccessListEntries.Ace']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-access-control-list:access-list-entries'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ace is not None:
                    for child_ref in self.ace:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_access_control_list as meta
                return meta._meta_table['AccessLists.Acl.AccessListEntries']['meta_info']

        @property
        def _common_path(self):
            if self.acl_name is None:
                raise YPYModelError('Key property acl_name is None')
            if self.acl_type is None:
                raise YPYModelError('Key property acl_type is None')

            return '/ietf-access-control-list:access-lists/ietf-access-control-list:acl[ietf-access-control-list:acl-name = ' + str(self.acl_name) + '][ietf-access-control-list:acl-type = ' + str(self.acl_type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.acl_name is not None:
                return True

            if self.acl_type is not None:
                return True

            if self.access_list_entries is not None and self.access_list_entries._has_data():
                return True

            if self.acl_oper_data is not None and self.acl_oper_data._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_access_control_list as meta
            return meta._meta_table['AccessLists.Acl']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-access-control-list:access-lists'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.acl is not None:
            for child_ref in self.acl:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_access_control_list as meta
        return meta._meta_table['AccessLists']['meta_info']


class Ipv6AclIdentity(AclBaseIdentity):
    """
    ACL that primarily matches on fields from the IPv6 header
    (e.g. IPv6 destination address) and layer 4 headers (e.g. TCP
    destination port). An acl of type ipv6\-acl does not contain
    matches on fields in the ethernet header or the IPv4 header.
    
    

    """

    _prefix = 'acl'
    _revision = '2016-10-12'

    def __init__(self):
        AclBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_access_control_list as meta
        return meta._meta_table['Ipv6AclIdentity']['meta_info']


class Ipv4AclIdentity(AclBaseIdentity):
    """
    ACL that primarily matches on fields from the IPv4 header
    (e.g. IPv4 destination address) and layer 4 headers (e.g. TCP
    destination port).  An acl of type ipv4\-acl does not contain
    matches on fields in the ethernet header or the IPv6 header.
    
    

    """

    _prefix = 'acl'
    _revision = '2016-10-12'

    def __init__(self):
        AclBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_access_control_list as meta
        return meta._meta_table['Ipv4AclIdentity']['meta_info']


class EthAclIdentity(AclBaseIdentity):
    """
    ACL that primarily matches on fields in the ethernet header,
    like 10/100/1000baseT or WiFi Access Control List. An acl of
    type eth\-acl does not contain matches on fields in the IPv4
    header, IPv6 header or layer 4 headers.
    
    

    """

    _prefix = 'acl'
    _revision = '2016-10-12'

    def __init__(self):
        AclBaseIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_access_control_list as meta
        return meta._meta_table['EthAclIdentity']['meta_info']


