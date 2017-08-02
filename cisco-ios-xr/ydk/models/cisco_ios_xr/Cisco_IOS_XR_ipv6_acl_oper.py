""" Cisco_IOS_XR_ipv6_acl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-acl package operational data.

This module contains definitions
for the following management objects\:
  ipv6\-acl\-and\-prefix\-list\: Root class of IPv6 Oper schema tree

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AclAce1(Enum):
    """
    AclAce1

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = Enum.YLeaf(0, "normal")

    remark = Enum.YLeaf(1, "remark")

    abf = Enum.YLeaf(2, "abf")


class AclAce1(Enum):
    """
    AclAce1

    ACE Types

    .. data:: normal = 0

    	This is Normal ACE

    .. data:: remark = 1

    	This is Remark ACE

    .. data:: abf = 2

    	This is ABF ACE

    """

    normal = Enum.YLeaf(0, "normal")

    remark = Enum.YLeaf(1, "remark")

    abf = Enum.YLeaf(2, "abf")


class AclAction(Enum):
    """
    AclAction

    Acl action

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    .. data:: encrypt = 2

    	Encrypt

    .. data:: bypass = 3

    	Bypass

    .. data:: fallthrough = 4

    	Fallthrough

    .. data:: invalid = 5

    	Invalid

    """

    deny = Enum.YLeaf(0, "deny")

    permit = Enum.YLeaf(1, "permit")

    encrypt = Enum.YLeaf(2, "encrypt")

    bypass = Enum.YLeaf(3, "bypass")

    fallthrough = Enum.YLeaf(4, "fallthrough")

    invalid = Enum.YLeaf(5, "invalid")


class AclLog(Enum):
    """
    AclLog

    Acl log

    .. data:: log_none = 0

    	Log None

    .. data:: log = 1

    	Log Regular

    .. data:: log_input = 2

    	Log Input

    """

    log_none = Enum.YLeaf(0, "log-none")

    log = Enum.YLeaf(1, "log")

    log_input = Enum.YLeaf(2, "log-input")


class AclPortOperator(Enum):
    """
    AclPortOperator

    Acl port operator

    .. data:: none = 0

    	None

    .. data:: eq = 1

    	Equal

    .. data:: gt = 2

    	Greater than

    .. data:: lt = 3

    	Less than

    .. data:: neq = 4

    	Not Equal

    .. data:: range = 5

    	Range

    .. data:: onebyte = 8

    	One Byte

    .. data:: twobytes = 9

    	Two Bytes

    """

    none = Enum.YLeaf(0, "none")

    eq = Enum.YLeaf(1, "eq")

    gt = Enum.YLeaf(2, "gt")

    lt = Enum.YLeaf(3, "lt")

    neq = Enum.YLeaf(4, "neq")

    range = Enum.YLeaf(5, "range")

    onebyte = Enum.YLeaf(8, "onebyte")

    twobytes = Enum.YLeaf(9, "twobytes")


class AclPortOperator(Enum):
    """
    AclPortOperator

    Acl port operator

    .. data:: none = 0

    	None

    .. data:: eq = 1

    	Equal

    .. data:: gt = 2

    	Greater than

    .. data:: lt = 3

    	Less than

    .. data:: neq = 4

    	Not Equal

    .. data:: range = 5

    	Range

    .. data:: onebyte = 8

    	One Byte

    .. data:: twobytes = 9

    	Two Bytes

    """

    none = Enum.YLeaf(0, "none")

    eq = Enum.YLeaf(1, "eq")

    gt = Enum.YLeaf(2, "gt")

    lt = Enum.YLeaf(3, "lt")

    neq = Enum.YLeaf(4, "neq")

    range = Enum.YLeaf(5, "range")

    onebyte = Enum.YLeaf(8, "onebyte")

    twobytes = Enum.YLeaf(9, "twobytes")


class AclPortOperator(Enum):
    """
    AclPortOperator

    Acl port operator

    .. data:: none = 0

    	None

    .. data:: eq = 1

    	Equal

    .. data:: gt = 2

    	Greater than

    .. data:: lt = 3

    	Less than

    .. data:: neq = 4

    	Not Equal

    .. data:: range = 5

    	Range

    .. data:: onebyte = 8

    	One Byte

    .. data:: twobytes = 9

    	Two Bytes

    """

    none = Enum.YLeaf(0, "none")

    eq = Enum.YLeaf(1, "eq")

    gt = Enum.YLeaf(2, "gt")

    lt = Enum.YLeaf(3, "lt")

    neq = Enum.YLeaf(4, "neq")

    range = Enum.YLeaf(5, "range")

    onebyte = Enum.YLeaf(8, "onebyte")

    twobytes = Enum.YLeaf(9, "twobytes")


class AclPortOperator(Enum):
    """
    AclPortOperator

    Acl port operator

    .. data:: none = 0

    	None

    .. data:: eq = 1

    	Equal

    .. data:: gt = 2

    	Greater than

    .. data:: lt = 3

    	Less than

    .. data:: neq = 4

    	Not Equal

    .. data:: range = 5

    	Range

    .. data:: onebyte = 8

    	One Byte

    .. data:: twobytes = 9

    	Two Bytes

    """

    none = Enum.YLeaf(0, "none")

    eq = Enum.YLeaf(1, "eq")

    gt = Enum.YLeaf(2, "gt")

    lt = Enum.YLeaf(3, "lt")

    neq = Enum.YLeaf(4, "neq")

    range = Enum.YLeaf(5, "range")

    onebyte = Enum.YLeaf(8, "onebyte")

    twobytes = Enum.YLeaf(9, "twobytes")


class AclTcpflagsOperator(Enum):
    """
    AclTcpflagsOperator

    Acl tcpflags operator

    .. data:: match_none = 0

    	Match None

    .. data:: match_all = 1

    	Match All

    .. data:: match_any_old = 2

    	Match any old

    .. data:: match_any = 3

    	Match any

    """

    match_none = Enum.YLeaf(0, "match-none")

    match_all = Enum.YLeaf(1, "match-all")

    match_any_old = Enum.YLeaf(2, "match-any-old")

    match_any = Enum.YLeaf(3, "match-any")


class BagAclNh(Enum):
    """
    BagAclNh

    Bag acl nh

    .. data:: nexthop_none = 0

    	Next Hop None

    .. data:: nexthop_default = 1

    	Nexthop Default

    .. data:: nexthop = 2

    	Nexthop

    """

    nexthop_none = Enum.YLeaf(0, "nexthop-none")

    nexthop_default = Enum.YLeaf(1, "nexthop-default")

    nexthop = Enum.YLeaf(2, "nexthop")


class BagAclNhAtStatus(Enum):
    """
    BagAclNhAtStatus

    Bag acl nh at status

    .. data:: unknown = 0

    	AT State Unknown

    .. data:: up = 1

    	AT State UP

    .. data:: down = 2

    	AT State DOWN

    .. data:: not_present = 3

    	AT State Not Present

    .. data:: max = 4

    	invalid status

    """

    unknown = Enum.YLeaf(0, "unknown")

    up = Enum.YLeaf(1, "up")

    down = Enum.YLeaf(2, "down")

    not_present = Enum.YLeaf(3, "not-present")

    max = Enum.YLeaf(4, "max")


class BagAclNhStatus(Enum):
    """
    BagAclNhStatus

    Bag acl nh status

    .. data:: not_present = 0

    	State Not Present

    .. data:: unknown = 1

    	State Unknown

    .. data:: down = 2

    	State DOWN

    .. data:: up = 3

    	State UP

    .. data:: max = 4

    	invalid status

    """

    not_present = Enum.YLeaf(0, "not-present")

    unknown = Enum.YLeaf(1, "unknown")

    down = Enum.YLeaf(2, "down")

    up = Enum.YLeaf(3, "up")

    max = Enum.YLeaf(4, "max")



class Ipv6AclAndPrefixList(Entity):
    """
    Root class of IPv6 Oper schema tree
    
    .. attribute:: access_list_manager
    
    	AccessListManager containing ACLs and prefix lists
    	**type**\:   :py:class:`AccessListManager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager>`
    
    .. attribute:: oor
    
    	Out Of Resources, Limits to the resources allocatable
    	**type**\:   :py:class:`Oor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor>`
    
    

    """

    _prefix = 'ipv6-acl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6AclAndPrefixList, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-acl-and-prefix-list"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-acl-oper"

        self.access_list_manager = Ipv6AclAndPrefixList.AccessListManager()
        self.access_list_manager.parent = self
        self._children_name_map["access_list_manager"] = "access-list-manager"
        self._children_yang_names.add("access-list-manager")

        self.oor = Ipv6AclAndPrefixList.Oor()
        self.oor.parent = self
        self._children_name_map["oor"] = "oor"
        self._children_yang_names.add("oor")


    class AccessListManager(Entity):
        """
        AccessListManager containing ACLs and prefix
        lists
        
        .. attribute:: accesses
        
        	ACL class displaying Usage and Entries
        	**type**\:   :py:class:`Accesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses>`
        
        .. attribute:: prefixes
        
        	Table of prefix lists
        	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes>`
        
        .. attribute:: usages
        
        	Table of Usage statistics of ACLs at different nodes
        	**type**\:   :py:class:`Usages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Usages>`
        
        

        """

        _prefix = 'ipv6-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6AclAndPrefixList.AccessListManager, self).__init__()

            self.yang_name = "access-list-manager"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"

            self.accesses = Ipv6AclAndPrefixList.AccessListManager.Accesses()
            self.accesses.parent = self
            self._children_name_map["accesses"] = "accesses"
            self._children_yang_names.add("accesses")

            self.prefixes = Ipv6AclAndPrefixList.AccessListManager.Prefixes()
            self.prefixes.parent = self
            self._children_name_map["prefixes"] = "prefixes"
            self._children_yang_names.add("prefixes")

            self.usages = Ipv6AclAndPrefixList.AccessListManager.Usages()
            self.usages.parent = self
            self._children_name_map["usages"] = "usages"
            self._children_yang_names.add("usages")


        class Prefixes(Entity):
            """
            Table of prefix lists
            
            .. attribute:: prefix
            
            	Name of the prefix list
            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Prefixes, self).__init__()

                self.yang_name = "prefixes"
                self.yang_parent_name = "access-list-manager"

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
                            super(Ipv6AclAndPrefixList.AccessListManager.Prefixes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.AccessListManager.Prefixes, self).__setattr__(name, value)


            class Prefix(Entity):
                """
                Name of the prefix list
                
                .. attribute:: prefix_list_name  <key>
                
                	Name of the prefix list
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: prefix_list_sequences
                
                	Table of all the SequenceNumbers per prefix list
                	**type**\:   :py:class:`PrefixListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "prefixes"

                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                    self.prefix_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                    self.prefix_list_sequences.parent = self
                    self._children_name_map["prefix_list_sequences"] = "prefix-list-sequences"
                    self._children_yang_names.add("prefix-list-sequences")

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
                                super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix, self).__setattr__(name, value)


                class PrefixListSequences(Entity):
                    """
                    Table of all the SequenceNumbers per prefix
                    list
                    
                    .. attribute:: prefix_list_sequence
                    
                    	Sequence Number of a prefix list entry
                    	**type**\: list of    :py:class:`PrefixListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence>`
                    
                    

                    """

                    _prefix = 'ipv6-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__init__()

                        self.yang_name = "prefix-list-sequences"
                        self.yang_parent_name = "prefix"

                        self.prefix_list_sequence = YList(self)

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
                                    super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences, self).__setattr__(name, value)


                    class PrefixListSequence(Entity):
                        """
                        Sequence Number of a prefix list entry
                        
                        .. attribute:: sequence_number  <key>
                        
                        	Sequence Number of the prefix list entry
                        	**type**\:  int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\:  str
                        
                        .. attribute:: hits
                        
                        	Number of hits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_ace_sequence_number
                        
                        	ACLE sequence number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_ace_type
                        
                        	ACE type (acl, remark)
                        	**type**\:   :py:class:`AclAce1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1>`
                        
                        .. attribute:: is_address_in_numbers
                        
                        	IPv6 prefix
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_address_mask_length
                        
                        	Prefix length 
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_comment_for_entry
                        
                        	Remark String
                        	**type**\:  str
                        
                        .. attribute:: is_length_operator
                        
                        	Port Operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:   :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAction>`
                        
                        .. attribute:: is_packet_maximum_length
                        
                        	Maximum length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_minimum_length
                        
                        	Min length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ipv6-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__init__()

                            self.yang_name = "prefix-list-sequence"
                            self.yang_parent_name = "prefix-list-sequences"

                            self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.hits = YLeaf(YType.uint32, "hits")

                            self.is_ace_sequence_number = YLeaf(YType.uint32, "is-ace-sequence-number")

                            self.is_ace_type = YLeaf(YType.enumeration, "is-ace-type")

                            self.is_address_in_numbers = YLeaf(YType.str, "is-address-in-numbers")

                            self.is_address_mask_length = YLeaf(YType.uint32, "is-address-mask-length")

                            self.is_comment_for_entry = YLeaf(YType.str, "is-comment-for-entry")

                            self.is_length_operator = YLeaf(YType.enumeration, "is-length-operator")

                            self.is_packet_allow_or_deny = YLeaf(YType.enumeration, "is-packet-allow-or-deny")

                            self.is_packet_maximum_length = YLeaf(YType.uint32, "is-packet-maximum-length")

                            self.is_packet_minimum_length = YLeaf(YType.uint32, "is-packet-minimum-length")

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
                                            "acl_name",
                                            "hits",
                                            "is_ace_sequence_number",
                                            "is_ace_type",
                                            "is_address_in_numbers",
                                            "is_address_mask_length",
                                            "is_comment_for_entry",
                                            "is_length_operator",
                                            "is_packet_allow_or_deny",
                                            "is_packet_maximum_length",
                                            "is_packet_minimum_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sequence_number.is_set or
                                self.acl_name.is_set or
                                self.hits.is_set or
                                self.is_ace_sequence_number.is_set or
                                self.is_ace_type.is_set or
                                self.is_address_in_numbers.is_set or
                                self.is_address_mask_length.is_set or
                                self.is_comment_for_entry.is_set or
                                self.is_length_operator.is_set or
                                self.is_packet_allow_or_deny.is_set or
                                self.is_packet_maximum_length.is_set or
                                self.is_packet_minimum_length.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sequence_number.yfilter != YFilter.not_set or
                                self.acl_name.yfilter != YFilter.not_set or
                                self.hits.yfilter != YFilter.not_set or
                                self.is_ace_sequence_number.yfilter != YFilter.not_set or
                                self.is_ace_type.yfilter != YFilter.not_set or
                                self.is_address_in_numbers.yfilter != YFilter.not_set or
                                self.is_address_mask_length.yfilter != YFilter.not_set or
                                self.is_comment_for_entry.yfilter != YFilter.not_set or
                                self.is_length_operator.yfilter != YFilter.not_set or
                                self.is_packet_allow_or_deny.yfilter != YFilter.not_set or
                                self.is_packet_maximum_length.yfilter != YFilter.not_set or
                                self.is_packet_minimum_length.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prefix-list-sequence" + "[sequence-number='" + self.sequence_number.get() + "']" + path_buffer

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
                            if (self.acl_name.is_set or self.acl_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_name.get_name_leafdata())
                            if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hits.get_name_leafdata())
                            if (self.is_ace_sequence_number.is_set or self.is_ace_sequence_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ace_sequence_number.get_name_leafdata())
                            if (self.is_ace_type.is_set or self.is_ace_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ace_type.get_name_leafdata())
                            if (self.is_address_in_numbers.is_set or self.is_address_in_numbers.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_address_in_numbers.get_name_leafdata())
                            if (self.is_address_mask_length.is_set or self.is_address_mask_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_address_mask_length.get_name_leafdata())
                            if (self.is_comment_for_entry.is_set or self.is_comment_for_entry.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_comment_for_entry.get_name_leafdata())
                            if (self.is_length_operator.is_set or self.is_length_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_length_operator.get_name_leafdata())
                            if (self.is_packet_allow_or_deny.is_set or self.is_packet_allow_or_deny.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_allow_or_deny.get_name_leafdata())
                            if (self.is_packet_maximum_length.is_set or self.is_packet_maximum_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_maximum_length.get_name_leafdata())
                            if (self.is_packet_minimum_length.is_set or self.is_packet_minimum_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_minimum_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sequence-number" or name == "acl-name" or name == "hits" or name == "is-ace-sequence-number" or name == "is-ace-type" or name == "is-address-in-numbers" or name == "is-address-mask-length" or name == "is-comment-for-entry" or name == "is-length-operator" or name == "is-packet-allow-or-deny" or name == "is-packet-maximum-length" or name == "is-packet-minimum-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sequence-number"):
                                self.sequence_number = value
                                self.sequence_number.value_namespace = name_space
                                self.sequence_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-name"):
                                self.acl_name = value
                                self.acl_name.value_namespace = name_space
                                self.acl_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "hits"):
                                self.hits = value
                                self.hits.value_namespace = name_space
                                self.hits.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ace-sequence-number"):
                                self.is_ace_sequence_number = value
                                self.is_ace_sequence_number.value_namespace = name_space
                                self.is_ace_sequence_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ace-type"):
                                self.is_ace_type = value
                                self.is_ace_type.value_namespace = name_space
                                self.is_ace_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-address-in-numbers"):
                                self.is_address_in_numbers = value
                                self.is_address_in_numbers.value_namespace = name_space
                                self.is_address_in_numbers.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-address-mask-length"):
                                self.is_address_mask_length = value
                                self.is_address_mask_length.value_namespace = name_space
                                self.is_address_mask_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-comment-for-entry"):
                                self.is_comment_for_entry = value
                                self.is_comment_for_entry.value_namespace = name_space
                                self.is_comment_for_entry.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-length-operator"):
                                self.is_length_operator = value
                                self.is_length_operator.value_namespace = name_space
                                self.is_length_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-allow-or-deny"):
                                self.is_packet_allow_or_deny = value
                                self.is_packet_allow_or_deny.value_namespace = name_space
                                self.is_packet_allow_or_deny.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-maximum-length"):
                                self.is_packet_maximum_length = value
                                self.is_packet_maximum_length.value_namespace = name_space
                                self.is_packet_maximum_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-minimum-length"):
                                self.is_packet_minimum_length = value
                                self.is_packet_minimum_length.value_namespace = name_space
                                self.is_packet_minimum_length.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prefix_list_sequence:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prefix_list_sequence:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefix-list-sequences" + path_buffer

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

                        if (child_yang_name == "prefix-list-sequence"):
                            for c in self.prefix_list_sequence:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prefix_list_sequence.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix-list-sequence"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.prefix_list_name.is_set or
                        (self.prefix_list_sequences is not None and self.prefix_list_sequences.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix_list_name.yfilter != YFilter.not_set or
                        (self.prefix_list_sequences is not None and self.prefix_list_sequences.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix" + "[prefix-list-name='" + self.prefix_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/prefixes/%s" % self.get_segment_path()
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

                    if (child_yang_name == "prefix-list-sequences"):
                        if (self.prefix_list_sequences is None):
                            self.prefix_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences()
                            self.prefix_list_sequences.parent = self
                            self._children_name_map["prefix_list_sequences"] = "prefix-list-sequences"
                        return self.prefix_list_sequences

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix-list-sequences" or name == "prefix-list-name"):
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
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
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
                    c = Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix()
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


        class Usages(Entity):
            """
            Table of Usage statistics of ACLs at different
            nodes
            
            .. attribute:: usage
            
            	Usage statistics of an ACL at a node
            	**type**\: list of    :py:class:`Usage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Usages.Usage>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Usages, self).__init__()

                self.yang_name = "usages"
                self.yang_parent_name = "access-list-manager"

                self.usage = YList(self)

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
                            super(Ipv6AclAndPrefixList.AccessListManager.Usages, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.AccessListManager.Usages, self).__setattr__(name, value)


            class Usage(Entity):
                """
                Usage statistics of an ACL at a node
                
                .. attribute:: access_list_name
                
                	Name of the ACL
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: application_id
                
                	Application ID
                	**type**\:   :py:class:`AclUsageAppIdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes.AclUsageAppIdEnum>`
                
                .. attribute:: node_name
                
                	Node where ACL is applied
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: usage_details
                
                	Usage Statistics Details
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Usages.Usage, self).__init__()

                    self.yang_name = "usage"
                    self.yang_parent_name = "usages"

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.application_id = YLeaf(YType.enumeration, "application-id")

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.usage_details = YLeaf(YType.str, "usage-details")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "application_id",
                                    "node_name",
                                    "usage_details") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6AclAndPrefixList.AccessListManager.Usages.Usage, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.AccessListManager.Usages.Usage, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.application_id.is_set or
                        self.node_name.is_set or
                        self.usage_details.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.application_id.yfilter != YFilter.not_set or
                        self.node_name.yfilter != YFilter.not_set or
                        self.usage_details.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "usage" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/usages/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.application_id.is_set or self.application_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.application_id.get_name_leafdata())
                    if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_name.get_name_leafdata())
                    if (self.usage_details.is_set or self.usage_details.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.usage_details.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "application-id" or name == "node-name" or name == "usage-details"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "application-id"):
                        self.application_id = value
                        self.application_id.value_namespace = name_space
                        self.application_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "node-name"):
                        self.node_name = value
                        self.node_name.value_namespace = name_space
                        self.node_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "usage-details"):
                        self.usage_details = value
                        self.usage_details.value_namespace = name_space
                        self.usage_details.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.usage:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.usage:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "usages" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "usage"):
                    for c in self.usage:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ipv6AclAndPrefixList.AccessListManager.Usages.Usage()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.usage.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "usage"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Accesses(Entity):
            """
            ACL class displaying Usage and Entries
            
            .. attribute:: access
            
            	Name of the Access List
            	**type**\: list of    :py:class:`Access <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.AccessListManager.Accesses, self).__init__()

                self.yang_name = "accesses"
                self.yang_parent_name = "access-list-manager"

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
                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses, self).__setattr__(name, value)


            class Access(Entity):
                """
                Name of the Access List
                
                .. attribute:: access_list_name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: access_list_sequences
                
                	Table of all the sequence numbers per ACL
                	**type**\:   :py:class:`AccessListSequences <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences>`
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access, self).__init__()

                    self.yang_name = "access"
                    self.yang_parent_name = "accesses"

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.access_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                    self.access_list_sequences.parent = self
                    self._children_name_map["access_list_sequences"] = "access-list-sequences"
                    self._children_yang_names.add("access-list-sequences")

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
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access, self).__setattr__(name, value)


                class AccessListSequences(Entity):
                    """
                    Table of all the sequence numbers per ACL
                    
                    .. attribute:: access_list_sequence
                    
                    	Sequence number of an ACL entry
                    	**type**\: list of    :py:class:`AccessListSequence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence>`
                    
                    

                    """

                    _prefix = 'ipv6-acl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__init__()

                        self.yang_name = "access-list-sequences"
                        self.yang_parent_name = "access"

                        self.access_list_sequence = YList(self)

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
                                    super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences, self).__setattr__(name, value)


                    class AccessListSequence(Entity):
                        """
                        Sequence number of an ACL entry
                        
                        .. attribute:: sequence_number  <key>
                        
                        	ACL entry sequence number
                        	**type**\:  int
                        
                        	**range:** 1..2147483646
                        
                        .. attribute:: acl_name
                        
                        	ACL Name
                        	**type**\:  str
                        
                        .. attribute:: capture
                        
                        	Capture option, TRUE if enabled
                        	**type**\:  bool
                        
                        .. attribute:: counter_name
                        
                        	Counter name
                        	**type**\:  str
                        
                        .. attribute:: destination_mask
                        
                        	Destination Mask
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_port_group
                        
                        	Destination port object\-group
                        	**type**\:  str
                        
                        .. attribute:: destination_prefix_group
                        
                        	Destination prefix object\-group
                        	**type**\:  str
                        
                        .. attribute:: hits
                        
                        	hits
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: hw_next_hop_info
                        
                        	HW Next hop info
                        	**type**\:   :py:class:`HwNextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo>`
                        
                        .. attribute:: is_ace_sequence_number
                        
                        	ACLE sequence number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_ace_type
                        
                        	ACE type (acl, remark)
                        	**type**\:   :py:class:`AclAce1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAce1>`
                        
                        .. attribute:: is_comment_for_entry
                        
                        	IsCommentForEntry
                        	**type**\:  str
                        
                        .. attribute:: is_destination_address_in_numbers
                        
                        	IsDestinationAddressInNumbers
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_destination_address_prefix_length
                        
                        	IsDestinationAddressPrefixLength
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_destination_operator
                        
                        	eq, ne, lt, etc..
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_destination_port1
                        
                        	IsDestinationPort1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_destination_port2
                        
                        	IsDestinationPort2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_dscp_present
                        
                        	IsDSCPPresent
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_dscp_valu
                        
                        	IsDSCPValu
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_flow_id
                        
                        	IsFlowId
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_header_matches
                        
                        	Match if routing header is presant
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_icmp_message_off
                        
                        	Don't generate the icmp message
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_ipv6_protocol2_type
                        
                        	Protocol 2
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_ipv6_protocol_type
                        
                        	Protocol 1
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_log_option
                        
                        	IsLogOption
                        	**type**\:   :py:class:`AclLog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclLog>`
                        
                        .. attribute:: is_packet_allow_or_deny
                        
                        	Grant value permit/deny 
                        	**type**\:   :py:class:`AclAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclAction>`
                        
                        .. attribute:: is_packet_length_end
                        
                        	IsPacketLengthEnd
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_packet_length_operator
                        
                        	Match if routing header is presant
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_packet_length_start
                        
                        	IsPacketLengthStart
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_precedence_present
                        
                        	IsPrecedencePresent
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_precedence_value
                        
                        	range from 0 to 7
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_protocol_operator
                        
                        	Protocol operator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_source_address_in_numbers
                        
                        	IsSourceAddressInNumbers
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: is_source_address_prefix_length
                        
                        	IsSourceAddressPrefixLength
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_source_operator
                        
                        	eq, ne, lt, etc..
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_source_port1
                        
                        	IsSourcePort1
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_source_port2
                        
                        	IsSourcePort2
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_tcp_bits
                        
                        	IsTCPBits
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_tcp_bits_mask
                        
                        	IsTCPBitsMask
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_tcp_bits_operator
                        
                        	IsTCPBitsOperator
                        	**type**\:   :py:class:`AclTcpflagsOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclTcpflagsOperator>`
                        
                        .. attribute:: is_time_to_live_end
                        
                        	IsTimeToLiveEnd
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_time_to_live_operator
                        
                        	IsTimeToLiveOperator
                        	**type**\:   :py:class:`AclPortOperator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.AclPortOperator>`
                        
                        .. attribute:: is_time_to_live_start
                        
                        	IsTimeToLiveStart
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_info
                        
                        	Next hop info
                        	**type**\: list of    :py:class:`NextHopInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo>`
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:   :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNh>`
                        
                        .. attribute:: no_stats
                        
                        	no stats
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: qos_group
                        
                        	Set qos\-group
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: sequence_str
                        
                        	Sequence String
                        	**type**\:  str
                        
                        .. attribute:: source_mask
                        
                        	Source Mask
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_port_group
                        
                        	Source port object\-group
                        	**type**\:  str
                        
                        .. attribute:: source_prefix_group
                        
                        	Source prefix object\-group
                        	**type**\:  str
                        
                        .. attribute:: udf
                        
                        	UDF
                        	**type**\: list of    :py:class:`Udf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf>`
                        
                        .. attribute:: undetermined_transport
                        
                        	Undetermined transport option, TRUE if enabled
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv6-acl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__init__()

                            self.yang_name = "access-list-sequence"
                            self.yang_parent_name = "access-list-sequences"

                            self.sequence_number = YLeaf(YType.uint32, "sequence-number")

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.capture = YLeaf(YType.boolean, "capture")

                            self.counter_name = YLeaf(YType.str, "counter-name")

                            self.destination_mask = YLeaf(YType.str, "destination-mask")

                            self.destination_port_group = YLeaf(YType.str, "destination-port-group")

                            self.destination_prefix_group = YLeaf(YType.str, "destination-prefix-group")

                            self.hits = YLeaf(YType.uint64, "hits")

                            self.is_ace_sequence_number = YLeaf(YType.uint32, "is-ace-sequence-number")

                            self.is_ace_type = YLeaf(YType.enumeration, "is-ace-type")

                            self.is_comment_for_entry = YLeaf(YType.str, "is-comment-for-entry")

                            self.is_destination_address_in_numbers = YLeaf(YType.str, "is-destination-address-in-numbers")

                            self.is_destination_address_prefix_length = YLeaf(YType.uint32, "is-destination-address-prefix-length")

                            self.is_destination_operator = YLeaf(YType.enumeration, "is-destination-operator")

                            self.is_destination_port1 = YLeaf(YType.uint32, "is-destination-port1")

                            self.is_destination_port2 = YLeaf(YType.uint32, "is-destination-port2")

                            self.is_dscp_present = YLeaf(YType.int32, "is-dscp-present")

                            self.is_dscp_valu = YLeaf(YType.uint32, "is-dscp-valu")

                            self.is_flow_id = YLeaf(YType.uint32, "is-flow-id")

                            self.is_header_matches = YLeaf(YType.uint32, "is-header-matches")

                            self.is_icmp_message_off = YLeaf(YType.int32, "is-icmp-message-off")

                            self.is_ipv6_protocol2_type = YLeaf(YType.int32, "is-ipv6-protocol2-type")

                            self.is_ipv6_protocol_type = YLeaf(YType.int32, "is-ipv6-protocol-type")

                            self.is_log_option = YLeaf(YType.enumeration, "is-log-option")

                            self.is_packet_allow_or_deny = YLeaf(YType.enumeration, "is-packet-allow-or-deny")

                            self.is_packet_length_end = YLeaf(YType.uint32, "is-packet-length-end")

                            self.is_packet_length_operator = YLeaf(YType.enumeration, "is-packet-length-operator")

                            self.is_packet_length_start = YLeaf(YType.uint32, "is-packet-length-start")

                            self.is_precedence_present = YLeaf(YType.int32, "is-precedence-present")

                            self.is_precedence_value = YLeaf(YType.uint32, "is-precedence-value")

                            self.is_protocol_operator = YLeaf(YType.enumeration, "is-protocol-operator")

                            self.is_source_address_in_numbers = YLeaf(YType.str, "is-source-address-in-numbers")

                            self.is_source_address_prefix_length = YLeaf(YType.uint32, "is-source-address-prefix-length")

                            self.is_source_operator = YLeaf(YType.enumeration, "is-source-operator")

                            self.is_source_port1 = YLeaf(YType.uint32, "is-source-port1")

                            self.is_source_port2 = YLeaf(YType.uint32, "is-source-port2")

                            self.is_tcp_bits = YLeaf(YType.uint32, "is-tcp-bits")

                            self.is_tcp_bits_mask = YLeaf(YType.uint32, "is-tcp-bits-mask")

                            self.is_tcp_bits_operator = YLeaf(YType.enumeration, "is-tcp-bits-operator")

                            self.is_time_to_live_end = YLeaf(YType.uint32, "is-time-to-live-end")

                            self.is_time_to_live_operator = YLeaf(YType.enumeration, "is-time-to-live-operator")

                            self.is_time_to_live_start = YLeaf(YType.uint32, "is-time-to-live-start")

                            self.next_hop_type = YLeaf(YType.enumeration, "next-hop-type")

                            self.no_stats = YLeaf(YType.int32, "no-stats")

                            self.qos_group = YLeaf(YType.uint16, "qos-group")

                            self.sequence_str = YLeaf(YType.str, "sequence-str")

                            self.source_mask = YLeaf(YType.str, "source-mask")

                            self.source_port_group = YLeaf(YType.str, "source-port-group")

                            self.source_prefix_group = YLeaf(YType.str, "source-prefix-group")

                            self.undetermined_transport = YLeaf(YType.boolean, "undetermined-transport")

                            self.hw_next_hop_info = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                            self.hw_next_hop_info.parent = self
                            self._children_name_map["hw_next_hop_info"] = "hw-next-hop-info"
                            self._children_yang_names.add("hw-next-hop-info")

                            self.next_hop_info = YList(self)
                            self.udf = YList(self)

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
                                            "acl_name",
                                            "capture",
                                            "counter_name",
                                            "destination_mask",
                                            "destination_port_group",
                                            "destination_prefix_group",
                                            "hits",
                                            "is_ace_sequence_number",
                                            "is_ace_type",
                                            "is_comment_for_entry",
                                            "is_destination_address_in_numbers",
                                            "is_destination_address_prefix_length",
                                            "is_destination_operator",
                                            "is_destination_port1",
                                            "is_destination_port2",
                                            "is_dscp_present",
                                            "is_dscp_valu",
                                            "is_flow_id",
                                            "is_header_matches",
                                            "is_icmp_message_off",
                                            "is_ipv6_protocol2_type",
                                            "is_ipv6_protocol_type",
                                            "is_log_option",
                                            "is_packet_allow_or_deny",
                                            "is_packet_length_end",
                                            "is_packet_length_operator",
                                            "is_packet_length_start",
                                            "is_precedence_present",
                                            "is_precedence_value",
                                            "is_protocol_operator",
                                            "is_source_address_in_numbers",
                                            "is_source_address_prefix_length",
                                            "is_source_operator",
                                            "is_source_port1",
                                            "is_source_port2",
                                            "is_tcp_bits",
                                            "is_tcp_bits_mask",
                                            "is_tcp_bits_operator",
                                            "is_time_to_live_end",
                                            "is_time_to_live_operator",
                                            "is_time_to_live_start",
                                            "next_hop_type",
                                            "no_stats",
                                            "qos_group",
                                            "sequence_str",
                                            "source_mask",
                                            "source_port_group",
                                            "source_prefix_group",
                                            "undetermined_transport") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence, self).__setattr__(name, value)


                        class HwNextHopInfo(Entity):
                            """
                            HW Next hop info
                            
                            .. attribute:: next_hop
                            
                            	The Next Hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: table_id
                            
                            	Table ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	The next\-hop type
                            	**type**\:   :py:class:`BagAclNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNh>`
                            
                            .. attribute:: vrf_name
                            
                            	Vrf Name
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__init__()

                                self.yang_name = "hw-next-hop-info"
                                self.yang_parent_name = "access-list-sequence"

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.table_id = YLeaf(YType.uint32, "table-id")

                                self.type = YLeaf(YType.enumeration, "type")

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
                                                "table_id",
                                                "type",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.next_hop.is_set or
                                    self.table_id.is_set or
                                    self.type.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.table_id.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "hw-next-hop-info" + path_buffer

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
                                if (self.table_id.is_set or self.table_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.table_id.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())
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
                                if(name == "next-hop" or name == "table-id" or name == "type" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
                                if(value_path == "table-id"):
                                    self.table_id = value
                                    self.table_id.value_namespace = name_space
                                    self.table_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class NextHopInfo(Entity):
                            """
                            Next hop info
                            
                            .. attribute:: acl_nh_exist
                            
                            	The nexthop exist
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: at_status
                            
                            	The next hop at status
                            	**type**\:   :py:class:`BagAclNhAtStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhAtStatus>`
                            
                            .. attribute:: next_hop
                            
                            	The next hop
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: status
                            
                            	The next hop status
                            	**type**\:   :py:class:`BagAclNhStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.BagAclNhStatus>`
                            
                            .. attribute:: track_name
                            
                            	Track name
                            	**type**\:  str
                            
                            	**length:** 0..33
                            
                            .. attribute:: vrf_name
                            
                            	Vrf Name
                            	**type**\:  str
                            
                            	**length:** 0..32
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__init__()

                                self.yang_name = "next-hop-info"
                                self.yang_parent_name = "access-list-sequence"

                                self.acl_nh_exist = YLeaf(YType.int32, "acl-nh-exist")

                                self.at_status = YLeaf(YType.enumeration, "at-status")

                                self.next_hop = YLeaf(YType.str, "next-hop")

                                self.status = YLeaf(YType.enumeration, "status")

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
                                    if name in ("acl_nh_exist",
                                                "at_status",
                                                "next_hop",
                                                "status",
                                                "track_name",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.acl_nh_exist.is_set or
                                    self.at_status.is_set or
                                    self.next_hop.is_set or
                                    self.status.is_set or
                                    self.track_name.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.acl_nh_exist.yfilter != YFilter.not_set or
                                    self.at_status.yfilter != YFilter.not_set or
                                    self.next_hop.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.track_name.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "next-hop-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.acl_nh_exist.is_set or self.acl_nh_exist.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.acl_nh_exist.get_name_leafdata())
                                if (self.at_status.is_set or self.at_status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.at_status.get_name_leafdata())
                                if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
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
                                if(name == "acl-nh-exist" or name == "at-status" or name == "next-hop" or name == "status" or name == "track-name" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "acl-nh-exist"):
                                    self.acl_nh_exist = value
                                    self.acl_nh_exist.value_namespace = name_space
                                    self.acl_nh_exist.value_namespace_prefix = name_space_prefix
                                if(value_path == "at-status"):
                                    self.at_status = value
                                    self.at_status.value_namespace = name_space
                                    self.at_status.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-hop"):
                                    self.next_hop = value
                                    self.next_hop.value_namespace = name_space
                                    self.next_hop.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "track-name"):
                                    self.track_name = value
                                    self.track_name.value_namespace = name_space
                                    self.track_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class Udf(Entity):
                            """
                            UDF
                            
                            .. attribute:: udf_mask
                            
                            	UDF Mask
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: udf_name
                            
                            	UDF Name
                            	**type**\:  str
                            
                            	**length:** 0..17
                            
                            .. attribute:: udf_value
                            
                            	UDF Value
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv6-acl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__init__()

                                self.yang_name = "udf"
                                self.yang_parent_name = "access-list-sequence"

                                self.udf_mask = YLeaf(YType.uint32, "udf-mask")

                                self.udf_name = YLeaf(YType.str, "udf-name")

                                self.udf_value = YLeaf(YType.uint32, "udf-value")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("udf_mask",
                                                "udf_name",
                                                "udf_value") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.udf_mask.is_set or
                                    self.udf_name.is_set or
                                    self.udf_value.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.udf_mask.yfilter != YFilter.not_set or
                                    self.udf_name.yfilter != YFilter.not_set or
                                    self.udf_value.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "udf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.udf_mask.is_set or self.udf_mask.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.udf_mask.get_name_leafdata())
                                if (self.udf_name.is_set or self.udf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.udf_name.get_name_leafdata())
                                if (self.udf_value.is_set or self.udf_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.udf_value.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "udf-mask" or name == "udf-name" or name == "udf-value"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "udf-mask"):
                                    self.udf_mask = value
                                    self.udf_mask.value_namespace = name_space
                                    self.udf_mask.value_namespace_prefix = name_space_prefix
                                if(value_path == "udf-name"):
                                    self.udf_name = value
                                    self.udf_name.value_namespace = name_space
                                    self.udf_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "udf-value"):
                                    self.udf_value = value
                                    self.udf_value.value_namespace = name_space
                                    self.udf_value.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.next_hop_info:
                                if (c.has_data()):
                                    return True
                            for c in self.udf:
                                if (c.has_data()):
                                    return True
                            return (
                                self.sequence_number.is_set or
                                self.acl_name.is_set or
                                self.capture.is_set or
                                self.counter_name.is_set or
                                self.destination_mask.is_set or
                                self.destination_port_group.is_set or
                                self.destination_prefix_group.is_set or
                                self.hits.is_set or
                                self.is_ace_sequence_number.is_set or
                                self.is_ace_type.is_set or
                                self.is_comment_for_entry.is_set or
                                self.is_destination_address_in_numbers.is_set or
                                self.is_destination_address_prefix_length.is_set or
                                self.is_destination_operator.is_set or
                                self.is_destination_port1.is_set or
                                self.is_destination_port2.is_set or
                                self.is_dscp_present.is_set or
                                self.is_dscp_valu.is_set or
                                self.is_flow_id.is_set or
                                self.is_header_matches.is_set or
                                self.is_icmp_message_off.is_set or
                                self.is_ipv6_protocol2_type.is_set or
                                self.is_ipv6_protocol_type.is_set or
                                self.is_log_option.is_set or
                                self.is_packet_allow_or_deny.is_set or
                                self.is_packet_length_end.is_set or
                                self.is_packet_length_operator.is_set or
                                self.is_packet_length_start.is_set or
                                self.is_precedence_present.is_set or
                                self.is_precedence_value.is_set or
                                self.is_protocol_operator.is_set or
                                self.is_source_address_in_numbers.is_set or
                                self.is_source_address_prefix_length.is_set or
                                self.is_source_operator.is_set or
                                self.is_source_port1.is_set or
                                self.is_source_port2.is_set or
                                self.is_tcp_bits.is_set or
                                self.is_tcp_bits_mask.is_set or
                                self.is_tcp_bits_operator.is_set or
                                self.is_time_to_live_end.is_set or
                                self.is_time_to_live_operator.is_set or
                                self.is_time_to_live_start.is_set or
                                self.next_hop_type.is_set or
                                self.no_stats.is_set or
                                self.qos_group.is_set or
                                self.sequence_str.is_set or
                                self.source_mask.is_set or
                                self.source_port_group.is_set or
                                self.source_prefix_group.is_set or
                                self.undetermined_transport.is_set or
                                (self.hw_next_hop_info is not None and self.hw_next_hop_info.has_data()))

                        def has_operation(self):
                            for c in self.next_hop_info:
                                if (c.has_operation()):
                                    return True
                            for c in self.udf:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sequence_number.yfilter != YFilter.not_set or
                                self.acl_name.yfilter != YFilter.not_set or
                                self.capture.yfilter != YFilter.not_set or
                                self.counter_name.yfilter != YFilter.not_set or
                                self.destination_mask.yfilter != YFilter.not_set or
                                self.destination_port_group.yfilter != YFilter.not_set or
                                self.destination_prefix_group.yfilter != YFilter.not_set or
                                self.hits.yfilter != YFilter.not_set or
                                self.is_ace_sequence_number.yfilter != YFilter.not_set or
                                self.is_ace_type.yfilter != YFilter.not_set or
                                self.is_comment_for_entry.yfilter != YFilter.not_set or
                                self.is_destination_address_in_numbers.yfilter != YFilter.not_set or
                                self.is_destination_address_prefix_length.yfilter != YFilter.not_set or
                                self.is_destination_operator.yfilter != YFilter.not_set or
                                self.is_destination_port1.yfilter != YFilter.not_set or
                                self.is_destination_port2.yfilter != YFilter.not_set or
                                self.is_dscp_present.yfilter != YFilter.not_set or
                                self.is_dscp_valu.yfilter != YFilter.not_set or
                                self.is_flow_id.yfilter != YFilter.not_set or
                                self.is_header_matches.yfilter != YFilter.not_set or
                                self.is_icmp_message_off.yfilter != YFilter.not_set or
                                self.is_ipv6_protocol2_type.yfilter != YFilter.not_set or
                                self.is_ipv6_protocol_type.yfilter != YFilter.not_set or
                                self.is_log_option.yfilter != YFilter.not_set or
                                self.is_packet_allow_or_deny.yfilter != YFilter.not_set or
                                self.is_packet_length_end.yfilter != YFilter.not_set or
                                self.is_packet_length_operator.yfilter != YFilter.not_set or
                                self.is_packet_length_start.yfilter != YFilter.not_set or
                                self.is_precedence_present.yfilter != YFilter.not_set or
                                self.is_precedence_value.yfilter != YFilter.not_set or
                                self.is_protocol_operator.yfilter != YFilter.not_set or
                                self.is_source_address_in_numbers.yfilter != YFilter.not_set or
                                self.is_source_address_prefix_length.yfilter != YFilter.not_set or
                                self.is_source_operator.yfilter != YFilter.not_set or
                                self.is_source_port1.yfilter != YFilter.not_set or
                                self.is_source_port2.yfilter != YFilter.not_set or
                                self.is_tcp_bits.yfilter != YFilter.not_set or
                                self.is_tcp_bits_mask.yfilter != YFilter.not_set or
                                self.is_tcp_bits_operator.yfilter != YFilter.not_set or
                                self.is_time_to_live_end.yfilter != YFilter.not_set or
                                self.is_time_to_live_operator.yfilter != YFilter.not_set or
                                self.is_time_to_live_start.yfilter != YFilter.not_set or
                                self.next_hop_type.yfilter != YFilter.not_set or
                                self.no_stats.yfilter != YFilter.not_set or
                                self.qos_group.yfilter != YFilter.not_set or
                                self.sequence_str.yfilter != YFilter.not_set or
                                self.source_mask.yfilter != YFilter.not_set or
                                self.source_port_group.yfilter != YFilter.not_set or
                                self.source_prefix_group.yfilter != YFilter.not_set or
                                self.undetermined_transport.yfilter != YFilter.not_set or
                                (self.hw_next_hop_info is not None and self.hw_next_hop_info.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "access-list-sequence" + "[sequence-number='" + self.sequence_number.get() + "']" + path_buffer

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
                            if (self.acl_name.is_set or self.acl_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.acl_name.get_name_leafdata())
                            if (self.capture.is_set or self.capture.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.capture.get_name_leafdata())
                            if (self.counter_name.is_set or self.counter_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.counter_name.get_name_leafdata())
                            if (self.destination_mask.is_set or self.destination_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_mask.get_name_leafdata())
                            if (self.destination_port_group.is_set or self.destination_port_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port_group.get_name_leafdata())
                            if (self.destination_prefix_group.is_set or self.destination_prefix_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_prefix_group.get_name_leafdata())
                            if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hits.get_name_leafdata())
                            if (self.is_ace_sequence_number.is_set or self.is_ace_sequence_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ace_sequence_number.get_name_leafdata())
                            if (self.is_ace_type.is_set or self.is_ace_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ace_type.get_name_leafdata())
                            if (self.is_comment_for_entry.is_set or self.is_comment_for_entry.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_comment_for_entry.get_name_leafdata())
                            if (self.is_destination_address_in_numbers.is_set or self.is_destination_address_in_numbers.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_destination_address_in_numbers.get_name_leafdata())
                            if (self.is_destination_address_prefix_length.is_set or self.is_destination_address_prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_destination_address_prefix_length.get_name_leafdata())
                            if (self.is_destination_operator.is_set or self.is_destination_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_destination_operator.get_name_leafdata())
                            if (self.is_destination_port1.is_set or self.is_destination_port1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_destination_port1.get_name_leafdata())
                            if (self.is_destination_port2.is_set or self.is_destination_port2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_destination_port2.get_name_leafdata())
                            if (self.is_dscp_present.is_set or self.is_dscp_present.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_dscp_present.get_name_leafdata())
                            if (self.is_dscp_valu.is_set or self.is_dscp_valu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_dscp_valu.get_name_leafdata())
                            if (self.is_flow_id.is_set or self.is_flow_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_flow_id.get_name_leafdata())
                            if (self.is_header_matches.is_set or self.is_header_matches.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_header_matches.get_name_leafdata())
                            if (self.is_icmp_message_off.is_set or self.is_icmp_message_off.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_icmp_message_off.get_name_leafdata())
                            if (self.is_ipv6_protocol2_type.is_set or self.is_ipv6_protocol2_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ipv6_protocol2_type.get_name_leafdata())
                            if (self.is_ipv6_protocol_type.is_set or self.is_ipv6_protocol_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_ipv6_protocol_type.get_name_leafdata())
                            if (self.is_log_option.is_set or self.is_log_option.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_log_option.get_name_leafdata())
                            if (self.is_packet_allow_or_deny.is_set or self.is_packet_allow_or_deny.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_allow_or_deny.get_name_leafdata())
                            if (self.is_packet_length_end.is_set or self.is_packet_length_end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_length_end.get_name_leafdata())
                            if (self.is_packet_length_operator.is_set or self.is_packet_length_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_length_operator.get_name_leafdata())
                            if (self.is_packet_length_start.is_set or self.is_packet_length_start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_packet_length_start.get_name_leafdata())
                            if (self.is_precedence_present.is_set or self.is_precedence_present.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_precedence_present.get_name_leafdata())
                            if (self.is_precedence_value.is_set or self.is_precedence_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_precedence_value.get_name_leafdata())
                            if (self.is_protocol_operator.is_set or self.is_protocol_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_protocol_operator.get_name_leafdata())
                            if (self.is_source_address_in_numbers.is_set or self.is_source_address_in_numbers.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_source_address_in_numbers.get_name_leafdata())
                            if (self.is_source_address_prefix_length.is_set or self.is_source_address_prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_source_address_prefix_length.get_name_leafdata())
                            if (self.is_source_operator.is_set or self.is_source_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_source_operator.get_name_leafdata())
                            if (self.is_source_port1.is_set or self.is_source_port1.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_source_port1.get_name_leafdata())
                            if (self.is_source_port2.is_set or self.is_source_port2.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_source_port2.get_name_leafdata())
                            if (self.is_tcp_bits.is_set or self.is_tcp_bits.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_tcp_bits.get_name_leafdata())
                            if (self.is_tcp_bits_mask.is_set or self.is_tcp_bits_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_tcp_bits_mask.get_name_leafdata())
                            if (self.is_tcp_bits_operator.is_set or self.is_tcp_bits_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_tcp_bits_operator.get_name_leafdata())
                            if (self.is_time_to_live_end.is_set or self.is_time_to_live_end.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_time_to_live_end.get_name_leafdata())
                            if (self.is_time_to_live_operator.is_set or self.is_time_to_live_operator.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_time_to_live_operator.get_name_leafdata())
                            if (self.is_time_to_live_start.is_set or self.is_time_to_live_start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_time_to_live_start.get_name_leafdata())
                            if (self.next_hop_type.is_set or self.next_hop_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_type.get_name_leafdata())
                            if (self.no_stats.is_set or self.no_stats.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_stats.get_name_leafdata())
                            if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.qos_group.get_name_leafdata())
                            if (self.sequence_str.is_set or self.sequence_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sequence_str.get_name_leafdata())
                            if (self.source_mask.is_set or self.source_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_mask.get_name_leafdata())
                            if (self.source_port_group.is_set or self.source_port_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_port_group.get_name_leafdata())
                            if (self.source_prefix_group.is_set or self.source_prefix_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_prefix_group.get_name_leafdata())
                            if (self.undetermined_transport.is_set or self.undetermined_transport.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.undetermined_transport.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "hw-next-hop-info"):
                                if (self.hw_next_hop_info is None):
                                    self.hw_next_hop_info = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo()
                                    self.hw_next_hop_info.parent = self
                                    self._children_name_map["hw_next_hop_info"] = "hw-next-hop-info"
                                return self.hw_next_hop_info

                            if (child_yang_name == "next-hop-info"):
                                for c in self.next_hop_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.next_hop_info.append(c)
                                return c

                            if (child_yang_name == "udf"):
                                for c in self.udf:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.udf.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hw-next-hop-info" or name == "next-hop-info" or name == "udf" or name == "sequence-number" or name == "acl-name" or name == "capture" or name == "counter-name" or name == "destination-mask" or name == "destination-port-group" or name == "destination-prefix-group" or name == "hits" or name == "is-ace-sequence-number" or name == "is-ace-type" or name == "is-comment-for-entry" or name == "is-destination-address-in-numbers" or name == "is-destination-address-prefix-length" or name == "is-destination-operator" or name == "is-destination-port1" or name == "is-destination-port2" or name == "is-dscp-present" or name == "is-dscp-valu" or name == "is-flow-id" or name == "is-header-matches" or name == "is-icmp-message-off" or name == "is-ipv6-protocol2-type" or name == "is-ipv6-protocol-type" or name == "is-log-option" or name == "is-packet-allow-or-deny" or name == "is-packet-length-end" or name == "is-packet-length-operator" or name == "is-packet-length-start" or name == "is-precedence-present" or name == "is-precedence-value" or name == "is-protocol-operator" or name == "is-source-address-in-numbers" or name == "is-source-address-prefix-length" or name == "is-source-operator" or name == "is-source-port1" or name == "is-source-port2" or name == "is-tcp-bits" or name == "is-tcp-bits-mask" or name == "is-tcp-bits-operator" or name == "is-time-to-live-end" or name == "is-time-to-live-operator" or name == "is-time-to-live-start" or name == "next-hop-type" or name == "no-stats" or name == "qos-group" or name == "sequence-str" or name == "source-mask" or name == "source-port-group" or name == "source-prefix-group" or name == "undetermined-transport"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sequence-number"):
                                self.sequence_number = value
                                self.sequence_number.value_namespace = name_space
                                self.sequence_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "acl-name"):
                                self.acl_name = value
                                self.acl_name.value_namespace = name_space
                                self.acl_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "capture"):
                                self.capture = value
                                self.capture.value_namespace = name_space
                                self.capture.value_namespace_prefix = name_space_prefix
                            if(value_path == "counter-name"):
                                self.counter_name = value
                                self.counter_name.value_namespace = name_space
                                self.counter_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-mask"):
                                self.destination_mask = value
                                self.destination_mask.value_namespace = name_space
                                self.destination_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port-group"):
                                self.destination_port_group = value
                                self.destination_port_group.value_namespace = name_space
                                self.destination_port_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-prefix-group"):
                                self.destination_prefix_group = value
                                self.destination_prefix_group.value_namespace = name_space
                                self.destination_prefix_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "hits"):
                                self.hits = value
                                self.hits.value_namespace = name_space
                                self.hits.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ace-sequence-number"):
                                self.is_ace_sequence_number = value
                                self.is_ace_sequence_number.value_namespace = name_space
                                self.is_ace_sequence_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ace-type"):
                                self.is_ace_type = value
                                self.is_ace_type.value_namespace = name_space
                                self.is_ace_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-comment-for-entry"):
                                self.is_comment_for_entry = value
                                self.is_comment_for_entry.value_namespace = name_space
                                self.is_comment_for_entry.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-destination-address-in-numbers"):
                                self.is_destination_address_in_numbers = value
                                self.is_destination_address_in_numbers.value_namespace = name_space
                                self.is_destination_address_in_numbers.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-destination-address-prefix-length"):
                                self.is_destination_address_prefix_length = value
                                self.is_destination_address_prefix_length.value_namespace = name_space
                                self.is_destination_address_prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-destination-operator"):
                                self.is_destination_operator = value
                                self.is_destination_operator.value_namespace = name_space
                                self.is_destination_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-destination-port1"):
                                self.is_destination_port1 = value
                                self.is_destination_port1.value_namespace = name_space
                                self.is_destination_port1.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-destination-port2"):
                                self.is_destination_port2 = value
                                self.is_destination_port2.value_namespace = name_space
                                self.is_destination_port2.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-dscp-present"):
                                self.is_dscp_present = value
                                self.is_dscp_present.value_namespace = name_space
                                self.is_dscp_present.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-dscp-valu"):
                                self.is_dscp_valu = value
                                self.is_dscp_valu.value_namespace = name_space
                                self.is_dscp_valu.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-flow-id"):
                                self.is_flow_id = value
                                self.is_flow_id.value_namespace = name_space
                                self.is_flow_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-header-matches"):
                                self.is_header_matches = value
                                self.is_header_matches.value_namespace = name_space
                                self.is_header_matches.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-icmp-message-off"):
                                self.is_icmp_message_off = value
                                self.is_icmp_message_off.value_namespace = name_space
                                self.is_icmp_message_off.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ipv6-protocol2-type"):
                                self.is_ipv6_protocol2_type = value
                                self.is_ipv6_protocol2_type.value_namespace = name_space
                                self.is_ipv6_protocol2_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-ipv6-protocol-type"):
                                self.is_ipv6_protocol_type = value
                                self.is_ipv6_protocol_type.value_namespace = name_space
                                self.is_ipv6_protocol_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-log-option"):
                                self.is_log_option = value
                                self.is_log_option.value_namespace = name_space
                                self.is_log_option.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-allow-or-deny"):
                                self.is_packet_allow_or_deny = value
                                self.is_packet_allow_or_deny.value_namespace = name_space
                                self.is_packet_allow_or_deny.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-length-end"):
                                self.is_packet_length_end = value
                                self.is_packet_length_end.value_namespace = name_space
                                self.is_packet_length_end.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-length-operator"):
                                self.is_packet_length_operator = value
                                self.is_packet_length_operator.value_namespace = name_space
                                self.is_packet_length_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-packet-length-start"):
                                self.is_packet_length_start = value
                                self.is_packet_length_start.value_namespace = name_space
                                self.is_packet_length_start.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-precedence-present"):
                                self.is_precedence_present = value
                                self.is_precedence_present.value_namespace = name_space
                                self.is_precedence_present.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-precedence-value"):
                                self.is_precedence_value = value
                                self.is_precedence_value.value_namespace = name_space
                                self.is_precedence_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-protocol-operator"):
                                self.is_protocol_operator = value
                                self.is_protocol_operator.value_namespace = name_space
                                self.is_protocol_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-source-address-in-numbers"):
                                self.is_source_address_in_numbers = value
                                self.is_source_address_in_numbers.value_namespace = name_space
                                self.is_source_address_in_numbers.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-source-address-prefix-length"):
                                self.is_source_address_prefix_length = value
                                self.is_source_address_prefix_length.value_namespace = name_space
                                self.is_source_address_prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-source-operator"):
                                self.is_source_operator = value
                                self.is_source_operator.value_namespace = name_space
                                self.is_source_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-source-port1"):
                                self.is_source_port1 = value
                                self.is_source_port1.value_namespace = name_space
                                self.is_source_port1.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-source-port2"):
                                self.is_source_port2 = value
                                self.is_source_port2.value_namespace = name_space
                                self.is_source_port2.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-tcp-bits"):
                                self.is_tcp_bits = value
                                self.is_tcp_bits.value_namespace = name_space
                                self.is_tcp_bits.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-tcp-bits-mask"):
                                self.is_tcp_bits_mask = value
                                self.is_tcp_bits_mask.value_namespace = name_space
                                self.is_tcp_bits_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-tcp-bits-operator"):
                                self.is_tcp_bits_operator = value
                                self.is_tcp_bits_operator.value_namespace = name_space
                                self.is_tcp_bits_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-time-to-live-end"):
                                self.is_time_to_live_end = value
                                self.is_time_to_live_end.value_namespace = name_space
                                self.is_time_to_live_end.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-time-to-live-operator"):
                                self.is_time_to_live_operator = value
                                self.is_time_to_live_operator.value_namespace = name_space
                                self.is_time_to_live_operator.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-time-to-live-start"):
                                self.is_time_to_live_start = value
                                self.is_time_to_live_start.value_namespace = name_space
                                self.is_time_to_live_start.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-type"):
                                self.next_hop_type = value
                                self.next_hop_type.value_namespace = name_space
                                self.next_hop_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-stats"):
                                self.no_stats = value
                                self.no_stats.value_namespace = name_space
                                self.no_stats.value_namespace_prefix = name_space_prefix
                            if(value_path == "qos-group"):
                                self.qos_group = value
                                self.qos_group.value_namespace = name_space
                                self.qos_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "sequence-str"):
                                self.sequence_str = value
                                self.sequence_str.value_namespace = name_space
                                self.sequence_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-mask"):
                                self.source_mask = value
                                self.source_mask.value_namespace = name_space
                                self.source_mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-port-group"):
                                self.source_port_group = value
                                self.source_port_group.value_namespace = name_space
                                self.source_port_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-prefix-group"):
                                self.source_prefix_group = value
                                self.source_prefix_group.value_namespace = name_space
                                self.source_prefix_group.value_namespace_prefix = name_space_prefix
                            if(value_path == "undetermined-transport"):
                                self.undetermined_transport = value
                                self.undetermined_transport.value_namespace = name_space
                                self.undetermined_transport.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.access_list_sequence:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.access_list_sequence:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-list-sequences" + path_buffer

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

                        if (child_yang_name == "access-list-sequence"):
                            for c in self.access_list_sequence:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.access_list_sequence.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-sequence"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        (self.access_list_sequences is not None and self.access_list_sequences.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        (self.access_list_sequences is not None and self.access_list_sequences.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "access" + "[access-list-name='" + self.access_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/accesses/%s" % self.get_segment_path()
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

                    if (child_yang_name == "access-list-sequences"):
                        if (self.access_list_sequences is None):
                            self.access_list_sequences = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences()
                            self.access_list_sequences.parent = self
                            self._children_name_map["access_list_sequences"] = "access-list-sequences"
                        return self.access_list_sequences

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-sequences" or name == "access-list-name"):
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
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/access-list-manager/%s" % self.get_segment_path()
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
                    c = Ipv6AclAndPrefixList.AccessListManager.Accesses.Access()
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
            return (
                (self.accesses is not None and self.accesses.has_data()) or
                (self.prefixes is not None and self.prefixes.has_data()) or
                (self.usages is not None and self.usages.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.accesses is not None and self.accesses.has_operation()) or
                (self.prefixes is not None and self.prefixes.has_operation()) or
                (self.usages is not None and self.usages.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "access-list-manager" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "accesses"):
                if (self.accesses is None):
                    self.accesses = Ipv6AclAndPrefixList.AccessListManager.Accesses()
                    self.accesses.parent = self
                    self._children_name_map["accesses"] = "accesses"
                return self.accesses

            if (child_yang_name == "prefixes"):
                if (self.prefixes is None):
                    self.prefixes = Ipv6AclAndPrefixList.AccessListManager.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                return self.prefixes

            if (child_yang_name == "usages"):
                if (self.usages is None):
                    self.usages = Ipv6AclAndPrefixList.AccessListManager.Usages()
                    self.usages.parent = self
                    self._children_name_map["usages"] = "usages"
                return self.usages

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "accesses" or name == "prefixes" or name == "usages"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Oor(Entity):
        """
        Out Of Resources, Limits to the resources
        allocatable
        
        .. attribute:: access_list_summary
        
        	Resource Limits pertaining to ACLs only
        	**type**\:   :py:class:`AccessListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.AccessListSummary>`
        
        .. attribute:: details
        
        	Details of the overall out of resource limit
        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.Details>`
        
        .. attribute:: oor_accesses
        
        	Resource occupation details for ACLs
        	**type**\:   :py:class:`OorAccesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorAccesses>`
        
        .. attribute:: oor_prefixes
        
        	Resource occupation details for prefix lists
        	**type**\:   :py:class:`OorPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorPrefixes>`
        
        .. attribute:: prefix_list_summary
        
        	Summary of the prefix Lists resource utilization
        	**type**\:   :py:class:`PrefixListSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.PrefixListSummary>`
        
        

        """

        _prefix = 'ipv6-acl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6AclAndPrefixList.Oor, self).__init__()

            self.yang_name = "oor"
            self.yang_parent_name = "ipv6-acl-and-prefix-list"

            self.access_list_summary = Ipv6AclAndPrefixList.Oor.AccessListSummary()
            self.access_list_summary.parent = self
            self._children_name_map["access_list_summary"] = "access-list-summary"
            self._children_yang_names.add("access-list-summary")

            self.details = Ipv6AclAndPrefixList.Oor.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")

            self.oor_accesses = Ipv6AclAndPrefixList.Oor.OorAccesses()
            self.oor_accesses.parent = self
            self._children_name_map["oor_accesses"] = "oor-accesses"
            self._children_yang_names.add("oor-accesses")

            self.oor_prefixes = Ipv6AclAndPrefixList.Oor.OorPrefixes()
            self.oor_prefixes.parent = self
            self._children_name_map["oor_prefixes"] = "oor-prefixes"
            self._children_yang_names.add("oor-prefixes")

            self.prefix_list_summary = Ipv6AclAndPrefixList.Oor.PrefixListSummary()
            self.prefix_list_summary.parent = self
            self._children_name_map["prefix_list_summary"] = "prefix-list-summary"
            self._children_yang_names.add("prefix-list-summary")


        class Details(Entity):
            """
            Details of the overall out of resource limit
            
            .. attribute:: is_current_configured_ac_ls
            
            	Current configured acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_configured_aces
            
            	Current configured aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_maximum_configurable_aces
            
            	Current max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_current_maximum_configurable_acls
            
            	Current max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_default_maximum_configurable_ac_es
            
            	default max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_default_maximum_configurable_ac_ls
            
            	default max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_maximum_configurable_ac_es
            
            	max configurable aces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_maximum_configurable_ac_ls
            
            	max configurable acls
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "oor"

                self.is_current_configured_ac_ls = YLeaf(YType.uint32, "is-current-configured-ac-ls")

                self.is_current_configured_aces = YLeaf(YType.uint32, "is-current-configured-aces")

                self.is_current_maximum_configurable_aces = YLeaf(YType.uint32, "is-current-maximum-configurable-aces")

                self.is_current_maximum_configurable_acls = YLeaf(YType.uint32, "is-current-maximum-configurable-acls")

                self.is_default_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-es")

                self.is_default_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-ls")

                self.is_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-maximum-configurable-ac-es")

                self.is_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-maximum-configurable-ac-ls")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("is_current_configured_ac_ls",
                                "is_current_configured_aces",
                                "is_current_maximum_configurable_aces",
                                "is_current_maximum_configurable_acls",
                                "is_default_maximum_configurable_ac_es",
                                "is_default_maximum_configurable_ac_ls",
                                "is_maximum_configurable_ac_es",
                                "is_maximum_configurable_ac_ls") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv6AclAndPrefixList.Oor.Details, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.Oor.Details, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.is_current_configured_ac_ls.is_set or
                    self.is_current_configured_aces.is_set or
                    self.is_current_maximum_configurable_aces.is_set or
                    self.is_current_maximum_configurable_acls.is_set or
                    self.is_default_maximum_configurable_ac_es.is_set or
                    self.is_default_maximum_configurable_ac_ls.is_set or
                    self.is_maximum_configurable_ac_es.is_set or
                    self.is_maximum_configurable_ac_ls.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.is_current_configured_ac_ls.yfilter != YFilter.not_set or
                    self.is_current_configured_aces.yfilter != YFilter.not_set or
                    self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set or
                    self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set or
                    self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                    self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set or
                    self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                    self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.is_current_configured_ac_ls.is_set or self.is_current_configured_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_current_configured_ac_ls.get_name_leafdata())
                if (self.is_current_configured_aces.is_set or self.is_current_configured_aces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_current_configured_aces.get_name_leafdata())
                if (self.is_current_maximum_configurable_aces.is_set or self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_current_maximum_configurable_aces.get_name_leafdata())
                if (self.is_current_maximum_configurable_acls.is_set or self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_current_maximum_configurable_acls.get_name_leafdata())
                if (self.is_default_maximum_configurable_ac_es.is_set or self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_default_maximum_configurable_ac_es.get_name_leafdata())
                if (self.is_default_maximum_configurable_ac_ls.is_set or self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_default_maximum_configurable_ac_ls.get_name_leafdata())
                if (self.is_maximum_configurable_ac_es.is_set or self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_maximum_configurable_ac_es.get_name_leafdata())
                if (self.is_maximum_configurable_ac_ls.is_set or self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_maximum_configurable_ac_ls.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "is-current-configured-ac-ls" or name == "is-current-configured-aces" or name == "is-current-maximum-configurable-aces" or name == "is-current-maximum-configurable-acls" or name == "is-default-maximum-configurable-ac-es" or name == "is-default-maximum-configurable-ac-ls" or name == "is-maximum-configurable-ac-es" or name == "is-maximum-configurable-ac-ls"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "is-current-configured-ac-ls"):
                    self.is_current_configured_ac_ls = value
                    self.is_current_configured_ac_ls.value_namespace = name_space
                    self.is_current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                if(value_path == "is-current-configured-aces"):
                    self.is_current_configured_aces = value
                    self.is_current_configured_aces.value_namespace = name_space
                    self.is_current_configured_aces.value_namespace_prefix = name_space_prefix
                if(value_path == "is-current-maximum-configurable-aces"):
                    self.is_current_maximum_configurable_aces = value
                    self.is_current_maximum_configurable_aces.value_namespace = name_space
                    self.is_current_maximum_configurable_aces.value_namespace_prefix = name_space_prefix
                if(value_path == "is-current-maximum-configurable-acls"):
                    self.is_current_maximum_configurable_acls = value
                    self.is_current_maximum_configurable_acls.value_namespace = name_space
                    self.is_current_maximum_configurable_acls.value_namespace_prefix = name_space_prefix
                if(value_path == "is-default-maximum-configurable-ac-es"):
                    self.is_default_maximum_configurable_ac_es = value
                    self.is_default_maximum_configurable_ac_es.value_namespace = name_space
                    self.is_default_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "is-default-maximum-configurable-ac-ls"):
                    self.is_default_maximum_configurable_ac_ls = value
                    self.is_default_maximum_configurable_ac_ls.value_namespace = name_space
                    self.is_default_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                if(value_path == "is-maximum-configurable-ac-es"):
                    self.is_maximum_configurable_ac_es = value
                    self.is_maximum_configurable_ac_es.value_namespace = name_space
                    self.is_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                if(value_path == "is-maximum-configurable-ac-ls"):
                    self.is_maximum_configurable_ac_ls = value
                    self.is_maximum_configurable_ac_ls.value_namespace = name_space
                    self.is_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix


        class PrefixListSummary(Entity):
            """
            Summary of the prefix Lists resource
            utilization
            
            .. attribute:: details
            
            	Summary Detail of the prefix list Resource Utilisation
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.PrefixListSummary, self).__init__()

                self.yang_name = "prefix-list-summary"
                self.yang_parent_name = "oor"

                self.details = Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._children_yang_names.add("details")


            class Details(Entity):
                """
                Summary Detail of the prefix list Resource
                Utilisation
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "prefix-list-summary"

                    self.is_current_configured_ac_ls = YLeaf(YType.uint32, "is-current-configured-ac-ls")

                    self.is_current_configured_aces = YLeaf(YType.uint32, "is-current-configured-aces")

                    self.is_current_maximum_configurable_aces = YLeaf(YType.uint32, "is-current-maximum-configurable-aces")

                    self.is_current_maximum_configurable_acls = YLeaf(YType.uint32, "is-current-maximum-configurable-acls")

                    self.is_default_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-es")

                    self.is_default_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-ls")

                    self.is_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-maximum-configurable-ac-es")

                    self.is_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-maximum-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_current_configured_ac_ls",
                                    "is_current_configured_aces",
                                    "is_current_maximum_configurable_aces",
                                    "is_current_maximum_configurable_acls",
                                    "is_default_maximum_configurable_ac_es",
                                    "is_default_maximum_configurable_ac_ls",
                                    "is_maximum_configurable_ac_es",
                                    "is_maximum_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.is_current_configured_ac_ls.is_set or
                        self.is_current_configured_aces.is_set or
                        self.is_current_maximum_configurable_aces.is_set or
                        self.is_current_maximum_configurable_acls.is_set or
                        self.is_default_maximum_configurable_ac_es.is_set or
                        self.is_default_maximum_configurable_ac_ls.is_set or
                        self.is_maximum_configurable_ac_es.is_set or
                        self.is_maximum_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.is_current_configured_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "details" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/prefix-list-summary/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_current_configured_ac_ls.is_set or self.is_current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_ac_ls.get_name_leafdata())
                    if (self.is_current_configured_aces.is_set or self.is_current_configured_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_aces.is_set or self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_acls.is_set or self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_acls.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_es.is_set or self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_ls.is_set or self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_ls.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_es.is_set or self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_ls.is_set or self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "is-current-configured-ac-ls" or name == "is-current-configured-aces" or name == "is-current-maximum-configurable-aces" or name == "is-current-maximum-configurable-acls" or name == "is-default-maximum-configurable-ac-es" or name == "is-default-maximum-configurable-ac-ls" or name == "is-maximum-configurable-ac-es" or name == "is-maximum-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-current-configured-ac-ls"):
                        self.is_current_configured_ac_ls = value
                        self.is_current_configured_ac_ls.value_namespace = name_space
                        self.is_current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-aces"):
                        self.is_current_configured_aces = value
                        self.is_current_configured_aces.value_namespace = name_space
                        self.is_current_configured_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-aces"):
                        self.is_current_maximum_configurable_aces = value
                        self.is_current_maximum_configurable_aces.value_namespace = name_space
                        self.is_current_maximum_configurable_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-acls"):
                        self.is_current_maximum_configurable_acls = value
                        self.is_current_maximum_configurable_acls.value_namespace = name_space
                        self.is_current_maximum_configurable_acls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-es"):
                        self.is_default_maximum_configurable_ac_es = value
                        self.is_default_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-ls"):
                        self.is_default_maximum_configurable_ac_ls = value
                        self.is_default_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-es"):
                        self.is_maximum_configurable_ac_es = value
                        self.is_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-ls"):
                        self.is_maximum_configurable_ac_ls = value
                        self.is_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.details is not None and self.details.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.details is not None and self.details.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "prefix-list-summary" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "details"):
                    if (self.details is None):
                        self.details = Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details()
                        self.details.parent = self
                        self._children_name_map["details"] = "details"
                    return self.details

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "details"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class OorAccesses(Entity):
            """
            Resource occupation details for ACLs
            
            .. attribute:: oor_access
            
            	Resource occupation details for a particular ACL
            	**type**\: list of    :py:class:`OorAccess <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.OorAccesses, self).__init__()

                self.yang_name = "oor-accesses"
                self.yang_parent_name = "oor"

                self.oor_access = YList(self)

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
                            super(Ipv6AclAndPrefixList.Oor.OorAccesses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.Oor.OorAccesses, self).__setattr__(name, value)


            class OorAccess(Entity):
                """
                Resource occupation details for a particular
                ACL
                
                .. attribute:: access_list_name  <key>
                
                	Name of the Access List
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__init__()

                    self.yang_name = "oor-access"
                    self.yang_parent_name = "oor-accesses"

                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                    self.is_current_configured_ac_ls = YLeaf(YType.uint32, "is-current-configured-ac-ls")

                    self.is_current_configured_aces = YLeaf(YType.uint32, "is-current-configured-aces")

                    self.is_current_maximum_configurable_aces = YLeaf(YType.uint32, "is-current-maximum-configurable-aces")

                    self.is_current_maximum_configurable_acls = YLeaf(YType.uint32, "is-current-maximum-configurable-acls")

                    self.is_default_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-es")

                    self.is_default_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-ls")

                    self.is_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-maximum-configurable-ac-es")

                    self.is_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-maximum-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("access_list_name",
                                    "is_current_configured_ac_ls",
                                    "is_current_configured_aces",
                                    "is_current_maximum_configurable_aces",
                                    "is_current_maximum_configurable_acls",
                                    "is_default_maximum_configurable_ac_es",
                                    "is_default_maximum_configurable_ac_ls",
                                    "is_maximum_configurable_ac_es",
                                    "is_maximum_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.access_list_name.is_set or
                        self.is_current_configured_ac_ls.is_set or
                        self.is_current_configured_aces.is_set or
                        self.is_current_maximum_configurable_aces.is_set or
                        self.is_current_maximum_configurable_acls.is_set or
                        self.is_default_maximum_configurable_ac_es.is_set or
                        self.is_default_maximum_configurable_ac_ls.is_set or
                        self.is_maximum_configurable_ac_es.is_set or
                        self.is_maximum_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.access_list_name.yfilter != YFilter.not_set or
                        self.is_current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.is_current_configured_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oor-access" + "[access-list-name='" + self.access_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/oor-accesses/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_list_name.get_name_leafdata())
                    if (self.is_current_configured_ac_ls.is_set or self.is_current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_ac_ls.get_name_leafdata())
                    if (self.is_current_configured_aces.is_set or self.is_current_configured_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_aces.is_set or self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_acls.is_set or self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_acls.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_es.is_set or self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_ls.is_set or self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_ls.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_es.is_set or self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_ls.is_set or self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "access-list-name" or name == "is-current-configured-ac-ls" or name == "is-current-configured-aces" or name == "is-current-maximum-configurable-aces" or name == "is-current-maximum-configurable-acls" or name == "is-default-maximum-configurable-ac-es" or name == "is-default-maximum-configurable-ac-ls" or name == "is-maximum-configurable-ac-es" or name == "is-maximum-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "access-list-name"):
                        self.access_list_name = value
                        self.access_list_name.value_namespace = name_space
                        self.access_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-ac-ls"):
                        self.is_current_configured_ac_ls = value
                        self.is_current_configured_ac_ls.value_namespace = name_space
                        self.is_current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-aces"):
                        self.is_current_configured_aces = value
                        self.is_current_configured_aces.value_namespace = name_space
                        self.is_current_configured_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-aces"):
                        self.is_current_maximum_configurable_aces = value
                        self.is_current_maximum_configurable_aces.value_namespace = name_space
                        self.is_current_maximum_configurable_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-acls"):
                        self.is_current_maximum_configurable_acls = value
                        self.is_current_maximum_configurable_acls.value_namespace = name_space
                        self.is_current_maximum_configurable_acls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-es"):
                        self.is_default_maximum_configurable_ac_es = value
                        self.is_default_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-ls"):
                        self.is_default_maximum_configurable_ac_ls = value
                        self.is_default_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-es"):
                        self.is_maximum_configurable_ac_es = value
                        self.is_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-ls"):
                        self.is_maximum_configurable_ac_ls = value
                        self.is_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.oor_access:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.oor_access:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "oor-accesses" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "oor-access"):
                    for c in self.oor_access:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.oor_access.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "oor-access"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class OorPrefixes(Entity):
            """
            Resource occupation details for prefix lists
            
            .. attribute:: oor_prefix
            
            	Resource occupation details for a particular prefix list
            	**type**\: list of    :py:class:`OorPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.OorPrefixes, self).__init__()

                self.yang_name = "oor-prefixes"
                self.yang_parent_name = "oor"

                self.oor_prefix = YList(self)

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
                            super(Ipv6AclAndPrefixList.Oor.OorPrefixes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6AclAndPrefixList.Oor.OorPrefixes, self).__setattr__(name, value)


            class OorPrefix(Entity):
                """
                Resource occupation details for a particular
                prefix list
                
                .. attribute:: prefix_list_name  <key>
                
                	Name of a prefix list
                	**type**\:  str
                
                	**length:** 1..65
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__init__()

                    self.yang_name = "oor-prefix"
                    self.yang_parent_name = "oor-prefixes"

                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                    self.is_current_configured_ac_ls = YLeaf(YType.uint32, "is-current-configured-ac-ls")

                    self.is_current_configured_aces = YLeaf(YType.uint32, "is-current-configured-aces")

                    self.is_current_maximum_configurable_aces = YLeaf(YType.uint32, "is-current-maximum-configurable-aces")

                    self.is_current_maximum_configurable_acls = YLeaf(YType.uint32, "is-current-maximum-configurable-acls")

                    self.is_default_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-es")

                    self.is_default_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-ls")

                    self.is_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-maximum-configurable-ac-es")

                    self.is_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-maximum-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prefix_list_name",
                                    "is_current_configured_ac_ls",
                                    "is_current_configured_aces",
                                    "is_current_maximum_configurable_aces",
                                    "is_current_maximum_configurable_acls",
                                    "is_default_maximum_configurable_ac_es",
                                    "is_default_maximum_configurable_ac_ls",
                                    "is_maximum_configurable_ac_es",
                                    "is_maximum_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.prefix_list_name.is_set or
                        self.is_current_configured_ac_ls.is_set or
                        self.is_current_configured_aces.is_set or
                        self.is_current_maximum_configurable_aces.is_set or
                        self.is_current_maximum_configurable_acls.is_set or
                        self.is_default_maximum_configurable_ac_es.is_set or
                        self.is_default_maximum_configurable_ac_ls.is_set or
                        self.is_maximum_configurable_ac_es.is_set or
                        self.is_maximum_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix_list_name.yfilter != YFilter.not_set or
                        self.is_current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.is_current_configured_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oor-prefix" + "[prefix-list-name='" + self.prefix_list_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/oor-prefixes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix_list_name.is_set or self.prefix_list_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_list_name.get_name_leafdata())
                    if (self.is_current_configured_ac_ls.is_set or self.is_current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_ac_ls.get_name_leafdata())
                    if (self.is_current_configured_aces.is_set or self.is_current_configured_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_aces.is_set or self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_acls.is_set or self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_acls.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_es.is_set or self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_ls.is_set or self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_ls.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_es.is_set or self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_ls.is_set or self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix-list-name" or name == "is-current-configured-ac-ls" or name == "is-current-configured-aces" or name == "is-current-maximum-configurable-aces" or name == "is-current-maximum-configurable-acls" or name == "is-default-maximum-configurable-ac-es" or name == "is-default-maximum-configurable-ac-ls" or name == "is-maximum-configurable-ac-es" or name == "is-maximum-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix-list-name"):
                        self.prefix_list_name = value
                        self.prefix_list_name.value_namespace = name_space
                        self.prefix_list_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-ac-ls"):
                        self.is_current_configured_ac_ls = value
                        self.is_current_configured_ac_ls.value_namespace = name_space
                        self.is_current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-aces"):
                        self.is_current_configured_aces = value
                        self.is_current_configured_aces.value_namespace = name_space
                        self.is_current_configured_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-aces"):
                        self.is_current_maximum_configurable_aces = value
                        self.is_current_maximum_configurable_aces.value_namespace = name_space
                        self.is_current_maximum_configurable_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-acls"):
                        self.is_current_maximum_configurable_acls = value
                        self.is_current_maximum_configurable_acls.value_namespace = name_space
                        self.is_current_maximum_configurable_acls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-es"):
                        self.is_default_maximum_configurable_ac_es = value
                        self.is_default_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-ls"):
                        self.is_default_maximum_configurable_ac_ls = value
                        self.is_default_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-es"):
                        self.is_maximum_configurable_ac_es = value
                        self.is_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-ls"):
                        self.is_maximum_configurable_ac_ls = value
                        self.is_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.oor_prefix:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.oor_prefix:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "oor-prefixes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "oor-prefix"):
                    for c in self.oor_prefix:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.oor_prefix.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "oor-prefix"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AccessListSummary(Entity):
            """
            Resource Limits pertaining to ACLs only
            
            .. attribute:: details
            
            	Details containing the resource limits of the ACLs
            	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper.Ipv6AclAndPrefixList.Oor.AccessListSummary.Details>`
            
            

            """

            _prefix = 'ipv6-acl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6AclAndPrefixList.Oor.AccessListSummary, self).__init__()

                self.yang_name = "access-list-summary"
                self.yang_parent_name = "oor"

                self.details = Ipv6AclAndPrefixList.Oor.AccessListSummary.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._children_yang_names.add("details")


            class Details(Entity):
                """
                Details containing the resource limits of the
                ACLs
                
                .. attribute:: is_current_configured_ac_ls
                
                	Current configured acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_configured_aces
                
                	Current configured aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_aces
                
                	Current max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_current_maximum_configurable_acls
                
                	Current max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_es
                
                	default max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_default_maximum_configurable_ac_ls
                
                	default max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_es
                
                	max configurable aces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_configurable_ac_ls
                
                	max configurable acls
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv6-acl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv6AclAndPrefixList.Oor.AccessListSummary.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "access-list-summary"

                    self.is_current_configured_ac_ls = YLeaf(YType.uint32, "is-current-configured-ac-ls")

                    self.is_current_configured_aces = YLeaf(YType.uint32, "is-current-configured-aces")

                    self.is_current_maximum_configurable_aces = YLeaf(YType.uint32, "is-current-maximum-configurable-aces")

                    self.is_current_maximum_configurable_acls = YLeaf(YType.uint32, "is-current-maximum-configurable-acls")

                    self.is_default_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-es")

                    self.is_default_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-default-maximum-configurable-ac-ls")

                    self.is_maximum_configurable_ac_es = YLeaf(YType.uint32, "is-maximum-configurable-ac-es")

                    self.is_maximum_configurable_ac_ls = YLeaf(YType.uint32, "is-maximum-configurable-ac-ls")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_current_configured_ac_ls",
                                    "is_current_configured_aces",
                                    "is_current_maximum_configurable_aces",
                                    "is_current_maximum_configurable_acls",
                                    "is_default_maximum_configurable_ac_es",
                                    "is_default_maximum_configurable_ac_ls",
                                    "is_maximum_configurable_ac_es",
                                    "is_maximum_configurable_ac_ls") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv6AclAndPrefixList.Oor.AccessListSummary.Details, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv6AclAndPrefixList.Oor.AccessListSummary.Details, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.is_current_configured_ac_ls.is_set or
                        self.is_current_configured_aces.is_set or
                        self.is_current_maximum_configurable_aces.is_set or
                        self.is_current_maximum_configurable_acls.is_set or
                        self.is_default_maximum_configurable_ac_es.is_set or
                        self.is_default_maximum_configurable_ac_ls.is_set or
                        self.is_maximum_configurable_ac_es.is_set or
                        self.is_maximum_configurable_ac_ls.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_current_configured_ac_ls.yfilter != YFilter.not_set or
                        self.is_current_configured_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set or
                        self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set or
                        self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "details" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/access-list-summary/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_current_configured_ac_ls.is_set or self.is_current_configured_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_ac_ls.get_name_leafdata())
                    if (self.is_current_configured_aces.is_set or self.is_current_configured_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_configured_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_aces.is_set or self.is_current_maximum_configurable_aces.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_aces.get_name_leafdata())
                    if (self.is_current_maximum_configurable_acls.is_set or self.is_current_maximum_configurable_acls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_current_maximum_configurable_acls.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_es.is_set or self.is_default_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_default_maximum_configurable_ac_ls.is_set or self.is_default_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_default_maximum_configurable_ac_ls.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_es.is_set or self.is_maximum_configurable_ac_es.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_es.get_name_leafdata())
                    if (self.is_maximum_configurable_ac_ls.is_set or self.is_maximum_configurable_ac_ls.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_configurable_ac_ls.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "is-current-configured-ac-ls" or name == "is-current-configured-aces" or name == "is-current-maximum-configurable-aces" or name == "is-current-maximum-configurable-acls" or name == "is-default-maximum-configurable-ac-es" or name == "is-default-maximum-configurable-ac-ls" or name == "is-maximum-configurable-ac-es" or name == "is-maximum-configurable-ac-ls"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-current-configured-ac-ls"):
                        self.is_current_configured_ac_ls = value
                        self.is_current_configured_ac_ls.value_namespace = name_space
                        self.is_current_configured_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-configured-aces"):
                        self.is_current_configured_aces = value
                        self.is_current_configured_aces.value_namespace = name_space
                        self.is_current_configured_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-aces"):
                        self.is_current_maximum_configurable_aces = value
                        self.is_current_maximum_configurable_aces.value_namespace = name_space
                        self.is_current_maximum_configurable_aces.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-current-maximum-configurable-acls"):
                        self.is_current_maximum_configurable_acls = value
                        self.is_current_maximum_configurable_acls.value_namespace = name_space
                        self.is_current_maximum_configurable_acls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-es"):
                        self.is_default_maximum_configurable_ac_es = value
                        self.is_default_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-default-maximum-configurable-ac-ls"):
                        self.is_default_maximum_configurable_ac_ls = value
                        self.is_default_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_default_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-es"):
                        self.is_maximum_configurable_ac_es = value
                        self.is_maximum_configurable_ac_es.value_namespace = name_space
                        self.is_maximum_configurable_ac_es.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-configurable-ac-ls"):
                        self.is_maximum_configurable_ac_ls = value
                        self.is_maximum_configurable_ac_ls.value_namespace = name_space
                        self.is_maximum_configurable_ac_ls.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.details is not None and self.details.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.details is not None and self.details.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "access-list-summary" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/oor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "details"):
                    if (self.details is None):
                        self.details = Ipv6AclAndPrefixList.Oor.AccessListSummary.Details()
                        self.details.parent = self
                        self._children_name_map["details"] = "details"
                    return self.details

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "details"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.access_list_summary is not None and self.access_list_summary.has_data()) or
                (self.details is not None and self.details.has_data()) or
                (self.oor_accesses is not None and self.oor_accesses.has_data()) or
                (self.oor_prefixes is not None and self.oor_prefixes.has_data()) or
                (self.prefix_list_summary is not None and self.prefix_list_summary.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.access_list_summary is not None and self.access_list_summary.has_operation()) or
                (self.details is not None and self.details.has_operation()) or
                (self.oor_accesses is not None and self.oor_accesses.has_operation()) or
                (self.oor_prefixes is not None and self.oor_prefixes.has_operation()) or
                (self.prefix_list_summary is not None and self.prefix_list_summary.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "oor" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "access-list-summary"):
                if (self.access_list_summary is None):
                    self.access_list_summary = Ipv6AclAndPrefixList.Oor.AccessListSummary()
                    self.access_list_summary.parent = self
                    self._children_name_map["access_list_summary"] = "access-list-summary"
                return self.access_list_summary

            if (child_yang_name == "details"):
                if (self.details is None):
                    self.details = Ipv6AclAndPrefixList.Oor.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                return self.details

            if (child_yang_name == "oor-accesses"):
                if (self.oor_accesses is None):
                    self.oor_accesses = Ipv6AclAndPrefixList.Oor.OorAccesses()
                    self.oor_accesses.parent = self
                    self._children_name_map["oor_accesses"] = "oor-accesses"
                return self.oor_accesses

            if (child_yang_name == "oor-prefixes"):
                if (self.oor_prefixes is None):
                    self.oor_prefixes = Ipv6AclAndPrefixList.Oor.OorPrefixes()
                    self.oor_prefixes.parent = self
                    self._children_name_map["oor_prefixes"] = "oor-prefixes"
                return self.oor_prefixes

            if (child_yang_name == "prefix-list-summary"):
                if (self.prefix_list_summary is None):
                    self.prefix_list_summary = Ipv6AclAndPrefixList.Oor.PrefixListSummary()
                    self.prefix_list_summary.parent = self
                    self._children_name_map["prefix_list_summary"] = "prefix-list-summary"
                return self.prefix_list_summary

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "access-list-summary" or name == "details" or name == "oor-accesses" or name == "oor-prefixes" or name == "prefix-list-summary"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.access_list_manager is not None and self.access_list_manager.has_data()) or
            (self.oor is not None and self.oor.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.access_list_manager is not None and self.access_list_manager.has_operation()) or
            (self.oor is not None and self.oor.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-acl-oper:ipv6-acl-and-prefix-list" + path_buffer

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

        if (child_yang_name == "access-list-manager"):
            if (self.access_list_manager is None):
                self.access_list_manager = Ipv6AclAndPrefixList.AccessListManager()
                self.access_list_manager.parent = self
                self._children_name_map["access_list_manager"] = "access-list-manager"
            return self.access_list_manager

        if (child_yang_name == "oor"):
            if (self.oor is None):
                self.oor = Ipv6AclAndPrefixList.Oor()
                self.oor.parent = self
                self._children_name_map["oor"] = "oor"
            return self.oor

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "access-list-manager" or name == "oor"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ipv6AclAndPrefixList()
        return self._top_entity

